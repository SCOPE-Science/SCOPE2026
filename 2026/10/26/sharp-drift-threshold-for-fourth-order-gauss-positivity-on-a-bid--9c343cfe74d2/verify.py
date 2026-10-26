"""Exact reproducibility checks for two-stage Gauss positivity on a biased 4-cycle.

Run with Python 3 and SymPy (see requirements.txt). This script tests rational
identities and finite illustrations; the all-parameter signs use the proof.
"""
from fractions import Fraction
from itertools import product
from sympy import Matrix, I, Rational, Poly, symbols, conjugate, im, re, cancel, expand, factor, simplify

a,b,h=symbols('a b h', positive=True)
s=a+b
R=lambda z:(12+6*z+z*z)/(12-6*z+z*z)
D=2*(s*s*h*h+3*s*h+3)*((a*a+b*b)**2*h**4+6*s*(a*a+b*b)*h**3+(18*(a*a+b*b)+24*a*b)*h*h+36*s*h+36)
N0=(216+216*s*h+72*(a*a+4*a*b+b*b)*h*h+144*a*b*s*h**3
+6*(a*a+4*a*b+b*b)**2*h**4+3*s*(a*a+b*b)*(3*a*a+4*a*b+3*b*b)*h**5+2*s*s*(a*a+b*b)**2*h**6)
N2=3*h*h*(a*a+b*b)*(36+36*s*h+12*s*s*h*h+s*(a*a+4*a*b+b*b)*h**3)
Fa=(216*a+216*a*s*h+36*(2*a**3+5*a*a*b+2*a*b*b+b**3)*h*h
+36*b*s*(a*a+b*b)*h**3+3*s*(a*a+b*b)*(3*b*b-a*a)*h**4)
Fb=(216*b+216*b*s*h+36*(a**3+2*a*a*b+5*a*b*b+2*b**3)*h*h
+36*a*s*(a*a+b*b)*h**3+3*s*(a*a+b*b)*(3*a*a-b*b)*h**4)
Ns=[N0,h*Fa,N2,h*Fb]
r=R(-s*h+I*(a-b)*h)
r2=R(-2*s*h)
forms=[(1+r2+2*re(expand(r,complex=True)))/4,
       (1-r2+2*im(expand(r,complex=True)))/4,
       (1+r2-2*re(expand(r,complex=True)))/4,
       (1-r2-2*im(expand(r,complex=True)))/4]
for i,(e,n) in enumerate(zip(forms,Ns)):
 assert cancel(e-n/D)==0, f'Fourier identity failed for shift {i}'
print('SYMBOLIC_OK 4 Fourier-to-polynomial rational identities')
# Exact direct rational-matrix checks, varying the rate asymmetry and timestep.
P=Matrix(4,4,lambda i,j:int(j==(i+1)%4))
for A,B,H in product([Rational(1,3),Rational(1,1),Rational(2,1),Rational(4,1)],
                      [Rational(1,4),Rational(1,1),Rational(3,1)],
                      [Rational(1,20),Rational(1,2),Rational(1,1),Rational(3,1),Rational(10,1)]):
 Q=A*(P-Matrix.eye(4))+B*(P.T-Matrix.eye(4))
 Z=H*Q
 M=(12*Matrix.eye(4)+6*Z+Z**2)*(12*Matrix.eye(4)-6*Z+Z**2).inv()
 for k in range(4):
  assert cancel(M[0,k]-Ns[k].subs({a:A,b:B,h:H})/D.subs({a:A,b:B,h:H}))==0,(A,B,H,k)
 assert all(sum(M.row(i))==1 for i in range(4))
print('VERIFY_OK 4 symbolic identities; 240 exact direct-matrix entries; 60 stochastic row checks')
