#!/usr/bin/env python3
"""Exact enumeration for the centered Euclidean inball of clique-windmill root polytopes.

Standard library only. For each pair, enumerate every vertex of the polar
using its product-of-clique decomposition and compare maximizers, norm and
contact span with the formula. This is finite corroboration, not a proof
of the infinite parameter family.
"""
from fractions import Fraction
from itertools import product
from math import comb


def clique_states(q):
    # All nonzero binary choices of q leaves, with one common sign.
    for mask in range(1, 1 << q):
        plus = tuple(int(bool(mask & (1 << j))) for j in range(q))
        yield plus
        yield tuple(-v for v in plus)


def norm2(x):
    # The hub has potential 0; intrinsic coordinates are mean-centered.
    n = len(x) + 1
    return Fraction(n * sum(v * v for v in x) - sum(x) ** 2, n)


def rank_rational(rows):
    if not rows:
        return 0
    a = [[Fraction(v) for v in row] for row in rows]
    k = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(k, len(a)) if a[i][j] != 0), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        z = a[k][j]
        a[k] = [v / z for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                c = a[i][j]
                a[i] = [v - c * w for v, w in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def verify(m, q):
    n = m * q + 1
    states = list(clique_states(q))
    maximum = Fraction(-1)
    maximizers = []
    for blocks in product(states, repeat=m):
        x = sum(blocks, ())
        v = norm2(x)
        if v > maximum:
            maximum, maximizers = v, [x]
        elif v == maximum:
            maximizers.append(x)
    expected_norm = Fraction(m * q * n - (m % 2) * q * q, n)
    expected_count = comb(m, m // 2) * (2 if m % 2 else 1)
    assert maximum == expected_norm, (m, q, maximum, expected_norm)
    assert len(maximizers) == expected_count, (m, q, len(maximizers), expected_count)
    for x in maximizers:
        assert all(len(set(x[i*q:(i+1)*q])) == 1 for i in range(m))
        assert abs(sum(x)) == (m % 2) * q
    # Rows are contact normals in coordinates given by leaf-minus-hub
    # differences; removing the mean does not change their span.
    contact_rank = rank_rational(maximizers)
    expected_rank = m if m % 2 else m - 1
    assert contact_rank == expected_rank, (m, q, contact_rank, expected_rank)
    center_dim = m*q - contact_rank
    assert center_dim == m*(q-1)+(1 if m % 2 == 0 else 0)
    return len(states)**m, expected_count, maximum, center_dim


def direct_facet_check(m, q):
    # Independent tight-constraint rank criterion from the whole graph,
    # enumerating ALL integer feasible potential assignments.
    E = [(0, i + 1) for i in range(m*q)]
    for b in range(m):
        I = range(1 + b*q, 1 + (b+1)*q)
        E += [(i,j) for i in I for j in I if i<j]
    actual = set()
    for x in product((-1,0,1), repeat=m*q):
        z = (0,) + x
        if any(abs(z[i]-z[j]) > 1 for i,j in E):
            continue
        # Equality rows span the zero-hub potential space exactly when
        # their edge graph is connected.
        neigh = [[] for _ in range(m*q+1)]
        for i,j in E:
            if abs(z[i]-z[j]) == 1:
                neigh[i].append(j)
                neigh[j].append(i)
        seen = {0}
        queue = [0]
        for i in queue:
            for j in neigh[i]:
                if j not in seen:
                    seen.add(j)
                    queue.append(j)
        if len(seen)==m*q+1:
            actual.add(x)
    expected={sum(blocks,()) for blocks in product(list(clique_states(q)),repeat=m)}
    assert actual==expected, (m,q,len(actual),len(expected))
    return len(actual)


def main():
    tested = [(m,q) for m in range(2,7) for q in range(1,3)]
    tested += [(2,3), (3,3), (4,3), (2,4), (3,4), (7,1), (8,1), (9,1)]
    checked = 0
    vertices = 0
    for m,q in tested:
        total, contacts, squared_radius, center_dim = verify(m,q)
        vertices += total
        checked += 1
        print(f'm={m} q={q} polar_vertices={total} contacts={contacts} '
              f'polar_R2={squared_radius} inball_center_dim={center_dim}')
    for m,q in [(2,1),(2,2),(2,3),(3,2),(4,2)]:
        got=direct_facet_check(m,q)
        print(f'direct_facet_check m={m} q={q} vertices={got}')
    print(f'ALL_EXACT_CHECKS_PASSED cases={checked} polar_vertices={vertices} direct_facets=5')


if __name__ == '__main__':
    main()
