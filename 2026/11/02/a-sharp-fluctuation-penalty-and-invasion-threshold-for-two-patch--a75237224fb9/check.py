#!/usr/bin/env python3
"""Exact arithmetic checks for a two-habitat periodic dispersal result.

Runs with the Python standard library. Finite checks supplement, not replace,
the analytic proof and do not certify generality or historical novelty.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

ZERO, ONE, TWO, HALF = F(0), F(1), F(2), F(1, 2)


def mat(s, a, b):
    return ((a * (ONE-s), b*s), (a*s, b*(ONE-s)))


def mult(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def tr(A):
    return A[0][0] + A[1][1]


def det(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]


def largest(T, U):
    return (float(T) + sqrt(max(0.0, float(T*T-4*U)))) / 2


def characteristic(z, T, U):
    return z*z - T*z + U


def run():
    cases = 0
    exact = 0
    equal_numerical = 0
    grids = [F(1, 10), F(1, 2), F(1), F(7, 5), F(2), F(3)]
    means = [ZERO, F(1, 10), F(1, 4), F(2, 5), HALF]
    for a, b, m in product(grids, grids, means):
        h = min(m, HALF-m)
        ds = sorted(set([ZERO, h/3, h/2, h]))
        prev = None
        for d in ds:
            B = mult(mat(m+d, a, b), mat(m-d, a, b))
            x = d*d
            T = (a*a+b*b)*(ONE-m)**2+TWO*a*b*m*m-(a+b)**2*x
            U = (a*b)**2*(ONE-2*m)**2-4*(a*b)**2*x
            assert tr(B) == T
            assert det(B) == U
            assert T > 0 and U >= 0
            assert T*T-4*U >= 0
            exact += 4
            lam = largest(T, U)
            if a != b:
                K = 4*a*a*b*b/(a+b)**2
                bracket = 4*m*(a+b)**2 - 3*(a*a+b*b) - 10*a*b
                rhs = a*a*b*b*(a-b)**2*bracket/(a+b)**4
                assert characteristic(K, T, U) == rhs and rhs < 0
                exact += 2
                if prev is not None:
                    assert lam < prev - 1e-11
                    cases += 1
            else:
                assert characteristic(a*a, T, U) == 0
                exact += 1
                assert abs(lam - float(a*a)) < 1e-10
                equal_numerical += 1
            prev = lam
            if a > 1 and 0 < b < 1/a:
                t = (a+b)*(ONE-m)
                u = a*b*(ONE-2*m)
                C = (a+b)**2-4*(a*b)**2
                assert C > 0
                assert characteristic(ONE, T, U) == (ONE-t+u)*(ONE+t+u)+C*x
                exact += 2
    a, b, m, d = F(7, 5), F(1, 10), F(1, 4), F(1, 4)
    constant = mat(m, a, b)
    alternating = mult(mat(m+d, a, b), mat(m-d, a, b))
    assert characteristic(ONE, tr(constant), det(constant)) == -F(11, 200)
    assert det(alternating) == ZERO
    assert tr(alternating) == F(197, 200)
    t, u = (a+b)*(ONE-m), a*b*(ONE-2*m)
    C = (a+b)**2-4*(a*b)**2
    assert (t-ONE-u)*(ONE+t+u)/C == F(4829, 86864)
    assert F(4829, 86864) < d*d
    exact += 5
    print(f'OK: {exact} exact-rational checks, {cases} sampled strict comparisons, and {equal_numerical} sampled equality checks')


if __name__ == '__main__':
    run()
