#!/usr/bin/env python3
"""Exact consistency checks for an elliptic-ruled symmetric-tensor Hilbert function.

Only the Python 3 standard library is required. Finite tests are not a
replacement for the geometric all-degree argument.
"""
from math import comb
from fractions import Fraction


def mul(A, B):
    rows, shared, cols = len(A), len(B), len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(shared))
             for j in range(cols)] for i in range(rows)]


def rank(A):
    if not A:
        return 0
    B = [[Fraction(x) for x in row] for row in A]
    m, n = len(B), len(B[0]); h = 0
    for j in range(n):
        p = next((k for k in range(h, m) if B[k][j]), None)
        if p is None:
            continue
        B[h], B[p] = B[p], B[h]
        z = B[h][j]
        B[h] = [x/z for x in B[h]]
        for k in range(m):
            if k != h and B[k][j]:
                z = B[k][j]
                B[k] = [B[k][s]-z*B[h][s] for s in range(n)]
        h += 1
        if h == m:
            break
    return h


def check():
    # h(m) = 1+d * sum_{j=1}^m j*(m-j+1)
    for m in range(25):
        s = sum(j*(m-j+1) for j in range(1, m+1))
        target = comb(m+2, 3) if m else 0
        assert s == target, (m, s, target)
        for d in range(1, 9):
            assert 1+d*s == 1+d*target
    assert [1 + (comb(m+2,3) if m else 0) for m in range(7)] == [1,2,5,11,21,36,57]
    # Substitution b -> b+a on degree-n binary forms has one Jordan block.
    for n in range(10):
        dim = n+1
        T = [[comb(j,i) if j >= i else 0 for j in range(dim)]
             for i in range(dim)]
        N = [[T[i][j]-(1 if i == j else 0) for j in range(dim)]
             for i in range(dim)]
        assert rank(N) == n
        P = [[int(i == j) for j in range(dim)] for i in range(dim)]
        for exponent in range(dim+1):
            assert rank(P) == dim-exponent, (n, exponent, rank(P))
            if exponent < dim:
                P = mul(P, N)
    print('VERIFY_OK degrees=0..24 base_degrees=1..8 unipotent_blocks=0..9')


if __name__ == '__main__':
    check()
