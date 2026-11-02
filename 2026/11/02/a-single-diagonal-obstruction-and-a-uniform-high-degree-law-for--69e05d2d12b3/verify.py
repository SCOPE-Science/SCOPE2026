#!/usr/bin/env python3
"""Independent checks for exact [3/3] Padé positivity on complete bipartite diffusion networks.
Run: python verify.py (requires sympy; numpy for finite floating checks).
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

z=sp.symbols('z')
num=120-60*z+12*z**2-z**3
den=120+60*z+12*z**2+z**3
r=sp.factor(num/den)
phi=sp.factor((1-r)/z)
assert sp.simplify(sp.diff(r,z)+24*(z**4-30*z**2+600)/den**2)==0
assert sp.simplify(sp.diff(phi,z)+2*(z**4+120*z**2+1200*z+3600)/den**2)==0
# Taylor series order six of the matrix-exponential stability function.
assert sp.series(r-sp.exp(-z),z,0,7).removeO()==0
print('3 scalar symbolic identities PASS')

checks=0
for p in range(1,6):
 for q in range(p,7):
  n=p+q
  L=sp.zeros(n)
  for i in range(p):
   for j in range(p,n):
    L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
  I=sp.eye(n)
  for h in [sp.Rational(1,7),sp.Rational(1,2),sp.Rational(3,2),sp.Rational(11,3)]:
   E=(120*I-60*h*L+12*h*h*L*L-h**3*L**3)*(120*I+60*h*L+12*h*h*L*L+h**3*L**3).inv()
   rq=r.subs(z,h*q);rp=r.subs(z,h*p);rn=r.subs(z,h*n)
   diagA=sp.Rational(1,n)+sp.Rational(q,p*n)*rn+sp.Rational(p-1,p)*rq
   diagB=sp.Rational(1,n)+sp.Rational(p,q*n)*rn+sp.Rational(q-1,q)*rp
   cross=(1-rn)/n
   for i in range(n):
    for j in range(n):
     if i<p and j<p:
      v=diagA if i==j else sp.Rational(1,n)+sp.Rational(q,p*n)*rn-rq/p
     elif i>=p and j>=p:
      v=diagB if i==j else sp.Rational(1,n)+sp.Rational(p,q*n)*rn-rp/q
     else:v=cross
     assert sp.factor(E[i,j]-v)==0,(p,q,h,i,j,v,E[i,j])
     checks+=1
print('exact matrix entries checked',checks,'PASS')

def R(t):return (120-60*t+12*t*t-t**3)/(120+60*t+12*t*t+t**3)
def dA(p,q,t):
 N=p+q
 return 1/N+q/(p*N)*R(N*t)+(p-1)/p*R(q*t)
def dB(p,q,t):
 N=p+q
 return 1/N+p/(q*N)*R(N*t)+(q-1)/q*R(p*t)
def root(p,q):
 lo=0.;hi=1.
 while dA(p,q,hi)>0:hi*=2
 for j in range(80):
  md=(lo+hi)/2
  if dA(p,q,md)>0:lo=md
  else:hi=md
 return (lo+hi)/2

def direct_matrix(p,q,t):
 n=p+q
 L=np.zeros((n,n))
 for i in range(p):
  for j in range(p,n):
   L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
 I=np.eye(n)
 return np.linalg.solve(120*I+60*t*L+12*t*t*(L@L)+t**3*(L@L@L),
                       120*I-60*t*L+12*t*t*(L@L)-t**3*(L@L@L))

tests=0
for p in range(1,8):
 for q in range(p,13):
  if p+q<3:continue
  H=root(p,q)
  assert 0< H <math.inf
  assert dA(p,q,.999*H)>0 and dA(p,q,1.001*H)<0
  for t in [H*.01,H*.5,H*.999,H*1.001,H*1.5]:
   E=direct_matrix(p,q,t)
   assert np.max(np.abs(E.sum(axis=1)-1))<2e-11
   O=E.copy();np.fill_diagonal(O,1.)
   assert O.min()>-2e-11
   if t < H: assert E.min()>-2e-11,(p,q,t,E.min())
   else:assert E.min() < -1e-8,(p,q,t,E.min())
   assert abs(E[0,0]-dA(p,q,t))<4e-11
   assert dB(p,q,t)+1e-12 >=dA(p,q,t)
   tests+=1
print('numerical timestep checks',tests,'PASS')

z0=float(sp.nroots(num)[0]); assert abs(R(z0))<1e-12
for q in [100,400,1600,6400]:
 for p in [1,2,max(1,q//3),q]:
  ratio=q*root(p,q)
  assert abs(ratio-z0)<100/q,(p,q,ratio,z0)
print('uniform high-order boundary test PASS; scalar root',repr(z0))
print('ALL CHECKS PASS')
