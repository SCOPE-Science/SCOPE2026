#!/usr/bin/env python3
"""Independent finite graph checks for three-sum incidence cycle-rank law.

The unbounded theorem is proved mathematically; these checks test boundary cases.
"""
from itertools import combinations
from math import gcd


def graph_nullity(sums):
    high = max(sums)
    count_vertices = 2 * (high + 1)
    parent = list(range(count_vertices))
    components = count_vertices
    edge_count = 0

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for summand in sorted(sums):
        for left in range(summand + 1):
            right = high + 1 + summand - left
            edge_count += 1
            u, v = find(left), find(right)
            if u != v:
                parent[u] = v
                components -= 1
    return edge_count - count_vertices + components


def formula(a, b, c):
    delta = c - b
    return max(0, a + 1 - delta + gcd(b - a, delta))


def main():
    tests = 0
    for c in range(2, 45):
        for a, b in combinations(range(c), 2):
            observed = graph_nullity((a, b, c))
            predicted = formula(a, b, c)
            assert observed == predicted, (a, b, c, observed, predicted)
            tests += 1
    print(f"three-sum exhaustive triples through c=44: {tests} PASS")

    for a,b,c in ((0,6,10), (1,2,4), (0,1,2), (2,5,9), (3,7,14), (1,6,14)):
        print(f"triple {(a,b,c)}: beta={graph_nullity((a,b,c))}; formula={formula(a,b,c)}")

    # Exact stability of forestness when each new sum exceeds twice the prior maximum.
    extend_checks = 0
    for c in range(2, 24):
        for a,b in combinations(range(c),2):
            if formula(a,b,c) != 0:
                continue
            previous = (a,b,c)
            for _ in range(3):
                new = 2 * max(previous) + 1
                previous = (*previous,new)
                assert graph_nullity(previous) == 0, previous
                extend_checks += 1
    print(f"finite forest-extension tests: {extend_checks} PASS")
    print("ALL CHECKS PASS")

if __name__ == '__main__':
    main()
