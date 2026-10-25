#!/usr/bin/env python3
"""Reproduce the finite-poset example used in the result."""
from itertools import combinations
from fractions import Fraction

BASE_VERTICES = ("a", "b", "c", "d")
BASE_RELATIONS = {( "a", "c"), ("a", "d"), ("b", "c"), ("b", "d")}


def transitive_closure(vertices, strict_edges):
    relation = {(x, x) for x in vertices} | set(strict_edges)
    changed = True
    while changed:
        changed = False
        for x, y in tuple(relation):
            for z, w in tuple(relation):
                if y == z and (x, w) not in relation:
                    relation.add((x, w))
                    changed = True
    return relation


def order_complex(vertices, relation):
    faces = []
    for size in range(1, len(vertices) + 1):
        for face in combinations(vertices, size):
            if all((face[i], face[j]) in relation or (face[j], face[i]) in relation
                   for i in range(size) for j in range(i + 1, size)):
                faces.append(face)
    return faces


def matrix_rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(v) for v in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pivot_value = a[pivot_row][col]
        a[pivot_row] = [v / pivot_value for v in a[pivot_row]]
        for r in range(pivot_row + 1, rows):
            if a[r][col] != 0:
                factor = a[r][col]
                a[r] = [a[r][j] - factor * a[pivot_row][j] for j in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def boundary_matrix(k_faces, lower_faces):
    lower_index = {face: i for i, face in enumerate(lower_faces)}
    matrix = [[0 for _ in k_faces] for _ in lower_faces]
    for j, face in enumerate(k_faces):
        for i in range(len(face)):
            subface = face[:i] + face[i + 1:]
            matrix[lower_index[subface]][j] += (-1) ** i
    return matrix


def invariants(vertices, strict_edges):
    relation = transitive_closure(vertices, strict_edges)
    faces = order_complex(vertices, relation)
    by_dim = {k: [f for f in faces if len(f) == k + 1] for k in range(3)}
    d1 = boundary_matrix(by_dim[1], by_dim[0])
    d2 = boundary_matrix(by_dim[2], by_dim[1])
    rank_d1 = matrix_rank(d1)
    rank_d2 = matrix_rank(d2)
    beta0 = len(by_dim[0]) - rank_d1
    beta1 = len(by_dim[1]) - rank_d1 - rank_d2
    return relation, by_dim, (beta0, beta1)


def minimal_opens(vertices, relation):
    return {x: {y for y in vertices if (y, x) in relation} for x in vertices}


def main():
    vertices = BASE_VERTICES
    edges_p = set(BASE_RELATIONS)
    edges_q = set(BASE_RELATIONS) | {( "a", "b")}
    rel_p, faces_p, betti_p = invariants(vertices, edges_p)
    rel_q, faces_q, betti_q = invariants(vertices, edges_q)

    assert tuple(len(faces_p[k]) for k in range(3)) == (4, 4, 0)
    assert tuple(len(faces_q[k]) for k in range(3)) == (4, 5, 2)
    assert betti_p == (1, 1)
    assert betti_q == (1, 0)

    opens_p = minimal_opens(vertices, rel_p)
    opens_q = minimal_opens(vertices, rel_q)
    differences = {x: opens_p[x] ^ opens_q[x] for x in vertices if opens_p[x] != opens_q[x]}
    assert differences == {"b": {"a"}}

    # Add isolated points: they add singleton minimal opens and do not affect H_1.
    for n in (4, 5, 10, 100):
        all_vertices = tuple(vertices) + tuple(f"p{i}" for i in range(n - 4))
        rel_p_n = transitive_closure(all_vertices, edges_p)
        rel_q_n = transitive_closure(all_vertices, edges_q)
        u_p = minimal_opens(all_vertices, rel_p_n)
        u_q = minimal_opens(all_vertices, rel_q_n)
        total_difference = sum(len(u_p[x] ^ u_q[x]) for x in all_vertices)
        assert total_difference == 1
        assert Fraction(total_difference, n * n) == Fraction(1, n * n)

    print("PASS: P has f-vector (4, 4, 0) and beta_1=1.")
    print("PASS: P+ has f-vector (4, 5, 2) and beta_1=0.")
    print("PASS: exactly one minimal open changes by one point.")
    print("PASS: normalized discrepancy equals 1/N^2 for N=4,5,10,100.")
    print("Integral H_1 follows from the explicit cycle and disk descriptions in the proof.")


if __name__ == "__main__":
    main()
