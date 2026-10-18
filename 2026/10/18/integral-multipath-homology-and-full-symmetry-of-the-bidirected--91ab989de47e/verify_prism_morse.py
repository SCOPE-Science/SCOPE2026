#!/usr/bin/env python3
"""Exact chain-level verification for the bidirected triangular-prism multipath complex.
Uses only the Python standard library. Integer coefficients throughout the Morse calculation.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 6
UNDIRECTED = sorted(
    {tuple(sorted((i, (i + 1) % 3))) for i in range(3)}
    | {tuple(sorted((3 + i, 3 + (i + 1) % 3))) for i in range(3)}
    | {(i, i + 3) for i in range(3)}
)
ARCS = sorted([(u, v) for u, v in UNDIRECTED] +
              [(v, u) for u, v in UNDIRECTED])
assert len(UNDIRECTED) == 9 and len(ARCS) == 18
ARC_ID = {a: i for i, a in enumerate(ARCS)}
M = len(ARCS)
TOGGLE_ORDER = (13, 12, 4, 9, 5, 7, 16, 6, 10,
                15, 1, 11, 2, 14, 17, 8, 0, 3)
assert sorted(TOGGLE_ORDER) == list(range(M))


def permitted(mask):
    incoming = [0] * N
    outgoing = [0] * N
    successor = [-1] * N
    for i, (u, v) in enumerate(ARCS):
        if mask & (1 << i):
            incoming[v] += 1
            outgoing[u] += 1
            if incoming[v] > 1 or outgoing[u] > 1:
                return False
            successor[u] = v
    for start in range(N):
        seen = set()
        v = start
        while successor[v] != -1:
            if v in seen:
                return False
            seen.add(v)
            v = successor[v]
    return True


ALL = {mask for mask in range(1, 1 << M) if permitted(mask)}
assert len(ALL) == 686
fvector = Counter(mask.bit_count() - 1 for mask in ALL)
assert [fvector[i] for i in range(5)] == [18, 108, 260, 240, 60]


def bdry(mask):
    indices = [i for i in range(M) if mask & (1 << i)]
    return [(mask ^ (1 << i), 1 if j % 2 == 0 else -1)
            for j, i in enumerate(indices)]


# A full matching on every stage's remaining cells, with the empty face excluded.
unmatched = set(ALL)
PAIRS = []
for vertex in TOGGLE_ORDER:
    bit = 1 << vertex
    for f in sorted(unmatched):
        if f & bit:
            continue
        h = f | bit
        if h in unmatched:
            unmatched.remove(f)
            unmatched.remove(h)
            PAIRS.append((f, h))
CRITICAL = set(unmatched)
LOW_HIGH = dict(PAIRS)
HIGH = {h for _, h in PAIRS}
assert len(PAIRS) == 326 and len(CRITICAL) == 34
assert Counter(c.bit_count() - 1 for c in CRITICAL) == {0: 1, 2: 5, 3: 22, 4: 6}
assert len(set(LOW_HIGH)) == len(PAIRS) == len(HIGH)

# Reversed matching edges in a downward-oriented Hasse diagram must be acyclic.
indegree = {f: 0 for f in ALL}
adj = {f: [] for f in ALL}
matching_edges = set(PAIRS)
cover_count = 0
for h in ALL:
    for f, _ in bdry(h):
        if f == 0:
            continue
        u, v = (f, h) if (f, h) in matching_edges else (h, f)
        adj[u].append(v)
        indegree[v] += 1
        cover_count += 1
queue = deque(f for f, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert cover_count == 2256 and visited == len(ALL)


@lru_cache(None)
def proj(f):
    """Integral projection of an oriented simplex to Morse-critical cells."""
    if f in CRITICAL:
        return {f: 1}
    if f in HIGH:
        return {}
    assert f in LOW_HIGH
    h = LOW_HIGH[f]
    a = next(c for t, c in bdry(h) if t == f)
    result = defaultdict(int)
    for t, coeff in bdry(h):
        if t == f:
            continue
        for z, value in proj(t).items():
            result[z] -= a * coeff * value
    return {z: value for z, value in result.items() if value}


@lru_cache(None)
def chain_homotopy(f):
    """Matching homotopy from a lower paired face to its upper partner."""
    if f not in LOW_HIGH:
        return {}
    h = LOW_HIGH[f]
    a = next(c for t, c in bdry(h) if t == f)
    result = defaultdict(int)
    result[h] += a
    for t, coeff in bdry(h):
        if t == f:
            continue
        for z, value in chain_homotopy(t).items():
            result[z] -= a * coeff * value
    return {z: value for z, value in result.items() if value}


BY_DIM = {k: sorted(c for c in CRITICAL if c.bit_count() == k + 1)
          for k in (0, 2, 3, 4)}
for k in (3, 4):
    for c in BY_DIM[k]:
        differential = defaultdict(int)
        for f, coeff in bdry(c):
            for z, val in proj(f).items():
                differential[z] += coeff * val
        assert not any(differential.values())


def lift(c):
    """Integral cycle representing the specified critical generator."""
    result = defaultdict(int)
    result[c] = 1
    for f, coeff in bdry(c):
        for z, value in chain_homotopy(f).items():
            result[z] -= coeff * value
    result = {z: value for z, value in result.items() if value}
    out = defaultdict(int)
    for z, value in result.items():
        for f, coeff in bdry(z):
            out[f] += value * coeff
    assert not any(out.values()), c
    reduced = defaultdict(int)
    for z, value in result.items():
        for f, coeff in proj(z).items():
            reduced[f] += value * coeff
    assert {z: v for z, v in reduced.items() if v} == {c: 1}
    return result


LIFTS = {k: {c: lift(c) for c in BY_DIM[k]} for k in (2, 3, 4)}


def vperm(i, rot, refl, swap):
    return (((-1 if refl else 1) * (i % 3) + rot) % 3) + 3 * ((i // 3) ^ swap)


def arcperm(rot, refl, swap):
    return tuple(ARC_ID[(vperm(u, rot, refl, swap),
                         vperm(v, rot, refl, swap))] for u, v in ARCS)


def image_face(face, permutation):
    mapped = [permutation[i] for i in range(M) if face & (1 << i)]
    parity = sum(mapped[i] > mapped[j] for i in range(len(mapped))
                 for j in range(i + 1, len(mapped))) % 2
    return sum(1 << i for i in mapped), (-1 if parity else 1)


def homology_action(k, permutation):
    basis = BY_DIM[k]
    index = {c: j for j, c in enumerate(basis)}
    output = [[0] * len(basis) for _ in basis]
    for col, c in enumerate(basis):
        result = defaultdict(int)
        for f, coeff in LIFTS[k][c].items():
            mapped, sign = image_face(f, permutation)
            for z, val in proj(mapped).items():
                result[z] += coeff * sign * val
        for z, value in result.items():
            output[index[z]][col] = value
    return output


def product(a, b):
    return [[sum(a[i][z] * b[z][j] for z in range(len(a)))
             for j in range(len(a))] for i in range(len(a))]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


CHARS = {}
for rot in range(3):
    for refl in range(2):
        for swap in range(2):
            p = arcperm(rot, refl, swap)
            CHARS[rot, refl, swap] = tuple(
                sum(homology_action(k, p)[i][i] for i in range(len(BY_DIM[k])))
                for k in (2, 3, 4))
for k in (2, 3, 4):
    R = homology_action(k, arcperm(1, 0, 0))
    S = homology_action(k, arcperm(0, 1, 0))
    T = homology_action(k, arcperm(0, 0, 1))
    I = eye(len(BY_DIM[k]))
    assert product(product(R, R), R) == I
    assert product(S, S) == I
    assert product(T, T) == I
    assert product(product(S, R), S) == product(R, R)
    assert product(T, R) == product(R, T)
    assert product(T, S) == product(S, T)

# Check the homological trace using the signed simplicial Lefschetz number.
for key, hchar in CHARS.items():
    permutation = arcperm(*key)
    trace_chain = []
    for k in range(5):
        trace_chain.append(sum(sign for f in ALL if f.bit_count() == k + 1
                               for mapped, sign in [image_face(f, permutation)]
                               if f == mapped))
    assert sum((-1) ** k * trace_chain[k] for k in range(5)) == \
        1 + hchar[0] - hchar[1] + hchar[2]

expected = {
    (0, 0, 0): (5, 22, 6),
    (1, 0, 0): (5, 4, 0),
    (0, 1, 0): (-1, 0, 0),
    (0, 0, 1): (1, 2, 0),
    (1, 0, 1): (1, 2, 0),
    (0, 1, 1): (-1, 0, -2),
}
for key, answer in expected.items():
    assert CHARS[key] == answer
assert len(CHARS) == 12
invariants = tuple(sum(v[j] for v in CHARS.values()) // len(CHARS)
                   for j in range(3))
assert invariants == (1, 3, 0)

print('arc_vertices:', M)
print('face_numbers_dim_0_through_4:', [fvector[k] for k in range(5)])
print('nonempty_faces:', len(ALL))
print('Hasse_covers:', cover_count)
print('acyclic_matching_pairs:', len(PAIRS))
print('critical_cells_dim_0_2_3_4:', [len(BY_DIM[k]) for k in (0, 2, 3, 4)])
print('integral_morse_d3_d4: ZERO')
print('homology_ranks_dim_2_3_4:', [len(BY_DIM[k]) for k in (2, 3, 4)])
for key in sorted(expected):
    print('character_(rotation_reflection_layerswap)', key, expected[key])
print('fully_invariant_dimensions_dim_2_3_4:', invariants)
print('exact_chain_symmetry_verification: PASS')
