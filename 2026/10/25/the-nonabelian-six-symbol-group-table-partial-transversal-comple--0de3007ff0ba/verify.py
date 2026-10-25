#!/usr/bin/env python3
"""Reproduce the finite enumeration, Morse matching and integer homotopy calculation.

Requires Python 3.9+ standard library only. Run: python3 verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations

N = 6
PERMS = list(permutations(range(3)))
INDEX = {p: i for i, p in enumerate(PERMS)}

def product(a, b):
    return INDEX[tuple(PERMS[a][PERMS[b][x]] for x in range(3))]

TABLE = tuple(tuple(product(r, c) for c in range(N)) for r in range(N))
assert all(set(row) == set(range(N)) for row in TABLE)
assert all(set(TABLE[r][c] for r in range(N)) == set(range(N))
           for c in range(N))

# A face is encoded by a 36-bit row-major cell mask. Each row is treated once,
# and each selected column and product symbol must be previously unused.
states = [(0, 0, 0)]
for r in range(N):
    next_states = []
    for mask, used_col, used_symbol in states:
        next_states.append((mask, used_col, used_symbol))
        for c in range(N):
            s = TABLE[r][c]
            if (used_col & (1 << c)) or (used_symbol & (1 << s)):
                continue
            next_states.append((mask | (1 << (N*r+c)),
                                used_col | (1 << c),
                                used_symbol | (1 << s)))
    states = next_states
faces = {mask for mask, _, _ in states}
assert len(faces) == len(states), 'Enumeration generated duplicate masks'
assert Counter(m.bit_count() for m in faces) == {
    0: 1, 1: 36, 2: 360, 3: 1200, 4: 1242, 5: 216}
faces.remove(0)

maximal = Counter()
for m in faces:
    if not any((m | (1 << v)) in faces for v in range(N*N)
               if not m & (1 << v)):
        maximal[m.bit_count()] += 1
assert maximal == {3: 12, 4: 324, 5: 216}

# Lexicographic vertex-toggle matching; at each pass, all matches are between
# faces unmatched at the beginning of the pass. Inclusion of the empty face is
# intentionally avoided so one ordinary zero-cell remains critical.
unmatched = set(faces)
pairs = []
for v in range(N*N):
    removed = []
    for lower in sorted(unmatched, key=lambda m: (m.bit_count(), m)):
        upper = lower | (1 << v)
        if not lower & (1 << v) and upper in unmatched:
            removed.extend((lower, upper))
            pairs.append((lower, upper))
    assert len(set(removed)) == len(removed)
    unmatched.difference_update(removed)

critical = Counter(m.bit_count()-1 for m in unmatched)
assert critical == {0: 1, 2: 49, 3: 200}
assert len(pairs) == 1402
paired_upper = {upper: lower for lower, upper in pairs}
paired_lower = {lower: upper for lower, upper in pairs}
assert len(paired_upper) == len(paired_lower) == len(pairs)

# Full signed Hasse graph orientation: matched cover relations point upward,
# all other codimension-one cover relations point downward. DAG check covers
# every vertex and edge; a mere match count would not certify acyclicity.
ordered = sorted(faces)
number = {m: i for i, m in enumerate(ordered)}
outgoing = [[] for _ in ordered]
indegree = [0]*len(ordered)
edges = 0
for upper in ordered:
    rest = upper
    while rest:
        bit = rest & -rest
        rest -= bit
        lower = upper ^ bit
        if not lower:
            continue
        if paired_upper.get(upper) == lower:
            src, dst = number[lower], number[upper]
        else:
            src, dst = number[upper], number[lower]
        outgoing[src].append(dst)
        indegree[dst] += 1
        edges += 1
assert edges == 10368
queue = deque(i for i, d in enumerate(indegree) if d == 0)
seen = 0
while queue:
    u = queue.popleft()
    seen += 1
    for v in outgoing[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert seen == len(faces) == 3054, 'Directed Hasse graph has a cycle'

# Signed simplicial incidence [coface : face] for ascending vertex order.
def incidence(face, coface):
    missing = coface ^ face
    assert missing and not missing & (missing-1)
    assert face | missing == coface
    return -1 if (coface & (missing-1)).bit_count() % 2 else 1

critical_two = sorted(m for m in unmatched if m.bit_count() == 3)
critical_three = sorted(m for m in unmatched if m.bit_count() == 4)
crit_index = {m: i for i, m in enumerate(critical_two)}

@lru_cache(None)
def phi(m):
    """Integer vector after elementary Morse cancellations in dimension 2."""
    if m in crit_index:
        return {crit_index[m]: 1}
    if m in paired_upper:
        return {}
    assert m in paired_lower
    upper = paired_lower[m]
    pivot = incidence(m, upper)  # plus or minus one
    sums = defaultdict(int)
    rest = upper
    while rest:
        bit = rest & -rest
        rest -= bit
        other = upper ^ bit
        if other == m:
            continue
        coeff = -pivot * incidence(other, upper)
        for k, v in phi(other).items():
            sums[k] += coeff * v
    return {i: v for i, v in sums.items() if v}

# Matrix has one row per critical 2-simplex, one column per critical 3-simplex.
boundary = [[0]*len(critical_three) for _ in critical_two]
for j, cell in enumerate(critical_three):
    rest = cell
    while rest:
        bit = rest & -rest
        rest -= bit
        face = cell ^ bit
        sign = incidence(face, cell)
        for i, coeff in phi(face).items():
            boundary[i][j] += sign*coeff
assert Counter(a for row in boundary for a in row) == {
    0: 8547, 1: 627, -1: 593, 2: 16, -2: 17}

# Integral elementary row/column operations. Each unit pivot splits a copy
# of Z -> Z. After 37 unit pivots the entire residual matrix is zero, which
# certifies that all 37 nonzero Smith invariant factors are exactly one.
mat = [row.copy() for row in boundary]
r, c = len(mat), len(mat[0])
unit_pivots = 0
for k in range(min(r, c)):
    pos = next(((i, j) for i in range(k, r) for j in range(k, c)
                if abs(mat[i][j]) == 1), None)
    if pos is None:
        break
    i, j = pos
    mat[k], mat[i] = mat[i], mat[k]
    for row in mat:
        row[k], row[j] = row[j], row[k]
    if mat[k][k] == -1:
        mat[k] = [-v for v in mat[k]]
    for i in range(r):
        if i != k and mat[i][k]:
            factor = mat[i][k]
            mat[i] = [a-factor*b for a, b in zip(mat[i], mat[k])]
    for j in range(c):
        if j != k and mat[k][j]:
            factor = mat[k][j]
            for i in range(r):
                mat[i][j] -= factor * mat[i][k]
    assert all(mat[k][j] == (1 if j == k else 0) for j in range(c))
    assert all(mat[i][k] == (1 if i == k else 0) for i in range(r))
    unit_pivots += 1
assert unit_pivots == 37
assert not any(mat[i][j] for i in range(unit_pivots, r)
               for j in range(unit_pivots, c))

# Independent mod-two ranks computed directly on the unreduced simplicial
# boundary matrices, rather than by reusing the Morse boundary above.
mod_two_ranks = []
for k in range(1, 5):
    lowers = sorted(m for m in faces if m.bit_count() == k)
    uppers = sorted(m for m in faces if m.bit_count() == k+1)
    lower_id = {m: i for i, m in enumerate(lowers)}
    pivots = {}
    for upper in uppers:
        col = 0
        rest = upper
        while rest:
            bit = rest & -rest
            rest -= bit
            col ^= 1 << lower_id[upper ^ bit]
        while col:
            lead = col.bit_length()-1
            if lead not in pivots:
                pivots[lead] = col
                break
            col ^= pivots[lead]
    mod_two_ranks.append(len(pivots))
assert mod_two_ranks == [35, 325, 863, 216]

print('group=S3; cells=36; faces_nonempty=3054')
print('face_vector=(36,360,1200,1242,216)')
print('maximal_by_size=(3:12,4:324,5:216)')
print('morse_pairs=1402; directed_incidences=10368; topological_sort=3054')
print('critical_cells=(dim0:1,dim2:49,dim3:200)')
print('morse_boundary=49x200; integer_unit_pivots=37; residual_zero=True')
print('simplicial_mod2_boundary_ranks=(35,325,863,216)')
print('homotopy=12*S^2 wedge 163*S^3')
print('VERIFY_OK')
