#!/usr/bin/env python3
"""Exact independent low-dimensional Rota--Baxter census and tree/EGF checks."""
from itertools import product
from collections import Counter
from math import factorial,comb
import heapq
from fractions import Fraction

def gauss_rank(a,p):
    a=[[(x%p) for x in row] for row in a];n=len(a);r=0
    for j in range(n):
        k=next((i for i in range(r,n) if a[i][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        c=pow(a[r][j],-1,p)
        a[r]=[(t*c)%p for t in a[r]]
        for i in range(r+1,n):
            if a[i][j]:
                k=a[i][j];a[i]=[(t-k*s)%p for t,s in zip(a[i],a[r])]
        r+=1
    return r

def direct(n,p):
    counts=Counter()
    for colors in product([0,1],repeat=n):
        sign=[1 if x==0 else -1 for x in colors]
        for bits in product([0,1],repeat=n*(n-1)):
            a=[[0]*n for _ in range(n)];b=iter(bits)
            for i in range(n):
                a[i][i]=0 if sign[i]==1 else -1
                for j in range(n):
                    if j!=i:a[i][j]=next(b)*sign[i]
            ok=True
            for i in range(n):
                for j in range(i,n):
                    for k in range(n):
                        l=(a[i][k]*a[j][k])%p
                        rr=(a[i][j]*a[j][k]+a[j][i]*a[i][k]+(a[i][k] if i==j else 0))%p
                        if l!=rr:ok=False;break
                    if not ok:break
                if not ok:break
            if ok:counts[gauss_rank(a,p)]+=1
    return counts

def tree_counts(n):
    N=n+1; hist=Counter()
    for prufer in product(range(N), repeat=max(N-2,0)):
        deg=[1]*N
        for q in prufer:deg[q]+=1
        leaves=[i for i in range(N) if deg[i]==1];heapq.heapify(leaves)
        adj=[[] for _ in range(N)]
        for q in prufer:
            v=heapq.heappop(leaves)
            adj[v].append(q);adj[q].append(v)
            deg[v]-=1;deg[q]-=1
            if deg[q]==1:heapq.heappush(leaves,q)
        v=heapq.heappop(leaves);w=heapq.heappop(leaves)
        adj[v].append(w);adj[w].append(v)
        parent=[-1]*N;parent[0]=0;queue=[0];children=[[] for _ in range(N)]
        for u in queue:
            for v in adj[u]:
                if parent[v]==-1:
                    parent[v]=u;children[u].append(v);queue.append(v)
        for mask in range(1<<n):
            nullity=sum(1 for i in range(1,N) if not((mask>>(i-1))&1) and all(((mask>>(j-1))&1) for j in children[i]))
            hist[n-nullity]+=1
    return hist

def exp_series(c,n):
    e=[Fraction(0)]*(n+1);e[0]=Fraction(1)
    for m in range(1,n+1):
        e[m]=sum(Fraction(k)*c[k]*e[m-k] for k in range(1,m+1))/m
    return e

def egf_count(n,u):
    b=[Fraction(0)]*(n+1);w=b.copy()
    for _ in range(n):
        ew=exp_series(w,n);eb=exp_series(b,n)
        es=exp_series([b[i]+w[i] for i in range(n+1)],n)
        bn=[Fraction(0)]*(n+1);wn=bn.copy()
        for j in range(1,n+1):
            bn[j]=es[j-1]
            wn[j]=u*eb[j-1]+sum(eb[k]*ew[j-1-k] for k in range(j-1))
        b,w=bn,wn
    f=exp_series([b[i]+w[i] for i in range(n+1)],n)
    return f[n]*factorial(n)

if __name__=='__main__':
    for n in range(1,5):
        tr=tree_counts(n)
        for p in [2,3]:
            dr=direct(n,p)
            assert tr==dr, (n,p,tr,dr)
        assert sum(tr.values())==2**n*(n+1)**(n-1)
        N=n+1
        mu=Fraction(n,2)*(1-Fraction(1,2*N))**(N-2)
        assert Fraction(sum((n-k)*v for k,v in tr.items()),sum(tr.values()))==mu
        for u in range(n+1):
            assert egf_count(n,u)==sum(v*u**(n-k) for k,v in tr.items()), (n,u)
        print('EXHAUSTIVE_OK',n,dict(sorted(tr.items())))
    for n in [5]:
        tr=tree_counts(n)
        assert sum(tr.values())==2**n*(n+1)**(n-1)
        N=n+1
        mu=Fraction(n,2)*(1-Fraction(1,2*N))**(N-2)
        assert Fraction(sum((n-k)*v for k,v in tr.items()),sum(tr.values()))==mu
        for u in range(n+1):
            assert egf_count(n,u)==sum(v*u**(n-k) for k,v in tr.items()), (n,u)
        print('TREE_OK',n,dict(sorted(tr.items())))
    print('VERIFY_OK')
