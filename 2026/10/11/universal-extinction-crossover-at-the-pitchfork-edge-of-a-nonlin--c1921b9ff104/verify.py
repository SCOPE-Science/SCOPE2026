#!/usr/bin/env python3
"""Exact rational coefficients for the source SIRS threshold equations.

Only Python standard library is used. This tests exact polynomial identities
for rational parameter families; the analytic theorem proves all parameters.
"""
from fractions import Fraction as F
from math import log

def add(x,y):
 z=dict(x)
 for k,v in y.items(): z[k]=z.get(k,F(0))+v
 return {k:v for k,v in z.items() if v}

def mul(x,y):
 z={}
 for (i,j),u in x.items():
  for (k,l),v in y.items():z[(i+k,j+l)]=z.get((i+k,j+l),F(0))+u*v
 return {k:v for k,v in z.items() if v}

def scale(x,c):return {k:c*v for k,v in x.items() if c*v}

one={(0,0):F(1)};i={(1,0):F(1)};w={(0,1):F(1)}
for p in [
 (F(1),F(1),F(1),F(1),F(1),F(0)),
 (F(1),F(1),F(1),F(1),F(1),F(1,10)),
 (F(2),F(3),F(1,2),F(4),F(5,6),F(1,7)),
 (F(7,3),F(5,4),F(2,3),F(3,2),F(3,7),F(2,5)),
]:
 b,d,gamma,nu,alpha,eps=p
 N0=b/d;lam=d+gamma;rho=d+nu;a=gamma/rho
 k1=lam/N0;k2=(k1*(1+a)-eps)/N0
 assert k2>0 and k1*N0==lam
 kappa=k1*(1+a)-k2*N0
 C=lam*alpha+k2*(1+a);C0=lam*alpha+(k1*(1+a)/N0)*(1+a)
 assert kappa==eps and C==C0-(1+a)*eps/N0
 # (1+alpha*I^2) I'/I from the source system, R=aI+w
 source=add(mul(add(scale(one,k1),scale(i,k2)),add(scale(one,N0),add(scale(i,-(1+a)),scale(w,-1)))),add(scale(one,-lam),scale(mul(i,i),-lam*alpha)))
 reduced=add(add(scale(i,-eps),scale(mul(i,i),-C)),scale(mul(add(scale(one,k1),scale(i,k2)),w),-1))
 assert source==reduced,(source,reduced)
 # exact identity for w'=-(rho-a*B(I))*w+a*D(I) follows from w'=R'-a*I'
 assert rho*a==gamma

# Rational verification of G'(z)=-1/[z^2(1+z)] by analytic
# derivative: -1/z^2 + 1/[z(z+1)] has numerator -(z+1)+z=-1.
assert -(F(5)+1)+F(5)==-1
# For a fixed rational z, equality of transformed differential form:
# G'(C0 I/eps) * (C0/eps) * (C0/eps^2) = -1/[I^2(eps+C0 I)].
for I,eps,C0 in [(F(1,5),F(1,10),F(13,2)),(F(2,7),F(3,5),F(5,3))]:
 z=C0*I/eps
 gprime=-1/(z*z*(1+z))
 lhs=gprime*(C0/eps)*(C0/(eps*eps))
 rhs=-1/(I*I*(eps+C0*I))
 assert lhs==rhs
print('CHECK_OK')
