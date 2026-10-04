#!/usr/bin/env python3
from collections import Counter
from math import comb


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def brute(part_sizes):
    part_of = []
    for i, size in enumerate(part_sizes):
        part_of.extend([i] * size)
    n = len(part_of)
    adjacency = [[part_of[u] != part_of[v] for v in range(n)] for u in range(n)]
    counts = Counter()
    maximum = 0
    for mask in range(1 << n):
        chosen = [v for v in range(n) if (mask >> v) & 1]
        if any(adjacency[u][v] for j, u in enumerate(chosen) for v in chosen[j + 1:]):
            continue
        chosen_set = set(chosen)
        ok = True
        for v in range(n):
            if v in chosen_set:
                continue
            seen = sum(adjacency[v][u] for u in chosen)
            if seen != 0 and seen % 2 == 0:
                ok = False
                break
        if ok:
            counts[len(chosen)] += 1
            maximum = max(maximum, len(chosen))
    return counts, maximum


def predicted(part_sizes):
    counts = Counter({0: 1})
    for size in part_sizes:
        for k in range(1, size + 1, 2):
            counts[k] += comb(size, k)
    largest = max(part_sizes)
    maximum = largest if largest % 2 else largest - 1
    return counts, maximum


def main():
    types = 0
    subsets = 0
    for n in range(2, 12):
        for part_sizes in partitions(n):
            if len(part_sizes) < 2:
                continue
            observed_counts, observed_max = brute(part_sizes)
            expected_counts, expected_max = predicted(part_sizes)
            assert observed_counts == expected_counts, (part_sizes, observed_counts, expected_counts)
            assert observed_max == expected_max, (part_sizes, observed_max, expected_max)
            types += 1
            subsets += 1 << n
    print(f"ALL CHECKS PASSED; multipartite_types={types}; subsets={subsets}; max_order=11")


if __name__ == "__main__":
    main()
