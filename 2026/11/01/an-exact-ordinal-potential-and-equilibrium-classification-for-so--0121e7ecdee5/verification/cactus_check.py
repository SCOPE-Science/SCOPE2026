"""Exact finite tests for cycle-factorized social distancing network formation.

The general theorem is proved in RESULT.md; this executable tests examples and
comparisons against direct move evaluations on independently enumerated states.
Python 3.10+, standard library only.
"""
from collections import deque
from itertools import product
from fractions import Fraction
from random import Random


def distances(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    out = []
    for a in range(n):
        dist = [-1] * n
        dist[a] = 0
        queue = deque([a])
        while queue:
            v = queue.popleft()
            for w in graph[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        if min(dist) < 0:
            return None
        out.append(dist)
    return out


def canonical(a, b):
    return tuple(sorted((a, b)))


def cycle_edges(vertices):
    return tuple(canonical(a, b) for a, b in zip(vertices, vertices[1:] + vertices[:1]))


def welfare(n, edges, alpha):
    d = distances(n, edges)
    if d is None:
        raise ValueError("disconnected")
    return 2 * alpha * len(edges) + sum(map(sum, d))


def utilities(n, edges, alpha):
    d = distances(n, edges)
    if d is None:
        raise ValueError("disconnected")
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return [alpha * deg[a] + sum(d[a]) for a in range(n)]


def cycle_thresholds(n, host, cycles, alpha):
    H = set(host)
    d = distances(n, H)
    assert d is not None
    t, w = {}, {}
    for c in cycles:
        for e in c:
            assert e in H and e not in t
            D = distances(n, H - {e})
            assert D is not None
            g = {x: sum(D[x][z] - d[x][z] for z in range(n)) for x in e}
            t[e] = max(g.values())
            w[e] = sum(D[x][y] - d[x][y] for x in range(n) for y in range(n)) - 2 * alpha
    return t, w


def enumerate_states(host, cycles):
    for choices in product(*[[(None,)] + [(e,) for e in c] for c in cycles]):
        removed = set()
        for choice in choices:
            if choice[0] is not None:
                removed.add(choice[0])
        yield frozenset(set(host) - removed), tuple(choice[0] for choice in choices)


def test_case(n, host, cycles, alpha):
    H = frozenset(host)
    t, w = cycle_thresholds(n, H, cycles, alpha)
    maximum = [max(t[e] for e in c) for c in cycles]
    states = list(enumerate_states(H, cycles))
    records = []
    for G, choices in states:
        u = utilities(n, G, alpha)
        phi = sum(alpha if e is None else t[e] for e in choices)
        stability = True
        for k, C in enumerate(cycles):
            if choices[k] is None:
                for e in C:
                    G2 = G - {e}
                    v = utilities(n, G2, alpha)
                    profitable = any(v[x] > u[x] for x in e)
                    assert profitable == (alpha < t[e])
                    if profitable:
                        stability = False
                        choices2 = choices[:k] + (e,) + choices[k+1:]
                        assert sum(alpha if x is None else t[x] for x in choices2) > phi
            else:
                e = choices[k]
                G2 = G | {e}
                v = utilities(n, G2, alpha)
                profitable = all(v[x] > u[x] for x in e)
                assert profitable == (alpha > t[e])
                if profitable:
                    stability = False
                    choices2 = choices[:k] + (None,) + choices[k+1:]
                    assert sum(alpha if x is None else t[x] for x in choices2) > phi
        predicted_stable = all(
            (alpha >= maximum[k] if e is None else alpha <= t[e])
            for k, e in enumerate(choices)
        )
        assert predicted_stable == stability
        predicted_SW = welfare(n, H, alpha) + sum(w[e] for e in choices if e is not None)
        assert welfare(n, G, alpha) == predicted_SW
        records.append((stability, predicted_SW, choices))
    eq_count = 1
    for c, maximum_C in zip(cycles, maximum):
        eq_count *= (int(alpha >= maximum_C) + sum(alpha <= t[e] for e in c))
    assert sum(rec[0] for rec in records) == eq_count
    best = welfare(n, H, alpha) + sum(max([0] + [w[e] for e in c]) for c in cycles)
    assert best == max(rec[1] for rec in records)
    assert any(rec[0] for rec in records)
    return len(states)


def check_all_connected_subgraphs(n, host, cycles):
    H = list(sorted(host))
    predicted = {G for G, _ in enumerate_states(host, cycles)}
    observed = set()
    for mask in range(1 << len(H)):
        G = frozenset(e for j, e in enumerate(H) if (mask >> j) & 1)
        if distances(n, G) is not None:
            observed.add(G)
    assert observed == predicted
    return len(observed)


def grow_cactus(rng, nlimit):
    n = 1
    edges = set()
    cycles = []
    while n < nlimit:
        anchor = rng.randrange(n)
        if n + 2 <= nlimit and rng.randrange(3) != 0:
            k = rng.randint(3, min(5, nlimit - n + 1))
            new_vertices = list(range(n, n + k - 1))
            cyc = cycle_edges([anchor] + new_vertices)
            cycles.append(cyc)
            edges.update(cyc)
            n += k - 1
        else:
            edges.add(canonical(anchor, n))
            n += 1
    return n, edges, cycles


def main():
    rng = Random(20261027)
    states_checked = 0
    cases_checked = 0
    completeness_checked = 0
    for n in range(3, 11):
        for _ in range(24):
            size, edges, cycles = grow_cactus(rng, n)
            if not cycles:
                continue
            if n <= 8:
                completeness_checked += check_all_connected_subgraphs(size, edges, cycles)
            for alpha in (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5), Fraction(10)):
                states_checked += test_case(size, edges, cycles, alpha)
                cases_checked += 1
    n = 11
    edges = set(cycle_edges([0, 1, 2]))
    edges.update(canonical(0, i) for i in range(3, 7))
    edges.update(canonical(1, i) for i in range(7, 11))
    alpha = Fraction(10)
    cycles = [cycle_edges([0, 1, 2])]
    t, w = cycle_thresholds(n, edges, cycles, alpha)
    assert all(t[e] == 5 for e in cycles[0])
    assert w[canonical(0, 1)] == 30
    assert w[canonical(0, 2)] == -10
    assert w[canonical(1, 2)] == -10
    states_checked += test_case(n, edges, cycles, alpha)
    cases_checked += 1
    print(f"PASS: {cases_checked} cactus/parameter instances, {states_checked} states, exact pairwise moves, welfare and potential")
    print(f"Connected-state exhaustive equality: {completeness_checked} states checked via every edge subset")
    print(f"Eleven-vertex example: host welfare {welfare(n, edges, alpha)}, optimum {welfare(n, edges, alpha)+30}")


if __name__ == '__main__':
    main()
