#!/usr/bin/env python3
"""Exact rational replay of a four-stake Bernoulli upper-tail formula."""
from fractions import Fraction as F
from math import comb

def sharp(p, t):
    q = 1-p
    if t <= F(1,4): return 1-q**4
    if t <= F(1,3): return 1-q**3
    if t <= F(1,2): return 1-q**2
    if t <= F(2,3): return max(p, 3*p*p-2*p*p*p)
    return p

def direct(w,p,t):
    q=1-p
    return sum((p**mask.bit_count())*(q**(4-mask.bit_count()))
               for mask in range(16)
               if sum(w[i] for i in range(4) if mask&(1<<i)) >= t)

def equal_stakes(k):
    return tuple([F(1,k)]*k+[F(0)]*(4-k))

# Each weight grid includes every nonnegative integer composition of the denominator.
# Finite grids are replay checks only, not certificates for a continuum theorem.
pvals=[F(1,8),F(1,4),F(3,10),F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(3,4),F(9,10),F(1)]
tvals=sorted(set(F(i,24) for i in range(1,25)) |
             {F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(31,100),F(61,100),F(99,100)})
cases=0
for den in (4,6,8,12):
    for a in range(den+1):
        for b in range(den-a+1):
            for c in range(den-a-b+1):
                w=tuple(F(x,den) for x in (a,b,c,den-a-b-c))
                for p in pvals:
                    q=1-p
                    prob_by_count=[p**j*q**(4-j) for j in range(5)]
                    for t in tvals:
                        if p>t: continue
                        wins=[0]*5
                        for mask in range(16):
                            if sum(w[i] for i in range(4) if mask&(1<<i)) >= t:
                                wins[mask.bit_count()]+=1
                        val=sum(wins[j]*prob_by_count[j] for j in range(5))
                        upper=sharp(p,t)
                        assert val<=upper,(den,w,p,t,val,upper)
                        cases+=1

for p,t,k in [
 (F(1,8),F(1,4),4),
 (F(3,10),F(31,100),3),
 (F(1,3),F(1,3),3),
 (F(2,5),F(1,2),2),
 (F(3,5),F(3,5),3),
 (F(3,5),F(2,3),3),
 (F(2,5),F(2,3),1),
 (F(3,4),F(3,4),1),
 (F(1),F(1),1)]:
    assert direct(equal_stakes(k),p,t)==sharp(p,t)

p=F(3,5);t=F(3,5)
assert direct(equal_stakes(3),p,t)==F(81,125)
assert direct(equal_stakes(1),p,t)==F(3,5)
print(f"VERIFY_OK cases={cases} example_majority={F(81,125)}")
