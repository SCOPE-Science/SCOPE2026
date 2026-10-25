#!/usr/bin/env python3
"""Exact characteristic-three verification of a smooth cubic net.

Requires SymPy 1.10+; computes over GF(3), not floating point.
"""
from itertools import product
import sympy as sp

X, Y, Z = sp.symbols('X Y Z')
F = -X**3 + X*Z**2 + Y**2*Z
G = X**3 - X**2*Z + Y*Z**2 + X*Y**2
H = Z**3 - X**2*Y + Y**2*Z - Y**3
POLYS = (F,G,H)
PARAMETERS = tuple(t for t in product(range(3),repeat=3)
                   if any(t) and next(c for c in t if c) == 1)
assert len(PARAMETERS) == 13

def unit_on_chart(polys, chart):
    coordinates = [t for t in (X,Y,Z) if t != chart]
    forms = [sp.expand(p.subs(chart,1)) for p in polys]
    gb = sp.groebner(forms,*coordinates,modulus=3,order='lex')
    return list(gb) == [sp.Integer(1)]

for chart in (X,Y,Z):
    assert unit_on_chart(POLYS,chart), 'geometric base locus is not empty'
print('base_locus: empty on all 3 projective charts')
for abc in PARAMETERS:
    P = sp.expand(sum(a*f for a,f in zip(abc,POLYS)))
    for chart in (X,Y,Z):
        vars2 = [t for t in (X,Y,Z) if t != chart]
        f = sp.expand(P.subs(chart,1))
        assert unit_on_chart([f,sp.diff(f,vars2[0]),sp.diff(f,vars2[1])],chart), (abc,chart)
    pts = [(1,i,j) for i,j in product(range(3), repeat=2)]
    pts += [(0,1,i) for i in range(3)] + [(0,0,1)]
    N = sum(int(P.subs({X:x,Y:y,Z:z})%3 == 0) for x,y,z in pts)
    print('%s smooth N=%d' % (abc,N))
print('PASS: all 13 rational projective cubics geometrically smooth; basepoint free')
