#!/usr/bin/env python3
"""Finite, independent checks for cubic Fibonacci-window GCD formulas.

The mathematical proof is supplied separately; this script only tests finite ranges.
Run with: python3 verify_cubic_windows.py
"""
from math import gcd
from functools import reduce

MAX_K = 300
MAX_N = 14
F = [0, 1]
for _ in range(MAX_K + MAX_N + 5):
    F.append(F[-1] + F[-2])
L = [2, 1]
for _ in range(MAX_K + 5):
    L.append(L[-1] + L[-2])


def predicted(k):
    if k % 2:
        return 2 if k % 3 == 0 else 1
    h = k // 2
    num = L[h] if h % 2 else F[h] * (3 if k % 8 == 0 else 1)
    return num // (2 if k % 6 == 0 else 1)


def actual(k, begin):
    return reduce(gcd, (sum(F[i] ** 3 for i in range(n, n + k)) for n in range(begin, begin + MAX_N)), 0)


win_count = 0
for k in range(1, MAX_K + 1):
    g0 = actual(k, 0)
    g1 = actual(k, 1)
    p = predicted(k)
    assert g0 == g1 == p, (k, g0, g1, p)
    win_count += 2 * MAX_N
    x, y = F[k], F[k + 1]
    ds = [F[k + i] ** 3 - F[i] ** 3 for i in range(4)]
    d = reduce(gcd, ds, 0)
    eps = gcd(x + y, 2)
    h = gcd(x, y - (-1 if k & 1 else 1))
    assert d == gcd(x ** 3, y ** 3 - 1, 3 * x * eps)
    assert d == h * (3 if k % 8 == 0 else 1)
    base = sum(F[j] ** 3 for j in range(k))
    assert gcd(d, base) == p

# Test the cubic telescoper (including nontrivial offsets).
for n in range(MAX_K):
    x, y = F[n], F[n + 1]
    xp, yp = F[n + 1], F[n + 2]
    T = -3 * x**3 + 3 * x * y**2 - y**3
    Tp = -3 * xp**3 + 3 * xp * yp**2 - yp**3
    assert Tp - T == 2 * F[n]**3

# Check the integral fourth-order recurrence, both powers and window sums.
for n in range(MAX_N + MAX_K - 4):
    fs = [F[n + i] ** 3 for i in range(5)]
    assert fs[4] == 3 * fs[3] + 6 * fs[2] - 3 * fs[1] - fs[0]

print(f'PASS cubic Fibonacci windows k=1..{MAX_K}, two offset sets of {MAX_N} starts: {win_count} window-sum comparisons.')
print(f'PASS gcd of four differences, closed difference gcd, telescoper, recurrence ({MAX_K} lengths).')
print('First 24 cubic-window gcds:', [predicted(k) for k in range(1, 25)])
