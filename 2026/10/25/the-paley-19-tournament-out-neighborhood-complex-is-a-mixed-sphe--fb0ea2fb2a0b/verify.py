#!/usr/bin/env python3
"""Exact finite certificate for the Paley-19 out-neighborhood complex.

Python 3 standard library only. Builds all faces (including the empty face),
checks an acyclic face-poset matching, and computes the integral Morse boundary.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import json

P = 19
QR = frozenset((x * x) % P for x in range(1, P))
assert QR == {1, 4, 5, 6, 7, 9, 11, 16, 17}
OUT = [sum(1 << j for j in range(P) if (j-i) % P in QR) for i in range(P)]
assert all(a.bit_count() == 9 for a in OUT)
assert all((OUT[i] & OUT[j]).bit_count() == 4 for i in range(P) for j in range(i+1, P))
assert all(bool(OUT[i] & (1 << j)) != bool(OUT[j] & (1 << i))
           for i in range(P) for j in range(i+1, P))

FACES = {0}
for facet in OUT:
    sub = facet
    while sub:
        FACES.add(sub)
        sub = (sub-1) & facet
FV = tuple(Counter(s.bit_count() for s in FACES)[j] for j in range(1, 10))
assert FV == (19, 171, 969, 2223, 2394, 1596, 684, 171, 19)
assert len(FACES) == 8247
assert len(set(OUT)) == 19


def make_matching(order):
    remaining = FACES.copy()
    pairs = {}
    for v in order:
        bit = 1 << v
        candidates = [s for s in remaining if not s & bit and s | bit in remaining]
        for lower in candidates:
            upper = lower | bit
            assert lower in remaining and upper in remaining
            remaining.remove(lower)
            remaining.remove(upper)
            pairs[lower] = upper
    return remaining, pairs


CRIT, PAIR = make_matching(range(P))
assert len(PAIR) == 4081
assert Counter(s.bit_count()-1 for s in CRIT) == {2:4, 3:81}


def assert_acyclic(pairs):
    """Reverse every matched covering relation and topologically sort."""
    edges = defaultdict(list)
    indeg = defaultdict(int)
    total = 0
    for big in FACES:
        x = big
        while x:
            bit = x & -x
            x -= bit
            small = big ^ bit
            if pairs.get(small) == big:
                a, b = small, big
            else:
                a, b = big, small
            edges[a].append(b)
            indeg[b] += 1
            total += 1
    roots = deque(x for x in FACES if indeg[x] == 0)
    processed = 0
    while roots:
        u = roots.popleft()
        processed += 1
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                roots.append(v)
    assert processed == len(FACES), (processed, len(FACES))
    assert total == 40033
    return total

COVER = assert_acyclic(PAIR)


def facets_with_sign(cell):
    """Oriented boundary of increasing ordered vertices of this simplex."""
    terms = []
    x, index = cell, 0
    while x:
        bit = x & -x
        x -= bit
        terms.append((cell ^ bit, -1 if index & 1 else 1))
        index += 1
    return terms


def morse_boundary(critical, pairs):
    """Algebraic Morse projection via signed gradient-path substitutions."""
    upper = set(pairs.values())
    low_cells = sorted(x for x in critical if x.bit_count() == 3)
    high_cells = sorted(x for x in critical if x.bit_count() == 4)

    @lru_cache(None)
    def project(s):
        if s in critical:
            return {s: 1}
        if s in upper:
            return {}
        t = pairs[s]
        bd = dict(facets_with_sign(t))
        pivot = bd.pop(s)
        acc = defaultdict(int)
        for a, sg in bd.items():
            for crit, value in project(a).items():
                acc[crit] -= pivot * sg * value
        return {key:value for key,value in acc.items() if value}

    mat = [[0 for _ in high_cells] for _ in low_cells]
    row = {cell:i for i,cell in enumerate(low_cells)}
    for j,cell in enumerate(high_cells):
        for facet,sgn in facets_with_sign(cell):
            for crit,coefficient in project(facet).items():
                if crit in row:
                    mat[row[crit]][j] += sgn * coefficient
    assert project.cache_info().currsize <= len(FACES)
    return low_cells, high_cells, mat

LOWS, HIGHS, M = morse_boundary(CRIT, PAIR)
assert len(M) == 4 and all(len(row) == 81 for row in M)
# Exact integral rank bound, verified independently on all 81 columns.
assert all(M[0][j] - 2*M[1][j] - M[2][j] + M[3][j] == 0
           for j in range(81))
# A displayed 3-by-3 unimodular minor proves rank at least 3 and
# a primitive image (torsion-free cokernel).
R = (0,1,2)
C = (0,1,4)
SUB = [[M[i][j] for j in C] for i in R]
assert SUB == [[0,1,0],[0,1,1],[-1,0,-2]]
det = (SUB[0][0]*(SUB[1][1]*SUB[2][2]-SUB[1][2]*SUB[2][1])
       - SUB[0][1]*(SUB[1][0]*SUB[2][2]-SUB[1][2]*SUB[2][0])
       + SUB[0][2]*(SUB[1][0]*SUB[2][1]-SUB[1][1]*SUB[2][0]))
assert abs(det) == 1
# Ranks: C_3=Z^81, C_2=Z^4, boundary rank=3.
# The augmented Morse vector has no degrees <=1, giving simple connectivity.
assert sum((-1)**(j-1) * FV[j-1] for j in range(1,10)) == -76
assert 1 + 4 - 81 == -76

# A second, different acyclic matching gives an independent cell-count check.
REV, REVPAIR = make_matching(reversed(range(P)))
assert Counter(s.bit_count()-1 for s in REV) == {2:6,3:83}
assert_acyclic(REVPAIR)
# Independent boundary reduction for reverse priority, with exact rational rank.
_, REVERSE_HIGH, RM = morse_boundary(REV, REVPAIR)
from fractions import Fraction
RR = [[Fraction(v) for v in row] for row in RM]
rrank = 0
for col in range(len(REVERSE_HIGH)):
    pivotrow = next((i for i in range(rrank, len(RR)) if RR[i][col]), None)
    if pivotrow is None:
        continue
    RR[rrank], RR[pivotrow] = RR[pivotrow], RR[rrank]
    pivot = RR[rrank][col]
    RR[rrank] = [x / pivot for x in RR[rrank]]
    for i in range(rrank + 1, len(RR)):
        factor = RR[i][col]
        if factor:
            RR[i] = [RR[i][j] - factor * RR[rrank][j]
                     for j in range(len(REVERSE_HIGH))]
    rrank += 1
assert rrank == 5
assert len(RM) - rrank == 1 and len(REVERSE_HIGH) - rrank == 78

print(json.dumps({"status":"VERIFY_OK", "prime":19,
                  "quadratic_residues":sorted(QR), "face_vector":FV,
                  "face_count_with_empty":len(FACES),
                  "cover_relations":COVER, "matched_pairs":len(PAIR),
                  "critical_cells":{"dimension_2":4,"dimension_3":81},
                  "morse_boundary_shape":[4,81],"boundary_rank":3,
                  "unimodular_minor_rows":R,"unimodular_minor_columns":C,
                  "unimodular_minor_det":det,
                  "left_relation":[1,-2,-1,1],
                  "reduced_homology":{"degree_2":1,"degree_3":78},
                  "reverse_critical_cells":{"dimension_2":6,"dimension_3":83},
                  "reverse_morse_boundary_rank": rrank},
                 sort_keys=True))
