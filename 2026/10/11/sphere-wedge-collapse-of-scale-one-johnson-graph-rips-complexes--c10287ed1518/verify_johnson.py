#!/usr/bin/env python3
"""Finite checks for clique complexes of Johnson graphs.

Usage: python3 verify_johnson.py
Only Python's standard library is needed. The finite tests supplement,
but do not establish, the all-parameter topological argument.
"""
from itertools import combinations
from math import comb


def facets_from_subsets(n, k, vertices):
    ix = {x: i for i, x in enumerate(vertices)}
    stars = [frozenset(ix[tuple(sorted(w + (j,)))]
                       for j in range(n) if j not in w)
             for w in combinations(range(n), k - 1)]
    tops = [frozenset(ix[v] for v in combinations(u, k))
            for u in combinations(range(n), k + 1)]
    return stars + tops


def maximal_cliques(adjacency):
    """Bron-Kerbosch with pivot, using adjacency rather than star/top facets."""
    ans = set()
    def visit(r, p, x):
        if not p and not x:
            ans.add(frozenset(r))
            return
        pool = p | x
        if pool:
            pivot = max(pool, key=lambda v: len(p & adjacency[v]))
            trials = list(p - adjacency[pivot])
        else:
            trials = list(p)
        for v in trials:
            visit(r | {v}, p & adjacency[v], x & adjacency[v])
            p.remove(v)
            x.add(v)
    visit(set(), set(range(len(adjacency))), set())
    return ans


def all_faces(facets):
    out = set()
    for f in facets:
        f = sorted(f)
        for r in range(1, len(f) + 1):
            out.update(frozenset(s) for s in combinations(f, r))
    return out


def rank_mod_two(columns):
    pivots = {}
    for column in columns:
        while column:
            i = column.bit_length() - 1
            if i not in pivots:
                pivots[i] = column
                break
            column ^= pivots[i]
    return len(pivots)


def run_case(n, k):
    vs = list(combinations(range(n), k))
    sets = [set(v) for v in vs]
    adjacency = [set() for _ in vs]
    for a in range(len(vs)):
        for b in range(a+1, len(vs)):
            if len(sets[a] & sets[b]) == k - 1:
                adjacency[a].add(b)
                adjacency[b].add(a)
    facets = facets_from_subsets(n, k, vs)
    assert len(facets) == comb(n, k-1) + comb(n, k+1)
    assert len(set(facets)) == len(facets)
    found = maximal_cliques(adjacency)
    assert found == set(facets), ('maximal clique mismatch', n, k)
    faces = all_faces(facets)
    vertex_number = len(vs)
    edges = frozenset(f for f in faces if len(f) == 2)
    assert len(edges) == comb(n,k)*k*(n-k)//2
    chi_full = sum((-1)**(len(f)-1) for f in faces)
    beta_formula = (comb(n,k)-1-len(edges)
                    + comb(n,k-1)*comb(n-k,2)
                    + comb(n,k+1)*comb(k,2))
    assert chi_full == 1 + beta_formula

    # Each high-dimensional face lies in exactly one clique facet.
    for face in list(faces):
        if len(face) >= 3:
            assert sum(face <= facet for facet in facets) == 1
    steps = 0
    for facet in sorted(facets, key=lambda f: (len(f), tuple(sorted(f)))):
        apex = min(facet)
        base = sorted(facet - {apex})
        for r in range(len(base), 2, -1):
            for a in combinations(base, r):
                low = frozenset(a)
                high = low | {apex}
                assert low in faces and high in faces
                # The removed face has exactly one immediate coface.
                cofaces = [v for v in range(vertex_number)
                           if v not in low and low | {v} in faces]
                assert cofaces == [apex], (n, k, low, cofaces)
                faces.remove(low)
                faces.remove(high)
                steps += 1
    assert all(len(f) <= 3 for f in faces)
    assert frozenset(f for f in faces if len(f) == 2) == edges
    assert len([f for f in faces if len(f)==1]) == vertex_number
    triangles = sorted((f for f in faces if len(f) == 3), key=lambda x:tuple(sorted(x)))
    expected_triangles = (comb(n,k-1)*comb(n-k,2)
                          + comb(n,k+1)*comb(k,2))
    assert len(triangles) == expected_triangles
    edge_ids = {e: i for i,e in enumerate(sorted(edges, key=lambda x:tuple(sorted(x))))}
    columns = [sum(1 << edge_ids[frozenset(e)] for e in combinations(t,2))
               for t in triangles]
    rank = rank_mod_two(columns)
    b1 = len(edges) - vertex_number + 1 - rank
    b2 = len(triangles) - rank
    assert b1 == 0 and b2 == beta_formula
    assert len(faces) == vertex_number + len(edges) + len(triangles)
    return steps, beta_formula, (vertex_number, len(edges), len(triangles))


def main():
    count = 0
    total_steps = 0
    for n in range(4,9):
        for k in range(2,n-1):
            steps, beta, vector = run_case(n,k)
            count += 1
            total_steps += steps
            print(f'n={n} k={k} beta2={beta} f2d={vector} collapse_pairs={steps}')
    print(f'VERIFY_OK cases={count} exact_collapse_pairs={total_steps}')


if __name__ == '__main__':
    main()
