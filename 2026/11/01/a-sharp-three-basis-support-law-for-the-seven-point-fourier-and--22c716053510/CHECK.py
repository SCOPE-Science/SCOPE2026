#!/usr/bin/env python3
"""Exact finite-field certificate for three Fourier/chirp bases in dimension seven.

Run with Python 3.9+: python3 CHECK.py
All rank tests use F_1009.  Rank full modulo 1009 implies the
corresponding cyclotomic matrix has full rank over C.
"""
from itertools import combinations
from math import comb

P, Q, ROOT = 7, 1009, 105
assert all(Q % d for d in range(2, int(Q**0.5) + 1)), 'modulus must be prime'
assert ROOT != 1 and pow(ROOT, P, Q) == 1
OMEGA = [pow(ROOT, j, Q) for j in range(P)]
SUBSETS = {s: list(combinations(range(P), s)) for s in range(P + 1)}


def full_column_rank(rows, n):
    """Exact Gaussian elimination over F_1009; matrix has >= n rows."""
    a = [list(row) for row in rows]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(a)) if a[i][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], Q - 2, Q)
        a[rank][col:] = [(inv * v) % Q for v in a[rank][col:]]
        for i in range(rank + 1, len(a)):
            factor = a[i][col]
            if factor:
                a[i][col:] = [(x - factor * y) % Q for x, y in zip(a[i][col:], a[rank][col:])]
        rank += 1
        if rank == n:
            return True
    return False


def verify_all():
    total = 0
    by_support = {}
    for s in range(1, P + 1):
        nchecked = 0
        for a in range(P + 1):
            b = s + 1 - a
            if b < 0 or b > P or a > s-1 or b > s-1:
                continue
            for support in SUBSETS[s]:
                row_f = [[OMEGA[k*j % P] for j in support] for k in range(P)]
                row_c = [[OMEGA[(k*j-j*j) % P] for j in support] for k in range(P)]
                for zeros_f in SUBSETS[a]:
                    first = [row_f[k] for k in zeros_f]
                    for zeros_c in SUBSETS[b]:
                        rows = first + [row_c[k] for k in zeros_c]
                        assert full_column_rank(rows, s), (
                            'full-rank counterexample', support, zeros_f, zeros_c)
                        nchecked += 1
        by_support[s] = nchecked
        total += nchecked
        print('support %d: %d full-column-rank certificates' % (s, nchecked))
    expected = {1:0,2:0,3:15435,4:51450,5:56595,6:23324,7:2989}
    assert by_support == expected, (by_support, expected)
    assert total == 149793
    # The explicit sharp vector f = delta_0 - delta_1.  Fourier zeros
    # require omega^k=1 => k=0.  Chirp-Fourier zeros require
    # omega^(k-1)=1 => k=1.  Thus supports are (2,6,6).
    assert [k for k in range(P) if (1 - OMEGA[k]) % Q == 0] == [0]
    assert [k for k in range(P) if (1 - OMEGA[(k-1) % P]) % Q == 0] == [1]
    print('PASS: %d exact rank tests, and sharp example supports (2,6,6)' % total)

if __name__ == '__main__':
    verify_all()
