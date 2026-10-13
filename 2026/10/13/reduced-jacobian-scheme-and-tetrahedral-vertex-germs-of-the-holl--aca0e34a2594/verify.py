#!/usr/bin/env python3
"""Exact algebraic checks for the Jacobian scheme of the hollow 4-by-4 determinant."""
import itertools
from math import comb
import sympy as sp

a,b,c,d,e,f,w=sp.symbols('a b c d e f w')
M=sp.Matrix([[0,a,b,c],[a,0,d,e],[b,d,0,f],[c,e,f,0]])
F=sp.expand(M.det())
assert sp.expand(F-(a*a*f*f+b*b*e*e+c*c*d*d-2*a*b*e*f-2*a*c*d*f-2*b*c*d*e))==0
Fa=sp.expand(F.subs(a,1))
assert sp.expand(Fa.subs(f,w+b*e+c*d)-(w*w-4*b*c*d*e))==0
J=[sp.diff(Fa,v) for v in [b,c,d,e,f]]
expected=[-4*c*d*e,-4*b*d*e,-4*b*c*e,-4*b*c*d,0]
for der,rem in zip(J,expected):
    assert sp.expand(der.subs(f,w+b*e+c*d).subs(w,0)-rem)==0
assert sp.expand(J[-1].subs(f,w+b*e+c*d)-2*w)==0
# The squarefree cubic ideal is the intersection of the six pair-coordinate ideals.
vs=[b,c,d,e]
for deg in range(0,9):
    monomials=[z for exponent in itertools.product(range(deg+1),repeat=4) if sum(exponent)==deg for z in [exponent]]
    is_not_zero=lambda ex:sum(v>0 for v in ex)<=2
    good=sum(is_not_zero(ex) for ex in monomials)
    calc=1 if deg==0 else (4 if deg==1 else 6*deg-2)
    assert good==calc,(deg,good,calc)
    # Verify a monomial vanishes in the squarefree cubic ideal iff it vanishes
    # under restriction to every coordinate two-plane.
    for ex in monomials:
        in_ideal=sum(v>0 for v in ex)>=3
        vanishes_every_pair=all(any(ex[k]>0 for k in range(4) if k not in pair)
                                for pair in itertools.combinations(range(4),2))
        assert in_ideal==vanishes_every_pair
print('DET_IDENTITY_OK')
print('AFFINE_JACOBIAN_GENERATORS_OK')
print('SQUAREFREE_PRIMARY_INTERSECTION_DEGREES_0_TO_8_OK')
print('HILBERT_SERIES=(1+2t+3t^2)/(1-t)^2')
print('LOCAL_HILBERT_SAMUEL_MULTIPLICITY=6')
print('VERIFY_OK')
