#!/usr/bin/env python3
"""Exact-rational diagnostics for lifted polygonal McMillan-Henon dynamics.

This finite test suite supports, but does not replace, the parameter-uniform proof.
Run: python3 verify_transport.py
"""
from fractions import Fraction as Q
from math import gcd


def force(p):
    r = p % 2
    return Q(0) if r < 1 else 2 * (r - 1)


def step(z):
    q, p = z
    return p, -q + force(p)


def orbit(z, steps):
    for _ in range(steps):
        z = step(z)
    return z


def torus(z):
    return tuple(v % 2 for v in z)


def branch(z):
    return 'A' if z[1] % 2 < 1 else 'B'


def matmul(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


A = ((0, 1), (-1, 0))
B = ((0, 1), (-1, 2))
I = ((1, 0), (0, 1))


def matpow(M, n):
    R = I
    while n:
        if n & 1:
            R = matmul(R, M)
        M = matmul(M, M)
        n >>= 1
    return R


checks = 0
for N in range(4, 262, 2):
    t = Q(1, N)
    n = N + 4
    m = N // 2
    expected_word = 'A' + 'B' * m + 'AA' + 'B' * m + 'A'
    total_matrix = matmul(A, matmul(matpow(B, m), matmul(matpow(A, 2), matmul(matpow(B, m), A))))
    assert total_matrix == ((N + 1, N), (-N, 1 - N))
    checks += 1
    center = (t, t)
    halfway = orbit(center, n // 2)
    expected_half = {
        0: (-1 - t, 1 - t),
        2: (1 - t, 1 - t),
        4: (1 - t, -1 - t),
        6: (-1 - t, -1 - t),
    }[N % 8]
    assert halfway == expected_half, (N, halfway, expected_half)
    checks += 1
    for multiplier in (Q(0), Q(1, 4), -Q(1, 4), Q(1, 2), -Q(1, 2), Q(3, 4)):
        h = multiplier * t
        z0 = (t + h, t - h)
        z = z0
        seen_branches = ''
        for _ in range(n):
            seen_branches += branch(z)
            z = step(z)
        assert seen_branches == expected_word, (N, h, seen_branches, expected_word)
        expected = (z0[0] + 2, z0[1] - 2) if N % 4 == 0 else z0
        assert z == expected, (N, z, expected)
        for k in range(4):
            z = orbit(z, n)
            expected = (z0[0] + 2 * (k + 2), z0[1] - 2 * (k + 2)) if N % 4 == 0 else z0
            assert z == expected, (N, k, z, expected)
            checks += 1

# Rational-grid return dichotomy, including points on switching interfaces.
for den in range(1, 13):
    states_seen = set()
    for i in range(2 * den):
        for j in range(2 * den):
            s = (Q(i, den), Q(j, den))
            if torus(s) in states_seen:
                continue
            observed = {}
            z = s
            while torus(z) not in observed:
                observed[torus(z)] = z
                states_seen.add(torus(z))
                z = step(z)
            assert torus(z) == torus(s), (den, s)
            n = len(observed)
            v = ((z[0] - s[0]) / 2, (z[1] - s[1]) / 2)
            assert all(x.denominator == 1 for x in v)
            if n % 4:
                zfin = orbit(s, (4 // gcd(n, 4)) * n)
                assert zfin == s, (den, s, n, zfin)
            else:
                for k in range(1, 4):
                    zfin = orbit(s, k * n)
                    assert zfin == (s[0] + 2 * k * v[0], s[1] + 2 * k * v[1])
            checks += 1
print('EXACT_RATIONAL_CHECKS_OK', checks)
