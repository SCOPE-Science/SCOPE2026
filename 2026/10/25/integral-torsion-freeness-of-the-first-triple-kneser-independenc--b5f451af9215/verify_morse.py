"""Exact integral chain certificate for the six-point pairwise-intersecting
triple complex with transversal number at most two.

Use: python3 verify_morse.py. Requires only the Python standard library.
Faces are finite bit masks; no floating point or randomized steps are used.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, product

TRIPLES = list(combinations(range(6), 3))
PAIRS = []
seen = set()
for t in TRIPLES:
    if t in seen:
        continue
    c = tuple(x for x in range(6) if x not in t)
    PAIRS.append((TRIPLES.index(t), TRIPLES.index(c)))
    seen.add(t)
    seen.add(c)
assert len(PAIRS) == 10 and len(seen) == 20

COVERS = [sum(1 << i for i, t in enumerate(TRIPLES) if a in t or b in t)
          for a, b in combinations(range(6), 2)]
FACES = set()
for states in product((0, 1, 2), repeat=10):
    f = 0
    for j, choice in enumerate(states):
        if choice:
            f |= 1 << PAIRS[j][choice-1]
    if f and any((f & ~cover) == 0 for cover in COVERS):
        FACES.add(f)
assert len(FACES) == 54870
assert dict(sorted(Counter(f.bit_count()-1 for f in FACES).items())) == {
    0: 20, 1: 180, 2: 960, 3: 3360, 4: 8064,
    5: 13410, 6: 14640, 7: 9900, 8: 3740, 9: 596}

# Construct a deterministic matching on the nonempty-face Hasse poset.
remaining = set(FACES)
LOWER_TO_UPPER = {}
for v in range(20):
    bit = 1 << v
    for f in sorted((x for x in remaining if not x & bit),
                    key=lambda x: (x.bit_count(), x)):
        upper = f | bit
        if f in remaining and upper in remaining:
            remaining.remove(f)
            remaining.remove(upper)
            LOWER_TO_UPPER[f] = upper
UPPER_TO_LOWER = {u: l for l, u in LOWER_TO_UPPER.items()}
assert len(LOWER_TO_UPPER) == 27398
assert len(remaining) == 74
critical_by_degree = {d: sorted(f for f in remaining if f.bit_count()-1 == d)
                      for d in range(10)}
assert {d: len(v) for d, v in critical_by_degree.items() if v} == {
    0: 1, 5: 42, 6: 19, 7: 6, 8: 6}

# Every covering incidence: matched arrows lower -> upper, others upper -> lower.
indegree = {f: 0 for f in FACES}
outgoing = defaultdict(list)
cover_count = 0
for f in FACES:
    t = f
    while t:
        bit = t & -t
        t -= bit
        lower = f ^ bit
        if not lower:
            continue
        if LOWER_TO_UPPER.get(lower) == f:
            src, dst = lower, f
        else:
            src, dst = f, lower
        outgoing[src].append(dst)
        indegree[dst] += 1
        cover_count += 1
queue = deque(f for f in FACES if indegree[f] == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in outgoing[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert cover_count == 358760
assert visited == len(FACES), 'gradient cycle detected'

@lru_cache(maxsize=None)
def project(f):
    """Integral elimination of the matched faces in fixed degree.

    For paired (l,u), the relation boundary(u)=0 solves for l with
    incidence coefficient +/-1. Acyclicity makes the recursion finite.
    """
    if f in remaining:
        return {f: 1}
    if f in UPPER_TO_LOWER:
        return {}
    upper = LOWER_TO_UPPER[f]
    pivot = upper ^ f
    sign_pivot = (-1) ** ((upper & (pivot - 1)).bit_count())
    output = Counter()
    t = upper ^ pivot
    while t:
        bit = t & -t
        t -= bit
        other = upper ^ bit
        sign = (-1) ** ((upper & (bit - 1)).bit_count())
        for h, coefficient in project(other).items():
            output[h] -= sign_pivot * sign * coefficient
    return {h: c for h, c in output.items() if c}

def morse_boundary(f):
    total = Counter()
    t = f
    while t:
        bit = t & -t
        t -= bit
        facet = f ^ bit
        if not facet:
            continue
        sign = (-1) ** ((f & (bit - 1)).bit_count())
        for h, coefficient in project(facet).items():
            total[h] += sign * coefficient
    return {h: c for h, c in total.items() if c}

def boundary_matrix(d):
    rows = critical_by_degree[d-1]
    cols = critical_by_degree[d]
    entries = [[0 for _ in cols] for _ in rows]
    row_index = {f: i for i, f in enumerate(rows)}
    for j, f in enumerate(cols):
        for h, value in morse_boundary(f).items():
            entries[row_index[h]][j] = value
    return entries

def unit_pivots_to_zero(matrix, ncols):
    """Unimodular row and column elimination; requires unit pivots.
    If the final residual is zero, Smith nonzero invariants all equal one.
    """
    A = [list(row) for row in matrix]
    nrows = len(A)
    k = 0
    while k < min(nrows, ncols):
        pos = next(((i, j) for i in range(k, nrows)
                    for j in range(k, ncols) if abs(A[i][j]) == 1), None)
        if pos is None:
            break
        i, j = pos
        A[k], A[i] = A[i], A[k]
        for row in A:
            row[k], row[j] = row[j], row[k]
        s = A[k][k]
        assert abs(s) == 1
        for ii in range(k+1, nrows):
            q = A[ii][k] * s
            if q:
                for jj in range(k, ncols):
                    A[ii][jj] -= q * A[k][jj]
        for jj in range(k+1, ncols):
            q = A[k][jj] * s
            if q:
                for ii in range(k, nrows):
                    A[ii][jj] -= q * A[ii][k]
        k += 1
    assert all(A[i][j] == 0 for i in range(k, nrows)
               for j in range(k, ncols)), 'nonunit Smith remainder'
    return k

matrices = {}
for d in (6, 7, 8):
    M = boundary_matrix(d)
    matrices[d] = M
    nz = sum(x != 0 for row in M for x in row)
    max_entry = max((abs(x) for row in M for x in row), default=0)
    pivots = unit_pivots_to_zero(M, len(critical_by_degree[d]))
    print(f'd{d}: {len(M)}x{len(critical_by_degree[d])} '
          f'nonzero={nz} max_abs={max_entry} unit_pivots={pivots} residual=0')
    assert (d, pivots, nz, max_entry) in {
        (6, 13, 186, 1), (7, 6, 40, 1), (8, 0, 0, 0)}

# Confirm the chain condition directly, rather than relying solely on the theorem.
for d in (7, 8):
    B = matrices[d-1]
    C = matrices[d]
    for row in B:
        for col in zip(*C):
            assert sum(x*y for x, y in zip(row, col)) == 0

print('nonempty_faces=54870 directed_covers=358760 gradient_DAG=TRUE')
print('matched_pairs=27398 critical_cells={0:1,5:42,6:19,7:6,8:6}')
print('integral_reduced_homology={5:Z^29,8:Z^6} torsion=NONE')
print('VERIFICATION_OK')
