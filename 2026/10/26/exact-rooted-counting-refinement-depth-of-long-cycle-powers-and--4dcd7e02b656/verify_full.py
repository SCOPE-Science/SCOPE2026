#!/usr/bin/env python3
"""Standalone direct adjacency-based color-refinement verification.

Inputs are all integral and the script uses only Python's standard library.
"""
from collections import Counter


def all_rounds(n, k):
    adjacency = [tuple((v + delta) % n for delta in range(-k, k + 1)
                       if delta != 0) for v in range(n)]
    colours = [1 if v == 0 else 0 for v in range(n)]
    yield colours
    while True:
        signatures = [(colours[v], tuple(sorted(Counter(colours[w] for w in adjacency[v]).items())))
                      for v in range(n)]
        palette = {x: c for c, x in enumerate(sorted(set(signatures)))}
        new = [palette[x] for x in signatures]
        if len(set(new)) == len(set(colours)):
            break
        yield new
        colours = new


def profile(n, k, iteration, v):
    j = min(v, n - v)
    if iteration == 0:
        return ('root',) if j == 0 else ('other',)
    if iteration == 1:
        return ('root',) if j == 0 else ('near',) if j <= k else ('far',)
    return ('d', j) if j <= iteration * k else ('tail',)


def check(n, k, expected_rounds, predicted_intermediates=True):
    rounds = list(all_rounds(n, k))
    assert len(rounds) - 1 == expected_rounds, (n, k, 'rounds', len(rounds) - 1, expected_rounds)
    for iteration, colours in enumerate(rounds):
        if predicted_intermediates:
            actual_to_expected, expected_to_actual = {}, {}
            for v, colour in enumerate(colours):
                p = profile(n, k, iteration, v)
                assert actual_to_expected.setdefault(colour, p) == p, (n, k, iteration, v, 'too coarse')
                assert expected_to_actual.setdefault(p, colour) == colour, (n, k, iteration, v, 'too fine')
        if iteration == expected_rounds:
            assert len(set(colours)) == n // 2 + 1, (n, k, 'stable class count')
            assert all(colours[v] == colours[(-v) % n] for v in range(n))
    return sum(len(a) for a in rounds)


def main():
    cases = total_round_vertices = 0
    for k in range(1, 13):
        for n in range(4 * k + 1, min(4 * k + 71, 136)):
            d = n // 2
            expected = (d - 2) // k + 1
            total_round_vertices += check(n, k, expected)
            cases += 1
    boundary_cases = 0
    for k in range(2, 31):
        check(4 * k, k, 3, False)
        boundary_cases += 1
    print(f'full_graph_main_cases={cases}')
    print(f'full_graph_boundary_cases={boundary_cases}')
    print(f'vertex_round_instances={total_round_vertices}')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
