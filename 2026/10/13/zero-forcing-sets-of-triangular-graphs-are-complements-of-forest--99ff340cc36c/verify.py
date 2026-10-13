"""Independent exact and sampled checks for zero forcing on triangular graphs."""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def is_forest_with_isolate(n, edges, white):
    parent = list(range(n))
    degree = [0] * n

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for index, (a, b) in enumerate(edges):
        if not ((white >> index) & 1):
            continue
        degree[a] += 1
        degree[b] += 1
        a_root, b_root = root(a), root(b)
        if a_root == b_root:
            return False
        parent[a_root] = b_root
    return 0 in degree


def actually_zero_forces(adjacency, initial_black):
    total = (1 << len(adjacency)) - 1
    white = total ^ initial_black
    while white:
        changed = False
        for index, neighbors in enumerate(adjacency):
            if not ((white >> index) & 1):
                remaining = neighbors & white
                if remaining and (remaining & (remaining - 1) == 0):
                    white ^= remaining
                    changed = True
                    break
        if not changed:
            return False
    return True


def forest_polynomials(max_n):
    # Coefficient index is the number of selected (white) edges.
    forests = [[1]]
    for n in range(1, max_n + 1):
        arr = [0] * n
        for k in range(1, n + 1):
            trees = 1 if k == 1 else k ** (k - 2)
            multiplier = comb(n - 1, k - 1) * trees
            for i, coefficient in enumerate(forests[n - k]):
                arr[k - 1 + i] += multiplier * coefficient
        forests.append(arr)
    isolated = []
    for n in range(max_n + 1):
        arr = [0] * max(1, n)
        for j in range(1, n + 1):
            sign = 1 if j % 2 else -1
            for i, coefficient in enumerate(forests[n - j]):
                arr[i] += sign * comb(n, j) * coefficient
        isolated.append(arr)
    return isolated


def test_case(n, sample=None):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    total = (1 << m) - 1
    adjacency = [0] * m
    for i, (a, b) in enumerate(edges):
        adjacency[i] = sum(
            1 << j
            for j, (c, d) in enumerate(edges)
            if j != i and (a == c or a == d or b == c or b == d)
        )
    masks = range(total + 1) if sample is None else (Random(2048 + n).getrandbits(m) for _ in range(sample))
    counts = Counter()
    trials = 0
    for white in masks:
        expect = is_forest_with_isolate(n, edges, white)
        observed = actually_zero_forces(adjacency, total ^ white)
        assert observed == expect, (n, white, observed, expect)
        if expect and sample is None:
            counts[white.bit_count()] += 1
        trials += 1
    return trials, counts


def main():
    isolated = forest_polynomials(16)
    checked = 0
    for n in range(2, 7):
        trials, observed = test_case(n)
        checked += trials
        for k, predicted in enumerate(isolated[n]):
            assert observed[k] == predicted, (n, k, observed[k], predicted)
        assert all(k < len(isolated[n]) for k in observed)
        assert isolated[n][n - 2] == (1 if n == 2 else n * (n - 1) ** (n - 3))
        assert sum(isolated[n]) == sum(observed.values())
        print('exhaustive', n, 'subsets', trials, 'white_edge_counts', isolated[n])
    for n in range(7, 12):
        trials, _ = test_case(n, sample=4096)
        checked += trials
        assert isolated[n][n - 2] == n * (n - 1) ** (n - 3)
        assert all(x == 0 for x in isolated[n][n - 1:])
        print('randomized', n, 'subsets', trials, 'maximum_white_edges', n - 2)
    for n in range(2, 17):
        assert isolated[n][0] == 1
        assert isolated[n][1] == (0 if n == 2 else comb(n, 2))
        assert isolated[n][n-2] == (1 if n==2 else n*(n-1)**(n-3))
        assert all(x >= 0 for x in isolated[n])
    print('PASS checked_initial_sets', checked, 'recurrence_range', '2..16')


if __name__ == '__main__':
    main()
