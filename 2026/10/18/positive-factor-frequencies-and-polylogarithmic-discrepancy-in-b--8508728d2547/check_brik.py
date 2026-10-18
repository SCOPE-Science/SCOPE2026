#!/usr/bin/env python3
"""Finite checks for factor-frequency recurrences in Brik's recursively defined word.
No finite test certifies the infinite theorem: see the accompanying proof.
"""
from itertools import product


def occurrences(word, pattern):
    k = len(pattern)
    return [p for p in range(len(word) - k + 1) if word[p:p + k] == pattern]


def blocks(last):
    b = '101'
    yield 1, b
    for i in range(1, last):
        b = b + b[i:]
        yield i + 1, b


def run():
    patterns = [''.join(p) for k in range(1, 5) for p in product('01', repeat=k)]
    stages = list(blocks(17))
    assert all(len(b) == 2**(i - 1) + i + 1 for i, b in stages)
    for pattern in patterns:
        k = len(pattern)
        for (i, old), (_, new) in zip(stages, stages[1:]):
            cut_suffix = old[i:]
            left = occurrences(old, pattern)
            right = occurrences(new, pattern)
            deleted = sum(p < i for p in left)
            boundary = sum(p < len(old) and p + k > len(old) for p in right)
            assert len(right) == 2 * len(left) - deleted + boundary
            assert 0 <= deleted <= i and 0 <= boundary <= k - 1
            assert len(right) == len(left) + len(occurrences(cut_suffix, pattern)) + boundary
    print('EXACT BUILDING-BLOCK RECURRENCE: PASS (30 patterns, 16 transitions)')
    longword = stages[-1][1]
    nmax = len(longword)
    for pattern in patterns:
        k = len(pattern)
        # independent prefix count by incrementing the ending position
        counts = [0] * (nmax + 1)
        for end in range(1, nmax + 1):
            counts[end] = counts[end - 1] + (end >= k and longword[end - k:end] == pattern)
        assert counts[nmax] == len(occurrences(longword, pattern))
        for (i, bi), (_, bnext) in zip(stages, stages[1:]):
            lo = len(bi)
            hi = len(bnext)
            if hi > nmax: break
            # For all intermediate prefixes, the sole discrepancy in
            # the prefix-count decomposition is due to two boundaries.
            for n in range(lo, hi):
                t = n - lo
                err = counts[n] - (counts[lo] + counts[i + t] - counts[i])
                assert -k + 1 <= err <= k - 1, (i, n, pattern, err)
    print('EVERY INTERMEDIATE PREFIX DECOMPOSITION: PASS (30 patterns, lengths <= 65554)')
    for pattern in ('0', '1', '01', '11', '111', '1111', '1010'):
        c16 = len(occurrences(stages[15][1], pattern))
        c17 = len(occurrences(stages[16][1], pattern))
        print(f'pattern={pattern:5s}  counts=(B16:{c16},B17:{c17})  ratios=({c16/len(stages[15][1]):.9f},{c17/len(stages[16][1]):.9f})')
    assert not occurrences(longword,'00')
    print('ALL FINITE TESTS PASSED; infinite assertions rely on proof.')


if __name__ == '__main__':
    run()
