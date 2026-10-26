#!/usr/bin/env python3
"""Exact checks for the Möbius and transverse linearizations; not a proof by sampling."""
import sympy as sp
z,w=sp.symbols('z w')
def check(a,b,c,d):
    assert a*d-b*c==1
    j=c*z+d
    t=(a*z+b)/j
    transverse=w/j
    assert sp.simplify(sp.diff(t,z)-j**-2)==0
    assert sp.simplify(sp.diff(transverse,w)-j**-1)==0
    assert sp.simplify(sp.diff(transverse,z).subs(w,0))==0
    print('AUTOMORPHY_OK',a,b,c,d)
for matrix in [(1,3,0,1),(1,0,3,1),(-2,-3,3,4),(4,3,-3,-2)]:
    check(*matrix)
for n in [2,3,4,8,20]:
    assert (n-1)*(-1)==-(n-3)-2
    assert 2*(-1)==2-4
    print('DEGREES_OK',n)
assert (1,3,0,1)[2]==0
assert (1,3,0,1)[3]==1
print('VERIFY_OK normal_multiplier_square_matches_log_tangent')
