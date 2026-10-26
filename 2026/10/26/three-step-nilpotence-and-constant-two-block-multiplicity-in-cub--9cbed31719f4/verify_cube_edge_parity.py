#!/usr/bin/env python3
"""Exact GF(2) verification for binary edge-neighbour XOR on Q_d.

Uses direct adjacency construction and independent Gaussian elimination.
Does not require third-party packages. It tests finite instances only.
"""

from collections import Counter
from random import Random


def edge_graph_rows(d):
    n = 1 << d
    edges = []
    for u in range(n):
        for bit in range(d):
            if not ((u >> bit) & 1):
                edges.append((u, u ^ (1 << bit)))
    neighbours = [0] * len(edges)
    # Direct pairwise comparison of edge endpoints, not an incidence product.
    for i, e in enumerate(edges):
        for j, f in enumerate(edges):
            if i != j and (e[0] in f or e[1] in f):
                neighbours[i] |= 1 << j
    return neighbours


def mat_vec(rows, vec):
    out = 0
    for i, row in enumerate(rows):
        if (row & vec).bit_count() % 2:
            out |= 1 << i
    return out


def product_rows(rows):
    ans = []
    for mask in rows:
        result = 0
        while mask:
            low = mask & -mask
            result ^= rows[low.bit_length() - 1]
            mask ^= low
        ans.append(result)
    return ans


def matrix_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def hit_time(rows, state):
    for t in range(4):
        if not state:
            return t
        state = mat_vec(rows, state)
    raise AssertionError('state did not vanish in three updates')


def main():
    rng = Random(20261024)
    checked_ranks = 0
    exhaustive_states = 0
    sampled_states = 0
    for d in range(2, 9):
        n = 1 << d
        m = d * n // 2
        a = edge_graph_rows(d)
        assert len(a) == m
        a2 = product_rows(a)
        a3 = product_rows(a2)
        assert a3 == [0] * m
        expected = (m, n - 2, n // 2 - 2, 0)
        observed = (m, matrix_rank(a), matrix_rank(a2), matrix_rank(a3))
        assert observed == expected, (d, observed, expected)
        checked_ranks += 4
        if m <= 12:
            counts = Counter(hit_time(a, state) for state in range(1 << m))
            exhaustive_states += 1 << m
            exact = [1]
            for t in range(1, 4):
                exact.append((1 << (m - expected[t])) - (1 << (m - expected[t-1])))
            assert [counts.get(t, 0) for t in range(4)] == exact
            print(f'd={d} vertices={n} edges={m} ranks={observed} exact_depth_counts={exact}')
        else:
            for _ in range(512):
                state = rng.getrandbits(m)
                step = hit_time(a, state)
                assert 0 <= step <= 3
                sampled_states += 1
            print(f'd={d} vertices={n} edges={m} ranks={observed} sample_trajectories=512')
    # Degenerate one-dimensional boundary: one isolated edge-site.
    assert edge_graph_rows(1) == [0]
    assert hit_time([0], 0) == 0 and hit_time([0], 1) == 1
    print(f'checked_ranks={checked_ranks} exhaustive_states={exhaustive_states} sampled_states={sampled_states}')
    print('CUBE_EDGE_PARITY_VERIFY_OK')


if __name__ == '__main__':
    main()
