#!/usr/bin/env python3
"""Exact rational finite checks for uniform real Lipschitz potentials on weighted book metrics."""
from fractions import Fraction as F
from math import comb


def integral(m, t, power):
    """Direct binomial expansion of integral_0^t x^power (2-x)^m dx."""
    return sum((F(comb(m, j) * 2**(m-j) * (-1)**j, j+power+1)
                * t**(j+power+1) for j in range(m+1)), F(0))


def h(m, t):
    return (F(2**(m+1)) - (2-t)**(m+1)) / F(m+1)


def determinant(matrix):
    """Fraction Gaussian elimination, independent of block determinant lemma."""
    a = [[F(x) for x in row] for row in matrix]
    n = len(a)
    res = F(1)
    for i in range(n):
        pivot = next(j for j in range(i, n) if a[j][i] != 0)
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            res = -res
        p = a[i][i]
        res *= p
        for j in range(i+1, n):
            factor = a[j][i] / p
            for k in range(i+1, n):
                a[j][k] -= factor * a[i][k]
            a[j][i] = F(0)
    return res


def check(m, t):
    base = integral(m, t, 0)
    second = integral(m, t, 2)
    assert base == h(m, t)
    explicit_second = (4*h(m,t) - 4*(F(2**(m+2))-(2-t)**(m+2))/F(m+2)
                       + (F(2**(m+3))-(2-t)**(m+3))/F(m+3))
    assert second == explicit_second
    v = second / base
    w = integral(m+2,t,0)/(12*base)
    assert w == h(m+2,t)/(12*h(m,t))
    # Reconstruct each covariance entry independently from the fiber law.
    d = m+1
    cov = [[F(0) for _ in range(d)] for _ in range(d)]
    for i in range(d):
        for j in range(d):
            if i == j == 0:
                cov[i][j] = second/base
            elif i == 0 or j == 0:
                cov[i][j] = second/(2*base)
            elif i != j:
                cov[i][j] = second/(4*base)
            else:
                conditional_variance_numerator = integral(m+2,t,0)/12
                cov[i][j] = second/(4*base)+conditional_variance_numerator/base
    target = [[(v if i == j == 0 else
                v/2 if i == 0 or j == 0 else
                v/4+(w if i==j else 0)) for j in range(d)] for i in range(d)]
    assert cov == target
    assert determinant(cov) == v*w**m
    assert base > 0 and v > 0 and w > 0


def main():
    params = [F(1,4),F(1,2),F(1),F(3,2),F(2)]
    count=0
    for m in range(2, 11):
        for t in params:
            check(m,t)
            count += 1
    print('EXACT_WEIGHTED_BOOK_MOMENT_CHECKS_PASS',count,'cases')


if __name__ == '__main__':
    main()
