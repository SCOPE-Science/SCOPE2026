#!/usr/bin/env python3
"""Exact finite verification of an induced-forest complex and its symmetry.

Uses only the Python standard library. Graph vertices 0,...,6 are Fano
points, 7,...,13 are the lines (listed in lexicographic order).
"""
from collections import Counter, deque
from itertools import product

POINT_LINES = tuple(sorted(tuple(sorted((x + t) % 7 for x in (0, 1, 3))) for t in range(7)))
N = 14
EDGES = tuple((p, 7 + j) for j, L in enumerate(POINT_LINES) for p in L)
NEIGHBORS = [0] * N
for u, v in EDGES:
    NEIGHBORS[u] |= 1 << v
    NEIGHBORS[v] |= 1 << u


def forest_union_find(mask):
    parent = list(range(N))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in EDGES:
        if mask & (1 << u) and mask & (1 << v):
            a, b = root(u), root(v)
            if a == b:
                return False
            parent[a] = b
    return True


def forest_euler_components(mask):
    seen, count = 0, 0
    for v in range(N):
        bit = 1 << v
        if not mask & bit or seen & bit:
            continue
        count += 1
        seen |= bit
        stack = [v]
        while stack:
            x = stack.pop()
            available = NEIGHBORS[x] & mask & ~seen
            while available:
                b = available & -available
                available ^= b
                w = b.bit_length() - 1
                seen |= b
                stack.append(w)
    edge_count = sum(bool(mask & (1 << a) and mask & (1 << b)) for a, b in EDGES)
    return edge_count == mask.bit_count() - count


def signature(face, permutation):
    """Sign of a permutation restricted to an invariant simplex."""
    vs = tuple(i for i in range(N) if face & (1 << i))
    mapped = tuple(permutation[i] for i in vs)
    assert tuple(sorted(mapped)) == vs
    inv = sum(x > y for j, x in enumerate(mapped) for y in mapped[j+1:])
    return -1 if inv & 1 else 1


def induced_action(mask, permutation):
    result = 0
    while mask:
        b = mask & -mask
        mask -= b
        result |= 1 << permutation[b.bit_length() - 1]
    return result


def all_fano_symmetries():
    """Enumerate GL_3(F_2) by images of an ordered basis."""
    labels = (1, 2, 4, 3, 6, 7, 5)
    label_to_point = {u: i for i, u in enumerate(labels)}
    line_to_index = {frozenset(L): j for j, L in enumerate(POINT_LINES)}
    for a, b, c in product(range(1, 8), repeat=3):
        if b == a or c in (a, b, a ^ b):
            continue
        def linear(x):
            return (a if x & 1 else 0) ^ (b if x & 2 else 0) ^ (c if x & 4 else 0)
        p = tuple(label_to_point[linear(x)] for x in labels)
        q = tuple(7 + line_to_index[frozenset(p[v] for v in L)] for L in POINT_LINES)
        yield p + q


def main():
    assert len(POINT_LINES) == 7 and len(set(POINT_LINES)) == 7
    assert len(EDGES) == 21
    assert all(sum(u in L for L in POINT_LINES) == 3 for u in range(7))
    assert all(sum({i, j}.issubset(L) for L in POINT_LINES) == 1
               for i in range(7) for j in range(i + 1, 7))

    faces = set()
    for mask in range(1 << N):
        a = forest_union_find(mask)
        b = forest_euler_components(mask)
        assert a == b, (mask, a, b)
        if a:
            faces.add(mask)
    assert len(faces) == 12792 and 0 in faces
    fv = Counter(x.bit_count() - 1 for x in faces)
    assert tuple(fv.get(j, 0) for j in range(-1, 10)) == (
        1, 14, 91, 364, 1001, 2002, 2975, 3208, 2254, 812, 70)
    print('VERTICES', N, 'EDGES', len(EDGES), 'FACES_WITH_EMPTY', len(faces))
    print('FVECTOR_MINUS_ONE_TO_NINE', tuple(fv.get(j, 0) for j in range(-1, 10)))

    # A fully specified deterministic matching: repeatedly choose the smallest
    # vertex maximizing eligible toggles in the currently unmatched faces.
    unmatched = set(faces)
    pairs = []
    pivot_log = []
    for _ in range(N):
        choices = []
        for vertex in range(N):
            b = 1 << vertex
            p = tuple((f, f | b) for f in sorted(unmatched)
                      if not (f & b) and f | b in unmatched)
            choices.append((len(p), -vertex, p))
        num, neg_vertex, best = max(choices, key=lambda x: x[:2])
        if num == 0:
            break
        pivot_log.append((-neg_vertex, num))
        pairs.extend(best)
        for lo, hi in best:
            assert lo in unmatched and hi in unmatched and (hi ^ lo).bit_count() == 1
            unmatched.remove(lo)
            unmatched.remove(hi)
    assert len(pairs) == 6392
    assert len(unmatched) == 8 and {f.bit_count() for f in unmatched} == {9}
    assert any(lo == 0 for lo, _ in pairs)
    assert len({x for pair in pairs for x in pair}) == 2 * len(pairs)
    print('PIVOTS_AND_MATCH_COUNTS', pivot_log)
    print('MATCHED_PAIRS', len(pairs), 'CRITICAL_8_CELLS', len(unmatched))

    # Prove there is no closed gradient path by topological sorting of the
    # *entire* oriented augmented face Hasse diagram, not a sample.
    matching = {hi: lo for lo, hi in pairs}
    indegree = {f: 0 for f in faces}
    arcs = {f: [] for f in faces}
    incidence_count = 0
    for hi in faces:
        bits = hi
        while bits:
            b = bits & -bits
            bits ^= b
            lo = hi ^ b
            assert lo in faces
            if matching.get(hi) == lo:
                source, target = lo, hi
            else:
                source, target = hi, lo
            arcs[source].append(target)
            indegree[target] += 1
            incidence_count += 1
    q = deque(f for f in faces if indegree[f] == 0)
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in arcs[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    assert visited == len(faces)
    assert incidence_count == 81648
    print('DIRECTED_HASSE_INCIDENCES', incidence_count, 'TOPOLOGICAL_SORT', visited)

    # For any automorphism g, the signed face permutation on augmented
    # simplicial chains computes the alternating trace, so it equals
    # trace(g | reduced H_8), all other reduced homology being zero.
    symmetries = tuple(all_fano_symmetries())
    assert len(symmetries) == len(set(symmetries)) == 168
    edge_set = {frozenset(e) for e in EDGES}
    all_character_values = []
    for permutation in symmetries:
        assert tuple(sorted(permutation)) == tuple(range(N))
        assert {frozenset((permutation[u], permutation[v])) for u, v in EDGES} == edge_set
        trace = -1  # empty simplex in degree -1
        for f in faces:
            if not f:
                continue
            if induced_action(f, permutation) == f:
                trace += (-1 if f.bit_count() % 2 == 0 else 1) * signature(f, permutation)
        # The Fano building is exactly the incidence graph. Its H_1 character
        # follows from C_1 -> C_0 -> H_0 for a connected graph. Bipartition-
        # preserving symmetries cannot reverse an individual oriented edge.
        fixed_vertices = sum(permutation[i] == i for i in range(N))
        fixed_edges = sum(permutation[u] == u and permutation[v] == v for u, v in EDGES)
        building_trace = fixed_edges - fixed_vertices + 1
        assert trace == building_trace
        all_character_values.append(trace)
    counts = Counter(all_character_values)
    assert counts == Counter({8: 1, 1: 48, -1: 56, 0: 63})
    assert sum(x * x for x in all_character_values) == 168
    assert sum(all_character_values) == 0
    print('GL3_F2_ORDER', len(symmetries))
    print('CHARACTER_VALUE_MULTIPLICITIES', sorted(counts.items()))
    print('CHARACTER_SQUARED_NORM_NUMERATOR', sum(x*x for x in all_character_values))
    print('BUILDING_H1_CHARACTER_IDENTICAL', True)
    print('GL3_F2_RATIONAL_H8_IRREDUCIBLE', True)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
