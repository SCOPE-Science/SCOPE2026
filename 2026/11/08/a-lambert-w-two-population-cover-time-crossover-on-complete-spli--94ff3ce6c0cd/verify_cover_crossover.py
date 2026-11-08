#!/usr/bin/env python3
"""Standalone small-case and asymptotic checks for a two-class walk cover limit."""
from fractions import Fraction as F
import mpmath as mp
import sympy as sp

checks=0

# An exact identity for the eigenvalue equation at z=1.
A,B,K,L=sp.symbols('A B K L',positive=True)
u=(A-K-1)/(A+B-1)
v=(B-L)/(A+B-1)
w=(A-K)/A
assert sp.factor(1-u-v*w-(A*K+A*L+B*K-K*L)/(A*(A+B-1)))==0
checks+=1
# First-order derivatives of the dominant root at an empty forbidden set.
z=sp.symbols('z')
f=z*z-u*z-v*w
f_z=sp.diff(f,z)
for variable, wanted in ((K,-(1+B/A)/(A+2*B-1)),(L,-1/(A+2*B-1))):
    derivative=-sp.diff(f,variable)/f_z
    assert sp.factor(derivative.subs({K:0,L:0,z:1})-wanted)==0
    checks+=1

def survive_reduced(a,b,k,l,start,t):
    den=a+b-1
    u=F(a-k-1,den);v=F(b-l,den);w=F(a-k,a)
    x,y=(F(1),F(0)) if start=='A' else (F(0),F(1))
    for _ in range(t):
        x,y=x*u+y*w,x*v
    return x+y

def survive_full(a,b,removed,start,t):
    verts=list(range(a+b))
    probs={start:F(1)}
    for _ in range(t):
        update={}
        for i,p in probs.items():
            if i<a:
                nbrs=[j for j in verts if j!=i]
            else:
                nbrs=list(range(a))
            for j in nbrs:
                if j in removed:continue
                update[j]=update.get(j,F(0))+p/F(len(nbrs))
        probs=update
    return sum(probs.values(),F(0))

for a in range(3,7):
 for b in range(2,6):
  for start in (0,a):
   for k in range(0,min(2,a-1)+1):
    for l in range(0,min(2,b-1)+1):
     A=[j for j in range(a) if j!=start][:k]
     B=[j for j in range(a,a+b) if j!=start][:l]
     if len(A)!=k or len(B)!=l: continue
     for t in (0,1,2,5):
      got=survive_full(a,b,set(A+B),start,t)
      expected=survive_reduced(a,b,k,l,'A' if start<a else 'B',t)
      assert got==expected,(a,b,start,k,l,t,got,expected)
      checks+=1

mp.mp.dps=65
for a in (10**4,10**6,10**8,10**10):
 L=mp.log(a); w0=mp.lambertw(L); b=int(mp.floor(a*w0/L));c=mp.mpf(b)/a
 eta=mp.log(a)-(1+c)*mp.log(b)
 assert abs(eta)<.4
 checks+=1
 den=mp.mpf(a+b-1)
 for k,l in ((1,0),(0,1),(1,1),(2,0),(0,2),(2,1)):
  u=(a-k-1)/den;v=(b-l)/den;z=mp.mpf(a-k)/a
  disc=mp.sqrt(u*u+4*v*z)
  lp=(u+disc)/2;ln=(u-disc)/2
  pplus=((u+v-ln)/(lp-ln))*mp.power(lp,(a+2*b-1)*mp.log(b))
  mom=mp.rf(a-1-k+1,k)*mp.rf(b-l+1,l)*pplus
  # avoiding all k+l choices, factorial moments near e^(k eta)
  target=mp.exp(k*eta)
  assert abs(mom/target-1)<mp.mpf('0.018'),(a,b,k,l,mom,target)
  checks+=1
print('VERIFY_OK',checks,'assertions')
