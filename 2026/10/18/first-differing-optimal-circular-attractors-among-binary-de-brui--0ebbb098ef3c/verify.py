#!/usr/bin/env python3
"""Finite certificates for cyclic de Bruijn string-attractor separation.

Uses only the Python standard library. Indices are zero based, cyclic.
The analytic lower-bound argument is written in RESULT.md.
"""
from itertools import combinations

LOW32 = '59a674386baa7f818d8939eb07cc2821376d4792d15bc5f652af72e3bf488c80'
HIGH33 = '614087653eb755de5c70d3637fb6bdc98ac17c488fce9667a139a92a2d190780'
# The order-eight obstruction pairs: (residue, length-seven factor, its two starts).
OBSTRUCTIONS = [
    (0, '0000111', (17, 241)),
    (1, '1000010', (2, 194)),
    (2, '0000101', (3, 139)),
    (3, '0011011', (84, 92)),
    (4, '0001000', (13, 157)),
    (5, '1101100', (22, 86)),
    (6, '1011111', (95, 143)),
    (7, '1011011', (40, 104)),
]


def bits_from_hex(s, n):
    assert len(s) == n // 4 and len(s) * 4 == n
    assert all(x in '0123456789abcdef' for x in s)
    return format(int(s, 16), '0%db' % n)


def factor(w, i, t):
    n = len(w)
    return ''.join(w[(i + j) % n] for j in range(t))


def is_debruijn(w, k):
    n = len(w)
    return n == (1 << k) and len({factor(w, i, k) for i in range(n)}) == n


def uncovered(w, k, S):
    n = len(w)
    misses = []
    for t in range(1, k + 1):
        covered = {}
        for i in range(n):
            u = factor(w, i, t)
            hits = any((i + j) % n in S for j in range(t))
            covered[u] = covered.get(u, False) or hits
        misses.extend((t, u) for u, hit in covered.items() if not hit)
    return sorted(misses)


def canonical_debruijn_words(k):
    n = 1 << k
    # Every binary order-k de Bruijn necklace has exactly one occurrence
    # of 0^k, so there is exactly one representative beginning with 0^k.
    for ones in combinations(range(k, n), n // 2):
        arr = ['0'] * n
        for i in ones:
            arr[i] = '1'
        w = ''.join(arr)
        if is_debruijn(w, k):
            yield w


def check_small_orders():
    expected_cycles = {1: 1, 2: 1, 4: 16}
    expected_profile = {1: {1: 1}, 2: {2: 1}, 4: {2: 4, 3: 8, 4: 4}}
    for k in (1, 2, 4):
        cycles = list(canonical_debruijn_words(k))
        assert len(cycles) == expected_cycles[k], (k, len(cycles))
        n = 1 << k
        histogram = {}
        for w in cycles:
            valid = [r for r in range(k)
                     if not uncovered(w, k, set(range(r, n, k)))]
            assert valid, (k, w)
            histogram[len(valid)] = histogram.get(len(valid), 0) + 1
        assert histogram == expected_profile[k], (k, histogram)
        print('order %d: %d necklaces, valid-residue histogram %s' %
              (k, len(cycles), sorted(histogram.items())))


def check_order_eight():
    n, k = 256, 8
    w32 = bits_from_hex(LOW32, n)
    w33 = bits_from_hex(HIGH33, n)
    assert is_debruijn(w32, k)
    assert is_debruijn(w33, k)
    s32 = set(range(3, n, 8))
    assert len(s32) == 32
    assert not uncovered(w32, k, s32)
    print('order 8, example A: 256 distinct 8-factors, 32-set covers all factors')

    misses_for_seven = []
    for r, u, starts in OBSTRUCTIONS:
        S = set(range(r, n, 8))
        assert len(S) == 32
        actual = tuple(i for i in range(n) if factor(w33, i, 7) == u)
        assert actual == starts, (r, actual, starts)
        assert all(not any((i + j) % n in S for j in range(7))
                   for i in starts)
        misses = uncovered(w33, k, S)
        assert (7, u) in misses, (r, u, misses)
        if r == 7:
            assert misses == [(7, '1011011')], misses
        misses_for_seven = misses if r == 7 else misses_for_seven
    s33 = set(range(7, n, 8)) | {40}
    assert len(s33) == 33
    assert not uncovered(w33, k, s33)
    assert misses_for_seven == [(7, '1011011')]
    print('order 8, example B: every one of 8 possible 32-sets fails')
    print('order 8, example B: the specified 33-set covers all factors')


if __name__ == '__main__':
    check_small_orders()
    check_order_eight()
    print('ALL CYCLIC ATTRACTOR CERTIFICATES PASSED')
