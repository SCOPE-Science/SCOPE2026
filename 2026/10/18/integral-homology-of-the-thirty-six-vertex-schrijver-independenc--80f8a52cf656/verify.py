#!/usr/bin/env python3
"""Exact finite verifier for integral-homology computation on SG(5,2)."""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

ORDER = [1,3,4,6,7,8,10,11,12,13,16,18,19,21,22,23,25,26,27,28,31,32,33,34,0,2,5,9,14,15,17,20,24,29,30,35]
CRITICAL = [446791680,6722945024,11045175296,11950113312,19549913088,23636475904,25849593856,47857696768]
F_VECTOR_AUGMENTED = (1,36,540,4476,22941,77256,177884,288696,338652,292700,188196,89484,30586,7092,996,64)

# Canonical graph: zero-based cyclic twelve-gon; lexicographic stable five-sets.
sets = [a for a in combinations(range(12),5) if all((b-a)%12 not in (1,11) for a,b in combinations(a,2))]
assert len(sets) == 36 and len(ORDER) == 36 and sorted(ORDER) == list(range(36))
closed = []
for a in sets:
    m = 0
    for j,b in enumerate(sets):
        if a==b or set(a).isdisjoint(b):
            m |= 1 << j
    closed.append(m)
assert Counter(m.bit_count()-1 for m in closed) == Counter({4:24,7:12})

# Independently obtain f-polynomial by deletion of a vertex and its closed neighborhood.
@lru_cache(None)
def count_polynomial(avail):
    if not avail: return (1,)
    v = max((j for j in range(36) if avail & (1<<j)), key=lambda j:(avail & closed[j]).bit_count())
    a = count_polynomial(avail & ~(1<<v))
    b = count_polynomial(avail & ~closed[v])
    out = [0]*max(len(a),len(b)+1)
    for i,c in enumerate(a): out[i] += c
    for i,c in enumerate(b): out[i+1] += c
    return tuple(out)
assert count_polynomial((1<<36)-1) == F_VECTOR_AUGMENTED

# Enumerate each independent set once using the increasing-order branch recursion.
faces = []
def build(avail, chosen):
    faces.append(chosen)
    while avail:
        bit = avail & -avail
        avail -= bit
        j = bit.bit_length()-1
        build(avail & ~closed[j], chosen | bit)
build((1<<36)-1,0)
assert len(faces) == sum(F_VECTOR_AUGMENTED) == 1519600
assert Counter(s.bit_count() for s in faces) == {j:v for j,v in enumerate(F_VECTOR_AUGMENTED)}
assert len(set(faces)) == len(faces)

# Explicit ordered vertex-pair matching on the augmented simplex poset.
live = set(faces)
matching = {}
for v in ORDER:
    bit = 1 << v
    removed = []
    for a in live:
        b = a | bit
        if not a & bit and b in live:
            assert a not in matching
            matching[a] = b
            removed.extend((a,b))
    assert len(removed) == len(set(removed))
    live.difference_update(removed)
assert len(matching) == 759796
assert live == set(CRITICAL)
assert Counter(s.bit_count()-1 for s in live) == Counter({6:6,8:2})

# Verify Forman acyclicity on *all* cover relations. Matched edges point up;
# unmatched edges point down. Kahn sorting then rules out every directed cycle.
indeg = {s:0 for s in faces}
incidences = 0
for upper in faces:
    bits = upper
    while bits:
        bit = bits & -bits
        bits -= bit
        lower = upper ^ bit
        incidences += 1
        if matching.get(lower) == upper:
            indeg[upper] += 1
        else:
            indeg[lower] += 1
queue = deque(s for s in faces if indeg[s] == 0)
processed = 0
while queue:
    s = queue.popleft()
    processed += 1
    if s in matching:
        top = matching[s]
        indeg[top] -= 1
        if indeg[top] == 0: queue.append(top)
    bits = s
    while bits:
        bit = bits & -bits
        bits -= bit
        low = s ^ bit
        if matching.get(low) == s: continue
        indeg[low] -= 1
        if indeg[low] == 0: queue.append(low)
assert processed == len(faces)
# With an acyclic augmented matching, the unmatched faces make the reduced
# Morse chain complex; all Morse differentials are zero by degree reasons.
assert sum((-1)**(j-1)*v for j,v in enumerate(F_VECTOR_AUGMENTED)) == 8
print('PASS SG(5,2): vertices=36, faces=1519600 (including empty), matched_pairs=759796, critical={6:6,8:2}, directed_cover_relations=%d, topological_sort=%d' % (incidences,processed))
print('Reduced integral homology: H_6=Z^6, H_8=Z^2, all others zero.')
