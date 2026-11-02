#!/usr/bin/env python3
"""Independent complete 3-round logical types of double line Johnson graphs."""
from itertools import combinations

def graph(n,k):
    pts = list(combinations(range(n),k))
    links=[]
    for i,a in enumerate(pts):
        sa=set(a)
        for j in range(i+1,len(pts)):
            if len(sa.intersection(pts[j])) == k-1:
                links.append((i,j))
    # Build line graph independently of any bitset construction.
    link_endpoint_sets = [set(e) for e in links]
    return [tuple(int(i!=j and bool(x.intersection(y)))
                  for j,y in enumerate(link_endpoint_sets))
            for i,x in enumerate(link_endpoint_sets)]

def diagram(g, verts):
    return (tuple(int(a==b) for a,b in combinations(verts,2)),
            tuple(g[a][b] for a,b in combinations(verts,2)))

def three_round_theory(g):
    N=len(g)
    # For a rooted pair, list every third-vertex quantifier-free type, including
    # choices equal to an earlier pebble. Then collect every second-move type,
    # and finally collect every first-move type (full 3-round back-and-forth).
    rooted=set()
    for x in range(N):
        options=set()
        for y in range(N):
            continuations=frozenset(diagram(g,(x,y,z)) for z in range(N))
            options.add((diagram(g,(x,y)),continuations))
        rooted.add(frozenset(options))
    return frozenset(rooted)

REPS={"small":(4,2),"middle":(5,2),"stable":(6,2)}
theories={name:three_round_theory(graph(*par)) for name,par in REPS.items()}
assert len(set(theories.values()))==3
for n,k in [(6,3),(7,2),(7,3),(8,2)]:
    g=graph(n,k)
    assert three_round_theory(g)==theories['stable'],(n,k)
    print('STABLE_PASS',n,k,'line_vertices',len(g))
for name,par in REPS.items():
    print('REP_PASS',name,par,'line_vertices',len(graph(*par)))
print('EF_RECURSION_PASS; representatives=3; supplementary=4; distinct_theories=3')
