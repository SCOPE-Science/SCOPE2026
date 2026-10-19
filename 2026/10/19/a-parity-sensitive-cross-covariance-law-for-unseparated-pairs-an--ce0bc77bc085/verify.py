#!/usr/bin/env python3
"""Independent finite verification for the succession--fixed-point cross-covariance law.

This finite checker corroborates, but does not replace, the all-size counting proof.
Run with Python 3 using only the standard library.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def claimed(n, i, j):
    """1-based indices, 1 <= i < n, 1 <= j <= n."""
    if j in (i, i + 1) or j in (1, n):
        return Fraction(1, n*n*(n-1))
    return Fraction(-2, n*n*(n-1)*(n-2))


def rank(matrix):
    m = [[Fraction(v) for v in row] for row in matrix]
    h = len(m)
    w = len(m[0]) if h else 0
    r = 0
    for col in range(w):
        pivot = next((i for i in range(r, h) if m[i][col]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][col]
        m[r] = [x / p for x in m[r]]
        for i in range(h):
            if i != r and m[i][col]:
                k = m[i][col]
                m[i] = [a-k*b for a,b in zip(m[i], m[r])]
        r += 1
        if r == h:
            break
    return r


def brute(n):
    pa = [0]*(n-1)
    pf = [0]*n
    joint = [[0]*n for _ in range(n-1)]
    total = 0
    weighted_sum = 0
    for p in permutations(range(1,n+1)):
        a = [int(p[i+1] == p[i]+1) for i in range(n-1)]
        f = [int(p[j] == j+1) for j in range(n)]
        for i in range(n-1):
            pa[i] += a[i]
            if a[i]:
                for j in range(n):
                    joint[i][j] += f[j]
        for j in range(n):
            pf[j] += f[j]
        total += 1
        weighted_sum += sum(a)*sum(f)
    assert total == factorial(n)
    assert pa == [total//n]*(n-1)
    assert pf == [total//n]*n
    matrix = [[Fraction(joint[i][j],total)-Fraction(pa[i]*pf[j],total*total)
               for j in range(n)] for i in range(n-1)]
    for i in range(n-1):
        for j in range(n):
            assert matrix[i][j] == claimed(n,i+1,j+1), (n,i,j,matrix[i][j])
    expected_rank = n-1 if n%2 == 0 else n-2
    assert rank(matrix) == expected_rank
    if n >= 3:
        assert Fraction(weighted_sum,total)-Fraction(n-1,n) == Fraction(2,n*(n-1))
    else:
        assert Fraction(weighted_sum,total)-Fraction(n-1,n) == Fraction(1,2)
    if n%2 == 1:
        assert [sum(((-1)**i)*matrix[i][j] for i in range(n-1)) for j in range(n)] == [0]*n
    print(f'n={n}: all {(n-1)*n} indexed covariances, aggregate, rank, and parity checked')


for n in range(2,9):
    brute(n)

for n in range(3,41):
    M = [[n-2 if j in (1,n,i,i+1) else -2 for j in range(1,n+1)] for i in range(1,n)]
    assert rank(M) == (n-1 if n%2 == 0 else n-2)
print('ranks verified for n=3,...,40; finite checks completed')
