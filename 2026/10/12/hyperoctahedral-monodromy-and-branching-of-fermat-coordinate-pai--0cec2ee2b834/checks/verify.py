#!/usr/bin/env python3
"""Exact finite sanity checks for an all-degree binomial monodromy theorem.

The mathematical proof for all d uses cyclotomic roots of unity, not enumeration.
"""
from math import comb
from sympy import Poly, discriminant, diff, gcd, symbols

u, v = symbols("u v")
for d in range(4, 26):
    m = d // 2
    p = sum(2 * comb(d, 2 * j) * u**j for j in range(m + 1))
    assert Poly(p, u).degree() == m
    assert p.subs(u, 0) == 2
    critical_values = Poly(discriminant(p - v, u), v)
    assert critical_values.degree() == m - 1
    assert gcd(critical_values, critical_values.diff()).degree() == 0
    assert gcd(Poly(p - 2, u), Poly(diff(p, u), u)).degree() == 0
    assert Poly(p.subs(u, u**2), u).degree() == 2 * m
print("VERIFY_OK")
