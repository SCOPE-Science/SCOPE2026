#!/usr/bin/env python3
"""Independent exact-arithmetic checks for a three-habitat binary environment theorem."""
from fractions import Fraction as F
from itertools import product
from math import comb, log


def masses(p,q,r):
    return [1-3*p+3*q-r,3*(p-2*q+r),3*(q-r),r]

def range_r(p,q):
    return max(F(0),2*q-p),min(q,1-3*p+3*q)

def growth(l,h):
    return [l+(h-l)*F(k,3) for k in range(4)]

checks=0
for pp in range(13):
 p=F(pp,12)
 for qq in range(13):
  q=F(qq,12)
  lo,hi=range_r(p,q)
  if lo>hi:continue
  for r in {lo, hi, (lo+hi)/2}:
   ms=masses(p,q,r)
   assert min(ms)>=0 and sum(ms)==1
   assert sum(F(k,3)*ms[k] for k in range(4))==p
   assert sum(F(k*(k-1),6)*ms[k] for k in range(4))==q
   assert ms[3]==r
   for k in range(4):
    # Each of the choose(3,k) labeled configurations has identical weight.
    assert F(ms[k],comb(3,k))>=0
   checks+=7
  for l,h in [(F(1,30),F(10,3)),(F(1,4),F(4)),(F(2,3),F(7,5))]:
   g=growth(l,h)
   D=g[3]*g[1]**3-g[0]*g[2]**3
   assert D==F((h-l)**3*(h+l),27)
   assert D>0
   def gain(r):return sum(float(m)*log(float(gg)) for m,gg in zip(masses(p,q,r),g))
   if hi>lo:assert gain(hi)>gain(lo)
   checks+=3

l,h=F(1,30),F(10,3)
g=growth(l,h)
p,q=F(1,2),F(1,4)
assert range_r(p,q)==(F(0),F(1,4))
assert masses(p,q,F(0))==[F(1,4),F(0),F(3,4),F(0)]
assert masses(p,q,F(1,4))==[F(0),F(3,4),F(0),F(1,4)]
assert g==[F(1,30),F(17,15),F(67,30),F(10,3)]
assert g[0]*g[2]**3==F(300763,810000)<1
assert g[1]**3*g[3]==F(9826,2025)>1
assert l*h==F(1,9)<1
checks+=7
print('PASS:',checks,'exact identities/feasibility checks plus sampled logarithmic orderings; general proof remains analytic.')
