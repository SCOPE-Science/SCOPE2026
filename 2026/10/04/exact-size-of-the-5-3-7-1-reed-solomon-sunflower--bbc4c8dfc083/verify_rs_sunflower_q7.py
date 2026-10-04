#!/usr/bin/env python3
from itertools import permutations
from collections import Counter

P = 7
N = 5
K = 3


def inv(a):
    a %= P
    if a == 0:
        raise ZeroDivisionError
    return pow(a, P - 2, P)


def rref(rows):
    A = [[x % P for x in row] for row in rows if any(x % P for x in row)]
    if not A:
        return tuple()
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] % P), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        z = inv(A[r][c])
        A[r] = [(z * x) % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % P:
                z = A[i][c] % P
                A[i] = [(x - z * y) % P for x, y in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return tuple(tuple(row) for row in A if any(row))


def rank(rows):
    return len(rref(rows))


def rs_code(alpha):
    return rref([
        [1] * N,
        list(alpha),
        [(x * x) % P for x in alpha],
    ])


def intersection_dimension(C, D):
    return len(C) + len(D) - rank(list(C) + list(D))


def build_graph():
    # Affine normalization sends the first two distinct evaluation points to 0,1.
    reps = [(0, 1) + tail for tail in permutations(range(2, P), 3)]
    assert len(reps) == 60
    codes = [rs_code(a) for a in reps]
    assert len(set(codes)) == 60

    # Independent exhaustiveness check: all ordered 5-tuples of distinct elements
    # collapse to these same 60 row spaces.
    all_codes = {rs_code(a) for a in permutations(range(P), N)}
    assert set(codes) == all_codes

    adj = [0] * len(codes)
    dims = Counter()
    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            d = intersection_dimension(codes[i], codes[j])
            dims[d] += 1
            if d == 1:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    assert dims == Counter({1: 1200, 2: 570})
    assert {x.bit_count() for x in adj} == {40}
    return reps, codes, adj


def bron_kerbosch_histogram(adj):
    # Enumerates every maximal clique exactly once using a standard pivot rule.
    hist = Counter()
    max_clique = []

    def rec(R, Pset, Xset):
        nonlocal max_clique
        if Pset == 0 and Xset == 0:
            hist[len(R)] += 1
            if len(R) > len(max_clique):
                max_clique = R[:]
            return
        union = Pset | Xset
        if union:
            candidates_u = [i for i in range(len(adj)) if (union >> i) & 1]
            u = max(candidates_u, key=lambda z: (Pset & adj[z]).bit_count())
            candidates = Pset & ~adj[u]
        else:
            candidates = Pset
        while candidates:
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            rec(R + [v], Pset & adj[v], Xset & adj[v])
            Pset &= ~bit
            Xset |= bit
            candidates &= ~bit

    rec([], (1 << len(adj)) - 1, 0)
    return hist, max_clique


def greedy_coloring_bound_order(Pset, adj):
    # Partition the current candidate graph greedily into independent color classes.
    # The color number attached to a vertex bounds the clique size in the prefix.
    vertices, bounds = [], []
    color = 0
    U = Pset
    while U:
        color += 1
        Q = U
        while Q:
            bit = Q & -Q
            v = bit.bit_length() - 1
            vertices.append(v)
            bounds.append(color)
            U &= ~bit
            Q &= ~bit
            Q &= ~adj[v]
    return vertices, bounds


def branch_and_bound_max(adj):
    best = []
    def expand(R, Pset):
        nonlocal best
        if not Pset:
            if len(R) > len(best):
                best = R[:]
            return
        vertices, bounds = greedy_coloring_bound_order(Pset, adj)
        for idx in range(len(vertices) - 1, -1, -1):
            if len(R) + bounds[idx] <= len(best):
                return
            v = vertices[idx]
            if not ((Pset >> v) & 1):
                continue
            expand(R + [v], Pset & adj[v])
            Pset &= ~(1 << v)
    expand([], (1 << len(adj)) - 1)
    return best


def main():
    reps, codes, adj = build_graph()

    witness = [
        (0, 1, 6, 5, 4),
        (0, 1, 6, 4, 3),
        (0, 1, 5, 3, 4),
        (0, 1, 6, 3, 5),
        (0, 1, 5, 6, 2),
        (0, 1, 5, 2, 3),
        (0, 1, 4, 2, 5),
        (0, 1, 3, 2, 4),
        (0, 1, 2, 6, 4),
        (0, 1, 2, 3, 6),
    ]
    index = {a: i for i, a in enumerate(reps)}
    W = [index[a] for a in witness]
    assert all((adj[i] >> j) & 1 for x, i in enumerate(W) for j in W[x + 1:])

    hist, bk_best = bron_kerbosch_histogram(adj)
    assert hist == Counter({6: 30, 7: 1920, 8: 5070, 9: 1800, 10: 138})
    assert len(bk_best) == 10

    bb_best = branch_and_bound_max(adj)
    assert len(bb_best) == 10

    print('distinct_codes=60')
    print('intersection_pairs_dim1=1200 dim2=570')
    print('compatibility_graph_degree=40')
    print('maximal_clique_histogram=' + repr(dict(sorted(hist.items()))))
    print('maximum_sunflower_size=10')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
