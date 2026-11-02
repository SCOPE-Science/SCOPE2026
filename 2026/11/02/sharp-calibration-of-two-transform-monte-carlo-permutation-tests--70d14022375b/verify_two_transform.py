#!/usr/bin/env python3
"""Exact finite-orbit enumeration and binomial checks of unanchored two-transform p-values."""
from fractions import Fraction as Q
from itertools import permutations, product
from math import comb

def cdf(M,a,k):
    return sum(Q(comb(M,j))*a**j*(1-a)**(M-j) for j in range(k+1))

checks=0
for h in range(2,7):
  delta=Q(h-1,h)
  for ranks in permutations(range(h)):
    desc=sum(ranks[x]>ranks[(x+1)%h] for x in range(h))
    assert desc<=h-1;checks+=1
    for M in range(1,5):
      for a in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
        # independent exact enumeration of all start states, iid transformation draws
        masses=[Q(0) for _ in range(M+2)]
        for x in range(h):
          for bits in product((0,1),repeat=M):
            # bit 0=e with probability a; bit 1=g with probability 1-a
            n_id=bits.count(0)
            prob=a**n_id*(1-a)**(M-n_id)/h
            ge=sum((ranks[x]>=ranks[x] if bit==0 else ranks[(x+1)%h]>=ranks[x]) for bit in bits)
            masses[ge+1]+=prob
        assert sum(masses)==1;checks+=1
        for k in range(1,M+1):
          actual=sum(masses[:k+1])
          expected=Q(desc,h)*cdf(M,a,k-1)
          assert actual==expected and actual<=delta*cdf(M,a,k-1)
          checks+=1
  # ranking strictly decreasing along 0->1->...->h-1 attains h-1 descents
  ranks=tuple(h-1-i for i in range(h))
  assert sum(ranks[x]>ranks[(x+1)%h] for x in range(h))==h-1
  checks+=1

# M=1 is valid at a=27/100, M=2 is invalid at 1/3, for cycles of length three.
a=Q(27,100);delta=Q(2,3)
assert delta*(1-a)<=Q(1,2)
assert delta*(1-a)**2>Q(1,3)
checks+=2
# Uniform validity if a>=delta follows from a binomial size-bias identity.
for h in range(2,30):
 delta=Q(h-1,h)
 for M in range(1,35):
  for k in range(1,M+1):
   assert delta*cdf(M,delta,k-1)<=Q(k,M+1)
   checks+=1
print('PASSED',checks,'deterministic exact checks')
