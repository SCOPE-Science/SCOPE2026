"""Exact finite checks for fan graphical-zonotope slicing theorem.

Uses standard-library integers and fractions. The general-dimension conclusion
comes from the separate analytical proof, not from these finite tests.
"""
from fractions import Fraction
from itertools import product
from random import Random


def fan_edges(n):
    return [(0, i) for i in range(1, n + 1)] + [
        (i, i + 1) for i in range(1, n)
    ]


def is_acyclic(nv, edges, mask):
    indeg = [0] * nv
    adj = [[] for _ in range(nv)]
    for j, (a, b) in enumerate(edges):
        if (mask >> j) & 1:
            a, b = b, a
        adj[a].append(b)
        indeg[b] += 1
    pending = [i for i, degree in enumerate(indeg) if degree == 0]
    found = 0
    while pending:
        a = pending.pop()
        found += 1
        for b in adj[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                pending.append(b)
    return found == nv


def vertices_and_edges(n, edges=None):
    if edges is None:
        edges = fan_edges(n)
    orientations = {
        mask for mask in range(1 << len(edges))
        if is_acyclic(n + 1, edges, mask)
    }
    vertices = {}
    for mask in orientations:
        coord = [0] * (n + 1)
        for j, (a, b) in enumerate(edges):
            coord[a if (mask >> j) & 1 else b] += 1
        coordinates = tuple(coord)
        assert coordinates not in vertices.values()
        vertices[mask] = coordinates
    links = []
    counts = [0] * len(edges)
    for mask in orientations:
        for j in range(len(edges)):
            other = mask ^ (1 << j)
            if other in orientations and mask < other:
                va, vb = vertices[mask], vertices[other]
                diff = [va[i] - vb[i] for i in range(n + 1)]
                nonzero = [i for i, v in enumerate(diff) if v != 0]
                assert nonzero == list(edges[j])
                assert abs(diff[nonzero[0]]) == abs(diff[nonzero[1]]) == 1
                links.append((mask, other, j))
                counts[j] += 1
    return vertices, links, counts


def expression(n, u):
    x = [u[i] - u[0] for i in range(1, n + 1)]
    total = sum(abs(z) for z in x)
    total += sum(abs(x[i] - x[i + 1]) for i in range(n - 1))
    assert total > 0
    interior = sum(abs(z) for z in x[1:-1])
    c = 2 * 3 ** (n - 2)
    return Fraction(c) - Fraction(2 * 3 ** (n - 3) * interior, total)


def cut_count(vertices, links, u):
    levels = {key: sum(a * b for a, b in zip(coord, u))
              for key, coord in vertices.items()}
    bottom, top = min(levels.values()), max(levels.values())
    assert top > bottom
    # Independent geometric formula: integrate how many edges are crossed.
    profile = sorted(set(levels.values()))
    integral = Fraction(0)
    for lo, hi in zip(profile, profile[1:]):
        mid = Fraction(lo + hi, 2)
        section_vertices = sum(1 for p, q, _ in links if
                               min(levels[p], levels[q]) < mid <
                               max(levels[p], levels[q]))
        integral += section_vertices * (hi - lo)
    return integral / (top - bottom)


def main():
    rng = Random(20261014)
    assertions = 0
    for n in range(3, 8):
        edges = fan_edges(n)
        vertices, links, counts = vertices_and_edges(n)
        assert len(vertices) == 2 * 3 ** (n - 1)
        expected = [
            2 ** (1 if i in (1, n) else 2) *
            3 ** (n - 1 - (1 if i in (1, n) else 2))
            for i in range(1, n + 1)
        ] + [2 * 3 ** (n - 2)] * (n - 1)
        assert counts == expected, (n, counts, expected)
        assertions += len(counts) + 1
        lower = Fraction(4 * (n + 1) * 3 ** (n - 3), n)
        upper = Fraction(2 * 3 ** (n - 2))
        for sample in range(60):
            u = [rng.randrange(-10, 11) for _ in range(n + 1)]
            if len(set(u)) == 1:
                continue
            x = [u[i] - u[0] for i in range(1, n + 1)]
            d = sum(abs(y) for y in x) + sum(abs(x[i+1]-x[i]) for i in range(n-1))
            m = sum(c * abs(u[a] - u[b]) for c, (a, b) in zip(counts, edges))
            a = Fraction(m, d)
            formula = expression(n, u)
            assert a == formula
            assert lower <= a <= upper
            # Exact independent integral via explicit edge crossing, in small rank.
            if n <= 5 and sample < 15:
                assert cut_count(vertices, links, u) == a
                assertions += 1
            assertions += 3
        for scale in [-3, 1, 5]:
            u = [0] + [scale] * n
            u[1], u[n] = 0, scale // 2 if scale % 2 == 0 else 0
            # Internal indices are identical and endpoints lie between 0 and scale.
            if scale > 0:
                u[1], u[n] = 0, scale
            else:
                u[1], u[n] = scale, 0
            assert expression(n, u) == lower
            u = [0] + [0] * n
            u[1], u[n] = scale, -2 * scale
            assert expression(n, u) == upper
            assertions += 2
        print(f'n={n}: {len(vertices)} exact vertices, {len(links)} edges, '
              f'[{lower}, {upper}], tests passed')
    # Exhaustive small-integer normal grid, including equality classification.
    grid_checked = 0
    for n in range(3, 7):
        lo = Fraction(4 * (n + 1) * 3 ** (n - 3), n)
        hi = Fraction(2 * 3 ** (n - 2))
        for x in product(range(-2, 3), repeat=n):
            if all(y == 0 for y in x):
                continue
            val = expression(n, [0] + list(x))
            internal = x[1:-1]
            optimal_low = (len(set(internal)) == 1 and internal[0] != 0 and
                           all(min(0, internal[0]) <= x[j] <= max(0, internal[0])
                               for j in (0, n - 1)))
            optimal_high = all(y == 0 for y in internal)
            assert (val == lo) == optimal_low, (n, x, val, lo)
            assert (val == hi) == optimal_high, (n, x, val, hi)
            grid_checked += 1
    print(f'PASS equality-classification grid normals={grid_checked}')
    # Non-path trees: degree-dependent coefficients of the general cone formula.
    # Each case is checked against explicit flip edges in the zonotope graph.
    tree_samples = 0
    for n in range(3, 7):
        trees = [
            [(1, j) for j in range(2, n + 1)],
            [(1, 2), (2, 3)] + [(3, j) for j in range(4, n + 1)]
        ]
        for tree in trees:
            edge_set = [(0, j) for j in range(1, n + 1)] + tree
            _, _, counts = vertices_and_edges(n, edge_set)
            degrees = [0] * (n + 1)
            for a, b in tree:
                degrees[a] += 1
                degrees[b] += 1
            expected = [2 ** degrees[j] * 3 ** (n - 1 - degrees[j])
                        for j in range(1, n + 1)]
            expected += [2 * 3 ** (n - 2)] * (n - 1)
            assert counts == expected, (n, tree, counts, expected)
            tree_samples += 1
    print(f'PASS non-path tree-cone coefficient profiles={tree_samples}')
    print(f'PASS assertions={assertions}; exhaustive orientations for n=3..7; '
          'integrated finite slice profiles for n=3..5')


if __name__ == '__main__':
    main()
