#!/usr/bin/env python3
"""Independent 18-vertex LCF graph, exact matchings, elementary hexagon flips."""
from collections import Counter,deque
import json
n=18
shifts=[5,7,-7,7,-7,-5]*3
edges={tuple(sorted((i,(i+1)%n))) for i in range(n)}
edges|={tuple(sorted((i,(i+shifts[i])%n))) for i in range(n)}
assert len(edges)==27
edges=sorted(edges); index={e:i for i,e in enumerate(edges)}
N={i:set() for i in range(n)}
for u,v in edges:N[u].add(v);N[v].add(u)
assert all(len(N[i])==3 for i in N)
matchings=[]
def extend(unused,mask):
    if not unused: matchings.append(mask);return
    u=min(unused)
    for v in sorted(N[u]&unused):
        extend(unused-{u,v},mask | (1<<index[tuple(sorted((u,v)))]))
extend(set(range(n)),0)
assert len(matchings)==42
allmatch=set(matchings)
# Visit oriented simple hexagons, retaining edge masks only.
hexagons=set()
def walk(path):
    if len(path)==6:
        if path[0] in N[path[-1]]:
            hexagons.add(sum(1<<index[tuple(sorted((path[i],path[(i+1)%6])))] for i in range(6)))
        return
    for v in N[path[-1]]:
        if v not in path and v>path[0]:walk(path+[v])
for u in range(n):walk([u])
assert len(hexagons)==18
A={m:set() for m in matchings}
for m in matchings:
    for h in hexagons:
        if (m & h).bit_count()==3:
            q=m^h
            assert q in allmatch
            A[m].add(q)
assert all(m in A[z] for m in matchings for z in A[m])
seen=set();cs=[]
for m in matchings:
    if m in seen:continue
    c={m};todo=[m];seen.add(m)
    while todo:
        u=todo.pop()
        for v in A[u]-seen:seen.add(v);c.add(v);todo.append(v)
    cs.append(c)
assert sorted(map(len,cs))==[21,21]
assert sum(len(A[m]) for m in A)//2==72
for c in cs:
    assert Counter(map(lambda z:len(A[z]),c))=={3:18,6:3}
    distmax=0
    for start in c:
        Q=deque([start]);D={start:0}
        while Q:
            v=Q.popleft()
            for z in A[v]:
                if z not in D:D[z]=D[v]+1;Q.append(z)
        assert len(D)==21
        distmax=max(distmax,max(D.values()))
    assert distmax==4
print(json.dumps({'graph':'LCF [5,7,-7,7,-7,-5]^3','perfect_matchings':42,'six_cycles':18,
                  'flip_edges':72,'components':[21,21],'degree_profile_per_component':{'3':18,'6':3},
                  'diameters':[4,4]},sort_keys=True,indent=2))
