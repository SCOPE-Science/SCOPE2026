"""Standalone exhaustive graph/color enumeration for a 3-color cyclic graph automaton.

Python 3 standard library. Every labelled connected simple graph of order 2..5
with cycle rank at most one is checked, using a direct synchronous orbit simulator.
"""
from itertools import combinations, product


def connected(n, edges):
    seen = {0}
    while True:
        old = len(seen)
        for a, b in edges:
            if a in seen or b in seen:
                seen.add(a)
                seen.add(b)
        if len(seen) == old:
            return len(seen) == n


def cycle_vertices(n, edges):
    nb = [set() for _ in range(n)]
    for u, v in edges:
        nb[u].add(v)
        nb[v].add(u)
    alive = set(range(n))
    while True:
        leaves = [i for i in alive if len(nb[i] & alive) <= 1]
        if not leaves:
            break
        alive.difference_update(leaves)
    return alive


def formula(n, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    if len(edges) == n - 1:
        result = 3
        for d in deg:
            result *= 2**d - 1
        return result
    cycle = cycle_vertices(n, edges)
    assert len(cycle) >= 3
    result = 3
    for v in set(range(n)) - cycle:
        result *= 2**deg[v] - 1
    coeff = {0: 1}
    for v in cycle:
        r = deg[v] - 2
        a, b = 2 ** (r + 1) - 1, 2**r
        nxt = {}
        for k, c in coeff.items():
            for step, weight in [(-1, b), (0, a), (1, b)]:
                nxt[k + step] = nxt.get(k + step, 0) + c * weight
        coeff = nxt
    return result * coeff[0]


def brute(n, edges):
    m = len(edges)
    neighbors = [[] for _ in range(m)]
    for i, (u, v) in enumerate(edges):
        for j, (a, b) in enumerate(edges):
            if i != j and (u == a or u == b or v == a or v == b):
                neighbors[i].append(j)
    successes = 0
    for state in product(range(3), repeat=m):
        colors = state
        for _ in range(n + 2):
            if len(set(colors)) == 1:
                successes += 1
                break
            colors = tuple(
                (colors[i] + 1) % 3
                if (colors[i] + 1) % 3 in {colors[j] for j in neighbors[i]}
                else colors[i]
                for i in range(m)
            )
    return successes


def main():
    graph_count = state_count = 0
    for n in range(2, 6):
        all_edges = list(combinations(range(n), 2))
        for m in (n - 1, n):
            if m > len(all_edges):
                continue
            for edges in combinations(all_edges, m):
                if not connected(n, edges):
                    continue
                a, b = formula(n, edges), brute(n, edges)
                assert a == b, (n, edges, a, b)
                graph_count += 1
                state_count += 3**m
    print(f"PASS standalone_python labelled_graphs={graph_count} states={state_count} n_le_5")


if __name__ == '__main__':
    main()
