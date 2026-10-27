#!/usr/bin/env python3
"""Exact exhaustive certification for single-node immunization on small trees.
Python 3 standard library only.  All polynomial arithmetic uses integers.
"""
from itertools import product
from math import comb
from collections import deque
from fractions import Fraction
from time import monotonic


def tree_from_prufer(seq,n):
    deg=[1]*n
    for x in seq:deg[x]+=1
    edges=[]
    for x in seq:
        y=next(j for j in range(n) if deg[j]==1)
        edges.append((x,y));deg[x]-=1;deg[y]-=1
    last=[i for i in range(n) if deg[i]==1]
    edges.append((last[0],last[1]));return edges

def adjacency(edges,n):
    A=[[] for _ in range(n)]
    for a,b in edges:A[a].append(b);A[b].append(a)
    return A

def canonical(edges,n):
    A=adjacency(edges,n);deg=[len(x) for x in A]
    leaves=[x for x in range(n) if deg[x]<=1]
    left=n
    while left>2:
        left-=len(leaves)
        nxt=[]
        for u in leaves:
            deg[u]=0
            for v in A[u]:
                if deg[v]:
                    deg[v]-=1
                    if deg[v]==1:nxt.append(v)
        leaves=nxt
    def code(v, parent):
        return '(' + ''.join(sorted(code(w,v) for w in A[v] if w!=parent)) + ')'
    if left==1:
        return 'C'+code(leaves[0],-1)
    return 'U'+''.join(sorted((code(leaves[0],leaves[1]),code(leaves[1],leaves[0]))))

def outbreak_coeffs(edges,n,v):
    A=adjacency(edges,n);coef=[0]*(n-1)
    for root in range(n):
        if root==v:continue
        dist=[-1]*n;dist[root]=0; Q=deque([root])
        while Q:
            u=Q.popleft()
            for w in A[u]:
                if w!=v and dist[w]<0:
                    dist[w]=dist[u]+1;Q.append(w)
        for target in range(n):
            if target!=root and dist[target]>0:coef[dist[target]]+=1
    return tuple(coef)

def bernstein_positive(f,g,n):
    # certify sum_k (f[k]-g[k])*p^k >= 0 for every 0<p<1
    # by multiplying by (1+t)^d and substituting p=t/(1+t).
    d=n-2
    coeff=[sum((f[k]-g[k])*comb(d-k,j-k) for k in range(1,j+1)) for j in range(d+1)]
    return all(x>=0 for x in coeff)

def objective(coefs,p):return sum(coefs[k]*p**k for k in range(1,len(coefs)))

def optimal_vertices(P,p):
    values=[objective(x,p) for x in P]
    minimum=min(values)
    return {v for v,x in enumerate(values) if x==minimum}

# Two explicit eight-vertex representatives; vertices are named in RESULT.md.
BROOM=[(1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(6,7)]
DOUBLE=[(1,0),(1,2),(2,3),(2,4),(0,5),(5,6),(5,7)]
expected={canonical(BROOM,8),canonical(DOUBLE,8)}
assert len(expected)==2
counts={};exceptions={}
start=monotonic()
for n in range(2,9):
    reps={}
    for seq in product(range(n),repeat=n-2):
        edges=tree_from_prufer(seq,n)
        k=canonical(edges,n)
        if k not in reps:reps[k]=edges
    counts[n]=len(reps)
    for key,edges in reps.items():
        P=[outbreak_coeffs(edges,n,v) for v in range(n)]
        universal=[v for v in range(n) if all(bernstein_positive(P[w],P[v],n) for w in range(n))]
        if not universal:
            assert n==8 and key in expected,(n,edges)
            assert not optimal_vertices(P,Fraction(1,2)).intersection(optimal_vertices(P,Fraction(9,10)))
            exceptions[key]=edges
    print('n=%d distinct=%d'%(n,len(reps)))
assert counts=={2:1,3:1,4:2,5:3,6:6,7:11,8:23},counts
assert set(exceptions)==expected,(exceptions,expected)
# Verify exact analytic formulas and all-vertex dominance in witness cases.
for kind,edges,hub,bridge in [('broom',BROOM,2,1),('double',DOUBLE,2,1)]:
    P=[outbreak_coeffs(edges,8,v) for v in range(8)]
    if kind=='broom':
        assert P[hub][1:]==(8,6,4,2,0,0)
        assert P[bridge][1:]==(10,6,2,0,0,0)
    else:
        assert P[hub][1:]==(8,8,4,0,0,0)
        assert P[bridge][1:]==(10,8,0,0,0,0)
        assert P[2]==P[5] and P[1]==P[0]
    # For each remaining candidate, bridge beats it at every p in (0,1).
    for w in range(8):
        if kind=='broom' and w==hub:continue
        if kind=='double' and w in (hub,5):continue
        assert bernstein_positive(P[w],P[bridge],8),(kind,w,P[w],P[bridge])
print('PASS: no crossover through 7 vertices; precisely two 8-vertex cases; rational comparisons checked')
print('elapsed %.3fs'%(monotonic()-start))
