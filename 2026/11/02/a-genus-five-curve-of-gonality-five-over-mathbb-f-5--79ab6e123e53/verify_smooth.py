#!/usr/bin/env python3
"""Geometric smoothness via five exact Jacobian-ideal Groebner certificates."""
import itertools
import sympy as sp
x=sp.symbols('x0:5')
a,b,c,d,e=x
forms=[a*b+c*c+2*d*d,
       4*a*d+b*c+3*d*e+3*e*e,
       a*a+2*b*b+4*c*c+4*d*e]
J=sp.Matrix([[sp.diff(f,v) for v in x] for f in forms])
minors=[sp.expand(J[:,cols].det()) for cols in itertools.combinations(range(5),3)]
assert len(minors)==10
for i in range(5):
    remaining=[x[j] for j in range(5) if j!=i]
    ideal=[sp.expand(f.subs({x[i]:sp.Integer(1)})) for f in forms+minors]
    gb=sp.groebner(ideal,*remaining,modulus=5,order='grevlex')
    assert [p.as_expr() for p in gb.polys]==[sp.Integer(1)],(i,gb)
    print('AFFINE_CHART',i,'JACOBIAN_IDEAL_UNIT')
print('GEOMETRIC_SMOOTHNESS_VERIFY_OK')
