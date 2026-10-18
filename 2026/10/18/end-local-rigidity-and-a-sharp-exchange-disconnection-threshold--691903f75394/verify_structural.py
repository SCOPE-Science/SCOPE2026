#!/usr/bin/env python3
"""Finite boundary classification and abstract exchange graph for three-row grids."""
from itertools import combinations
from collections import deque,Counter

L_EXPECTED = [
 ((0,0),(0,1),(0,2)),
 ((0,0),(0,1),(1,1)),
 ((0,0),(0,1),(2,0)),
 ((0,0),(0,2),(1,0)),
 ((0,0),(0,2),(1,2)),
 ((0,0),(1,0),(1,1)),
 ((0,0),(1,0),(2,0)),
 ((0,1),(0,2),(1,1)),
 ((0,1),(0,2),(2,2)),
 ((0,2),(1,1),(1,2)),
 ((0,2),(1,2),(2,2)),
 ((1,0),(1,1),(2,0)),
 ((1,1),(1,2),(2,2)),
]

def make_grid(n):
    nodes=[(c,r) for c in range(n) for r in range(3)]
    neighbors={u:tuple(v for v in nodes if abs(u[0]-v[0])+abs(u[1]-v[1])==1) for u in nodes}
    return nodes,neighbors

def closure(seed, neighbors, stop_after=None):
    blue=set(seed)
    history=[set(blue)]
    while True:
        targets=set()
        for u in sorted(blue):
            white=[v for v in neighbors[u] if v not in blue]
            if len(white)==1: targets.add(white[0])
        if not targets: break
        blue |= targets
        history.append(set(blue))
        if stop_after is not None and len(history)>=stop_after: break
    return blue,history

def graph_info(sets):
    edges=[(i,j) for i,j in combinations(range(len(sets)),2) if len(set(sets[i]).intersection(sets[j]))==2]
    adj=[set() for _ in sets]
    for i,j in edges: adj[i].add(j);adj[j].add(i)
    components=[];seen=set();diameters=[];radii=[]
    for s in range(len(sets)):
        if s in seen:continue
        q=[s];seen.add(s)
        for u in q:
            for v in adj[u]:
                if v not in seen:seen.add(v);q.append(v)
        components.append(set(q))
        eccentricities=[]
        for u in q:
            dist={u:0};dq=deque([u])
            while dq:
                a=dq.popleft()
                for b in adj[a]:
                    if b not in dist:dist[b]=dist[a]+1;dq.append(b)
            assert len(dist)==len(q)
            eccentricities.append(max(dist.values()))
        diameters.append(max(eccentricities));radii.append(min(eccentricities))
    return len(edges),sorted([len(c) for c in components]),sorted(diameters),sorted(radii), Counter(len(a) for a in adj)

nodes5,N5=make_grid(5)
left=[x for x in combinations([v for v in nodes5 if v[0]<=2],3) if len(closure(x,N5)[0])==15]
assert left==L_EXPECTED,(len(left),left)
EXPECTED_ROUNDS=[2,3,5,3,3,4,4,3,5,4,4,5,5]
for k,B in enumerate(left):
    _,history=closure(B,N5)
    first_three=frozenset((c,r) for c in range(3) for r in range(3))
    index=next(i for i,X in enumerate(history) if first_three.issubset(X))
    assert index==EXPECTED_ROUNDS[k] and all(v[0]<3 for v in history[index]),(B,index,history[index])
E_EXPECTED=[(0,1),(0,2),(0,3),(0,4),(0,7),(0,8),(1,2),(1,5),(1,7),(2,6),(3,4),(3,5),(3,6),(4,9),(4,10),(5,6),(5,11),(6,11),(7,8),(7,9),(8,10),(9,10),(9,12),(10,12)]
assert [(i,j) for i,j in combinations(range(13),2) if len(set(left[i])&set(left[j]))==2]==E_EXPECTED
assert graph_info(left)==(24,[13],[5],[3],Counter({4:8,3:2,2:2,6:1})),graph_info(left)
for n in range(3,13):
    nodes,N=make_grid(n)
    all_sets=[x for x in combinations(nodes,3) if len(closure(x,N)[0])==3*n]
    edges,components,diameters,radii,degrees=graph_info(all_sets)
    if n==3: expected=(20,44,[20],[4],[3])
    elif n==4: expected=(26,56,[26],[6],[4])
    else: expected=(26,48,[13,13],[5,5],[3,3])
    assert (len(all_sets),edges,components,diameters,radii)==expected,(n,len(all_sets),edges,components,diameters,radii)
    if n>=5:
        right=[tuple(sorted((n-1-c,r) for c,r in B)) for B in left]
        assert set(all_sets)==set(left)|set(right) and len(set(left)&set(right))==0
    print(f'n={n}: bases={len(all_sets)} edges={edges} components={components} diameters={diameters} radii={radii}')
print('boundary_table=13, cap=5 rounds; F edges=24, diameter=5, radius=3')
print('VERIFY_OK')
