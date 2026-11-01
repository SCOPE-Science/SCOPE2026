"""Finite base certificate and independent cross-checks for four-tuples of cyclic 8-polytope boundaries.

Run: python3 verify.py  (standard library only)
The infinite-range connectivity proof is in RESULT.md, not inferred from this finite test.
"""
from itertools import combinations
from collections import Counter
from math import comb

R = 4


def matching_facets(n, circular):
    """Eight-sets covered by four pairwise disjoint cycle/path edges."""
    edge_starts = range(n) if circular else range(n - 1)
    result = set()
    for starts in combinations(edge_starts, R):
        covered = set()
        for v in starts:
            covered.update((v, (v + 1) % n))
        if len(covered) == 2 * R:
            result.add(tuple(sorted(covered)))
    return result


def gale_facets(n):
    """Independent facet enumeration from Gale's original evenness condition."""
    result = set()
    for F in combinations(range(n), 2 * R):
        complement = sorted(set(range(n)) - set(F))
        if all(sum(a < f < b for f in F) % 2 == 0
               for a, b in combinations(complement, 2)):
            result.add(F)
    return result


def edges_and_classes(n, facets):
    vertices = list(combinations(range(n), R))
    indexes = {v: i for i, v in enumerate(vertices)}
    edges = set()
    for F in facets:
        for a in combinations(F, R):
            b = tuple(v for v in F if v not in a)
            x, y = sorted((indexes[a], indexes[b]))
            edges.add((x, y))
    adjacency = [set() for _ in vertices]
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    unseen = set(range(len(vertices)))
    components = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        component = set([start])
        while stack:
            x = stack.pop()
            for y in adjacency[x] & unseen:
                unseen.remove(y)
                stack.append(y)
                component.add(y)
        components.append(component)
    return vertices, edges, components


def parity_class(subset):
    k = sum(v % 2 == 0 for v in subset)
    return min(k, R - k)


def predicted_facets(n):
    return n * (n - 5) * (n - 6) * (n - 7) // 24


def check(n, circular):
    facets = matching_facets(n, circular)
    if circular:
        assert len(facets) == predicted_facets(n), (n, 'facet count')
    vertices, edges, components = edges_and_classes(n, facets)
    assert len(vertices) == comb(n, R)
    assert len(edges) == 35 * len(facets)
    assert all(len(c) > 0 for c in components)
    if not circular or n % 2 == 0:
        assert len(components) == 3, (n, circular, list(map(len, components)))
        assert {parity_class(vertices[next(iter(c))]) for c in components} == {0, 1, 2}
        assert all(len({parity_class(vertices[j]) for j in c}) == 1 for c in components)
        if circular:
            m = n // 2
            counts = {k: len(c) for c in components for k in [parity_class(vertices[next(iter(c))])]}
            assert counts == {0: 2*comb(m,4), 1: 2*m*comb(m,3), 2: comb(m,2)**2}
            # Count edges separately inside each connected component.
            by_index = {j: parity_class(vertices[j]) for j in range(len(vertices))}
            edge_counts = Counter(by_index[i] for i, j in edges)
            assert all(by_index[i] == by_index[j] for i, j in edges)
            assert edge_counts == {0: len(facets), 1: 16*len(facets), 2: 18*len(facets)}
            betti = {k: edge_counts[k] - counts[k] + 1 for k in (0,1,2)}
            assert all(betti[k] >= 0 for k in betti)
            return n, len(vertices), len(facets), len(edges), counts, betti
        return n, len(vertices), len(facets), len(edges), len(components), 'path'
    else:
        assert len(components) == 1, (n, list(map(len,components)))
        b1 = len(edges) - len(vertices) + 1
        assert b1 == 35*predicted_facets(n) - comb(n,4) + 1
        return n, len(vertices), len(facets), len(edges), 1, b1


def base_path_certificate():
    n = 10
    F = matching_facets(n, circular=False)
    V, E, C = edges_and_classes(n, F)
    assert len(F) == 15 and len(V) == 210 and len(E) == 525
    assert len(C) == 3
    sizes = sorted(len(c) for c in C)
    assert sizes == [10, 100, 100]
    for c in C:
        assert len({parity_class(V[j]) for j in c}) == 1
    print('BASE_PATH_OK n=10 facets=15 vertices=210 edges=525 components=3 sizes=(10,100,100)')


def mark_cover_test():
    # Independently sanity-check the matching-cover lemma used in induction.
    for N in range(9, 17):
        all_edges = set(range(N-1))
        covers = []
        for I in combinations(all_edges, 3):
            covered = {x for v in I for x in (v,v+1)}
            if len(covered) == 6:
                covers.append(covered)
        for s in range(4):
            for marked in combinations(range(N), s):
                assert any(set(marked) <= U for U in covers), (N, marked)
    print('MATCHING_COVER_OK sizes_N=9..16 all_marked_subsets_of_size_at_most_3')


def main():
    base_path_certificate()
    mark_cover_test()
    for n in range(9, 15):
        F = matching_facets(n, True)
        G = gale_facets(n)
        assert F == G, (n, len(F), len(G), len(F ^ G))
    print('GALE_OK n=9..14 facet_sets_identical_to_circular_edge_matchings')
    for n in range(9, 18):
        assert check(n, True)
        print('CYCLE_OK', check(n, True))
    for n in range(10, 15):
        assert check(n, False)
    print('PATH_OK n=10..14 three_component_parity_partition')
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
