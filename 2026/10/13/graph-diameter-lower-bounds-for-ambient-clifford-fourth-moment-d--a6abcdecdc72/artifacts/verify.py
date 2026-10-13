#!/usr/bin/env python3
from collections import deque
import math

def graph_ball(adj, v, L):
    seen={v}
    q=deque([(v,0)])
    while q:
        x,d=q.popleft()
        if d==L:
            continue
        for y in adj[x]:
            if y not in seen:
                seen.add(y); q.append((y,d+1))
    return seen

def diameter(adj):
    return max(maxdist(adj,v) for v in adj)

def maxdist(adj,v):
    dist={v:0}; q=deque([v])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in dist:
                dist[y]=dist[x]+1; q.append(y)
    assert len(dist)==len(adj)
    return max(dist.values())

def path(n):
    a={i:set() for i in range(n)}
    for i in range(n-1):
        a[i].add(i+1); a[i+1].add(i)
    return a

def cycle(n):
    a=path(n)
    if n>2:
        a[0].add(n-1); a[n-1].add(0)
    return a

def complete(n):
    return {i:{j for j in range(n) if j!=i} for i in range(n)}

def star(n):
    a={i:set() for i in range(n)}
    for i in range(1,n):
        a[0].add(i); a[i].add(0)
    return a

def grid(r,c):
    a={(i,j):set() for i in range(r) for j in range(c)}
    for i in range(r):
        for j in range(c):
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                z=(i+di,j+dj)
                if z in a: a[(i,j)].add(z)
    return a

def lb(n,s):
    return 1-(4**s-1)/(4**n-1)

def required_ball(n,eps):
    x=1+(1-eps)*(4**n-1)
    # robust integer implementation of ceil(log_4 x)
    k=0; p=1
    while p < x:
        p*=4; k+=1
    return k

# Source path specialization: endpoint radius-L ball has L+1 vertices.
for n in range(2,15):
    a=path(n)
    for L in range(n):
        s=len(graph_ball(a,0,L))
        assert s==L+1
        assert abs(lb(n,s) - (1-(4**(L+1)-1)/(4**n-1))) < 1e-15

# Fixed-error threshold below 3/4 always requires all n qubits.
for n in range(1,30):
    for eps in (0.0,0.1,0.5,0.749999):
        assert required_ball(n,eps)==n

# Representative graph checks: if every L-ball is all vertices, L is at least diameter.
examples=[path(9),cycle(10),star(11),complete(8),grid(3,4)]
for a in examples:
    d=diameter(a)
    n=len(a)
    for L in range(d+2):
        all_full=all(len(graph_ball(a,v,L))==n for v in a)
        assert all_full == (L>=d)

print('VERIFY_OK')
