#!/usr/bin/env python3
"""Exact small-modulus ambiguity checks for a geometric cyclic STFT window.

Requires Python 3 and SymPy. Exact cyclotomic arithmetic covers every
translation and modulation in dimensions 2 through 12. Floating-point
cross-checks test the stated exceptional signal fibers and added probe;
these checks are not a substitute for the proof for arbitrary dimensions.
"""
import cmath
from math import pi
import sympy as sp

X = sp.Symbol('X')
checks = 0
for n in range(2, 13):
    phi = sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
    expected = {(n // 2, ell) for ell in range(1, n, 2)} if n % 2 == 0 else set()
    zeros = set()
    for k in range(n):
        for ell in range(n):
            a = sp.Poly(sum(2 ** (j + (j-k) % n) * X ** ((-ell*j) % n)
                            for j in range(n)), X, domain=sp.ZZ)
            if a.rem(phi).is_zero:
                zeros.add((k, ell))
            # Clear the r^{-k} term from the exact geometric-sum identity.
            lhs = 2**k * a * sp.Poly(1 - 4*X**((-ell) % n), X, domain=sp.ZZ)
            rhs = sp.Poly((1-2**n)*(2**n + 2**(2*k)*X**((-ell*k) % n)),
                          X, domain=sp.ZZ)
            assert (lhs - rhs).rem(phi).is_zero, (n, k, ell)
            checks += 1
    assert zeros == expected, (n, sorted(zeros), sorted(expected))
    checks += 1
print(f'Exact cyclotomic zero classification and closed-form checks: {checks} passed')


def stft_powers(x, r=2.0):
    n = len(x)
    g = [r**j for j in range(n)]
    return [[abs(sum(x[j]*g[(j-m) % n]*cmath.exp(-2j*pi*ell*j/n)
                     for j in range(n)))**2
             for ell in range(n)] for m in range(n)]


def extra_power(x):
    h = len(x)//2
    return abs(sum(x[:h])+1j*sum(x[h:]))**2

for n in range(2, 12, 2):
    h = n//2
    for j in range(h):
        x = [0j]*n
        y = [0j]*n
        x[j]=y[j]=1+0j
        x[j+h]=2+3j
        y[j+h]=2-3j
        ax=stft_powers(x)
        ay=stft_powers(y)
        assert max(abs(ax[m][ell]-ay[m][ell]) for m in range(n)
                   for ell in range(n)) < 1e-5
        assert abs(extra_power(x)-extra_power(y)) > 1
        checks += 2
print(f'All tests including exceptional pairs and one-probe completion: {checks} passed')
