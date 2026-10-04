#!/usr/bin/env python3
from math import comb

def q2(n):
    q = 0
    while comb(q, 2) < n:
        q += 1
    return q

def q3(N):
    target = comb(N, 2)
    q = 0
    while comb(q, 3) < target:
        q += 1
    return q

def B(n):
    a = q2(n)
    N = n + a
    return N + q3(N) + 2

def t(m):
    return m + comb(m, 2) + comb(m, 3)

def s(m):
    return (3*m + 4) * t(m) + 1

# Exact definition checks and comparison with the printed source bound.
for n in range(1, 10001):
    a = q2(n)
    assert comb(a, 2) >= n
    if a > 0:
        assert comb(a-1, 2) < n

    N = n + a
    b = q3(N)
    assert comb(b, 3) >= comb(N, 2)
    if b > 0:
        assert comb(b-1, 3) < comb(N, 2)

    assert B(n) == n + a + b + 2
    assert B(n) <= 15 * n * n

# The improved obstruction bound is the envelope evaluated at s(m).
for m in range(1, 101):
    r = s(m)
    improved = B(r)
    printed = 15 * r * r
    assert improved < printed

# Numerical growth diagnostics: B(n)-n is sublinear and B(s(m)) is quartic scale.
samples_n = [10, 100, 1000, 10000]
samples_m = [5, 10, 20, 40]
print("B_VALUES", [(n, B(n)) for n in samples_n])
print("OBSTRUCTION_VALUES", [(m, B(s(m)), 15*s(m)*s(m)) for m in samples_m])
print("VERIFY_OK")
