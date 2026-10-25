#!/usr/bin/env python3
"""Finite exhaustive checks for the triangular-graph three-cut dual theorem.
No external packages are needed. The uniform proof is in RESULT.md.
"""
from itertools import combinations
from collections import defaultdict, deque
from math import comb


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def data(n):
    edges = list(combinations(range(n), 2))
    ids = {e: i for i, e in enumerate(edges)}
    faces = set()
    for S in combinations(range(n), 4):
        verts = [ids[e] for e in combinations(S, 2)]
        for r in range(1, 7):
            for subset in combinations(verts, r):
                faces.add(sum(1 << j for j in subset))
    for v in range(n):
        verts = [ids[tuple(sorted((v, w)))] for w in range(n) if w != v]
        for r in range(1, len(verts) + 1):
            for subset in combinations(verts, r):
                faces.add(sum(1 << j for j in subset))
    return edges, ids, faces


def disjoint(e, f):
    return not (set(e) & set(f))


def hasse_acyclic(faces, pairs):
    # Matched incidences lower -> upper; all other incidences upper -> lower.
    matched = {higher: lower for lower, higher in pairs}
    successors = defaultdict(list)
    indeg = {f: 0 for f in faces}
    for higher in faces:
        for i in bits(higher):
            lower = higher ^ (1 << i)
            if lower not in faces:
                continue
            a, b = ((lower, higher) if matched.get(higher) == lower else (higher, lower))
            successors[a].append(b)
            indeg[b] += 1
    todo = deque(f for f in faces if indeg[f] == 0)
    processed = 0
    while todo:
        f = todo.popleft()
        processed += 1
        for g in successors[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                todo.append(g)
    return processed == len(faces)


def morse_matching(n, edges, ids, faces):
    full = set(faces)
    r0, U = set(), set()
    Bof = {}
    for F in full:
        B = tuple(edges[j] for j in bits(F) if 0 not in edges[j])
        Bof[F] = B
        if any(disjoint(x, y) for x, y in combinations(B, 2)):
            U.add(F)
        else:
            r0.add(F)
    assert full == r0 | U and not (r0 & U)
    pairs = []
    residual = set(r0)
    # R_0 cone fibers indexed by B. A single spoke is a cone apex in each.
    by_B = defaultdict(list)
    for F in residual:
        by_B[Bof[F]].append(F)
    for B, fiber in by_B.items():
        if not B:
            pivot = ids[(0, 1)]
        else:
            common = set(B[0])
            for edge in B[1:]:
                common.intersection_update(edge)
            pivot = ids[(0, min(common))] if common else ids[(0, min(set().union(*map(set, B))))]
        bit = 1 << pivot
        fset = set(fiber)
        for F in fiber:
            if F & bit:
                continue
            upper = F | bit
            assert upper in fset, ('missing cone apex', B, F)
            pairs.append((F, upper))
            residual.discard(F)
            residual.discard(upper)
    assert residual == {1 << ids[(0, 1)]}
    # All faces in U have a uniquely determined four-vertex support.
    by_S = defaultdict(set)
    for F in U:
        support = frozenset(v for j in bits(F) for v in edges[j])
        assert len(support) == 4 and 0 not in support
        by_S[support].add(F)
    assert len(by_S) == comb(n - 1, 4)
    for S, fset in by_S.items():
        assert len(fset) == 37
        a, b, c, d = sorted(S)
        for v in [b, c, d]:
            pivot = 1 << ids[(a, v)]
            newpairs = [(F, F | pivot) for F in sorted(fset)
                        if not F & pivot and (F | pivot) in fset]
            for lo, hi in newpairs:
                assert lo in fset and hi in fset
                pairs.append((lo, hi))
                fset.remove(lo)
                fset.remove(hi)
        wanted = sum(1 << ids[e] for e in [(a, b), (b, c), (b, d), (c, d)])
        assert fset == {wanted}, (S, fset)
        residual.add(wanted)
    assert len(residual) == 1 + comb(n - 1, 4)
    assert sum(F.bit_count() == 1 for F in residual) == 1
    assert all(F.bit_count() in (1, 4) for F in residual)
    assert len(pairs) * 2 + len(residual) == len(full)
    assert hasse_acyclic(full, pairs)
    return len(full), len(r0), len(U), len(pairs), len(residual)


def direct_dual_check(n, edges, faces):
    # Check every nonempty face against the original graph-connected-triple condition
    # whenever enumeration is affordable, and every triple of the full edge set.
    for x, y, z in combinations(range(len(edges)), 3):
        connected = (int(not disjoint(edges[x], edges[y])) +
                     int(not disjoint(edges[x], edges[z])) +
                     int(not disjoint(edges[y], edges[z])) >= 2)
        actual = ((1 << x) | (1 << y) | (1 << z)) in faces
        assert connected == actual
    for F in faces:
        selected = [edges[i] for i in bits(F)]
        assert all(sum(not disjoint(x, y) for x, y in combinations(T, 2)) >= 2
                   for T in combinations(selected, 3))


def test():
    for n in range(5, 9):
        edges, ids, faces = data(n)
        direct_dual_check(n, edges, faces)
        nf, nr0, nu, npairs, ncrit = morse_matching(n, edges, ids, faces)
        assert nu == 37 * comb(n-1, 4)
        print(f'n={n}: dual_faces={nf}, contractible_core_faces={nr0}, '
              f'four_support_faces={nu}, pairs={npairs}, '
              f'critical_0=1, critical_3={ncrit-1}, acyclic=YES')
    print('PASS: exhaustive local classification and finite gradient certificates')

if __name__ == '__main__':
    test()
