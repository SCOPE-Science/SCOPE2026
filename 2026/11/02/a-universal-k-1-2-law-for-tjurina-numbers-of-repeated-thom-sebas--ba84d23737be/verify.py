#!/usr/bin/env python3
"""Finite arithmetic checks for exact Tjurina numbers of separated sums.

This is a reproducibility aid, not a proof of the infinite or asymptotic claims.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

PRIME = 1000003


def char(blocks):
    c = Counter()
    for ell in blocks:
        for j in range(ell):
            c[ell - 1 - 2 * j] += 1
    return c


def multiply(a, b):
    out = Counter()
    for x, u in a.items():
        for y, v in b.items():
            out[x + y] += u * v
    return out


def coefficient_count(blocks, k):
    c = Counter({0: 1})
    for _ in range(k):
        c = multiply(c, char(blocks))
    return c[0] + c[1]


def rank_mod(mat, p):
    a = [[v % p for v in row] for row in mat]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for i in range(rank + 1, m):
            factor = a[i][col]
            if factor:
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def matrix_cokernel_dim(blocks, k):
    d = sum(blocks)
    successor = [-1] * d
    offset = 0
    for ell in blocks:
        for j in range(1, ell):
            successor[offset + j] = offset + j - 1
        offset += ell
    tuples = list(product(range(d), repeat=k))
    lookup = {t: i for i, t in enumerate(tuples)}
    D = len(tuples)
    mat = [[0] * D for _ in range(D)]
    for col, t in enumerate(tuples):
        for i, current in enumerate(t):
            next_index = successor[current]
            if next_index != -1:
                w = list(t)
                w[i] = next_index
                mat[lookup[tuple(w)]][col] += 1
    return D - rank_mod(mat, PRIME)


def main():
    # Independent Kronecker-sum arithmetic in sufficiently small dimensions.
    cases = [([2], 4), ([3], 3), ([1, 2], 3), ([1, 3], 3), ([2, 2], 3)]
    for blocks, largest_k in cases:
        for k in range(1, largest_k + 1):
            assert coefficient_count(blocks, k) == matrix_cokernel_dim(blocks, k), (blocks, k)

    # For f=x^4+y^5+x^2y^3, weighted initial Jacobian ideal is (x^3,y^4),
    # and its equation class reduces to -x^2 y^3/10 in the local Milnor algebra.
    assert Fraction(1) - Fraction(1, 2) - Fraction(3, 5) == -Fraction(1, 10)
    assert [coefficient_count([2] + [1] * 10, k) for k in range(1, 9)] == [
        11, 122, 1363, 15326, 173310, 1969620, 22482435, 257618870
    ]
    for k in range(1, 20):
        assert coefficient_count([1] * 5, k) == 5 ** k
        assert 0 < coefficient_count([2] + [1] * 10, k) < 12 ** k
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
