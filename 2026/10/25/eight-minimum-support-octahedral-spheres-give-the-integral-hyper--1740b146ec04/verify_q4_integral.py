#!/usr/bin/env python3
"""Exact finite verifier for the integral four-cube crosspolytopal-cycle theorem."""
from itertools import combinations, permutations
from collections import Counter, deque

V = tuple(range(16))
ADJ = tuple(sum(1 << w for w in V if (v ^ w).bit_count() == 1) for v in V)
EDGES = tuple((v, w) for v in V for w in V if v < w and (v ^ w).bit_count() == 1)
FACES = tuple(s for s in range(1, 1 << 16)
              if all((s & (1 << v)) == 0 or (s & ADJ[v]) == 0 for v in V))
FSET = set(FACES)
FVEC = Counter(s.bit_count() - 1 for s in FACES)
assert len(EDGES) == 32 and len(FACES) == 742
assert [FVEC[i] for i in range(8)] == [16, 88, 208, 228, 128, 56, 16, 2]

# Select each maximal nonoverlapping matching at successive vertex toggles.
unused = set(FACES)
MATCHED = []
PIVOT_COUNTS = []
for v in V:
    before = len(MATCHED)
    for s in sorted(unused):
        if s & (1 << v):
            continue
        t = s | (1 << v)
        if t in unused:
            unused.remove(s)
            unused.remove(t)
            MATCHED.append((s, t))
    PIVOT_COUNTS.append(len(MATCHED) - before)
assert len(MATCHED) == 367
assert sorted(unused) == [1, 1680, 2400, 10370, 17028, 24600, 33064, 33096]
assert Counter(s.bit_count() - 1 for s in unused) == {0: 1, 3: 7}
assert PIVOT_COUNTS == [176, 134, 10, 4, 5, 5, 13, 4, 0, 3, 4, 3, 3, 1, 1, 1]

# Check acyclicity independently, orienting unmatched incidences downward
# and matched incidences upward.
match_set = set(MATCHED)
indeg = {s: 0 for s in FACES}
succ = {s: [] for s in FACES}
incidences = 0
for upper in FACES:
    for v in V:
        if not (upper & (1 << v)):
            continue
        lower = upper ^ (1 << v)
        if not lower:
            continue
        incidences += 1
        if (lower, upper) in match_set:
            a, b = lower, upper
        else:
            a, b = upper, lower
        succ[a].append(b)
        indeg[b] += 1
queue = deque(x for x in FACES if indeg[x] == 0)
visited = 0
while queue:
    a = queue.popleft()
    visited += 1
    for b in succ[a]:
        indeg[b] -= 1
        if indeg[b] == 0:
            queue.append(b)
assert incidences == 2816 and visited == 742

# The eight full-size induced 4K2 subgraphs of Q4 are all enumerated,
# rather than sampled from a list of plausible support sets.
CARRIERS = []
for edge_group in combinations(EDGES, 4):
    vertex_mask = 0
    for u, v in edge_group:
        vertex_mask |= (1 << u) | (1 << v)
    if vertex_mask.bit_count() != 8:
        continue
    if all((ADJ[v] & vertex_mask).bit_count() == 1
           for v in V if vertex_mask & (1 << v)):
        CARRIERS.append(tuple(edge_group))
CARRIERS.sort()
assert len(CARRIERS) == 8
# Each carrier consists of the 4 parallel edges whose fixed three bits
# have one prescribed parity.
LABELS = []
for group in CARRIERS:
    direction = (group[0][0] ^ group[0][1]).bit_length() - 1
    assert all((u ^ v) == (1 << direction) for u, v in group)
    parities = {((u & ~(1 << direction)).bit_count() & 1) for u, v in group}
    assert len(parities) == 1
    LABELS.append((direction, next(iter(parities))))
assert sorted(LABELS) == [(i, p) for i in range(4) for p in range(2)]

# Orient the induced octahedral 3-sphere as the exterior join of
# ([lower endpoint]-[upper endpoint]) factors, with integer coefficients.
def orientation_sign(seq):
    return -1 if sum(a > b for i, a in enumerate(seq)
                     for b in seq[i + 1:]) % 2 else 1

def sphere_chain(group):
    result = {}
    for bits in range(16):
        selected = [group[j][(bits >> j) & 1] for j in range(4)]
        mask = sum(1 << a for a in selected)
        result[mask] = (-1 if bits.bit_count() & 1 else 1) * orientation_sign(selected)
    assert len(result) == 16 and set(result).issubset(FSET)
    return result

SPHERES = [sphere_chain(group) for group in CARRIERS]

# Form integral cellular differential columns indexed by masks.
D = {k: {} for k in range(1, 8)}
for s in FACES:
    k = s.bit_count() - 1
    if k >= 1:
        vertices = [v for v in V if s & (1 << v)]
        D[k][s] = {s ^ (1 << v): (-1 if j % 2 else 1)
                   for j, v in enumerate(vertices)}
for k in range(2, 8):
    for s, col in D[k].items():
        d2 = {}
        for t, a in col.items():
            for u, b in D[k - 1][t].items():
                d2[u] = d2.get(u, 0) + a * b
        assert all(c == 0 for c in d2.values())
for cycle in SPHERES:
    d = {}
    for s, c in cycle.items():
        for t, a in D[3][s].items():
            d[t] = d.get(t, 0) + c * a
    assert all(c == 0 for c in d.values())

# Integral algebraic-Morse cancellations on the actual signed matrices.
# At each pairing (a,b), with dim(b)=dim(a)+1 and u=d(b)[a]=+/-1,
# take the exact Schur complement. A cycle in the dimension-3 group is
# projected by subtracting its coefficient at a times d(b)/u (if dim b=4),
# or by deleting the b coefficient (if dim b=3).
projected = [dict(c) for c in SPHERES]
for a, b in MATCHED:
    k = b.bit_count() - 1
    column_b = D[k][b]
    u = column_b[a]
    assert u in (-1, 1)
    if k == 4:
        for z in projected:
            coeff = z.pop(a, 0)
            if coeff:
                for lower, value in column_b.items():
                    if lower != a:
                        new_value = z.get(lower, 0) - coeff * value // u
                        if new_value:
                            z[lower] = new_value
                        else:
                            z.pop(lower, None)
    elif k == 3:
        for z in projected:
            z.pop(b, None)
    for other_b, column in list(D[k].items()):
        if other_b == b:
            continue
        t = column.pop(a, 0)
        if t:
            for lower, value in column_b.items():
                if lower != a:
                    new_value = column.get(lower, 0) - t * value // u
                    if new_value:
                        column[lower] = new_value
                    else:
                        column.pop(lower, None)
    del D[k][b]
    if k >= 2:
        del D[k - 1][a]
    if k + 1 in D:
        for column in D[k + 1].values():
            column.pop(b, None)
assert all(not column for layer in D.values() for column in layer.values())
critical3 = sorted(s for s in unused if s.bit_count() == 4)
assert all(set(z).issubset(set(critical3)) for z in projected)
M = [[z.get(a, 0) for z in projected] for a in critical3]
assert M == [
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, -1, -1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, -1],
    [0, 0, 0, 0, -1, -1, 0, 0],
]

# Exact Bareiss determinant on 7 x 7 integral matrices.
def det(A):
    A = [list(row) for row in A]
    n = len(A)
    sign = 1
    last = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((i for i in range(k + 1, n) if A[i][k]), None)
            if p is None:
                return 0
            A[k], A[p] = A[p], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numerator % last == 0
                A[i][j] = numerator // last
            A[i][k] = 0
        last = pivot
    return sign * A[n-1][n-1]

minors = []
for omitted in range(8):
    minor = det([[row[j] for j in range(8) if j != omitted] for row in M])
    minors.append(minor)
assert minors == [-1, -1, -1, -1, 1, 1, 1, 1]
RELATION = [1, -1, 1, -1, -1, 1, -1, 1]
assert all(sum(M[i][j] * RELATION[j] for j in range(8)) == 0 for i in range(7))

# Full hyperoctahedral group: each automorphism is v -> t xor pi(v).
# Test the integral action on all eight oriented cycles and all 384 maps.
def action_on_cycle(z, mapping):
    out = {}
    for mask, coeff in z.items():
        src = [v for v in V if mask & (1 << v)]
        dest = [mapping[v] for v in src]
        key = sum(1 << v for v in dest)
        out[key] = coeff * orientation_sign(dest)
    return out

def permutation_sign(p):
    return orientation_sign(list(p))

checks = 0
for pi in permutations(range(4)):
    sign_pi = permutation_sign(pi)
    moved = [sum(((v >> i) & 1) << pi[i] for i in range(4)) for v in V]
    for translation in range(16):
        mapping = [m ^ translation for m in moved]
        assert {mapping[v] for v in V} == set(V)
        assert all(((a ^ b).bit_count() == 1) ==
                   ((mapping[a] ^ mapping[b]).bit_count() == 1)
                   for a in V for b in V)
        for j, (direction, parity) in enumerate(LABELS):
            next_dir = pi[direction]
            next_par = parity ^ ((translation & ~(1 << next_dir)).bit_count() & 1)
            dest_index = LABELS.index((next_dir, next_par))
            target = {s: sign_pi * RELATION[dest_index] * a // RELATION[j]
                      for s, a in SPHERES[dest_index].items()}
            assert action_on_cycle(SPHERES[j], mapping) == target
        checks += 1
assert checks == 384
print('VERIFY_OK_Q4_INTEGRAL_CROSSCYCLE_AUGMENTATION_QUOTIENT')
print('FACE_VECTOR', tuple(FVEC[k] for k in range(8)))
print('ACYCLIC_MATCHING_PAIRS', len(MATCHED), 'HASSE', incidences, 'VISITED', visited)
print('CRITICAL', tuple(critical3), 'REDUCED_DIFFERENTIAL_ZERO')
print('EIGHT_MINIMAL_SUPPORT_SPHERES', len(CARRIERS), 'LABELS', LABELS)
print('MORSE_COORDINATE_MATRIX', M)
print('SEVEN_BY_SEVEN_MINOR_DETERMINANTS', tuple(minors))
print('UNIQUE_PRIMITIVE_RELATION', tuple(RELATION))
print('ALL_HYPEROCTAHEDRAL_AUTOMORPHISMS_VERIFIED', checks)
print('MODULE_SIGN_OF_COORDINATE_PERMUTATION_TENSOR_Z8_MOD_DIAGONAL')
