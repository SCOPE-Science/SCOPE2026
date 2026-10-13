#!/usr/bin/env python3
from math import comb


def adjacency(n):
    adj = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n + j)
                adj[n + j].add(i)
    return adj


def zero_forcing(adj, selected):
    blue = set(selected)
    while True:
        forced = None
        for u in tuple(blue):
            white = adj[u] - blue
            if len(white) == 1:
                forced = next(iter(white))
                break
        if forced is None:
            return len(blue) == len(adj)
        blue.add(forced)


def criterion(n, selected):
    I = {i for i in range(n) if i not in selected}
    J = {j for j in range(n) if n + j not in selected}
    p, q = len(I), len(J)
    return p <= 2 and q <= 2 and not (p == q == 2 and I == J)


def predicted_counts(n):
    counts = {}
    for p in range(3):
        for q in range(3):
            degree = 2 * n - p - q
            value = comb(n, p) * comb(n, q)
            if p == 2 and q == 2:
                value -= comb(n, 2)
            counts[degree] = counts.get(degree, 0) + value
    return counts


def main():
    subset_checks = 0
    criterion_checks = 0
    coefficient_checks = 0
    minimum_checks = 0
    for n in range(3, 10):
        adj = adjacency(n)
        actual = {}
        for mask in range(1 << (2 * n)):
            selected = {v for v in range(2 * n) if (mask >> v) & 1}
            z = zero_forcing(adj, selected)
            c = criterion(n, selected)
            subset_checks += 1
            criterion_checks += 1
            if z != c:
                raise AssertionError((n, mask, z, c))
            if z:
                actual[len(selected)] = actual.get(len(selected), 0) + 1
        predicted = predicted_counts(n)
        degrees = set(actual) | set(predicted)
        for degree in degrees:
            coefficient_checks += 1
            if actual.get(degree, 0) != predicted.get(degree, 0):
                raise AssertionError((n, degree, actual, predicted))
        minimum_checks += 2
        zmin = min(actual)
        if zmin != 2 * n - 4:
            raise AssertionError((n, zmin))
        expected_bases = comb(n, 2) * (comb(n, 2) - 1)
        if actual[zmin] != expected_bases:
            raise AssertionError((n, actual[zmin], expected_bases))
    print(
        'VERIFY_OK '
        'n_range=3..9 '
        f'subset_checks={subset_checks} '
        f'criterion_checks={criterion_checks} '
        f'coefficient_checks={coefficient_checks} '
        f'minimum_checks={minimum_checks} '
        'max_order=18'
    )


if __name__ == '__main__':
    main()
