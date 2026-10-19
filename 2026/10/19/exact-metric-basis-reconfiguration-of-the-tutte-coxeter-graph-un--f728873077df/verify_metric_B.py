#!/usr/bin/env python3
"""Independent generalized-quadrangle model and distance-signature replay.
Vertices are nonzero vectors and isotropic F2 projective lines in F2^4.
Computations use exact arithmetic and direct distance codes, without the
pair-separation masks or the duad/syntheme construction.
"""
from itertools import combinations
from collections import deque,Counter
POINTS=tuple(range(1,16))
def dot(x,y):
    return ((x&1 != 0) and (y&4 != 0)) ^ ((x&4 != 0) and (y&1 != 0)) ^ ((x&2 != 0) and (y&8 != 0)) ^ ((x&8 != 0) and (y&2 != 0))
LINES=tuple(sorted({tuple(sorted((x,y,x^y))) for x,y in combinations(POINTS,2) if not dot(x,y)}))
assert len(LINES)==15
Pidx={x:i for i,x in enumerate(POINTS)}
Lidx={line:i+15 for i,line in enumerate(LINES)}
neighbors=[[] for _ in range(30)]
for i,p in enumerate(POINTS):
    for j,line in enumerate(LINES):
        if p in line:
            neighbors[i].append(j+15);neighbors[j+15].append(i)
assert all(len(s)==3 for s in neighbors)
def bfs_graph(start,graph):
    dd=[-1]*len(graph);dd[start]=0;q=deque([start])
    while q:
        x=q.popleft()
        for y in graph[x]:
            if dd[y]==-1:dd[y]=dd[x]+1;q.append(y)
    assert -1 not in dd
    return dd
D=[bfs_graph(i,neighbors) for i in range(30)]
assert all(max(row)==4 for row in D)
# Direct signatures, not pair-set cover.
def distinguish(S):
    return len({tuple(D[w][u] for w in S) for u in range(30)})==30
for k in range(1,6):
    assert all(not distinguish(s) for s in combinations(range(30),k))
B=[s for s in combinations(range(30),6) if distinguish(s)]
assert len(B)==32460
assert Counter(sum(x<15 for x in s) for s in B)=={2:7470,3:17520,4:7470}
index={s:i for i,s in enumerate(B)}
# Alternate adjacency construction: bucket common five landmarks; each
# bucket forms a clique because every pair differs by one exchanged vertex.
graph=[set() for _ in B]
buckets={}
for i,s in enumerate(B):
    for reduced in combinations(s,5):buckets.setdefault(reduced,[]).append(i)
for bucket in buckets.values():
    for i,j in combinations(bucket,2):
        graph[i].add(j);graph[j].add(i)
assert sum(map(len,graph))//2==403020
seen={0};q=deque([0])
while q:
    for v in graph[q.popleft()]:
        if v not in seen:seen.add(v);q.append(v)
assert len(seen)==len(B)
# Symplectic transvections are genuine graph automorphisms, independent
# of the six-symbol permutation model of the other verification.
gens=[]
for v in POINTS:
    g=[]
    for x in POINTS:g.append(Pidx[x ^ (v if dot(x,v) else 0)])
    for line in LINES:
        image=tuple(sorted(x ^ (v if dot(x,v) else 0) for x in line))
        g.append(Lidx[image])
    assert sorted(g)==list(range(30))
    for a in range(30):assert {g[b] for b in neighbors[a]}==set(neighbors[g[a]])
    gens.append(g)
seen=set();orbits=[]
for i,s in enumerate(B):
    if i in seen:continue
    orbit={i};q=deque([i])
    while q:
        a=q.popleft()
        for g in gens:
            j=index[tuple(sorted(g[x] for x in B[a]))]
            if j not in orbit:orbit.add(j);q.append(j)
    seen.update(orbit);orbits.append((i,len(orbit)))
assert len(seen)==len(B)
assert len(orbits)==62
assert Counter(size for i,size in orbits)=={720:32,360:24,180:2,120:2,90:2}
ecc=Counter();witness=[]
for i,size in orbits:
    max_dist=max(bfs_graph(i,graph))
    ecc[max_dist]+=size
    if max_dist==8:witness.append((i,size))
assert ecc=={7:31740,8:720}
assert len(witness)==1 and witness[0][1]==720
# Second slide graph construction: for each occupied vertex, replace it
# only by an adjacent unoccupied vertex, and require the result be a basis.
slide=[set() for _ in B]
for i,S in enumerate(B):
    inside=set(S)
    for u in S:
        for v in neighbors[u]:
            if v in inside:continue
            j=index.get(tuple(sorted((inside-{u})|{v})))
            if j is not None:slide[i].add(j)
assert sum(map(len,slide))//2==55440
assert all(i in slide[j] for i,x in enumerate(slide) for j in x)
slide_ecc=Counter()
for i,size in orbits:
    slide_ecc[max(bfs_graph(i,slide))]+=size
assert slide_ecc=={17:3780,18:11040,19:10440,20:7200}
print('INCIDENCE_GRAPH_F2_SYMPLECTIC=30_VERTICES_45_EDGES')
print('DIRECT_SIGNATURE_MINIMUM_SIZE=6;BASES=32460')
print('BASE_SPLIT=2:7470,3:17520,4:7470')
print('FIVE_LANDMARK_BUCKET_EDGE_COUNT=403020')
print('ALL_BASES_CONNECTED=TRUE')
print('SYMPLECTIC_TRANSVECTION_ORBITS=62')
print('ECCENTRICITY_PROFILE=7:31740,8:720')
print('SLIDE_EDGE_COUNT=55440;CONNECTED=TRUE')
print('SLIDE_ECCENTRICITIES=17:3780,18:11040,19:10440,20:7200')
print('INDEPENDENT_VERIFY_OK')
