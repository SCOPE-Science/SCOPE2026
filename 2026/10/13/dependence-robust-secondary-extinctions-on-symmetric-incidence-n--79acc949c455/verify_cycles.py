#!/usr/bin/env python3
"""Finite exact checks of deterministic cycle edge profiles and orbit witnesses.
The unrestricted result follows from the proof, not this finite enumeration.
"""
from fractions import Fraction
from itertools import product

def cycle_edges(mask,n):
    return sum((mask>>i&1) * (mask>>((i+1)%n)&1) for i in range(n))

def low(n,s):
    return max(0,2*s-n)

def rotation(mask,n,k):
    return sum(((mask>>i)&1) << ((i+k)%n) for i in range(n))

def analytic(n,q):
    if not n%2:
        return n*max(Fraction(0),2*q-1)
    k=n//2
    if n*q<=k: return Fraction(0)
    if n*q<=k+1: return n*q-k
    return n*(2*q-1)

for n in range(3,13):
    profiles={s:[] for s in range(n+1)}
    for mask in range(1<<n):
        s=mask.bit_count()
        profiles[s].append(cycle_edges(mask,n))
        assert cycle_edges(mask,n)>=low(n,s)
    for s,vals in profiles.items():
        assert min(vals)==low(n,s),(n,s,min(vals))
        mask=next(mask for mask in range(1<<n) if mask.bit_count()==s and cycle_edges(mask,n)==low(n,s))
        orbit=[rotation(mask,n,k) for k in range(n)]
        assert sum(Fraction(sum((z>>v)&1 for z in orbit),n) for v in range(n))==s
        assert all(sum((z>>v)&1 for z in orbit)==s for v in range(n))
        assert Fraction(sum(cycle_edges(z,n) for z in orbit),n)==low(n,s)
    for a in range(101):
        q=Fraction(a,100)
        # Convex-hull lower bound from every pair of discrete cardinalities.
        candidates=[]
        target=n*q
        for s in range(n+1):
            for t in range(s,n+1):
                if not s<=target<=t: continue
                if s==t:
                    if target==s:candidates.append(Fraction(low(n,s)))
                else:
                    w=(target-s)/Fraction(t-s)
                    candidates.append((1-w)*low(n,s)+w*low(n,t))
        assert min(candidates)==analytic(n,q),(n,q,min(candidates),analytic(n,q))
print('VERIFY_OK cycles=3..12 all_binary_subsets=8184 marginal_grid=101 exact_profiles_and_orbit_achievability=1')
