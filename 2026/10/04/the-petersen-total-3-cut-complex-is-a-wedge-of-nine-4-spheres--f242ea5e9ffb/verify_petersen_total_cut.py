#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque

V = tuple(range(10))
EDGES = {
    tuple(sorted(e)) for e in [
        (0,1),(1,2),(2,3),(3,4),(4,0),
        (0,5),(1,6),(2,7),(3,8),(4,9),
        (5,7),(7,9),(9,6),(6,8),(8,5),
    ]
}

def edge(a,b):
    return tuple(sorted((a,b))) in EDGES

def independent(S):
    return all(not edge(a,b) for a,b in combinations(S,2))

ind3 = [S for S in combinations(V,3) if independent(S)]
facets = [tuple(v for v in V if v not in S) for S in ind3]
assert len(ind3) == 30
assert len(set(facets)) == 30
assert all(len(F) == 7 for F in facets)

faces = set()
for F in facets:
    for r in range(1,len(F)+1):
        faces.update(combinations(F,r))
assert len(faces) == 790
face_vector = Counter(len(s)-1 for s in faces)
assert [face_vector[d] for d in range(7)] == [10,45,120,210,240,135,30]

# Sequential element matching, pivots 0,1,...,9.
# At pivot v, pair each currently unmatched sigma not containing v with sigma U {v},
# when both are faces and currently unmatched.
unmatched = set(faces)
pairs = []
for v in V:
    for s in sorted([x for x in unmatched if v not in x], key=lambda x:(len(x),x)):
        if s not in unmatched:
            continue
        t = tuple(sorted(s + (v,)))
        if t in unmatched:
            unmatched.remove(s)
            unmatched.remove(t)
            pairs.append((s,t))
assert len(pairs) == 390
critical = sorted(unmatched, key=lambda x:(len(x),x))
critical_dims = Counter(len(s)-1 for s in critical)
assert critical_dims == Counter({4:9,0:1})
assert critical[0] == (0,)

pairset = set(pairs)
assert len(pairset) == len(pairs)
used = set()
for lo,hi in pairs:
    assert len(hi) == len(lo)+1
    assert set(lo) < set(hi)
    assert lo in faces and hi in faces
    assert lo not in used and hi not in used
    used.add(lo); used.add(hi)
assert used.isdisjoint(unmatched)
assert len(used) + len(unmatched) == len(faces)

# Full Hasse diagram on nonempty faces.
covers = []
for hi in faces:
    if len(hi) >= 2:
        for i in range(len(hi)):
            lo = hi[:i] + hi[i+1:]
            covers.append((lo,hi))
assert len(covers) == 3510

# Forman orientation: unmatched covers point downward; matched covers point upward.
adj = {s: [] for s in faces}
indeg = {s: 0 for s in faces}
for lo,hi in covers:
    if (lo,hi) in pairset:
        a,b = lo,hi
    else:
        a,b = hi,lo
    adj[a].append(b)
    indeg[b] += 1
q = deque([s for s in faces if indeg[s] == 0])
seen = 0
while q:
    u = q.popleft(); seen += 1
    for w in adj[u]:
        indeg[w] -= 1
        if indeg[w] == 0:
            q.append(w)
assert seen == len(faces), "directed cycle in Morse orientation"

# Independent mod-2 boundary-rank check.
def rank_mod2(rows, ncols):
    rows = rows[:]
    rank = 0
    for c in range(ncols):
        p = next((i for i in range(rank,len(rows)) if (rows[i] >> c) & 1), None)
        if p is None:
            continue
        rows[rank], rows[p] = rows[p], rows[rank]
        for i in range(len(rows)):
            if i != rank and ((rows[i] >> c) & 1):
                rows[i] ^= rows[rank]
        rank += 1
    return rank

bydim = {d: sorted(s for s in faces if len(s)==d+1) for d in range(7)}
ranks = {}
for d in range(1,7):
    lower = bydim[d-1]
    upper = bydim[d]
    col_index = {s:j for j,s in enumerate(upper)}
    rows = []
    for lo in lower:
        bits = 0
        for j,hi in enumerate(upper):
            if set(lo).issubset(hi):
                bits |= (1 << j)
        rows.append(bits)
    ranks[d] = rank_mod2(rows, len(upper))
betti = []
for d in range(7):
    betti.append(len(bydim[d]) - ranks.get(d,0) - ranks.get(d+1,0))
assert betti == [1,0,0,0,9,0,0]

print("PETERSEN_TOTAL_3_CUT_VERIFY_OK")
print("independent_triples=30 facets=30 nonempty_faces=790 hasse_covers=3510 morse_pairs=390")
print("critical_dims=" + repr(dict(sorted(critical_dims.items()))))
print("mod2_betti=" + repr(betti))
