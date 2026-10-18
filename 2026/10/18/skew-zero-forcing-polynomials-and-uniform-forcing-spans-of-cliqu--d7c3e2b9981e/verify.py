#!/usr/bin/env python3
"""Exhaustive checks for the skew-forcing enumerator of clique bouquets.

Uses the graph adjacency rule to compute skew zero forcing by saturation;
no characterization is used in that simulation.
"""
from collections import Counter
from itertools import product
from math import comb, prod


def graph(sizes):
    groups = []
    next_vertex = 1
    for size in sizes:
        groups.append(tuple(range(next_vertex, next_vertex + size)))
        next_vertex += size
    adjacency = []
    for vertex in range(next_vertex):
        if vertex == 0:
            neighbors = range(1, next_vertex)
        else:
            neighbors = [0] + [other for group in groups if vertex in group
                               for other in group if other != vertex]
        adjacency.append(sum(1 << other for other in neighbors))
    return adjacency, groups


def simulated_skew_forcing(adjacency, blue):
    white = ((1 << len(adjacency)) - 1) & ~blue
    while white:
        newly_blue = 0
        for neighbors in adjacency:
            possible = neighbors & white
            if possible and not (possible & (possible - 1)):
                newly_blue |= possible
        if not newly_blue:
            return False
        white &= ~newly_blue
    return True


def proposed_skew_forcing(groups, blue):
    omitted = [sum(not ((blue >> vertex) & 1) for vertex in group)
               for group in groups]
    return (max(omitted) <= 2 and
            (blue & 1 or any(number <= 1 for number in omitted)))


def multiply(left, right):
    out = Counter()
    for degree_a, coefficient_a in left.items():
        for degree_b, coefficient_b in right.items():
            out[degree_a + degree_b] += coefficient_a * coefficient_b
    return out


def polynomial_coefficients(sizes):
    q = Counter({0: 1})
    e = Counter({0: 1})
    for size in sizes:
        q = multiply(q, Counter({size: 1, size - 1: size,
                                 size - 2: comb(size, 2)}))
        e = multiply(e, Counter({size - 2: comb(size, 2)}))
    out = multiply(q, Counter({0: 1, 1: 1}))
    out.subtract(e)
    return {degree: coefficient for degree, coefficient in out.items()
            if coefficient}


def alleged_minimum_data(sizes):
    minimum = sum(size - 2 for size in sizes) + 1
    count = prod(comb(size, 2) for size in sizes)
    count += sum(size * prod(comb(s, 2) for j, s in enumerate(sizes)
                              if j != i)
                 for i, size in enumerate(sizes))
    return minimum, count


def check_all():
    profiles = 0
    tested = 0
    forts_checked = 0
    for number_of_blades in (2, 3, 4):
        for sizes in product(range(2, 6), repeat=number_of_blades):
            if sum(sizes) + 1 > 14:
                continue
            adjacency, groups = graph(sizes)
            n = len(adjacency)
            counts = Counter()
            minimum = n + 1
            max_failed = -1
            minimum_count = 0
            for blue in range(1 << n):
                simulation = simulated_skew_forcing(adjacency, blue)
                criterion = proposed_skew_forcing(groups, blue)
                assert simulation == criterion, (sizes, blue, simulation, criterion)
                size = blue.bit_count()
                if simulation:
                    counts[size] += 1
                    if size < minimum:
                        minimum = size
                        minimum_count = 1
                    elif size == minimum:
                        minimum_count += 1
                else:
                    max_failed = max(max_failed, size)
                tested += 1
            assert dict(counts) == polynomial_coefficients(sizes), sizes
            predicted_minimum, predicted_count = alleged_minimum_data(sizes)
            assert (minimum, minimum_count) == (predicted_minimum, predicted_count), sizes
            assert max_failed == (n - 3 if max(sizes) >= 3 else 0), sizes
            profiles += 1
            if n <= 11:
                all_vertices = (1 << n) - 1
                expected = set()
                for group in groups:
                    for i in range(len(group)):
                        for j in range(i + 1, len(group)):
                            for k in range(j + 1, len(group)):
                                expected.add((1 << group[i]) | (1 << group[j]) | (1 << group[k]))
                for picks in product(*[list(__import__('itertools').combinations(g, 2)) for g in groups]):
                    expected.add(1 | sum((1 << a) | (1 << b) for a, b in picks))
                actual = set()
                for white in range(1, all_vertices + 1):
                    if all((adj & white).bit_count() != 1 for adj in adjacency):
                        if not any(other != white and other & white == other
                                   and all((adj & other).bit_count() != 1 for adj in adjacency)
                                   for other in range(1, white)):
                            actual.add(white)
                    forts_checked += 1
                assert actual == expected, (sizes, len(actual), len(expected))
    print(f'VERIFICATION_OK profiles={profiles} initial_subsets={tested} fort_subsets={forts_checked}')


if __name__ == '__main__':
    check_all()
