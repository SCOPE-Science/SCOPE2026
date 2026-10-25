#!/usr/bin/env python3
"""Exact finite certificate for homology characters of Ind(C8 x K3).

Requires only Python 3 standard library. Every face, matching pair, boundary
coefficient and symmetry action is reconstructed from the graph definition.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations

N, COLORS = 8, 3
SIZE = N * COLORS
PIVOTS = (21, 8, 7, 12, 13, 5, 18, 1, 6, 22, 2, 10, 19, 15, 14, 11, 3, 4, 0, 16, 20, 23, 9, 17)


def vertices(mask):
    return [i for i in range(SIZE) if (mask >> i) & 1]


def signed_boundary(mask):
    return {mask ^ (1 << v): (-1 if j % 2 else 1)
            for j, v in enumerate(vertices(mask))}


def nonzero(mapping):
    return {k: v for k, v in mapping.items() if v}


# Independence faces are stored as masks, including the empty simplex.
adj = [0] * SIZE
for r in range(N):
    for c in range(COLORS):
        idx = COLORS * r + c
        for step in (-1, 1):
            for d in range(COLORS):
                if d != c:
                    adj[idx] |= 1 << (COLORS * ((r + step) % N) + d)
assert all((adj[u] >> v) & 1 == (adj[v] >> u) & 1
           for u in range(SIZE) for v in range(SIZE))
faces = {0}
for v in range(SIZE):
    bit = 1 << v
    faces.update(f | bit for f in tuple(faces) if not (f & adj[v]))
assert len(faces) == 18722
counts = Counter(f.bit_count() - 1 for f in faces)
assert counts == {-1: 1, 0: 24, 1: 228, 2: 1112, 3: 3042, 4: 4848,
                  5: 4652, 6: 2880, 7: 1305, 8: 472, 9: 132, 10: 24, 11: 2}

# The staged vertex matching is the standard acyclic poset matching obtained
# by pairing remaining faces through their specified pivot vertex.
remaining = set(faces)
matched_low = {}
for v in PIVOTS:
    bit = 1 << v
    for f in faces:
        g = f | bit
        if not (f & bit) and f in remaining and g in remaining:
            remaining.remove(f)
            remaining.remove(g)
            matched_low[f] = g
matched_high = {g: f for f, g in matched_low.items()}
assert len(matched_low) == 9358
assert len(remaining) == 6
assert all(remaining == {0x18424, 0x408c02, 0x18c06, 0x90609, 0x124809, 0x124812}
           for _ in (0,))
critical = {k: sorted(f for f in remaining if f.bit_count() == k + 1)
            for k in (4, 5)}
assert len(critical[4]) == 2 and len(critical[5]) == 4

# Check acyclicity of the ENTIRE augmented face poset, not just a sample.
indeg = {f: 0 for f in faces}
out = defaultdict(list)
for high in faces:
    for low in signed_boundary(high):
        if matched_low.get(low) == high:
            a, b = low, high
        else:
            a, b = high, low
        out[a].append(b)
        indeg[b] += 1
queue = deque(f for f in faces if indeg[f] == 0)
visited = 0
while queue:
    cell = queue.popleft()
    visited += 1
    for successor in out[cell]:
        indeg[successor] -= 1
        if indeg[successor] == 0:
            queue.append(successor)
assert visited == len(faces)
assert sum(map(len, out.values())) == 104592


@lru_cache(None)
def projection(cell):
    """Integral algebraic-Morse projection on the degree of cell."""
    if cell in remaining:
        return {cell: 1}
    if cell in matched_high:
        return {}
    upper = matched_low[cell]
    terms = signed_boundary(upper)
    pivot_sign = terms[cell]  # equals +/-1
    result = Counter()
    for lower, sign in terms.items():
        if lower == cell:
            continue
        for basis_cell, coefficient in projection(lower).items():
            result[basis_cell] -= pivot_sign * sign * coefficient
    return nonzero(result)


@lru_cache(None)
def lower_pair_order(degree):
    """Dependency order for cancelling matched degree-(degree-1) faces."""
    low = {f for f in matched_low if f.bit_count() == degree}
    incoming = {f: 0 for f in low}
    downstream = defaultdict(set)
    for f in low:
        for other in signed_boundary(matched_low[f]):
            if other != f and other in low:
                downstream[f].add(other)
                incoming[other] += 1
    todo = deque(f for f in low if incoming[f] == 0)
    result = []
    while todo:
        face = todo.popleft()
        result.append(face)
        for other in downstream[face]:
            incoming[other] -= 1
            if incoming[other] == 0:
                todo.append(other)
    assert len(result) == len(low)
    return tuple(result)


def lift_critical(degree, critical_face):
    """Lift a Morse generator to the original chain complex integrally."""
    chain = Counter({critical_face: 1})
    boundary = Counter(signed_boundary(critical_face))
    for low in lower_pair_order(degree):
        coeff = boundary[low]
        if not coeff:
            continue
        high = matched_low[low]
        correction = -coeff * signed_boundary(high)[low]
        chain[high] += correction
        for t, s in signed_boundary(high).items():
            boundary[t] += correction * s
    return nonzero(chain), nonzero(boundary)


lifts = {}
for degree in (4, 5):
    for cell in critical[degree]:
        chain, boundary = lift_critical(degree, cell)
        lifts[cell] = chain
        reconstructed = Counter()
        for f, c in chain.items():
            for t, s in signed_boundary(f).items():
                reconstructed[t] += c * s
        assert nonzero(reconstructed) == boundary
        compressed = Counter()
        for f, c in chain.items():
            for t, s in projection(f).items():
                compressed[t] += c * s
        assert nonzero(compressed) == {cell: 1}
        if degree == 4:
            assert not boundary

# Critical Morse boundary has rank one and a unit entry.
d5 = []
for cell in critical[5]:
    coeffs = Counter()
    for low, b in signed_boundary(cell).items():
        for target, coeff in projection(low).items():
            coeffs[target] += b * coeff
    d5.append(tuple(coeffs[f] for f in critical[4]))
assert d5 == [(-1, -1), (0, 0), (0, 0), (1, 1)]

# Basis for reduced H5, using e0+e3, e1, e2 in Morse coordinates.
# H4 is the quotient on e0 and e1 by the primitive relation e0+e1=0.
e0, e1, e2, e3 = critical[5]
h5_basis = [Counter({e0: 1, e3: 1}), Counter({e1: 1}), Counter({e2: 1})]
h5_cycles = []
for basis_vector in h5_basis:
    original = Counter()
    for f, a in basis_vector.items():
        for cell, b in lifts[f].items():
            original[cell] += a * b
    original = nonzero(original)
    boundary = Counter()
    for cell, a in original.items():
        for face, s in signed_boundary(cell).items():
            boundary[face] += a * s
    assert not nonzero(boundary)
    h5_cycles.append(original)


def symmetry(face, shift, sign_r, color_perm):
    image = [COLORS * ((sign_r * (v // COLORS) + shift) % N)
             + color_perm[v % COLORS] for v in vertices(face)]
    inversions = sum(image[i] > image[j]
                     for i in range(len(image)) for j in range(i + 1, len(image)))
    return sum(1 << v for v in image), (-1 if inversions % 2 else 1)


def act_project(chain, shift, sign_r, color_perm):
    result = Counter()
    for simplex, coeff in chain.items():
        image, orient = symmetry(simplex, shift, sign_r, color_perm)
        for critical_simplex, projected in projection(image).items():
            result[critical_simplex] += coeff * orient * projected
    return result


def perm_sign(perm):
    inv = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inv % 2 else 1


def trace_direct(shift, sign_r, color_perm):
    """Independent signed simplicial Lefschetz trace, including empty face."""
    total = 0
    for face in faces:
        image, orientation = symmetry(face, shift, sign_r, color_perm)
        if image == face:
            total += (1 if face.bit_count() % 2 else -1) * orientation
    return total

result_rows = []
for shift in range(N):
    for sign_r in (1, -1):
        for color_perm in permutations(range(COLORS)):
            sign_p = perm_sign(color_perm)
            h4_image = act_project(lifts[critical[4][0]], shift, sign_r, color_perm)
            trace_h4 = h4_image[critical[4][0]] - h4_image[critical[4][1]]
            h5_images = [act_project(c, shift, sign_r, color_perm) for c in h5_cycles]
            assert all(x[e0] == x[e3] for x in h5_images)
            trace_h5 = h5_images[0][e0] + h5_images[1][e1] + h5_images[2][e2]
            expected_h4 = ((-1) ** (shift + (sign_r == -1))) * sign_p
            expected_h5 = ((-1) ** shift) * sign_p * sum(color_perm[i] == i for i in range(COLORS))
            assert (trace_h4, trace_h5) == (expected_h4, expected_h5), (shift, sign_r, color_perm, trace_h4, trace_h5, expected_h4, expected_h5)
            assert trace_direct(shift, sign_r, color_perm) == trace_h4 - trace_h5
            result_rows.append((shift, sign_r, color_perm, trace_h4, trace_h5))
assert len(result_rows) == 96
assert sum(1 for row in result_rows if row[3] == 1) == 48
assert sum(1 for row in result_rows if row[4] == 3) == 8
print('C8_K3_EQUIVARIANT_HOMOLOGY_VERIFIED', len(faces), len(matched_low), len(remaining), len(result_rows), 'boundary_rank_1', 'H4_1', 'H5_3')
