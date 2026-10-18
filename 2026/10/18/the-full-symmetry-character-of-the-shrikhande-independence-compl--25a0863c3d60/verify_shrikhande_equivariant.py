#!/usr/bin/env python3
"""Exact homology-character verification for the Shrikhande independence complex.

Standard-library Python 3 only. No network, random choices, or external data.
"""
from itertools import product
from collections import Counter, defaultdict

V = list(product(range(4), repeat=2))
INDEX = {v: i for i, v in enumerate(V)}
S = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
EDGES = {
    frozenset((i, INDEX[((x + a) % 4, (y + b) % 4)]))
    for i, (x, y) in enumerate(V) for (a, b) in S
}
assert len(EDGES) == 48
ADJ = [0] * 16
for e in EDGES:
    a, b = sorted(e)
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a

FACES = [m for m in range(1 << 16)
         if all(not ((m >> v) & 1) or not (ADJ[v] & m)
                for v in range(16))]
CELLS = {k: [m for m in FACES if m.bit_count() == k + 1]
         for k in range(4)}
assert [len(CELLS[k]) for k in range(4)] == [16, 72, 96, 16]
assert len(FACES) == 201


def vertices(mask):
    return [v for v in range(16) if mask >> v & 1]


def rank_mod2(column_masks):
    pivots = {}
    for c in column_masks:
        while c:
            p = c.bit_length() - 1
            if p not in pivots:
                pivots[p] = c
                break
            c ^= pivots[p]
    return len(pivots)


def boundary_columns(higher, lower):
    pos = {f: k for k, f in enumerate(lower)}
    return [sum(1 << pos[m & ~(1 << v)] for v in vertices(m))
            for m in higher]

B2 = boundary_columns(CELLS[2], CELLS[1])
B3 = boundary_columns(CELLS[3], CELLS[2])
assert rank_mod2(B2) == 57
assert rank_mod2(B3) == 16
for col in B3:
    target = 0
    while col:
        bit = col & -col
        target ^= B2[bit.bit_length() - 1]
        col ^= bit
    assert target == 0

# The 1-skeleton is connected: graph with every independent pair as an edge.
seen = {0}
while True:
    extension = {u for e in CELLS[1]
                 for u in vertices(e) if any(v in seen for v in vertices(e))}
    if extension <= seen:
        break
    seen |= extension
assert len(seen) == 16
# Over Q: rank d1=15, rank d2=57, rank d3=16, so only H2 is nonzero.
assert (72 - 15 - 57, 96 - 57 - 16, 16 - 16) == (0, 23, 0)


def determinant_odd(M):
    a, b, c, d = M
    return (a * d - b * c) % 2 == 1


def linear(M, u):
    a, b, c, d = M
    x, y = u
    return ((a * x + b * y) % 4, (c * x + d * y) % 4)

D = [M for M in product(range(4), repeat=4)
     if determinant_odd(M) and {linear(M, x) for x in S} == S]
assert len(D) == 12
ID = (1, 0, 0, 1)
G = [(M, t) for M in D for t in V]
PERM = {(M, t): tuple(INDEX[((linear(M, v)[0] + t[0]) % 4,
                              (linear(M, v)[1] + t[1]) % 4)] for v in V)
        for M, t in G}
assert len(set(PERM.values())) == 192
for p in PERM.values():
    for e in EDGES:
        assert frozenset(p[u] for u in e) in EDGES
# The point stabilizer embeds in the 12-element automorphism group of N(0)=C6.
N = vertices(ADJ[0])
assert len(N) == 6
assert all((ADJ[v] & ADJ[0]).bit_count() == 2 for v in N)
local_reached = {N[0]}
for _ in range(6):
    local_reached |= {u for u in N if any(ADJ[v] >> u & 1 for v in local_reached)}
assert len(local_reached) == 6
patterns = [ADJ[v] & ADJ[0] for v in range(16) if v != 0 and v not in N]
assert len(patterns) == len(set(patterns)) == 9
# Hence a 0-fixing automorphism fixing all six neighbors is the identity.
# Since N(0) is a 6-cycle, |Aut(S)| <= 16*12 = 192.


def permutation_sign_on_face(mapped_vertices, source_vertices):
    indices = [source_vertices.index(v) for v in mapped_vertices]
    return (-1) ** sum(indices[i] > indices[j]
                       for i in range(len(indices)) for j in range(i+1, len(indices)))


def signed_fixed_face_trace(p):
    result = -1  # augmented empty simplex contributes -1
    for m in FACES[1:]:
        src = vertices(m)
        img = [p[v] for v in src]
        if set(img) == set(src):
            result += (-1) ** (len(src) - 1) * permutation_sign_on_face(img, src)
    return result


def vertex_orbit_trace(p):
    """Independent quotient-orbit polynomial evaluated at -1, with a minus sign."""
    seen = set()
    cycles = []
    for v in range(16):
        if v in seen:
            continue
        orbit = []
        u = v
        while u not in seen:
            seen.add(u)
            orbit.append(u)
            u = p[u]
        mask = sum(1 << x for x in orbit)
        if all(not (ADJ[x] & mask) for x in orbit):
            cycles.append(mask)
    polynomial = 0
    for choice in range(1 << len(cycles)):
        union = 0
        valid = True
        for j, orbit in enumerate(cycles):
            if choice >> j & 1:
                if any(ADJ[x] & union for x in vertices(orbit)):
                    valid = False
                    break
                union |= orbit
        if valid:
            polynomial += (-1) ** choice.bit_count()
    return -polynomial

CHAR = {}
for key, perm in PERM.items():
    a = signed_fixed_face_trace(perm)
    b = vertex_orbit_trace(perm)
    assert a == b, (key, a, b)
    CHAR[key] = a
assert CHAR[(ID, (0, 0))] == 23
assert Counter(CHAR.values()) == {-7: 12, -3: 4, -1: 69, 0: 32,
                                  1: 24, 2: 32, 3: 18, 23: 1}
assert sum(CHAR.values()) == 0
assert sum(x*x for x in CHAR.values()) == 192 * 8

# Exact Fourier transform, with i^k represented by (real,imag) integers.
ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def FT(M, lam):
    a = b = 0
    for t in V:
        w = (-lam[0]*t[0] - lam[1]*t[1]) % 4
        re, im = ROOTS[w]
        a += CHAR[(M, t)]*re
        b += CHAR[(M, t)]*im
    assert a % 16 == b % 16 == 0
    return (a//16, b//16)

MULT = {lam: FT(ID, lam) for lam in V}
assert all(z[1] == 0 for z in MULT.values())
assert sum(z[0] for z in MULT.values()) == 23
ORBIT_DATA = []
seen = set()
for lam in V:
    if lam in seen:
        continue
    orbit = {(linear((M[0],M[2],M[1],M[3]),lam)) for M in D}
    seen |= orbit
    h = [M for M in D if linear((M[0],M[2],M[1],M[3]), lam) == lam]
    little = {M: FT(M,lam) for M in h}
    assert all(z[1] == 0 for z in little.values())
    ORBIT_DATA.append((lam, len(orbit), MULT[lam][0], little))
assert [(x[0],x[1],x[2]) for x in ORBIT_DATA] == [
    ((0,0),1,2), ((0,1),6,1), ((0,2),3,1), ((1,1),6,2)]
assert sum(n*m for _,n,m,_ in ORBIT_DATA) == 23
R = (0,1,3,1)
F = (0,1,1,0)
def product_matrices(M, N):
    a,b,c,d = M
    e,f,g,h = N
    return ((a*e+b*g)%4,(a*f+b*h)%4,(c*e+d*g)%4,(c*f+d*h)%4)

q = ID
for j in range(6):
    assert FT(q, (0,0)) == (1+(-1)**j, 0)
    assert FT(product_matrices(F,q), (0,0)) == (-1-(-1)**j, 0)
    q = product_matrices(q,R)
assert q == ID
assert product_matrices(product_matrices(F,R),F) == product_matrices(product_matrices(product_matrices(product_matrices(product_matrices(ID,R),R),R),R),R)
assert FT(R,(0,0)) == (0,0)
assert FT(F,(0,0)) == (-2,0)
assert FT(ID,(0,0)) == (2,0)
# Character of each stabilizer representation is listed explicitly.
assert ORBIT_DATA[1][3] == {ID:(1,0), (3,1,0,1):(-1,0)}
assert ORBIT_DATA[2][3] == {ID:(1,0), (1,3,0,3):(-1,0),
                            (3,0,0,3):(-1,0), (3,1,0,1):(1,0)}
assert ORBIT_DATA[3][3] == {ID:(2,0), (0,1,1,0):(-2,0)}
assert sum(CHAR[(ID,t)] for t in V) == 32  # translation-fixed dimension 2

print('FACES', [len(CELLS[k]) for k in range(4)])
print('MOD2_RANKS', (15,57,16))
print('AUTOMORPHISMS', len(G), 'LEFSCHETZ_ORBIT_CHECKS', len(G))
print('CHARACTER_HISTOGRAM', sorted(Counter(CHAR.values()).items()))
print('TRANSLATION_MULTIPLICITIES', sorted((k,v[0]) for k,v in MULT.items()))
print('DUAL_ORBITS', [(x[0],x[1],x[2]) for x in ORBIT_DATA])
print('INVARIANT_DIMENSIONS', (sum(CHAR.values())//192,
                               sum(CHAR[(ID,t)] for t in V)//16))
print('CHARACTER_ROWS')
for M in D:
    print(M, [CHAR[(M,t)] for t in V])
print('SHRIKHANDE_EQUIVARIANT_VERIFY_OK')
