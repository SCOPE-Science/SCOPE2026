#!/usr/bin/env python3
"""Independent exhaustive check of fixed-weight binary three-subsequence universality.

Uses direct subsequence matching rather than the arch-factor argument.
"""
from collections import Counter
from itertools import product
from math import comb

TRIPLES = tuple(''.join(t) for t in product('01', repeat=3))

def contains_scattered(word, target):
    i = 0
    for symbol in word:
        if symbol == target[i]:
            i += 1
            if i == len(target):
                return True
    return False

def is_three_universal(word):
    return all(contains_scattered(word, target) for target in TRIPLES)

def main():
    total = 0
    pairs = 0
    for n in range(0, 17):
        bad = Counter()
        count = Counter()
        for tpl in product('01', repeat=n):
            w = ''.join(tpl)
            k = w.count('1')
            count[k] += 1
            bad[k] += not is_three_universal(w)
            total += 1
        for k in range(n+1):
            assert count[k] == comb(n,k), (n,k,count[k])
            expected_bad = 3*(n-2) if min(k,n-k)>=3 else comb(n,k)
            assert bad[k] == expected_bad, (n,k,bad[k],expected_bad)
            pairs += 1
    print(f'PASS_FIXED_WEIGHT_3_UNIVERSAL n=0..16 words={total} parameter_pairs={pairs}')
if __name__ == '__main__':
    main()
