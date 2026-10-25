#!/usr/bin/env python3
"""Reproduce the Petersen line-graph Rips and S5 character calculation.

Only Python's standard library is required. All graph, chain, and group data
are rebuilt from 2-subsets of five points; there are no external inputs.
"""
from collections import Counter
from itertools import combinations, permutations, product

POINTS = tuple(range(5))
P_VERTICES = tuple(combinations(POINTS, 2))
P_EDGES = tuple((a, b) for a, b in combinations(P_VERTICES, 2)
                if not (set(a) & set(b)))
assert len(P_VERTICES) == 10 and len(P_EDGES) == 15


def pairing_label(edge):
    a, b = edge
    missing = next(iter(set(POINTS) - set(a) - set(b)))
    return missing, tuple(sorted((a, b)))


L_VERTICES = tuple(sorted(pairing_label(e) for e in P_EDGES))
L_INDEX = {v: i for i, v in enumerate(L_VERTICES)}
assert len(set(L_VERTICES)) == 15
FIBERS = {a: tuple(i for i, (b, _) in enumerate(L_VERTICES) if a == b)
          for a in POINTS}
assert all(len(f) == 3 for f in FIBERS.values())
L_EDGES = set()
for a, b in combinations(range(15), 2):
    x = set(L_VERTICES[a][1])
    y = set(L_VERTICES[b][1])
    if x & y:
        L_EDGES.add((a, b))
assert len(L_EDGES) == 30


def dist(i, j):
    if i == j:
        return 0
    if (min(i, j), max(i, j)) in L_EDGES:
        return 1
    if any((min(i, k), max(i, k)) in L_EDGES and
           (min(j, k), max(j, k)) in L_EDGES for k in range(15) if k not in (i, j)):
        return 2
    return 3


for a, b in combinations(range(15), 2):
    assert (dist(a, b) == 3) == (L_VERTICES[a][0] == L_VERTICES[b][0])
assert Counter(dist(a, b) for a, b in combinations(range(15), 2)) == {1: 30, 2: 60, 3: 15}

# These are exact face lists, not a random sample.
FACES_0 = [()] + [(i,) for i in range(15)]
FACES_1 = [()] + [(i,) for i in range(15)] + sorted(L_EDGES)
FACES_1 += [c for c in combinations(range(15), 3)
            if all((a, b) in L_EDGES for a, b in combinations(c, 2))]
assert len(FACES_1) == 56
FACES_2 = [tuple(sorted(v for v in picks if v is not None))
           for picks in product(*((None,) + FIBERS[i] for i in POINTS))]
assert len(FACES_2) == 1024 and len(set(FACES_2)) == 1024
assert Counter(len(x) for x in FACES_2) == {0: 1, 1: 15, 2: 90, 3: 270, 4: 405, 5: 243}


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            top = col.bit_length() - 1
            if top not in pivots:
                pivots[top] = col
                break
            col ^= pivots[top]
    return len(pivots)


def reduced_betti(faces):
    max_size = max(map(len, faces))
    sets = {k: sorted(f for f in faces if len(f) == k) for k in range(max_size + 1)}
    ranks = {}
    for k in range(2, max_size + 1):
        lowindex = {f: i for i, f in enumerate(sets[k - 1])}
        columns = []
        for f in sets[k]:
            bits = 0
            for idx in range(k):
                bits ^= 1 << lowindex[f[:idx] + f[idx + 1:]]
            columns.append(bits)
        ranks[k] = rank_mod2(columns)
    # For connected nonempty complexes, reduced rank H_0 = n_0-1-rank(d1).
    out = [len(sets[1]) - 1 - ranks.get(2, 0)]
    for k in range(2, max_size + 1):
        out.append(len(sets[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0))
    return out, ranks


b1, ranks1 = reduced_betti(FACES_1)
b2, ranks2 = reduced_betti(FACES_2)
assert b1 == [0, 6, 0], (b1, ranks1)
assert b2 == [0, 0, 0, 0, 32], (b2, ranks2)
assert ranks1 == {2: 14, 3: 10}
assert ranks2 == {2: 14, 3: 76, 4: 194, 5: 211}


def parity(values):
    return (-1) ** sum(a > b for i, a in enumerate(values) for b in values[i + 1:])


def permute_label(sigma, label):
    missing, blocks = label
    return sigma[missing], tuple(sorted(tuple(sorted(sigma[x] for x in block))
                                        for block in blocks))


def induced_perm(sigma):
    return tuple(L_INDEX[permute_label(sigma, label)] for label in L_VERTICES)


def lefschetz(faces, perm):
    """Reduced simplicial Lefschetz trace, including the empty face."""
    total = -1
    for face in faces:
        if not face:
            continue
        moved = tuple(perm[i] for i in face)
        if tuple(sorted(moved)) == face:
            total += (-1) ** (len(face) - 1) * parity(moved)
    return total


def cycles(sigma):
    unseen = set(POINTS)
    answer = []
    while unseen:
        start = min(unseen)
        orbit = []
        i = start
        while i in unseen:
            unseen.remove(i)
            orbit.append(i)
            i = sigma[i]
        answer.append(tuple(orbit))
    return answer


def cycle_type(sigma):
    return tuple(sorted((len(c) for c in cycles(sigma)), reverse=True))


def power_perm(sigma, length):
    out = tuple(POINTS)
    for _ in range(length):
        out = tuple(sigma[i] for i in out)
    return out


def join_character(sigma):
    """Twisted tensor trace on join of five 3-point complexes."""
    trace = parity(sigma)
    for c in cycles(sigma):
        index = c[0]
        power = power_perm(sigma, len(c))
        fixed = sum(permute_label(power, L_VERTICES[i]) == L_VERTICES[i]
                    for i in FIBERS[index])
        trace *= (fixed - 1)
    return trace


def graph_cycle_character(sigma):
    """Alternating cellular character 1-C0+C1 of the Petersen graph."""
    fixed_vertices = sum(tuple(sorted(sigma[x] for x in a)) == a for a in P_VERTICES)
    signed_edges = 0
    for a, b in P_EDGES:
        new_a = tuple(sorted(sigma[x] for x in a))
        new_b = tuple(sorted(sigma[x] for x in b))
        if {new_a, new_b} == {a, b}:
            signed_edges += 1 if (new_a, new_b) == (a, b) else -1
    return 1 - fixed_vertices + signed_edges


CHARS1, CHARS4, SIZES = {}, {}, Counter()
for sigma in permutations(POINTS):
    perm = induced_perm(sigma)
    # Independent direct signed fixed-simplex calculations at both radii.
    c1 = -lefschetz(FACES_1, perm)
    c4 = lefschetz(FACES_2, perm)
    assert c1 == graph_cycle_character(sigma)
    assert c4 == join_character(sigma)
    # The permutation preserves the graph metric independently of the formula.
    assert all(dist(a, b) == dist(perm[a], perm[b])
               for a, b in combinations(range(15), 2))
    key = cycle_type(sigma)
    if key in CHARS1:
        assert (CHARS1[key], CHARS4[key]) == (c1, c4)
    else:
        CHARS1[key], CHARS4[key] = c1, c4
    SIZES[key] += 1

CLASSES = ((1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1),
           (3, 1, 1), (3, 2), (4, 1), (5,))
assert [SIZES[k] for k in CLASSES] == [1, 10, 15, 20, 20, 30, 24]
assert [CHARS1[k] for k in CLASSES] == [6, 0, -2, 0, 0, 0, 1]
assert [CHARS4[k] for k in CLASSES] == [32, 0, 8, 2, 0, 0, 2]


def inner(f, g):
    num = sum(SIZES[k] * f[k] * g[k] for k in CLASSES)
    assert num % 120 == 0
    return num // 120


# Seven rational irreducible characters derived from standard S5 constructions.
IRREP = {i: {} for i in ('5', '11111', '41', '2111', '32', '221', '311')}
for key in CLASSES:
    # Representative in the cycle class.
    pos, perm = 0, list(range(5))
    for length in key:
        cycle = list(range(pos, pos + length))
        for index, j in enumerate(cycle):
            perm[j] = cycle[(index + 1) % length]
        pos += length
    perm = tuple(perm)
    standard = sum(perm[i] == i for i in POINTS) - 1
    sign = parity(perm)
    fixed_two_sets = sum({perm[i], perm[j]} == {i, j} for i, j in combinations(POINTS, 2))
    two_row = fixed_two_sets - 1 - standard
    sq = power_perm(perm, 2)
    wedge = (standard ** 2 - (sum(sq[i] == i for i in POINTS) - 1)) // 2
    for name, val in {
        '5': 1, '11111': sign, '41': standard, '2111': standard * sign,
        '32': two_row, '221': two_row * sign, '311': wedge
    }.items():
        IRREP[name][key] = val
assert all(inner(IRREP[a], IRREP[b]) == (a == b)
           for a in IRREP for b in IRREP)
assert {a: inner(CHARS4, c) for a, c in IRREP.items()} == {
    '5': 2, '11111': 2, '41': 1, '2111': 1, '32': 2, '221': 2, '311': 0}
assert {a: inner(CHARS1, c) for a, c in IRREP.items()} == {
    '5': 0, '11111': 0, '41': 0, '2111': 0, '32': 0, '221': 0, '311': 1}
assert inner(CHARS4, IRREP['5']) == 2

print('PETERSEN_LINE_RIPS_EQUIVARIANT_CHECKS_OK',
      'r1_faces', len(FACES_1), 'r2_faces', len(FACES_2),
      'permutations', sum(SIZES.values()))
