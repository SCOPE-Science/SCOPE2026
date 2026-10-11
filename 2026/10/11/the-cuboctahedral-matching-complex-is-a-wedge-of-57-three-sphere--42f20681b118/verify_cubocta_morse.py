"""Exact cellular certificate for the ordinary cuboctahedral matching complex.
Requires Python 3 standard library only. Run: python3 verify_cubocta_morse.py.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

# The cube has binary vertices 0,...,7, with edges differing in one bit.
cube_edges = [(a, b) for a in range(8) for b in range(a + 1, 8)
              if (a ^ b) in (1, 2, 4)]
assert len(cube_edges) == 12
# Each cube edge is a vertex of the cuboctahedron; two such vertices
# are adjacent precisely when their original cube edges meet.
poly_edges = [(i, j) for i in range(12) for j in range(i + 1, 12)
              if set(cube_edges[i]) & set(cube_edges[j])]
assert len(poly_edges) == 24
assert {sum(i in e for e in poly_edges) for i in range(12)} == {4}
size = len(poly_edges)
conflict = [sum(1 << j for j, f in enumerate(poly_edges)
                if i != j and set(e) & set(f))
            for i, e in enumerate(poly_edges)]
# Bit masks encode matchings of the cuboctahedral graph.
all_faces = [0]
for vertex in range(size):
    all_faces += [mask | (1 << vertex) for mask in all_faces[:]
                  if not mask & conflict[vertex]]
assert len(all_faces) == len(set(all_faces)) == 2649
faces = set(all_faces) - {0}
face_vector = [sum(mask.bit_count() == k for mask in faces)
               for k in range(1, 7)]
assert face_vector == [24, 204, 744, 1116, 528, 32], face_vector

# Sequential vertex toggles, restricted at each step to the still
# unmatched nonempty faces. This is a matching on the ordinary face poset.
unmatched = set(faces)
pairs = []
for pivot in range(size):
    stage = [(low, low | (1 << pivot)) for low in unmatched
             if not (low & (1 << pivot))
             and (low | (1 << pivot)) in unmatched]
    for low, high in stage:
        unmatched.remove(low)
        unmatched.remove(high)
    pairs.extend(stage)
assert len(pairs) == 1287
crit_count = Counter(mask.bit_count() - 1 for mask in unmatched)
assert crit_count == {0: 1, 3: 65, 4: 8}, crit_count

# Test the COMPLETE oriented Hasse diagram, not just the gradient subgraph.
paired = set(pairs)
indeg = dict.fromkeys(faces, 0)
arcs = {f: [] for f in faces}
for high in faces:
    for j in range(size):
        if high & (1 << j):
            low = high ^ (1 << j)
            if low == 0:
                continue
            if (low, high) in paired:
                src, dst = low, high
            else:
                src, dst = high, low
            arcs[src].append(dst)
            indeg[dst] += 1
number_arcs = sum(map(len, arcs.values()))
assert number_arcs == 9936, number_arcs
pending = deque(f for f, d in indeg.items() if d == 0)
visited = 0
while pending:
    src = pending.popleft()
    visited += 1
    for dst in arcs[src]:
        indeg[dst] -= 1
        if indeg[dst] == 0:
            pending.append(dst)
assert visited == len(faces) == 2648, (visited, len(faces))

# Compute the SIGNED integral Morse boundary via gradient paths. In
# degree 3 a critical 3-face survives, an upper-paired 3-face dies,
# and a lower-paired 3-face is recursively replaced using its 4-coface.
low_to_high = {low: high for low, high in pairs if high.bit_count() == 5}
upper_3 = {high for low, high in pairs if high.bit_count() == 4}
critical3 = sorted(f for f in unmatched if f.bit_count() == 4)
critical4 = sorted(f for f in unmatched if f.bit_count() == 5)
critical3_set = set(critical3)

@lru_cache(maxsize=None)
def oriented_facets(simplex):
    return tuple((simplex ^ (1 << j),
                  -1 if ((simplex & ((1 << j) - 1)).bit_count() % 2) else 1)
                 for j in range(size) if simplex & (1 << j))

@lru_cache(maxsize=None)
def reduce_face(simplex):
    if simplex in critical3_set:
        return {simplex: 1}
    if simplex in upper_3:
        return {}
    assert simplex in low_to_high, hex(simplex)
    upper = low_to_high[simplex]
    facets = oriented_facets(upper)
    incidence = next(s for f, s in facets if f == simplex)
    ans = defaultdict(int)
    for other, s in facets:
        if other != simplex:
            for crit, mult in reduce_face(other).items():
                ans[crit] -= incidence * s * mult
    return {f: x for f, x in ans.items() if x}

positions = {f: i for i, f in enumerate(critical3)}
matrix = [[0] * len(critical4) for _ in critical3]
for col, top in enumerate(critical4):
    coefficient = defaultdict(int)
    for lower, sign in oriented_facets(top):
        for crit, mult in reduce_face(lower).items():
            coefficient[crit] += sign * mult
    for crit, value in coefficient.items():
        matrix[positions[crit]][col] = value

# Eight explicitly singled-out rows yield a diagonal unimodular 8x8
# minor. All eight four-cell attachments have independent unit degrees.
pivot_rows = [2, 15, 5, 40, 42, 19, 51, 56]
minor = [[matrix[i][j] for j in range(8)] for i in pivot_rows]
assert all(minor[i][j] == (minor[i][i] if i == j else 0)
           for i in range(8) for j in range(8)), minor
assert all(abs(minor[i][i]) == 1 for i in range(8)), minor
# No other nonzero cells occur except in dimensions 0, 3 and 4.
# The resulting wedge has 65-8=57 three-spheres.
print('VERIFY_OK graph=12v_24e faces=2648 face_vector=' + ','.join(map(str, face_vector))
      + ' matched_pairs=1287 critical=1,65,8 Hasse_arcs=9936 acyclic=true'
      + ' integral_Morse_minor=unimodular rank=8 wedge_S3=57')
