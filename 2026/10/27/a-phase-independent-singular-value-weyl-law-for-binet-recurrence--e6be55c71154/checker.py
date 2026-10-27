#!/usr/bin/env python3
"""Finite checks for the Binet-recurrence Fock singular-value normalization.

Numerical samples are not a proof of the Weyl law.
"""
import cmath
import math


def weights(amps, roots, N):
    assert abs(sum(amps)) < 1e-10
    return [sum(a * (r ** n) for a, r in zip(amps, roots)) / math.sqrt(n)
            for n in range(1, N + 1)]


def verify_periodic(N=10000):
    amps = [1, -1]
    roots = [1, -1]
    arr = weights(amps, roots, N)
    for n in range(1, N + 1):
        expected = (0 if n % 2 == 0 else 2) / math.sqrt(n)
        assert abs(arr[n-1] - expected) < 2e-12
    squares = sorted((abs(a) ** 2 for a in arr), reverse=True)
    k = N // 10
    assert abs(k * squares[k-1] - 2.0) < 0.01
    return k * squares[k-1]


def verify_irrational(N=20000):
    amps = [1, -1]
    q = cmath.exp(1j * math.sqrt(2))
    roots = [1, q]
    arr = weights(amps, roots, N)
    for n in [1, 2, 3, 7, 31, 113, 1011]:
        assert abs(arr[n-1] - (1-q ** n) / math.sqrt(n)) < 2e-12
    squares = sorted((abs(a) ** 2 for a in arr), reverse=True)
    k = N // 10
    assert abs(k * squares[k-1] - 2.0) < 0.05
    return k * squares[k-1]


def verify_jackson():
    for q in [0.5, 0.8j, -1.0]:
        amps = [1/(1-q), -1/(1-q)]
        roots = [1, q]
        arr = weights(amps, roots, 100)
        for n in [1, 2, 3, 7, 17, 37]:
            expected = (1-q**n) / ((1-q)*math.sqrt(n))
            assert abs(arr[n-1] - expected) < 2e-12


if __name__ == '__main__':
    verify_jackson()
    print('periodic k*s_k^2 =', verify_periodic())
    print('irrational k*s_k^2 =', verify_irrational())
    print('finite coefficient and sorted-singular-value checks passed')
