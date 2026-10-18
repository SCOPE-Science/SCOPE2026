#!/usr/bin/env python3
"""Independent hyperoval construction by unique completion of four-arcs."""
import json, hashlib
from itertools import combinations
from collections import Counter, deque

# Represent GF(4) as 0,1,t,t+1; t^2=t+1. Construct its product table explicitly.
table=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
def dot(u,v):
    return table[u[0]][v[0]] ^ table[u[1]][v[1]] ^ table[u[2]][v[2]]

# Last nonzero coordinate normalized to 1 (distinct from the other checker).
points=[]
for z in range(4):
    for y in range(4):
        for x in range(4):
            a=(x,y,z)
            if not any(a):continue
            idx=max(i for i in range(3) if a[i])
            inverse=next(k for k in (1,2,3) if table[a[idx]][k]==1)
            b=tuple(table[inverse][v] for v in a)
            if b not in points:points.append(b)
points=sorted(points)
assert len(points)==21
lines=[]
for c in points:
    row=frozenset(i for i,p in enumerate(points) if dot(c,p)==0)
    if row not in lines:lines.append(row)
assert len(lines)==21
pairs_to_line={frozenset((i,j)):next(k for k,l in enumerate(lines) if i in l and j in l)
               for i,j in combinations(range(21),2)}
assert all(sum(int(i in l) for l in lines)==5 for i in range(21))

def arc(S):
    return len({pairs_to_line[frozenset(pair)] for pair in combinations(S,2)}) == len(S)*(len(S)-1)//2

hyperoval_sets=set()
quadrangle_count=0
for quad in combinations(range(21),4):
    if not arc(quad):continue
    quadrangle_count+=1
    outside=[j for j in range(21) if j not in quad]
    options=[frozenset((*quad,*ext)) for ext in combinations(outside,2) if arc((*quad,*ext))]
    assert len(options)==1, ('nonunique completion',quad,len(options))
    hyperoval_sets.add(options[0])
assert quadrangle_count==2520 and len(hyperoval_sets)==168
# Every hyperoval has 15 quadrangles; all 4-arcs have appeared in completion.
assert quadrangle_count == len(hyperoval_sets)*15
H=sorted(sum(1<<j for j in h) for h in hyperoval_sets)
adj=[set(j for j,b in enumerate(H) if i!=j and (a&b).bit_count()==3) for i,a in enumerate(H)]
assert all(len(row)==40 for row in adj)
common_spectrum={r:Counter() for r in (0,1,2,3)}
for i in range(168):
    for j in range(i+1,168):
        common_spectrum[(H[i]&H[j]).bit_count()][len(adj[i]&adj[j])]+=1
assert {r:dict(v) for r,v in common_spectrum.items()}=={0:{4:840},1:{5:6048},2:{16:3780},3:{11:3360}}
# All states have eccentricity two, checked by BFS independently.
ecc=Counter()
for i in range(168):
    dist={i:0};q=deque([i])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==168
    ecc[max(dist.values())]+=1
assert ecc=={2:168}
# H coordinate order differs from the first program. Canonicalize by projective point coordinates.
coords={p:i for i,p in enumerate(points)}
Hcanonical=[]
for h in hyperoval_sets:
    triples=[points[i] for i in h]
    # Normalize each under first-coordinate convention for cross-replay certificate hash.
    res=[]
    for p in triples:
        k=next(x for x in p if x)
        inv=next(j for j in (1,2,3) if table[k][j]==1)
        q=tuple(table[inv][x] for x in p)
        res.append(q)
    # Same ordering as first checker (lexicographic triples).
    allpts=[]
    for v in [(x,y,z) for x in range(4) for y in range(4) for z in range(4) if x or y or z]:
        first=next(x for x in v if x)
        inv=next(j for j in (1,2,3) if table[first][j]==1)
        q=tuple(table[inv][x] for x in v)
        if q not in allpts:allpts.append(q)
    allpts=sorted(allpts)
    Hcanonical.append(sum(1<<allpts.index(q) for q in res))
cert='\n'.join(format(h,'021b') for h in sorted(Hcanonical))+'\n'
print(json.dumps({'points':21,'lines':21,'quadrangles':quadrangle_count,
 'unique_six_arc_completions':quadrangle_count,'hyperovals':len(H),
 'degree_histogram':dict(Counter(map(len,adj))),
 'edges':sum(map(len,adj))//2,
 'common_neighbor_counts':{str(k):dict(sorted(v.items())) for k,v in common_spectrum.items()},
 'eccentricities':dict(ecc),
 'canonical_hyperoval_sha256':hashlib.sha256(cert.encode()).hexdigest(),
 'verified':True},sort_keys=True,indent=2))
