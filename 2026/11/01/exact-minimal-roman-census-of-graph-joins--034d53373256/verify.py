#!/usr/bin/env python3
"""Independent finite check of the minimal-Roman join enumerator.

Minimality is checked by trying every strict one-coordinate decrease;
no structural lemmas from the proof are assumed in the direct enumeration.
Only standard-library modules are used.
"""
from collections import Counter
from itertools import product
from random import Random


def graph_edges(n):
    candidates = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(candidates)):
        yield tuple(e for k, e in enumerate(candidates) if mask & (1 << k))


def direct_polynomial(n, edges):
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)

    def feasible(labels):
        return all(labels[v] != 0 or any(labels[w] == 2 for w in neighbors[v])
                   for v in range(n))

    answer = Counter()
    tested = 0
    for labels in product(range(3), repeat=n):
        tested += 1
        if not feasible(labels):
            continue
        minimal = True
        for i, value in enumerate(labels):
            for smaller in range(value):
                reduced = list(labels)
                reduced[i] = smaller
                if feasible(reduced):
                    minimal = False
                    break
            if not minimal:
                break
        if minimal:
            answer[(labels.count(2), sum(labels))] += 1
    return +answer, tested


def actual_join(n, m, left_edges, right_edges):
    return (tuple(left_edges)
            + tuple((n + a, n + b) for a, b in right_edges)
            + tuple((i, n + j) for i in range(n) for j in range(m)))


def summary(n, edges):
    degree = [0] * n
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    isolates = sum(d == 0 for d in degree)
    nonuniversal = sum(d != n - 1 for d in degree)
    return isolates, nonuniversal


def check(n, m, left_edges, right_edges):
    L, count_l = direct_polynomial(n, left_edges)
    R, count_r = direct_polynomial(m, right_edges)
    J, count_j = direct_polynomial(n + m,
                                  actual_join(n, m, left_edges, right_edges))
    a, p = summary(n, left_edges)
    b, q = summary(m, right_edges)
    expect = L + R
    expect[(0, n)] -= 1
    expect[(0, m)] -= 1
    expect[(0, n + m)] += 1
    expect[(1, n + 1)] += a
    expect[(1, m + 1)] += b
    expect[(2, 4)] += p * q
    expect = +expect
    assert J == expect, (n, m, left_edges, right_edges, J, expect)
    return count_j


def main():
    cases = 0
    assignments = 0
    # All labeled graphs on each shore of orders 1, 2, or 3.
    for n in range(1, 4):
        for m in range(1, 4):
            for left in graph_edges(n):
                for right in graph_edges(m):
                    assignments += check(n, m, left, right)
                    cases += 1

    # Independent larger tests, including disconnected graphs and isolates.
    rng = Random(20261030)
    for _ in range(160):
        n, m = rng.choice((3, 4)), rng.choice((2, 3, 4))

        def graph(order):
            return tuple((i, j) for i in range(order)
                         for j in range(i + 1, order) if rng.getrandbits(1))

        assignments += check(n, m, graph(n), graph(m))
        cases += 1
    print('VERIFY_OK join_pairs=%s direct_join_assignments=%s' % (cases, assignments))


if __name__ == '__main__':
    main()
