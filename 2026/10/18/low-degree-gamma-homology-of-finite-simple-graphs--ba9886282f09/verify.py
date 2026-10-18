#!/usr/bin/env python3
"""Finite cross-checks for integral low-degree Gamma-homology of simple graphs.

The infinite-family proof does not rely on these finite examples.
The Gamma cube has vertices (0,1)^n and closed Hamming-radius-one hyperedges.
"""
from collections import defaultdict
from itertools import combinations, product


def is_nondegenerate(t, n):
    return all(any(t[k] != t[k ^ (1 << i)] for k in range(1 << n))
               for i in range(n))


def gamma_cells(n, vertices, graph_edges):
    edges = {frozenset(e) for e in graph_edges}
    if n == 0:
        supported = {x for edge in edges for x in edge}
        return [(i,) for i in range(vertices) if i in supported]
    balls = [tuple([x] + [x ^ (1 << j) for j in range(n)])
             for x in range(1 << n)]
    cells = []
    for t in product(range(vertices), repeat=1 << n):
        if not is_nondegenerate(t, n):
            continue
        legal = True
        for ball in balls:
            vals = frozenset(t[k] for k in ball)
            if len(vals) > 2 or not any(vals <= e for e in edges):
                legal = False
                break
        if legal:
            cells.append(t)
    return cells


def face(t, n, i, side):
    return tuple(t[j] for j in range(1 << n)
                 if ((j >> i) & 1) == side)


def boundary(t, n):
    out = defaultdict(int)
    for i in range(n):
        for side, sign in ((0, (-1) ** (i + 1)), (1, (-1) ** i)):
            f = face(t, n, i, side)
            if is_nondegenerate(f, n - 1):
                out[f] += sign
    return {f: a for f, a in out.items() if a}


def signed_sum(*terms):
    out = defaultdict(int)
    for a, d in terms:
        for x, v in d.items():
            out[x] += a * v
    return {x: v for x, v in out.items() if v}


def cone(t, n, anchor=0):
    return t + (anchor,) * (1 << n)


def cone_chain(c, n, anchor=0):
    out = defaultdict(int)
    for t, coeff in c.items():
        x = cone(t, n, anchor)
        if is_nondegenerate(x, n + 1):
            out[x] += coeff * (-1) ** (n + 1)
    return {x: y for x, y in out.items() if y}


def chain_boundary(c, n):
    out = defaultdict(int)
    for t, coeff in c.items():
        for f, a in boundary(t, n).items():
            out[f] += coeff * a
    return {x: y for x, y in out.items() if y}


def gf2_rank(columns):
    basis = {}
    for vector in columns:
        while vector:
            p = vector.bit_length() - 1
            if p in basis:
                vector ^= basis[p]
            else:
                basis[p] = vector
                break
    return len(basis)


def graph_comp_count(v, edges):
    parent = list(range(v))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in edges:
        parent[find(a)] = find(b)
    return len({find(x) for x in range(v)})


def check_edge_contraction():
    checked = 0
    for n in range(4):
        for t in gamma_cells(n, 2, [(0, 1)]):
            first = chain_boundary(cone_chain({t: 1}, n), n + 1)
            second = cone_chain(boundary(t, n), n - 1) if n else {}
            right = {t: 1}
            if n == 0:
                # The degree-zero augmentation sends each vertex to the anchor.
                right = {t: 1} if t == (1,) else {}
                if t == (1,):
                    right[(0,)] = -1
            assert signed_sum((1, first), (1, second)) == right, (n, t)
            checked += 1
    return checked


def check_graph(v, edges):
    assert len({x for edge in edges for x in edge}) == v
    C = {n: gamma_cells(n, v, edges) for n in range(4)}
    # Every nondegenerate Gamma square has exactly the two endpoints of one edge.
    for t in C[2]:
        assert frozenset(t) in {frozenset(e) for e in edges}
    index = [{cell: k for k, cell in enumerate(C[n])} for n in range(3)]
    ranks = {}
    for n in (1, 2, 3):
        columns = []
        for t in C[n]:
            b = boundary(t, n)
            assert all(f in index[n - 1] for f in b)
            if n >= 2:
                assert not chain_boundary(b, n - 1)
            vec = 0
            for f, coeff in b.items():
                if coeff % 2:
                    vec ^= 1 << index[n - 1][f]
            columns.append(vec)
        ranks[n] = gf2_rank(columns)
    b0 = len(C[0]) - ranks[1]
    b1 = len(C[1]) - ranks[1] - ranks[2]
    b2 = len(C[2]) - ranks[2] - ranks[3]
    expected_b1 = len(edges) - v + graph_comp_count(v, edges)
    assert (b0, b1, b2) == (graph_comp_count(v, edges), expected_b1, 0)
    return tuple(len(C[k]) for k in range(4)), (b0, b1, b2)


def main():
    nc = check_edge_contraction()
    cases = [
        ('edge', 2, [(0, 1)]),
        ('path3', 3, [(0, 1), (1, 2)]),
        ('triangle', 3, [(0, 1), (1, 2), (0, 2)]),
        ('path4', 4, [(0, 1), (1, 2), (2, 3)]),
        ('cycle4', 4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        ('complete4', 4, list(combinations(range(4), 2))),
        ('disjoint_edges', 4, [(0, 1), (2, 3)]),
    ]
    for name, v, edges in cases:
        sizes, betti = check_graph(v, edges)
        print(f'{name}: C0..C3={sizes}, mod2 Betti_0..2={betti}')
    print(f'VERIFY_OK: {len(cases)} graphs, {nc} exact signed single-edge contraction tests')


if __name__ == '__main__':
    main()
