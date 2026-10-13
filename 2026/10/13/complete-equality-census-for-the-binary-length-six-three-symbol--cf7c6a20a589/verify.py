#!/usr/bin/env python3
import itertools

N = 6
B = 3
WORDS = list(range(1 << N))
FULL_VERTICES = (1 << (1 << N)) - 1

def bit(x, i):
    return (x >> (i % N)) & 1

def bdist_direct(x, y):
    return sum(
        any(bit(x, i + j) != bit(y, i + j) for j in range(B))
        for i in range(N)
    )

def bdist_support(x, y):
    z = x ^ y
    bad = set()
    for j in range(N):
        if (z >> j) & 1:
            for t in range(B):
                bad.add((j - t) % N)
    return len(bad)

# Independent construction of the full distance matrix.
D1 = [[0] * (1 << N) for _ in WORDS]
D2 = [[0] * (1 << N) for _ in WORDS]
for x in WORDS:
    for y in WORDS:
        D1[x][y] = bdist_direct(x, y)
        D2[x][y] = bdist_support(x, y)
assert D1 == D2

adj = [0] * (1 << N)
for x in WORDS:
    for y in WORDS:
        if x != y and D1[x][y] >= 6:
            adj[x] |= 1 << y

# Complete Bron--Kerbosch enumeration of maximal cliques.
best = 0
maxima_bk = set()

def bronk(R, P, X):
    global best, maxima_bk
    if not P and not X:
        C = tuple(i for i in WORDS if (R >> i) & 1)
        if len(C) > best:
            best = len(C)
            maxima_bk = {C}
        elif len(C) == best:
            maxima_bk.add(C)
        return

    U = P | X
    if U:
        candidates = [u for u in WORDS if (U >> u) & 1]
        pivot = max(candidates, key=lambda u: (P & adj[u]).bit_count())
        Q = P & ~adj[pivot]
    else:
        Q = P

    while Q:
        vbit = Q & -Q
        v = vbit.bit_length() - 1
        bronk(R | vbit, P & adj[v], X & adj[v])
        P &= ~vbit
        X |= vbit
        Q &= ~vbit

bronk(0, FULL_VERTICES, 0)
assert best == 8
assert len(maxima_bk) == 776

# Independent fixed-size increasing-vertex clique census.
def k_cliques(k):
    out = set()
    def rec(prefix, cand, need):
        if need == 0:
            out.add(tuple(prefix))
            return
        if cand.bit_count() < need:
            return
        while cand:
            vbit = cand & -cand
            v = vbit.bit_length() - 1
            cand ^= vbit
            rec(prefix + [v], cand & adj[v], need - 1)
    rec([], FULL_VERTICES, k)
    return out

maxima_k = k_cliques(8)
assert maxima_k == maxima_bk
assert len(k_cliques(9)) == 0
maxima = maxima_bk

# Singleton bound check at these parameters:
# M <= 2^(n-d+b) = 2^3 = 8.
assert 2 ** (N - 6 + B) == 8

# Natural binary b-symbol isometry subgroup:
# all translations plus dihedral symmetries of the cyclic coordinates.
perms = []
for k in range(N):
    perms.append(tuple((i + k) % N for i in range(N)))
for k in range(N):
    perms.append(tuple((k - i) % N for i in range(N)))
perms = list(dict.fromkeys(perms))
assert len(perms) == 12

def perm_word(x, p):
    y = 0
    for i, j in enumerate(p):
        if (x >> i) & 1:
            y |= 1 << j
    return y

transforms = []
for p in perms:
    pm = [perm_word(x, p) for x in WORDS]
    for a in WORDS:
        transforms.append([pm[x] ^ a for x in WORDS])
assert len(transforms) == 768

def transform_code(C, T):
    return tuple(sorted(T[x] for x in C))

def is_affine(C):
    base = C[0]
    S = {x ^ base for x in C}
    return all((u ^ v) in S for u in S for v in S)

seen = set()
orbit_data = []
for C in sorted(maxima):
    if C in seen:
        continue
    orbit = {transform_code(C, T) for T in transforms}
    assert orbit <= maxima
    seen |= orbit
    rep = min(orbit)
    orbit_data.append((len(orbit), 768 // len(orbit), is_affine(rep), rep))
assert seen == maxima

orbit_data.sort()
expected = [
    (8, 96, True),
    (24, 32, True),
    (24, 32, True),
    (32, 24, True),
    (48, 16, True),
    (64, 12, False),
    (96, 8, False),
    (96, 8, True),
    (192, 4, False),
    (192, 4, False),
]
assert [(a,b,c) for a,b,c,_ in orbit_data] == expected

affine_total = sum(size for size, stab, affine, rep in orbit_data if affine)
assert affine_total == 232
assert len(maxima) - affine_total == 544

def fmt(x):
    return format(x, "06b")

print("DISTANCE_OK methods_agree=true ambient=64")
print("MAXIMUM=8 LABELED_MAXIMA=776")
print("AFFINE=232 NONLINEAR=544 ORBITS=10")
for i, (size, stab, affine, rep) in enumerate(orbit_data, 1):
    print(
        f"ORBIT{i} size={size} stabilizer={stab} affine={str(affine).lower()} "
        f"rep={','.join(fmt(x) for x in rep)}"
    )
print(
    "VERIFY_OK maximum=8 labeled_maxima=776 affine=232 nonlinear=544 "
    "orbits=10 orbit_sizes=8,24,24,32,48,64,96,96,192,192 "
    "stabilizers=96,32,32,24,16,12,8,8,4,4"
)
