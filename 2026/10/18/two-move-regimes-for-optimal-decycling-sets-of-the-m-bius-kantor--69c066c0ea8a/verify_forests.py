#!/usr/bin/env python3
"""Independent induced-forest census using DFS, set operations, and graph BFS."""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256
import json

vertices=tuple(range(16))
links=set()
for j in range(8):
    links.add(frozenset((j,(j+1)%8)))
    links.add(frozenset((j,j+8)))
    links.add(frozenset((j+8,8+(j+3)%8)))
assert len(links)==24
NB={v:set() for v in vertices}
for edge in links:
    a,b=tuple(edge);NB[a].add(b);NB[b].add(a)
assert all(len(NB[v])==3 for v in vertices)

def components(K):
    rest=set(K);comp=[]
    while rest:
        x=rest.pop(); seen={x};stack=[x]
        while stack:
            w=stack.pop()
            for z in NB[w]&rest:
                rest.remove(z);seen.add(z);stack.append(z)
        comp.append(seen)
    return comp

def forest(K):
    # A simple graph is a forest iff number of edges is vertices minus components.
    ne=sum(len(NB[v]&K) for v in K)//2
    return ne==len(K)-len(components(K))

F=set()
for keep_seq in combinations(vertices,11):
    keep=set(keep_seq)
    if forest(keep):F.add(frozenset(set(vertices)-keep))
assert len(F)==672
assert not any(forest(set(S)) for S in combinations(vertices,12))

classes=Counter(sum(e<=s for e in links) for s in F)
assert classes=={0:192,1:480}


def pack(s):return sum(1<<v for v in s)

def graph(rule):
    adj={s:set() for s in F}
    for s in F:
        for u in s:
            for v in vertices:
                if v in s:continue
                if rule=='TS' and v not in NB[u]:continue
                t=s.difference((u,)).union((v,))
                if t in F:adj[s].add(t)
    assert all(s in adj[t] for s in F for t in adj[s])
    e=sorted({(min(pack(s),pack(t)),max(pack(s),pack(t))) for s in F for t in adj[s]})
    ecc=Counter(); distribution=Counter()
    for s in F:
        ds={s:0};q=deque([s])
        while q:
            a=q.popleft()
            for t in adj[a]:
                if t not in ds:
                    ds[t]=ds[a]+1;q.append(t)
        assert len(ds)==len(F)
        ecc[max(ds.values())]+=1
        for t,d in ds.items():
            if pack(s)<pack(t):distribution[d]+=1
    return dict(vertices=len(F),edges=len(e),degree_distribution=dict(sorted(Counter(len(x) for x in adj.values()).items())),eccentricity_distribution=dict(sorted(ecc.items())),radius=min(ecc),diameter=max(ecc),pair_distance_distribution=dict(sorted(distribution.items())),fingerprint=sha256(json.dumps({'states':sorted(pack(s) for s in F),'edges':e},separators=(',',':')).encode()).hexdigest())

out={'graph':'GP(8,3)','minimum_fvs_size':5,'forest_types_by_internal_deletion_edges':dict(sorted(classes.items())),'TJ':graph('TJ'),'TS':graph('TS')}
print(json.dumps(out,sort_keys=True,separators=(',',':')))
print('VERIFY_OK')
