#!/usr/bin/env python3
"""Finite consistency checks for periodic Cesaro-weight algebraic identities.

This executable is supplementary: no finite test certifies the Calkin-algebra
limit, compactness, or distance theorem. Only Python's standard library is used.
"""
import cmath
import math
import random


def matrix_entry(n, k):
    return 1.0 / (n + 1) if 0 <= k <= n else 0.0


def center(a):
    mean = sum(a) / len(a)
    return [z - mean for z in a], mean


def variance(a):
    b, _ = center(a)
    return sum(abs(x)**2 for x in b) / len(a)


def rmean_diff(a):
    m = len(a)
    return math.sqrt(sum(abs(a[(i+1) % m] - a[i])**2 for i in range(m))/m)


def tail_piece(a, M, end=200000):
    # Finite section of the zero-mean periodic tail in the Gram kernel.
    return sum(a[n % len(a)] / ((n+1)**2) for n in range(M, end))


def numeric_tests():
    rng = random.Random(17733)
    checks = 0
    for m in range(1, 9):
        for trial in range(24):
            a = [complex(rng.randrange(-5,6),rng.randrange(-5,6)) for _ in range(m)]
            b, mu = center(a)
            assert abs(sum(b)) < 2e-12
            checks += 1
            va = variance(a)
            assert abs(va-(sum(abs(z)**2 for z in a)/m-abs(mu)**2)) < 2e-11
            checks += 1
            # Calkin shift-orbit average identities, reduced to exact finite periods.
            for i in range(m):
                assert abs(sum(a[(i+j) % m] for j in range(m))/m-mu) < 2e-12
                checks += 1
            assert abs(sum(abs(b[(i+1) % m])**2 for i in range(m))/m-va)<2e-12
            checks += 1
    for n in range(0, 48):
        for k in range(n+1):
            # (S* C S - C)_(n,k), the Hilbert-Schmidt covariance defect.
            expected = -1.0/((n+1)*(n+2))
            observed = matrix_entry(n+1,k+1)-matrix_entry(n,k)
            assert abs(expected-observed) < 2e-16
            checks += 1
    for a in ([1, -1], [1, 0, 0], [1, 2j, -1, -2j], [0, 0, 1, 1, -2]):
        b, _ = center(a)
        m = len(b)
        B = max(abs(v) for v in b)
        # Abel summation proves |tail(M)| <= 2 m B/(M+1)^2; numerical
        # truncation has an additional O(mB/end^2) remainder.
        for M in [10, 21, 78, 159, 999, 5001]:
            tail = tail_piece(b, M)
            bound = 2*m*B/(M+1)**2 + 2*m*B/200001**2
            assert abs(tail) <= bound*(1+1e-9), (a,M,tail,bound)
            checks += 1
    for a in ([1,-1], [1,0,0], [1,1j,-1,-1j], [3,3,3]):
        va = variance(a)
        dist = 2*math.sqrt(va)
        normess = 2*math.sqrt(sum(abs(x)**2 for x in a)/len(a))
        assert dist <= normess + 1e-13
        assert abs((normess**2 - dist**2) - 4*abs(sum(a)/len(a))**2)<1e-12
        assert abs(rmean_diff(a) - math.sqrt(sum(abs(a[(i+1)%len(a)]-a[i])**2 for i in range(len(a)))/len(a)))<1e-13
        checks += 3
    return checks


if __name__ == '__main__':
    n = numeric_tests()
    print('PASS: %d finite algebraic and kernel-tail checks' % n)
    print('Scope: numerical and finite identities only; no infinite-dimensional certification')
