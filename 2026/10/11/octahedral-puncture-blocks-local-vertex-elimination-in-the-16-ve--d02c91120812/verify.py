from itertools import combinations
from collections import Counter

FACETS = [
(1,2,4,9),(1,2,4,15),(1,2,6,14),(1,2,6,15),(1,2,9,14),(1,3,4,12),(1,3,4,15),(1,3,7,10),
(1,3,7,12),(1,3,10,15),(1,4,9,12),(1,5,6,13),(1,5,6,14),(1,5,8,11),(1,5,8,13),(1,5,11,14),
(1,6,13,15),(1,7,8,10),(1,7,8,11),(1,7,11,12),(1,8,10,13),(1,9,11,12),(1,9,11,14),(1,10,13,15),
(2,3,5,10),(2,3,5,11),(2,3,7,10),(2,3,7,13),(2,3,11,13),(2,4,9,13),(2,4,11,13),(2,4,11,15),
(2,5,8,11),(2,5,8,12),(2,5,10,12),(2,6,10,12),(2,6,10,14),(2,6,12,15),(2,7,9,13),(2,7,9,14),
(2,7,10,14),(2,8,11,15),(2,8,12,15),(3,4,5,14),(3,4,5,15),(3,4,12,14),(3,5,10,15),(3,5,11,14),
(3,7,12,13),(3,11,13,14),(3,12,13,14),(4,5,6,7),(4,5,6,14),(4,5,7,15),(4,6,7,11),(4,6,10,11),
(4,6,10,14),(4,7,11,15),(4,8,9,12),(4,8,9,13),(4,8,10,13),(4,8,10,14),(4,8,12,14),(4,10,11,13),
(5,6,7,13),(5,7,9,13),(5,7,9,15),(5,8,9,12),(5,8,9,13),(5,9,10,12),(5,9,10,15),(6,7,11,12),
(6,7,12,13),(6,10,11,12),(6,12,13,15),(7,8,10,14),(7,8,11,15),(7,8,14,15),(7,9,14,15),(8,12,14,15),
(9,10,11,12),(9,10,11,16),(9,10,15,16),(9,11,14,16),(9,14,15,16),(10,11,13,16),(10,13,15,16),
(11,13,14,16),(12,13,14,15),(13,14,15,16)
]
F = {tuple(sorted(t)) for t in FACETS}
assert len(F) == 90
V = sorted(set().union(*map(set,F)))
edges = {e for t in F for e in combinations(t,2)}
tris = {q for t in F for q in combinations(t,3)}
assert (len(V),len(edges),len(tris),len(F)) == (16,106,180,90)

vdeg = {v:sum(v in t for t in F) for v in V}
assert vdeg[16] == 8
assert [v for v in V if vdeg[v] == min(vdeg.values())] == [16]
assert sorted(vdeg.values()) == [8,18,18,20,22,24,24,24,24,24,24,26,26,26,26,26]

link16 = {tuple(x for x in t if x != 16) for t in F if 16 in t}
link_vertices = sorted(set().union(*map(set,link16)))
link_edges = {e for tri in link16 for e in combinations(tri,2)}
assert link_vertices == [9,10,11,13,14,15]
assert len(link16) == 8 and len(link_edges) == 12
opposite = sorted(e for e in combinations(link_vertices,2) if e not in link_edges)
assert opposite == [(9,13),(10,14),(11,15)]
assert all(e in edges for e in opposite)

# Each opposite edge already lies in a tetrahedron of the deletion K-{16}.
deleted_facets = [t for t in F if 16 not in t]
assert all(any(set(e).issubset(t) for t in deleted_facets) for e in opposite)

# The octahedral graph has no 4-clique. Therefore every tetrahedron on these
# six vertices contains at least one opposite pair. This exhaustively checks it.
for tet in combinations(link_vertices,4):
    assert any(set(e).issubset(tet) for e in opposite)

# Boundary triangles of the deletion are exactly link(16): count triangles in
# the remaining tetrahedra and select those incident to exactly one tetrahedron.
tri_count = Counter(q for t in deleted_facets for q in combinations(t,3))
boundary = {q for q,c in tri_count.items() if c == 1}
assert boundary == link16
assert all(c in (1,2) for c in tri_count.values())

print("VERIFY_OK f=16,106,180,90 vertex_tet_degrees=" + ",".join(map(str,sorted(vdeg.values()))) +
      " unique_min_vertex=16 min_degree=8 link16=octahedral link_vertices=9,10,11,13,14,15" +
      " opposite_edges=9-13,10-14,11-15 all_opposites_in_deletion=yes boundary_triangles=8" +
      " no_same_boundary_vertex_refill=yes")
