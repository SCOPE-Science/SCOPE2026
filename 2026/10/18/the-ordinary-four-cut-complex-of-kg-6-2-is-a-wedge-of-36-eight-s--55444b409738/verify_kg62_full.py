"""Exact homotopy certificate for the four-cut complex of KG(6,2).
Requires standard Python 3 only. Run `python verify_kg62_full.py`.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

labels = tuple(combinations(range(6), 2))
assert len(labels) == 15
adj = tuple(sum(1 << j for j, v in enumerate(labels)
                if i != j and set(u).isdisjoint(v))
            for i, u in enumerate(labels))

def connected(subset):
    """Induced connectivity on a nonempty tuple of vertex indices."""
    available = sum(1 << i for i in subset)
    reached = 1 << subset[0]
    while True:
        new_reached = reached
        for i in subset:
            if reached & (1 << i):
                new_reached |= adj[i] & available
        if new_reached == reached:
            return reached == available
        reached = new_reached

foursets = tuple(combinations(range(15), 4))
disconnected = {sum(1 << i for i in c) for c in foursets if not connected(c)}
assert len(disconnected) == 615

# The Alexander dual consists of all sets containing no disconnected quadruple.
# Its complete simplicial faces (including the empty face) are exhaustively built.
dual_faces = {0}
face_counts = Counter({0:1})
for size in range(1, 8):
    total = 0
    for seq in combinations(range(15), size):
        s = sum(1 << i for i in seq)
        if all(s & obstruction != obstruction for obstruction in disconnected):
            dual_faces.add(s)
            total += 1
    face_counts[size] = total
assert [face_counts[k] for k in range(8)] == [1,15,105,455,750,492,70,0]
faces = dual_faces - {0}
assert len(faces) == 1887

# Vertex-toggle matching. The prescribed order is part of the certificate.
order = (8,1,5,9,11,3,14,13,12,2,6,10,0,7,4)
assert sorted(order) == list(range(15))
remaining = set(faces)
mate = {}
for i in order:
    bit = 1 << i
    for low in sorted(remaining, key=lambda m: (m.bit_count(),m)):
        if low & bit:
            continue
        high = low | bit
        if high in remaining:
            assert low in remaining
            remaining.remove(low)
            remaining.remove(high)
            mate[low] = high
            mate[high] = low
crit = Counter(m.bit_count()-1 for m in remaining)
assert crit == {0:1,4:36}, crit
assert len(mate) == 1850 and len(mate)//2 == 925

# Exhaustive acyclicity: reverse matched Hasse covers and topologically sort.
in_degree = {m:0 for m in faces}
arcs = {m:[] for m in faces}
covers = 0
for high in faces:
    if high.bit_count() < 2:
        continue
    for i in range(15):
        if high & (1 << i):
            low = high & ~(1 << i)
            assert low in faces
            if mate.get(low) == high:
                origin, target = low, high
            else:
                origin, target = high, low
            arcs[origin].append(target)
            in_degree[target] += 1
            covers += 1
queue = deque(s for s,v in in_degree.items() if v == 0)
visited = 0
while queue:
    s = queue.popleft()
    visited += 1
    for t in arcs[s]:
        in_degree[t] -= 1
        if not in_degree[t]:
            queue.append(t)
assert visited == len(faces), (visited,len(faces))

# Every 7-vertex subset has a disconnected quadruple. This guarantees
# a full seven-skeleton in the original cut complex.
for s in combinations(range(15), 7):
    mask = sum(1 << i for i in s)
    assert any(mask & q == q for q in disconnected), s

# Independent check: alternating Morse count agrees with full face vector.
euler_reduced = sum((-1)**(k-1)*face_counts[k] for k in range(8))
assert euler_reduced == 36
print('VERIFY_OK', 'connected_4sets=750', 'disconnected_4sets=615',
      'dual_nonempty_faces=1887', 'matched_pairs=925',
      'critical_vertex=1', 'critical_4cells=36',
      'hasse_covers='+str(covers),'DAG_nodes='+str(visited),
      'checked_7sets='+str(comb(15,7)), 'reduced_Euler=36')
