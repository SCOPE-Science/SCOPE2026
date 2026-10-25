#!/usr/bin/env python3
"""Exact, standard-library certificate for the ternary three-cube translation module."""
from collections import Counter, deque
from itertools import product

V = list(product(range(3), repeat=3))
assert len(V) == 27
IX = {v: i for i, v in enumerate(V)}
FULL = (1 << 27) - 1

def dist(v, w):
    return sum(x != y for x, y in zip(v, w))

N = []
for i, x in enumerate(V):
    N.append(sum(1 << j for j, y in enumerate(V) if i != j and dist(x, y) <= 2))

# The increasing-vertex backtracking rule produces every nonempty clique once.
F = set()
def extend(sigma, candidates):
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        i = bit.bit_length() - 1
        tau = sigma | bit
        assert tau not in F
        F.add(tau)
        extend(tau, candidates & N[i])
extend(0, FULL)
bydim = [sorted(s for s in F if s.bit_count() == k) for k in range(1, 10)]
fvector = tuple(len(x) for x in bydim)
assert fvector == (27, 243, 945, 1728, 1620, 945, 351, 81, 9)
assert len(F) == 5949

# A complete acyclic discrete-Morse matching gives an integral homotopy proof.
U = set(F)
pairs = []
for i in range(27):
    b = 1 << i
    for s in sorted(U):
        if s & b:
            continue
        t = s | b
        if t in U:
            U.remove(s)
            U.remove(t)
            pairs.append((s, t))
critical = Counter(s.bit_count() - 1 for s in U)
assert len(pairs) == 2951
assert critical == {0: 1, 3: 46}, critical
pair_set = set(pairs)
indeg = {s: 0 for s in F}
out = {s: [] for s in F}
edge_count = 0
for upper in F:
    bits = upper
    while bits:
        bit = bits & -bits
        bits ^= bit
        lower = upper ^ bit
        if not lower:
            continue
        if (lower, upper) in pair_set:
            start, stop = lower, upper
        else:
            start, stop = upper, lower
        out[start].append(stop)
        indeg[stop] += 1
        edge_count += 1
q = deque(s for s in F if indeg[s] == 0)
visited = 0
while q:
    s = q.popleft()
    visited += 1
    for t in out[s]:
        indeg[t] -= 1
        if indeg[t] == 0:
            q.append(t)
assert (edge_count, visited) == (27189, 5949)

# Independent mod-two chain boundary ranks, for checking the Morse theorem's input.
def rank2(cols):
    pivots = {}
    for x in cols:
        while x:
            k = x.bit_length() - 1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return len(pivots)
ranks = []
for d in range(1, 9):
    ix = {face: j for j, face in enumerate(bydim[d - 1])}
    cols = []
    for face in bydim[d]:
        r = 0
        bits = face
        while bits:
            b = bits & -bits
            bits ^= b
            r |= 1 << ix[face ^ b]
        cols.append(r)
    ranks.append(rank2(cols))
assert ranks == [26, 217, 728, 954, 666, 279, 72, 9]
betti = [fvector[d] - (ranks[d-1] if d else 0) - (ranks[d] if d < 8 else 0) for d in range(9)]
assert betti == [1, 0, 0, 46, 0, 0, 0, 0, 0], betti

# Signed Lefschetz trace on all invariant simplices for all 27 translations.
def lex_bits(mask):
    while mask:
        b = mask & -mask
        mask ^= b
        yield b.bit_length() - 1

def perm_for(a):
    return [IX[tuple((v[j] + a[j]) % 3 for j in range(3))] for v in V]

def signed_trace(perm):
    L = 0
    for s in F:
        vertices = list(lex_bits(s))
        mapped = [perm[v] for v in vertices]
        if sum(1 << k for k in mapped) != s:
            continue
        inversions = sum(mapped[i] > mapped[j] for i in range(len(mapped))
                         for j in range(i + 1, len(mapped)))
        L += -1 if ((len(vertices) - 1 + inversions) & 1) else 1
    return L

traces = {}
for a in V:
    w = sum(c != 0 for c in a)
    L = signed_trace(perm_for(a))
    traces[a] = 1 - L
    assert traces[a] == (46, 4, -2, 1)[w], (a, traces[a])

# Independent fixed-face orbit-complex census for the three representative types.
quotients = {}
for a in ((1,0,0), (1,1,0), (1,1,1)):
    perm = perm_for(a)
    orbits = []
    unseen = set(range(27))
    while unseen:
        i = min(unseen)
        orbit = {i, perm[i], perm[perm[i]]}
        assert len(orbit) == 3
        unseen.difference_update(orbit)
        orbits.append(sum(1 << j for j in orbit))
    Qf = Counter()
    for selection in range(1, 1 << 9):
        merged = 0
        for j in range(9):
            if selection >> j & 1:
                merged |= orbits[j]
        if merged in F:
            Qf[selection.bit_count() - 1] += 1
    quotients[sum(x != 0 for x in a)] = [Qf[i] for i in range(3)]
assert quotients == {1:[9,18,6],2:[9,9,3],3:[0,0,0]}, quotients

# Character orthogonality, performed with exact integer coefficients.
mult = {}
for weight in range(4):
    polynomial = [1]
    for j in range(3):
        factor = [1, -1 if j < weight else 2]
        nxt = [0] * (len(polynomial) + 1)
        for i, c in enumerate(polynomial):
            for h, d in enumerate(factor):
                nxt[i+h] += c*d
        polynomial = nxt
    numerator = sum(polynomial[j] * (46,4,-2,1)[j] for j in range(4))
    assert numerator % 27 == 0
    mult[weight] = numerator // 27
assert mult == {0:2,1:2,2:2,3:1}, mult
assert sum(mult[w] * __import__('math').comb(3,w) * 2**w for w in range(4)) == 46
assert sum(traces.values()) // 27 == 2
print('F_VECTOR', fvector)
print('MORSE_PAIRS_CRITICAL_ACYCLIC',len(pairs),dict(critical),edge_count,visited)
print('MOD2_BOUNDARY_RANKS', tuple(ranks), 'BETTI', tuple(betti))
print('TRANSLATION_H3_TRACES_WEIGHT_0_TO_3', (46,4,-2,1))
print('FIXED_ORBIT_FACE_VECTORS', quotients)
print('FOURIER_MULTIPLICITIES_WEIGHT_0_TO_3',mult)
print('INVARIANT_DIMENSION',2)
print('VERIFY_OK_TERNARY_RIPS_TRANSLATION_CHARACTER')
