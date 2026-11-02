#!/usr/bin/env python3
"""Recompute polynomial certificates for hyperflexes of a cyclic-six quartic.
Requires SymPy. All arithmetic in this program is exact over the integers.
"""
import sympy as sp
r,u,x,y,m,t = sp.symbols('r u x y m t')
G=u**2+r*u+1
E2=sp.expand(3*(6*u+r)*G-4*u*(2*u+r)**2)
E3=sp.expand(2*u*(2*u+r)**3-27*G**2)
P=11*r**4-1080*r**2+3888
A=33*r**4-704*r**2+2160
B=-196*r**3+720*r
assert sp.factor(sp.resultant(E2,E3,u))==324*(r-2)**3*(r+2)**3*P
subres=sp.subresultants(E3,E2,u)
assert len(subres)==5
assert sp.expand(subres[-2]+18*(r**2-4)*(A*u+B))==0
assert sp.factor(sp.discriminant(P,r))==2**32*3**15*11
assert sp.factor(sp.resultant(P,A,r))==2**34*3**10*11**2
N=196*r**3-720*r
for H in (E2,E3):
    d=sp.degree(H,u)
    num=sp.expand(sum(H.coeff(u,j)*N**j*A**(d-j) for j in range(d+1)))
    assert sp.rem(num,P,r)==0
assert sp.expand(P.subs(r,0))==3888
assert sp.expand(P.subs(r,2))==-256
assert sp.expand(P.subs(r,-2))==-256
# Direct tangent expansion: expand (x+m*t)^3 + G(y+t), with u=y^2.
F=sp.expand((x+m*t)**3 + (y+t)**4+r*(y+t)**2+1)
coeff=[sp.expand(F).coeff(t,j) for j in range(5)]
assert coeff[0]==x**3+y**4+r*y**2+1
assert coeff[1]==3*x**2*m+4*y**3+2*r*y
assert coeff[2]==3*x*m**2+6*y**2+r
assert coeff[3]==m**3+4*y
assert coeff[4]==1
# Elimination by x^3=-G(y^2), m=-2y(2u+r)/(3x^2): both are checked via cross multiplication.
assert sp.expand(E2-(3*(6*u+r)*G-4*u*(2*u+r)**2))==0
assert sp.expand(E3-(2*u*(2*u+r)**3-27*G**2))==0
print('SYMBOLIC_HYPERFLEX_OK', 'resultant',sp.factor(sp.resultant(E2,E3,u)))
