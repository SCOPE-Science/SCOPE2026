#!/usr/bin/env python3
"""Independent finite checks for the near-distinct Burrows-Wheeler run theorem.

No external dependencies; runs with Python >=3.9. The infinite theorem rests on a combinatorial counting argument, not this enumeration.
"""
from collections import Counter
from itertools import permutations
from math import factorial


def bwt(w):
    n = len(w)
    rotations = sorted((w[i:] + w[:i], i) for i in range(n))
    return tuple(w[(i - 1) % n] for _, i in rotations)


def runs(v):
    return 1 + sum(v[i] != v[i + 1] for i in range(len(v) - 1))


def single_cycle(v):
    offs = {}
    total = 0
    for c in sorted(set(v)):
        offs[c] = total
        total += v.count(c)
    used = Counter()
    pi = []
    for c in v:
        pi.append(offs[c] + used[c])
        used[c] += 1
    reached = set()
    j = 0
    while j not in reached:
        reached.add(j)
        j = pi[j]
    return j == 0 and len(reached) == len(v)


def check():
    for q in range(2, 8):
        n = q + 1
        for c in range(q):
            # Each necklace admits a unique lexicographically smallest rotation.
            necklaces = set()
            for w in set(permutations(tuple(range(q)) + (c,))):
                necklaces.add(min(w[i:] + w[:i] for i in range(n)))
            by_runs = Counter()
            for w in necklaces:
                L = bwt(w)
                assert single_cycle(L), (q, c, w, L)
                by_runs[runs(L)] += 1
            expected = {n - 1: factorial(q - 1)}
            if q > 2:
                expected[n] = factorial(q - 1) * (q - 2) // 2
            assert dict(by_runs) == expected, (q, c, dict(by_runs), expected)
            assert len(necklaces) == factorial(q) // 2
        print(f'q={q}: all {q} duplicated-letter cases verified')
    print('ALL NEAR-DISTINCT BWT CHECKS PASSED')


if __name__ == '__main__':
    check()
