"""Standalone small-graph verification of the generalized-theta Lights Out formula.

Run with Python 3.10+ as: python verify.py
"""
from itertools import product
from functools import lru_cache


def theta_graph(lengths):
    assert len(lengths) >= 2 and len(lengths) % 2 == 0
    assert all(x >= 2 for x in lengths)
    vertices = 2 + sum(x - 1 for x in lengths)
    adj = [0] * vertices
    next_vertex = 2
    for length in lengths:
        path = [0] + list(range(next_vertex, next_vertex + length - 1)) + [1]
        next_vertex += length - 1
        for a, b in zip(path, path[1:]):
            assert not (adj[a] >> b) & 1
            adj[a] |= 1 << b
            adj[b] |= 1 << a
    assert next_vertex == vertices
    assert all(x.bit_count() % 2 == 0 for x in adj)
    return adj


def gf2_nullity(adj):
    n = len(adj)
    rows = [x | (1 << i) for i, x in enumerate(adj)]
    rank = 0
    for col in range(n):
        pivot = next((j for j in range(rank, n) if (rows[j] >> col) & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for j in range(n):
            if j != rank and (rows[j] >> col) & 1:
                rows[j] ^= rows[rank]
        rank += 1
    return n - rank


def prediction(lengths):
    t0 = sum(l % 3 == 0 for l in lengths)
    t1 = sum(l % 3 == 1 for l in lengths)
    if t0 == 0:
        return 2 if t1 % 2 else 0
    return t0 if t0 % 2 == 0 else t0 - 1


def matching_parity(adj):
    n = len(adj)
    @lru_cache(None)
    def f(mask):
        if mask == 0:
            return 1
        vertex = (mask & -mask).bit_length() - 1
        rem = mask & ~(1 << vertex)
        ans = f(rem)
        neighbors = adj[vertex] & rem
        while neighbors:
            t = neighbors & -neighbors
            neighbors ^= t
            ans ^= f(rem ^ t)
        return ans
    return f((1 << n) - 1)


def simulate_kernel_all(adj):
    n = len(adj)
    masks = [adj[v] | (1 << v) for v in range(n)]
    count = 0
    for x in range(1 << n):
        if all(((x & mask).bit_count() % 2) == 0 for mask in masks):
            count += 1
    return count


def main():
    checks = 0
    for number, upper in [(2, 12), (4, 7), (6, 5), (8, 4)]:
        subtotal = 0
        for lengths in product(range(2, upper + 1), repeat=number):
            actual = gf2_nullity(theta_graph(lengths))
            assert actual == prediction(lengths), (lengths, actual, prediction(lengths))
            checks += 1
            subtotal += 1
        print('GF2_ELIMINATION_ALL_LABELLED_PATH_LENGTH_VECTORS_OK', number, upper, subtotal)

    count_matchings = 0
    for number, upper in [(2, 9), (4, 4)]:
        for lengths in product(range(2, upper + 1), repeat=number):
            graph = theta_graph(lengths)
            if len(graph) > 15:
                continue
            parity = matching_parity(graph)
            assert parity == (1 if prediction(lengths) == 0 else 0), (lengths, parity)
            count_matchings += 1
    print('SEPARATE_MATCHING_PARITY_RECURRENCE_OK', count_matchings)

    count_direct = 0
    for number, upper in [(2, 6), (4, 3)]:
        for lengths in product(range(2, upper + 1), repeat=number):
            graph = theta_graph(lengths)
            if len(graph) > 12:
                continue
            solutions = simulate_kernel_all(graph)
            assert solutions == 2 ** prediction(lengths), (lengths, solutions)
            count_direct += 1
    print('EXHAUSTIVE_BINARY_PRESS_PATTERNS_OK', count_direct)

    for lengths in [(3, 4, 5, 2), (4, 4, 5, 5), (2, 2, 2, 2), (3, 3, 3, 3), (3, 3, 4, 5, 2, 2), (3, 6, 9, 12, 5, 8)]:
        graph = theta_graph(lengths)
        d = gf2_nullity(graph)
        assert d == prediction(lengths)
        print('WITNESS', lengths, 'vertices', len(graph), 'nullity', d, 'solutions', 2 ** d)

    print('VERIFY_OK', checks)


if __name__ == '__main__':
    main()
