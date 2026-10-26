#!/usr/bin/env python3
"""Finite independent enumeration of quasi-kernels in directed circulant powers."""
from itertools import combinations
from math import comb

def predicted(n,k):
    out={}
    for s in range(1,n+1):
        lo,hi=k+1,2*k+1
        if not s*lo<=n<=s*hi: continue
        # ordered bounded compositions, with inclusion-exclusion
        rem=n-s*lo; width=k+1
        a=sum((-1)**j*comb(s,j)*comb(rem-j*width+s-1,s-1)
              for j in range(s+1) if rem-j*width>=0)
        assert (n*a)%s==0
        out[s]=n*a//s
    return out

def actual(n,k):
    arcs=[{(v+d)%n for d in range(1,k+1)} for v in range(n)]
    reach=[set(arcs[v])|{w for y in arcs[v] for w in arcs[y]}|{v} for v in range(n)]
    out={}
    for mask in range(1,1<<n):
        S=[i for i in range(n) if mask>>i&1]
        if any(w in arcs[v] for v,w in combinations(S,2)) or any(v in arcs[w] for v,w in combinations(S,2)):
            continue
        coverage=set().union(*(reach[v] for v in S))
        if len(coverage)!=n:continue
        out[len(S)]=out.get(len(S),0)+1
    return out

cases=0
for n in range(3,15):
    for k in range(1,n):
        if k>=n:continue
        p=predicted(n,k);a=actual(n,k)
        assert a==p,(n,k,a,p)
        cases+=1
print('VERIFY_OK exhaustive_circulant_cases='+str(cases))
