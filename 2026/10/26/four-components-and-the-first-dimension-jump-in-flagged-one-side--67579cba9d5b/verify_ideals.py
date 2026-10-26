#!/usr/bin/env python3
"""Symbolic verification of component decomposition. Requires sympy>=1.12."""
import sympy as s
x,y,z,p,h,r,t=s.symbols('x y z p h r t')
V=[x,y,z,p,h,r]
I=[x*p,z*r,x*h+y*r]
P1=[x,r]
P2=[p,h,r]
P3=[x,y,z]
P4=[z,p,x*h+y*r]
def intersection(A,B,modulus=None):
    opts={'order':'lex'}
    if modulus is not None:opts['modulus']=modulus
    G=s.groebner([t*a for a in A]+[(1-t)*b for b in B],t,*V,**opts)
    return [f.as_expr() for f in G.polys if not f.as_expr().has(t)]
def equality(A,B,modulus=None):
    opts={'order':'lex'}
    if modulus is not None:opts['modulus']=modulus
    ga=s.groebner(A,*V,**opts)
    gb=s.groebner(B,*V,**opts)
    return all(ga.reduce(f)[1]==0 for f in B) and all(gb.reduce(f)[1]==0 for f in A)
for modulus in (None,2,3,5):
    J=intersection(P1,P2,modulus)
    J=intersection(J,P3,modulus)
    J=intersection(J,P4,modulus)
    assert equality(J,I,modulus)
    print('radical_intersection_equal',modulus if modulus else 'QQ')
print('VERIFY_OK_PRIMARY_INTERSECTION_N4')
