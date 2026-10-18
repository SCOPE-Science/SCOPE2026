"""Numerical reproducibility for the high-server critical reset crossover.
The exact proof (in RESULT.md) is required for all-dimensional quantifiers.
"""
from math import sqrt,log,log1p,exp
from scipy.optimize import brentq
import numpy as np

def lc(v):return float(np.logaddexp(v,-v)-np.log(2))

def crossing(c,L=2.,D=1.,mu=1.):
 C=c*mu*L*L/D
 assert C>2.5
 x=(2*D/(c*mu))/(L+sqrt(L*L-2*D/(c*mu)))
 z=x/L
 def q(y):
  k=y/z
  return y+log1p(exp(-2*k))-log1p(exp(-2*(k-y)))-log1p(k*k/C)
 lo=.15*log(C);hi=6*log(C)
 assert q(lo)<0 and q(hi)>0
 y=brentq(q,lo,hi,xtol=1.e-12)
 r=D*(y/x)**2
 assert abs(q(y))<2.e-10
 return C,y,r

tests=0
for L,D,mu in [(2.,1.,1.),(.75,2.,3.),(4.,5.,.4)]:
 previous=None
 for c in [100,1000,10000,100000,1000000,100000000]:
  C,y,r=crossing(c,L,D,mu)
  lead=c*c*mu*mu*L*L/D *log(C)**2
  assert 1.1<r/lead<5
  if previous is not None: assert y>previous
  previous=y
  tests+=3
 # Check coefficient pattern for near threshold and large C.
 for C in [2.51,2.6,3.,5.,20.,100.,10000.]:
  b2=1-2/C;t=1/b2
  vals=[];S=0.
  for n in range(1,300):
   S+=t**(n-1)
   vals.append(S-n*(2*n-1))
   if S>1e100:break
  neg=[i for i,v in enumerate(vals[1:],2) if v<0]
  pos=[i for i,v in enumerate(vals[1:],2) if v>0]
  assert neg and (not pos or max(neg)<min(pos))
  tests+=1
print('PASS:',tests,'assertion groups; root and sign-variation checks')
