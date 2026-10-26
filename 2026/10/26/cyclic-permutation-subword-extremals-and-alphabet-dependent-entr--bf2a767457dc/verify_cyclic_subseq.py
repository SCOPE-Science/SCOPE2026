#!/usr/bin/env python3
"""Standalone finite checks for subsequence occurrences in repeated permutations.
Only Python's standard library is required."""
from collections import defaultdict
from math import comb


def cyclic_word(q, m):
    return tuple(range(q)) * m


def weak_descents(u):
    return sum(a >= b for a, b in zip(u, u[1:]))


def predicted(m, u):
    delta = weak_descents(u)
    return comb(m + len(u) - 1 - delta, len(u)) if m > delta else 0


def all_occurrences(word):
    counts = {(): 1}
    for c in word:
        new = counts.copy()
        for u, v in counts.items():
            new[u + (c,)] = new.get(u + (c,), 0) + v
        counts = new
    return counts


def formula_max(q, m):
    return max(comb(m + (q - 1) * r, q * r) for r in range(m + 1))


def recurrence_moment(q, top=36):
    a = [sum(comb(m + (q - 1) * r, q * r) for r in range(m + 1)) for m in range(top + 1)]
    # ((1-x)^q-x) A(x) = (1-x)^(q-1).
    for m in range(top + 1):
        left = sum((-1)**j * comb(q, j) * a[m-j] for j in range(min(m,q)+1))
        if m >= 1:
            left -= a[m-1]
        right = (-1)**m * comb(q-1,m) if m <= q-1 else 0
        assert left == right,(q,m,left,right)


def run():
    cases=0
    patterns=0
    maxima=0
    for q, lim in ((2, 8), (3, 5), (4, 4), (5, 3)):
        for m in range(1, lim+1):
            count = all_occurrences(cyclic_word(q,m))
            for u, actual in count.items():
                assert actual == predicted(m,u),(q,m,u,actual,predicted(m,u))
            expected = formula_max(q,m)
            leaders = {u for u, x in count.items() if x == expected}
            assert max(count.values()) == expected
            if m >= 2:
                expected_leaders = {cyclic_word(q,r) for r in range(m+1)
                                    if comb(m+(q-1)*r,q*r) == expected}
                assert leaders == expected_leaders,(q,m,leaders,expected_leaders)
            cases+=1
            patterns+=len(count)
            maxima+=len(leaders)
        recurrence_moment(q)
    for q in range(2,11):
        for m in range(2,41):
            vals=[comb(m+(q-1)*r,q*r) for r in range(m+1)]
            for j in range(1,m):
                assert vals[j]**2 > vals[j-1]*vals[j+1]
            winners=[j for j,v in enumerate(vals) if v==max(vals)]
            assert len(winners)<=2 and (len(winners)<2 or winners[1]==winners[0]+1)
    print('CYCLIC_PERM_SUBSEQUENCE_PASS', 'full_DP_cases='+str(cases),
          'tested_patterns='+str(patterns),'winning_patterns='+str(maxima),
          'GF_coefficients=0..36 q=2..5', 'strict_log_concavity=q2..10,m2..40')

if __name__ == '__main__':
    run()
