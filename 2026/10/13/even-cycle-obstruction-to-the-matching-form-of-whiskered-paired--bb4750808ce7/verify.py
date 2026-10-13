#!/usr/bin/env python3
"""Direct finite checks for the whiskered paired-domination/matching correspondence.

No external modules or network access are required. Finite checks corroborate the
all-order combinatorial proof; they do not replace it.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter


def edge_list(n, bits):
    pairs = list(combinations(range(n), 2))
    return [e for j, e in enumerate(pairs) if bits & (1 << j)]


def perfect_matching_count(n, edges, subset):
    neighbors = [0] * n
    for u, v in edges:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u

    @lru_cache(None)
    def rec(mask):
        if mask == 0:
            return 1
        ubit = mask & -mask
        u = ubit.bit_length() - 1
        remaining = mask ^ ubit
        partners = remaining & neighbors[u]
        count = 0
        while partners:
            vbit = partners & -partners
            partners ^= vbit
            count += rec(remaining ^ vbit)
        return count

    return rec(subset)


def independent_paired_poly(n, edges):
    # Vertices 0..n-1 are the original vertices; n..2n-1 their leaves.
    neighbors = [0] * (2 * n)
    for u, v in edges + [(i, n + i) for i in range(n)]:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    all_mask = (1 << (2 * n)) - 1

    @lru_cache(None)
    def perfect(mask):
        if mask == 0:
            return True
        if mask.bit_count() & 1:
            return False
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        choices = rest & neighbors[u]
        while choices:
            vbit = choices & -choices
            choices ^= vbit
            if perfect(rest ^ vbit):
                return True
        return False

    out = Counter()
    checked = 0
    for chosen in range(1 << (2 * n)):
        checked += 1
        if not perfect(chosen):
            continue
        covered = chosen
        rem = chosen
        while rem:
            bit = rem & -rem
            rem ^= bit
            covered |= neighbors[bit.bit_length() - 1]
        if covered == all_mask:
            out[chosen.bit_count()] += 1
    return out, checked


def formula_poly(n, edges):
    paired, matchings, multiple = Counter(), Counter(), False
    for subset in range(1 << n):
        c = perfect_matching_count(n, edges, subset)
        if c:
            degree = 2 * n - subset.bit_count()
            paired[degree] += 1
            matchings[degree] += c
        multiple |= c > 1
    return paired, matchings, multiple


def contains_even_cycle(n, edges):
    neigh = [[] for _ in range(n)]
    for a, b in edges:
        neigh[a].append(b)
        neigh[b].append(a)
    for start in range(n):
        stack = [(start, (start,))]
        while stack:
            u, path = stack.pop()
            for v in neigh[u]:
                if v == start and len(path) >= 4 and len(path) % 2 == 0:
                    return True
                if v not in path and v > start and len(path) < n:
                    stack.append((v, path + (v,)))
    return False


def run():
    graphs = 0
    subsets = 0
    even_cycle_graphs = 0
    strict_differences = 0
    max_n = 5
    for n in range(1, max_n + 1):
        for encoding in range(1 << (n * (n - 1) // 2)):
            edges = edge_list(n, encoding)
            direct, checks = independent_paired_poly(n, edges)
            predicted, weighted_matchings, multiple = formula_poly(n, edges)
            even_cycle = contains_even_cycle(n, edges)
            assert direct == predicted, (n, edges, direct, predicted)
            assert multiple == even_cycle, (n, edges, multiple, even_cycle)
            assert all(weighted_matchings[d] >= direct[d] for d in direct)
            assert (predicted == weighted_matchings) == (not even_cycle)
            graphs += 1
            subsets += checks
            even_cycle_graphs += even_cycle
            strict_differences += (predicted != weighted_matchings)

    for n, ed in [
        (6, [(j, (j + 1) % 6) for j in range(6)]),
        (7, [(j, (j + 1) % 7) for j in range(7)]),
        (6, [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (4, 5)]),
        (7, [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (5, 6)]),
    ]:
        direct, checks = independent_paired_poly(n, ed)
        predicted, weighted, multiple = formula_poly(n, ed)
        assert direct == predicted
        assert multiple == contains_even_cycle(n, ed)
        assert (predicted == weighted) == (not multiple)
        graphs += 1
        subsets += checks
    print('VERIFY_OK graphs=%d subset_checks=%d even_cycle_graphs=%d strict_differences=%d max_order=%d' %
          (graphs, subsets, even_cycle_graphs, strict_differences, 7))


if __name__ == '__main__':
    run()
