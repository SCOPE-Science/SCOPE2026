#!/usr/bin/env python3
"""Direct brute-force census of strong domination after one vertex deletion."""
from math import comb

def polypred(n):
    h=[0]*(2*n)
    for k in range(n):h[n-1+k]+=comb(n-1,k)   # no distinguished B
    h[n]+=1                                # distinguished B, no A
    for k in range(n-1):h[3+k]+=(n-1)*comb(n-2,k) # B0, A_i, B_i
    for a in range(2,n):
        for k in range(n):h[1+a+k]+=comb(n-1,a)*comb(n-1,k)
    return h

def direct(n):
    # Graph has A_1,...,A_{n-1},B_0,...,B_{n-1}.
    v=list(range(1,n))+list(range(n,2*n)); inds={x:i for i,x in enumerate(v)}
    N=len(v)
    adj=[0]*N
    for a in range(1,n):
        for b in range(n):
            if a==b:continue
            i,j=inds[a],inds[n+b];adj[i]|=1<<j;adj[j]|=1<<i
    deg=[a.bit_count() for a in adj]
    eligible=[sum(1<<j for j in range(N) if (adj[i]>>j&1) and deg[j]>=deg[i]) for i in range(N)]
    cnt=[0]*(N+1)
    for mask in range(1<<N):
        if all((mask>>i&1) or (mask&eligible[i]) for i in range(N)):
            cnt[mask.bit_count()]+=1
    return cnt

for n in range(3,10):
    d=direct(n);p=polypred(n)
    assert d==p,(n,d,p)
    first=next(i for i,v in enumerate(d) if v)
    print(f'REMOVAL_ALL_SUBSETS_OK n={n} subsets={1<<(2*n-1)} first={first} count={d[first]} total={sum(d)}')
print('VERIFY_OK')
