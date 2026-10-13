#!/usr/bin/env python3
"""Exact finite certificate for two-intersecting four-part integer partitions.

Requires Python 3.9+ standard library only.

The complement of the 2-intersection conflict graph is a compatibility
(graph) clique problem. The search is exact: every branch is considered,
except when a valid greedy-vertex-colouring upper bound proves it cannot
improve the current best clique. This code does not assert a computational
proof of any unbounded parameter range.
"""
from collections import Counter
from functools import lru_cache


def partitions(n, k, low=1):
    """All nondecreasing positive k-tuples of total n, without duplicates."""
    if k == 0:
        if n == 0:
            yield ()
        return
    for a in range(low, n // k + 1):
        for rest in partitions(n - a, k - 1, a):
            yield (a,) + rest


@lru_cache(None)
def p(n, k):
    """Independent partition-number recurrence."""
    if n == 0 and k == 0:
        return 1
    if n <= 0 or k <= 0 or n < k:
        return 0
    return p(n - 1, k - 1) + p(n - k, k)


def common(a, b):
    ca, cb = Counter(a), Counter(b)
    return sum(min(ca[x], cb[x]) for x in ca)


def labels(a):
    """Occurrence-label representation: (value, occurrence index)."""
    multiplicity = Counter(a)
    return frozenset((x, j) for x, m in multiplicity.items()
                     for j in range(1, m + 1))


def compatibility(parts, t=2):
    size = len(parts)
    adj = [0] * size
    for i in range(size):
        for j in range(i):
            c = common(parts[i], parts[j])
            assert c == len(labels(parts[i]) & labels(parts[j]))
            if c >= t:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return adj


def maximum_clique_exact(adjacency):
    """Exact branch-and-bound maximum clique with sound coloring bounds."""
    adj = adjacency
    best, nodes = 0, 0

    def greedy_color_order(remaining):
        order, bounds = [], []
        color_number = 0
        while remaining:
            color_number += 1
            this_color = remaining
            while this_color:
                bit = this_color & -this_color
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(color_number)
                remaining ^= bit
                this_color &= ~(bit | adj[vertex])
        # Each color class has no adjacent vertices. A clique in any
        # prefix of 'order' therefore has size <= its last color number.
        return order, bounds

    def visit(remaining, chosen):
        nonlocal best, nodes
        nodes += 1
        if not remaining:
            best = max(best, chosen)
            return
        if chosen + remaining.bit_count() <= best:
            return
        order, upper = greedy_color_order(remaining)
        for j in range(len(order) - 1, -1, -1):
            if chosen + upper[j] <= best:
                return
            vertex = order[j]
            bit = 1 << vertex
            if remaining & bit:
                visit(remaining & adj[vertex], chosen + 1)
                remaining &= ~bit

    visit((1 << len(adj)) - 1, 0)
    return best, nodes


def brute_force_maximum(adjacency):
    """Independent subset census for very small ambient sets."""
    size = len(adjacency)
    max_size = 0
    for bits in range(1 << size):
        if bits.bit_count() <= max_size:
            continue
        current = bits
        valid = True
        while current:
            bit = current & -current
            v = bit.bit_length() - 1
            current ^= bit
            if current & ~adjacency[v]:
                valid = False
                break
        if valid:
            max_size = bits.bit_count()
    return max_size


def main():
    witness = [(1, 1, 2, 5), (1, 1, 3, 4),
               (1, 2, 2, 4), (1, 2, 3, 3)]
    assert all(sum(row) == 9 for row in witness)
    assert all(common(witness[i], witness[j]) >= 2
               for i in range(4) for j in range(i))
    assert not any(all(Counter(Q) <= Counter(row) for row in witness)
                   for Q in [(a,b) for a in range(1,10)
                             for b in range(a,10)])
    print('n partition_count optimum canonical_star search_nodes')
    for n in range(4, 30):
        parts = list(partitions(n, 4))
        assert len(parts) == p(n, 4)
        assert len(set(parts)) == len(parts)
        adj = compatibility(parts)
        actual, nodes = maximum_clique_exact(adj)
        canonical = (n - 2) // 2
        expected = canonical + (1 if n == 9 else 0)
        assert actual == expected, (n, actual, expected)
        if n <= 13:
            assert brute_force_maximum(adj) == actual
        print(n, len(parts), actual, canonical, nodes)
    assert all((n - 2) // 2 > 13 for n in range(30, 300))
    print('FINITE_CENSUS_COMPLETE n=4..29')
    print('GENERAL_CASE n>=30 uses proved nontrivial-family bound 13')
    print('EXCEPTIONAL_N9_WITNESS', witness)
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
