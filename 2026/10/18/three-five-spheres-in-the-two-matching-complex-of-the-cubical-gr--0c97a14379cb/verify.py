#!/usr/bin/env python3
"""Exact face-poset matching certificate for the 2-matching complex of the cubical graph."""
from collections import Counter, deque
import json
import sys

N = 8
EDGES = tuple((u, u ^ (1 << axis)) for u in range(N) for axis in range(3)
              if u < (u ^ (1 << axis)))
assert len(EDGES) == 12 and len(set(EDGES)) == 12
STARS = tuple(sum(1 << i for i, (u, v) in enumerate(EDGES) if x in (u, v))
              for x in range(N))
assert all(s.bit_count() == 3 for s in STARS)

# Enumerate all and only nonempty edge sets of maximum induced degree at most two.
FACES = {mask for mask in range(1, 1 << len(EDGES))
         if all((mask & star) != star for star in STARS)}
by_dim = Counter(mask.bit_count() - 1 for mask in FACES)
assert [by_dim[k] for k in range(8)] == [12, 66, 212, 423, 516, 352, 108, 9]
assert len(FACES) == 1698

# Repeated face-poset vertex toggles, from the last edge to the first.
active = set(FACES)
paired = []
per_pivot = []
for i in reversed(range(len(EDGES))):
    bit = 1 << i
    this = []
    for lo in sorted(active):
        hi = lo | bit
        if not (lo & bit) and hi in active:
            active.remove(lo)
            active.remove(hi)
            this.append((lo, hi))
    paired.extend(this)
    per_pivot.append((i, len(this)))

critical = sorted(active)
assert len(paired) == 847 and len(critical) == 4
assert Counter(mask.bit_count() - 1 for mask in critical) == {0: 1, 5: 3}
assert len({x for lo, hi in paired for x in (lo, hi)}) == 1694
assert set(critical).isdisjoint(x for lo, hi in paired for x in (lo, hi))
assert all(hi == (lo | (hi ^ lo)) and (hi ^ lo).bit_count() == 1
           and (lo & hi) == lo for lo, hi in paired)

# Exhaustively check no closed gradient path: matched cover arrows ascend,
# unmatched cover arrows descend. Topological sorting checks acyclicity.
paired_set = set(paired)
indegree = {mask: 0 for mask in FACES}
adjacency = {mask: [] for mask in FACES}
cover_count = 0
for lo in FACES:
    for i in range(len(EDGES)):
        bit = 1 << i
        hi = lo | bit
        if not (lo & bit) and hi in FACES:
            cover_count += 1
            src, dst = ((lo, hi) if (lo, hi) in paired_set else (hi, lo))
            adjacency[src].append(dst)
            indegree[dst] += 1
queue = deque(sorted(mask for mask, deg in indegree.items() if deg == 0))
processed = 0
topo_order = []
while queue:
    mask = queue.popleft()
    topo_order.append(mask)
    processed += 1
    for nxt in adjacency[mask]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
assert processed == len(FACES)

# Separate modular chain rank calculation; it is not used to certify the
# homotopy result (which follows from the acyclic matching).
faces_by_dim = {k: sorted(mask for mask in FACES if mask.bit_count() == k + 1)
                for k in range(8)}
def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)
boundary_rank = {-1: 0, 0: 0, 8: 0}
for k in range(1, 8):
    rows = {mask: i for i, mask in enumerate(faces_by_dim[k - 1])}
    cols = []
    for mask in faces_by_dim[k]:
        col = 0
        for i in range(12):
            if mask & (1 << i):
                col ^= (1 << rows[mask ^ (1 << i)])
        cols.append(col)
    boundary_rank[k] = gf2_rank(cols)
betti = [by_dim[k] - boundary_rank[k] - boundary_rank[k + 1]
         for k in range(8)]
assert betti == [1, 0, 0, 0, 0, 3, 0, 0]
assert sum((-1)**k * by_dim[k] for k in range(8)) == -2

facets = [face for face in FACES if all((face | (1 << i)) not in FACES
          for i in range(12) if not (face & (1 << i)))]
assert Counter(face.bit_count() - 1 for face in facets) == {5: 4, 6: 36, 7: 9}

print('cubical edges:', EDGES)
print('vertex-star masks:', STARS)
print('nonempty face count:', len(FACES))
print('face vector f_0,...,f_7:', [by_dim[k] for k in range(8)])
print('facets by dimension:', sorted(Counter(face.bit_count() - 1 for face in facets).items()))
print('toggle pivot, number of matched pairs:', per_pivot)
print('matching pairs:', len(paired))
print('critical face masks (decimal):', critical)
print('critical dimensions:', [x.bit_count() - 1 for x in critical])
print('Hasse cover relations:', cover_count)
print('acyclic directed Hasse vertices checked:', processed)
print('boundary ranks mod 2:', [boundary_rank[k] for k in range(1, 8)])
print('unreduced Betti dimensions 0,...,7 mod 2:', betti)
print('Euler characteristic:', -2)
print('all checks passed')

# The certificate includes every face, matching pair and a topological order
# of the reoriented Hasse diagram, so its validity is independently decidable.
CERTIFICATE = {
    "graph_vertices": list(range(8)),
    "graph_edges": [list(edge) for edge in EDGES],
    "nonempty_faces": sorted(FACES),
    "morse_matching_pairs": [list(pair) for pair in paired],
    "critical_faces": critical,
    "directed_hasse_topological_order": topo_order,
}
if len(sys.argv) == 3 and sys.argv[1] == "--certificate":
    with open(sys.argv[2], "w", encoding="utf-8") as file:
        json.dump(CERTIFICATE, file, separators=(",", ":"), ensure_ascii=False)
        file.write("\n")
elif len(sys.argv) == 3 and sys.argv[1] == "--check-certificate":
    with open(sys.argv[2], "r", encoding="utf-8") as file:
        assert json.load(file) == CERTIFICATE, "certificate disagrees with independent recomputation"
    print("serialized face, pairing, and topological-order certificate: exact match")
elif len(sys.argv) != 1:
    raise SystemExit("usage: python verify.py [--certificate PATH | --check-certificate PATH]")
