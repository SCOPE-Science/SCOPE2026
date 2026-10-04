#!/usr/bin/env python3
from itertools import combinations


def integer_partitions(n, minimum=1):
    if n == 0:
        yield []
        return
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield [first] + rest


def build_graph(parts):
    part_of = []
    for i, size in enumerate(parts):
        part_of.extend([i] * size)
    n = len(part_of)
    adjacency = [[False] * n for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if part_of[u] != part_of[v]:
                adjacency[u][v] = adjacency[v][u] = True
    return adjacency


def shortest_path_vertex_sets_upto_two(adjacency):
    n = len(adjacency)
    paths = {frozenset([v]) for v in range(n)}
    for u in range(n):
        for v in range(u + 1, n):
            if adjacency[u][v]:
                paths.add(frozenset([u, v]))
            else:
                for middle in range(n):
                    if adjacency[u][middle] and adjacency[middle][v]:
                        paths.add(frozenset([u, middle, v]))
    return paths


def direct_omega_3_2(adjacency):
    n = len(adjacency)
    path_triples = {p for p in shortest_path_vertex_sets_upto_two(adjacency) if len(p) == 3}
    for size in range(n, 0, -1):
        for candidate in combinations(range(n), size):
            if all(frozenset(triple) in path_triples for triple in combinations(candidate, 3)):
                return size
    return 0


def direct_gamma_3_2(adjacency):
    n = len(adjacency)
    paths = shortest_path_vertex_sets_upto_two(adjacency)
    for size in range(n + 1):
        for chosen in combinations(range(n), size):
            chosen = set(chosen)
            good = True
            for v in range(n):
                if v in chosen:
                    continue
                if not any(v in path and len(path & chosen) >= 2 for path in paths):
                    good = False
                    break
            if good:
                return size
    raise RuntimeError("No dominating set found")


def formula(parts):
    order = sum(parts)
    number_of_parts = len(parts)
    non_singleton_parts = sum(size >= 2 for size in parts)
    omega = 2 + min(2, non_singleton_parts)
    if non_singleton_parts == 0:
        gamma = order
    elif number_of_parts == 2 or 2 in parts:
        gamma = 2
    else:
        gamma = 3
    return omega, gamma


def main():
    checked = 0
    maximum_order = 10
    for order in range(2, maximum_order + 1):
        for parts in integer_partitions(order):
            if len(parts) < 2:
                continue
            adjacency = build_graph(parts)
            observed = (direct_omega_3_2(adjacency), direct_gamma_3_2(adjacency))
            expected = formula(parts)
            if observed != expected:
                raise AssertionError(f"parts={parts}: observed={observed}, expected={expected}")
            checked += 1
    print(f"ALL CHECKS PASSED; multipartite_types={checked}; max_order={maximum_order}")


if __name__ == "__main__":
    main()
