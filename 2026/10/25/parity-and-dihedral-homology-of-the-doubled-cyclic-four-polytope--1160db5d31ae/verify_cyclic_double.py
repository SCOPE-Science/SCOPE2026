"""Exact finite cross-checks for doubles of four-dimensional cyclic polytopes.

Requires Python 3 standard library only. Universal statements have separate proofs.
"""
from itertools import combinations
from collections import defaultdict


def gale_facets(n):
    facets = set()
    for chosen in combinations(range(n), 4):
        chosen_set = set(chosen)
        absent = sorted(set(range(n)) - chosen_set)
        if all(sum(a < x < b for x in chosen) % 2 == 0
               for a, b in combinations(absent, 2)):
            facets.add(frozenset(chosen))
    return facets


def polygon_facets(n):
    boundary_edges = [frozenset((i, (i + 1) % n)) for i in range(n)]
    return {a | b for a, b in combinations(boundary_edges, 2) if not a & b}


def doubled_graph(n):
    facets = gale_facets(n)
    assert facets == polygon_facets(n), ('Gale criterion discrepancy', n)
    vertices = set(combinations(range(n), 2))
    edges = set()
    for facet in facets:
        for a in combinations(sorted(facet), 2):
            b = tuple(sorted(facet - set(a)))
            edges.add(tuple(sorted((a, b))))
    neighbors = {v: set() for v in vertices}
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    components = []
    unseen = set(vertices)
    while unseen:
        seed = next(iter(unseen))
        todo = [seed]
        comp = {seed}
        unseen.remove(seed)
        while todo:
            for w in neighbors[todo.pop()]:
                if w in unseen:
                    unseen.remove(w)
                    comp.add(w)
                    todo.append(w)
        components.append(comp)
    return vertices, edges, components


def theoretical_character(n, a, b):
    """Dihedral map i -> a*i + b, where a in {-1, +1}."""
    if a == 1:
        if b % n == 0:
            return n * (n - 4) + (2 if n % 2 == 0 else 1)
        if n % 2 == 0 and b % n == n // 2:
            return 2 - n
        return 2 if n % 2 == 0 else 1
    if n % 2:
        return 3 - n
    return 4 - n if b % 2 == 0 else 2 - n


def run():
    total_cases = 0
    for n in range(5, 25):
        vertices, edges, components = doubled_graph(n)
        assert len(vertices) == n * (n - 1) // 2
        assert len(edges) == 3 * n * (n - 3) // 2
        assert len(components) == (1 if n % 2 else 2)
        if n % 2:
            assert len(edges) - len(vertices) + 1 == n * (n - 4) + 1
        else:
            component_by_parity = {int(any((b - a) % 2 for a, b in c)): c for c in components}
            assert len(component_by_parity) == 2
            even = component_by_parity[0]
            odd = component_by_parity[1]
            even_edges = sum(a in even and b in even for a, b in edges)
            odd_edges = sum(a in odd and b in odd for a, b in edges)
            assert len(even) == n * (n - 2) // 4
            assert len(odd) == n * n // 4
            assert even_edges == n * (n - 3) // 2
            assert odd_edges == n * (n - 3)
            assert even_edges - len(even) + 1 == n * (n - 4) // 4 + 1
            assert odd_edges - len(odd) + 1 == (3 * n * n) // 4 - 3 * n + 1
        for a in (1, -1):
            for b in range(n):
                g = lambda x: (a * x + b) % n
                gv = lambda v: tuple(sorted((g(v[0]), g(v[1]))))
                vertex_trace = sum(gv(v) == v for v in vertices)
                edge_trace = 0
                for e in edges:
                    p, q = e
                    gp, gq = gv(p), gv(q)
                    if gp == p and gq == q:
                        edge_trace += 1
                    if gp == q and gq == p:
                        edge_trace -= 1
                component_trace = sum({gv(v) for v in c} == c for c in components)
                actual = edge_trace - vertex_trace + component_trace
                expected = theoretical_character(n, a, b)
                assert actual == expected, (n, a, b, actual, expected)
                total_cases += 1
        print(f'n={n} vertices={len(vertices)} edges={len(edges)} components={len(components)} rank={len(edges)-len(vertices)+len(components)}')
    print(f'PASS: n=5..24, {total_cases} signed dihedral Lefschetz checks, independent Gale facets.')


if __name__ == '__main__':
    run()
