#!/usr/bin/env python3
"""Exact independent small-case checks of maximal outer-visibility sets of rook graphs."""
from collections import Counter
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def s2(n, k):
    if (n, k) == (0, 0): return 1
    if n < 2 or k <= 0 or 2*k > n: return 0
    return k*s2(n-1,k) + (n-1)*s2(n-2,k-1)

def falling(n,k):
    return factorial(n)//factorial(n-k)

def direct_outer(m,n,mask):
    # Every pair having at least one vertex in S must admit a geodesic
    # with no internal vertex in S. For nonadjacent rook cells the only
    # geodesics have the two distinct cross corners as alternative centers.
    for i in range(m):
        for j in range(n):
            if not (mask >> (i*n+j)) & 1: continue
            for k in range(m):
                if k == i: continue
                for l in range(n):
                    if l == j: continue
                    if ((mask >> (i*n+l)) & 1) and ((mask >> (k*n+j)) & 1):
                        return False
    return True

def structural_starforest(m,n,mask):
    # Separate test using connected components of the row-column graph.
    adj=[[] for _ in range(m+n)]
    for i in range(m):
        for j in range(n):
            if (mask >> (i*n+j)) & 1:
                adj[i].append(m+j); adj[m+j].append(i)
    seen=set()
    for x in range(m+n):
        if x in seen: continue
        q=[x]; seen.add(x); k=0
        for u in q:
            k+=len(adj[u])
            for v in adj[u]:
                if v not in seen: seen.add(v); q.append(v)
        e=k//2
        if e and max(len(adj[u]) for u in q)!=e: return False
    return True

def classified_maximal(m,n,mask):
    if not structural_starforest(m,n,mask):return False
    rd=[sum((mask>>(i*n+j))&1 for j in range(n)) for i in range(m)]
    cd=[sum((mask>>(i*n+j))&1 for i in range(m)) for j in range(n)]
    if all(rd) and all(cd):return True
    if any(d==0 for d in rd) and all(cd):
        return all(d == 0 or d >= 2 for d in rd) and all(d==1 for d in cd)
    if any(d==0 for d in cd) and all(rd):
        return all(d == 0 or d >= 2 for d in cd) and all(d==1 for d in rd)
    return False

def maximal_direct(m,n,mask):
    if not direct_outer(m,n,mask):return False
    return all(not direct_outer(m,n,mask | (1<<k)) for k in range(m*n) if not ((mask>>k)&1))

@lru_cache(None)
def A(m,n):
    if m==0 and n==0:return {0:1}
    if not m or not n:return {}
    ans=Counter()
    for b in range(1,n+1):
        for d,t in A(m-1,n-b).items():ans[d+b]+=comb(n,b)*t
    for a in range(2,m+1):
        for d,t in A(m-a,n-1).items():ans[d+a]+=n*comb(m-1,a-1)*t
    return dict(ans)

def formula(m,n):
    out=Counter(A(m,n))
    out[n]+=sum(falling(m,s)*s2(n,s) for s in range(1,min(m-1,n//2)+1))
    out[m]+=sum(falling(n,t)*s2(m,t) for t in range(1,min(n-1,m//2)+1))
    return {d:a for d,a in out.items() if a}

def min_count(m,n):
    if m>n:m,n=n,m
    base=sum(falling(n,k)*s2(m,k) for k in range(1,m//2+1))
    if m==n:return factorial(m)+2*base
    return base

mask_checks=0
cases=[(m,n) for m in range(2,5) for n in range(2,5)]+[(2,5),(3,5)]
for m,n in cases:
    counts=Counter()
    for mask in range(1<<(m*n)):
        v=direct_outer(m,n,mask)
        assert v==structural_starforest(m,n,mask),(m,n,mask,'starforest')
        mx=maximal_direct(m,n,mask)
        assert mx==classified_maximal(m,n,mask),(m,n,mask,'maximal')
        if mx:counts[mask.bit_count()]+=1
        mask_checks+=1
    actual=dict(counts)
    expected=formula(m,n)
    assert actual==expected,(m,n,actual,expected)
    assert min(actual)==min(m,n),(m,n,'minimum cardinality')
    assert actual[min(m,n)]==min_count(m,n),(m,n,'minimum count')
    print('EXHAUSTIVE',m,n,'all_subsets',1<<(m*n),'maximal_profile',sorted(actual.items()))
for m in range(2,13):
    for n in range(2,13):
        assert formula(m,n)==formula(n,m),(m,n,'symmetry')
        assert min(formula(m,n))==min(m,n),(m,n,'degree floor')
        assert formula(m,n)[min(m,n)]==min_count(m,n),(m,n,'minimum count identity')
print('OK mask_checks=',mask_checks,'analytic_parameter_checks=',121)
