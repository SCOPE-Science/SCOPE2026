"""Independent finite checks for triangle-avoiding complexes of edge-glued cliques.

Usage: python3 verify_clique_glue.py [max_private_part_size]
Default tests all integer (a,b) in [2,6] x [2,6].
The exhaustive finite tests corroborate, but do not prove, the infinite homotopy claim.
"""
import itertools
import math
import sys


def binary_rank(columns):
    pivots = {}
    for value in columns:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def all_faces_from_graph(a, b):
    n = a + b + 2
    u, v = n - 2, n - 1
    edges = set()
    for clique in [list(range(a)) + [u, v],
                   list(range(a, a+b)) + [u, v]]:
        for i, j in itertools.combinations(clique, 2):
            edges.add((min(i, j), max(i, j)))
    triples = []
    for i, j, k in itertools.combinations(range(n), 3):
        if all((x, y) in edges for x, y in [(i, j), (j, k), (i, k)]):
            triples.append((1 << i) | (1 << j) | (1 << k))
    faces = {0: [0]}
    for p in range(1, n + 1):
        faces[p] = []
        for selected in itertools.combinations(range(n), p):
            mask = sum(1 << j for j in selected)
            if all((mask & triangle) != triangle for triangle in triples):
                faces[p].append(mask)
    return faces


def face_count_by_decomposition(a, b):
    # F_A*F_B plus the two cones over their 0-skeleton joins plus uv edge.
    from math import comb
    polys = [[1, a, comb(a, 2)], [1, b, comb(b, 2)]]
    expected = [0] * (a+b+3)
    for i, c in enumerate(polys[0]):
        for j, d in enumerate(polys[1]):
            expected[i+j] += c*d
    # New faces involving exactly one of u and v.
    expected[1] += 2
    expected[2] += 2*(a+b)
    expected[3] += 2*a*b
    # The only new face involving both u and v is their edge.
    expected[2] += 1
    return expected


def reduced_betti_mod_two(faces, n):
    r = [0] * (n+2)
    for size in range(1, n+1):
        indices = {mask: i for i, mask in enumerate(faces[size-1])}
        columns = []
        for mask in faces[size]:
            boundary = 0
            for vertex in range(n):
                if (mask >> vertex) & 1:
                    boundary ^= 1 << indices[mask ^ (1 << vertex)]
            columns.append(boundary)
        r[size] = binary_rank(columns)
    return [len(faces[size]) - r[size] - r[size+1]
            for size in range(1, n+1)]


def run(high=6):
    assert high >= 2
    pairs = 0
    total_faces = 0
    for a in range(2, high+1):
        for b in range(2, high+1):
            faces = all_faces_from_graph(a, b)
            observed = [len(faces[p]) for p in range(a+b+3)]
            expected_faces = face_count_by_decomposition(a, b)
            assert observed == expected_faces, (a, b, observed, expected_faces)
            homology = reduced_betti_mod_two(faces, a+b+2)
            predicted = [0] * (a+b+2)
            predicted[1] = 1
            predicted[2] = 2*(a-1)*(b-1)
            predicted[3] = math.comb(a-1, 2)*math.comb(b-1, 2)
            assert homology == predicted, (a, b, homology, predicted)
            pairs += 1
            total_faces += sum(len(faces[p]) for p in faces)
            print('a={} b={} faces={} reduced_betti={}'.format(
                a, b, sum(observed), homology[:4]))
    print('CASES={} TOTAL_FACES={} ALL_F_POLYNOMIALS_AND_BETTI_MATCH'.format(
        pairs, total_faces))
    print('VERIFY_OK')


if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
