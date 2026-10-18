"""Standalone checks for an S5 co-occurrence formula / independence polynomial theorem.

Python 3, standard library only. No external papers or network access required.
"""
from itertools import combinations, permutations, product
from math import comb, factorial
from random import Random


def stirling2(n, k):
    if k == 0:
        return int(n == 0)
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for r in range(1, n + 1):
        for j in range(1, min(r, k) + 1):
            table[r][j] = table[r - 1][j - 1] + j * table[r - 1][j]
    return table[n][k]


def independent_coefficients(q, edges):
    edges = [frozenset(e) for e in edges]
    coeffs = [0] * (q + 1)
    for mask in range(1 << q):
        vertices = {v for v in range(q) if mask & (1 << v)}
        if not any(edge <= vertices for edge in edges):
            coeffs[len(vertices)] += 1
    return coeffs


def nonmodels_closed(q, edges, n):
    coeffs = independent_coefficients(q, edges)
    return sum(coeffs[j] * factorial(j) * stirling2(n, j)
               for j in range(min(q, n) + 1))


def models_direct(q, edges, n):
    # In one complete S5 component, Diamond tau_v holds exactly when v
    # appears among the labels of the n worlds.
    total = 0
    for worlds in product(range(q), repeat=n):
        support = set(worlds)
        if any(u in support and v in support for u, v in edges):
            total += 1
    return total


def graph_polynomial_collision_is_genuine():
    # A 4-vertex path and a triangle with an isolated vertex.
    path = [(0, 1), (1, 2), (2, 3)]
    tri_isolate = [(0, 1), (0, 2), (1, 2)]
    assert independent_coefficients(4, path) == [1, 4, 3, 0, 0]
    assert independent_coefficients(4, tri_isolate) == [1, 4, 3, 0, 0]
    assert sorted(sum(v in e for e in path) for v in range(4)) == [1, 1, 2, 2]
    assert sorted(sum(v in e for e in tri_isolate) for v in range(4)) == [0, 2, 2, 2]
    # Support {0,2} satisfies the triangle formula but not the path formula.
    assert models_direct(4, path, 2) == models_direct(4, tri_isolate, 2) == 6
    assert not any(u in {0, 2} and v in {0, 2} for u, v in path)
    assert any(u in {0, 2} and v in {0, 2} for u, v in tri_isolate)
    for n in range(1, 9):
        expected = 4**n - (3 * 2**n - 2)
        assert nonmodels_closed(4, path, n) == 3 * 2**n - 2
        assert nonmodels_closed(4, tri_isolate, n) == 3 * 2**n - 2
        if n <= 6:
            assert models_direct(4, path, n) == expected
            assert models_direct(4, tri_isolate, n) == expected
    return path, tri_isolate


def isomorphic(q, edges1, edges2):
    edge2 = {frozenset(e) for e in edges2}
    return any({frozenset((p[u], p[v])) for u, v in edges1} == edge2
               for p in permutations(range(q)))


def check_smallest_collision():
    for q in range(1, 4):
        all_edges = list(combinations(range(q), 2))
        groups = {}
        for mask in range(1 << len(all_edges)):
            edges = [e for i, e in enumerate(all_edges) if mask & (1 << i)]
            poly = tuple(independent_coefficients(q, edges))
            for old in groups.get(poly, []):
                assert isomorphic(q, edges, old)
            groups.setdefault(poly, []).append(edges)


def check_complete_enumeration():
    evaluations = 0
    graphs = 0
    for q in (2, 4):
        edge_options = list(combinations(range(q), 2))
        for mask in range(1 << len(edge_options)):
            graph = [e for i, e in enumerate(edge_options) if mask & (1 << i)]
            i_coeffs = independent_coefficients(q, graph)
            recovered = [1]
            for n in range(1, q + 1):
                no_models = nonmodels_closed(q, graph, n)
                numerator = no_models - sum(
                    recovered[j] * factorial(j) * stirling2(n, j)
                    for j in range(1, n))
                assert numerator % factorial(n) == 0
                recovered.append(numerator // factorial(n))
            assert recovered == i_coeffs
            for n in range(1, 6):
                assert models_direct(q, graph, n) == q**n - nonmodels_closed(q, graph, n)
                evaluations += q**n
            graphs += 1
    rng = Random(104729)
    for _ in range(16):
        q = 8
        edges = [edge for edge in combinations(range(q), 2) if rng.randrange(3) == 0]
        for n in range(1, 5):
            assert models_direct(q, edges, n) == q**n - nonmodels_closed(q, edges, n)
            evaluations += q**n
        graphs += 1
    return graphs, evaluations


if __name__ == '__main__':
    p, t = graph_polynomial_collision_is_genuine()
    check_smallest_collision()
    graphs, worlds = check_complete_enumeration()
    print(f'VERIFY_OK graphs={graphs} complete_frame_valuations={worlds} '
          'inversion=PASS min_collision=4 path_triangle_isolate=PASS')
