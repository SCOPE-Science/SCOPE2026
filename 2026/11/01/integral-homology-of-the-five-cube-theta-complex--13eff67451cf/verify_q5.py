"""Exact finite certificate for the independence complex of the 5-cube.

Only Python standard library required. Run: python verify_q5.py
The Kahn test checks every nonempty face and every codimension-one
cover of the entire face poset with matched edges oriented upward.
"""
from collections import Counter, deque
from hashlib import sha256
import json

DIM = 5
N = 1 << DIM
NEIGHBORS = [sum(1 << (v ^ (1 << bit)) for bit in range(DIM)) for v in range(N)]

def independent_faces(vertex, blocked, selected):
    if vertex == N:
        yield selected
        return
    if not (blocked >> vertex) & 1:
        yield from independent_faces(vertex + 1, blocked | NEIGHBORS[vertex], selected | (1 << vertex))
    yield from independent_faces(vertex + 1, blocked, selected)

faces = set(independent_faces(0, 0, 0))
assert len(faces) == 254475 and 0 in faces
assert all(not (NEIGHBORS[v] & s) for s in faces for v in range(N) if (s >> v) & 1)
nonempty = faces - {0}
assert len(nonempty) == 254474
face_counts = Counter(s.bit_count()-1 for s in nonempty)

# Pairing in increasing order of parity and then natural binary labels.
# All pairs are made ONLY among faces still unmatched at that stage.
order = sorted(range(N), key=lambda v: (v.bit_count() & 1, v))
unmatched = set(nonempty)
partner = {}
paired_by_pivot = []
for v in order:
    bit = 1 << v
    lowers = [s for s in unmatched if (s & bit) == 0 and (s | bit) in unmatched]
    for s in lowers:
        t = s | bit
        assert s in unmatched and t in unmatched and s != 0
        assert s not in partner and t not in partner
        partner[s] = t
        partner[t] = s
    for s in lowers:
        unmatched.remove(s)
        unmatched.remove(s | bit)
    paired_by_pivot.append(len(lowers))
assert len(partner) + len(unmatched) == len(nonempty)
assert len(partner) % 2 == 0
crit_counts = Counter(s.bit_count()-1 for s in unmatched)
assert crit_counts == {0:1, 5:1, 7:10}, crit_counts

# Exhaustive acyclicity certificate: orient matched cover edges upward,
# all other cover edges downward. Kahn topological sorting must exhaust.
indegree = dict.fromkeys(nonempty,0)
cover_count = 0
for s in nonempty:
    bits=s
    while bits:
        bit=bits & -bits
        bits-=bit
        t=s^bit
        if not t:
            continue
        assert t in nonempty
        cover_count += 1
        if partner.get(s) == t:
            indegree[s] += 1   # reversed matching edge t -> s
        else:
            indegree[t] += 1   # ordinary downward edge s -> t

queue=deque(s for s in nonempty if indegree[s] == 0)
visited=0
while queue:
    s=queue.popleft()
    visited+=1
    p=partner.get(s)
    if p is not None and (p & s) == s: # s lower in matched edge
        indegree[p]-=1
        if indegree[p] == 0:
            queue.append(p)
    bits=s
    while bits:
        bit=bits & -bits
        bits-=bit
        t=s^bit
        if not t or p==t: # s upper in matched edge; edge goes up
            continue
        indegree[t]-=1
        if indegree[t] == 0:
            queue.append(t)
assert visited == len(nonempty), (visited,len(nonempty))
assert all(v==0 for v in indegree.values())

# Forman's acyclic matching theorem gives a CW model with one 0-cell,
# one 5-cell and ten 7-cells. No consecutive cells => every cellular
# differential is zero, over Z. Alexander duality for 32 vertices gives
# Theta(Cube(5,1)) with H_24=Z, H_22=Z^10 (reduced) and no torsion.
summary={
    "dimension": DIM,
    "cube_vertices":N,
    "independent_faces_including_empty":len(faces),
    "independent_faces_by_dimension":dict(sorted(face_counts.items())),
    "pivot_order":order,
    "matched_pairs":len(partner)//2,
    "pairs_by_pivot":paired_by_pivot,
    "critical_faces_by_dimension":dict(sorted(crit_counts.items())),
    "critical_faces":sorted(unmatched),
    "directed_nonempty_hasse_vertices":len(nonempty),
    "directed_hasse_edges":cover_count,
    "topological_sort_visited":visited,
    "independence_reduced_integral_homology":{"5":1,"7":10},
    "theta_reduced_integral_homology":{"22":10,"24":1},
}
print(json.dumps(summary,sort_keys=True,separators=(',',':')))
print('VERIFY_OK')
