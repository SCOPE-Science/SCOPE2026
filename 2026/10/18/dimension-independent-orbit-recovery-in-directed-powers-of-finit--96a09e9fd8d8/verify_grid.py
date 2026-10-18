#!/usr/bin/env python3
"""Independent explicit directed-cover graph refinement for Cartesian powers of chains.
All computations use exact integers and the Python standard library.
"""
from itertools import product
from collections import Counter, defaultdict
from math import comb, factorial, prod


def run(m, d):
    states = list(product(range(m + 1), repeat=d))
    index = {x: i for i, x in enumerate(states)}
    incoming, outgoing = [], []
    for x in states:
        inc, out = [], []
        for j in range(d):
            y = list(x)
            if x[j]:
                y[j] -= 1
                inc.append(index[tuple(y)])
            if x[j] < m:
                y[j] = x[j] + 1
                out.append(index[tuple(y)])
        incoming.append(inc)
        outgoing.append(out)
    colors = [0] * len(states)
    rounds = (m + 1) // 2
    for _ in range(rounds):
        signatures = []
        for i in range(len(states)):
            down = tuple(sorted(Counter(colors[j] for j in incoming[i]).items()))
            up = tuple(sorted(Counter(colors[j] for j in outgoing[i]).items()))
            signatures.append((colors[i], down, up))
        dictionary = {s: j for j, s in enumerate(sorted(set(signatures)))}
        colors = [dictionary[s] for s in signatures]
    groups = defaultdict(list)
    for x, c in zip(states, colors):
        groups[c].append(x)
    seen_profiles = set()
    for g in groups.values():
        profile = tuple(sorted(Counter(g[0]).items()))
        assert profile not in seen_profiles, (m, d, profile)
        seen_profiles.add(profile)
        assert all(tuple(sorted(Counter(x).items())) == profile for x in g)
        expected = factorial(d)
        for _, mult in profile:
            expected //= factorial(mult)
        assert len(g) == expected, (m, d, profile, len(g), expected)
    assert len(groups) == comb(m + d, d)
    return len(states), len(groups)


def main():
    tested = vertices = 0
    for m in range(1, 10):
        for d in range(1, 7):
            if (m + 1) ** d > 5500:
                continue
            v, _ = run(m, d)
            vertices += v
            tested += 1
    print('EXPLICIT_GRID_REFINEMENT_PASS', 'configurations', tested,
          'vertices_tested', vertices, 'max_vertices_per_instance', 5500)


if __name__ == '__main__':
    main()
