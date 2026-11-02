#!/usr/bin/env python3
"""Exact small-degree consistency tests for an arithmetic signature theorem.
Requires Python 3 and SymPy. This finite computation is not a proof for all degrees.
"""
from math import gcd
import sympy as sp

T=sp.symbols('T')
examples=0
for d in range(2,19):
    for e in ([1,-4] if d % 2 else [1]):
        P=sp.Poly(3*T**d-3*T-e,T)
        reciprocal=sp.Poly(e*T**d+3*T**(d-1)-3,T)
        assert all(int(reciprocal.nth(k))%3==0 for k in range(d))
        assert int(reciprocal.nth(0))%9 != 0 and e%3 != 0
        expected=2 if d%2==0 else (3 if e==1 else 1)
        actual=sp.polys.polytools.count_roots(P,-sp.oo,sp.oo)
        assert actual == expected, (d,e,actual,expected)
        if e==1 and d%2:
            assert P.eval(-1)<0<P.eval(sp.Rational(-1,2))
            assert P.eval(sp.Rational(-1,2))>0>P.eval(0)
            assert P.eval(0)<0<P.eval(2)
        elif e==1:
            assert P.eval(-1)>0>P.eval(0)
            assert P.eval(1)<0<P.eval(2)
        else:
            assert P.eval(-2)<0<P.eval(0)
        examples += 1

pair_cases=0
for A in range(1,7):
    for B in range(A+1,9):
        if gcd(A,B)!=1: continue
        H=T**A-T**B
        for c in [sp.Rational(1,1000), -sp.Rational(1,1000)]:
            count=sp.polys.polytools.count_roots(sp.Poly(H-c,T),-sp.oo,sp.oo)
            if A%2 and B%2:
                expect=3
            elif A%2==0 and B%2:
                expect=3 if c>0 else 1
            else:
                expect=2
            assert count==expect,(A,B,c,count,expect)
            pair_cases += 1
print(f'VERIFY_OK degrees=2..18 signature_examples={examples} trinomial_root_cases={pair_cases} eisenstein_exact=yes')
