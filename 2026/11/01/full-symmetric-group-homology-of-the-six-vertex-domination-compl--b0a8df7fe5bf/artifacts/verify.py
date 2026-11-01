#!/usr/bin/env python3
"""Exact integral chain and symmetric-group character verification for D_{6,3}.

Requires only Python 3 standard library. No precomputed mathematical certificates.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations
from math import factorial

N = 6
EDGES = list(combinations(range(N), 2))
EDGE_ID = {pair: j for j, pair in enumerate(EDGES)}
ALL_VERTICES = (1 << N) - 1
FACES = defaultdict(list)


def qualifies(edge_mask):
    neighbor = [0] * N
    for j, (u, v) in enumerate(EDGES):
        if (edge_mask >> j) & 1:
            neighbor[u] |= 1 << v
            neighbor[v] |= 1 << u
    closed = [neighbor[u] | (1 << u) for u in range(N)]
    a = all((closed[i] | closed[j]) != ALL_VERTICES
            for i, j in combinations(range(N), 2))
    # Independent formulation: every pair of closed-neighborhood complements intersects.
    omitted = [ALL_VERTICES ^ closed[u] for u in range(N)]
    b = all((omitted[i] & omitted[j]) != 0
            for i, j in combinations(range(N), 2))
    assert a == b, 'independent admissibility tests differ'
    return a


for mask in range(1 << len(EDGES)):
    if qualifies(mask):
        FACES[mask.bit_count() - 1].append(mask)

FVECTOR = (15, 105, 455, 1185, 1647, 915, 180)
assert tuple(len(FACES[d]) for d in range(7)) == FVECTOR
assert sum(FVECTOR) == 4502
for d in range(1, 7):
    lower = set(FACES[d - 1])
    for face in FACES[d]:
        for bit in range(len(EDGES)):
            if face & (1 << bit):
                assert (face ^ (1 << bit)) in lower


def boundary(face, index):
    active = [i for i in range(len(EDGES)) if (face >> i) & 1]
    return {index[face ^ (1 << i)]: (1 if j % 2 == 0 else -1)
            for j, i in enumerate(active)}


def eliminate(columns):
    """Integral sparse basis using unit triangular pivots (not floating point)."""
    basis = {}
    for original in columns:
        col = dict(original)
        while col:
            pivot = max(col)
            if pivot not in basis:
                break
            coeff = col[pivot]
            for row, val in basis[pivot].items():
                z = col.get(row, 0) - coeff * val
                if z:
                    col[row] = z
                else:
                    col.pop(row, None)
        if col:
            pivot = max(col)
            unit = col[pivot]
            assert unit in (-1, 1), (pivot, unit)
            basis[pivot] = {r: unit * v for r, v in col.items()}
    return basis


INDEX = {d: {mask: i for i, mask in enumerate(FACES[d])} for d in range(7)}
BOUNDARY_BASES = {}
for dim in range(1, 7):
    BOUNDARY_BASES[dim] = eliminate(boundary(face, INDEX[dim - 1])
                                    for face in FACES[dim])
RANKS = tuple(len(BOUNDARY_BASES[d]) for d in range(1, 7))
assert RANKS == (14, 91, 364, 821, 711, 180), RANKS
BETTI = tuple((FVECTOR[d] - (RANKS[d-1] if d else 0)
               - (RANKS[d] if d < 6 else 0)) for d in range(7))
assert BETTI == (1, 0, 0, 0, 115, 24, 0), BETTI
# Unit triangular pivots give a primitive minor and the full integral rank.
# Since each image has a basis extendible to a free ambient basis, all homology is torsion-free.

# Check boundary-square-zero on every basis simplex, with ordinary signed orientations.
for dim in range(2, 7):
    for face in FACES[dim]:
        z = defaultdict(int)
        for row, coeff in boundary(face, INDEX[dim-1]).items():
            f = FACES[dim-1][row]
            for col, c in boundary(f, INDEX[dim-2]).items():
                z[col] += coeff*c
        assert all(v == 0 for v in z.values())


def partitions(n, upper=None):
    if n == 0:
        yield ()
        return
    if upper is None:
        upper = n
    for j in range(min(n, upper), 0, -1):
        for rest in partitions(n-j, j):
            yield (j,) + rest


def canonical_permutation(cycle_type):
    output = []
    start = 0
    for k in cycle_type:
        output += [start + (i+1) % k for i in range(k)]
        start += k
    return tuple(output)


def permute_face(face, vertex_permutation):
    old = [j for j in range(len(EDGES)) if (face >> j) & 1]
    transformed = []
    for j in old:
        u,v = EDGES[j]
        transformed.append(EDGE_ID[tuple(sorted((vertex_permutation[u],vertex_permutation[v])))] )
    new_mask = sum(1 << x for x in transformed)
    inversions = sum(transformed[i] > transformed[j]
                     for i in range(len(transformed))
                     for j in range(i+1, len(transformed)))
    return new_mask, (-1 if inversions % 2 else 1)


def chain_trace(dim, g):
    return sum(sign for face in FACES[dim]
               for transformed, sign in [permute_face(face, g)]
               if transformed == face)


def image_trace_dim5(g, alternative=None):
    # The normalized triangular integral basis is an honest Z-basis of im(partial_5).
    # Compute trace on this image by acting on the 4-chain coordinate vectors.
    b = BOUNDARY_BASES[5] if alternative is None else alternative
    tr = 0
    for own_pivot, original in b.items():
        moved = {}
        for row, value in original.items():
            mask, sign = permute_face(FACES[4][row], g)
            new_row = INDEX[4][mask]
            z = moved.get(new_row, 0) + sign*value
            if z:
                moved[new_row] = z
            else:
                moved.pop(new_row, None)
        while moved:
            pivot = max(moved)
            assert pivot in b, ('image not invariant', pivot)
            coefficient = moved[pivot]
            if pivot == own_pivot:
                tr += coefficient
            for row, value in b[pivot].items():
                z = moved.get(row, 0) - coefficient*value
                if z:
                    moved[row] = z
                else:
                    moved.pop(row, None)
    return tr


def rim_hooks(lam, length):
    for smaller in partitions(sum(lam) - length):
        if len(smaller) > len(lam) or any(smaller[i]>lam[i] for i in range(len(smaller))):
            continue
        strip = {(r,c) for r,n in enumerate(lam)
                 for c in range(1,n+1)
                 if c > (smaller[r] if r<len(smaller) else 0)}
        if len(strip)!=length or not strip:
            continue
        if any({(r,c),(r+1,c),(r,c+1),(r+1,c+1)} <= strip for r,c in strip):
            continue
        found={next(iter(strip))}
        stack=list(found)
        while stack:
            r,c=stack.pop()
            for pair in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if pair in strip and pair not in found:
                    found.add(pair)
                    stack.append(pair)
        if len(found)==length:
            rows=[r for r,c in strip]
            yield smaller, (-1)**(max(rows)-min(rows))


@lru_cache(None)
def irrep_character(lam, cycles):
    if not cycles:
        return int(not lam)
    return sum(sign * irrep_character(smaller,cycles[1:])
               for smaller,sign in rim_hooks(lam,cycles[0]))


def class_size(part):
    z=1
    for k,v in Counter(part).items():
        z *= k**v * factorial(v)
    return factorial(N)//z


TYPES = list(partitions(N))
CHAR4 = []
CHAR5 = []
for typ in TYPES:
    perm = canonical_permutation(typ)
    c5 = chain_trace(5,perm)
    c6 = chain_trace(6,perm)
    image = image_trace_dim5(perm)
    # partial_6 injective, so im(partial_6) is C6 equivariantly.
    h5 = c5 - image - c6
    reduced_euler = sum((-1)**d*chain_trace(d,perm) for d in range(7))-1
    # Only positive homology H4, H5 survives.
    h4 = reduced_euler + h5
    CHAR4.append(h4)
    CHAR5.append(h5)
    fixed=sum(i==perm[i] for i in range(N))
    assert h5 == (fixed-1)**2-1, ('tensor-square character',typ,h5)

assert CHAR4 == [0,0,-1,-1,-2,0,-2,3,3,3,115],CHAR4
assert CHAR5 == [0,-1,0,0,0,-1,3,0,0,8,24],CHAR5
MULT4={};MULT5={}
for lam in TYPES:
    row=[irrep_character(lam,typ) for typ in TYPES]
    assert sum(class_size(typ)*v*v for typ,v in zip(TYPES,row)) == factorial(N)
    t4=sum(class_size(typ)*v*h for typ,v,h in zip(TYPES,row,CHAR4))
    t5=sum(class_size(typ)*v*h for typ,v,h in zip(TYPES,row,CHAR5))
    assert t4%factorial(N)==t5%factorial(N)==0
    m4=t4//factorial(N)
    m5=t5//factorial(N)
    assert m4>=0 and m5>=0
    if m4: MULT4[lam]=m4
    if m5: MULT5[lam]=m5
assert MULT4=={
    (5,1):1, (4,2):2, (4,1,1):1, (3,3):1,
    (3,2,1):3,(3,1,1,1):1,(2,2,2):1,(2,2,1,1):1,
    (2,1,1,1,1):1
},MULT4
assert MULT5=={(5,1):1,(4,2):1,(4,1,1):1},MULT5
assert not (6,) in MULT4 and not (6,) in MULT5

# Independent pivot ordering: rebuild the degree-five image lattice backwards.
REVERSED_BASIS = eliminate(boundary(face, INDEX[4])
                           for face in reversed(FACES[5]))
assert len(REVERSED_BASIS) == 711
for typ, expected in zip(TYPES, CHAR5):
    g = canonical_permutation(typ)
    actual = chain_trace(5,g) - image_trace_dim5(g, REVERSED_BASIS) - chain_trace(6,g)
    assert actual == expected, ('basis-independent character',typ,actual,expected)

print('D63_S6_INTEGRAL_CHAIN_CHARACTER_VERIFIED')
print('F_VECTOR',FVECTOR)
print('INTEGRAL_UNIT_PIVOT_RANKS',RANKS)
print('BETTI',BETTI)
print('CYCLE_TYPES',TYPES)
print('CHAR_H4',CHAR4)
print('CHAR_H5',CHAR5)
print('MULT_H4',MULT4)
print('MULT_H5',MULT5)
print('ALTERNATE_INTEGER_BASIS_CHARACTER_CHECK', True)
print('QUOTIENT_REDUCED_RATIONAL_HOMOLOGY_ZERO',True)
