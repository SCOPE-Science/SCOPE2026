#!/usr/bin/env python3
"""Independent finite enumeration and integer algebra checks for partial orientation-preserving idempotents."""
from itertools import product
from collections import Counter
from math import comb

def cyclic(seq):
    if len(seq)<2: return True
    return sum(seq[j]>seq[(j+1)%len(seq)] for j in range(len(seq)))<=1

def count_brute(n):
    # -1 stands for undefined; all defined inputs are scanned in their natural order.
    h=Counter()
    for mapping in product(range(-1,n),repeat=n):
        dom=[i for i,v in enumerate(mapping) if v>=0]
        images=[mapping[i] for i in dom]
        if any(mapping[i] not in dom or mapping[mapping[i]] !=mapping[i] for i in dom): continue
        if not cyclic(images): continue
        h[(len(dom),len(set(images)))]+=1
    return h

def rank_full(m,k):
    if m==0:return int(k==0)
    if k==1:return m
    if 2<=k<=m:
        num=m*comb(m+k-1,m-k)
        assert num%k==0
        return num//k
    return 0

def direct_formula(n):
    return Counter({(m,k):comb(n,m)*rank_full(m,k) for m in range(n+1) for k in range(m+1) if rank_full(m,k)})

def closed_recurrence(n):
    # S_m(u) = lambda(u)^m+lambda(u)^(-m): S_0=2,S_1=2+u,S_m=(2+u)S_(m-1)-S_(m-2).
    p0=[2]; p1=[2,1]
    if n==0:return [1]
    for m in range(2,n+1):
        p=[0]*(m+1)
        for k,v in enumerate(p1): p[k]+=2*v; p[k+1]+=v
        for k,v in enumerate(p0):p[k]-=v
        p0,p1=p1,p
    p1[0]-=2
    p1[1]-=n*(n-1)
    return p1

def verify():
    cases=0
    for n in range(1,7):
        observed=count_brute(n)
        predicted=direct_formula(n)
        assert observed==predicted,(n, observed, predicted)
        cases+=1
    for n in range(1,51):
        counts=[0]*(n+1)
        for (m,k),v in direct_formula(n).items():counts[k]+=v
        # Cross-check closed bivariate polynomial via binomial transform of Chebyshev-like recurrence.
        via=[0]*(n+1)
        via[0]=1
        for m in range(1,n+1):
            full=closed_recurrence(m)
            for k,c in enumerate(full): via[k]+=comb(n,m)*c
        assert via==counts, (n,via,counts)
        cases+=1
    print('VERIFY_OK:',cases,'enumeration and exact polynomial checks')

if __name__=='__main__': verify()
