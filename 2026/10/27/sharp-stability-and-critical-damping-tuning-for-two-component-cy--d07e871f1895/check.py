#!/usr/bin/env python3
"""Reproduce exact period-map identities and numerical boundary/rate checks."""
from fractions import Fraction as Q
from math import sqrt, isclose
import cmath

def mul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mat(a,b,h):
    P=[[1-h*a,-h*b],[1,0]]
    R=[[1-h*b,-h*a],[1,0]]
    return mul(R,P)
def rho(a,b,h):
    t=1-2*(a+b)*h+a*b*h*h
    d=a*b*h*h
    root=cmath.sqrt(t*t-4*d)
    return max(abs((t+root)/2),abs((t-root)/2))
def optimum(a,b):
    S=a+b+sqrt(a*b)
    return 1/(S+sqrt(S*S-a*b))

count=0
for a in (Q(1,3),Q(1),Q(2),Q(7,2),Q(13)):
 for b in (Q(1,7),Q(1),Q(3),Q(8)):
  for h in (Q(1,100),Q(1,5),Q(2,3),Q(3,2)):
   T=mat(a,b,h)
   tr=T[0][0]+T[1][1]
   det=T[0][0]*T[1][1]-T[0][1]*T[1][0]
   assert tr==1-2*(a+b)*h+a*b*h*h
   assert det==a*b*h*h
   assert 1+tr+det==2*(1-a*h)*(1-b*h)
   assert 1-tr+det==2*h*(a+b)
   count+=1
for a in (.2,.7,1.,3.,9.):
 for b in (.3,.8,1.,4.,11.):
  star=optimum(a,b)
  ceiling=1/max(a,b)
  assert 0<star<ceiling
  target=sqrt(a*b)*star
  assert isclose(rho(a,b,star),target,rel_tol=2e-7,abs_tol=1e-7)
  for s in (.001,.01,.25,.5,.9,.999):
   assert rho(a,b,s*star)>target*(1+1e-12)
  for s in (1.001,1.05,1.5,2,3,9):
   assert rho(a,b,s*star)>target*(1+1e-12)
  for s in (.001,.5,.999):
   assert rho(a,b,s*ceiling)<1
  for s in (1.001,1.1,2,10):
   assert rho(a,b,s*ceiling)>1-1e-9
assert abs(optimum(1,1)-(3-2*sqrt(2)))<1e-13
print('CHECK_OK exact rational cases:',count, 'numerical parameter pairs:',25)
