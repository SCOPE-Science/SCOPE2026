#!/usr/bin/env python3
"""Exhaustive finite-field certificate for ternary rank-three evolution algebras.

Rows of a 3x3 matrix W are the structure constants of the squares.
All computations use integers, exact reduction modulo 3, and standard library.
No database or external library is needed.
"""
from itertools import product, permutations
from collections import Counter, defaultdict
from math import factorial

Q = 3
N = 3
P = tuple(permutations(range(N)))
D = tuple(product((1, 2), repeat=N))
X = tuple(product(range(Q), repeat=N))


def determinant(m):
    a, b, c, d, e, f, g, h, i = m
    return (a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)) % Q


def all_idempotents_direct(m):
    # Direct substitution into the 3 quadratic equations, all 27 vectors.
    return tuple(x for x in X if all(
        sum(m[3*i+j]*x[i]*x[i] for i in range(N)) % Q == x[j]
        for j in range(N)))


def simple_warshall(m):
    reach = [[i == j or m[3*i+j] != 0 for j in range(N)]
             for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return all(all(row) for row in reach)


def transform(m, perm, colsign):
    # Relabel natural-basis vectors and rescale each by a unit in F_3.
    # In F_3 every nonzero scalar squares to 1, hence only column signs.
    return tuple((colsign[j]*m[3*perm[i]+perm[j]]) % Q
                 for i in range(N) for j in range(N))


def count_by_support(m):
    # Different route: x_i^2=1 iff x_i is nonzero in F_3.
    # Each support S gives exactly one candidate x_j=sum_{i in S}m_ij.
    ans = 0
    for mask in range(1, 1 << N):
        t = [sum(m[3*i+j] for i in range(N) if (mask >> i) & 1) % Q
             for j in range(N)]
        if all((t[j] != 0) == bool((mask >> j) & 1) for j in range(N)):
            ans += 1
    return ans


def rank_gauss(m):
    # Independent nonsingularity test using row reduction.
    rows = [list(m[3*i:3*i+3]) for i in range(N)]
    r = 0
    for j in range(N):
        pivot = next((i for i in range(r, N) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = 1 if rows[r][j] == 1 else 2
        rows[r] = [inv*t % Q for t in rows[r]]
        for i in range(N):
            if i != r:
                v = rows[i][j]
                rows[i] = [(rows[i][h]-v*rows[r][h]) % Q for h in range(N)]
        r += 1
    return r


def simple_bfs(m):
    for start in range(N):
        found = {start}
        queue = [start]
        while queue:
            i = queue.pop()
            for j in range(N):
                if m[3*i+j] != 0 and j not in found:
                    found.add(j)
                    queue.append(j)
        if len(found) != N:
            return False
    return True


EXPECTED = {
    "labeled": {0: 3600, 1: 5056, 2: 1800, 3: 600,
                4: 120, 5: 48, 7: 8},
    "simple": {0: 3408, 1: 3256, 2: 768, 3: 72},
    "classes": {0: 78, 1: 111, 2: 40, 3: 15,
                4: 3, 5: 1, 7: 1},
    "simple_classes": {0: 74, 1: 73, 2: 17, 3: 2},
}


def run():
    labeled = Counter()
    simple = Counter()
    class_sum_stabilizers = Counter()
    simple_class_sum_stabilizers = Counter()
    representatives = {}
    matrices = []
    # Route A: brute force in all F_3^9 and all x in F_3^3.
    for m in product(range(Q), repeat=N*N):
        d = determinant(m)
        assert (d != 0) == (rank_gauss(m) == N)
        if d == 0:
            continue
        k = len(all_idempotents_direct(m)) - 1
        assert k == count_by_support(m)
        is_simple = simple_warshall(m)
        assert is_simple == simple_bfs(m)
        labeled[k] += 1
        if is_simple:
            simple[k] += 1
            representatives.setdefault(k, m)
        matrices.append((m, k, is_simple))
    assert len(matrices) == 11232
    assert dict(labeled) == EXPECTED['labeled']
    assert dict(simple) == EXPECTED['simple']

    # Route B: compute each Burnside weight from fixed-group elements,
    # rather than computing orbit representatives or canonicalizing.
    # Stabilizer-weighted orbit count = sum_{matrices} |Stab(m)| / 48.
    for m, k, is_simple in matrices:
        stab = sum(transform(m, p, s) == m for p in P for s in D)
        assert 48 % stab == 0
        class_sum_stabilizers[k] += stab
        if is_simple:
            simple_class_sum_stabilizers[k] += stab
    assert all(v % 48 == 0 for v in class_sum_stabilizers.values())
    assert all(v % 48 == 0 for v in simple_class_sum_stabilizers.values())
    classes = {k: v//48 for k, v in class_sum_stabilizers.items()}
    simple_classes = {k: v//48 for k, v in simple_class_sum_stabilizers.items()}
    assert classes == EXPECTED['classes']
    assert simple_classes == EXPECTED['simple_classes']
    assert sum(classes.values()) == 249
    assert sum(simple_classes.values()) == 166

    # Third independent group-orbit route: disjoint orbits for every matrix.
    unseen = {m for m, _, _ in matrices}
    orbit_by_k = Counter()
    orbit_simple = Counter()
    while unseen:
        m = min(unseen)
        orb = {transform(m, p, s) for p in P for s in D}
        assert orb <= unseen
        k = count_by_support(m)
        simple_flag = simple_bfs(m)
        assert all(count_by_support(z) == k and simple_bfs(z) == simple_flag for z in orb)
        unseen.difference_update(orb)
        orbit_by_k[k] += 1
        if simple_flag:
            orbit_simple[k] += 1
    assert dict(orbit_by_k) == classes
    assert dict(orbit_simple) == simple_classes

    assert sum(k*v for k, v in labeled.items()) == 11232
    assert all(k in range(4) for k in simple)
    assert all(k in representatives for k in range(4))
    print('VERIFY_OK')
    print('labeled', dict(sorted(labeled.items())))
    print('simple', dict(sorted(simple.items())))
    print('classes', dict(sorted(classes.items())))
    print('simple_classes', dict(sorted(simple_classes.items())))
    print('simple_witnesses', {k: list(representatives[k]) for k in range(4)})


if __name__ == '__main__':
    run()
