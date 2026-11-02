"""Exact finite-state checks for stochastically rounded damped rotation.

Rational matrix calculations verify stationarity, flux and spectral polynomial.
The analytic proof establishes the parameter-uniform identities and limit.
"""
from fractions import Fraction as F
from itertools import product
from math import log, isclose

S=[(-1,-1),(-1,1),(1,1),(1,-1)]

def mat(c,h):
    a=1-h;b=h*c
    def prob(u,v):
        m1=a*u[0]+b*u[1]
        m2=-b*u[0]+a*u[1]
        return ((1+v[0]*m1)*(1+v[1]*m2))/4
    return [[prob(u,v) for v in S] for u in S]

count=0
for num in range(1,20):
 c=F(num,22)
 for den in range(2,30):
  h=F(1,den)
  if not 0<h<F(1)/(1+c):continue
  p=mat(c,h)
  assert all(sum(row)==1 and all(v>0 for v in row) for row in p)
  assert all(sum(p[i][j] for i in range(4))==1 for j in range(4))
  a=1-h;b=h*c
  for i,u in enumerate(S):
   f1=sum(p[i][j]*v[0] for j,v in enumerate(S))
   f2=sum(p[i][j]*v[1] for j,v in enumerate(S))
   f12=sum(p[i][j]*v[0]*v[1] for j,v in enumerate(S))
   assert f1==a*u[0]+b*u[1]
   assert f2==-b*u[0]+a*u[1]
   assert f12==(a*a-b*b)*u[0]*u[1]
  p_plus=h*(1+c)*(2-h*(1-c))/4
  p_minus=h*(1-c)*(2-h*(1+c))/4
  for i in range(4):
   j=(i+1)%4
   assert p[i][j]==p_plus
   assert p[j][i]==p_minus
   assert (p[i][j]-p[j][i])/4==h*c/4
  for i in range(2):
   j=i+2
   assert p[i][j]==p[j][i]
  ent=0.
  for i in range(4):
   for j in range(4):
    ent+=float(p[i][j])/4*log(float(p[i][j])/float(p[j][i]))
  assert isclose(ent,float(h*c)*log(float(p_plus/p_minus)),rel_tol=1e-9,abs_tol=1e-13)
  assert a*a+b*b<1 and abs(a*a-b*b)<1
  count+=1
print(f'VERIFY_OK {count} exact rational four-state transition systems, plus entropy calculations')
