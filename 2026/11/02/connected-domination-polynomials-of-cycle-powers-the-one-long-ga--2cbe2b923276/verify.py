#!/usr/bin/env python3
"""Independent finite checks for connected domination of powers of cycles."""
from collections import deque
from math import comb
from itertools import combinations

def graph(n, r):
    return [set(j for j in range(n) if j != i and min((j-i)%n,(i-j)%n)<=r) for i in range(n)]

def brute(n,r):
    adj=graph(n,r)
    out=[0]*(n+1)
    for mask in range(1,1<<n):
        S={i for i in range(n) if mask>>i&1}
        if any(not ((adj[v]&S) or v in S) for v in range(n)):
            continue
        seen={next(iter(S))}
        todo=list(seen)
        while todo:
            u=todo.pop()
            for v in adj[u]&S-seen:
                seen.add(v)
                todo.append(v)
        if seen==S:
            out[len(S)]+=1
    return out

def compositions_count(n,k,r):
    # independently compute coefficient of A^k and B A^(k-1)
    a=[0]*(n+1); a[0]=1
    arr=[a]
    for rep in range(k):
        nxt=[0]*(n+1)
        for s,c in enumerate(arr[-1]):
            if c:
                for gap in range(1,r+1):
                    if s+gap<=n:nxt[s+gap]+=c
        arr.append(nxt)
    short=arr[k][n]
    long=0
    for gap in range(r+1,2*r+2):
        if n-gap>=0:long+=arr[k-1][n-gap]
    numerator=n*short+k*n*long
    assert numerator%k==0,(n,k,r,numerator)
    return numerator//k

def formula(n,r):
    return [0]+[compositions_count(n,k,r) for k in range(1,n+1)]

def min_count(n,r):
    if n<=2*r+1:return 1,n
    k=(n-r-1+r-1)//r
    d=n-r*k
    assert 2<=d<=r+1
    return k,n*comb(k+r-d,r+1-d)

def run():
    cases=0;sets=0
    for r in range(1,5):
        for n in range(2*r+2,min(14,2*r+8)+1):
            obs=brute(n,r)
            exp=formula(n,r)
            assert obs==exp,(n,r,obs,exp)
            k,m=min_count(n,r)
            assert next(i for i,x in enumerate(obs) if x)!=0
            assert next(i for i,x in enumerate(obs) if x)==k,(n,r,k,obs)
            assert obs[k]==m,(n,r,m,obs[k])
            for j in range(n-2*r+1,n+1):
                assert obs[j]==comb(n,j),(n,r,j,obs[j])
            if n-2*r>=1:
                assert obs[n-2*r]<comb(n,n-2*r),(n,r)
            cases+=1;sets+=(1<<n)-1
    for n in range(3,12):
        for r in range(n//2,n+2):
            if n<=2*r+1:
                exp=formula(n,r)
                assert exp==[0]+[comb(n,k) for k in range(1,n+1)],(n,r,exp)
    # For r=1 (ordinary cycles), known exact polynomial; validates reduction.
    for n in range(4,25):
        f=formula(n,1)
        assert f[n]==1 and f[n-1]==n and f[n-2]==n
        assert all(f[j]==0 for j in range(1,n-2))
    print(f"VERIFY_OK: {cases} exhaustive graph instances, {sets} nonempty subsets; closed coefficient, extremal, saturation, and complete graph checks")
if __name__=="__main__":run()
