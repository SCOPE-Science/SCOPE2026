#!/usr/bin/env python3
"""Independent Fano-coordinate and paired-hexagon verification."""
from itertools import combinations

# Fano points are nonzero vectors of GF(2)^3; a line is {u,v,u XOR v}.
points = set(range(1, 8))
lines = sorted({frozenset((u, v, u ^ v)) for u, v in combinations(sorted(points), 2)})
assert len(lines) == 7 and all(len(l) == 3 for l in lines)
line_index = {x: i for i, x in enumerate(lines)}
N = 14
E = {(p - 1, 7 + i) for i, l in enumerate(lines) for p in l}
assert len(E) == 21
adj = [set() for _ in range(N)]
for u,v in E:adj[u].add(v);adj[v].add(u)
assert all(len(z)==3 for z in adj)
assert all(len(adj[x]&adj[y])==1 for x in range(7) for y in range(x+1,7))
assert all(len(adj[x]&adj[y])==1 for x in range(7,14) for y in range(x+1,14))

# A triangle of Fano points gives one induced six-cycle: three point
# vertices and three side-line vertices. Exactly 28 are noncollinear.
triangles = []
cycles = []
for triple in combinations(sorted(points),3):
    sides = {line_index[frozenset((u,v,u^v))] for u,v in combinations(triple,2)}
    if len(sides) != 3: continue
    triangles.append(tuple(triple))
    verts = frozenset([p-1 for p in triple] + [7+i for i in sides])
    assert all(len(adj[u] & verts)==2 for u in verts)
    cycles.append(verts)
assert len(cycles)==28
assert len(set(cycles))==28

# Every cycle has precisely three disjoint mates, and the two omitted
# vertices are incident and touch each cycle exactly once.
ordered_pairs = []
for a in cycles:
    mates = [b for b in cycles if a.isdisjoint(b)]
    assert len(mates)==3
    for b in mates:
        rest = set(range(N)) - a - b
        assert len(rest)==2
        u,v = sorted(rest)
        assert v in adj[u]
        assert all(len(adj[x] & a)==1 and len(adj[x] & b)==1 for x in rest)
        ordered_pairs.append((a,b,tuple(sorted(rest))))
assert len(ordered_pairs)==84

# An admissible order on an induced hexagon grows a single cyclic arc.
# Generate orders by search from *all* first vertices; there are 96.
def arc_orders(cycle):
    C=set(cycle)
    out=[]
    def rec(chosen,order):
        if len(order)==6:
            out.append(tuple(order));return
        choices=[u for u in C-chosen if len(adj[u] & chosen)==1] if len(chosen)<5 else list(C-chosen)
        for u in choices:rec(chosen|{u},order+[u])
    for u in C:rec({u},[u])
    assert len(out)==96 and len(set(out))==96
    return out

for C in cycles:
    arc_orders(C)

# Check a concrete full layout for each ordered pair, independent of
# the subset-DP verifier; the theorem then enumerates all choices.
def boundary(chosen):
    return sum((u in chosen)!=(v in chosen) for u,v in E)
profile = [0,3,4,5,6,7,6,7,6,7,6,5,4,3,0]
for a,b,rest in ordered_pairs:
    left = arc_orders(a)[0]
    right = arc_orders(b)[0]
    order = list(left) + list(rest) + list(reversed(right))
    chosen=set()
    for k,u in enumerate(order,1):
        chosen.add(u)
        assert boundary(chosen)==profile[k], (k, chosen)
assert len(ordered_pairs)*2*96*96 == 1548288
print('FANO_DISJOINT_HEXAGON_STRUCTURE_PASS')
print('Fano_triangles=28 disjoint_ordered_pairs=84')
print('arc_orders_per_hexagon=96 middle_orders=2 total=1548288')
