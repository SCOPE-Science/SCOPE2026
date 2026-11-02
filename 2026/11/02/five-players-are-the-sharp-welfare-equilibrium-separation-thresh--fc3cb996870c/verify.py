"""Exact small-graph checks for the binary threshold-coordination welfare theorem.

Python standard library only; no sampling is represented as a proof of a continuum claim.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def is_connected(n, edges):
    visited = {0}
    changed = True
    while changed:
        new = visited | {v for u, v in edges if u in visited} | {u for u, v in edges if v in visited}
        changed = new != visited
        visited = new
    return len(visited) == n


def welfare(n, edges, gamma, bits):
    total = Q(0)
    for i, j in edges:
        if bits[i] == bits[j]:
            total += gamma[i] + gamma[j] if bits[i] == 0 else 2 - gamma[i] - gamma[j]
    return total


def margins(n, edges, gamma, bits):
    result = []
    for i in range(n):
        neighbors = [v if u == i else u for u, v in edges if u == i or v == i]
        same = sum(bits[j] == bits[i] for j in neighbors)
        opposite = len(neighbors) - same
        stay = same * (gamma[i] if bits[i] == 0 else 1 - gamma[i])
        switch = opposite * (1 - gamma[i] if bits[i] == 0 else gamma[i])
        result.append(stay - switch)
    return result


def all_profiles(n):
    return list(product((0, 1), repeat=n))


def check_small_graphs():
    instances = 0
    optima = 0
    for n in range(2, 5):
        pairs = list(combinations(range(n), 2))
        states = all_profiles(n)
        for choice in all_profiles(len(pairs)):
            edges = [e for e, active in zip(pairs, choice) if active]
            if not is_connected(n, edges):
                continue
            for gamma in product((Q(1, 4), Q(1, 2), Q(3, 4)), repeat=n):
                values = [welfare(n, edges, gamma, state) for state in states]
                peak = max(values)
                for state, value in zip(states, values):
                    if value == peak:
                        assert all(x > 0 for x in margins(n, edges, gamma, state))
                        optima += 1
                instances += 1
    return instances, optima


def check_five_path():
    n = 5
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    gamma = (Q(1, 10), Q(2, 5), Q(2, 5), Q(9, 10), Q(9, 10))
    states = all_profiles(n)
    values = [welfare(n, edges, gamma, state) for state in states]
    peak = max(values)
    winners = [s for s, v in zip(states, values) if v == peak]
    assert winners == [(1, 1, 0, 0, 0)]
    assert peak == Q(23, 5)
    assert margins(n, edges, gamma, winners[0]) == [Q(9, 10), Q(1, 5), Q(-1, 5), Q(9, 5), Q(9, 10)] 
    nash = [s for s in states if all(m >= 0 for m in margins(n, edges, gamma, s))]
    assert nash == [(0, 0, 0, 0, 0), (1, 1, 1, 0, 0), (1, 1, 1, 1, 1)]
    best_eq = max(welfare(n, edges, gamma, s) for s in nash)
    assert best_eq == Q(9, 2)
    assert peak - best_eq == Q(1, 10)
    # Max-plus path recursion, independently recovering the peak.
    f0 = f1 = Q(0)
    for i in range(4):
        a = gamma[i] + gamma[i+1]
        b = 2 - a
        f0, f1 = max(f0 + a, f1), max(f1 + b, f0)
    assert max(f0, f1) == peak
    return peak, best_eq, nash


if __name__ == '__main__':
    count, optima = check_small_graphs()
    best, best_eq, nash = check_five_path()
    print(f'CHECK_OK small_connected_graph_parameter_cases={count} maximizing_states={optima}')
    print(f'CHECK_OK five_path_welfare_max={best} best_nash={best_eq} nash_count={len(nash)}')
