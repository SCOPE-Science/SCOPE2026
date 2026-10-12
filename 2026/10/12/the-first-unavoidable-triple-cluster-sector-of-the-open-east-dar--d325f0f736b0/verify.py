#!/usr/bin/env python3
"""Independent exact-arithmetic checks for four-excitation EAST-jump ranks.

Run with Python 3.10+ standard library: python3 verify.py.
Finite checks corroborate the accompanying all-size linear-algebra proof.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def masks(n, k):
    return [u for u in range(1 << n) if u.bit_count() == k]


def matrix(n, k, seeded=False, avoid_triples=False):
    cols = masks(n, k)
    if avoid_triples:
        cols = [v for v in cols if not (v & (v >> 1) & (v >> 2))]
    rows = masks(n, k - 1)
    index = {v: i for i, v in enumerate(rows)}
    a = [[0] * len(cols) for _ in rows]
    for j, v in enumerate(cols):
        for site in range(n):
            if not v & (1 << site):
                continue
            if (site == 0 and seeded) or (site > 0 and v & (1 << (site - 1))):
                a[index[v ^ (1 << site)]][j] = 1
    return a


def rank_mod(a, prime):
    if not a:
        return 0
    b = [row[:] for row in a]
    nr, nc = len(b), len(b[0])
    pivot = 0
    for j in range(nc):
        at = next((i for i in range(pivot, nr) if b[i][j] % prime), None)
        if at is None:
            continue
        b[pivot], b[at] = b[at], b[pivot]
        inv = pow(b[pivot][j], -1, prime)
        b[pivot] = [(x * inv) % prime for x in b[pivot]]
        for i in range(pivot + 1, nr):
            factor = b[i][j]
            if factor:
                b[i] = [(u - factor * v) % prime for u, v in zip(b[i], b[pivot])]
        pivot += 1
        if pivot == nr:
            break
    return pivot


def det_bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    assert all(len(row) == n for row in a)
    if not n:
        return 1
    sign, denom = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            nxt = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if nxt is None:
                return 0
            a[k], a[nxt] = a[nxt], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % denom == 0
                a[i][j] = num // denom
            a[i][k] = 0
        denom = pivot
    return sign * a[n - 1][n - 1]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def check():
    # The only nontrivial finite constants used in the infinite-size proof.
    assert det_bareiss(matrix(3, 2, seeded=True)) == -1
    a = matrix(4, 3, seeded=True)
    assert det_bareiss([a[i] for i in (0, 1, 2, 3)]) == 1
    assert det_bareiss(matrix(5, 3, seeded=True)) == -1
    for n in range(7, 13):
        full = matrix(n, 4)
        restricted = matrix(n, 4, avoid_triples=True)
        rank_full = choose(n, 3) - 5
        dim_full = choose(n, 4) - rank_full
        dim_no111 = choose(n - 3, 4) + 3 * choose(n - 3, 3) - choose(n - 2, 3) + 1
        rank_restricted = len(restricted[0]) - dim_no111
        for p in (1000003, 1000033):
            assert rank_mod(full, p) == rank_full, (n, p, 'full')
            assert rank_mod(restricted, p) == rank_restricted, (n, p, 'restricted')
        assert dim_full - dim_no111 == choose(n - 5, 2)
        print('n=%d full_dark=%d no_triple_dark=%d quotient=%d' %
              (n, dim_full, dim_no111, dim_full - dim_no111))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
