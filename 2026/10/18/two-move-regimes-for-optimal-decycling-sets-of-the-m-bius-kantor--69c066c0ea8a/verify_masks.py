#!/usr/bin/env python3
"""Exact finite enumeration of feedback-vertex-set exchanges in GP(8,3)."""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256
import json

N = 16
E = sorted({tuple(sorted(p)) for i in range(8) for p in ((i,(i+1)%8),(i,i+8),(i+8,8+(i+3)%8))})
assert len(E)==24
adj=[0]*N
for a,b in E:
    adj[a] |= 1<<b
    adj[b] |= 1<<a
assert all(x.bit_count()==3 for x in adj)


def acyclic_on_mask(keep):
    parent=list(range(N))
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    for a,b in E:
        if ((keep>>a)&1) and ((keep>>b)&1):
            ra, rb = root(a), root(b)
            if ra == rb:
                return False
            parent[ra]=rb
    return True

allmask=(1<<N)-1
minsets=[]
for chosen in combinations(range(N),5):
    mask=sum(1<<x for x in chosen)
    if acyclic_on_mask(allmask ^ mask):
        minsets.append(mask)
minsets.sort()
assert len(minsets)==672
states=set(minsets)
assert not any(acyclic_on_mask(allmask ^ sum(1<<x for x in c)) for c in combinations(range(N),4))

classcount=Counter(sum(bool((s>>a)&1 and (s>>b)&1) for a,b in E) for s in minsets)
assert classcount=={0:192,1:480}


def edges(kind):
    links=set()
    for s in minsets:
        for a in range(N):
            if not s>>a&1:continue
            for b in range(N):
                if s>>b&1:continue
                if kind=='TS' and not (adj[a]>>b&1):continue
                t=s ^ (1<<a) ^ (1<<b)
                if t in states and s<t:links.add((s,t))
    return sorted(links)


def distances(kind,links):
    neighbors={s:[] for s in minsets}
    for a,b in links:
        neighbors[a].append(b);neighbors[b].append(a)
    degree=Counter(map(len,neighbors.values()))
    ecc=Counter();distpairs=Counter()
    for start in minsets:
        seen={start:0};Q=deque([start])
        while Q:
            v=Q.popleft()
            for w in neighbors[v]:
                if w not in seen:
                    seen[w]=seen[v]+1;Q.append(w)
        assert len(seen)==len(minsets), f'{kind}: disconnected at {start}'
        ecc[max(seen.values())]+=1
        for w,d in seen.items():
            if start<w:distpairs[d]+=1
    canon={'states':minsets, 'edges':links}
    fingerprint=sha256(json.dumps(canon,separators=(',',':')).encode()).hexdigest()
    return dict(vertices=len(minsets),edges=len(links),degree_distribution=dict(sorted(degree.items())),eccentricity_distribution=dict(sorted(ecc.items())),radius=min(ecc),diameter=max(ecc),pair_distance_distribution=dict(sorted(distpairs.items())),fingerprint=fingerprint)

out={'graph':'GP(8,3)','minimum_fvs_size':5,'forest_types_by_internal_deletion_edges':dict(sorted(classcount.items()))}
for kind in ('TJ','TS'):
    out[kind]=distances(kind,edges(kind))
print(json.dumps(out,sort_keys=True,separators=(',',':')))
print('VERIFY_OK')
