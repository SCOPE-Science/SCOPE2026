#!/usr/bin/env python3
"""Exact identities for the K3 quotient of the Fermat quintic."""
from sympy import symbols, Matrix, Rational, expand
u,v,z,w,t=symbols('u v z w t')
assert expand(16*(((u+v)/2)**5+((u-v)/2)**5) -(u**5+10*u**3*v**2+5*u*v**4))==0
F=u**5+10*u**3*t+5*u*t**2+16*z**5+16*w**5
assert expand(F.subs(u,0)-16*(z**5+w**5))==0
assert F.diff(u).subs({u:0,z:0,w:0,t:1})==5
assert Rational(4*5,2)==10
assert (5-1)*(5-2)//2==6
M=Matrix([[-2,1,1,1,1,1],
          [1,-2,0,0,0,0],
          [1,0,-2,0,0,0],
          [1,0,0,-2,0,0],
          [1,0,0,0,-2,0],
          [1,0,0,0,0,-2]])
assert M.det()==-16
h=Matrix([5,2,2,2,2,2])
assert list(M*h)==[0,1,1,1,1,1]
assert (h.T*M*h)[0]==10
print('FERMAT_QUINTIC_K3_STAR_EXACT_OK')
