#!/usr/bin/env python3
"""Reproduce the integral Morse calculation of a graph perfect-matching complex.

The code uses only Python's standard library. Graph vertices are 0,...,17;
complex vertices are lexicographically ordered graph edges, 0,...,26.
"""
import collections
from functools import lru_cache

LCF = (5, 7, -7, 7, -7, -5) * 3
TOGGLE_ORDER = (25, 4, 11, 10, 26, 23, 7, 1, 15, 2, 14, 21, 24, 5,
                12, 3, 9, 6, 8, 17, 20, 13, 0, 18, 19, 16, 22)
EXPECTED_F = (27, 297, 1575, 3780, 4752, 3456, 1512, 378, 42)


def graph_edges():
    edge_set = set()
    for i, s in enumerate(LCF):
        edge_set.add(tuple(sorted((i, (i + 1) % 18))))
        edge_set.add(tuple(sorted((i, (i + s) % 18))))
    edges = tuple(sorted(edge_set))
    assert len(edges) == 27
    assert all(sum(i in edge for edge in edges) == 3 for i in range(18))
    return edges


def enumerations(edges):
    adj = [[] for _ in range(18)]
    for j, (a, b) in enumerate(edges):
        adj[a].append((b, j))
        adj[b].append((a, j))
    perfect = []
    def extend(unmatched, mask):
        if not unmatched:
            perfect.append(mask)
            return
        u = (unmatched & -unmatched).bit_length() - 1
        for v, j in adj[u]:
            if unmatched & (1 << v):
                extend(unmatched ^ (1 << u) ^ (1 << v), mask | (1 << j))
    extend((1 << 18) - 1, 0)
    assert len(perfect) == len(set(perfect)) == 42
    assert all(m.bit_count() == 9 for m in perfect)
    faces = {0}
    for m in perfect:
        sub = m
        while sub:
            faces.add(sub)
            sub = (sub - 1) & m
    f = tuple(sum(1 for x in faces if x.bit_count() == k) for k in range(1, 10))
    assert f == EXPECTED_F
    return perfect, faces


def toggles(faces):
    remaining = set(faces)
    remaining.remove(0)
    pivot = 1 << TOGGLE_ORDER[0]
    remaining.remove(pivot)  # reserve one critical vertex
    paired = {}
    for edge in TOGGLE_ORDER:
        bit = 1 << edge
        for x in tuple(remaining):
            y = x | bit
            if x & bit == 0 and y in remaining:
                remaining.remove(x)
                remaining.remove(y)
                paired[x] = y
    critical = remaining | {pivot}
    assert len(paired) == 7905
    assert len(critical) == 9
    assert collections.Counter(x.bit_count() - 1 for x in critical) == {0: 1, 2: 1, 3: 6, 4: 1}
    assert 2 * len(paired) + len(critical) == len(faces) - 1
    assert all(y in faces and x in faces and x & y == x and (x ^ y).bit_count() == 1
               for x, y in paired.items())
    return paired, critical


def lower_facets(mask):
    bits = mask
    while bits:
        bit = bits & -bits
        yield mask ^ bit
        bits ^= bit


def signed_incidence(upper, lower):
    deleted = upper ^ lower
    assert deleted and deleted & (deleted - 1) == 0 and lower & upper == lower
    return (-1) ** ((upper & (deleted - 1)).bit_count())


def verify_acyclic(faces, pairs):
    # Match edges point upward; all other covering relations point down.
    outgoing = collections.defaultdict(list)
    indegree = {x: 0 for x in faces if x}
    count = 0
    for upper in indegree:
        for lower in lower_facets(upper):
            if not lower:
                continue
            if pairs.get(lower) == upper:
                start, stop = lower, upper
            else:
                start, stop = upper, lower
            outgoing[start].append(stop)
            indegree[stop] += 1
            count += 1
    queue = collections.deque(x for x, val in indegree.items() if val == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in outgoing[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert visited == len(faces) - 1, (visited, len(faces) - 1)
    return count


def morse_boundary(crit, pairs, k):
    # The k-to-(k-1) differential: if a (k-1)-face u is paired upwards to v,
    # replace u using the integral relation d(v)=0 and unit incidence [v:u].
    low = {x for x in crit if x.bit_count() == k}
    lows_matched_up = {x: y for x, y in pairs.items() if x.bit_count() == k}
    lows_matched_down = {y for x, y in pairs.items() if y.bit_count() == k}
    seen = set()
    @lru_cache(None)
    def reduce_face(u):
        if u in seen:
            raise AssertionError('gradient recursion has a cycle')
        seen.add(u)
        if u in low:
            result = {u: 1}
        elif u in lows_matched_down:
            result = {}
        else:
            v = lows_matched_up[u]
            pivot = signed_incidence(v, u)
            coeffs = collections.defaultdict(int)
            for w in lower_facets(v):
                if w == u:
                    continue
                for basis, multiplicity in reduce_face(w).items():
                    coeffs[basis] -= pivot * signed_incidence(v, w) * multiplicity
            result = {key: value for key, value in coeffs.items() if value}
        seen.remove(u)
        return result
    rows = sorted(low)
    cols = sorted(x for x in crit if x.bit_count() == k + 1)
    matrix = []  # columns
    for sigma in cols:
        column = collections.defaultdict(int)
        for boundary_face in lower_facets(sigma):
            for basis, value in reduce_face(boundary_face).items():
                column[basis] += signed_incidence(sigma, boundary_face) * value
        matrix.append(tuple(column[row] for row in rows))
    return rows, cols, matrix


def matching_obstructions(edges, extendible):
    allmatch = {0}
    incident = [((1 << u) | (1 << v)) for u, v in edges]
    for j in range(len(edges)):
        prev = list(allmatch)
        allmatch.update(x | (1 << j) for x in prev
                        if all(not (incident[i] & incident[j])
                               for i in range(j) if x & (1 << i)))
    forbidden = allmatch - extendible
    minimal = [m for m in forbidden if all((m ^ (1 << i)) in extendible
                                          for i in range(len(edges)) if m & (1 << i))]
    return len(allmatch) - 1, len(forbidden), collections.Counter(x.bit_count() for x in minimal)


def mod2_betti(faces):
    graded = [[x for x in faces if x.bit_count() == k] for k in range(1, 10)]
    ranks = []
    for k in range(len(graded)):
        if k == 0:
            ranks.append(0)
            continue
        rowidx = {x: i for i, x in enumerate(graded[k - 1])}
        pivots = {}
        for sigma in graded[k]:
            bits = 0
            for sub in lower_facets(sigma):
                bits ^= 1 << rowidx[sub]
            while bits:
                p = bits.bit_length() - 1
                if p in pivots:
                    bits ^= pivots[p]
                else:
                    pivots[p] = bits
                    break
        ranks.append(len(pivots))
    betti = [len(graded[k]) - ranks[k] - (ranks[k + 1] if k + 1 < len(ranks) else 0)
             for k in range(len(graded))]
    betti[0] -= 1
    return ranks, betti


def main():
    edges = graph_edges()
    matching_list, faces = enumerations(edges)
    pairs, crit = toggles(faces)
    incidence_count = verify_acyclic(faces, pairs)
    crit2, crit3, b3 = morse_boundary(crit, pairs, 3)
    crit3b, crit4, b4 = morse_boundary(crit, pairs, 4)
    assert crit3 == crit3b and len(crit2) == 1 and len(crit4) == 1
    assert b3 == [(0,), (-1,), (-1,), (1,), (0,), (0,)], b3
    assert b4 == [(0, 0, 0, 0, 0, 0)], b4
    ranks, betti = mod2_betti(faces)
    assert betti == [0, 0, 0, 5, 1, 0, 0, 0, 0], (ranks, betti)
    total, forbidden, minimal = matching_obstructions(edges, faces)
    assert (total, forbidden, minimal) == (35367, 19548, {3: 144, 4: 351})
    print('VERIFY_OK')
    print('graph_vertices=18 graph_edges=27 perfect_matchings=42')
    print('faces_nonempty=15819 f_vector=' + repr(EXPECTED_F))
    print('matching_pairs=7905 critical=(one_0,one_2,six_3,one_4)')
    print('hasse_incidences=' + str(incidence_count) + ' full_acyclic_toposort=PASS')
    print('morse_d3_columns=' + repr(b3))
    print('morse_d4_columns=' + repr(b4))
    print('mod2_boundary_ranks=' + repr(ranks))
    print('mod2_reduced_betti=' + repr(betti))
    print('ordinary_matchings=' + str(total) + ' nonextendible=' + str(forbidden))
    print('minimal_nonextendible=' + repr(sorted(minimal.items())))
    print('H3_Z=Z^5 H4_Z=Z, all_other_reduced_H=0')


if __name__ == '__main__':
    main()
