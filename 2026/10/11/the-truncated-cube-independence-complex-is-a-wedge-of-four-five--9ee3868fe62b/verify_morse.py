#!/usr/bin/env python3
"""Exact certificate for the truncated-cube independence-complex homotopy type.

Python 3 standard library only. All faces and every face-poset incidence are
regenerated; no canned simplex or boundary tables are loaded.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 24
# Darts of a cube: 3*b+i encodes cube corner b in {0,...,7} and
# one of its incident coordinate axes i in {0,1,2}.
EDGES = set()
for b in range(8):
    for i in range(3):
        for j in range(i+1,3):
            EDGES.add(tuple(sorted((3*b+i, 3*b+j))))
        EDGES.add(tuple(sorted((3*b+i, 3*(b ^ (1 << i))+i))))
assert len(EDGES) == 36
neighbors = [0] * N
for a, b in EDGES:
    neighbors[a] |= 1 << b
    neighbors[b] |= 1 << a
assert all(x.bit_count() == 3 for x in neighbors)

faces = []
def visit(start, mask):
    faces.append(mask)
    for v in range(start, N):
        if not (mask & neighbors[v]):
            visit(v+1, mask | (1 << v))
visit(0, 0)
assert len(faces) == 26441
fvector = [sum(mask.bit_count() == d+1 for mask in faces) for d in range(8)]
assert fvector == [24, 240, 1296, 4092, 7632, 8056, 4272, 828]

# Stagewise first-available toggles; every chosen pair is a cover relation.
remaining = set(faces)
match_up = {}
for v in range(N):
    bit = 1 << v
    pairs = [(s, s | bit) for s in sorted(remaining)
             if not (s & bit) and (s | bit) in remaining]
    for lo, hi in pairs:
        assert lo in remaining and hi in remaining
        remaining.remove(lo)
        remaining.remove(hi)
        match_up[lo] = hi
assert 0 in match_up
# Treat the empty simplex only as a bookkeeping cell; unmatch its paired
# vertex when passing to the ordinary (nonaugmented) face poset.
basepoint = match_up.pop(0)
assert basepoint.bit_count() == 1
critical = remaining | {basepoint}
assert Counter(s.bit_count()-1 for s in critical) == {0: 1, 5: 5, 6: 12}
match_down = {hi: lo for lo, hi in match_up.items()}
assert len(match_up) == 13211

# Exhaustive oriented Hasse diagram: matched covers up, all others down.
nonempty = [s for s in faces if s]
indegree = {s: 0 for s in nonempty}
outgoing = defaultdict(list)
incidences = 0
for hi in nonempty:
    bits = hi
    while bits:
        bit = bits & -bits
        bits ^= bit
        lo = hi ^ bit
        if lo == 0:
            continue
        u, w = (lo, hi) if match_up.get(lo) == hi else (hi, lo)
        outgoing[u].append(w)
        indegree[w] += 1
        incidences += 1
queue = deque(s for s in nonempty if indegree[s] == 0)
topological_count = 0
while queue:
    s = queue.popleft()
    topological_count += 1
    for t in outgoing[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert incidences == 143760
assert topological_count == len(nonempty) == 26440

critical_5 = sorted(s for s in critical if s.bit_count() == 6)
critical_6 = sorted(s for s in critical if s.bit_count() == 7)
assert critical_5 == [608392, 2237698, 5251618, 8945828, 8945940]
assert critical_6 == [4752676, 4753700, 5391496, 5392520,
                      8946980, 9061512, 9061634, 9519650,
                      9520264, 9576980, 9577604, 9585800]
critical_index = {s: i for i, s in enumerate(critical_5)}

# Signed face incidence [t:s], deleting bit b in t, is
# (-1)^(number of retained elements with smaller indices than b).
def sign(t, bit):
    return -1 if ((t & (bit-1)).bit_count() & 1) else 1

@lru_cache(None)
def project(s):
    """Signed gradient-path projection of dimension-five cell s."""
    if s in critical_index:
        return {critical_index[s]: 1}
    if s in match_down:  # cell already paired with a lower-dimensional face
        return {}
    assert s in match_up and s.bit_count() == 6
    t = match_up[s]
    bit = t ^ s
    paired_sign = sign(t, bit)
    ans = defaultdict(int)
    available = t ^ bit
    while available:
        other = available & -available
        available ^= other
        coefficient = -paired_sign * sign(t, other)
        for row, weight in project(t ^ other).items():
            ans[row] += coefficient * weight
    return {k: v for k, v in ans.items() if v}

matrix = [[0 for _ in critical_6] for _ in critical_5]
for col, t in enumerate(critical_6):
    bits = t
    while bits:
        bit = bits & -bits
        bits ^= bit
        for row, weight in project(t ^ bit).items():
            matrix[row][col] += sign(t, bit) * weight
expected = [[0]*12 for _ in range(5)]
for row in (3, 4):
    expected[row][4] = -1
    expected[row][5] = -1
    expected[row][8] = +1
assert matrix == expected
# Its single nonzero Smith invariant factor equals 1; row 3, column 4
# is already a unimodular 1x1 minor. Therefore cancellation leaves
# 5-1=4 five-cells and 12-1=11 six-cells.
assert matrix[3][4] == -1
assert sum(bool(x) for row in matrix for x in row) == 6
print('PASS: graph=24 vertices, 36 edges, degree 3')
print('PASS: nonempty faces=', len(nonempty), '; f-vector=', fvector)
print('PASS: Morse pairs=', len(match_up), '; critical cells=', dict(Counter(s.bit_count()-1 for s in critical)))
print('PASS: oriented incidences=', incidences, '; topological count=', topological_count)
print('PASS: integer Morse boundary 5x12, rank 1, unit invariant factor')
print('PASS: homotopy type = four 5-spheres wedge eleven 6-spheres')
