#!/usr/bin/env python3
"""Exact integral boundary and symmetry checks for a dodecahedral graph complex.

Python 3 standard library only; no external downloads or dependencies.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import lcm

N = 20
E = set()
for i in range(10):
    E.add(tuple(sorted((i, (i + 1) % 10))))
    E.add((i, 10 + i))
    E.add(tuple(sorted((10 + i, 10 + (i + 2) % 10))))
assert len(E) == 30
A = [0] * N
for x, y in E:
    A[x] |= 1 << y
    A[y] |= 1 << x
assert all(z.bit_count() == 3 for z in A)
assert all(not ((A[i] & A[j]).bit_count()) for i, j in E)  # triangle-free

TRIPLES = []
for triple in combinations(range(N), 3):
    if all(not (A[x] >> y & 1) for x, y in combinations(triple, 2)):
        TRIPLES.append(sum(1 << v for v in triple))
assert len(TRIPLES) == 660

# Combinatorial Alexander dual: subsets with no independent triple.
F = {}
for size in range(1, 7):
    F[size] = []
    for vertices in combinations(range(N), size):
        mask = sum(1 << v for v in vertices)
        if not any((mask & t) == t for t in TRIPLES):
            F[size].append(mask)
assert tuple(len(F[k]) for k in range(1, 7)) == (20, 190, 480, 375, 12, 0)


def boundary_columns(size):
    """Integer boundary for oriented simplices, in lexicographic vertex order."""
    index = {face: i for i, face in enumerate(F[size - 1])}
    result = {}
    for col, face in enumerate(F[size]):
        vertices = [i for i in range(N) if face >> i & 1]
        result[col] = {index[face ^ (1 << v)]: (-1) ** j
                       for j, v in enumerate(vertices)}
    return result


def unimodular_rank(size):
    """Unimodular Smith reduction by integral unit pivots.

    A pivot with coefficient +/-1 is eliminated using integral column
    operations, followed by integer row operations clearing its column.
    The code stores only the Schur complement after both operations.
    No division except by a unit occurs. Exhaustive zero remainder proves
    that the Smith factors are exactly the recorded number of ones.
    """
    cols = boundary_columns(size)
    rank = 0
    while True:
        rowcol = defaultdict(list)
        degree = Counter()
        for j, column in cols.items():
            for i, value in column.items():
                degree[i] += 1
                if abs(value) == 1:
                    rowcol[i].append(j)
        if not rowcol:
            break
        _, _, row, pivot = min(
            (degree[row], len(cols[j]), row, j)
            for row, js in rowcol.items() for j in js
        )
        pc = cols.pop(pivot)
        unit = pc[row]
        assert abs(unit) == 1
        for j, column in cols.items():
            coefficient = column.pop(row, 0)
            if coefficient:
                for i, a in pc.items():
                    if i == row:
                        continue
                    updated = column.get(i, 0) - coefficient * unit * a
                    if updated:
                        column[i] = updated
                    else:
                        column.pop(i, None)
        rank += 1
    assert all(not column for column in cols.values()), 'nonunit Smith factors unresolved'
    return rank


assert tuple(unimodular_rank(k) for k in range(2, 6)) == (19, 171, 309, 12)

# Independent finite-field elimination, with no use of the integer pivot routine.
def modular_rank(size, prime):
    cols = boundary_columns(size)
    basis = {}
    for col in cols.values():
        v = {i: a % prime for i, a in col.items() if a % prime}
        while v:
            p = min(v)
            if p not in basis:
                scale = pow(v[p], -1, prime)
                basis[p] = {i: (x * scale) % prime for i, x in v.items()}
                break
            factor = v[p]
            for i, b in basis[p].items():
                new = (v.get(i, 0) - factor * b) % prime
                if new:
                    v[i] = new
                else:
                    v.pop(i, None)
    return len(basis)

for p in (2, 3, 5, 7):
    assert tuple(modular_rank(k, p) for k in range(2, 6)) == (19, 171, 309, 12)

# Exhaustive adjacency-preserving bijections, using backtracking and the
# full assigned/unassigned adjacency profile (not a claimed group order).
P = [-1] * N
AUT = []
search_nodes = 0

def visit(used, depth):
    global search_nodes
    search_nodes += 1
    if depth == N:
        AUT.append(tuple(P))
        return
    u = max((i for i in range(N) if P[i] < 0),
            key=lambda i: (sum(P[j] >= 0 for j in range(N) if A[i] >> j & 1), -i))
    for v in range(N):
        if used >> v & 1:
            continue
        if all(bool(A[u] >> j & 1) == bool(A[v] >> P[j] & 1)
               for j in range(N) if P[j] >= 0):
            P[u] = v
            visit(used | (1 << v), depth + 1)
            P[u] = -1

visit(0, 0)
assert len(AUT) == 120
assert len(set(AUT)) == 120


def sign_of_list(v):
    inversions = sum(a > b for i, a in enumerate(v) for b in v[i + 1:])
    return -1 if inversions % 2 else 1


def cycle_type(p):
    seen = set()
    typ = []
    for i in range(N):
        if i in seen:
            continue
        j = i
        sz = 0
        while j not in seen:
            seen.add(j)
            sz += 1
            j = p[j]
        typ.append(sz)
    return tuple(sorted(typ))


def dual_h3_character(g):
    alternating_trace = 0
    for k in range(1, 6):
        chain_trace = 0
        for mask in F[k]:
            vertices = [i for i in range(N) if mask >> i & 1]
            image = [g[i] for i in vertices]
            if set(image) == set(vertices):
                chain_trace += sign_of_list(image)
        alternating_trace += (-1) ** (k - 1) * chain_trace
    return 1 - alternating_trace


summary = Counter()
character = {}
for g in AUT:
    ct = cycle_type(g)
    order = lcm(*ct)
    # All dodecahedron vertex automorphisms have even permutation sign.
    assert sign_of_list(g) == 1
    trace = dual_h3_character(g)
    summary[(order, trace)] += 1
    character[g] = trace
assert dict(summary) == {(1, 54): 1, (2, 6): 31, (3, 0): 20,
                         (5, -1): 24, (6, 0): 20, (10, 1): 24}
assert sum(character.values()) == 240  # two invariant rational classes

# Identify the central involution using the multiplication of enumerated permutations.
center = []
for g in AUT:
    if all(all(g[h[i]] == h[g[i]] for i in range(N)) for h in AUT):
        center.append(g)
assert len(center) == 2
identity = tuple(range(N))
central = next(g for g in center if g != identity)
assert cycle_type(central) == (2,) * 10
assert character[central] == 6
assert (54 + 6) // 2 == 30 and (54 - 6) // 2 == 24

print('FACES_DUAL: 1,20,190,480,375,12')
print('INDEPENDENT_TRIPLES: 660')
print('UNIT_SMITH_RANKS: 19,171,309,12')
print('DUAL_REDUCED_HOMOLOGY: H3=Z^54; others=0')
print('AUTOMORPHISMS: 120')
print('CHARACTER_BY_ORDER: 1:54x1,2:6x31,3:0x20,5:-1x24,6:0x20,10:1x24')
print('INVARIANT_DIMENSION: 2')
print('CENTRAL_INVOLUTION_EIGEN_DIMS: plus=30 minus=24')
print('VERIFY_OK')

# Independent direct Lefschetz computation on the original total cut
# complex; fixed simplices are precisely unions of permutation cycles.
# Its membership is decided by independent triples in the complement.
FSET = {k: set(F[k]) for k in range(1, 6)}
FULL = (1 << N) - 1

def original_face(face):
    complement = FULL ^ face
    size = complement.bit_count()
    return size >= 6 or (size >= 3 and complement not in FSET[size])


def original_character_direct(g):
    seen = set()
    cyc = []
    for start in range(N):
        if start in seen:
            continue
        pos = start
        mask = 0
        while pos not in seen:
            seen.add(pos)
            mask |= 1 << pos
            pos = g[pos]
        cyc.append(mask)
    masks = [0] * (1 << len(cyc))
    total = 0
    for choice in range(1, len(masks)):
        low = choice & -choice
        prev = choice ^ low
        masks[choice] = masks[prev] | cyc[low.bit_length() - 1]
        if original_face(masks[choice]):
            total += 1 if (choice.bit_count() & 1) else -1
    return total - 1  # reduced Euler trace

for g in AUT:
    assert original_character_direct(g) == character[g]
print('DIRECT_ORIGINAL_COMPLEX_LEFSCHETZ: 120/120 agree')
print('VERIFICATION_COMPLETE')
