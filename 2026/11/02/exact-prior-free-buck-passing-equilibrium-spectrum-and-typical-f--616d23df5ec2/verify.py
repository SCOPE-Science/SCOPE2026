"""Exact finite-case verification of a bipartite deterministic buck-passing game.

This program enumerates every pure profile for several small complete bipartite
networks; it evaluates every unilateral change from the original long-run cost
formula, compares the equilibrium structure, and independently counts cycles.
The infinite-family theorem is proved analytically, not by these tests.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial, lgamma, log, exp


def decompose(successor):
    size = len(successor)
    cycle_id = [-1] * size
    height = [-1] * size
    cycles = []
    for origin in range(size):
        if cycle_id[origin] != -1:
            continue
        trail, seen = [], {}
        vertex = origin
        while cycle_id[vertex] == -1 and vertex not in seen:
            seen[vertex] = len(trail)
            trail.append(vertex)
            vertex = successor[vertex]
        if cycle_id[vertex] == -1:
            cyc = trail[seen[vertex]:]
            index = len(cycles)
            cycles.append(tuple(cyc))
            for node in cyc:
                cycle_id[node] = index
                height[node] = 0
        for node in reversed(trail):
            if cycle_id[node] == -1:
                cycle_id[node] = cycle_id[successor[node]]
                height[node] = height[successor[node]] + 1
    return cycles, cycle_id, height


def cost(successor, vertex):
    cycles, component, _ = decompose(successor)
    for index, cycle in enumerate(cycles):
        if vertex in cycle:
            return Fraction(sum(c == index for c in component), len(successor) * len(cycle))
    return Fraction(0)


def predicted_count(a, b, k):
    return comb(a, k) * comb(b, k) * factorial(k) * factorial(k - 1) * k ** (a + b - 2 * k)


def inspect(a, b):
    neighbors = [tuple(range(a, a + b)) for _ in range(a)] + [tuple(range(a)) for _ in range(b)]
    actual = {k: 0 for k in range(1, min(a, b) + 1)}
    tested = 0
    for strategy in product(*neighbors):
        tested += 1
        cycles, _, depth = decompose(strategy)
        is_equilibrium = True
        for player in range(a + b):
            old_cost = cost(strategy, player)
            if old_cost == 0:
                continue
            for target in neighbors[player]:
                if target == strategy[player]:
                    continue
                changed = list(strategy)
                changed[player] = target
                if cost(changed, player) < old_cost:
                    is_equilibrium = False
                    break
            if not is_equilibrium:
                break
        predicted_structure = len(cycles) == 1 and max(depth) <= 1
        assert is_equilibrium == predicted_structure, (a, b, strategy, cycles, depth)
        if is_equilibrium:
            actual[len(cycles[0]) // 2] += 1
    expected = {k: predicted_count(a, b, k) for k in actual}
    assert actual == expected, (a, b, actual, expected)
    return tested, sum(actual.values()), actual


def check_asymptotic_profile():
    from math import e
    lo, hi = 0.0, 1.0
    for _ in range(100):
        w = (lo + hi) / 2
        if w * exp(w) < 1:
            lo = w
        else:
            hi = w
    omega = (lo + hi) / 2
    alpha = 1 / (1 + omega)
    for m in (10, 20, 50, 100, 200, 500):
        values = [2 * lgamma(m + 1) - 2 * lgamma(m - k + 1) - log(k)
                  + 2 * (m - k) * log(k) for k in range(1, m + 1)]
        peak = 1 + max(range(m), key=lambda j: values[j])
        assert abs(peak / m - alpha) < 2 / m, (m, peak, alpha)
    return alpha, 1 + omega


if __name__ == '__main__':
    total_profiles = 0
    for a, b in ((1, 1), (1, 5), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)):
        tested, equilibria, spectrum = inspect(a, b)
        total_profiles += tested
        print(f'K_{{{a},{b}}}: tested={tested}, PFNE={equilibria}, spectrum={spectrum}')
    alpha, ratio = check_asymptotic_profile()
    print(f'cycle_fraction={alpha:.12f}; fairness_ratio={ratio:.12f}')
    print(f'EXACT_COMPARISONS_OK profiles={total_profiles}')
