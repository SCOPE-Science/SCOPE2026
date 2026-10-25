#!/usr/bin/env python3
"""Exact self-contained certificate for the binary projective three-space cap complex.

Requires Python >=3.9; standard library only. Run: python verify_pg32.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from itertools import combinations
from math import gcd

N = 15
points = tuple(range(1, 16))
lines = {frozenset((a, b, a ^ b)) for a, b in combinations(points, 2)}
assert len(lines) == 35 and all(len(line) == 3 for line in lines)
line_masks = tuple(sum(1 << (a - 1) for a in line) for line in lines)

# All nonempty faces, not just an experimental sample.
faces = {mask for mask in range(1, 1 << N)
         if all(mask & line != line for line in line_masks)}
assert len(faces) == 3048
face_counts = Counter(mask.bit_count() for mask in faces)
assert tuple(face_counts[k] for k in range(1, 9)) == (15, 105, 420, 945, 1008, 420, 120, 15)
assert all(face_counts[k] == 0 for k in range(9, 16))
maximal = [face for face in faces
           if all((face | (1 << i)) not in faces for i in range(N) if not (face >> i) & 1)]
assert Counter(m.bit_count() for m in maximal) == Counter({5: 168, 8: 15})

# Sequential lowest-coordinate toggle pairing: each simplex occurs in <=1 pair.
remaining = set(faces)
pairs = []
for bit_index in range(N):
    bit = 1 << bit_index
    batch = [(lower, lower | bit) for lower in sorted(remaining)
             if not lower & bit and (lower | bit) in remaining]
    for lower, upper in batch:
        assert lower in remaining and upper in remaining
        remaining.remove(lower)
        remaining.remove(upper)
        pairs.append((lower, upper))
assert len(pairs) == 1484
assert Counter(face.bit_count() - 1 for face in remaining) == Counter({0: 1, 3: 1, 4: 78})
assert [face for face in remaining if face.bit_count() == 1] == [1]
critical_three = next(face for face in remaining if face.bit_count() == 4)
assert critical_three == 534
critical_four = sorted(face for face in remaining if face.bit_count() == 5)
by_lower = dict(pairs)
by_upper = {upper: lower for lower, upper in pairs}
assert len(by_lower) == len(by_upper) == len(pairs)

# Verify acyclicity directly on the *entire* nonempty face-poset incidence graph.
paired = set(pairs)
successors = defaultdict(list)
indeg = {face: 0 for face in faces}
incidences = 0
for upper in faces:
    for i in range(N):
        if not upper & (1 << i):
            continue
        lower = upper ^ (1 << i)
        if not lower:
            continue
        start, end = ((lower, upper) if (lower, upper) in paired else (upper, lower))
        successors[start].append(end)
        indeg[end] += 1
        incidences += 1
assert incidences == 13770
queue = deque(face for face in faces if indeg[face] == 0)
visited = 0
while queue:
    face = queue.popleft()
    visited += 1
    for nxt in successors[face]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            queue.append(nxt)
assert visited == len(faces)

# For the canonical ascending vertex orientation, calculate the signed
# gradient-path projection of 3-faces onto the unique critical 3-cell.
def incidence(lower, upper):
    missing = upper ^ lower
    assert missing != 0 and (missing & (missing - 1)) == 0
    assert upper & missing and lower == upper ^ missing
    return -1 if (upper & (missing - 1)).bit_count() % 2 else 1

@lru_cache(maxsize=None)
def project(face):
    assert face.bit_count() == 4
    if face == critical_three:
        return 1
    if face in by_upper:  # Upper cell of a 2/3 pair, eliminated in degree 3.
        return 0
    assert face in by_lower
    upper = by_lower[face]
    assert upper.bit_count() == 5
    pivot = incidence(face, upper)  # Always +1 or -1.
    other = sum(incidence(upper ^ (1 << i), upper) * project(upper ^ (1 << i))
                for i in range(N) if upper & (1 << i) and (upper ^ (1 << i)) != face)
    return -pivot * other

coefficients = []
for upper in critical_four:
    value = sum(incidence(upper ^ (1 << i), upper) * project(upper ^ (1 << i))
                for i in range(N) if upper & (1 << i))
    coefficients.append(value)
assert Counter(coefficients) == Counter({0: 44, 2: 19, -2: 15})
assert reduce(gcd, coefficients, 0) == 2

# Independent boundary-rank check directly on the unreduced simplicial complex.
by_degree = {d: sorted(m for m in faces if m.bit_count() == d + 1) for d in range(8)}
def rank_mod2(d):
    index = {mask: i for i, mask in enumerate(by_degree[d - 1])}
    pivots = {}
    for upper in by_degree[d]:
        column = sum(1 << index[upper ^ (1 << i)] for i in range(N) if upper & (1 << i))
        while column:
            p = column.bit_length() - 1
            if p not in pivots:
                pivots[p] = column
                break
            column ^= pivots[p]
    return len(pivots)
assert [rank_mod2(d) for d in range(1, 8)] == [14, 91, 329, 615, 315, 105, 15]

def rank_mod3(d):
    index = {mask: i for i, mask in enumerate(by_degree[d - 1])}
    pivots = {}
    for upper in by_degree[d]:
        col = {index[upper ^ (1 << i)]:
               (-1 if (upper & ((1 << i) - 1)).bit_count() & 1 else 1)
               for i in range(N) if upper & (1 << i)}
        while col:
            p = max(col)
            if p not in pivots:
                factor = col[p]
                pivots[p] = {j: (v * factor) % 3 for j, v in col.items()}
                break
            factor = col[p]
            for j, v in pivots[p].items():
                new = (col.get(j, 0) - factor * v) % 3
                if new: col[j] = new
                else: col.pop(j, None)
    return len(pivots)
assert {d:rank_mod3(d) for d in (3, 4, 5)} == {3:329, 4:616, 5:315}

print('PROJECTIVE_LINES=35')
print('NONEMPTY_FACES=3048')
print('FACE_VECTOR=15,105,420,945,1008,420,120,15')
print('MAXIMAL_CAP_SIZES=5:168,8:15')
print('MATCHED_PAIRS=1484')
print('FACE_INCIDENCES=13770')
print('ACYCLIC_TOPOLOGICAL_SORT=3048/3048')
print('CRITICAL_CELLS=0:1,3:1,4:78')
print('MORSE_BOUNDARY_COEFFICIENTS=-2:15,0:44,2:19')
print('MORSE_BOUNDARY_GCD=2')
print('MOD2_BOUNDARY_RANKS=14,91,329,615,315,105,15')
print('MOD3_BOUNDARY_RANKS_3_4_5=329,616,315')
print('VERIFY_OK')
