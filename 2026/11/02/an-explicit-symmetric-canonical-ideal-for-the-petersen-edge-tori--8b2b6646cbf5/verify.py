"""Exact finite checks for the Petersen edge-ring canonical-module formula.

Standalone Python 3; standard library only. Vertices are two-subsets of 0,...,4
in lexicographic order. All calculations use integer tuples.
"""
from collections import Counter
from itertools import combinations
from math import comb

V = list(combinations(range(5), 2))
E = [(a, b) for a in range(10) for b in range(a + 1, 10)
     if set(V[a]).isdisjoint(V[b])]
assert len(V) == 10 and len(E) == 15
NEIGH = {v: {w for a, b in E for w in (a, b) if v in (a, b) and w != v}
         for v in range(10)}


def components(nodes, graph):
    rem = set(nodes)
    ans = []
    while rem:
        origin = min(rem)
        seen = {origin}
        queue = [origin]
        rem.remove(origin)
        while queue:
            a = queue.pop()
            for b in sorted(graph[a] & rem):
                seen.add(b)
                rem.remove(b)
                queue.append(b)
        ans.append(seen)
    return ans


def contains_odd_cycle(nodes):
    nodes = set(nodes)
    color = {}
    for start in sorted(nodes):
        if start in color:
            continue
        color[start] = 0
        queue = [start]
        while queue:
            a = queue.pop()
            for b in NEIGH[a] & nodes:
                if b not in color:
                    color[b] = 1 - color[a]
                    queue.append(b)
                elif color[b] == color[a]:
                    return True
    return False


def independent(T):
    return all(not (a in T and b in T) for a, b in E)


def fundamental(T):
    T = set(T)
    if not T or not independent(T):
        return False
    N = set().union(*(NEIGH[t] for t in T))
    graph = {a: set() for a in T | N}
    for a in T:
        for b in NEIGH[a]:
            graph[a].add(b)
            graph[b].add(a)
    if len(components(T | N, graph)) != 1:
        return False
    rem = set(range(10)) - (T | N)
    return all(contains_odd_cycle(C) for C in components(rem, NEIGH))


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for i in range(total + 1):
        for rest in compositions(total - i, length - 1):
            yield (i,) + rest


for a in range(10):
    assert all(contains_odd_cycle(C)
               for C in components(set(range(10)) - {a}, NEIGH))
Ts = [tuple(T) for size in range(1, 11)
      for T in combinations(range(10), size) if fundamental(T)]
assert Counter(map(len, Ts)) == {3: 10, 4: 5}, Counter(map(len, Ts))
assert all(set(T) | set().union(*(NEIGH[i] for i in T)) == set(range(10))
           for T in Ts)
print('FACETS_OK: 10 coordinate and 15 fundamental-set facets (10 triples, 5 quadruples)')

# Normality: Petersen has the odd-cycle condition since two disjoint odd
# cycles must each occupy exactly five vertices; the ten-vertex connected
# graph has a bridge between their vertex sets. Girth is exactly 5.
assert len(components(set(range(10)), NEIGH)) == 1
assert all(len(NEIGH[i] & NEIGH[j]) == (0 if j in NEIGH[i] else 1)
           for i in range(10) for j in range(i+1, 10))
# No three- or four-cycles. Disjoint odd cycles, if they exist, must be
# two length-five cycles partitioning the connected ten-vertex graph.
print('NORMALITY_OK: connected girth-five graph satisfies odd-cycle condition')
# Facet support: for T of size 3 or 4 and x=1+b, degree(x)=5+r,
# primitive normal value equals 5-|T|+r-sum_{i in T}b_i.

def interior_values(b, r):
    return [5 - len(T) + r - sum(b[i] for i in T) for T in Ts]


def is_minimal_interior(b, r):
    vals = interior_values(b, r)
    if min(vals) < 1:
        return False, False
    removable_edge = any(
        b[a] >= 1 and b[c] >= 1 and
        all(val >= 2 or (a in T) or (c in T) for T, val in zip(Ts, vals))
        for a, c in E
    )
    return True, not removable_edge

# Dimension is ten; for a normal standard graded ten-dimensional domain,
# the graded canonical module has regularity ten. Consequently, no minimal
# canonical generator has degree > 10. This finite test is therefore complete.
expected = {5: 1, 6: 0, 7: 10, 8: 0, 9: 0, 10: 0}
star_vectors = {tuple(1 if i == c or i in NEIGH[c] else 0
                      for i in range(10)) for c in range(10)}
assert len(star_vectors) == 10
for d in range(5, 11):
    r = d - 5
    interior_count = 0
    minimum = []
    for b in compositions(2*r, 10):
        interior, minimal = is_minimal_interior(b, r)
        interior_count += int(interior)
        if minimal:
            minimum.append(b)
    assert len(minimum) == expected[d], (d, len(minimum))
    if d == 5:
        assert minimum == [(0,) * 10]
    if d == 7:
        assert set(minimum) == star_vectors
    print(f'CANONICAL_DEGREE_{d}_OK: interior={interior_count}, minimal={len(minimum)}')

# Hilbert-function count from edge multisets through degree 5, independently
# recovered from exponent vectors in the degree-k semigroup.
H = [1]
current = {(0,) * 10}
for d in range(1, 6):
    current = {
        tuple(x[i] + int(i == a or i == c) for i in range(10))
        for x in current for a, c in E
    }
    H.append(len(current))
hstar = [sum((-1)**j * comb(10, j) * H[i-j] for j in range(i+1))
         for i in range(6)]
assert H == [1, 15, 120, 670, 2895, 10303]
assert hstar == [1, 5, 15, 25, 5, 1]
print('HILBERT_OK:', H)
print('H_STAR_OK:', hstar)
print('CANONICAL_GENERATORS_OK: one monomial in degree 5; ten star monomials in degree 7')
print('VERIFY_OK')
