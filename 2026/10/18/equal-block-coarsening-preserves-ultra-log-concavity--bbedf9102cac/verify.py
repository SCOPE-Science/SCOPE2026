#!/usr/bin/env python3
"""Standalone exact-arithmetic diagnostics for equal-width ULC block aggregation.

All checks are finite diagnostics; the universal proof is analytic.
"""
from fractions import Fraction
from math import factorial


def check_factorial_pairs():
    checks = 0
    for m in range(1, 11):
        for k in range(1, 13):
            for j in range(m):
                for l in range(m):
                    left = Fraction(factorial(k), factorial(m*k+j))
                    left *= Fraction(factorial(k), factorial(m*k+l))
                    right = Fraction(factorial(k-1), factorial(m*(k-1)+j))
                    right *= Fraction(factorial(k+1), factorial(m*(k+1)+l))
                    assert left >= right, (m, k, j, l)
                    if m >= 2 and (j < m-1 or l > 0):
                        assert left > right, (m, k, j, l)
                    checks += 1
    return checks


def check_ulc_sequences():
    checks = 0
    for m in range(1, 8):
        for n_max in range(0, 15):
            for n_min in range(n_max+1):
                for rho in (Fraction(1, 3), Fraction(1), Fraction(5, 2)):
                    a = [
                        (rho ** n) / factorial(n)
                        if n_min <= n <= n_max else Fraction(0)
                        for n in range(40)
                    ]
                    b = [sum(a[m*k:m*(k+1)], Fraction(0))
                         for k in range(40//m)]
                    for k in range(1, len(b)-1):
                        lhs = k*b[k]*b[k]
                        rhs = (k+1)*b[k-1]*b[k+1]
                        assert lhs >= rhs, (m, n_min, n_max, rho, k)
                        if m >= 2 and b[k-1]*b[k+1] > 0:
                            assert lhs > rhs, (m, n_min, n_max, rho, k)
                        checks += 1
    return checks


def check_cross_pairs():
    checks = 0
    for m in range(1, 6):
        for n_max in range(2, 17):
            for n_min in range(0, n_max+1, 2):
                rho = Fraction(3, 2)
                a = [rho**n/factorial(n) if n_min <= n <= n_max
                     else Fraction(0) for n in range(35)]
                for k in range(1, 5):
                    if m*(k+1)+m-1 >= len(a):
                        continue
                    for j in range(m):
                        for l in range(m):
                            left = (factorial(k)*a[m*k+j]
                                    *factorial(k)*a[m*k+l])
                            right = (factorial(k-1)*a[m*(k-1)+j]
                                     *factorial(k+1)*a[m*(k+1)+l])
                            assert left >= right, (m, n_min, n_max, k, j, l)
                            checks += 1
    return checks


if __name__ == '__main__':
    a = check_factorial_pairs()
    b = check_ulc_sequences()
    c = check_cross_pairs()
    print(f'PASS: {a} factorial-pair checks, {b} ULC-block checks, '
          f'{c} cross-pair checks ({a+b+c} total exact tests).')
