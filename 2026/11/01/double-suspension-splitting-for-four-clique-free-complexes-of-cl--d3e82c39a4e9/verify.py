"""Finite boundary-matrix checks for four-clique-free complexes of clique joins.

Run with: python3 verify.py. No external packages are required.
The checks are finite corroboration of a separate, all-parameter topological proof.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def reduced_betti(faces, vertices, prime):
    by_dim = defaultdict(list)
    for mask in faces:
        if mask:
            by_dim[mask.bit_count() - 1].append(mask)
    dimensions = sorted(by_dim)
    ranks = {}
    for d in dimensions:
        if d == 0:
            continue
        index = {mask: j for j, mask in enumerate(by_dim[d - 1])}
        pivots = {}
        for face in by_dim[d]:
            col = {}
            for offset, bit in enumerate(j for j in range(vertices) if face & (1 << j)):
                row = index[face ^ (1 << bit)]
                col[row] = (1 if offset % 2 == 0 else prime - 1)
            while col:
                pivot = max(col)
                if pivot not in pivots:
                    inverse = pow(col[pivot], -1, prime)
                    pivots[pivot] = {key: (value * inverse) % prime
                                     for key, value in col.items()}
                    break
                scalar = col[pivot]
                for key, value in pivots[pivot].items():
                    updated = (col.get(key, 0) - scalar * value) % prime
                    if updated:
                        col[key] = updated
                    else:
                        col.pop(key, None)
        ranks[d] = len(pivots)
    return {d: count for d, cells in by_dim.items()
            if (count := len(cells) - ranks.get(d, 0) - ranks.get(d + 1, 0)
                          - (1 if d == 0 else 0)) != 0}


def triangle_free(edges, n):
    adjacency = {tuple(sorted(edge)) for edge in edges}
    return not any(all(tuple(sorted((a, b))) in adjacency
                       for a, b in combinations(triple, 2))
                   for triple in combinations(range(n), 3))


def complex_faces(n, m, edges, forbidden_size):
    # Label clique vertices 0,...,m-1 and graph vertices m,...,m+n-1.
    adjacency = set(combinations(range(m), 2))
    adjacency.update((j, m + k) for j in range(m) for k in range(n))
    adjacency.update(tuple(sorted((m + a, m + b))) for a, b in edges)
    forbidden = []
    for subset in combinations(range(n + m), forbidden_size):
        if all(pair in adjacency for pair in combinations(subset, 2)):
            forbidden.append(sum(1 << j for j in subset))
    return [mask for mask in range(1 << (n + m))
            if all((mask & mask_banned) != mask_banned
                   for mask_banned in forbidden)]


def independent_faces(n, edges):
    forbidden = [(1 << a) | (1 << b) for a, b in edges]
    return [mask for mask in range(1 << n)
            if all((mask & edge) != edge for edge in forbidden)]


def check_exact_cover(n, m, edges, full):
    independent = set(independent_faces(n, edges))
    full_set = set(full)
    hub_mask = (1 << m) - 1
    for face in range(1 << (n + m)):
        apices = (face & hub_mask).bit_count()
        rim = face >> m
        b = apices <= 1
        y = (apices <= 2 and rim in independent) or (apices == 3 and rim == 0)
        z = apices <= 1 and rim in independent
        assert (face in full_set) == (b or y), (n, m, edges, face)
        assert z == (b and y), (n, m, edges, face)


def main():
    examples = 0
    prime_tests = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for bits in range(1 << len(pairs)):
            edges = [edge for i, edge in enumerate(pairs) if bits & (1 << i)]
            if not triangle_free(edges, n):
                continue
            ind = independent_faces(n, edges)
            for m in (2, 3, 4):
                full = complex_faces(n, m, edges, 4)
                check_exact_cover(n, m, edges, full)
                for p in (2, 3, 5):
                    hom_ind = reduced_betti(ind, n, p)
                    predicted = {d + 2: comb(m, 2) * count
                                 for d, count in hom_ind.items()}
                    predicted[2] = predicted.get(2, 0) + comb(m, 3)
                    predicted = {d: count for d, count in predicted.items() if count}
                    observed = reduced_betti(full, n + m, p)
                    assert predicted == observed, (n, m, edges, p,
                                                   predicted, observed)
                    prime_tests += 1
                examples += 1
    # Higher-order torsion-free examples with independence homology in degree 1 or 2.
    for n, edges in [
        (5, [(j, (j + 1) % 5) for j in range(5)]),
        (6, [(j, (j + 1) % 6) for j in range(6)]),
        (6, [(0, 1), (2, 3), (4, 5)]),
        (6, [(j, j + 1) for j in range(5)]),
    ]:
        ind = independent_faces(n, edges)
        for m in (2, 3, 4):
            full = complex_faces(n, m, edges, 4)
            check_exact_cover(n, m, edges, full)
            for p in (2, 3, 5):
                hom_ind = reduced_betti(ind, n, p)
                predicted = {d + 2: comb(m, 2) * value
                             for d, value in hom_ind.items()}
                predicted[2] = predicted.get(2, 0) + comb(m, 3)
                predicted = {d: value for d, value in predicted.items() if value}
                observed = reduced_betti(full, n + m, p)
                assert predicted == observed, (n, m, p, predicted, observed)
                prime_tests += 1
            examples += 1
    # The triangle-free hypothesis is essential: K_2 join K_3 is K_5.
    illegal_edges = [(0, 1), (0, 2), (1, 2)]
    illegal = complex_faces(3, 2, illegal_edges, 4)
    assert reduced_betti(illegal, 5, 2) == {2: 4}
    assert reduced_betti(independent_faces(3, illegal_edges), 3, 2) == {0: 2}
    print('TRIANGLE_BOUNDARY_CASE_OK CF4(K5): four 2-spheres; the excluded extrapolation gives two')
    print('FACE_COVER_INTERSECTION_IDENTITY_OK', examples)
    print('FINITE_COMPLEXES_OK', examples)
    print('INDEPENDENT_FIELD_HOMOLOGY_CHECKS_OK', prime_tests)
    print('ALL_VERIFY_OK')


if __name__ == '__main__':
    main()
