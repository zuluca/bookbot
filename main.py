from collections import Counter

def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = ''.join(char for char in string if char.isalpha())
    return Counter(string)

#def report(character_count, link):
    
def bookbot(link):
    with open(link) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    
    character_count = count_characters(file_contents).most_common()
    #print(character_count)

    print(f"--- Begin report of {link} ---")
    print(f"{word_count} words found in the document", end="\n\n")

    for char,count in character_count:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def main():
    frankenstein = "books/frankenstein.txt"
    bookbot(frankenstein)

if __name__ == '__main__':
    main()

