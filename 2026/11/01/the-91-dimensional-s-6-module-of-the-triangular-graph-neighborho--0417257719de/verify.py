#!/usr/bin/env python3
"""Exact rational cellular homology and symmetry of a triangular-graph neighborhood complex."""
import collections
import itertools
import math
from fractions import Fraction
from functools import lru_cache

N = 6
EDGES = list(itertools.combinations(range(N), 2))
ADJ = [tuple(j for j, f in enumerate(EDGES) if j != i and len(set(e) & set(f)) == 1) for i, e in enumerate(EDGES)]
FACES = collections.defaultdict(set)
for neighbors in ADJ:
    for k in range(1, len(neighbors) + 1):
        FACES[k - 1].update(itertools.combinations(neighbors, k))
FACES = {d: sorted(S) for d, S in FACES.items()}
assert len(EDGES) == 15 and all(len(t) == 8 for t in ADJ)
assert tuple(map(lambda d: len(FACES[d]), range(8))) == (15, 105, 420, 945, 840, 420, 120, 15)


def exact_rank(d):
    if d < 1:
        return 0
    idx = {s: i for i, s in enumerate(FACES[d - 1])}
    pivots = {}
    for s in FACES[d]:
        col = {idx[s[:j] + s[j + 1:]]: Fraction((-1) ** j) for j in range(d + 1)}
        while col:
            r = max(col)
            if r not in pivots:
                pivots[r] = col
                break
            z = col[r] / pivots[r][r]
            for i, a in pivots[r].items():
                t = col.get(i, 0) - z * a
                if t:
                    col[i] = t
                else:
                    col.pop(i, None)
    return len(pivots)

RANKS = {d: exact_rank(d) for d in range(1, 8)}
assert tuple(RANKS.values()) == (14, 91, 329, 525, 315, 105, 15)
BETTI = {d: len(FACES[d]) - RANKS.get(d, 0) - RANKS.get(d + 1, 0) for d in range(8)}
BETTI[0] -= 1  # reduced homology
assert BETTI == {0: 0, 1: 0, 2: 0, 3: 91, 4: 0, 5: 0, 6: 0, 7: 0}

# Verify chain-complex identities independently of rank elimination.
for d in range(2, 8):
    for s in FACES[d]:
        bd2 = collections.defaultdict(int)
        for i in range(d + 1):
            t = s[:i] + s[i + 1:]
            for j in range(d):
                u = t[:j] + t[j + 1:]
                bd2[u] += (-1) ** (i + j)
        assert all(v == 0 for v in bd2.values())


def partitions(n, hi=None):
    if n == 0:
        yield ()
        return
    for z in range(min(n, hi if hi is not None else n), 0, -1):
        for tail in partitions(n - z, z):
            yield (z,) + tail


def representative(mu):
    pi = []
    for size in mu:
        first = len(pi)
        pi.extend(list(range(first + 1, first + size)) + [first])
    return tuple(pi)


def zfactor(mu):
    return math.prod(j ** mu.count(j) * math.factorial(mu.count(j)) for j in set(mu))


def trace_h3(mu):
    pi = representative(mu)
    edge_map = [EDGES.index(tuple(sorted((pi[a], pi[b])))) for a, b in EDGES]
    alternating_chain_trace = 0
    for d, fs in FACES.items():
        for s in fs:
            image = [edge_map[x] for x in s]
            if set(image) != set(s):
                continue
            parity = sum(image[i] > image[j] for i in range(len(image)) for j in range(i + 1, len(image))) % 2
            alternating_chain_trace += (-1) ** (d + parity)
    #  H_0 is the trivial representation, and all other homology is H_3.
    return 1 - alternating_chain_trace

CLASSES = list(partitions(6))
TRACES = [trace_h3(mu) for mu in CLASSES]
assert TRACES == [1, 1, -3, -3, 1, -1, 1, 7, 7, -13, 91]

# Jacobi--Trudi character formula, using permutation characters on ordered
# blocks with row sizes determined by the Jacobi--Trudi determinant.
def character(lam, mu):
    ell = len(lam)
    @lru_cache(None)
    def count_assignments(capacities, remaining):
        if not capacities:
            return int(remaining == 0)
        if capacities[0] < 0:
            return 0
        ans, sub = 0, remaining
        while True:
            if sum(mu[i] for i in range(len(mu)) if (sub >> i) & 1) == capacities[0]:
                ans += count_assignments(capacities[1:], remaining ^ sub)
            if sub == 0:
                break
            sub = (sub - 1) & remaining
        return ans
    out = 0
    for pi in itertools.permutations(range(ell)):
        cap = tuple(lam[i] - i + pi[i] for i in range(ell))
        if min(cap) < 0:
            continue
        sign = (-1) ** sum(pi[i] > pi[j] for i in range(ell) for j in range(i + 1, ell))
        out += sign * count_assignments(cap, (1 << len(mu)) - 1)
    return out

DECOMP = {}
for lam in CLASSES:
    numerator = sum((math.factorial(6) // zfactor(mu)) * trace * character(lam, mu)
                    for mu, trace in zip(CLASSES, TRACES))
    assert numerator % math.factorial(6) == 0
    mult = numerator // math.factorial(6)
    assert mult >= 0
    if mult:
        DECOMP[lam] = mult
expected = {
    (4, 2): 1, (3, 3): 1, (3, 2, 1): 2, (3, 1, 1, 1): 1,
    (2, 2, 2): 2, (2, 2, 1, 1): 1, (2, 1, 1, 1, 1): 3,
    (1, 1, 1, 1, 1, 1): 1,
}
# Direct orthogonality and reconstruction in the character ring.
for lam in CLASSES:
    for rho in CLASSES:
        inner = sum((math.factorial(6) // zfactor(mu)) * character(lam, mu) * character(rho, mu)
                    for mu in CLASSES)
        assert inner == (math.factorial(6) if lam == rho else 0)
for mu, trace in zip(CLASSES, TRACES):
    assert sum(mult * character(lam, mu) for lam, mult in DECOMP.items()) == trace
assert DECOMP == expected
assert sum(m * character(lam, (1,) * 6) for lam, m in DECOMP.items()) == 91
assert DECOMP.get((6,), 0) == 0
assert DECOMP.get((1,) * 6, 0) == 1

# Identify the natural cut-complex alternative definition exhaustively.
cut_facets = set()
for seven in itertools.combinations(range(15), 7):
    chosen = set(seven)
    seen = {seven[0]}
    frontier = [seven[0]]
    while frontier:
        e = frontier.pop()
        for f in chosen - seen:
            if len(set(EDGES[e]) & set(EDGES[f])) == 1:
                seen.add(f)
                frontier.append(f)
    if len(seen) < 7:
        cut_facets.add(frozenset(set(range(15)) - chosen))
assert cut_facets == set(frozenset(n) for n in ADJ)
print('VERIFY_OK')
print('face_vector', [len(FACES[d]) for d in range(8)])
print('boundary_ranks_exact_Q', [RANKS[d] for d in range(1, 8)])
print('reduced_Q_homology', BETTI)
print('S6_classes_and_degree3_traces', list(zip(CLASSES, TRACES)))
print('Specht_multiplicities', DECOMP)
print('full_S6_invariants', DECOMP.get((6,), 0))
print('alternating_A6_invariants', DECOMP.get((6,), 0) + DECOMP.get((1,) * 6, 0))
print('seven_cut_facets', len(cut_facets))
