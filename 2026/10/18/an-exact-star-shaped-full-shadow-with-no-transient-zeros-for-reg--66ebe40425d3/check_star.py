#!/usr/bin/env python3
"""Exact supplementary checks of derivative root structure for binomial powers.

Requires SymPy. The finite test range is not an infinite proof.
"""
import sympy as sp

z, u = sp.symbols('z u')
number_checked = 0
for d in range(2, 8):
    for n in range(1, 7):
        base = (z**d - 1)**n
        q_previous = sp.Poly((u - 1)**n, u)
        r_previous = 0
        scalar = 1
        for m in range(d*n):
            raw = sp.Poly(sp.diff(base, z, m), z)
            r = (-m) % d
            assert r == r_previous
            q = sp.Poly(sum(c*u**((e-r)//d) for (e,), c in raw.terms()), u)
            assert all((e-r) % d == 0 for (e,), _ in raw.terms())
            assert q.as_expr() == scalar*q_previous.as_expr()
            expected_degree = (d*n - m - r)//d
            assert q.degree() == expected_degree
            assert q.eval(0) != 0
            endpoint_order = max(n-m, 0)
            reduced = q
            for _ in range(endpoint_order):
                reduced, remainder = reduced.div(sp.Poly(u-1, u))
                assert remainder.is_zero
            assert reduced.eval(1) != 0
            assert reduced.eval(0) != 0
            count = reduced.degree()
            if count:
                assert reduced.count_roots(sp.S.Zero, sp.S.One) == count
                assert sp.gcd(reduced, reduced.diff()).degree() == 0
            number_checked += 1
            if m+1 < d*n:
                if r == 0:
                    assert q_previous.degree() >= 1
                    q_previous = q_previous.diff()
                    scalar *= d
                    r_previous = d-1
                else:
                    q_previous = sp.Poly(r*q_previous.as_expr()+d*u*q_previous.diff().as_expr(), u)
                    r_previous = r-1

assert number_checked == 567
print('PASS: 567 exact descendants; factorization, multiplicity, real-root counts, simplicity, and recurrence.')
