#!/usr/bin/env python3
"""Reproduce finite checks for the Box-Diamond stabilization bound.

Public mathematical verifier; Python 3 standard library only.
Run: python3 checker.py
"""
from collections import Counter
from random import Random


def iterate(rows):
    """Independent bitmask evaluation of alpha_j=(box diamond)^j true."""
    n = len(rows)
    full = (1 << n) - 1
    masks = [full]
    while True:
        old = masks[-1]
        diamond = sum(1 << u for u, suc in enumerate(rows) if suc & old)
        new = sum(1 << v for v, suc in enumerate(rows) if suc & ~diamond == 0)
        if new == old:
            return masks
        assert new & ~old == 0
        masks.append(new)


def recursive_alpha(rows, v, depth):
    if depth == 0:
        return True
    return all(any(recursive_alpha(rows, z, depth - 1)
                   for z in range(len(rows)) if (rows[u] >> z) & 1)
               for u in range(len(rows)) if (rows[v] >> u) & 1)


def test(rows, direct=False):
    n = len(rows)
    full = (1 << n) - 1
    stages = iterate(rows)
    # Number of proper changes before equality (first stationary index).
    assert len(stages) - 1 <= n // 2
    T = [full ^ mask for mask in stages]
    U = [sum(1 << i for i, mask in enumerate(rows) if mask & ~t == 0)
         for t in T]
    for t in T:
        for u in U:
            assert t & u == 0, 'two-sided disjointness failure'
    if direct:
        for d in range(len(stages) + 2):
            truth = stages[min(d, len(stages)-1)]
            assert all(bool((truth >> v) & 1) == recursive_alpha(rows, v, d)
                       for v in range(n))
    return len(stages)-1


def main():
    counts = {}
    for n in range(1, 5):
        hist = Counter()
        lim = 1 << (n*n)
        for code in range(lim):
            rows = [(code >> (n*i)) & ((1 << n) - 1) for i in range(n)]
            hist[test(rows, direct=(n < 4 or code % 257 == 0))] += 1
        counts[n] = dict(sorted(hist.items()))
        assert sum(hist.values()) == lim
    assert counts == {1:{0:2}, 2:{0:12,1:4},
                      3:{0:374,1:138}, 4:{0:52056,1:12712,2:768}}
    # For arbitrarily long path examples, evaluate all levels by both methods.
    for n in range(1, 81):
        path = [(1 << (v+1)) if v < n-1 else 0 for v in range(n)]
        d = test(path, direct=(n <= 15))
        assert d == n//2
        for m in range(n//2):
            if n == 2*m+2:
                S = iterate(path)
                assert S[m] & 1 and not S[m+1] & 1
    # Reproducible samples above the full enumeration cutoff.
    random = Random(20261023)
    for n, trials in [(5,20000),(6,10000),(9,5000)]:
        for k in range(trials):
            rows = [random.getrandbits(n) for _ in range(n)]
            test(rows, direct=(k < 100))
    print('FULL_CENSUS', counts)
    print('PATH_SHARPNESS_N1_TO_80', 'OK')
    print('RANDOM_FRAMES_N5_6_9', 35000, 'OK')
    print('RECURSIVE_SEMANTICS_AND_TWO_SIDED_DISJOINTNESS', 'OK')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
