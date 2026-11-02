#!/usr/bin/env python3
"""Exact finite checks of derangement switch graphs (stdlib only)."""
from itertools import permutations, combinations
from math import comb, factorial
from collections import deque, Counter


def cycle_structure(perm):
    seen=set(); lengths=[]
    for i in range(len(perm)):
        if i not in seen:
            k=i; length=0
            while k not in seen:
                seen.add(k); k=perm[k]; length+=1
            lengths.append(length)
    return lengths


def no_short_cycles_count(k):
    a=[0]*(k+1); a[0]=1
    for n in range(1,k+1):
        a[n]=sum(comb(n-1,j-1)*factorial(j-1)*a[n-j] for j in range(3,n+1))
    return a


def theoretical_degree_counts(n):
    a=no_short_cycles_count(n)
    return Counter({comb(n,2)-n+t: factorial(n)//(2**t*factorial(t)*factorial(n-2*t))*a[n-2*t]
                    for t in range(n//2+1) if a[n-2*t]})


def all_distances(g,start):
    dist=[-1]*len(g);dist[start]=0;q=deque([start])
    while q:
        a=q.popleft()
        for b in g[a]:
            if dist[b]<0:dist[b]=dist[a]+1;q.append(b)
    return dist


def cayley_distance(a,b):
    inv=[0]*len(a)
    for i,v in enumerate(b):inv[v]=i
    relative=tuple(inv[x] for x in a)
    return len(a)-len(cycle_structure(relative))


def check(n):
    states=[p for p in permutations(range(n)) if all(p[i]!=i for i in range(n))]
    ix={p:i for i,p in enumerate(states)}
    adj=[[] for _ in states]
    for s,p in enumerate(states):
        for i,j in combinations(range(n),2):
            q=list(p);q[i],q[j]=q[j],q[i];q=tuple(q)
            if q in ix:adj[s].append(ix[q])
        expected=comb(n,2)-n+cycle_structure(p).count(2)
        assert len(adj[s])==expected,(n,p,len(adj[s]),expected)
    for u,ns in enumerate(adj):
        for v in ns: assert u in adj[v]
    assert Counter(map(len,adj))==theoretical_degree_counts(n)
    cnt=sum(map(len,adj))//2
    expected_edges=((comb(n,2)-n)*len(states)+comb(n,2)*
                    (0 if n-2==1 else len([p for p in permutations(range(n-2)) if all(p[i]!=i for i in range(n-2))])))//2
    assert cnt==expected_edges,(cnt,expected_edges)
    dist=all_distances(adj,0)
    if n==3: assert all(len(ns)==0 for ns in adj) and len(states)==2
    else: assert all(x>=0 for x in dist)
    if n==4:
        for i,p in enumerate(states):
            d=all_distances(adj,i)
            for j,q in enumerate(states): assert d[j]==cayley_distance(p,q)
    if n in (5,6):
        if n==5:
            a=(1,0,3,4,2);b=(1,0,4,2,3)
        else:
            a=(1,2,0,4,5,3);b=(2,0,1,4,5,3)
        assert cayley_distance(a,b)==2
        assert all_distances(adj,ix[a])[ix[b]]==4
    print(f'PRIMARY_OK n={n} derangements={len(states)} edges={cnt} components={1 if n>=4 else 2} degrees={dict(sorted(Counter(map(len,adj)).items()))}')

if __name__=='__main__':
    for n in range(3,9):check(n)
    print('PRIMARY_COMPLETE_OK')
