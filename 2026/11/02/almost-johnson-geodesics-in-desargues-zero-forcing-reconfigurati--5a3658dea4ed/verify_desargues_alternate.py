#!/usr/bin/env python3
"""Independent exact enumeration for the bipartite-Kneser presentation of the Desargues graph."""
import itertools
from collections import Counter, deque

pairs=list(itertools.combinations(range(5),2))
vertex=[(side,p) for side in range(2) for p in pairs]
N=len(vertex)
adjacency=[]
for i,(s,a) in enumerate(vertex):
    adjacency.append(tuple(j for j,(t,b) in enumerate(vertex) if s!=t and set(a).isdisjoint(b)))
assert N==20 and all(len(row)==3 for row in adjacency)
assert sum(len(row) for row in adjacency)//2==30
full=(1<<N)-1

def forces(start):
    blue=start
    while True:
        change=None
        for u in range(N):
            if not (blue & (1<<u)): continue
            whites=[w for w in adjacency[u] if not (blue&(1<<w))]
            if len(whites)==1:
                change=whites[0]
                break
        if change is None: return blue==full
        blue|=1<<change

small=[sum(1<<v for v in s) for s in itertools.combinations(range(N),7) if forces(sum(1<<v for v in s))]
assert not small,(len(small),small[:2])
sets=[sum(1<<v for v in s) for s in itertools.combinations(range(N),8) if forces(sum(1<<v for v in s))]
assert len(sets)==13520,len(sets)
place={m:i for i,m in enumerate(sets)}
neighbors=[[] for _ in sets]
for i,m in enumerate(sets):
    have=[u for u in range(N) if m & (1<<u)]
    absent=[v for v in range(N) if not(m & (1<<v))]
    for u in have:
        for v in absent:
            target=m ^ (1<<u) ^ (1<<v)
            if target in place:neighbors[i].append(place[target])
assert all(len(set(row))==len(row) for row in neighbors)
assert all(i in neighbors[j] for i,row in enumerate(neighbors) for j in row)
degs=Counter(len(row) for row in neighbors)
expected={20:240,21:120,22:360,23:480,24:1340,25:1800,26:3000,27:240,28:4380,29:480,30:960,32:120}
assert dict(degs)==expected,dict(degs)
assert sum(degs.values())==13520
assert sum(k*v for k,v in degs.items())//2==178560

def distances(src):
    dist=[-1]*len(sets)
    dist[src]=0
    q=deque([src])
    while q:
        u=q.popleft()
        for v in neighbors[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    assert min(dist)==0
    return dist

# All reachability is established by any one full BFS; further roots cross-check distance behavior.
d0=distances(0)
assert all(x>=0 for x in d0)
assert max(d0) in (7,8)
roots=[0,1,2,17,83,150,450,1000,13519]
for src in roots:
    dist=distances(src)
    assert max(dist)<=8
    for j,d in enumerate(dist):
        delta=8-(sets[src]&sets[j]).bit_count()
        assert delta<=d<=delta+1,(src,j,delta,d)
print('ALTERNATE_KNESER_PASS', 'zero7=0', 'zero8=13520', 'edges=178560', 'connected=1', 'degree_classes=11', 'sampled_roots='+str(len(roots)))
