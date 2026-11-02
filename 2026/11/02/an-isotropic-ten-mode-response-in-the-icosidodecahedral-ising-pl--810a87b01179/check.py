#!/usr/bin/env python3
"""Exact standard-library certificate for the dodecahedral plateau covariance."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

V = 20
E = set()
for i in range(10):
    E.add(tuple(sorted((i, (i+1)%10))))
    E.add(tuple(sorted((i, 10+i))))
    E.add(tuple(sorted((10+i, 10+(i+2)%10))))
edges = tuple(sorted(E))
assert len(edges) == 30
adj = [[] for _ in range(V)]
for e, (u,v) in enumerate(edges):
    adj[u].append((v,e))
    adj[v].append((u,e))
assert all(len(a)==3 for a in adj)

# Independent enumerator: take the lowest unmatched vertex, branch on its mate.
matchings = []
def collect(mask, selected):
    if not mask:
        matchings.append(frozenset(selected))
        return
    u = (mask & -mask).bit_length()-1
    for v,e in adj[u]:
        if mask & (1 << v):
            collect(mask ^ (1<<u) ^ (1<<v),selected+(e,))
collect((1<<V)-1,())
assert len(matchings)==36 == len(set(matchings))
assert all(len(m)==10 for m in matchings)

# Independent deletion-based dynamic programming for each pinned edge pair.
@lru_cache(None)
def count(mask):
    if not mask:
        return 1
    u=(mask & -mask).bit_length()-1
    return sum(count(mask ^ (1<<u) ^ (1<<v))
               for v,e in adj[u] if mask & (1<<v))
full=(1<<V)-1
assert count(full)==36
single=[sum(i in m for m in matchings) for i in range(30)]
assert single == [12]*30
for u,v in edges:
    assert count(full ^ (1<<u) ^ (1<<v)) == 12

# Pair cooccupancy computed by both algorithms.
K = [[0]*30 for _ in range(30)]
for i in range(30):
    K[i][i] = single[i]
    for j in range(i+1,30):
        co=sum(i in m and j in m for m in matchings)
        endpoints=set(edges[i]+edges[j])
        dp=0 if len(endpoints)<4 else count(full ^ sum(1<<v for v in endpoints))
        assert co == dp
        K[i][j] = K[j][i] = co

# Main exact projector certificate, using ONLY integer operations:
# Q = 36 Cov(n) = K-4 11^T; Q^2=24Q and BQ=0.
Q=[[K[i][j]-4 for j in range(30)] for i in range(30)]
assert sum(Q[i][i] for i in range(30))==240
assert all(sum(Q[i][k]*Q[k][j] for k in range(30))==24*Q[i][j]
           for i in range(30) for j in range(30))
assert all(sum(Q[e][j] for v,e in adj[u])==0
           for u in range(V) for j in range(30))
# Therefore Q/24 is a rank-10 orthogonal projection onto ker B:
# trace(Q)/24=10, B has rank 20 because the graph is connected
# and contains odd cycles (the 12 pentagonal faces).

# Build the line graph and compute both distances and shortest-path counts.
line=[set() for _ in edges]
for row in adj:
    ids={e for v,e in row}
    for e in ids: line[e].update(ids-{e})
assert all(len(s)==4 for s in line)
def line_paths(start):
    dist=[-1]*30; ways=[0]*30
    dist[start]=0;ways[start]=1
    q=deque([start])
    while q:
        e=q.popleft()
        for f in sorted(line[e]):
            if dist[f]<0:
                dist[f]=dist[e]+1;q.append(f)
            if dist[f]==dist[e]+1: ways[f]+=ways[e]
    return dist,ways

def canonical(c):
    return min(tuple(x[k:]+x[:k])
               for x in (list(c),list(reversed(c))) for k in range(5))
faces_as_nodes=set()
def find_5_cycles(path):
    if len(path)==5:
        if any(w==path[0] for w,e in adj[path[-1]]):
            faces_as_nodes.add(canonical(path))
        return
    for w,e in adj[path[-1]]:
        if w not in path: find_5_cycles(path+[w])
for v in range(V):find_5_cycles([v])
assert len(faces_as_nodes)==12
idx={e:i for i,e in enumerate(edges)}
faces=[]
for p in faces_as_nodes:
    faces.append(frozenset(idx[tuple(sorted((p[i],p[(i+1)%5])))]
                           for i in range(5)))
classes=defaultdict(Counter)
for e in range(30):
    dist,ways=line_paths(e)
    for f in range(e+1,30):
        in_face=sum(e in F and f in F for F in faces)
        classes[(dist[f],in_face,ways[f])][K[e][f]] += 1
expected={
    (1,1,1):(0,60), (2,0,1):(7,60), (2,1,1):(5,60),
    (3,0,1):(3,60), (3,0,2):(2,60), (4,0,1):(4,60),
    (4,0,3):(5,60), (5,0,4):(4,15)
}
assert set(classes)==set(expected)
for key,(co,number) in expected.items():
    assert classes[key]==Counter({co:number})
assert sum(count for _,count in expected.values()) == 435
assert sum(co*count for co,count in expected.values()) == 36*45
for key in sorted(expected):
    co,multiplicity=expected[key]
    print('distance,faces,geodesics,count,cooccupancy', *key,multiplicity,co)
print('ALL_EXACT_CHECKS_PASS matchings=36 faces=12 pairs=435 rank_projection=10')
