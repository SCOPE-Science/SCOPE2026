#!/usr/bin/env python3
"""Reproducible exact matching-complex homotopy and rational character checks.

Requires Python 3.9+ standard library only. All simplices and incidence
coefficients are generated from the Kneser model KG(5,2).
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

P = 1000003
BASE_VERTICES = list(combinations(range(5), 2))
GRAPH_EDGES = [
    (i, j) for i in range(10) for j in range(i + 1, 10)
    if set(BASE_VERTICES[i]).isdisjoint(BASE_VERTICES[j])
]
assert len(GRAPH_EDGES) == 15

# Enumerate matchings by two independent algorithms: occupied vertices
# and recursive edge-by-edge extension.
def enumerate_by_mask():
    out = set()
    for mask in range(1 << 15):
        used = 0
        ok = True
        for i, (a, b) in enumerate(GRAPH_EDGES):
            if mask & (1 << i):
                new = (1 << a) | (1 << b)
                if used & new:
                    ok = False
                    break
                used |= new
        if ok:
            out.add(mask)
    return out

def enumerate_recursively():
    out = set()
    def visit(i, chosen, used):
        if i == 15:
            out.add(chosen)
            return
        visit(i + 1, chosen, used)
        a, b = GRAPH_EDGES[i]
        if not (used & ((1 << a) | (1 << b))):
            visit(i + 1, chosen | (1 << i), used | (1 << a) | (1 << b))
    visit(0, 0, 0)
    return out

FACES = enumerate_by_mask()
assert FACES == enumerate_recursively()
BY_DIM = {k: sorted(m for m in FACES if m.bit_count() == k + 1)
          for k in range(-1, 5)}
INDEX = {k: {f: j for j, f in enumerate(fs)} for k, fs in BY_DIM.items()}
F_VECTOR = tuple(len(BY_DIM[k]) for k in range(5))
assert F_VECTOR == (15, 75, 145, 90, 6)
FACETS = [f for f in FACES if not any(
    not ((f >> i) & 1) and (f | (1 << i)) in FACES
    for i in range(15))]
FACET_DIMENSIONS = Counter(f.bit_count() - 1 for f in FACETS)
assert FACET_DIMENSIONS == {2: 5, 3: 60, 4: 6}


# Boundary ranks over F_2 via independent integer bitset elimination.
def binary_rank(k):
    pivots = {}
    for face in BY_DIM[k]:
        v = 0
        for j in range(15):
            if (face >> j) & 1:
                v ^= 1 << INDEX[k - 1][face ^ (1 << j)]
        while v:
            high = v.bit_length() - 1
            if high not in pivots:
                pivots[high] = v
                break
            v ^= pivots[high]
    return len(pivots)

RANK2 = {k: binary_rank(k) for k in range(1, 5)}
assert RANK2 == {1: 14, 2: 61, 3: 79, 4: 6}
BETTI2 = {k: len(BY_DIM[k]) - RANK2.get(k, 0) - RANK2.get(k + 1, 0)
          for k in range(5)}
assert BETTI2 == {0: 1, 1: 0, 2: 5, 3: 5, 4: 0}  # ordinary H_0=1

# A deterministic sequential toggle matching. Leave the empty simplex
# unmatched and therefore do not use any augmented-chain cancellation.
UNMATCHED = set(FACES - {0})
PAIRS = []
for edge in range(15):
    for a in sorted(UNMATCHED):
        b = a | (1 << edge)
        if not (a & (1 << edge)) and b in UNMATCHED:
            PAIRS.append((a, b))
            UNMATCHED.remove(a)
            UNMATCHED.remove(b)
assert len(PAIRS) == 158
assert Counter(m.bit_count() - 1 for m in UNMATCHED) == {0: 1, 2: 7, 3: 7}

# Verify every Hasse incidence of the acyclic matching using a DAG
# topological sort (the dimension-zero empty simplex is excluded).
PAIR_SET = set(PAIRS)
NONEMPTY = sorted(FACES - {0})
INDEX_ALL = {f: i for i, f in enumerate(NONEMPTY)}
OUT = [[] for _ in NONEMPTY]
INDEG = [0] * len(NONEMPTY)
incidences = 0
for b in NONEMPTY:
    for j in range(15):
        if (b >> j) & 1:
            a = b ^ (1 << j)
            if not a:
                continue
            incidences += 1
            if (a, b) in PAIR_SET:
                source, target = INDEX_ALL[a], INDEX_ALL[b]
            else:
                source, target = INDEX_ALL[b], INDEX_ALL[a]
            OUT[source].append(target)
            INDEG[target] += 1
queue = deque(i for i, x in enumerate(INDEG) if x == 0)
seen = 0
while queue:
    v = queue.popleft()
    seen += 1
    for w in OUT[v]:
        INDEG[w] -= 1
        if INDEG[w] == 0:
            queue.append(w)
assert seen == len(NONEMPTY)

# Exact integer Morse differential by algebraic elementary-unit-pivot
# cancellations, with signed orientations given by increasing edge indices.
D = {}
for b in NONEMPTY:
    if b.bit_count() < 2:
        continue
    D[b] = {b ^ (1 << j): (-1) ** (b & ((1 << j) - 1)).bit_count()
            for j in range(15) if (b >> j) & 1}
remaining = set(NONEMPTY)
for a, b in PAIRS:
    row = D[b]
    pivot = row[a]
    assert pivot in (-1, 1)
    for c in tuple(remaining):
        if c != b and c.bit_count() == b.bit_count():
            x = D[c].pop(a, 0)
            if x:
                for y, val in row.items():
                    if y == a:
                        continue
                    D[c][y] = D[c].get(y, 0) - (x * val // pivot)
                    if not D[c][y]:
                        del D[c][y]
    for c in tuple(remaining):
        if c.bit_count() == b.bit_count() + 1:
            D[c].pop(b, None)
    D.pop(a, None)
    D.pop(b, None)
    remaining.difference_update((a, b))
assert remaining == UNMATCHED
C2 = sorted(f for f in remaining if f.bit_count() == 3)
C3 = sorted(f for f in remaining if f.bit_count() == 4)
assert len(C2) == len(C3) == 7
MORSE = [[D[c].get(r, 0) for c in C3] for r in C2]
assert all(not D.get(f) for f in remaining if f.bit_count() != 4)

# Exact rank is two: each column is supported on three 2-cells, and
# these column vectors are in their integral sum-zero hyperplane.
nonzero_rows = [i for i, row in enumerate(MORSE) if any(row)]
assert len(nonzero_rows) == 3
assert all(sum(MORSE[i][j] for i in nonzero_rows) == 0 for j in range(7))
unit_minor = None
for i, j in combinations(range(7), 2):
    for a, b in combinations(range(7), 2):
        z = MORSE[i][a] * MORSE[j][b] - MORSE[i][b] * MORSE[j][a]
        if abs(z) == 1:
            unit_minor = (i, j, a, b, z)
            break
    if unit_minor is not None:
        break
assert unit_minor is not None

# Exact finite-field calculation of the character of the image of each
# boundary map. Rational characters equal these modular traces because
# each integer trace has absolute value < p/2 in these chain dimensions.

def vec_subtract(target, source, multiplier):
    for r, x in source.items():
        val = (target.get(r, 0) - multiplier * x) % P
        if val:
            target[r] = val
        else:
            target.pop(r, None)

def echelon_columns(k):
    echelon = {}  # pivot index -> (normalised vector, coefficients in basis)
    columns = []  # selected original chain columns
    for f in BY_DIM[k]:
        v = {INDEX[k - 1][f ^ (1 << e)]:
             (-1) ** (f & ((1 << e) - 1)).bit_count() % P
             for e in range(15) if (f >> e) & 1}
        orig = dict(v)
        coord = {len(columns): 1}
        for pivot in sorted(echelon, reverse=True):
            x = v.get(pivot, 0)
            if x:
                row, comb = echelon[pivot]
                vec_subtract(v, row, x)
                vec_subtract(coord, comb, x)
        if v:
            pivot = max(v)
            mult = pow(v[pivot], -1, P)
            v = {a: x * mult % P for a, x in v.items()}
            coord = {a: x * mult % P for a, x in coord.items()}
            echelon[pivot] = (v, coord)
            columns.append(orig)
    return echelon, columns

BASIS = {k: echelon_columns(k) for k in range(1, 5)}
assert {k: len(BASIS[k][1]) for k in BASIS} == RANK2

def permutation_action(perm, k):
    edge_id = {e: j for j, e in enumerate(GRAPH_EDGES)}
    move = []
    for a, b in GRAPH_EDGES:
        x = BASE_VERTICES.index(tuple(sorted(perm[t] for t in BASE_VERTICES[a])))
        y = BASE_VERTICES.index(tuple(sorted(perm[t] for t in BASE_VERTICES[b])))
        move.append(edge_id[tuple(sorted((x, y)))])
    out = []
    for f in BY_DIM[k]:
        coords = [move[j] for j in range(15) if (f >> j) & 1]
        inv = sum(coords[i] > coords[j]
                  for i in range(len(coords)) for j in range(i + 1, len(coords)))
        moved_mask = sum(1 << t for t in coords)
        out.append((INDEX[k][moved_mask], (-1) ** inv))
    return out

def trace_chain(perm, k):
    return sum(sign for a, (b, sign) in enumerate(permutation_action(perm, k)) if a == b)

def trace_image(perm, k):
    echelon, columns = BASIS[k + 1]
    action = permutation_action(perm, k)
    trace = 0
    for j, col in enumerate(columns):
        transformed = {}
        for row, value in col.items():
            target, sign = action[row]
            transformed[target] = (transformed.get(target, 0) + sign * value) % P
            if transformed[target] == 0:
                del transformed[target]
        coord = {}
        for pivot in sorted(echelon, reverse=True):
            x = transformed.get(pivot, 0)
            if x:
                vec, combine = echelon[pivot]
                vec_subtract(transformed, vec, x)
                for i, v in combine.items():
                    coord[i] = (coord.get(i, 0) + x * v) % P
        assert not transformed
        trace = (trace + coord.get(j, 0)) % P
    if trace > P // 2:
        trace -= P
    return trace

# One representative from each conjugacy class of S_5.
REPS = {}
for p in permutations(range(5)):
    visited = set()
    cycle_lengths = []
    for a in range(5):
        if a not in visited:
            b = a
            length = 0
            while b not in visited:
                visited.add(b)
                length += 1
                b = p[b]
            cycle_lengths.append(length)
    label = tuple(sorted(cycle_lengths, reverse=True))
    REPS.setdefault(label, p)

TABLE = {}
for label, p in sorted(REPS.items(), reverse=True):
    chains = {k: trace_chain(p, k) for k in range(2, 4)}
    bounds = {k: trace_image(p, k) for k in range(1, 4)}
    h2 = chains[2] - bounds[1] - bounds[2]
    h3 = chains[3] - bounds[2] - bounds[3]
    # Identify chars using the permutation on 5 points and on 2-sets.
    fixed_points = sum(p[i] == i for i in range(5))
    fixed_pairs = sum({p[i], p[j]} == {i, j} for i, j in combinations(range(5), 2))
    sign = (-1) ** (5 - len(label))
    assert (h2, h3) == (sign * fixed_points, fixed_pairs - fixed_points)
    TABLE[label] = (h2, h3)

# Verify all 120 group elements, not merely conjugacy representatives.
for p in permutations(range(5)):
    cyc = set()
    label_lengths = []
    for i in range(5):
        if i not in cyc:
            j = i
            length = 0
            while j not in cyc:
                cyc.add(j)
                length += 1
                j = p[j]
            label_lengths.append(length)
    label = tuple(sorted(label_lengths, reverse=True))
    a = trace_chain(p, 2) - trace_image(p, 1) - trace_image(p, 2)
    b = trace_chain(p, 3) - trace_image(p, 2) - trace_image(p, 3)
    assert (a, b) == TABLE[label]

print('PETERSEN_MATCHING_CHECK_OK')
print('f_vector', F_VECTOR, 'total_including_empty', len(FACES))
print('facet_dimension_counts', dict(sorted(FACET_DIMENSIONS.items())))
print('F2_boundary_ranks', RANK2, 'F2_reduced_betti', {2: 5, 3: 5})
print('matching_pairs', len(PAIRS), 'critical_by_dimension',
      dict(sorted(Counter(f.bit_count() - 1 for f in UNMATCHED).items())),
      'Hasse_incidences_checked', incidences)
print('critical_2cells', [hex(f) for f in C2])
print('critical_3cells', [hex(f) for f in C3])
print('signed_Morse_matrix_7x7', MORSE)
print('rank_two_unimodular_minor', unit_minor)
print('S5_character_columns H2 H3', TABLE)
print('S5_group_elements_checked', 120)
print('INTEGRAL_HOMOTOPY_AND_RATIONAL_CHARACTER_VERIFIED')
