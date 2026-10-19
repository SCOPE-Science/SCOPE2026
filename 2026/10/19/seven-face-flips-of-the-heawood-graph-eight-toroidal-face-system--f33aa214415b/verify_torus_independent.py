#!/usr/bin/env python3
"""Independent cyclic-difference-set and bitmask verifier for Heawood face flips."""
from itertools import permutations,combinations
from collections import Counter,defaultdict,deque
# Fano plane from the cyclic (7,3,1) difference set, not the binary XOR model.
points=range(7)
blocks=[frozenset(((i+d)%7) for d in (0,1,3)) for i in range(7)]
assert len(set(blocks))==7
assert all(sum({a,b}<=X for X in blocks)==1 for a,b in combinations(points,2))
edge=[(p,7+j) for p in points for j in range(7) if p in blocks[j]]
assert len(edge)==21
edge_id={e:i for i,e in enumerate(edge)}
# all 7-edge matchings independently as permutations satisfying incidence.
match=[]
for pi in permutations(range(7)):
    if all(p in blocks[pi[p]] for p in points):
        match.append(sum(1<<edge_id[(p,7+pi[p])] for p in points))
match.sort();assert len(match)==24
mi={m:i for i,m in enumerate(match)}
# All girth-six circuits from triples of points/lines and degree equations.
cycles=set(); angles_by_cycle={}
for pp in combinations(range(7),3):
    for ll in combinations(range(7),3):
        edges=[edge_id[(p,7+j)] for p in pp for j in ll if (p,7+j) in edge_id]
        if len(edges)!=6:continue
        if any(sum((p,7+j) in edge_id for j in ll)!=2 for p in pp):continue
        if any(sum((p,7+j) in edge_id for p in pp)!=2 for j in ll):continue
        mask=sum(1<<e for e in edges)
        cycles.add(mask)
assert len(cycles)==28
cy=sorted(cycles)
# Angle incidence as unordered pairs of graph-edge IDs sharing a vertex.
ANGLES=set(); cover={}
for c in cy:
    turns=set()
    for v in range(14):
        nearby=[k for k,e in enumerate(edge) if v in e and c>>k&1]
        if len(nearby)==2:
            turns.add((v,*sorted(nearby)))
    assert len(turns)==6
    cover[c]=frozenset(turns)
    ANGLES|=turns
assert len(ANGLES)==42
# Seven-face systems are exactly covers of all 42 cubic vertex angles.
facesystems=set()
def dfs(rem,sel):
    if not rem:
        assert len(sel)==7
        facesystems.add(tuple(sorted(sel)));return
    possible={a: [c for c in cy if a in cover[c] and cover[c].issubset(rem)] for a in rem}
    a=min(rem,key=lambda k:len(possible[k]))
    for c in possible[a]:dfs(rem-cover[c],sel+[c])
dfs(frozenset(ANGLES),[])
assert len(facesystems)==8
factors={tuple(sorted(group)) for group in combinations(range(24),3) if
    all(not(match[x]&match[y]) for x,y in combinations(group,2))}
assert len(factors)==8
all_E=Counter();cycles_frequency=Counter();seen_frozen=set()
for f in facesystems:
    neighbors=[set() for _ in match]
    for c in f:
        cycles_frequency[c]+=1
        assert sum((m&c).bit_count()==3 for m in match)==6
        for u,m in enumerate(match):
            if (m&c).bit_count()==3:
                v=mi[m^c];neighbors[u].add(v)
                neighbors[v].add(u)
    verts=set(range(24));components=[]
    while verts:
        start=verts.pop();queue=deque([start]);cc={start}
        while queue:
            for v in neighbors[queue.popleft()]:
                if v in verts:verts.remove(v);cc.add(v);queue.append(v)
        components.append(cc)
    assert Counter(map(len,components))=={7:3,1:3}
    assert Counter(map(len,neighbors))=={0:3,2:21}
    isolated=tuple(sorted(i for i in range(24) if not neighbors[i]))
    assert isolated in factors
    seen_frozen.add(isolated)
    assert all(sum(k in neighbors[i] for k in group)==2 for group in components if len(group)==7 for i in group)
    assert len({tuple(sorted((i,k))) for i in range(24) for k in neighbors[i]})==21
    for i in range(24):
        for k in neighbors[i]:
            if k>i:all_E[i,k]+=1
assert seen_frozen==factors
assert len(all_E)==84 and set(all_E.values())=={2}
assert len(cycles_frequency)==28 and set(cycles_frequency.values())=={2}
print('VERIFY_INDEPENDENT_OK incidence_representation=cyclic_difference_set vertices=14 edges=21')
print('VERIFY_INDEPENDENT_OK perfect_matchings=24 6cycles=28 toroidal_angle_covers=8 1factorisations=8')
print('VERIFY_INDEPENDENT_OK each_face_flip_graph=3xC7_plus_3isolated 8_bijective_frozen_factorisations=true')
print('VERIFY_INDEPENDENT_OK 84_distinct_flip_pairs_each_used_twice 28_hexagons_each_face_twice=true')
