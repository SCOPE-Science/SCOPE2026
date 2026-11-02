#!/usr/bin/env python3
"""Exact polynomial identities for the rational-tangent fibre theorem."""
import sympy as S
x,y,t=S.symbols('x y t')
z=1-x-y
xx=(x,y,z)
e2=x*y+y*z+z*x
e3=x*y*z
A=9*e2-27*e3-2
B=27*e3-3*e2
D=[t+3*(1-t)*v for v in xx]
N=S.expand(sum(xx[i]*D[(i+1)%3]*D[(i+2)%3] for i in range(3))-S.prod(D))
assert S.expand(N+t*(t-1)*(A*t+B))==0
u,v=S.symbols('u v')
w=-u-v
sub={x:(u+1)/3,y:(v+1)/3}
s2=u*v+v*w+w*u
s3=u*v*w
assert S.simplify(A.subs(sub)+s3)==0
assert S.simplify(B.subs(sub)-(S.Rational(2,3)*s2+s3))==0
assert S.simplify((A+B).subs(sub)-S.Rational(2,3)*s2)==0
r=S.symbols('r')
s=-2*(r*r+r+1)/(3*r*(r+1))
assert S.factor((S.Rational(2,3)*s2+s3).subs({u:s,v:r*s}))==0
for f,target in [(s+1,(r-1)*(r+2)),(r*s+1,(r-1)*(2*r+1)),(-(1+r)*s+1,(r+2)*(2*r+1))]:
 assert S.factor(f).as_numer_denom()[0].equals(S.factor(target)) or S.factor(f).as_numer_denom()[0].equals(-S.factor(target))
print('EXACT_TANGENT_FIBRE_CUBIC_AND_EXCEPTIONAL_STRATA_OK')
