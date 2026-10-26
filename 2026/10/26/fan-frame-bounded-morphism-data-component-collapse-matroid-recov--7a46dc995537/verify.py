#!/usr/bin/env python3
"""Finite verification for fan-frame morphisms from graph incidence posets."""
from itertools import product, permutations, combinations
from collections import Counter, defaultdict

def components(v, edges):
    parent=list(range(v))
    def root(i):
        while i!=parent[i]: i=parent[i]
        return i
    for a,b in edges:
        a,b=root(a),root(b)
        parent[a]=b
    return len({root(i) for i in range(v)})

def direct(v,edges,m):
    """Enumerate all maps, checking BOTH Kripke back and forth conditions."""
    e=len(edges); n=v+e; rights=[set([i]) for i in range(n)]
    for j,(a,b) in enumerate(edges): rights[v+j].update((a,b))
    count=0; cut=Counter()
    for f in product(range(m+1),repeat=n):
        if any(f[x] and any(f[y]!=f[x] for y in rights[x]) for x in range(n)):
            continue
        if any(f[x]==0 and not all(any(f[y]==color for y in rights[x]) for color in range(1,m+1)) for x in range(n)):
            continue
        count+=1
        if m==2:
            cut[tuple(j for j in range(e) if f[v+j]==0)]+=1
    return count,cut

def formula(v,edges,m):
    return (2**v if m==2 else m**components(v,edges))

def predicted_cut(v,edges):
    out=Counter()
    for colors in product((1,2),repeat=v):
        out[tuple(j for j,(a,b) in enumerate(edges) if colors[a]!=colors[b])]+=1
    return out

def canonical(v,edges):
    return min(tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in edges)) for p in permutations(range(v)))

def graph_classes(v, max_points):
    all_edges=[(a,b) for a in range(v) for b in range(a+1,v)]
    canonical_reps={}
    for k in range(min(len(all_edges),max_points-v)+1):
        for chosen in combinations(all_edges,k):
            edges=list(chosen)
            canonical_reps[canonical(v,edges)]=edges
    return list(canonical_reps.values())

cases=[
 (4,[(0,1),(2,3)]), (4,[(0,1),(1,2)]),
 (4,[(0,1),(1,2),(2,3)]), (4,[(0,1),(0,2),(0,3)]),
 (3,[(0,1),(1,2),(0,2)]), (4,[(0,1),(0,2),(1,2),(2,3)]),
 (5,[(0,1),(1,2),(2,3),(3,4)])
]
checks=0
for v,edges in cases:
    for m in ([2,3,4,5] if v+len(edges)<=7 else [2]):
        got,marked=direct(v,edges,m)
        expected=formula(v,edges,m)
        assert got==expected,(v,edges,m,got,expected)
        if m==2:assert marked==predicted_cut(v,edges)
        checks+=1
# Verify smallest collision in the graph-incidence family by independent isomorphism classification.
classes=[]
for v in range(1,7):
    classes.extend((v,tuple(edges),components(v,edges)) for edges in graph_classes(v,6))
groups=defaultdict(list)
for v,edges,c in classes:
    groups[(v+len(edges),v,c)].append(edges)
assert all(len(members)==1 for (n,v,c),members in groups.items() if n<6)
assert len(groups[(6,4,2)])==2
assert {canonical(4,edges) for edges in groups[(6,4,2)]}=={
    canonical(4,[(0,1),(2,3)]),canonical(4,[(0,1),(1,2)])}
# Cut polynomials of all forests with same edge count and component count coincide.
for v,edges in cases[:4]:
    assert predicted_cut(v,edges)==Counter({cut:2**components(v,edges) for cut in product((0,1),repeat=len(edges)) for cut in [tuple(i for i,x in enumerate(cut) if x)]})
# Triangle edge-marked spectrum has 4 even cuts, each multiplicity 2.
triangle=predicted_cut(3,[(0,1),(1,2),(0,2)])
assert len(triangle)==4 and set(map(len,triangle))=={0,2} and set(triangle.values())=={2}
print('ALL_CHECKS_PASS')
print(f'direct_bounded_morphism_comparisons={checks}')
print('smallest_collision_size=6; graph_vertex_count=4; graph_edge_count=2; graph_component_count=2')
print('six_world_collision_all_targets_m>=2; two-fan_count=16; m>=3_count=m^2')
print('four_vertex_connected_tree_pair_refined_polynomial=2*(1+z0)*(1+z1)*(1+z2)')
print(f'unlabelled_graph_classes_examined={len(classes)}')

def normalized_cut(v, edges):
    cuts=list(predicted_cut(v,edges).keys())
    e=len(edges)
    return min(tuple(sorted(sum(1<<p[j] for j in cut) for cut in cuts)) for p in permutations(range(e)))

classes8=[]
for v in range(1,9):
    classes8.extend((v,tuple(edges),components(v,edges)) for edges in graph_classes(v,8))
groups8=defaultdict(list)
for v,edges,c in classes8:
    groups8[(v+len(edges),v,c)].append((edges,normalized_cut(v,edges)))
sep=[]
for (size,v,c), members in groups8.items():
    if len({canonical(v,edges) for edges,_ in members})>=2 and len({cut for _,cut in members})>=2:
        sep.append((size,v,c))
assert sep and min(s[0] for s in sep)==8, sep
assert (8,4,1) in sep
cycle4=[(0,1),(1,2),(2,3),(0,3)]
paw=[(0,1),(1,2),(0,2),(2,3)]
assert normalized_cut(4,cycle4)!=normalized_cut(4,paw)
print('first_scalar_collision_resolved_by_marked_data=8')
print(f'unlabelled_graph_classes_examined_up_to_eight_points={len(classes8)}')
