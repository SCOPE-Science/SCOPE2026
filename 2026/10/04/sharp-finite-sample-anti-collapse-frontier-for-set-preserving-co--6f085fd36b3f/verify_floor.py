#!/usr/bin/env python3
"""Deterministic checks for the sharp conformal e-value floor theorem."""
from fractions import Fraction
import random

def frontier(N, a):
    k = (a.numerator * N) // a.denominator
    theta = a * N - k
    if theta == 0:
        return k, Fraction(0, 1)
    c = (Fraction(N, 1) - Fraction(k, 1) / a) / (N - k)
    return k, c

def check_nonlattice(N, a):
    k, c = frontier(N, a)
    assert 0 < k < N
    assert c > 0
    assert c < 1 / a
    vals = [1 / a] * k + [c] * (N - k)
    assert sum(vals) == N
    assert min(vals) == c
    assert all(v >= 1 / a for v in vals[:k])
    assert all(v < 1 / a for v in vals[k:])

    rng = random.Random(N * 10007 + a.numerator * 101 + a.denominator)
    q = N - k
    for _ in range(20):
        inc = [Fraction(rng.randint(0, 3), 100000) for _ in range(k)]
        extra = sum(inc)
        raw = [rng.randint(1, 10) for _ in range(q)]
        total = sum(raw)
        tail = [c - extra * Fraction(w, total) for w in raw]
        if min(tail) <= 0:
            continue
        vals2 = [Fraction(1, 1) / a + d for d in inc] + tail
        assert sum(vals2) == N
        assert min(vals2) <= c
        assert all(v >= 1 / a for v in vals2[:k])
        assert all(v < 1 / a for v in vals2[k:])

def check_lattice(N, a):
    k, c = frontier(N, a)
    assert c == 0
    assert a * N == k
    vals = [1 / a] * k + [Fraction(0, 1)] * (N - k)
    assert sum(vals) == N

cases = [
    (11, Fraction(1, 5)),
    (17, Fraction(1, 10)),
    (23, Fraction(3, 20)),
    (37, Fraction(13, 100)),
    (51, Fraction(1, 5)),
    (101, Fraction(1, 10)),
    (29, Fraction(7, 25)),
    (41, Fraction(9, 50)),
]
for N, a in cases:
    if a * N == int(a * N):
        check_lattice(N, a)
    else:
        check_nonlattice(N, a)

lattice_cases = [
    (10, Fraction(1, 5)),
    (20, Fraction(1, 10)),
    (25, Fraction(1, 5)),
    (40, Fraction(3, 20)),
]
for N, a in lattice_cases:
    check_lattice(N, a)

print("VERIFY_OK")
