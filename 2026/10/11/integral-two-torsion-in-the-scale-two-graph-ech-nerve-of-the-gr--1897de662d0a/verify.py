"""Exact, self-contained check of a closed-neighborhood Čech homology certificate.

Requires only Python 3 standard library; pass certificate.json as the argument.
The finite computation checks a matrix minor and a mod-two rank, not a
homotopy classification or an assertion about other graphs.
"""

import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path


def graph():
    neighbors = {v: set() for v in range(11)}

    def add(x, y):
        assert x != y
        neighbors[x].add(y)
        neighbors[y].add(x)

    for i in range(5):
        add(i, (i + 1) % 5)
    for i in range(5):
        add(5 + i, (i - 1) % 5)
        add(5 + i, (i + 1) % 5)
        add(5 + i, 10)
    assert sum(map(len, neighbors.values())) == 40
    assert sorted(map(len, neighbors.values())) == [3] * 5 + [4] * 5 + [5]
    return neighbors


def build_faces(neighbors):
    result = set()
    for v in range(11):
        facet = sorted(neighbors[v] | {v})
        for k in range(1, len(facet) + 1):
            for face in combinations(facet, k):
                result.add(frozenset(face))
    return result


def vector(faces):
    count = Counter(len(face) - 1 for face in faces)
    return [count[i] for i in range(max(count) + 1)]


def bareiss_det(matrix):
    """Exact determinant with integer-preserving elimination and row swaps."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    if not n:
        return 1
    sign, denom = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((p for p in range(k + 1, n) if a[p][k] != 0), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % denom == 0
                a[i][j] = num // denom
            a[i][k] = 0
        denom = pivot
    return sign * a[n - 1][n - 1]


def rank_mod_p(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    m, n = len(a), len(a[0])
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        for k in range(j, n):
            a[r][k] = a[r][k] * inv % p
        for i in range(r + 1, m):
            mul = a[i][j]
            if mul:
                for k in range(j, n):
                    a[i][k] = (a[i][k] - mul * a[r][k]) % p
        r += 1
        if r == m:
            break
    return r


def check(cert):
    assert cert['schema_version'] == 1
    neighbor = graph()
    faces = build_faces(neighbor)
    assert vector(faces) == cert['expected']['initial_f_vector'] == [11, 55, 90, 45, 11, 1]
    assert len(faces) == 213
    # Every recorded elementary simplicial collapse must remove a free codimension-one
    # face and its sole coface in the complex that remains at that step.
    moves = cert['collapses']
    assert len(moves) == cert['expected']['collapse_pairs'] == 55
    for move in moves:
        sigma = frozenset(move['free_face'])
        tau = frozenset(move['coface'])
        assert sigma in faces and tau in faces
        assert len(tau) == len(sigma) + 1 and sigma < tau
        assert [other for other in faces if sigma < other] == [tau]
        faces.difference_update((sigma, tau))
    assert vector(faces) == cert['expected']['remaining_f_vector'] == [11, 46, 46]
    assert all(frozenset(face) in faces for s in faces for k in range(1, len(s))
               for face in combinations(sorted(s), k))
    tree = [tuple(edge) for edge in cert['spanning_tree_edges']]
    assert tree == [(0, i) for i in range(1, 11)]
    edges = sorted(tuple(sorted(s)) for s in faces if len(s) == 2)
    triangles = sorted(tuple(sorted(s)) for s in faces if len(s) == 3)
    assert all(edge in edges for edge in tree)
    others = [edge for edge in edges if edge not in tree]
    assert len(others) == cert['expected']['non_tree_edges'] == 36
    assert len(triangles) == cert['expected']['triangles'] == 46
    row_of = {edge: i for i, edge in enumerate(others)}
    A = [[0 for _ in triangles] for _ in others]
    for j, (x, y, z) in enumerate(triangles):
        for edge, coefficient in [((y, z), 1), ((x, z), -1), ((x, y), 1)]:
            if edge in row_of:
                A[row_of[edge]][j] += coefficient
    assert all(c in (-1, 0, 1) for row in A for c in row)
    rank2 = rank_mod_p(A, 2)
    assert rank2 == cert['expected']['mod2_rank'] == 35
    piv = cert['pivot_triangle_indices']
    assert len(piv) == 36 and len(set(piv)) == 36 and min(piv) >= 0 and max(piv) < 46
    det = bareiss_det([[row[j] for j in piv] for row in A])
    assert det == cert['expected']['determinant'] == 2
    assert rank_mod_p(A, 3) == 36
    # There are 36 1-cycle generators, 46 2-cells, and an integer minor of
    # determinant 2. Rank_2=35 forces precisely one order-two invariant factor.
    # Hence H_1 = Z/2, H_2 = Z^10, and higher homology vanishes by collapses.
    assert 46 - 36 == 10
    return {'facets': 11, 'faces': 213, 'collapse_pairs': 55,
            'spine': [11, 46, 46], 'boundary_shape': [36, 46],
            'minor_determinant': det, 'rank_mod_2': rank2,
            'homology': 'H_1=Z/2; H_2=Z^10; all other reduced groups zero'}


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('certificate.json')
    with path.open(encoding='utf-8') as stream:
        certificate = json.load(stream)
    print('VERIFY_OK', json.dumps(check(certificate), sort_keys=True))
