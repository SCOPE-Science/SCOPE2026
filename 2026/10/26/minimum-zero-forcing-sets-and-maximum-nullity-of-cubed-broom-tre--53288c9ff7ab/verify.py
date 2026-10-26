"""Separate finite checks for zero-forcing sets of cubed broom trees.

Run with Python 3, standard library only: python verify.py
The checker constructs the tree and its third power by BFS, then tests
individual color-change moves; no theorem formula is used in the graph builder.
"""
from collections import deque
from itertools import combinations


def broom_cube(t, ell):
    n = t + ell + 1
    edges = [set() for _ in range(n)]
    for a in range(t):
        edges[a].add(t)
        edges[t].add(a)
    for j in range(ell):
        u, v = t + j, t + j + 1
        edges[u].add(v)
        edges[v].add(u)
    out = [0] * n
    for start in range(n):
        q = deque([(start, 0)])
        seen = {start}
        while q:
            v, d = q.popleft()
            if d == 3:
                continue
            for w in edges[v]:
                if w not in seen:
                    seen.add(w)
                    q.append((w, d + 1))
                    out[start] |= 1 << w
    return out


def can_force(adjacencies, initial):
    n = len(adjacencies)
    colored = sum(1 << x for x in initial)
    full = (1 << n) - 1
    while colored != full:
        move = None
        for v in range(n):
            if colored & (1 << v):
                whites = adjacencies[v] & (full ^ colored)
                if whites and (whites & (whites - 1)) == 0:
                    move = whites
                    break
        if move is None:
            return False
        colored |= move
    return True


def predicted_sets(t, ell):
    leaves = set(range(t))
    path = lambda indices: {t + j for j in indices}
    output = {frozenset(leaves | path(pair)) for pair in combinations(range(3), 2)}
    for absent in range(t):
        base = leaves - {absent}
        output.add(frozenset(base | path(range(3))))
        if ell >= 3:
            for pair in combinations(range(ell - 3, ell), 2):
                output.add(frozenset(base | path((*pair, ell))))
    return output


def gram_support(t, ell):
    dim = ell - 1
    n = t + ell + 1
    vectors = []
    for u in range(n):
        i = 0 if u < t else (u - t + 1)
        coords = {j for j in range(max(0, i - 3), min(i, dim - 1) + 1)}
        vectors.append(coords)
    return [sum(1 << v for v in range(n) if u != v and vectors[u] & vectors[v]) for u in range(n)], vectors


def rank_of_integer_vectors(vecs, d):
    from fractions import Fraction
    rows = [[Fraction(int(j in vecs[i])) for i in range(len(vecs))] for j in range(d)]
    r = 0
    for col in range(len(vecs)):
        pivot = next((i for i in range(r, d) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        x = rows[r][col]
        rows[r] = [a / x for a in rows[r]]
        for i in range(d):
            if i != r and rows[i][col]:
                x = rows[i][col]
                rows[i] = [a - x * b for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == d:
            break
    return r


def run():
    checked = 0
    graph_checks = 0
    gram_checks = 0
    for t in range(2, 6):
        for ell in range(2, 10):
            n = t + ell + 1
            adj = broom_cube(t, ell)
            expect = predicted_sets(t, ell)
            got = {frozenset(s) for s in combinations(range(n), t + 2) if can_force(adj, s)}
            assert got == expect, (t, ell, got - expect, expect - got)
            assert len(got) == (t + 3 if ell == 2 else 4 * t + 3)
            assert all(not can_force(adj, s) for s in combinations(range(n), t + 1))
            checked += 1
            g_support, vectors = gram_support(t, ell)
            assert g_support == adj, (t, ell, 'Gram support differs')
            assert rank_of_integer_vectors(vectors, ell - 1) == ell - 1
            gram_checks += 1
            graph_checks += 1
    print('BROOM_CUBE_VERIFY_OK')
    print('full_minimum_set_classification_cases:', checked)
    print('graph_support_checks:', graph_checks)
    print('psd_gram_rank_checks:', gram_checks)
    print('parameters: t=2..5, ell=2..9')


if __name__ == '__main__':
    run()
