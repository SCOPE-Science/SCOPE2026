#!/usr/bin/env python3
"""Exact algebraic consistency checks for the two-site frequency-crossover theorem.

Python 3 standard library only. This tests rational identities and finite examples;
the proof of generality and analytic perturbation limits is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, pi

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def matvec(A,v): return [dot(row,v) for row in A]
def quadratic(A,v): return dot(v,matvec(A,v))

assert F(4,3)*F(3,4)==1
assert 16*F(1,4)*F(1,4)==1
assert F(4,3)*F(3,4)==1
# The normalized Jacobian, input and second-variation matrix.
B=[[F(-16,3),F(12)],[F(4,3),F(-16,3)]]
v=[F(4),F(0)]
H=[[F(-1,42),F(-3,14)],[F(-3,14),F(33,14)]]
assert B[0][0]+B[1][1]==F(-32,3)
detB=B[0][0]*B[1][1]-B[0][1]*B[1][0]
assert detB==F(112,9)
assert H[1][0]==H[0][1]
assert H[0][0]==F(1,7)*F(-1,6)
assert H[1][1]==F(3,7)*F(11,2)
assert H[0][1]==-F(3,14)
adjminusB=[[ -B[1][1], B[0][1]],[B[1][0], -B[0][0]]]
u=matvec(adjminusB,v)
assert u==[F(64,3),F(16,3)]
U=quadratic(H,u)
V=quadratic(H,v)
assert U==F(1408,189)
assert V==F(-8,21)
assert -U/V==F(176,9)
# Denominator in z=9*omega^2: factors (z+16)(z+784)/81.
assert detB**2==F(16*784,81)
assert -2*detB+(B[0][0]+B[1][1])**2==F(16+784,9)
# Cross-multiply rational response expressions for all z (degree two).
# -1/2 * (U+V*z/9) / [ (z+16)(z+784)/81 ]
#     = 12*(z-176)/(7*(z+16)*(z+784)).
assert -F(81,2)*U == -F(12*176,7)
assert -F(81,18)*V == F(12,7)
# The unique maximum is at z=176+192*sqrt(5), since the derivative
# numerator is -z^2+352*z+153344 and has one positive root.
assert 176**2-352*176-153344 == -192**2*5
assert 176 > 0 and 192>0
zstar=176+192*sqrt(5)
q=lambda z:12*(z-176)/(7*(z+16)*(z+784))
assert abs(q(zstar)-(3-sqrt(5))/896)<1e-15
assert q(0)<0<q(9*8.2**2)
assert q(9*3**2)<0<q(9*6**2)
assert q(9*12**2)>0
# g'(x)>0 on [0,1] from 1/pi^2+5/(2*pi)<17/18.
assert 1/pi**2+5/(2*pi)<F(17,18)
# Node curvatures follow from d^2/dx^2 sin^2(4*pi*x)=32*pi^2
# at quarter-integer x. Thus g''(1/4)=-12, g''(3/4)=4.
g2a=F(-3,8)*32; g2b=F(1,8)*32
assert (g2a,g2b)==(F(-12),F(4))
print('PASS: exact rational identities and bounded numerical consistency checks')
