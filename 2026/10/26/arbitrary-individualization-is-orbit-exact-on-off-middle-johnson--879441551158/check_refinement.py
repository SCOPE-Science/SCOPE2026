#!/usr/bin/env python3
"""Finite checks for colour-refinement orbit recovery in off-middle Johnson graphs.
Science only; this program uses Python standard library and constructs its own graphs.
"""
from itertools import combinations
from collections import Counter, defaultdict
from random import Random
from math import comb


def vertices_and_adjacency(n, k):
    vertices = [sum(1 << x for x in c) for c in combinations(range(n), k)]
    adjacency = [[j for j, y in enumerate(vertices) if (x ^ y).bit_count() == 2]
                 for x in vertices]
    return vertices, adjacency


def refine(adjacency, indices):
    colors = [0] * len(adjacency)
    for i, index in enumerate(indices, 1):
        colors[index] = i
    initial = len(set(colors))
    for step in range(len(colors) + 1):
        signatures = [(colors[i], tuple(sorted(Counter(colors[j] for j in row).items())))
                      for i, row in enumerate(adjacency)]
        mapping = {signature: num for num, signature in enumerate(sorted(set(signatures)))}
        next_colors = [mapping[s] for s in signatures]
        if len(set(next_colors)) == len(set(colors)):
            return colors, step, initial
        colors = next_colors
    raise AssertionError('refinement never stabilized')


def profiles_and_expected_sizes(n, k, vertices, markers):
    atom_sizes = Counter(tuple((marker >> i) & 1 for marker in markers)
                         for i in range(n))
    profiles = []
    sizes = {}
    for x in vertices:
        profile = Counter(tuple((marker >> i) & 1 for marker in markers)
                          for i in range(n) if x & (1 << i))
        key = tuple((atom, profile[atom]) for atom in sorted(atom_sizes))
        profiles.append(key)
        sizes[key] = 1
        for atom, count in key:
            sizes[key] *= comb(atom_sizes[atom], count)
    return profiles, sizes


def test_case(n, k, vertices, adjacency, marker_indices):
    colors, rounds, _ = refine(adjacency, marker_indices)
    markers = [vertices[i] for i in marker_indices]
    profiles, expected = profiles_and_expected_sizes(n, k, vertices, markers)
    class_for_profile = {}
    profile_for_class = {}
    observed_sizes = Counter(colors)
    for color, profile in zip(colors, profiles):
        if profile in class_for_profile:
            assert class_for_profile[profile] == color
        else:
            class_for_profile[profile] = color
        if color in profile_for_class:
            assert profile_for_class[color] == profile
        else:
            profile_for_class[color] = profile
    assert len(class_for_profile) == len(profile_for_class)
    assert rounds <= k + 1, (n, k, marker_indices, rounds)
    for profile, color in class_for_profile.items():
        assert observed_sizes[color] == expected[profile]
    return rounds, len(class_for_profile)


def main():
    rng = Random(20261018)
    families = [(5, 2), (6, 2), (7, 3), (8, 3), (9, 4), (10, 4), (11, 5)]
    done = 0
    by_family = []
    max_rounds = 0
    max_markers = 0
    for n, k in families:
        assert n > 2*k
        vertices, adjacency = vertices_and_adjacency(n, k)
        cases = [()]
        # Structured cases include a sweep over small initial segments and all-one-mark cases.
        cases += [tuple(range(r)) for r in range(1, min(7, len(vertices)) + 1)]
        # Exhaust all one- and two-marker choices for smallest family only.
        if n <= 6:
            cases += [(i,) for i in range(len(vertices))]
            cases += list(combinations(range(len(vertices)), 2))
        # Random marker sets probe nontrivial atom patterns, including many marks.
        for r in range(1, min(8, len(vertices)) + 1):
            repeat = 14 if n <= 9 else 8
            for _ in range(repeat):
                cases.append(tuple(rng.sample(range(len(vertices)), r)))
        # Every vertex individualized in a small case probes the trivial extreme.
        if n == 5:
            cases.append(tuple(range(len(vertices))))
        cases = list(dict.fromkeys(cases))
        for markers in cases:
            rounds, classes = test_case(n, k, vertices, adjacency, markers)
            max_rounds = max(max_rounds, rounds)
            max_markers = max(max_markers, len(markers))
        done += len(cases)
        by_family.append((n, k, len(vertices), len(cases)))
        print('PASS family=(%d,%d), vertices=%d, marker-configurations=%d' % by_family[-1])
    print('ALL_TESTS_PASS cases=%d max_rounds=%d max_markers=%d' % (done, max_rounds, max_markers))


if __name__ == '__main__':
    main()
