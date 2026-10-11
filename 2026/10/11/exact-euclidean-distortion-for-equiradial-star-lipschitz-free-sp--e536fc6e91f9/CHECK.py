#!/usr/bin/env python3
"""Numerical sanity checks of a finite-dimensional algebraic formula.

The argument establishing that the formula is exact is in RESULT.md;
this program is not a proof of the universal assertion.
"""
import math


def branches(m, alpha):
    return range(-m, m + 1, 2)


def objective(m, alpha, c):
    assert m >= 2 and 0 <= alpha <= 1 and c > -1 / m
    R = max(m * (1 + alpha * alpha) + 2 * alpha * s
            - c * (s + alpha * m) ** 2 / (1 + m * c)
            for s in branches(m, alpha))
    D = max((1 + c) / (1 + alpha) ** 2, 0.5)
    return R * D


def candidates(m, alpha):
    c0 = (1 + alpha) ** 2 / 2 - 1
    low = max(c0, -1 / m)
    cand = set()
    if c0 > -1 / m:
        cand.add(c0)
    S = list(branches(m, alpha))
    for s in S:
        if abs(s) < m:
            c = (abs(s + alpha * m) * math.sqrt((m - 1) / (m*m-s*s)) - 1) / m
            if c > -1 / m and c + 1e-13 >= low:
                cand.add(c)
    for i, s in enumerate(S):
        for u in S[i+1:]:
            if s + u:
                c = 2 * alpha / (s + u)
                if c > -1 / m and c + 1e-13 >= low:
                    cand.add(c)
    assert cand
    return sorted(cand)


def distortion_squared(m, alpha):
    return min(objective(m, alpha, c) for c in candidates(m, alpha))


def close(actual, expected, tol=1e-9):
    assert math.isclose(actual, expected, rel_tol=tol, abs_tol=tol), (actual, expected)


for m in range(2, 30):
    close(distortion_squared(m, 0), m)
    n = m+1
    close(distortion_squared(m, 1), 2*(n//2)*((n+1)//2)/n)
close(distortion_squared(3, 0.5), 15/7)
close(distortion_squared(4, 0.4), 144/49)
for m in range(2, 22):
    for j in range(101):
        a = j / 100
        c = candidates(m, a)
        best = distortion_squared(m, a)
        # Many interior points, deliberately not taken as an infinite proof.
        for k in range(101):
            x = -1 / m + 0.003 + k * (3 + 1/m) / 100
            if x > -1/m:
                assert best <= objective(m, a, x) + 1e-8
print('Sample and endpoint checks passed.')
