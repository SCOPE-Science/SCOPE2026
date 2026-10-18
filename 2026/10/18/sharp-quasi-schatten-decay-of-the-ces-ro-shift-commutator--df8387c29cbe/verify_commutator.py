#!/usr/bin/env python3
"""Finite exact checks for a Cesaro/shift commutator and lower-triangular blocks.
The infinite-dimensional singular-number theorem is proved separately.
"""
from fractions import Fraction
from math import sin, pi, isclose


def multiply(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), Fraction(0))
             for j in range(n)] for i in range(n)]


def identity(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def check(n):
    z = Fraction(0)
    C = [[Fraction(1, i + 1) if j <= i else z for j in range(n)]
         for i in range(n)]
    S = [[Fraction(i == j + 1) for j in range(n)] for i in range(n)]
    CS, SC = multiply(C, S), multiply(S, C)
    actual = [[CS[i][j] - SC[i][j] for j in range(n)] for i in range(n)]
    expected = [[-Fraction(1, i*(i+1)) if i > 0 and j < i else z
                 for j in range(n)] for i in range(n)]
    assert actual == expected, (n, "commutator entries")

    # Every finite strict lower-triangular all-ones block contains an
    # (m-1)-square inclusive lower-triangular block with an extra null row/column.
    m = n
    T = [[Fraction(i > j) for j in range(m)] for i in range(m)]
    L = [[Fraction(i >= j) for j in range(m-1)] for i in range(m-1)]
    assert [row[:m-1] for row in T[1:]] == L
    D = [[Fraction(i == j) - Fraction(i == j + 1) for j in range(m-1)]
         for i in range(m-1)]
    assert multiply(D, L) == identity(m-1)
    assert multiply(L, D) == identity(m-1)

    # The inverse Gram tridiagonal and trace can be verified exactly.
    r = m - 1
    G = [[sum((D[k][i]*D[k][j] for k in range(r)), z)
          for j in range(r)] for i in range(r)]
    assert all(G[i][j] == (Fraction(2 if i < r-1 else 1) if i == j
                                  else Fraction(-1) if abs(i-j)==1
                                  else z)
               for i in range(r) for j in range(r))
    assert sum(G[i][i] for i in range(r)) == 2*r-1
    if r > 0:
        predicted = [1/(2*sin((2*k-1)*pi/(4*r+2))) for k in range(1, r+1)]
        assert isclose(sum(x*x for x in predicted), r*(r+1)/2,
                       rel_tol=3e-12, abs_tol=3e-10)


if __name__ == "__main__":
    for dimension in range(2, 30):
        check(dimension)
    print("CESARO_SHIFT_QUASI_SCHATTEN_FINITE_IDENTITIES_OK", "dimensions=28")
