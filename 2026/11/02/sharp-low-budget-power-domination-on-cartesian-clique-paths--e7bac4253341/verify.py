#!/usr/bin/env python3
"""Direct finite power-domination tests on Cartesian clique paths."""
from itertools import combinations
from math import comb


def neighbors(n, ell):
    adjacency = []
    for t in range(ell):
        for j in range(n):
            mask = ((((1 << n) - 1) ^ (1 << j)) << (t * n))
            if t > 0:
                mask |= 1 << ((t - 1) * n + j)
            if t + 1 < ell:
                mask |= 1 << ((t + 1) * n + j)
            adjacency.append(mask)
    return adjacency


def power_dominates(initial, adjacency):
    count = len(adjacency)
    observed = initial
    cursor = initial
    while cursor:
        bit = cursor & -cursor
        cursor ^= bit
        observed |= adjacency[bit.bit_length() - 1]
    full = (1 << count) - 1
    while True:
        forced = 0
        for vertex, edge_mask in enumerate(adjacency):
            if not (observed & (1 << vertex)):
                continue
            unseen_neighbors = edge_mask & ~observed
            if unseen_neighbors and not (unseen_neighbors & (unseen_neighbors - 1)):
                forced |= unseen_neighbors
        if forced & ~observed == 0:
            return observed == full
        observed |= forced


def occupied_layer_test(selection, n, ell):
    layers = {vertex // n for vertex in selection}
    return (0 in layers or ell - 1 in layers or
            any(t + 1 in layers for t in layers))


def path_independent_count(vertices, j):
    if j < 0 or 2 * j > vertices + 1:
        return 0
    return comb(vertices + 1 - j, j)


def predicted_failure_coefficient(n, ell, k):
    # Choose j nonconsecutive occupied interior layers; every one is nonempty.
    failures = 0
    for j in range((ell - 1) // 2 + 1):
        occupancy_patterns = path_independent_count(ell - 2, j)
        weighted_selections = sum(
            ((-1) ** (j - h)) * comb(j, h) *
            (comb(n * h, k) if k <= n * h else 0)
            for h in range(j + 1)
        )
        failures += occupancy_patterns * weighted_selections
    return failures


def verify():
    examined = 0
    dimensions = 0
    for n in range(3, 7):
        for ell in range(3, 8):
            N = n * ell
            adjacency = neighbors(n, ell)
            for k in range(n - 1):
                successful = 0
                for subset in combinations(range(N), k):
                    mask = sum(1 << vertex for vertex in subset)
                    direct = power_dominates(mask, adjacency)
                    proposed = occupied_layer_test(subset, n, ell)
                    assert direct == proposed, (n, ell, k, subset)
                    successful += direct
                    examined += 1
                failures = predicted_failure_coefficient(n, ell, k)
                assert successful == comb(N, k) - failures, (n, ell, k)
            # At k=n-1 the structural condition fails to capture all solutions.
            witness = tuple(n + j for j in range(n - 1))
            assert not occupied_layer_test(witness, n, ell)
            assert power_dominates(sum(1 << v for v in witness), adjacency)
            dimensions += 1
    print("PASS direct forcing, sharp cutoff and all low-degree coefficients:",
          examined, "subsets across", dimensions, "dimension pairs")


if __name__ == "__main__":
    verify()
