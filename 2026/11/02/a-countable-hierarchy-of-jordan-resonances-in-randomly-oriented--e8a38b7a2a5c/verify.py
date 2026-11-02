#!/usr/bin/env python3
"""Reproduce finite-branch coefficient identities and convergence checks for randomly oriented Luroth dynamics."""
from fractions import Fraction as Q
from math import comb
import mpmath as mp

def mult(a,b):
 o=[Q(0)]*(len(a)+len(b)-1)
 for i,aa in enumerate(a):
  for j,bb in enumerate(b):o[i+j]+=aa*bb
 return o

def pwr(a,k):
 o=[Q(1)]
 for _ in range(k): o=mult(o,a)
 return o

def transfer(poly,p,N):
 out=[Q(0)]*len(poly)
 for j in range(2,N+1):
  ell=Q(1,j*(j-1)); c=Q(1,j)+ell/2-Q(1,2)
  for t,coef in enumerate(poly):
   aa=pwr([c,ell],t); bb=pwr([c,-ell],t)
   for k in range(t+1):out[k]+=ell*coef*(p*aa[k]+(1-p)*bb[k])
 return out

def exact():
 count=0
 for N in (3,5,8):
  e=[Q(1,j*(j-1)) for j in range(2,N+1)]
  for d in (1,3,5):
   S=lambda k: sum((l**k for l in e),Q(0))
   q=S(d+2)/S(d+1); p=(1+q)/2; lamb=S(d+2)
   C=sum((Q(1,j*(j-1))**(d+1)*(Q(1,j)+Q(1,2*j*(j-1))-Q(1,2)) for j in range(2,N+1)),Q(0))
   beta=(d+1)*q*C
   f=[Q(0)]*(d+2); f[d+1]=Q(1)
   for k in range(1,5):
    f=transfer(f,p,N)
    assert f[d+1]==lamb**k
    assert f[d]==k*beta*lamb**(k-1), (N,d,k, f[d],k*beta*lamb**(k-1))
    count+=2
 print('exact coefficient assertions:',count)

def infinity():
 mp.mp.dps=60
 ls=[mp.mpf(1)/(j*(j-1)) for j in range(2,300)]
 ss=lambda k:mp.fsum([ell**k for ell in ls]); cs=lambda k:mp.fsum([ell**k*(mp.mpf(1)/j+ell/2-mp.mpf(1)/2) for j,ell in enumerate(ls,2)])
 ps=[]
 for d in range(1,16,2):
  p=(1+ss(d+2)/ss(d+1))/2; ps.append(p)
  assert 0.5<p<0.75 and cs(d+1)>0
  print('d',d,'p',mp.nstr(p,17),'C',mp.nstr(cs(d+1),12))
 assert all(ps[i]<ps[i+1] for i in range(len(ps)-1))
 print('infinite numerical checks done')
if __name__=='__main__':
 exact(); infinity()
