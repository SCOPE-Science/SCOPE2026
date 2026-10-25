#!/usr/bin/env python3
"""Exact finite checks for the induced-forest complex of the folded five-cube."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations
from hashlib import sha256
from math import prod
import json

N = 16
EDGES = tuple((u, v) for u in range(N) for v in range(u+1, N)
              if (u ^ v).bit_count() == 1 or (u ^ v) == 15)
NEIGH = [0] * N
for u, v in EDGES:
    NEIGH[u] |= 1 << v
    NEIGH[v] |= 1 << u
assert len(EDGES) == 40 and all(x.bit_count() == 5 for x in NEIGH)
assert all(sum(bool(NEIGH[u] & NEIGH[v] & (1 << w)) for w in range(N))
           == (0 if (u ^ v).bit_count() == 1 or (u ^ v) == 15 else 2)
           for u in range(N) for v in range(N) if u != v)


def forest_unionfind(mask):
    parent = list(range(N))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in EDGES:
        if ((mask >> u) & 1) and ((mask >> v) & 1):
            a, b = root(u), root(v)
            if a == b:
                return False
            parent[a] = b
    return True


def forest_components(mask):
    # Independent check using edge count and connected component count.
    remaining = mask
    components = 0
    while remaining:
        components += 1
        seed = remaining & -remaining
        stack = [seed.bit_length()-1]
        remaining ^= seed
        while stack:
            v = stack.pop()
            to_visit = NEIGH[v] & remaining
            while to_visit:
                bit = to_visit & -to_visit
                to_visit ^= bit
                remaining ^= bit
                stack.append(bit.bit_length()-1)
    e = sum(1 for a, b in EDGES if (mask >> a) & 1 and (mask >> b) & 1)
    return e == mask.bit_count() - components


FACES = {mask for mask in range(1 << N) if forest_unionfind(mask)}
assert FACES == {mask for mask in range(1 << N) if forest_components(mask)}
assert len(FACES) == 13839
f_vector = [sum(mask.bit_count() == i+1 for mask in FACES) for i in range(9)]
assert f_vector == [16, 120, 560, 1780, 3696, 4376, 2560, 650, 80]


def pivot_matching():
    unmatched = FACES.copy()
    pairs = []
    for v in range(N):
        bit = 1 << v
        choices = sorted(m for m in unmatched if not m & bit and (m | bit) in unmatched)
        for low in choices:
            assert low in unmatched and (low | bit) in unmatched
            unmatched.remove(low)
            unmatched.remove(low | bit)
            pairs.append((low, low | bit))
    return unmatched, pairs

critical, pairs = pivot_matching()
assert len(pairs) == 6908 and len(critical) == 23
assert Counter(mask.bit_count()-1 for mask in critical) == {5: 19, 6: 4}
assert not (0 in critical)


def check_matching_acyclic():
    # Hasse arrows point down except matched incidences, which point up.
    pair_set = set(pairs)
    out = defaultdict(list)
    indegree = {mask: 0 for mask in FACES}
    incidence = 0
    for upper in FACES:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if (lower, upper) in pair_set:
                a, b = lower, upper
            else:
                a, b = upper, lower
            out[a].append(b)
            indegree[b] += 1
            incidence += 1
    ready = deque(mask for mask, deg in indegree.items() if deg == 0)
    visited = 0
    while ready:
        a = ready.popleft()
        visited += 1
        for b in out[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                ready.append(b)
    assert visited == len(FACES), (visited, len(FACES))
    return incidence

incidences = check_matching_acyclic()

# Eliminating each matched upper/lower pair over the integers gives an
# integral Morse chain complex. The recursion below is the algebraic
# gradient-path expansion with the standard increasing-vertex orientation.
upper_to_lower = {up: low for low, up in pairs}
lower_to_upper = {low: up for low, up in pairs}


def vertices(mask):
    return [v for v in range(N) if (mask >> v) & 1]


@lru_cache(None)
def project(mask):
    if mask in critical:
        return {mask: 1}
    if mask in upper_to_lower:
        return {}
    upper = lower_to_upper[mask]
    vs = vertices(upper)
    removed = (upper ^ mask).bit_length()-1
    incidence_sign = (-1) ** vs.index(removed)
    out = defaultdict(int)
    for i, v in enumerate(vs):
        lower = upper ^ (1 << v)
        if lower == mask:
            continue
        for target, coef in project(lower).items():
            out[target] -= incidence_sign * ((-1) ** i) * coef
    return {target: coef for target, coef in out.items() if coef}


def morse_boundary(mask):
    out = defaultdict(int)
    for i, v in enumerate(vertices(mask)):
        for target, coef in project(mask ^ (1 << v)).items():
            out[target] += ((-1) ** i) * coef
    return {target: coef for target, coef in out.items() if coef}

critical5 = sorted(c for c in critical if c.bit_count() == 6)
critical6 = sorted(c for c in critical if c.bit_count() == 7)
morse_matrix = [[morse_boundary(column).get(row, 0) for column in critical6]
                for row in critical5]
# An actual unimodular maximal minor (the four rows indexed here).
minor_rows = [0, 1, 3, 4]
minor = [[morse_matrix[i][j] for j in range(4)] for i in minor_rows]

def determinant(M):
    if len(M) == 1:
        return M[0][0]
    return sum(((-1) ** i) * M[0][i] * determinant([row[:i] + row[i+1:] for row in M[1:]])
               for i in range(len(M)))
assert abs(determinant(minor)) == 1

# Ordinary mod-2 simplicial boundary ranks, not using the Morse reduction.
by_size = [[m for m in sorted(FACES) if m.bit_count() == k] for k in range(N+1)]

def rank_mod2(cols):
    pivots = {}
    for v in cols:
        while v:
            pivot = v.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = v
                break
            v ^= pivots[pivot]
    return len(pivots)

ranks = {-1: 0, 0: 1}
for k in range(1, 9):
    previous = {face: j for j, face in enumerate(by_size[k])}
    cols = []
    for face in by_size[k+1]:
        bits = face
        v = 0
        while bits:
            bit = bits & -bits
            bits ^= bit
            v ^= 1 << previous[face ^ bit]
        cols.append(v)
    ranks[k] = rank_mod2(cols)
ranks[9] = 0
betti = {k: len(by_size[k+1]) - ranks[k] - ranks[k+1] for k in range(9)}
assert betti == {k: (15 if k == 5 else 0) for k in range(9)}

# Even-weight five-bit representatives identify the vertices with Q_5/antipodes.
# The coordinate permutations and all even translations give 16*120=1920
# automorphisms. The five neighbors of zero determine its stabilizer, giving
# the reverse bound and therefore the full automorphism group.
even_5 = tuple((v ^ (15 if v.bit_count() & 1 else 0)) |
               ((v.bit_count() & 1) << 4) for v in range(N))
assert len(set(even_5)) == 16 and all(x.bit_count() % 2 == 0 for x in even_5)
from_even = {x: v for v, x in enumerate(even_5)}

def permute_five(x, sigma):
    out = 0
    for i in range(5):
        if (x >> i) & 1:
            out |= 1 << sigma[i]
    return out


def orbit_partition(g):
    unseen = set(range(N))
    orbits = []
    while unseen:
        first = min(unseen)
        orbit = []
        v = first
        while v in unseen:
            unseen.remove(v)
            orbit.append(v)
            v = g[v]
        assert v == first
        orbits.append(orbit)
    return orbits


def forest_lefschetz_character(g):
    orbits = orbit_partition(g)
    masks = [sum(1 << v for v in orbit) for orbit in orbits]
    # An invariant oriented simplex is a union of vertex orbits. The
    # combined alternating-simplex and permutation sign is (-1)^number_orbits.
    result = 0
    subsets = [0] * (1 << len(masks))
    for s in range(len(subsets)):
        if s:
            bit = s & -s
            subsets[s] = subsets[s ^ bit] | masks[bit.bit_length()-1]
        if subsets[s] in FACES:
            result += (-1) ** s.bit_count()
    return result

character_counts = Counter()
character_pair_inner = 0
character_sum = 0
traces = []
for sigma in permutations(range(5)):
    sign = (-1) ** sum(sigma[i] > sigma[j] for i in range(5) for j in range(i+1, 5))
    for shift in even_5:
        mapping = tuple(from_even[permute_five(even_5[v], sigma) ^ shift] for v in range(N))
        assert len(set(mapping)) == N
        assert all(((mapping[u] ^ mapping[v]).bit_count() == 1 or (mapping[u] ^ mapping[v]) == 15)
                   for u, v in EDGES)
        computed = forest_lefschetz_character(mapping)
        fixed = sum(mapping[v] == v for v in range(N))
        expected = sign * (fixed - 1)
        assert computed == expected, (sigma, shift, computed, expected)
        traces.append(computed)
        character_counts[computed] += 1
        character_sum += computed
        character_pair_inner += computed**2
assert len(traces) == 1920
assert character_sum == 0
assert character_pair_inner == 1920 * 2
assert dict(sorted(character_counts.items())) == {-7: 20, -1: 835, 0: 384, 1: 540, 3: 140, 15: 1}
assert incidences > 0

report = {
    'graph_vertices': N, 'graph_edges': len(EDGES),
    'face_count_including_empty': len(FACES), 'nonempty_f_vector': f_vector,
    'hasse_incidences': incidences,
    'matched_pairs': len(pairs), 'critical_dimensions': {'5': 19, '6': 4},
    'critical_5_masks': critical5, 'critical_6_masks': critical6,
    'morse_boundary_rows': morse_matrix, 'unimodular_minor_rows_zero_based': minor_rows,
    'unimodular_minor_determinant': determinant(minor),
    'mod2_reduced_betti': betti,
    'mod2_boundary_ranks': ranks,
    'automorphism_group_order': len(traces),
    'homology_character_values_and_multiplicities': dict(sorted(character_counts.items())),
    'homology_character_squared_norm': character_pair_inner // 1920,
    'full_group_invariants_dimension': character_sum // 1920,
}
print(json.dumps(report, sort_keys=True, separators=(',', ':')))
print('VERIFY_OK')
