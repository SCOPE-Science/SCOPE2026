#!/usr/bin/env python3
"""Finite checks for uniform nonzero rank-one masking over prime fields."""

from fractions import Fraction
from itertools import product
import cmath
import math


def rank_mod_p(flat, n, p):
    a = [list(flat[i*n:(i+1)*n]) for i in range(n)]
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, n) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % p, -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(n):
            if i != r and a[i][c] % p:
                f = a[i][c] % p
                a[i] = [(a[i][j] - f * a[r][j]) % p for j in range(n)]
        r += 1
    return r


def outer(u, v, p):
    return tuple((x*y) % p for x in u for y in v)


def dot_h(flat, n, s, p):
    return sum(flat[i*n+i] for i in range(s)) % p


def lambda_formula(q, n, s):
    N = q**n
    return Fraction(q**(2*n-s) - 2*N + 1, (N-1)**2)


def direct_prime_check(p, n=3):
    vecs = [v for v in product(range(p), repeat=n) if any(v)]
    masks = {outer(u, v, p) for u in vecs for v in vecs}
    expected = (p**n - 1)**2 // (p - 1)
    assert len(masks) == expected
    assert all(rank_mod_p(m, n, p) == 1 for m in masks)
    omega = cmath.exp(2j * math.pi / p)
    for s in range(1, n+1):
        empirical = sum(omega ** dot_h(m, n, s, p) for m in masks) / len(masks)
        exact = float(lambda_formula(p, n, s))
        assert abs(empirical.imag) < 1e-10
        assert abs(empirical.real - exact) < 1e-10
    return expected


def symbolic_checks():
    qs = [2, 3, 4, 5, 7, 8, 9, 11, 16]
    count = 0
    for q in qs:
        for n in range(3, 11):
            vals = [lambda_formula(q, n, s) for s in range(1, n+1)]
            assert all(vals[s] < vals[s-1] for s in range(1, len(vals)))
            assert vals[-1] == Fraction(-1, q**n - 1)
            assert vals[0] >= abs(vals[-1])
            target = Fraction(q**(2*n-1) - 2*q**n + 1, (q**n - 1)**2)
            assert vals[0] == target
            assert Fraction(1, q) - target == Fraction((q-1)*(2*q**n-1), q*(q**n-1)**2)
            count += 1
    return count


if __name__ == "__main__":
    counts = {p: direct_prime_check(p) for p in (2, 3, 5)}
    symbolic = symbolic_checks()
    print("direct rank-one shell checks:", counts)
    print("symbolic parameter checks:", symbolic)
    print("PASS")
