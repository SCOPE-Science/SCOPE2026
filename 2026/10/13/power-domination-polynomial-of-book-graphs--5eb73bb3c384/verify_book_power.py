#!/usr/bin/env python3
from itertools import combinations
from math import comb

def graph(n):
    # vertices 0=u, 1=v, then 2+2*i=a_i, 3+2*i=b_i
    N=2+2*n
    adj=[set() for _ in range(N)]
    def add(a,b):
        adj[a].add(b); adj[b].add(a)
    add(0,1)
    for i in range(n):
        a=2+2*i; b=a+1
        add(0,a); add(a,b); add(b,1)
    return adj

def power_dominates(adj,S):
    obs=set(S)
    for v in list(S):
        obs.update(adj[v])
    changed=True
    while changed:
        changed=False
        for v in list(obs):
            white=adj[v]-obs
            if len(white)==1:
                obs.add(next(iter(white)))
                changed=True
    return len(obs)==len(adj)

def criterion(n,S):
    if 0 in S or 1 in S:
        return True
    empty=0
    for i in range(n):
        if 2+2*i not in S and 3+2*i not in S:
            empty+=1
    return empty<=1

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,n):
    r=[1]
    for _ in range(n): r=mul(r,a)
    return r

def addpoly(*polys):
    m=max(map(len,polys)); out=[0]*m
    for p in polys:
        for i,v in enumerate(p): out[i]+=v
    return out

def formula(n):
    spine=[0,2,1]                    # 2x+x^2
    pages_any=power([1,1],2*n)       # (1+x)^(2n)
    first=mul(spine,pages_any)
    q=[0,2,1]
    all_pages=power(q,n)
    one_empty=[n*v for v in power(q,n-1)]
    return addpoly(first,all_pages,one_empty)

subset_checks=criterion_checks=coefficient_checks=minimum_checks=0
for n in range(2,8):
    adj=graph(n); N=len(adj); counts=[0]*(N+1)
    for mask in range(1<<N):
        S={i for i in range(N) if (mask>>i)&1}
        actual=power_dominates(adj,S)
        predicted=criterion(n,S)
        subset_checks+=1; criterion_checks+=1
        assert actual==predicted, (n,S,actual,predicted)
        if actual: counts[len(S)]+=1
    f=formula(n)+[0]*(N+1-len(formula(n)))
    f=f[:N+1]
    for k in range(N+1):
        coefficient_checks+=1
        assert counts[k]==f[k], (n,k,counts[k],f[k])
    total=sum(counts)
    assert total==3*(4**n)+(n+3)*(3**(n-1)), (n,total)
    nz=[k for k,c in enumerate(counts) if c]
    assert nz and nz[0]==1
    minimum_checks+=1
    assert counts[1]==(6 if n==2 else 2), (n,counts[1])
print(f"VERIFY_OK n_range=2..7 subset_checks={subset_checks} classification_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=16")
