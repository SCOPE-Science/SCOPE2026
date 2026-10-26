#!/usr/bin/env python3
"""Independent LCF realization and forcing-spectrum certificate, Python 3 standard library.
Uses bitmask dynamic programming and an explicit distinguishing-subset test.
"""
from itertools import combinations
from collections import defaultdict,Counter,deque
import json
steps=[10,7,4,-4,-7,10,-4,7,-7,4]*2
edges={tuple(sorted((i,(i+1)%20))) for i in range(20)}
for i,delta in enumerate(steps):edges.add(tuple(sorted((i,(i+delta)%20))))
edges=sorted(edges)
assert len(edges)==30
id_edges={e:i for i,e in enumerate(edges)}
nbr=[[] for _ in range(20)]
for a,b in edges:nbr[a].append(b);nbr[b].append(a)
# Solve exact covers recursively, selecting a currently-unmatched vertex with minimum free degree.
sol=[]
def fill(free,chosen):
    if not free:sol.append(frozenset(chosen));return
    a=min(free,key=lambda v:sum(w in free for w in nbr[v]))
    for b in nbr[a]:
        if b in free:fill(free-{a,b},chosen+[id_edges[tuple(sorted((a,b)))]] )
fill(set(range(20)),[])
sol=list(set(sol));assert len(sol)==36
# A selected matching subset forces iff it meets every difference (M \ M') for M'!=M.
classes=Counter();type_of={}
for m in sol:
    diffs=[m-other for other in sol if other!=m]
    polynomial=[0]*11
    arr=sorted(m)
    for mask in range(1<<10):
        sel={arr[k] for k in range(10) if mask>>k&1}
        if all(sel&diff for diff in diffs):polynomial[len(sel)]+=1
    classes[tuple(polynomial)]+=1
    type_of[m]=polynomial[3]
expected={(0,0,0,24,122,216,204,120,45,10,1):30,(0,0,0,20,110,202,200,120,45,10,1):6}
assert dict(classes)==expected
# Build alternating-eight-cycle flips without comparing symmetric differences of matchings.
solset={m:i for i,m in enumerate(sol)}; links=set()
for i,m in enumerate(sol):
    for a,b,c,d in combinations(sorted(m),4):
        verts={v for e in (a,b,c,d) for v in edges[e]}
        # Enumerate four-edge alternative matchings on these eight vertices.
        possibles=[]
        def alt(rem, chosen):
            if not rem:possibles.append(frozenset(chosen));return
            u=min(rem)
            for w in nbr[u]:
                if w in rem:
                    z=id_edges[tuple(sorted((u,w)))]
                    if z not in m:alt(rem-{u,w},chosen+[z])
        alt(verts,[])
        for altset in possibles:
            target=(m-{a,b,c,d})|altset
            if target in solset:
                j=solset[target]
                if j!=i:links.add(tuple(sorted((i,j))))
assert len(links)==120
adj=[set() for _ in sol]
for i,j in links:adj[i].add(j);adj[j].add(i)
assert sorted(Counter(map(len,adj)).items())==[(6,30),(10,6)]
assert Counter(type_of[sol[i]] for i in range(36) if len(adj[i])==10)==Counter({20:6})
# Use explicit transitive closure with repeated boolean neighbor expansion.
lengths=[]
for i in range(36):
    visited={i};layer={i};radius=0
    while len(visited)<36:
        layer=set.union(*(adj[k] for k in layer))-visited
        assert layer
        visited|=layer;radius+=1
    lengths.append(radius)
assert set(lengths)=={3}
print(json.dumps({"representation":"LCF [10,7,4,-4,-7,10,-4,7,-7,4]^2", "graph_vertices":20,"graph_edges":30,"perfect_matchings":36,"forcing_polynomial_orbits":sorted([{"multiplicity":v,"coefficients":list(k)} for k,v in classes.items()],key=lambda d:d['multiplicity']),"flip8_vertices":36,"flip8_edges":120,"flip8_components":[36],"flip8_radius":3,"flip8_diameter":3,"flip8_degree_profile":{6:30,10:6}},sort_keys=True))
