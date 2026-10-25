#!/usr/bin/env python3
"""Exact finite verification for the 2-independence complex of the four-cube.

Uses only Python's standard library. Vertices are integers 0..15, interpreted
as four-bit words; simplex orientations are increasing vertex order.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

N = 16
adj = [sum(1 << (v ^ (1 << j)) for j in range(4)) for v in range(N)]
faces = [mask for mask in range(1 << N)
         if all((adj[v] & mask).bit_count() <= 1 for v in range(N)
                if mask & (1 << v))]
face_set = set(faces)
fvector = Counter(m.bit_count() - 1 for m in faces if m)
assert len(faces) == 3055
assert [fvector[d] for d in range(8)] == [16, 120, 464, 964, 960, 440, 80, 10]
facets = [m for m in faces if all((m | (1 << v)) not in face_set
                for v in range(N) if not m & (1 << v))]
assert Counter(m.bit_count() - 1 for m in facets) == {3: 16, 5: 160, 7: 10}

# Sequential elementary matchings on the entire augmented face poset.
unmatched = set(faces)
pairs = {}  # upper simplex -> lower simplex
for v in range(N):
    bit = 1 << v
    for m in list(unmatched):
        if not m & bit and m | bit in unmatched:
            unmatched.remove(m)
            unmatched.remove(m | bit)
            pairs[m | bit] = m
critical = sorted(unmatched, key=lambda m: (m.bit_count(), m))
assert len(pairs) == 1514
assert len(critical) == 27
assert Counter(m.bit_count() - 1 for m in critical) == {3: 17, 4: 6, 5: 4}

# Complete acyclicity test (matched cover arrows are reversed).
index = {m: i for i, m in enumerate(faces)}
indegree = [0] * len(faces)
succ = [[] for _ in faces]
incidences = 0
for m in faces:
    if not m:
        continue
    for v in range(N):
        if not m & (1 << v):
            continue
        lo = m ^ (1 << v)
        a, b = (lo, m) if pairs.get(m) == lo else (m, lo)
        succ[index[a]].append(index[b])
        indegree[index[b]] += 1
        incidences += 1
queue = deque(i for i, d in enumerate(indegree) if d == 0)
visited = 0
while queue:
    i = queue.popleft()
    visited += 1
    for j in succ[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)
assert incidences == 13584 and visited == len(faces)

# Exact cellular Gaussian elimination with integer pivots +/-1.
boundary = {}
reverse = defaultdict(set)
for m in faces:
    if not m:
        continue
    dd = {m ^ (1 << v): (-1 if pos & 1 else 1)
          for pos, v in enumerate(v for v in range(N) if m & (1 << v))}
    boundary[m] = dd
    for t in dd:
        reverse[t].add(m)
# Store only the changes required to lift and project four-cycles.
records = []
for upper, lower in sorted(pairs.items(), key=lambda pr: (pr[0].bit_count(), pr[0])):
    pivot = boundary[upper][lower]
    assert pivot in (-1, 1)
    if upper.bit_count() == 5:
        rows = {x: boundary[x][lower] for x in reverse[lower] if x != upper}
        records.append((upper, lower, pivot, "upper4", rows))
    elif lower.bit_count() == 5:
        records.append((upper, lower, pivot, "lower4", dict(boundary[upper])))
    for x in list(reverse[lower]):
        if x == upper:
            continue
        factor = boundary[x][lower] // pivot
        for y, coeff in boundary[upper].items():
            new_coeff = boundary[x].get(y, 0) - factor * coeff
            if new_coeff:
                boundary[x][y] = new_coeff
                reverse[y].add(x)
            else:
                boundary[x].pop(y, None)
                reverse[y].discard(x)
    for x in list(reverse[upper]):
        boundary[x].pop(upper, None)
    reverse.pop(upper, None)
    for y in boundary[upper]:
        reverse[y].discard(upper)
    boundary.pop(upper)
    reverse.pop(lower, None)
    boundary.pop(lower, None)

assert len(boundary) == len(critical)
assert sorted(critical) == sorted(boundary)
crit4 = sorted(m for m in critical if m.bit_count() == 5)
crit3 = sorted(m for m in critical if m.bit_count() == 4)
crit5 = sorted(m for m in critical if m.bit_count() == 6)
assert crit4 == [5272, 10328, 10340, 37442, 49442, 49682]
assert crit5 == [26904, 26916, 38424, 38530]
assert {x: boundary[x] for x in crit4 if boundary[x]} == {
    49442: {49158: 1, 49162: -1},
    49682: {49158: -1, 49162: 1}}
assert {x: boundary[x] for x in crit5} == {
    26904: {10328: -1},
    26916: {10340: -1},
    38424: {5272: -1, 37442: -1, 49442: 1, 49682: 1},
    38530: {37442: 1}}
assert all(not boundary[x] for x in crit3)
# d5 has a unimodular 4-by-4 minor with rows 5272,10328,10340,37442.
rows = [5272, 10328, 10340, 37442]
minor = [[boundary[c].get(r, 0) for c in crit5] for r in rows]
det = sum((-1 if sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4)) % 2 else 1)
          * __import__('math').prod(minor[i][perm[i]] for i in range(4))
          for perm in permutations(range(4)))
assert abs(det) == 1
for c in crit5:
    total = defaultdict(int)
    for mid, coeff in boundary[c].items():
        for lo, coeff2 in boundary[mid].items():
            total[lo] += coeff * coeff2
    assert not any(total.values())

# Independent homology-rank check on the original simplicial complex mod 2.
face_by_dim = {d: sorted(m for m in faces if m.bit_count() == d + 1)
               for d in range(8)}
mod2_ranks = {}
for d in range(8):
    piv = {}
    for m in face_by_dim[d]:
        if d == 0:
            col = 1  # augmented H_0 boundary to the empty face
        else:
            targets = face_by_dim[d - 1]
            # Index lookup uses a dictionary once per degree.
            break
        while col:
            p = col.bit_length() - 1
            if p in piv:
                col ^= piv[p]
            else:
                piv[p] = col
                break
    if d > 0:
        target_idx = {m: i for i, m in enumerate(targets)}
        for m in face_by_dim[d]:
            col = 0
            for v in range(N):
                if m & (1 << v):
                    col ^= 1 << target_idx[m ^ (1 << v)]
            while col:
                p = col.bit_length() - 1
                if p in piv:
                    col ^= piv[p]
                else:
                    piv[p] = col
                    break
    mod2_ranks[d] = len(piv)
assert mod2_ranks == {0: 1, 1: 15, 2: 105, 3: 359, 4: 589,
                      5: 370, 6: 70, 7: 10}

# Lift the primitive critical-four-cell 5272 to an integral simplicial cycle.
z = {5272: 1}
for upper, lower, pivot, kind, neighbors in reversed(records):
    if kind == 'upper4':
        coefficient = -sum(z.get(x, 0) * a for x, a in neighbors.items()) // pivot
        if coefficient:
            z[upper] = coefficient
assert len(z) == 92 and max(abs(a) for a in z.values()) == 1
z_boundary = defaultdict(int)
for m, a in z.items():
    for pos, v in enumerate(v for v in range(N) if m & (1 << v)):
        z_boundary[m ^ (1 << v)] += a * (-1 if pos & 1 else 1)
assert not any(z_boundary.values())

def apply_group(mask, flip, perm):
    images = []
    for x in range(N):
        if mask & (1 << x):
            y = sum(((x >> j) & 1) << perm[j] for j in range(4)) ^ flip
            images.append(y)
    parity = sum(images[i] > images[j]
                 for i in range(len(images)) for j in range(i + 1, len(images))) % 2
    return sum(1 << y for y in images), (-1 if parity else 1)

def project_chain(chain):
    chain = dict(chain)
    for upper, lower, pivot, kind, bd in records:
        if kind == 'upper4':
            chain.pop(upper, None)
        elif kind == 'lower4':
            a = chain.pop(lower, 0)
            if a:
                for y, b in bd.items():
                    if y == lower:
                        continue
                    val = chain.get(y, 0) - a * b // pivot
                    if val:
                        chain[y] = val
                    else:
                        chain.pop(y, None)
    return chain

# All 384 signed Lefschetz traces and 384 integral H4 actions.
class_counts = Counter()
for perm in permutations(range(4)):
    inv = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
    perm_sign = -1 if inv & 1 else 1
    fixed_coord = sum(perm[i] == i for i in range(4))
    for flip in range(16):
        # Identify H4 action by transporting its explicit integral cycle.
        action = defaultdict(int)
        for m, a in z.items():
            m2, sg = apply_group(m, flip, perm)
            action[m2] += a * sg
        critical_action = project_chain(action)
        assert all(m in crit4 for m in critical_action)
        assert critical_action.get(49442, 0) == critical_action.get(49682, 0)
        degree = critical_action.get(5272, 0) + critical_action.get(49442, 0)
        assert degree == perm_sign

        # L = 1 - trace(H3) + trace(H4).
        lefschetz = 0
        for m in faces:
            if not m:
                continue
            m2, sg = apply_group(m, flip, perm)
            if m2 == m:
                lefschetz += sg * (-1 if (m.bit_count() - 1) & 1 else 1)
        trace_3 = 1 + perm_sign - lefschetz
        expected = fixed_coord
        for P in combinations(range(4), 2):
            if {perm[j] for j in P} != set(P):
                continue
            count_fixed_outside = sum(perm[b] == b for b in range(4) if b not in P)
            image_P = {perm[j] for j in P}
            parity_flip = sum((flip >> j) & 1 for j in image_P) % 2
            expected += (-1 if parity_flip else 1) * count_fixed_outside
        assert trace_3 == expected, (flip, perm, trace_3, expected)
        class_counts[(perm_sign, flip.bit_count())] += 1
assert sum(class_counts.values()) == 384
print('FACE_VECTOR', [fvector[d] for d in range(8)])
print('FACETS_BY_DIMENSION', dict(Counter(m.bit_count() - 1 for m in facets)))
print('MORSE_MATCHED_PAIRS', len(pairs), 'CRITICAL_CELLS', dict(Counter(m.bit_count() - 1 for m in critical)))
print('ACYCLIC_INCIDENCES', incidences)
print('EXACT_MORSE_MINOR_DETERMINANT', det)
print('MOD2_BOUNDARY_RANKS', [mod2_ranks[d] for d in range(8)])
print('INTEGRAL_CYCLE_FACES', len(z))
print('FULL_GROUP_ELEMENTS_VERIFIED', sum(class_counts.values()))
print('H3_RANK_16_H4_RANK_1; H4_COORDINATE_SIGN_CHAR; H3_V_PLUS_W_CHARACTER')
print('VERIFY_OK')
