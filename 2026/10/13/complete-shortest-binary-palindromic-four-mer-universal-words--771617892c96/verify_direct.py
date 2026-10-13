"""Independent exhaustive verification of shortest binary palindromic four-mer covers.
Run: python3 verify_direct.py
"""
from itertools import product

EXPECTED = (
    '000010110011110011010000',
    '000011001011110100110000',
    '000011010011110010110000',
    '111100101100001101001111',
    '111100110100001011001111',
    '111101001100001100101111',
)

def palindromes(length):
    for half in product('01', repeat=(length + 1)//2):
        prefix = ''.join(half)
        suffix = prefix[::-1] if length % 2 == 0 else prefix[-2::-1]
        yield prefix + suffix

def contains_all_kmers(word, k):
    seen = {word[i:i+k] for i in range(len(word)-k+1)}
    return len(seen) == (1 << k)

def run():
    counts = []
    for length in range(4, 25):
        covers = [word for word in palindromes(length) if contains_all_kmers(word, 4)]
        counts.append((length, len(covers)))
        if length < 24:
            assert not covers
        else:
            assert tuple(covers) == EXPECTED
    assert len(EXPECTED) == 6
    print('DIRECT_OK length=24 count=6 no shorter candidates; counts:', counts)

if __name__ == '__main__':
    run()
