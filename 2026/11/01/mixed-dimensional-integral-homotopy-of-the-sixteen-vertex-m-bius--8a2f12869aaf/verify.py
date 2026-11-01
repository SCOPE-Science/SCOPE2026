#!/usr/bin/env python3
"""Exact certificate for the ordinary matching complex of the 16-vertex Möbius ladder.
Python 3 standard library only; no external datasets or imported project modules.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 16
EDGE_ORDER = [11, 5, 22, 13, 20, 7, 17, 12, 3, 4, 1, 0,
              18, 19, 8, 6, 2, 10, 16, 21, 14, 23, 9, 15]
EXPECTED_CRITICAL = [2048, 49985, 69968, 594064, 2105680,
                     2114324, 2146625, 2367620, 2376204,
                     2425601, 8422209, 8921232, 8950792]
EXPECTED_BOUNDARY = [[0, 0, 0, 0, 0, 0, 0],
                     [-1, -1, -1, 0, 0, 0, 0],
                     [1, -1, 1, 0, 0, 0, 0],
                     [0, 0, 0, -1, 0, 1, 0],
                     [-1, 0, -1, -1, 0, 1, 0]]


def edges_and_faces():
    edges = sorted({tuple(sorted((i, (i+1) % N))) for i in range(N)} |
                   {tuple(sorted((i, i+N//2))) for i in range(N//2)})
    assert len(edges) == 24
    # A face is a matching of graph edges, encoded by its 24-bit incidence mask.
    faces = {0}
    for j, (u, v) in enumerate(edges):
        conflict = sum(1 << k for k, (a, b) in enumerate(edges)
                       if u in (a, b) or v in (a, b))
        faces.update(f | (1 << j) for f in tuple(faces) if not f & conflict)
    return edges, faces


def verify_face_enumeration(edges, faces):
    assert len(faces) == 11394  # includes the empty face
    histogram = Counter(f.bit_count()-1 for f in faces if f)
    assert [histogram[d] for d in range(8)] == [24, 228, 1096, 2834, 3880, 2588, 696, 47]
    # Recheck each face directly against graph endpoints, without relying on
    # the incremental construction's conflict masks.
    for f in faces:
        used = 0
        for j, (u, v) in enumerate(edges):
            if f & (1 << j):
                assert not used & ((1 << u) | (1 << v))
                used |= (1 << u) | (1 << v)
    return histogram


def boundary(f):
    terms, bits = [], f
    i = 0
    while bits:
        b = bits & -bits
        terms.append((f ^ b, 1 if i % 2 == 0 else -1))
        bits -= b
        i += 1
    return terms


def verify_acyclic(faces, pairs):
    all_faces = faces - {0}
    matched = {lower: upper for lower, upper in pairs}
    indegree = {f: 0 for f in all_faces}
    graph = defaultdict(list)
    incidences = 0
    for upper in all_faces:
        if upper.bit_count() == 1:
            continue
        for lower, _ in boundary(upper):
            # Reverse each matched codimension-one incidence; all other
            # incidences retain the downward orientation.
            source, target = ((lower, upper) if matched.get(lower) == upper
                              else (upper, lower))
            graph[source].append(target)
            indegree[target] += 1
            incidences += 1
    queue = deque(f for f, d in indegree.items() if d == 0)
    processed = 0
    while queue:
        f = queue.popleft()
        processed += 1
        for g in graph[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert incidences == 55256 and processed == len(all_faces)
    return incidences


def integral_morse_boundary(critical, pairs):
    critical = set(critical)
    lower_to_upper = {a: b for a, b in pairs}
    upper_to_lower = {b: a for a, b in pairs}
    rows = sorted(f for f in critical if f.bit_count() == 5)
    cols = sorted(f for f in critical if f.bit_count() == 6)
    assert len(rows) == 5 and len(cols) == 7

    @lru_cache(None)
    def reduce_four(f):
        if f in critical:
            return {f: 1}
        if f in upper_to_lower:
            return {}  # Removed by a lower-dimensional matched incidence.
        upper = lower_to_upper[f]
        bnd = dict(boundary(upper))
        pivot = bnd.pop(f)  # The coefficient is exactly ±1.
        out = defaultdict(int)
        for g, sign in bnd.items():
            for h, coeff in reduce_four(g).items():
                out[h] -= pivot * sign * coeff
        return {h: coeff for h, coeff in out.items() if coeff}

    matrix = [[0 for _ in cols] for _ in rows]
    row_index = {f: i for i, f in enumerate(rows)}
    for j, upper in enumerate(cols):
        result = defaultdict(int)
        for lower, sign in boundary(upper):
            for h, coeff in reduce_four(lower).items():
                result[h] += sign * coeff
        for h, coeff in result.items():
            matrix[row_index[h]][j] = coeff
    assert matrix == EXPECTED_BOUNDARY, (matrix, EXPECTED_BOUNDARY)
    return matrix, rows, cols


def det(matrix):
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    return sum((-1 if j % 2 else 1) * matrix[0][j] *
               det([row[:j] + row[j+1:] for row in matrix[1:]])
               for j in range(n) if matrix[0][j])


def verify_integral_rank(matrix):
    # A unit 3-minor and vanishing 4-minors imply rank exactly three,
    # and the Smith invariants are all one. Full integral torsion check.
    minor = [[matrix[i][j] for j in (0, 1, 3)] for i in (1, 3, 4)]
    assert abs(det(minor)) == 1
    for rows in combinations(range(5), 4):
        for cols in combinations(range(7), 4):
            assert det([[matrix[i][j] for j in cols] for i in rows]) == 0


def gf2_reduced_betti(faces):
    layers = {k: sorted(f for f in faces if f.bit_count() == k)
              for k in range(1, 9)}
    rank = {1: 1}  # augmented boundary of degree-zero simplices
    for k in range(2, 9):
        idx = {f: j for j, f in enumerate(layers[k-1])}
        pivots = {}
        for face in layers[k]:
            col = 0
            for subface, sign in boundary(face):
                col ^= 1 << idx[subface]
            while col:
                pivot = col.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot] = col
                    break
                col ^= pivots[pivot]
        rank[k] = len(pivots)
    betti = {k-1: len(layers[k])-rank.get(k, 0)-rank.get(k+1, 0)
             for k in range(1, 9)}
    assert betti == {0: 0, 1: 0, 2: 0, 3: 0, 4: 2, 5: 4, 6: 0, 7: 0}
    return betti


def main():
    edges, faces = edges_and_faces()
    histogram = verify_face_enumeration(edges, faces)
    nonempty = sorted(faces - {0})
    remaining = set(nonempty)
    pairs = []
    for j in EDGE_ORDER:
        bit = 1 << j
        for lower in nonempty:
            upper = lower | bit
            if not (lower & bit) and lower in remaining and upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                pairs.append((lower, upper))
    assert sorted(remaining) == EXPECTED_CRITICAL
    assert len(pairs) == 5690
    assert Counter(f.bit_count()-1 for f in remaining) == {0:1, 4:5, 5:7}
    incidences = verify_acyclic(faces, pairs)
    matrix, rows, cols = integral_morse_boundary(remaining, pairs)
    verify_integral_rank(matrix)
    betti = gf2_reduced_betti(faces)
    print('VERIFY_OK edges=24 faces=11393 f_vector='+str(tuple(histogram[d] for d in range(8))))
    print('VERIFY_OK incidences='+str(incidences)+' matched_pairs='+str(len(pairs))+
          ' critical=(1_0,5_4,7_5) acyclic=11393')
    print('VERIFY_OK Morse_D5_to_D4='+str(matrix)+' integral_smith=(1,1,1)')
    print('VERIFY_OK reduced_Betti_mod2='+str(betti)+
          ' homotopy=2S4_plus_4S5')


if __name__ == '__main__':
    main()
