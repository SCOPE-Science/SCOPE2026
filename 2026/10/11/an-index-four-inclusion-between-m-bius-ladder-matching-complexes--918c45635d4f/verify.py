"""Reproducible integral-chain verification for the ten-vertex Möbius ladder.

Run: python3 verify.py. Uses only Python's standard library.
All orientations order graph edges lexicographically.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 10
EDGES = sorted({tuple(sorted((i, (i + 1) % N))) for i in range(N)} |
               {(i, i + 5) for i in range(5)})
assert len(EDGES) == 15


def simplices():
    faces = [0]
    for j, (u, v) in enumerate(EDGES):
        incompatible = sum(1 << i for i, (a, b) in enumerate(EDGES)
                           if i != j and (u in (a, b) or v in (a, b)))
        faces += [mask | (1 << j) for mask in faces
                  if mask & incompatible == 0]
    assert len(faces) == len(set(faces))
    return faces


def perfect_subcomplex(faces):
    perfects = [x for x in faces if x.bit_count() == 5]
    sub = {x for x in faces if any(x & y == x for y in perfects)}
    assert len(perfects) == 13
    return sub


def incidence_boundary(face):
    indices = [j for j in range(15) if face & (1 << j)]
    return [(face ^ (1 << j), (-1) ** k) for k, j in enumerate(indices)]


def toggle_matching(face_list):
    free = set(face_list)
    pairs = []
    # Pair every possible surviving face with its extension by the next edge.
    for i in range(15):
        bit = 1 << i
        for face in face_list:
            if face in free and not face & bit and face | bit in free:
                free.remove(face)
                free.remove(face | bit)
                pairs.append((face, face | bit))
    assert len(pairs) * 2 + len(free) == len(face_list)
    assert sum(a == 0 for a, b in pairs) == 1
    return pairs, free


def acyclicity_check(faces, pairs):
    """Direct exhaustive Hasse-orientation test, not an assumed theorem."""
    V = set(faces)
    up = {a: b for a, b in pairs}
    indeg = {x: 0 for x in V}
    adj = {x: [] for x in V}
    arc_count = 0
    for larger in V:
        for smaller, coeff in incidence_boundary(larger):
            assert smaller in V
            if up.get(smaller) == larger:
                source, target = smaller, larger
            else:
                source, target = larger, smaller
            adj[source].append(target)
            indeg[target] += 1
            arc_count += 1
    Q = deque(x for x in V if indeg[x] == 0)
    visited = 0
    while Q:
        x = Q.popleft()
        visited += 1
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                Q.append(y)
    assert visited == len(V), (visited, len(V))
    return arc_count


def morse_matrix(pairs, critical):
    critical_2 = sorted(x for x in critical if x.bit_count() == 3)
    critical_3 = sorted(x for x in critical if x.bit_count() == 4)
    upper = {b for a, b in pairs}
    lower = {a: b for a, b in pairs}

    @lru_cache(None)
    def project(face):
        if face in critical:
            return {face: 1}
        if face in upper:
            return {}
        partner = lower[face]
        coeff_face = next(c for z, c in incidence_boundary(partner)
                          if z == face)
        ans = {}
        for other, c in incidence_boundary(partner):
            if other == face:
                continue
            for target, val in project(other).items():
                ans[target] = ans.get(target, 0) - coeff_face * c * val
        return {k: v for k, v in ans.items() if v}

    ans = []
    for bigger in critical_3:
        image = {}
        for smaller, sign in incidence_boundary(bigger):
            for target, coeff in project(smaller).items():
                image[target] = image.get(target, 0) + sign * coeff
        ans.append([image.get(z, 0) for z in critical_2])
    return critical_2, critical_3, ans


def bareiss(A):
    """Fraction-free determinant, all calculations over exact integers."""
    n = len(A)
    assert all(len(r) == n for r in A)
    A = [list(row) for row in A]
    if not n:
        return 1
    sign, denominator = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if A[i][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        p = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * p - A[i][k] * A[k][j]
                assert numerator % denominator == 0
                A[i][j] = numerator // denominator
        for i in range(k + 1, n):
            A[i][k] = 0
        denominator = p
    return sign * A[-1][-1]


def relative_components(faces, perfect):
    bad = set(faces) - perfect
    tri = sorted(x for x in bad if x.bit_count() == 3)
    tet = sorted(x for x in bad if x.bit_count() == 4)
    assert len(bad) == 60 and len(tri) == len(tet) == 30
    assert not (bad - set(tri) - set(tet))
    row_idx = {mask: i for i, mask in enumerate(tri)}
    incidence = [[0] * 30 for _ in range(30)]
    adj = {('r', i): set() for i in range(30)}
    adj.update({('c', j): set() for j in range(30)})
    for j, larger in enumerate(tet):
        for smaller, sign in incidence_boundary(larger):
            if smaller in row_idx:
                i = row_idx[smaller]
                incidence[i][j] = sign
                adj[('r', i)].add(('c', j))
                adj[('c', j)].add(('r', i))
    unseen = set(adj)
    blocks = []
    while unseen:
        component = set()
        stack = [min(unseen)]
        while stack:
            x = stack.pop()
            if x in component:
                continue
            component.add(x)
            unseen.remove(x)
            stack.extend(adj[x] - component)
        rows = sorted(i for t, i in component if t == 'r')
        cols = sorted(i for t, i in component if t == 'c')
        assert len(rows) == len(cols)
        block = [[incidence[i][j] for j in cols] for i in rows]
        blocks.append((len(rows), bareiss(block),
                       Counter(len(adj[x]) for x in component), block))
    assert Counter((size, abs(det)) for size, det, _, _ in blocks) == {
        (1, 1): 10, (10, 2): 2
    }
    for size, det, degrees, matrix in blocks:
        if size == 10:
            assert degrees == {2: 20}
            # An arbitrary deleted row and column of a signed cycle is a
            # signed path, which has a unimodular full-rank minor.
            assert abs(bareiss([r[1:] for r in matrix[1:]])) == 1
        else:
            assert degrees == {1: 2}
    return Counter((size, det) for size, det, _, _ in blocks)


def main():
    F = simplices()
    K = set(F)
    P = perfect_subcomplex(F)
    assert len(K) == 344 and len(P) == 284
    assert Counter(x.bit_count()-1 for x in K if x) == {
        0: 15, 1: 75, 2: 145, 3: 95, 4: 13}
    assert Counter(x.bit_count()-1 for x in P if x) == {
        0: 15, 1: 75, 2: 115, 3: 65, 4: 13}
    Kpairs, Kcrit = toggle_matching(F)
    Ppairs, Pcrit = toggle_matching(sorted(P))
    assert len(Kpairs) == 167 and len(Ppairs) == 141
    assert Counter(x.bit_count()-1 for x in Kcrit) == {2: 6, 3: 4}
    assert Counter(x.bit_count()-1 for x in Pcrit) == {2: 2}
    k_arcs = acyclicity_check(K, Kpairs)
    p_arcs = acyclicity_check(P, Ppairs)
    k2, k3, M = morse_matrix(Kpairs, Kcrit)
    assert M == [[1,-1,0,-1,0,0],
                 [0,0,-1,0,1,0],
                 [1,0,-1,0,0,0],
                 [0,-1,0,0,0,1]]
    assert bareiss([row[:4] for row in M]) == 1
    blocks = relative_components(F, P)
    print('VERIFY_OK graph_edges=15 complex_faces=344 perfect_faces=284 '
          'perfect_matchings=13')
    print('MORSE ordinary critical=(six 2-cells, four 3-cells), '
          'perfect critical=(two 2-cells); arcs=', k_arcs, p_arcs)
    print('MORSE_BOUNDARY', M, 'unit_4x4_minor=1')
    print('RELATIVE_BOUNDARY components', sorted(blocks.items()))
    print('CONCLUSION both complexes wedge of two 2-spheres; '
          'H_2(ordinary,perfect)=(Z/2)^2; H_3(relative)=0; '
          'inclusion H_2 has Smith form (2,2).')

if __name__ == '__main__':
    main()
