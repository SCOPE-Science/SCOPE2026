#!/usr/bin/env python3
"""Exact finite checks for opposite binary-block minimal supersequences.

Usage: python verify.py
No external dependencies. The infinite-parameter theorem needs its written proof.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

SWAP = str.maketrans('01', '10')


def subsequence(pattern, word):
    pos = 0
    for symbol in word:
        if pos < len(pattern) and symbol == pattern[pos]:
            pos += 1
    return pos == len(pattern)


def minimal_common_supersequence(word, m):
    u = '0' * m + '1' * m
    v = '1' * m + '0' * m
    if not subsequence(u, word) or not subsequence(v, word):
        return False
    for k in range(len(word)):
        shorter = word[:k] + word[k + 1:]
        if subsequence(u, shorter) and subsequence(v, shorter):
            return False
    return True


def constructive_family(m):
    out = set()
    for j in range(m):
        # First arm ends with 0; second arm begins with 0.
        for left_ones in combinations(range(m + j - 1), j):
            left = ['0'] * (m + j)
            for k in left_ones:
                left[k] = '1'
            for right_ones in combinations(range(1, m + j), j):
                right = ['0'] * (m + j)
                for k in right_ones:
                    right[k] = '1'
                word = ''.join(left) + '1' * (m - j) + ''.join(right)
                out.add(word)
                out.add(word.translate(SWAP))
    return out


def all_binary_words(length):
    return (''.join(t) for t in product('01', repeat=length))


def structurally_eligible_words(m):
    # The analytical proof shows every minimal word has exactly 2m
    # occurrences of one symbol and between m and 2m-1 of the other.
    for length in range(3 * m, 4 * m):
        for n_zeros in {2 * m, length - 2 * m}:
            if n_zeros < m or n_zeros > 2 * m:
                continue
            if length - n_zeros < m or length - n_zeros > 2 * m:
                continue
            for positions in combinations(range(length), n_zeros):
                word = ['1'] * length
                for k in positions:
                    word[k] = '0'
                yield ''.join(word)


def main():
    for m in range(1, 6):
        family = constructive_family(m)
        predicted = {3 * m + j: 2 * comb(m + j - 1, j)**2 for j in range(m)}
        observed = dict(sorted(Counter(map(len, family)).items()))
        assert observed == predicted, (m, observed, predicted)
        assert all(minimal_common_supersequence(w, m) for w in family)
        if m <= 4:
            actual = {
                word for length in range(2 * m, 4 * m + 1)
                for word in all_binary_words(length)
                if minimal_common_supersequence(word, m)
            }
            assert actual == family, (m, len(actual), len(family))
            test = 'full_binary_exhaustion'
        else:
            actual = {
                word for word in structurally_eligible_words(m)
                if minimal_common_supersequence(word, m)
            }
            assert actual == family, (m, len(actual), len(family))
            test = 'full_structurally_eligible_exhaustion'
        print(f'm={m}; method={test}; counts={observed}; total={len(family)}; PASS')
    print('ALL CHECKS PASS')

if __name__ == '__main__':
    main()
