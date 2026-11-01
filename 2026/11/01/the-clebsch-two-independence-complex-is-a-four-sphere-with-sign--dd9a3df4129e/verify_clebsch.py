#!/usr/bin/env python3
"""Reproduce the folded-five-cube two-independence homotopy and character calculation.
Python 3 standard library only; deterministic exact integer arithmetic.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations

N = 16
EDGE_LIST = [(i, j) for i in range(N) for j in range(i) if (i ^ j).bit_count() in (1, 4)]
ADJ = [0] * N
for i, j in EDGE_LIST:
    ADJ[i] |= 1 << j
    ADJ[j] |= 1 << i
assert len(EDGE_LIST) == 40 and all(row.bit_count() == 5 for row in ADJ)

# Two independent membership implementations: induced-degree and forbidden wedges.
WEDGES = set()
for center in range(N):
    neigh = [j for j in range(N) if (ADJ[center] >> j) & 1]
    for a, b in combinations(neigh, 2):
        WEDGES.add((1 << center) | (1 << a) | (1 << b))
assert len(WEDGES) == 160

def valid_degrees(s):
    return all((ADJ[v] & s).bit_count() <= 1 for v in range(N) if (s >> v) & 1)

def valid_wedges(s):
    return all((s & w) != w for w in WEDGES)

FACES = [s for s in range(1, 1 << N) if valid_degrees(s)]
assert FACES == [s for s in range(1, 1 << N) if valid_wedges(s)]
FACE_SET = set(FACES)
FVECTOR = tuple(sum(s.bit_count() == k + 1 for s in FACES) for k in range(8))
assert FVECTOR == (16, 120, 400, 660, 576, 280, 80, 10)
assert len(FACES) == 2142

# Fixed vertex order determines one reproducible sequential element matching.
UNMATCHED = FACE_SET.copy()
MATCH = {}
for vertex in range(N):
    bit = 1 << vertex
    for lower in sorted((s for s in UNMATCHED if not s & bit), key=lambda s: (s.bit_count(), s)):
        upper = lower | bit
        if lower in UNMATCHED and upper in UNMATCHED:
            MATCH[lower] = upper
            UNMATCHED.remove(lower)
            UNMATCHED.remove(upper)
assert len(MATCH) == 1065 and len(UNMATCHED) == 12
CRIT = {k: sorted(s for s in UNMATCHED if s.bit_count() == k + 1) for k in range(8)}
assert tuple(len(CRIT[k]) for k in range(8)) == (1, 0, 0, 5, 6, 0, 0, 0)

def boundary_of(s):
    i = 0
    t = s
    while t:
        bit = t & -t
        yield (s ^ bit, -1 if i & 1 else 1)
        t ^= bit
        i += 1

# Reverse the matched covering arrows, orient all others downward.
children = defaultdict(list)
indeg = {s: 0 for s in FACES}
incidences = 0
for higher in FACES:
    for lower, sign in boundary_of(higher):
        if lower == 0:
            continue
        a, b = (lower, higher) if MATCH.get(lower) == higher else (higher, lower)
        children[a].append(b)
        indeg[b] += 1
        incidences += 1
Q = deque(x for x in FACES if indeg[x] == 0)
visited = 0
while Q:
    x = Q.popleft()
    visited += 1
    for y in children[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            Q.append(y)
assert visited == len(FACES) and incidences == 9280

# Exact signed Morse differential D_4: Z^6 -> Z^5.
TARGET = {s: i for i, s in enumerate(CRIT[3])}
LOWERS = set(MATCH)
UPPERS = set(MATCH.values())
@lru_cache(None)
def projection(f):
    if f in TARGET:
        return {TARGET[f]: 1}
    if f in UPPERS:
        return {}
    assert f in LOWERS, (f, 'unclassified third simplex')
    upper = MATCH[f]
    incidence = next(c for g, c in boundary_of(upper) if g == f)
    result = Counter()
    for g, c in boundary_of(upper):
        if g == f:
            continue
        for j, v in projection(g).items():
            result[j] -= incidence * c * v
    return {j: v for j, v in result.items() if v}
M = [[0] * len(CRIT[4]) for _ in CRIT[3]]
for col, upper in enumerate(CRIT[4]):
    for low, c in boundary_of(upper):
        for row, v in projection(low).items():
            M[row][col] += c * v

def det5(A):
    result = 0
    for p in permutations(range(5)):
        sign = -1 if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) & 1 else 1
        product = 1
        for i in range(5):
            product *= A[i][p[i]]
        result += sign * product
    return result

D = det5([row[:5] for row in M])
assert abs(D) == 1

# Second independent, uncollapsed simplicial chain computation over GF(2).
bydim = {k: sorted(s for s in FACES if s.bit_count() == k + 1) for k in range(8)}
def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            i = col.bit_length() - 1
            if i in pivots:
                col ^= pivots[i]
            else:
                pivots[i] = col
                break
    return len(pivots)
ranks = {-1: 0, 0: 1, 8: 0}
for q in range(1, 8):
    indices = {s: i for i, s in enumerate(bydim[q - 1])}
    columns = [sum(1 << indices[f] for f, _ in boundary_of(s)) for s in bydim[q]]
    ranks[q] = rank_mod2(columns)
betti = {q: len(bydim[q]) - ranks[q] - ranks[q + 1] for q in range(8)}
assert betti == {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0}

# The 16 even-weight words of length five; edges differ in four coordinates.
ALL5 = (1 << 5) - 1
five_generators = [ALL5 ^ (1 << j) for j in range(5)]
Y = [0] * N
for a in range(N):
    for i in range(4):
        if (a >> i) & 1:
            Y[a] ^= five_generators[i]
FROM_Y = {y: i for i, y in enumerate(Y)}
assert len(FROM_Y) == N
assert all((Y[a] ^ Y[b]).bit_count() == 4 for a, b in EDGE_LIST)

def perm_word(w, p):
    return sum(1 << p[i] for i in range(5) if (w >> i) & 1)

def induced_perm(p, t):
    return tuple(FROM_Y[perm_word(y, p) ^ t] for y in Y)

def orientation_trace(g):
    traces = [0] * 8
    for f in FACES:
        vertices = [i for i in range(N) if (f >> i) & 1]
        permuted = [g[i] for i in vertices]
        if set(vertices) != set(permuted):
            continue
        sign = -1 if (sum(permuted[i] > permuted[j]
                          for i in range(len(permuted)) for j in range(i + 1, len(permuted))) & 1) else 1
        traces[len(vertices) - 1] += sign
    return sum((-1 if q & 1 else 1) * traces[q] for q in range(8)) - 1

seen = set()
traces = Counter()
for p in permutations(range(5)):
    permutation_sign = -1 if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) & 1 else 1
    for t in Y:
        g = induced_perm(p, t)
        assert g not in seen
        seen.add(g)
        assert all((g[a] ^ g[b]).bit_count() in (1, 4) for a, b in EDGE_LIST)
        ch = orientation_trace(g)
        assert ch == permutation_sign, (p, t, ch, permutation_sign)
        traces[ch] += 1
assert len(seen) == 1920 and traces == {1: 960, -1: 960}
# The full group assertion is self-contained: the point stabilizer acts faithfully
# on five neighbours, because each of the ten other vertices is uniquely
# determined by its two neighbours in the origin's neighbour set.
N0 = [j for j in range(N) if ADJ[0] & (1 << j)]
second = [j for j in range(N) if j != 0 and j not in N0]
signatures = {tuple(v for v in N0 if ADJ[j] & (1 << v)) for j in second}
assert len(N0) == 5 and len(second) == 10 and len(signatures) == 10
assert all(len(sig) == 2 for sig in signatures)

def chain_traces(g):
    result = [0] * 8
    for f in FACES:
        v = [i for i in range(N) if (f >> i) & 1]
        w = [g[i] for i in v]
        if set(w) != set(v):
            continue
        inv = sum(w[i] > w[j] for i in range(len(w)) for j in range(i + 1, len(w)))
        result[len(v) - 1] += (-1 if inv & 1 else 1)
    return result
translation_trace_vector = chain_traces(induced_perm(tuple(range(5)), five_generators[0]))
transposition_trace_vector = chain_traces(induced_perm((1, 0, 2, 3, 4), 0))

print('graph: vertices=16 edges=40 automorphisms=1920')
print('wedge triples:', len(WEDGES))
print('face vector:', FVECTOR, 'nonempty=', len(FACES))
print('matching pairs:', len(MATCH), 'critical dimension counts:', tuple(len(CRIT[k]) for k in range(8)))
print('matched Hasse DAG: incidences=', incidences, 'visited=', visited)
print('critical 3-face masks:', CRIT[3])
print('critical 4-face masks:', CRIT[4])
print('Morse D4:')
for row in M:print(row)
print('unimodular first-five-column minor determinant:', D)
print('original simplicial F2 ranks d_0..d_7:', [ranks[k] for k in range(8)])
print('original reduced F2 Betti 0..7:', [betti[k] for k in range(8)])
print('signed simplex trace q=0..7 translation:', translation_trace_vector)
print('signed simplex trace q=0..7 coordinate transposition:', transposition_trace_vector)
print('automorphism orientation traces:', dict(sorted(traces.items())))
print('ALL_CHECKS_PASS')
