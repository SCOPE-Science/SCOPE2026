#!/usr/bin/env python3
"""Reproducible finite checks for 1-WL and stabilizer orbits on marked cubes.

The program compares canonical 1-WL partitions against closed-form stabilizer
orbits, and checks the signature criterion for discreteness. This tests finitely
many instances; it is not a proof of the theorem for all dimensions.
"""
import itertools
import json
import random
from collections import defaultdict


def signatures(d, marks):
    b = marks[0]
    return [tuple(((a >> i) & 1) ^ ((b >> i) & 1)
                  for a in marks[1:]) for i in range(d)]


def orbit_key(d, marks, x):
    sig = signatures(d, marks)
    counts = defaultdict(lambda: [0, 0])
    for i, s in enumerate(sig):
        counts[s][0] += 1
        counts[s][1] += ((x >> i) & 1) ^ ((marks[0] >> i) & 1)
    return tuple(sorted((s, tuple(c)) for s, c in counts.items()))


def refine(d, marks):
    n = 1 << d
    rank = {x: j + 1 for j, x in enumerate(marks)}
    colors = tuple(rank.get(v, 0) for v in range(n))
    for t in range(d + 4):
        patterns = [(colors[v], tuple(sorted(colors[v ^ (1 << i)]
                                                  for i in range(d))))
                    for v in range(n)]
        order = {p: j for j, p in enumerate(sorted(set(patterns)))}
        new = tuple(order[p] for p in patterns)
        if len(set(new)) == len(set(colors)):
            return new, t + 1
        colors = new
    raise AssertionError('Unexpected failure to stabilize')


def test_case(d, marks):
    colors, rounds = refine(d, marks)
    co = {}
    oc = {}
    for x, color in enumerate(colors):
        key = orbit_key(d, marks, x)
        if color in co:
            assert co[color] == key, ('WL under-refines orbits', d, marks, x)
        else:
            co[color] = key
        if key in oc:
            assert oc[key] == color, ('WL over-refines orbits', d, marks, x)
        else:
            oc[key] = color
    sig = signatures(d, marks)
    assert (len(co) == (1 << d)) == (len(set(sig)) == d)
    assert rounds <= d + 1
    expected = 1
    multiplicities = defaultdict(int)
    for t in sig:
        multiplicities[t] += 1
    for m in multiplicities.values():
        expected *= m + 1
    assert len(co) == expected
    return rounds


def main():
    rng = random.Random(1030614)
    cases = 0
    maximal = 0
    # Exhaustive choices of a few individually marked vertices for small cubes.
    for d in range(1, 5):
        for r in range(1, min(4, 1 << d) + 1):
            for marks in itertools.combinations(range(1 << d), r):
                maximal = max(maximal, test_case(d, marks))
                cases += 1
    # Samples with no restrictive pattern on the positions of marked vertices.
    for d in range(5, 11):
        for r in range(1, 7):
            for _ in range(120):
                marks = tuple(rng.sample(range(1 << d), r))
                maximal = max(maximal, test_case(d, marks))
                cases += 1
    # Optimal explicit distinct-column construction.
    opt = {}
    for d in range(1, 15):
        k = 1 + (d - 1).bit_length()
        marks = (0,) + tuple(sum(((i >> j) & 1) << i for i in range(d))
                             for j in range(k - 1))
        if len(set(marks)) != len(marks):
            raise AssertionError(('duplicate marked vertex', d, marks))
        rounds = test_case(d, marks)
        opt[d] = {'min_marks': k, 'rounds': rounds}
        maximal = max(maximal, rounds)
        cases += 1
    print(json.dumps({'status':'PASS', 'tested_cases':cases,
                      'maximum_refinement_rounds':maximal,
                      'exhaustive_dimensions':[1, 2, 3, 4],
                      'random_dimensions':[5, 6, 7, 8, 9, 10],
                      'explicit_dimensions':opt}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
