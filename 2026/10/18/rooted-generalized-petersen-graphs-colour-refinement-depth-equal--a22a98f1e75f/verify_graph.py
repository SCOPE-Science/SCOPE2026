#!/usr/bin/env python3
"""Independent direct-graph tests for a rooted generalized Petersen graph.
Only finite checks: the all-n theorem is proved in RESULT.md.
"""
from collections import Counter, deque

def build(n):
    E=[set() for _ in range(2*n)]
    def add(x,y):
        assert x != y
        E[x].add(y); E[y].add(x)
    for i in range(n):
        add(i,(i+1)%n)
        add(i,n+i)
        add(n+i,n+(i+2)%n)
    assert all(len(x)==3 for x in E)
    return E

def refine(E):
    C=[int(i==0) for i in range(len(E))]
    states=[C]
    while True:
        labels=[(C[v],tuple(sorted(C[w] for w in E[v]))) for v in range(len(E))]
        d={k:i for i,k in enumerate(sorted(set(labels)))}
        new=[d[k] for k in labels]
        if len(set(new))==len(set(C)):return states
        states.append(new)
        C=new

def orbit_partition(n):
    return [tuple(sorted((layer,min(i,n-i)))) for layer in [0,1] for i in range(n)]

def groups(labels):
    d={}
    for i,a in enumerate(labels):d.setdefault(a,set()).add(i)
    return frozenset(frozenset(s) for s in d.values())

def bfs(E):
    dist=[-1]*len(E);dist[0]=0;queue=deque([0])
    while queue:
        v=queue.popleft()
        for w in E[v]:
            if dist[w]<0:dist[w]=dist[v]+1;queue.append(w)
    return dist

cases=0;vertex_total=0
for n in range(14,301):
    E=build(n)
    p=refine(E)
    depth=len(p)-1
    target=(n+10)//4
    assert depth==target,(n,depth,target)
    want=[(0 if i<n else 1,min(i%n,n-(i%n))) for i in range(2*n)]
    assert groups(p[-1])==groups(want),('orbits',n)
    dist=bfs(E)
    h=n//2
    assert max(dist)==target,('eccentricity',n)
    for j in range(h+1):
        assert dist[j]==min(j,2+(j+1)//2)
        assert dist[n+j]==1+(j+1)//2
    if n<=25:
        assert len(p[target-1])>0 and groups(p[target-1])!=groups(want)
    cases+=1;vertex_total+=2*n
print('PASS direct full graph: n=14..300,',cases,'instances,',vertex_total,'aggregate vertices; orbit classes, depths and distance formulas')
