#!/usr/bin/env python3
"""Exact symbolic replay for the symmetry-fixed dual futile-cycle Jacobian."""
import sympy as sp

A,E,U2,U3,B,H,V5,V6,z = sp.symbols('A E U2 U3 B H V5 V6 z')
G = sp.Matrix([
    [0,0,-U3,0,V6,0],
    [0,0,0,V6,0,-U3],
    [A,0,-A-E-U2-U3,-E,0,0],
    [-B,-B,-H,-B-H-V5-V6,-B,0],
    [-B,-B,0,-B,-B-H-V5-V6,-H],
    [0,A,0,0,-E,-A-E-U2-U3],
])
# Columns are q+,u+,v+,q-,u-,v-, with q±=Q1±Q2, u±=U±X, v±=V±Y.
P = sp.Matrix([
    [1,0,0,1,0,0],
    [1,0,0,-1,0,0],
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,1,0,0,-1],
    [0,1,0,0,-1,0],
])
T = sp.simplify(P.inv()*G*P)
assert T[:3,3:] == sp.zeros(3)
assert T[3:,:3] == sp.zeros(3)
Gp, Gm = T[:3,:3], T[3:,3:]
expected_p = sp.Matrix([
    [0,-U3,V6],
    [A,-A-E-U2-U3,-E],
    [-2*B,-H,-2*B-H-V5-V6],
])
expected_m = sp.Matrix([
    [0,-U3,-V6],
    [A,-A-E-U2-U3,-E],
    [0,-H,-H-V5-V6],
])
assert Gp == expected_p and Gm == expected_m
cp = sp.Poly((z*sp.eye(3)-Gp).det(), z).all_coeffs()
cm = sp.Poly((z*sp.eye(3)-Gm).det(), z).all_coeffs()
Delta = U3*(H+V5+V6)-H*V6
assert sp.expand(cm[3]-A*Delta) == 0
vars_ = (A,E,U2,U3,B,H,V5,V6)
def positive_coefficients(expr):
    p=sp.Poly(sp.expand(expr), *vars_)
    return len(p.terms()), min(p.coeffs())
# Cubic Hurwitz margins. Exact expansion must have only positive coefficients.
np,minp = positive_coefficients(cp[1]*cp[2]-cp[3])
nm,minm = positive_coefficients(cm[1]*cm[2]-cm[3])
assert minp > 0 and minm > 0
# The plus cubic has strictly positive coefficients.
for c in cp[1:]:
    assert min(sp.Poly(sp.expand(c), *vars_).coeffs()) > 0
# The minus cubic has positive first two coefficients and constant A*Delta.
for c in cm[1:3]:
    assert min(sp.Poly(sp.expand(c), *vars_).coeffs()) > 0
# Full determinant has the sign of Delta because the plus constant is positive.
assert sp.expand(G.det() - cp[3]*cm[3]) == 0
print('plus_hurwitz_margin_terms=', np)
print('minus_hurwitz_margin_terms=', nm)
print('minus_constant_factor=', sp.factor(cm[3]))
print('det_factor=', sp.factor(G.det()))
print('VERIFY_OK')
