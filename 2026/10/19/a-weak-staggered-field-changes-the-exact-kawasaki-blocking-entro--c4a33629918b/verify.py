#!/usr/bin/env python3
"""Exact checks for the weak staggered-field Kawasaki blocking polynomial.

Requires Python >=3.9 and sympy.  No random sampling is used.
The analytic proof is given separately; these finite computations are checks.
"""
from itertools import product
from fractions import Fraction
import sympy as sp

spins = tuple(product((-1, 1), repeat=3))
labels = {s: k for k, s in enumerate(spins)}
z, x, t = sp.symbols('z x t')


def allowed(a, b, c, d, parity):
    if b == c:
        return True
    wall_energy = b*(a-d)
    return wall_energy > 0 or (wall_energy == 0 and (-1)**parity*b > 0)


def transfer(parity, weight=z):
    a = sp.zeros(8)
    for first, mid, last in spins:
        for fourth in (-1, 1):
            if allowed(first, mid, last, fourth, parity):
                a[labels[(first, mid, last)], labels[(mid, last, fourth)]] += (
                    weight if mid == 1 else 1
                )
    return a

T = transfer(0)*transfer(1)
f = x**5-(1+z**2)*x**4-(z+z**2+z**3)*x**3-z**5
assert sp.expand(T.charpoly(x).as_expr()-x**3*f) == 0
D = 1-(1+z**2)*t-(z+z**2+z**3)*t**2-z**5*t**5
assert sp.expand((sp.eye(8)-t*T).det()-D) == 0


def direct_energy(config, h):
    n = len(config)
    bond = -sum(config[i]*config[(i+1) % n] for i in range(n))
    field = -h*sum((-1)**i*config[i] for i in range(n))
    return bond+field


def blocked(config, h):
    n = len(config)
    en = direct_energy(config, h)
    for i in range(n):
        j = (i+1) % n
        if config[i] == config[j]:
            continue
        other = list(config)
        other[i], other[j] = other[j], other[i]
        if direct_energy(other, h) < en:
            return False
    return True


def brute_polynomial(n, h):
    cs = [0]*(n+1)
    for conf in product((-1, 1), repeat=n):
        if blocked(conf, h):
            cs[sum(v == 1 for v in conf)] += 1
    return sum(value*z**k for k, value in enumerate(cs))

# Two independently specified methods: complete energy comparisons and
# local four-spin transfer graph; use two different weak positive fields.
for n in (4, 6, 8, 10, 12):
    exact = sp.expand(sp.trace(T**(n//2)))
    low = sp.expand(brute_polynomial(n, Fraction(1, 7)))
    high = sp.expand(brute_polynomial(n, Fraction(9, 10)))
    assert exact == low == high, (n, exact, low, high)
    print('n=', n, 'count=', exact.subs(z,1), 'magnetization polynomial PASS')

# New and old no-field states differ even at the smallest physical length.
assert sp.trace(T**2).subs(z, 1) == 10

# Exact quintic and rational-series checks, with no numerical approximation.
G = ((1+z**2)*t + 2*(z+z**2+z**3)*t**2+5*z**5*t**5)/D
for m in range(1, 9):
    assert sp.expand(sp.series(G,t,0,m+1).removeO().coeff(t,m)
                     - sp.trace(T**m)) == 0
print('matrix, determinant, rational generator and brute force checks PASS')
