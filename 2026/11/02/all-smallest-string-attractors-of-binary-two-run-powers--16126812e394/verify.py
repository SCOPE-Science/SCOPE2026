#!/usr/bin/env python3
"""Independent finite checks of two-run-power string attractor classification.

Usage: python3 verify.py
Only standard Python is required. Positions in the theorem are 1-based.
"""
from collections import Counter
from itertools import combinations


def all_substring_masks(word):
    """Mask of every position covered by at least one occurrence of each factor."""
    masks = {}
    for i in range(len(word)):
        mask = 0
        for j in range(i, len(word)):
            mask |= 1 << j
            key = word[i:j + 1]
            masks[key] = masks.get(key, 0) | mask
    return masks


def predicted(a, b, k):
    p = a + b
    # 0 positions are one-indexed (i-1)*p+1 through (i-1)*p+a.
    # 1 positions are one-indexed (i-1)*p+a+1 through i*p.
    last0 = [(i-1)*p+a for i in range(1, k+1)]
    last1_int = [i*p for i in range(1, k)]
    first0_int = [(i-1)*p+1 for i in range(2, k+1)]
    first1 = [(i-1)*p+a+1 for i in range(1, k+1)]
    zeros = [(i-1)*p+j for i in range(1, k+1) for j in range(1, a+1)]
    ones = [(i-1)*p+a+j for i in range(1, k+1) for j in range(1, b+1)]
    # 01 is crossed exactly at (last 0, first 1); 10 at
    # (last 1 of a nonterminal block, first 0 of a subsequent block).
    p01 = set(last0 + first1)
    p10 = set(last1_int + first0_int)
    return {tuple(sorted((x,y))) for x in zeros for y in ones
            if (x in p01 or y in p01) and (x in p10 or y in p10)}


def completely_independent_check(word, pair):
    """Literal direct occurrence test, with no precomputed coverage masks."""
    factors = {word[i:j] for i in range(len(word))
               for j in range(i + 1, len(word) + 1)}
    for sub in factors:
        ok = False
        for start in range(len(word) - len(sub) + 1):
            if word[start:start + len(sub)] == sub and any(
                 start + 1 <= x <= start + len(sub) for x in pair):
                ok = True
                break
        if not ok:
            return False
    return True


def run():
    tested_pairs = 0
    tested_cases = 0
    second_check_pairs = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for k in range(2, 6):
                word = ('0'*a + '1'*b)*k
                masks = tuple(all_substring_masks(word).values())
                actual = set()
                for i, j in combinations(range(1, len(word) + 1), 2):
                    seen = (1 << (i-1)) | (1 << (j-1))
                    if all(cov & seen for cov in masks):
                        actual.add((i,j))
                    tested_pairs += 1
                expected = predicted(a, b, k)
                assert actual == expected, (a,b,k, actual^expected)
                expected_count = ((k-1)*(max(a,b)*k+1)
                                  if min(a,b) == 1 else 2*k*(k-1))
                assert len(actual) == expected_count, (a,b,k,len(actual))
                if a >= 2 and b >= 2:
                    p = a+b
                    spectrum = Counter(abs(i-j) for i,j in actual)
                    formula = Counter()
                    for m in range(2-k, k):
                        c = k-1+m if m <= 0 else k-m
                        formula[abs(m*p-a)] += 2*c
                    assert spectrum == formula
                    assert min(spectrum) == min(a,b)
                    assert max(spectrum) == (k-1)*p-min(a,b)
                tested_cases += 1
    for a in range(1, 4):
        for b in range(1, 4):
            for k in range(2, 5):
                word = ('0'*a + '1'*b)*k
                exp = predicted(a,b,k)
                for pair in combinations(range(1, len(word)+1), 2):
                    assert completely_independent_check(word, pair) == (pair in exp), (a,b,k,pair)
                    second_check_pairs += 1
    print('VERIFY_OK parameter_cases=%d masked_pair_tests=%d direct_pair_tests=%d span_spectra=True'%(
           tested_cases,tested_pairs,second_check_pairs))

if __name__ == '__main__':
    run()
