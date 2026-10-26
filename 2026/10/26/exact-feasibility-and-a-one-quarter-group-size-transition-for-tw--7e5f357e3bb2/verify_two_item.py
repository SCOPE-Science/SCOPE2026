#!/usr/bin/env python3
"""Self-contained checks for two-item signed group EF1 feasibility.
All profiles and group assignments are enumerated from the additive EF1 definition.
"""
from collections import Counter
from itertools import product,combinations
from math import factorial,comb
from fractions import Fraction

TYPES=((1,1),(1,-1),(-1,1),(-1,-1))

def is_ef1(valuations,group,items_one):
    # Explicitly enumerate the two possible bundle removals, not a derived criterion.
    n=len(valuations)
    group=set(group)
    own_goods=set(items_one)
    other_goods={0,1}-own_goods
    for i,v in enumerate(valuations):
        own=own_goods if i in group else other_goods
        other=other_goods if i in group else own_goods
        def score(g):return sum(v[j] for j in g)
        if score(own)>=score(other):continue
        if not any(score(own)>=score(other-{j}) for j in other) and not any(score(own-{j})>=score(other) for j in own):
            return False
    return True

def brute_exists(vals,p):
    n=len(vals)
    for subset in ((),(0,),(1,),(0,1)):
        for group in combinations(range(n),p):
            if is_ef1(vals,group,subset):return True
    return False

def criterion(vals,p):
    freq=Counter(vals)
    return min(freq[t] for t in TYPES) <= min(p,len(vals)-p)

def exact_bad(n,q):
    total=0
    for c0 in range(n+1):
      for c1 in range(n-c0+1):
       for c2 in range(n-c0-c1+1):
        c3=n-c0-c1-c2
        if min(c0,c1,c2,c3)>q:
          total += factorial(n)//(factorial(c0)*factorial(c1)*factorial(c2)*factorial(c3))
    return Fraction(total,4**n)

profiles=0
for n in range(2,8):
    for p in range(1,n):
        for vals in product(TYPES,repeat=n):
            a=brute_exists(vals,p)
            b=criterion(vals,p)
            assert a==b,(n,p,vals,a,b)
            profiles+=1
    print('exhaustive n =',n, 'PASS')
print('total exhaustive labeled (profile,group-size) comparisons',profiles)
for n,q in ((8,1),(9,1),(12,1),(20,2),(100,20)):
    bad=exact_bad(n,q)
    print('exact_bad',n,q,bad,'decimal',float(bad))
assert exact_bad(8,1)==Fraction(315,8192)
assert exact_bad(7,1)==0
assert exact_bad(11,2)==0
assert exact_bad(12,2)>0
# Direct sample check of balanced-and-unbalanced cases at n=8.
for vals in product(TYPES,repeat=8):
  if criterion(vals,7)!= (min(Counter(vals)[t] for t in TYPES)<=1):raise AssertionError
print('All checks passed.')
