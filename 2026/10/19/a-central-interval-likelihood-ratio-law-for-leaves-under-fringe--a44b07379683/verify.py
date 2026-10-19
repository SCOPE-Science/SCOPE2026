#!/usr/bin/env python3
"""Exact enumeration and arithmetic checks for plane-tree leaf/fringe Palm law."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb

@lru_cache(None)
def trees(n):
    if n == 1: return ((),)
    # Ordered lists of positive-size subtrees whose total size is n-1.
    @lru_cache(None)
    def forests(s):
        if s == 0: return ((),)
        return tuple((t,)+f for a in range(1,s+1) for t in trees(a) for f in forests(s-a))
    return forests(n-1)

@lru_cache(None)
def size(t): return 1+sum(size(c) for c in t)
@lru_cache(None)
def leaf(t): return 1 if not t else sum(leaf(c) for c in t)
@lru_cache(None)
def count(t,tau): return int(t==tau)+sum(count(c,tau) for c in t)

def catalan(q):return comb(2*q,q)//(q+1)
def narayana_leaf_counts(n):
    if n == 1: return {1:1}
    return {j:comb(n-1,j)*comb(n-1,j-1)//(n-1) for j in range(1,n)}

def exact_delta(n,k,ell):
    m=n-k+1
    if m==1:return Fraction(ell,1)-Fraction(n,2)
    return Fraction(ell,1)-Fraction(k+1,2)+Fraction(m-2,2*(2*m-3))

cnt=0
for n in range(2,11):
    sample=trees(n)
    assert len(sample)==catalan(n-1)
    histogram=Counter(leaf(t) for t in sample)
    assert dict(histogram)==narayana_leaf_counts(n)
    for k in range(2,min(n,5)+1):
        m=n-k+1
        lower=narayana_leaf_counts(m)
        # all distinct shapes tau, exhaustive in size<=5
        for tau in trees(k):
            ell=leaf(tau)
            palm=Counter()
            total=0
            weighted_leaf=0
            for t in sample:
                v=count(t,tau)
                if v:
                    palm[leaf(t)]+=v
                    total+=v
                    weighted_leaf+=v*leaf(t)
            expected=Counter({j+ell-1:j*ways for j,ways in lower.items()})
            assert palm==expected,(n,k,tau,palm,expected)
            assert sum(palm.values())==total
            assert Fraction(weighted_leaf,total)-Fraction(sum(leaf(t) for t in sample),len(sample)) == exact_delta(n,k,ell)
            # likelihood-ratio log-concavity on the full (unconditional) support
            ratios={r:Fraction(palm[r]*len(sample),total*histogram[r]) for r in histogram}
            for r in range(2,n-1):
                assert ratios[r]**2 >= ratios[r-1]*ratios[r+1],(n,k,tau,r)
            upper=[r for r in ratios if ratios[r]>1]
            if upper: assert max(upper)-min(upper)+1==len(upper)
            cnt+=1
print('PASS: all plane trees n=2..10, all fringe patterns size 2..min(n,5);', cnt, 'pattern/sample comparisons')
# Strict ratio decrease for parameters beyond enumerated sizes.
num_ratio_tests=0
for k in range(2,75):
 for ell in range(1,k):
  s=ell-1;t=k-ell
  for m in range(4,90):
   vals=[]
   for j in range(1,m-1):
    A=m-j
    vals.append(Fraction((A-1)*A*(j+s)*(j+s+1), (A+t-1)*(A+t)*j*j))
   assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))
   num_ratio_tests+=1
print('PASS: strictly decreasing adjacent Palm likelihood ratios for',num_ratio_tests,'(k, leaf, m) parameter triples')
