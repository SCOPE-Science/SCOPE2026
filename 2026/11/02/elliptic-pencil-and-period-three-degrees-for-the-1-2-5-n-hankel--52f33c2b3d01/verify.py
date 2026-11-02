#!/usr/bin/env python3
"""Exact finite cross-checks of the recurrence/elimination identities.

Uses SymPy. The theorem for all n follows from the mathematical proof,
not from the finite range verified by this program.
"""
import sympy as sp
S,P,T=sp.symbols('S P T')
for b,c in [(sp.Integer(2),sp.Integer(3)),(sp.Integer(3),sp.Integer(7))]:
    F=P**2-(S**2+2*b*S)*P+b*S**3-c
    disc=sp.discriminant(F,P)
    assert sp.expand(disc-(S**4+4*b*b*S*S+4*c))==0
    assert sp.gcd(sp.Poly(disc,S),sp.Poly(sp.diff(disc,S),S)).degree()==0
    a=[sp.Integer(1),b]
    for j in range(2,13):
        a.append(sp.rem(sp.expand(S*a[-1]-P*a[-2]),F,P).expand())
    assert sp.expand(a[4]-c)==0
    for n in range(6,13):
        poly=sp.Poly(sp.resultant(F,a[n-1]-T,P),S)
        predicted=2*n-7 if n%3==2 else 2*n-6
        assert poly.degree()==predicted, (b,c,n,poly.degree(),predicted)
        assert sp.gcd(poly,poly.diff()).degree()==0, (b,c,n)
print('VERIFY_OK')
