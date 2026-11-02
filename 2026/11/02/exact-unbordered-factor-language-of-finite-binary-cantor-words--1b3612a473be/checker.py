#!/usr/bin/env python3
"""Standalone exact finite checks for the Cantor-word unbordered-factor theorem.

Checks use a direct prefix-function implementation for borders, independent
of the 2-adic criterion in the proof. Run: python3 checker.py
"""
from collections import Counter

def cantor(level):
    word = '1'
    for rank in range(level):
        word = word + '0' * (3**rank) + word
    return word

def unbordered(word):
    # Proper borders are exactly nonzero prefix-function values at the end.
    pi = [0] * len(word)
    for i in range(1, len(word)):
        j = pi[i - 1]
        while j and word[i] != word[j]:
            j = pi[j - 1]
        if word[i] == word[j]:
            j += 1
        pi[i] = j
    return not pi[-1]

def predicted(level):
    oriented = set()
    for m in range(level):
        base = cantor(m)
        lower = 0 if m == 0 else 3**(m-1)
        upper = 3**m
        starts = [i for i, x in enumerate(base) if x == '1']
        for i in starts:
            for t in range(lower+1, upper+1):
                oriented.add(base[i:] + '0' * t)
    return {'0', '1'} | oriented | {w[::-1] for w in oriented}

def exhaustive(level):
    word = cantor(level)
    oriented = set()
    for i, c in enumerate(word):
        if c != '1':
            continue
        for j in range(i+2, len(word)+1):
            if word[j-1] == '0':
                factor = word[i:j]
                if factor not in oriented and unbordered(factor):
                    oriented.add(factor)
    return {'0', '1'} | oriented | {w[::-1] for w in oriented}

def main():
    for level in range(1, 7):
        actual = exhaustive(level)
        expect = predicted(level)
        value = (8 * 6 ** (level - 1) + 12) // 5
        assert actual == expect, (level, 'missing', sorted(expect-actual)[:5], 'extra', sorted(actual-expect)[:5])
        assert len(actual) == value
        assert max(map(len, actual)) == 2*3**(level-1)
        print(f'level={level} length={3**level} unbordered={len(actual)} predicted={value} exact_sets=yes')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
