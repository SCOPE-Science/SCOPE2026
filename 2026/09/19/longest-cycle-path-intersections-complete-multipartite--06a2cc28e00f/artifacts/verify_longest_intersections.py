#!/usr/bin/env python3
"""Definition-level verification for complete multipartite longest-path/cycle formulas."""

from itertools import combinations
from math import comb


def integer_partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(max_part, 0, -1):
        for rest in integer_partitions(n - first, min(first, n - first)):
            yield (first,) + rest


def graph_from_parts(parts):
    labels = []
    for i, size in enumerate(parts):
        labels.extend([i] * size)
    n = len(labels)
    adj = [[False] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            adj[u][v] = labels[u] != labels[v]
    return labels, adj


def hamilton_path_exists(vertices, adj):
    vertices = tuple(vertices)
    k = len(vertices)
    if k <= 1:
        return True
    states = [set() for _ in range(1 << k)]
    for i in range(k):
        states[1 << i].add(i)
    for mask in range(1 << k):
        for last in tuple(states[mask]):
            u = vertices[last]
            for nxt in range(k):
                if (mask >> nxt) & 1:
                    continue
                if adj[u][vertices[nxt]]:
                    states[mask | (1 << nxt)].add(nxt)
    return bool(states[-1])


def hamilton_cycle_exists(vertices, adj):
    vertices = tuple(vertices)
    k = len(vertices)
    if k < 3:
        return False
    states = [set() for _ in range(1 << k)]
    states[1].add(0)
    for mask in range(1 << k):
        if not (mask & 1):
            continue
        for last in tuple(states[mask]):
            u = vertices[last]
            for nxt in range(1, k):
                if (mask >> nxt) & 1:
                    continue
                if adj[u][vertices[nxt]]:
                    states[mask | (1 << nxt)].add(nxt)
    return any(last != 0 and adj[vertices[last]][vertices[0]]
               for last in states[-1])


def longest_vertex_sets(parts, kind):
    labels, adj = graph_from_parts(parts)
    n = len(labels)
    best = 0
    family = []
    for size in range(1, n + 1):
        for vertices in combinations(range(n), size):
            if kind == "path":
                ok = hamilton_path_exists(vertices, adj)
            else:
                ok = hamilton_cycle_exists(vertices, adj)
            if not ok:
                continue
            if size > best:
                best = size
                family = [frozenset(vertices)]
            elif size == best:
                family.append(frozenset(vertices))
    return labels, best, family


def predicted(parts, kind):
    n = sum(parts)
    M = max(parts)
    q = n - M
    if kind == "cycle":
        if q < 2:
            return None
        if M <= q:
            return n, {n}, None
        low = q + max(0, 2 * q - M)
        return 2 * q, set(range(low, 2 * q + 1)), q
    if M <= q + 1:
        return n, {n}, None
    low = q + max(0, 2 * (q + 1) - M)
    return 2 * q + 1, set(range(low, 2 * q + 2)), q + 1


def main():
    graph_types = 0
    checks = 0
    nonspanning_checks = 0

    for n in range(2, 10):
        for parts in integer_partitions(n):
            if len(parts) < 2:
                continue
            graph_types += 1
            M = max(parts)
            q = n - M

            for kind in ("path", "cycle"):
                if kind == "cycle" and q < 2:
                    continue

                labels, order, family = longest_vertex_sets(parts, kind)
                expected = predicted(parts, kind)
                expected_order, expected_spectrum, chosen_from_big = expected

                if order != expected_order:
                    raise AssertionError((parts, kind, order, expected_order))

                spectrum = {len(A & B) for A in family for B in family}
                if spectrum != expected_spectrum:
                    raise AssertionError((parts, kind, spectrum, expected_spectrum))

                if chosen_from_big is not None:
                    largest_label = labels[0]
                    outside = {v for v, label in enumerate(labels)
                               if label != largest_label}
                    common = set.intersection(*(set(S) for S in family))
                    if common != outside:
                        raise AssertionError((parts, kind, common, outside))
                    if len(family) != comb(M, chosen_from_big):
                        raise AssertionError(
                            (parts, kind, len(family), comb(M, chosen_from_big))
                        )
                    nonspanning_checks += 1

                checks += 1

    print(f"verified graph types: {graph_types}")
    print(f"verified longest-object checks: {checks}")
    print(f"verified nonspanning core/count checks: {nonspanning_checks}")


if __name__ == "__main__":
    main()
