#!/usr/bin/env python3
"""Exhaustive Property-B recoloring graph of PG(2,3), standard library only."""
from itertools import product
from collections import Counter, deque

Q=3
vecs=[v for v in product(range(Q),repeat=3) if any(v)]
def normalize(v):
    z=next(t for t in v if t)
    return tuple((x*z)%Q for x in v) if z==1 else tuple((x*2)%Q for x in v)
pts=sorted({normalize(v) for v in vecs})
lines=sorted({sum(1<<i for i,p in enumerate(pts) if sum(x*y for x,y in zip(a,p))%3==0) for a in pts})
assert len(pts)==len(lines)==13 and all(x.bit_count()==4 for x in lines)
FULL=(1<<13)-1
valid={m for m in range(1<<13) if all(0<(m&l).bit_count()<4 for l in lines)}
assert len(valid)==468
assert Counter(m.bit_count() for m in valid)=={6:234,7:234}
G={m:{m^(1<<i) for i in range(13) if (m^(1<<i)) in valid} for m in valid}
assert all(len(nei)==3 for nei in G.values())
assert sum(map(len,G.values()))//2==702

def metrics(adj):
    degree=Counter(map(len,adj.values())); patterns=set();diameter=0;girth=10**6
    for root in adj:
        dist={root:0}; parent={root:None};q=deque([root])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in dist:
                    dist[w]=dist[v]+1; parent[w]=v;q.append(w)
                elif parent[v]!=w and parent[w]!=v:
                    girth=min(girth,dist[v]+dist[w]+1)
        assert len(dist)==len(adj)
        diameter=max(diameter,max(dist.values()))
        patterns.add(tuple(Counter(dist.values()).get(i,0) for i in range(max(dist.values())+1)))
    assert len(patterns)==1
    return degree,diameter,girth,next(iter(patterns))

DG,diam,girth,profile=metrics(G)
assert diam==13 and girth==12
assert profile==(1,3,6,12,24,48,72,96,116,68,12,6,3,1)
small={m for m in valid if m.bit_count()==6}
H={s:{t for t in small if t&s==0} for s in small}
assert all(len(N)==3 for N in H.values())
assert set(H)==small
DH,diamH,girthH,profileH=metrics(H)
assert diamH==8 and girthH==12
assert profileH==(1,3,6,12,24,48,72,48,20)
assert all({FULL^y for y in G[x]}==H[x] for x in small)
print('PROPERTY_B_COLORING_EXHAUSTIVE_PASS')
print('valid',len(valid),'edges',sum(map(len,G.values()))//2,'girth',girth,'diameter',diam,'distance_profile',profile)
print('six_point_frame_graph',len(H),'edges',sum(map(len,H.values()))//2,'girth',girthH,'diameter',diamH,'distance_profile',profileH)
