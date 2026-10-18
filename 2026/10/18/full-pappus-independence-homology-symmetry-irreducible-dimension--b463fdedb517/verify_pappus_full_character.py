#!/usr/bin/env python3
"""Exact, standard-library verification of a Pappus independence homology character."""
from collections import Counter

F = range(3)
POINTS = [(x, y) for x in F for y in F]
LINES = [(m, b) for m in F for b in F]
P_INDEX = {p: i for i, p in enumerate(POINTS)}
L_INDEX = {l: 9 + i for i, l in enumerate(LINES)}
EDGES = {frozenset((P_INDEX[(x, y)], L_INDEX[(m, b)]))
         for x, y in POINTS for m, b in LINES if (m * x + b - y) % 3 == 0}
assert len(EDGES) == 27
VERTICES = tuple(range(18))
IDENTITY = VERTICES

def compose(g, h):
    return tuple(g[h[i]] for i in VERTICES)

def inverse(g):
    return tuple(g.index(i) for i in VERTICES)

def preserving(a, b, c, d, e):
    """A triangular invertible affine transformation and its line action."""
    g = [None] * 18
    for x, y in POINTS:
        g[P_INDEX[(x, y)]] = P_INDEX[((a*x+b) % 3, (c*x+d*y+e) % 3)]
    for m, k in LINES:
        mp = (a*(c+d*m)) % 3  # a inverse equals a over F_3
        kp = (d*k+e-mp*b) % 3
        g[L_INDEX[(m, k)]] = L_INDEX[(mp, kp)]
    return tuple(g)

def duality():
    g = [None] * 18
    for x, y in POINTS:
        g[P_INDEX[(x, y)]] = L_INDEX[(x, (-y) % 3)]
    for m, b in LINES:
        g[L_INDEX[(m, b)]] = P_INDEX[(m, (-b) % 3)]
    return tuple(g)

H = [preserving(a,b,c,d,e) for a in (1,2) for b in F for c in F
     for d in (1,2) for e in F]
DELTA = duality()
G = H + [compose(DELTA, h) for h in H]
assert len(G) == len(set(G)) == 216
assert len(H) == 108 and compose(DELTA, DELTA) == IDENTITY
assert all({frozenset((g[u], g[v])) for u,v in (tuple(edge) for edge in EDGES)} == EDGES for g in G)
assert set(compose(g,h) for g in (IDENTITY,DELTA) for h in H).issubset(set(G))

# Enumerate *all* independent sets, including the empty face.
NEIGHBORS = [0] * 18
for u, v in (tuple(edge) for edge in EDGES):
    NEIGHBORS[u] |= 1 << v
    NEIGHBORS[v] |= 1 << u
FACES = [0]
for vertex in VERTICES:
    FACES += [s | (1 << vertex) for s in FACES if not (s & NEIGHBORS[vertex])]
F_VECTOR = Counter(s.bit_count()-1 for s in FACES if s)
assert len(FACES) == 2598
assert tuple(F_VECTOR[i] for i in range(9)) == (18,126,438,801,756,348,90,18,2)

# An independent full enumeration of the simplicial boundaries modulo two.
GROUPED = {i: sorted(s for s in FACES if s.bit_count() == i+1) for i in range(9)}
def rank_mod2(dim):
    lower_index = {s: j for j, s in enumerate(GROUPED[dim-1])}
    pivots = {}
    for face in GROUPED[dim]:
        col = 0
        for v in VERTICES:
            if (face >> v) & 1:
                col ^= 1 << lower_index[face ^ (1 << v)]
        while col:
            i = col.bit_length() - 1
            if i in pivots:
                col ^= pivots[i]
            else:
                pivots[i] = col
                break
    return len(pivots)
RANKS = tuple(rank_mod2(i) for i in range(1, 9))
assert RANKS == (17,109,329,472,274,74,16,2)
bettis = tuple(len(GROUPED[i]) - (RANKS[i-1] if i else 0)
                - (RANKS[i] if i < 8 else 0) for i in range(9))
assert bettis == (1,0,0,0,10,0,0,0,0)
assert sum((-1)**i * len(GROUPED[i]) for i in range(9)) == 11

# Exact augmented Lefschetz trace on all oriented independent faces.
FACE_VERTICES = [tuple(i for i in VERTICES if (s >> i) & 1) for s in FACES[1:]]
def chi(g):
    result = -1  # augmented empty face contributes minus one
    for face in FACE_VERTICES:
        image = tuple(g[i] for i in face)
        if set(image) != set(face):
            continue
        inversions = sum(image[i] > image[j] for i in range(len(image))
                         for j in range(i+1, len(image)))
        result += (-1) ** (len(face) - 1 + inversions)
    return result

CHAR = {g: chi(g) for g in G}
assert len(CHAR) == 216
assert CHAR[IDENTITY] == 10
assert sum(CHAR.values()) == 0
assert sum(t*t for t in CHAR.values()) == 2*216
assert Counter(CHAR.values()) == {-2:21, -1:72, 0:54, 1:32, 2:36, 10:1}

# The normal order-three vertical translation subgroup.
Z = preserving(1,0,0,1,1)
Z2 = compose(Z,Z)
assert compose(Z,Z2) == IDENTITY
assert CHAR[Z] == CHAR[Z2] == 1
assert all(compose(compose(g, Z), inverse(g)) in (Z,Z2) for g in G)

# The rational central idempotent (1+z+z^2)/3 defines the 4D summand.
CHAR4 = {}
CHAR6 = {}
for g in G:
    numerator = CHAR[g] + CHAR[compose(Z,g)] + CHAR[compose(Z2,g)]
    assert numerator % 3 == 0
    CHAR4[g] = numerator // 3
    CHAR6[g] = CHAR[g] - CHAR4[g]
assert CHAR4[IDENTITY] == 4 and CHAR6[IDENTITY] == 6
assert sum(a*a for a in CHAR4.values()) == 216
assert sum(b*b for b in CHAR6.values()) == 216
assert sum(CHAR4[g]*CHAR6[g] for g in G) == 0
assert sum(CHAR4.values()) == sum(CHAR6.values()) == 0

def element_order(g):
    h = IDENTITY
    for r in range(1,217):
        h = compose(g,h)
        if h == IDENTITY:
            return r
    raise AssertionError('nonfinite group element')

TABLE = Counter((element_order(g), 'preserving' if g[0] < 9 else 'exchanging',
                 CHAR4[g],CHAR6[g]) for g in G)
EXPECTED = {
    (1,'preserving',4,6):1,
    (2,'exchanging',0,0):18,
    (2,'preserving',0,-2):9,
    (2,'preserving',2,0):18,
    (3,'preserving',-2,0):12,
    (3,'preserving',1,0):12,
    (3,'preserving',4,-3):2,
    (4,'exchanging',0,2):18,
    (6,'exchanging',0,0):36,
    (6,'preserving',-1,0):36,
    (6,'preserving',0,1):18,
    (12,'exchanging',0,-1):36,
}
assert TABLE == EXPECTED
print('PASS: 18 vertices, 27 edges; all 216 automorphisms represented.')
print('PASS: all 2598 independent faces, rank vector', RANKS, 'and rational Betti vector', bettis)
print('PASS: full top rational character: degree 10, norm squared 2, no invariant line.')
print('PASS: normal cyclic subgroup of order 3 separates absolutely irreducible 4D and 6D modules.')
print('Exact 216-element distribution (order, side, trace4, trace6, multiplicity):')
for (o, side, t4, t6), mult in sorted(TABLE.items()):
    print(o, side, t4, t6, mult)
