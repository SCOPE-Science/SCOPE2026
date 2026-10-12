#!/usr/bin/env python3
import itertools
from collections import Counter

N = 5
WORDS = list(range(1 << N))
FULL = (1 << N) - 1

def bits(x):
    return tuple((x >> i) & 1 for i in range(N))

def asym_distance(x, y):
    bx, by = bits(x), bits(y)
    down = sum(a == 1 and b == 0 for a, b in zip(bx, by))
    up = sum(a == 0 and b == 1 for a, b in zip(bx, by))
    return max(down, up)

def zball1(x):
    out = {x}
    for i in range(N):
        if (x >> i) & 1:
            out.add(x & ~(1 << i))
    return frozenset(out)

# Build the compatibility graph independently from the asymmetric metric
# and from disjoint one-error Z-channel balls.
adj_metric = [0] * (1 << N)
adj_ball = [0] * (1 << N)
for x in WORDS:
    for y in WORDS:
        if x == y:
            continue
        if asym_distance(x, y) >= 2:
            adj_metric[x] |= 1 << y
        if zball1(x).isdisjoint(zball1(y)):
            adj_ball[x] |= 1 << y

assert adj_metric == adj_ball

# Exact Bron--Kerbosch enumeration of every maximal clique.
best = 0
maxima = set()

def bronk(R, P, X):
    global best, maxima
    if not P and not X:
        C = tuple(i for i in WORDS if (R >> i) & 1)
        size = len(C)
        if size > best:
            best = size
            maxima = {C}
        elif size == best:
            maxima.add(C)
        return

    union = P | X
    if union:
        candidates = [u for u in WORDS if (union >> u) & 1]
        pivot = max(candidates, key=lambda v: (P & adj_metric[v]).bit_count())
        Q = P & ~adj_metric[pivot]
    else:
        Q = P

    while Q:
        bit = Q & -Q
        v = bit.bit_length() - 1
        bronk(R | bit, P & adj_metric[v], X & adj_metric[v])
        P &= ~bit
        X |= bit
        Q &= ~bit

bronk(0, (1 << (1 << N)) - 1, 0)

assert best == 6
assert len(maxima) == 120
maxima = {tuple(sorted(C)) for C in maxima}

# Classify maxima under coordinate permutations and global bit complement.
perms = list(itertools.permutations(range(N)))

def perm_word(x, p):
    y = 0
    for i, j in enumerate(p):
        if (x >> i) & 1:
            y |= 1 << j
    return y

def transform(C, p, flip):
    return tuple(sorted(
        (FULL ^ perm_word(x, p)) if flip else perm_word(x, p)
        for x in C
    ))

seen = set()
orbits = []
for C in sorted(maxima):
    if C in seen:
        continue
    orbit = {transform(C, p, flip) for p in perms for flip in (0, 1)}
    assert orbit <= maxima
    seen |= orbit
    orbits.append(orbit)

assert seen == maxima
orbit_sizes = sorted(len(o) for o in orbits)
stabilizers = sorted(240 // len(o) for o in orbits)
assert orbit_sizes == [30, 30, 60]
assert stabilizers == [4, 8, 8]

def fmt(x):
    return format(x, "05b")

representatives = []
for orbit in sorted(orbits, key=lambda o: (len(o), min(o))):
    C = min(orbit)
    weight_profile = tuple(sorted(Counter(x.bit_count() for x in C).items()))
    distance_profile = tuple(sorted(
        Counter(asym_distance(x, y) for x, y in itertools.combinations(C, 2)).items()
    ))
    representatives.append(
        (len(orbit), 240 // len(orbit), C, weight_profile, distance_profile)
    )

print("GRAPH_OK vertices=32 metric_ball_adjacency_agree=true")
print("MAXIMUM", best, "LABELED_MAXIMA", len(maxima))
print("ORBITS", ",".join(map(str, orbit_sizes)),
      "STABILIZERS", ",".join(map(str, stabilizers)))
for k, (osz, stab, C, wp, dp) in enumerate(representatives, 1):
    print(
        "REP", k,
        "orbit", osz,
        "stabilizer", stab,
        "code", ",".join(fmt(x) for x in C),
        "weight_profile", wp,
        "distance_profile", dp,
    )
print("VERIFY_OK maximum=6 labeled_maxima=120 orbits=3 "
      "orbit_sizes=30,30,60 stabilizers=4,8,8")
