#!/usr/bin/env python3
"""Independent graph-distance and Walsh-block checks for subdivided cubes.

Uses unweighted graph breadth-first search for all distances; checks the closed
forms against independently constructed adjacency. Walsh block identities are
verified as exact integer matrix equalities. Finite cases support, but do not
replace, the arbitrary-dimension proof in RESULT.md.
"""
from collections import deque
from itertools import combinations
from math import sqrt
import numpy as np


def construct(d):
    vertices = [('v', x, -1) for x in range(1 << d)]
    edges = [('e', x, i) for i in range(d) for x in range(1 << d) if (x & (1 << i)) == 0]
    labels = vertices + edges
    index = {z: j for j, z in enumerate(labels)}
    adjacency = [[] for _ in labels]
    for j, (_, x, i) in enumerate(edges, len(vertices)):
        for endpoint in (x, x | (1 << i)):
            q = index[('v', endpoint, -1)]
            adjacency[q].append(j)
            adjacency[j].append(q)
    return labels, adjacency


def formula_dist(u, v):
    tu, x, i = u
    tv, y, j = v
    if tu == 'v' and tv == 'v':
        return 2 * (x ^ y).bit_count()
    if tu == 'e' and tv == 'v':
        return formula_dist(v, u)
    if tu == 'v':
        return 2 * ((x ^ y) & ~(1 << j)).bit_count() + 1
    if i == j and x == y:
        return 0
    return 2 * ((x ^ y) & ~((1 << i) | (1 << j))).bit_count() + 2


def direct_distances(labels, adj):
    n = len(labels)
    result = np.empty((n, n), dtype=np.int64)
    for source in range(n):
        levels = [-1] * n
        levels[source] = 0
        queue = deque([source])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if levels[w] < 0:
                    levels[w] = levels[v] + 1
                    queue.append(w)
        assert min(levels) >= 0
        result[source] = levels
    return result


def all_subsets(d):
    return [sum(1 << i for i in tup) for size in range(d + 1) for tup in combinations(range(d), size)]


def basis(d, labels, mask):
    eligible = [-1] + [i for i in range(d) if not (mask & (1 << i))]
    P = np.zeros((len(labels), len(eligible)), dtype=np.int64)
    for t, direction in enumerate(eligible):
        for j, (kind, x, i) in enumerate(labels):
            if (kind == 'v' and direction == -1) or (kind == 'e' and i == direction):
                P[j, t] = (-1) ** ((x & mask).bit_count() % 2)
    return eligible, P


def expected_block(d, mask, eligible):
    a = 1 << (d - 1)
    C = np.zeros((len(eligible), len(eligible)), dtype=np.int64)
    level = mask.bit_count()
    for t, it in enumerate(eligible):
        for u, iu in enumerate(eligible):
            if level == 0:
                if it == -1:
                    C[t, u] = (2*d*a if iu == -1 else d*a)
                elif iu == -1:
                    C[t, u] = 2*d*a
                else:
                    C[t, u] = ((d+1)*a-2 if it == iu else d*a)
            elif level == 1:
                if it == -1:
                    C[t, u] = (-2*a if iu == -1 else -a)
                elif iu == -1:
                    C[t, u] = -2*a
                else:
                    C[t, u] = (-a-2 if it == iu else -a)
            elif it == iu and it != -1:
                C[t, u] = -2
    return C


def theory_spectrum(d):
    if d == 1:
        return np.array([-2., -2./3., 0.])
    a = 1 << (d-1)
    total = (d+2)*a
    tr = -((d+1)*a+2)
    root = sqrt(tr*tr-16*a)
    eta_plus = (tr+root)/2
    eta_minus = (tr-root)/2
    spec = [0.]*(2**d-d)
    spec += [float(a-2)]*(d-1)
    spec += [float(2*(a-2)/(d+2))]
    spec += [eta_plus]*d + [eta_minus]*d
    spec += [-2.]*(d*a-2*d)
    assert len(spec) == total
    return np.sort(spec)


def theory_uncentered_spectrum(d):
    a = 1 << (d - 1)
    t0 = (d + 1)**2*a - 2
    discriminant = t0*t0 - 8*d*a*(a-2)
    eigen_a = (t0 + sqrt(discriminant))/2
    eigen_b = (t0 - sqrt(discriminant))/2
    if d == 1:
        return np.sort([eigen_a, eigen_b, -2.])
    tr = -((d+1)*a+2)
    root = sqrt(tr*tr-16*a)
    spec = [eigen_a, eigen_b]
    spec += [float(a-2)]*(d-1)
    spec += [(tr+root)/2]*d+[(tr-root)/2]*d
    spec += [-2.]*(d*a-2*d)
    spec += [0.]*(2**d-d-1)
    assert len(spec) == len(construct(d)[0])
    return np.sort(spec)


def inspect_dimension(d):
    labels, adj = construct(d)
    D = direct_distances(labels, adj)
    n = len(labels)
    assert np.array_equal(D, D.T)
    assert np.all(np.diag(D) == 0)
    assert all(int(D[i, j]) == formula_dist(labels[i], labels[j]) for i in range(n) for j in range(n))
    blocks = 0
    for mask in all_subsets(d):
        eligible, P = basis(d, labels, mask)
        C = expected_block(d, mask, eligible)
        assert np.array_equal(D @ P, P @ C), (d, mask)
        assert np.array_equal(P.T @ P, np.diag(np.diag(P.T @ P)))
        blocks += len(eligible)
    assert blocks == n
    actual_full = np.linalg.eigvalsh(D.astype(float))
    expected_full = theory_uncentered_spectrum(d)
    assert np.max(np.abs(actual_full-expected_full)) < 2e-7, (d, actual_full, expected_full)
    J = np.eye(n)-np.ones((n,n))/n
    spectrum = np.linalg.eigvalsh(J@D@J)
    expected = theory_spectrum(d)
    assert np.max(np.abs(spectrum-expected)) < 2e-7, (d, spectrum, expected)
    if d >= 3:
        e0 = next(j for j, z in enumerate(labels) if z == ('e', 0, 0))
        # Directional contrast, exactly: +1 on direction 0, -1 on direction 1.
        c = np.array([int(z[0] == 'e' and z[2] == 0)-int(z[0] == 'e' and z[2] == 1) for z in labels], dtype=np.int64)
        assert int(sum(c)) == 0
        a = 1 << (d-1)
        assert int(c @ D @ c) == 2*a*(a-2)
        assert int(c @ c) == 2*a
    return n, n*n, blocks


def main():
    cases = [inspect_dimension(d) for d in range(1,7)]
    print('SUBDIVIDED_CUBE_EXACT_BLOCKS_AND_BFS_OK')
    print('dimensions=1..6; vertices=', [x[0] for x in cases])
    print('all_pairs_distances_checked=', sum(x[1] for x in cases))
    print('Walsh_basis_dimensions_checked=', sum(x[2] for x in cases))
    print('analytic_eigenvalue_crosschecks=12 (centered and uncentered)')
    print('No finite computation is claimed to certify all dimensions.')


if __name__ == '__main__':
    main()
