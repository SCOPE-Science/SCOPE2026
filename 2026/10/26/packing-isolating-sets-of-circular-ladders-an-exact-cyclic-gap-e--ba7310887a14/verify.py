#!/usr/bin/env python3
"""Independent enumeration of packing-isolating vertex sets in cycle prisms."""
from collections import Counter
from math import comb
from itertools import combinations

def graph(n):
    N=2*n
    adj=[0]*N
    for i in range(n):
        for r in (0,1):
            v=2*i+r
            for w in (2*((i-1)%n)+r,2*((i+1)%n)+r,2*i+1-r):
                adj[v]|=1<<w
    return adj

def count_exhaustive(n, collect=False):
    adj=graph(n)
    N=2*n
    forb=[0]*N
    for v in range(N):
        a=adj[v]
        b=a|(1<<v)
        while a:
            w=(a&-a).bit_length()-1
            b|=adj[w]
            a&=a-1
        forb[v]=b
    count=Counter()
    accepted=set() if collect else None
    def dfs(pos,sel,banned,dom):
        if pos==N:
            rem=((1<<N)-1)&~dom
            for v in range(N):
                if rem & (1<<v) and adj[v]&rem:
                    return
            count[sel.bit_count()]+=1
            if collect: accepted.add(sel)
            return
        dfs(pos+1,sel,banned,dom)
        if not (banned>>pos)&1:
            dfs(pos+1,sel|(1<<pos),banned|forb[pos],dom|adj[pos]|(1<<pos))
    dfs(0,0,0,0)
    return count, accepted

def masks_via_gap_words(n):
    """Construct all predicted sets via a separate cyclic-gap description."""
    out=set()
    for k in range(2,n//2+1,2):
        for cols in combinations(range(n),k):
            ds=[(cols[(j+1)%k]-cols[j])%n for j in range(k)]
            if all(d in (2,3) for d in ds):
                for startrow in (0,1):
                    out.add(sum(1<<(2*c+((startrow+j)%2)) for j,c in enumerate(cols)))
    return out

def formula(n):
    c=Counter()
    for k in range(2,n//2+1,2):
        r=n-2*k
        if 0<=r<=k:
            total=2*n*comb(k,r)
            assert total%k==0
            c[k]+=total//k
    return c

if __name__=='__main__':
    for n in range(3,22):
        a, actual=count_exhaustive(n, collect=(n<=14))
        b=formula(n)
        assert a==b,(n,a,b)
        if actual is not None:
            predicted=masks_via_gap_words(n)
            assert actual==predicted,(n,len(actual),len(predicted))
        print(f'n={n} k_counts={dict(sorted(a.items()))} total={sum(a.values())}')
    # Independent formal-series recurrence over 120 coefficients.
    totals=[0]*121
    for n in range(1,121):
        totals[n]=sum(formula(n).values())
        rhs=(totals[n-4] if n>=4 else 0)+(2*totals[n-5] if n>=5 else 0)+(totals[n-6] if n>=6 else 0)
        numerator={4:4,5:10,6:6}.get(n,0)
        assert totals[n]==rhs+numerator,(n,totals[n],rhs+numerator)
    print('RECURRENCE_120_OK')
    print('VERIFY_OK')
