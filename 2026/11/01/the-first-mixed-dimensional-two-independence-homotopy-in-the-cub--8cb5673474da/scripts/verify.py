#!/usr/bin/env python3
"""Exact, standalone verification of a cubical two-independence homotopy calculation.

Requires only Python 3.10+ standard library. Vertex labels are binary integers;
a simplex is represented by its vertex-incidence bitmask.
"""
from collections import Counter, deque
from functools import lru_cache

ORDER4 = (0, 3, 4, 8, 10, 1, 15, 7, 11, 5, 9, 2, 6, 13, 12, 14)


def neighbors(d):
    n = 1 << d
    return [sum(1 << (v ^ (1 << i)) for i in range(d)) for v in range(n)]


def predicate_degree(s, adj):
    left = s
    while left:
        b = left & -left
        left ^= b
        v = b.bit_length() - 1
        if (adj[v] & s).bit_count() > 1:
            return False
    return True


def face_sets(d):
    adj = neighbors(d)
    n = len(adj)
    forbidden = set()
    for v in range(n):
        nbs = [u for u in range(n) if adj[v] & (1 << u)]
        for k, u in enumerate(nbs):
            for w in nbs[k+1:]:
                forbidden.add((1 << v) | (1 << u) | (1 << w))
    fbd = sorted(forbidden)
    faces_degree = set()
    faces_forbidden = set()
    for s in range(1, 1 << n):
        if predicate_degree(s, adj):
            faces_degree.add(s)
        if all((s & t) != t for t in fbd):
            faces_forbidden.add(s)
    assert faces_degree == faces_forbidden, 'Independent predicates disagree'
    return faces_degree, len(fbd)


def match(faces, order):
    unmatched = set(faces)
    pairs = []
    for v in order:
        bit = 1 << v
        for lower in sorted(tuple(unmatched)):
            upper = lower | bit
            if not (lower & bit) and upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    assert len(faces) == len(unmatched) + 2 * len(pairs)
    assert all((upper ^ lower).bit_count() == 1 and lower & upper == lower for lower, upper in pairs)
    return pairs, unmatched


def acyclicity(faces, pairs):
    matching = dict(pairs)
    outgoing = {face: [] for face in faces}
    indegree = {face: 0 for face in faces}
    edge_count = 0
    for upper in faces:
        t = upper
        while t:
            b = t & -t
            t ^= b
            lower = upper ^ b
            if lower == 0:
                continue
            if matching.get(lower) == upper:
                src, dst = lower, upper
            else:
                src, dst = upper, lower
            outgoing[src].append(dst)
            indegree[dst] += 1
            edge_count += 1
    queue = deque(face for face in faces if indegree[face] == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        for nxt in outgoing[face]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    assert visited == len(faces), 'Directed matching has a cycle'
    return edge_count


def signed_boundary(face):
    bits = []
    s = face
    while s:
        b = s & -s
        s ^= b
        bits.append(b)
    return [(face ^ b, -1 if i % 2 else 1) for i, b in enumerate(bits)]


def critical_boundary(critical_upper, pairs, critical):
    lower_to_upper = dict(pairs)
    upper_to_lower = {b: a for a, b in pairs}

    @lru_cache(maxsize=None)
    def projection(face):
        if face in critical:
            return {face: 1}
        if face in upper_to_lower:
            return {}
        upper = lower_to_upper[face]
        signs = signed_boundary(upper)
        pivot = next(c for f, c in signs if f == face)
        result = {}
        for f, c in signs:
            if f == face:
                continue
            for z, coeff in projection(f).items():
                result[z] = result.get(z, 0) - pivot * c * coeff
        return {z: val for z, val in result.items() if val}

    result = {}
    for face, sign in signed_boundary(critical_upper):
        for z, coeff in projection(face).items():
            result[z] = result.get(z, 0) + sign * coeff
    return {z: val for z, val in result.items() if val}


def gf2_ranks(faces):
    bydim = {}
    for face in faces:
        bydim.setdefault(face.bit_count() - 1, []).append(face)
    for layer in bydim.values():
        layer.sort()
    ranks = {}
    for dim in sorted(bydim):
        if dim == 0:
            continue
        rowpos = {f: i for i, f in enumerate(bydim[dim - 1])}
        pivots = {}
        for upper in bydim[dim]:
            column = 0
            for lower, _ in signed_boundary(upper):
                column ^= 1 << rowpos[lower]
            while column:
                k = column.bit_length() - 1
                if k not in pivots:
                    pivots[k] = column
                    break
                column ^= pivots[k]
        ranks[dim] = len(pivots)
    betti = {}
    for dim, layer in bydim.items():
        val = len(layer) - ranks.get(dim, 0) - ranks.get(dim + 1, 0)
        if dim == 0:
            val -= 1
        if val:
            betti[dim] = val
    return ranks, betti


def run(d, order, expected_fvector, expected_critical, expected_betti):
    faces, forbidden_count = face_sets(d)
    fv = tuple(Counter(s.bit_count() - 1 for s in faces)[i] for i in range(d + 5))
    while fv and fv[-1] == 0:
        fv = fv[:-1]
    assert fv == expected_fvector, (fv, expected_fvector)
    pairs, crit = match(faces, order)
    ck = {str(k): c for k, c in sorted(Counter(s.bit_count() - 1 for s in crit).items())}
    assert Counter(s.bit_count() - 1 for s in crit) == expected_critical
    incidence = acyclicity(faces, pairs)
    ranks, betti = gf2_ranks(faces)
    assert betti == expected_betti, betti
    facets = Counter(s.bit_count() - 1 for s in faces
                     if not any((s | (1 << v)) in faces for v in range(1 << d) if not (s & (1 << v))))
    print(f'Q{d} checked_subsets={1 << (1 << d)} forbidden_triples={forbidden_count}')
    print(f'Q{d} f_vector={fv} maximal_dimensions={dict(sorted(facets.items()))}')
    print(f'Q{d} matched_pairs={len(pairs)} critical_cells={ck}')
    print(f'Q{d} acyclic_hasse_incidence_count={incidence} visited={len(faces)}')
    print(f'Q{d} gf2_boundary_ranks={dict(sorted(ranks.items()))} reduced_betti={dict(sorted(betti.items()))}')
    if d == 4:
        fourth = [f for f in crit if f.bit_count() == 5]
        assert len(fourth) == 1
        assert fourth[0] == 0x4a30, hex(fourth[0])
        m = critical_boundary(fourth[0], pairs, crit)
        assert m == {}, m
        print(f'Q4 critical_4_cell=0x{fourth[0]:04x} integral_Morse_d4_zero=True')
    if d == 3:
        assert all(c.bit_count() - 1 in (0, 2) for c in crit)
    return faces


def main():
    run(1, tuple(range(2)), (2, 1), Counter({0: 1}), {})
    run(2, tuple(range(4)), (4, 6), Counter({0: 1, 1: 3}), {1: 3})
    run(3, tuple(range(8)), (8, 28, 32, 8), Counter({0: 1, 2: 3}), {2: 3})
    run(4, ORDER4, (16, 120, 464, 964, 960, 440, 80, 10),
        Counter({0: 1, 3: 16, 4: 1}), {3: 16, 4: 1})
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
