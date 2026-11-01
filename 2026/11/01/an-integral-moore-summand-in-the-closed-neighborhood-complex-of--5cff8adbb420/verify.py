"""Exact finite homotopy certificate for the closed-neighborhood complex of Paley(13).

Run: python verify.py
Requires SymPy (see requirements.txt). No network or external data needed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

P = 13
Q = {x*x % P for x in range(1, P)}
assert Q == {1, 3, 4, 9, 10, 12}
BALLS = [sum(1 << y for y in range(P)
             if y == x or (y-x) % P in Q) for x in range(P)]
assert len(set(BALLS)) == 13
assert all(b.bit_count() == 7 for b in BALLS)

# Faces: all subsets of the thirteen seven-vertex closed neighborhoods.
faces = {0}
for b in BALLS:
    sub = [0]
    for j in range(P):
        if b >> j & 1:
            sub += [s | (1 << j) for s in sub]
    faces.update(sub)
faces = sorted(faces)
face_set = set(faces)
fvector = tuple(sum(m.bit_count() == k for m in faces) for k in range(P+1))
assert len(faces) == 1171
assert fvector[:8] == (1, 13, 78, 286, 416, 273, 91, 13)
assert sum(fvector[8:]) == 0
assert all((m & (m-1)) in face_set for m in faces if m)

# Deterministic repeated vertex-toggle matching. Selection uses the number of
# available pairs; tie-break by the largest vertex label.
remain = face_set.copy()
pairs = []
order = []
for _ in range(P):
    score = []
    for v in range(P):
        if v in order:
            continue
        bit = 1 << v
        count = sum((m | bit) in remain for m in remain if not (m & bit))
        score.append((count, v))
    count, v = max(score)
    order.append(v)
    bit = 1 << v
    new_pairs = [(m, m | bit) for m in sorted(remain)
                 if not (m & bit) and (m | bit) in remain]
    assert len(new_pairs) == count
    for a, b in new_pairs:
        remain.remove(a)
        remain.remove(b)
    pairs.extend(new_pairs)
assert order == [12, 10, 5, 7, 2, 4, 11, 6, 9, 3, 0, 8, 1]
assert len(pairs) == 579
assert len(remain) == 13
crit2 = sorted(f for f in remain if f.bit_count() == 3)
crit3 = sorted(f for f in remain if f.bit_count() == 4)
assert (len(crit2), len(crit3)) == (6, 7)
assert not (remain - set(crit2) - set(crit3))
assert sum(len(pair) == 2 for pair in pairs) == 579
assert (0, 1 << order[0]) in pairs  # empty simplex paired to a vertex, producing a basepoint

# Global acyclicity, not merely each toggle stage: reverse ALL matched
# codimension-one arrows, then topologically sort the complete Hasse graph.
ids = {f: i for i, f in enumerate(faces)}
match_up = {a: b for a, b in pairs}
indeg = [0] * len(faces)
arcs = [[] for _ in faces]
incidences = 0
for upper in faces:
    for v in range(P):
        if not (upper >> v & 1):
            continue
        lower = upper ^ (1 << v)
        assert lower in ids
        if match_up.get(lower) == upper:
            source, target = ids[lower], ids[upper]
        else:
            source, target = ids[upper], ids[lower]
        arcs[source].append(target)
        indeg[target] += 1
        incidences += 1
assert incidences == 4693
queue = deque(i for i, d in enumerate(indeg) if d == 0)
seen = 0
while queue:
    x = queue.popleft()
    seen += 1
    for y in arcs[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
assert seen == len(faces), 'directed cycle in the proposed Morse matching'

# Signed reduced Morse differential C3 -> C2. Each original face receives
# ascending orientations by increasing vertex label.
@lru_cache(None)
def boundary(f):
    verts = [v for v in range(P) if f >> v & 1]
    return tuple((f ^ (1 << v), (-1) ** i) for i, v in enumerate(verts))

matched_upper = {b for _, b in pairs}
@lru_cache(None)
def projection(f):
    if f in match_up:
        upper = match_up[f]
        bd = boundary(upper)
        incidence = dict(bd)[f]  # either +1 or -1
        assert abs(incidence) == 1
        out = Counter()
        for g, sgn in bd:
            if g != f:
                for h, coeff in projection(g).items():
                    out[h] -= incidence * sgn * coeff
        return {h: c for h, c in out.items() if c}
    if f in matched_upper:
        return {}  # paired to a lower-dimensional face
    assert f in crit2
    return {f: 1}

columns = []
for upper in crit3:
    out = Counter()
    for f, sgn in boundary(upper):
        for h, c in projection(f).items():
            out[h] += sgn * c
    columns.append([out[h] for h in crit2])
M = Matrix(6, 7, lambda i, j: columns[j][i])
expected = Matrix([
    [ 0, 0,  0,-1, 0, 0,-1],
    [ 0, 0, -1, 0, 1, 0, 0],
    [ 0, 1,  0, 0, 0,-1, 0],
    [-1, 1, -1,-1,-1, 1, 0],
    [-1, 0,  0, 0, 0, 0,-1],
    [ 0, 0,  1, 0,-1, 0, 0]])
assert M == expected
D = smith_normal_form(M, domain=ZZ)
assert [D[i, i] for i in range(6)] == [1, 1, 1, 1, 2, 0]

# A separate construction of the original integral oriented boundary
# matrices, with modular column elimination for homological cross-checks.
levels = defaultdict(list)
for f in faces:
    levels[f.bit_count()].append(f)
for k in levels:
    levels[k].sort()

def raw_rank(k, prime):
    rows = {f: i for i, f in enumerate(levels[k-1])}
    pivots = {}
    rank = 0
    for upper in levels[k]:
        col = {rows[f]: sgn % prime for f, sgn in boundary(upper)}
        while col:
            i = min(col)
            if i not in pivots:
                inv = pow(col[i], -1, prime)
                pivots[i] = {j: (a * inv) % prime for j, a in col.items()}
                rank += 1
                break
            pivot_coefficient = col[i]
            for j, a in pivots[i].items():
                val = (col.get(j, 0) - pivot_coefficient * a) % prime
                if val: col[j] = val
                else: col.pop(j, None)
    return rank

for prime, expected_betti in [(2, (2, 3)), (3, (1, 2)), (5, (1, 2))]:
    ranks = {k: raw_rank(k, prime) for k in range(1, 8)}
    assert [ranks[k] for k in range(1, 8)] == [1, 12, 66, 218 if prime == 2 else 219, 195, 78, 13]
    betti = {d: len(levels[d+1]) - ranks.get(d+1, 0) - ranks.get(d+2, 0)
             for d in range(0, 7)}
    assert (betti[2], betti[3]) == expected_betti
    assert all(betti[d] == 0 for d in [0, 1, 4, 5, 6])

print('FACES_OK',fvector[:8])
print('MATCHING_OK',len(pairs),'critical',{'two':len(crit2),'three':len(crit3)})
print('ACYCLIC_OK',len(faces),incidences)
print('INTEGRAL_MORSE_OK',list(D.diagonal()))
print('RAW_FIELD_HOMOLOGY_OK', {2:(2,3),3:(1,2),5:(1,2)})
print('HOMOTOPY_OK Moore(Z/2,2) wedge S2 wedge 2*S3')
print('ALL_VERIFY_OK')
