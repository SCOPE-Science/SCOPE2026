#!/usr/bin/env python3
"""Reproduce finite checks for the two-coordinate flip fixed-locus theorem.

Only Python's standard library is required. This is a finite check, not a proof
for arbitrary dimension; the universal argument is supplied separately.
"""
from itertools import combinations
from math import comb


def graph(d):
    # Orbit vertices (u,w), u in {0,1}, w in {0,1}^d.
    vertices = [(u, w) for u in range(2) for w in range(1 << d)]
    neighbors = [set() for _ in vertices]
    for i, (u, x) in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            v, y = vertices[j]
            delta = (x ^ y).bit_count()
            # Check all four original Hamming distances, not merely
            # the predicted orbit-compatibility graph relation.
            a = (u << 1) | (x << 2)
            b = (v << 1) | (y << 2)
            tr = lambda z: z ^ 0b11
            is_clique = max((p ^ q).bit_count()
                            for p in (a, tr(a)) for q in (b, tr(b))) <= 3
            predicted = delta <= (2 if u != v else 1)
            assert is_clique == predicted
            if is_clique:
                neighbors[i].add(j)
                neighbors[j].add(i)
    return vertices, neighbors


def clique_faces(adj):
    faces = [[]]
    def visit(prefix, possible):
        for k, v in enumerate(possible):
            f = prefix + (v,)
            if len(faces) <= len(f):
                faces.append([])
            faces[len(f)].append(f)
            visit(f, [z for z in possible[k + 1:] if z in adj[v]])
    visit((), list(range(len(adj))))
    return faces


def rank_gf2(columns):
    pivots = {}
    for vector in columns:
        while vector:
            i = vector.bit_length() - 1
            if i not in pivots:
                pivots[i] = vector
                break
            vector ^= pivots[i]
    return len(pivots)


def betti_mod2(faces):
    ranks = [0] * len(faces)
    for k in range(2, len(faces)):
        rows = {f: i for i, f in enumerate(faces[k - 1])}
        cols = []
        for face in faces[k]:
            vector = 0
            for t in range(k):
                vector ^= (1 << rows[face[:t] + face[t + 1:]])
            cols.append(vector)
        ranks[k] = rank_gf2(cols)
    return [len(faces[k + 1]) - ranks[k + 1] - (ranks[k + 2] if k + 2 < len(faces) else 0)
            - (1 if k == 0 else 0) for k in range(len(faces) - 1)]


def all_squares(d):
    for i, j in combinations(range(d), 2):
        mask = (1 << i) | (1 << j)
        for a in range(1 << d):
            if a & mask:
                continue
            yield {a, a ^ (1 << i), a ^ (1 << j), a ^ mask}


def verify(d):
    vertices, edges = graph(d)
    faces = clique_faces(edges)
    assert len(faces) == 5
    squares = list(all_squares(d))
    cube_edges = []
    for w in range(1 << d):
        for i in range(d):
            if not (w & (1 << i)):
                cube_edges.append({w, w ^ (1 << i)})
    # Every orbit simplex has its outside-coordinate support in a square.
    for k in range(1, 5):
        for face in faces[k]:
            support = {vertices[i][1] for i in face}
            assert any(support <= square for square in squares)
    # In each square, induced four-layer complex is a join of two 4-cycles;
    # in each edge, it is one tetrahedron.
    for square in squares:
        inds = {i for i, (u, w) in enumerate(vertices) if w in square}
        local = [f for level in faces[1:] for f in level if set(f) <= inds]
        assert [sum(len(f) == size for f in local) for size in range(1, 5)] == [8, 24, 32, 16]
    for e in cube_edges:
        inds = {i for i, (u, w) in enumerate(vertices) if w in e}
        local = [f for level in faces[1:] for f in level if set(f) <= inds]
        assert [sum(len(f) == size for f in local) for size in range(1, 5)] == [4, 6, 4, 1]
    betti = betti_mod2(faces)
    num_squares = 2 ** (d - 2) * comb(d, 2)
    b2 = (1 << d) - d * (1 << (d - 1)) + num_squares - 1
    assert betti == [0, 0, b2, num_squares]
    print(f'd={d}, n={d + 2}: f={list(map(len, faces[1:]))}, mod2 reduced Betti={betti}, square blocks={num_squares}')


if __name__ == '__main__':
    for d in range(2, 8):
        verify(d)
    print('PASS: exact orbit distances, all-simplex square cover, local blocks, and independent mod-2 homology')
