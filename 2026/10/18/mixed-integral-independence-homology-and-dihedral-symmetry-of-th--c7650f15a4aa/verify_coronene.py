#!/usr/bin/env python3
"""Exact finite computations for the coronene independence-complex homology.

Requires only Python 3 standard library. Run: python3 verify_coronene.py
All topological claims involving a finite simplicial complex are checked over its
entire face set; the output describes what was checked, not an external audit.
"""
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations
import struct

CENTERS = [(0, 0), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
OFFSETS = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]


def graph():
    edges, vertices = set(), set()
    for q, r in CENTERS:
        x, y = 3 * q, q + 2 * r
        ring = [(x + a, y + b) for a, b in OFFSETS]
        vertices.update(ring)
        for i in range(6):
            edges.add(tuple(sorted((ring[i], ring[(i + 1) % 6]))))
    vertices = sorted(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    edges = sorted((min(index[a], index[b]), max(index[a], index[b])) for a, b in edges)
    adjacency = [0] * len(vertices)
    for a, b in edges:
        adjacency[a] |= 1 << b
        adjacency[b] |= 1 << a
    assert len(vertices) == 24 and len(edges) == 30
    assert sorted(a.bit_count() for a in adjacency) == [2] * 12 + [3] * 12
    assert len(edges) - len(vertices) + 1 == 7
    return vertices, edges, adjacency


def all_independent_faces(adjacency):
    n = len(adjacency)
    faces = []
    def rec(mask, available):
        if mask:
            faces.append(mask)
        while available:
            bit = available & -available
            available ^= bit
            rec(mask | bit, available & ~adjacency[bit.bit_length() - 1])
    rec(0, (1 << n) - 1)
    assert len(faces) == 62506 and len(set(faces)) == len(faces)
    return faces


def exact_morse(faces):
    # At each vertex, simultaneously reverse all still available pairs
    # S < S union {v}. The subsequent explicit DAG check proves acyclicity.
    alive = set(faces)
    pair_lower_upper = {}
    for i in range(24):
        bit = 1 << i
        proposed = [(mask, mask | bit) for mask in sorted(alive)
                    if not mask & bit and mask | bit in alive]
        for lo, hi in proposed:
            assert lo in alive and hi in alive and lo not in pair_lower_upper
            pair_lower_upper[lo] = hi
        for lo, hi in proposed:
            alive.remove(lo)
            alive.remove(hi)
    critical = sorted(alive)
    assert len(pair_lower_upper) == 31251
    assert Counter(x.bit_count() - 1 for x in critical) == {0: 1, 5: 1, 7: 2}
    assert 2 * len(pair_lower_upper) + len(critical) == len(faces)
    return pair_lower_upper, critical


def verify_dag(faces, matching):
    # Full, untruncated Hasse graph of all nonempty faces, with paired
    # incidence arcs reversed. A topological ordering is a finite certificate
    # that there is no closed gradient path.
    index = {face: j for j, face in enumerate(sorted(faces))}
    faces = sorted(faces)
    outgoing = [[] for _ in faces]
    indegree = [0] * len(faces)
    edges = 0
    for hi in faces:
        hi_ix = index[hi]
        rem = hi
        while rem:
            bit = rem & -rem
            rem ^= bit
            lo = hi ^ bit
            if not lo:  # augmented empty face not part of ordinary complex
                continue
            lo_ix = index[lo]
            if matching.get(lo) == hi:
                source, target = lo_ix, hi_ix
            else:
                source, target = hi_ix, lo_ix
            outgoing[source].append(target)
            indegree[target] += 1
            edges += 1
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    orderhash = sha256()
    processed = 0
    while queue:
        i = queue.popleft()
        processed += 1
        orderhash.update(struct.pack('<I', faces[i]))
        for j in outgoing[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    assert processed == len(faces), (processed, len(faces))
    assert all(d == 0 for d in indegree)
    return edges, orderhash.hexdigest()


def symmetries(vertices, edges):
    index = {v: i for i, v in enumerate(vertices)}
    all_edges = set(edges)
    def rotate(v):
        x, y = v
        assert (x - 3 * y) % 2 == (x + y) % 2 == 0
        return ((x - 3 * y) // 2, (x + y) // 2)
    def reflect(v):
        return v[0], -v[1]
    ans = []
    for a in range(6):
        for b in (0, 1):
            p = []
            for x in vertices:
                if b:
                    x = reflect(x)
                for _ in range(a):
                    x = rotate(x)
                p.append(index[x])
            assert len(set(p)) == 24
            assert {tuple(sorted((p[u], p[v]))) for u, v in edges} == all_edges
            ans.append((a, b, p))
    return ans


def reduced_lefschetz(faces, perm):
    # The empty face contributes -1 to reduced Lefschetz.
    result = -1
    for mask in faces:
        ids = [i for i in range(24) if mask >> i & 1]
        tgt = [perm[i] for i in ids]
        if sum(1 << j for j in tgt) != mask:
            continue
        inversions = sum(tgt[i] > tgt[j]
                         for i in range(len(tgt)) for j in range(i + 1, len(tgt)))
        result += (-1) ** (len(ids) - 1 + inversions)
    return result


def all_dihedral_subgroups():
    elements = [(a, b) for a in range(6) for b in (0, 1)]
    def mul(x, y):
        a, b = x
        c, d = y
        return ((a + (1 if b == 0 else -1) * c) % 6, (b + d) % 2)
    def generated(gens):
        group = {(0, 0)}
        changed = True
        while changed:
            new = set(group)
            for g in group:
                for h in gens:
                    new.add(mul(g, h))
                    new.add(mul(h, g))
            changed = new != group
            group = new
        return frozenset(group)
    subgroups = {generated(())}
    for x in elements:
        subgroups.add(generated((x,)))
        for y in elements:
            subgroups.add(generated((x, y)))
    assert len(subgroups) == 16
    return sorted(subgroups, key=lambda H: (len(H), sorted(H)))


def quotient_ranks(H):
    # Averaging rational characters equals the dimension of invariant homology.
    chi5 = sum((-1)**a for a, b in H)
    chi7 = sum(0 if b else (2 if a % 3 == 0 else -1) for a, b in H)
    assert chi5 % len(H) == chi7 % len(H) == 0
    rank5, rank7 = chi5 // len(H), chi7 // len(H)
    image = {(a % 3, b) for a, b in H}
    predicted7 = 2 if len(image) == 1 else (1 if len(image) == 2 else 0)
    assert rank5 == int(all(a % 2 == 0 for a, b in H))
    assert rank7 == predicted7
    return rank5, rank7


def main():
    vertices, edges, adj = graph()
    faces = all_independent_faces(adj)
    fvector = [sum(m.bit_count() == d + 1 for m in faces) for d in range(12)]
    assert fvector == [24, 246, 1412, 5001, 11358, 16663,
                       15540, 8853, 2876, 489, 42, 2]
    matching, critical = exact_morse(faces)
    covers, topo_hash = verify_dag(faces, matching)
    expected = {
        (0, 0): -3, (1, 0): 2, (2, 0): 0,
        (3, 0): -1, (4, 0): 0, (5, 0): 2,
        (0, 1): -1, (1, 1): 1, (2, 1): -1,
        (3, 1): 1, (4, 1): -1, (5, 1): 1,
    }
    got = {}
    for a, b, perm in symmetries(vertices, edges):
        got[(a, b)] = reduced_lefschetz(faces, perm)
    assert got == expected, got
    # Homology: critical cells only in dimensions 0,5,7, so all
    # possible positive-dimensional Morse differentials are zero.
    # The 1-dimensional character of r must be -1: else the 2-dimensional
    # trace of r would be -3, impossible for a finite-order operator.
    # Consequently r on H_7 has trace -1 and eigenvalues omega, omega^2.
    # Reflection t exchanges their eigenspaces, forcing trace 0.
    for a in range(6):
        assert got[(a,0)] == -((-1)**a + (2 if a%3 == 0 else -1))
        assert got[(a,1)] == -((-1)**a)
    print('graph: 24 vertices, 30 edges, 7 bounded hexagonal faces, D6 symmetries: 12')
    print('nonempty simplices:', len(faces), 'face_vector:', fvector)
    print('Morse pairs:', len(matching), 'critical_dimensions:',
          [m.bit_count()-1 for m in critical])
    print('critical_bitmasks:', critical)
    print('oriented_cover_relations:', covers, 'acyclic: YES')
    print('topological_order_sha256:', topo_hash)
    print('reduced_lefschetz_rotation_r^a:', [got[(a,0)] for a in range(6)])
    print('reduced_lefschetz_reflection_r^a_t:', [got[(a,1)] for a in range(6)])
    print('homology: reduced H_5=Z, reduced H_7=Z^2, all others zero')
    print('character_H5_r^a:', [(-1)**a for a in range(6)])
    print('character_H5_r^a_t:', [(-1)**a for a in range(6)])
    print('character_H7_r^a:', [2 if a%3 == 0 else -1 for a in range(6)])
    print('character_H7_r^a_t:', [0]*6)
    groups = all_dihedral_subgroups()
    ranks = Counter(quotient_ranks(H) for H in groups)
    print('all_subgroup_quotients:', len(groups), 'rank_pairs_H5_H7:', sorted(ranks.items()))
    print('VERIFICATION OK')


if __name__ == '__main__':
    main()
