"""Exhaustive three-edge-coloring/Kempe census for circular ladders.

Requires Python 3.9+, standard library only. Does not assume the dual-face model.
"""
from collections import Counter, deque


def prism_edges(n):
    assert n >= 3
    out = set()
    for i in range(n):
        j = (i + 1) % n
        for a, b in ((i, j), (n + i, n + j), (i, n + i)):
            out.add(tuple(sorted((a, b))))
    return tuple(sorted(out))


def enumerate_colours(n):
    edges = prism_edges(n)
    incidence = [[] for _ in range(2 * n)]
    for j, (u, v) in enumerate(edges):
        incidence[u].append(j)
        incidence[v].append(j)
    assigned = [-1] * len(edges)
    states = []
    def dfs(i):
        if i == len(edges):
            states.append(tuple(assigned))
            return
        u, v = edges[i]
        used = {assigned[j] for w in (u, v) for j in incidence[w]
                if assigned[j] >= 0}
        for c in range(3):
            if c not in used:
                assigned[i] = c
                dfs(i + 1)
                assigned[i] = -1
    dfs(0)
    return edges, incidence, states


def kempe_neighbours(state, edges, incidence):
    nverts = len(incidence)
    neighbours = set()
    counts = []
    for a, b in ((0, 1), (0, 2), (1, 2)):
        seen = set()
        number = 0
        for v in range(nverts):
            if v in seen:
                continue
            stack = [v]
            seen.add(v)
            involved = set()
            while stack:
                x = stack.pop()
                for j in incidence[x]:
                    if state[j] not in (a, b):
                        continue
                    involved.add(j)
                    u, w = edges[j]
                    y = (u ^ w ^ x)
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
            assert involved
            number += 1
            changed = list(state)
            for j in involved:
                changed[j] = a + b - state[j]
            neighbours.add(tuple(changed))
        counts.append(number)
    assert sum(counts) == len(neighbours)
    return neighbours, counts


def expected(n):
    if n % 2:
        return {n: 2 ** n - 2}, n * (2 ** n - 2) // 2
    return Counter({n: 2 ** n - 4}) + Counter({n+2: 6}) + Counter({4: 6}), (n * (2 ** n + 2) + 36) // 2


def main():
    for n in range(3, 13):
        edges, incidence, states = enumerate_colours(n)
        labels = {s: i for i, s in enumerate(states)}
        assert len(states) == len(labels)
        degrees = Counter()
        m2 = 0
        adjacency = []
        for state in states:
            neighbours, counts = kempe_neighbours(state, edges, incidence)
            assert all(s in labels and s != state for s in neighbours)
            degrees[len(neighbours)] += 1
            m2 += len(neighbours)
            adjacency.append({labels[s] for s in neighbours})
        assert m2 % 2 == 0
        expected_degs, expected_edges = expected(n)
        assert degrees == Counter(expected_degs), (n, degrees, expected_degs)
        assert m2 // 2 == expected_edges
        if n <= 10:
            # Connectivity is prior literature; this is a sanity check, not a novelty claim.
            seen = {0}; queue = deque([0])
            while queue:
                for v in adjacency[queue.popleft()]:
                    if v not in seen:
                        seen.add(v); queue.append(v)
            assert len(seen) == len(states)
        print(f"n={n} states={len(states)} edges={m2//2} degrees={dict(sorted(degrees.items()))}")
    print("PRISM_DIRECT_EDGE_KEMPE_PASS")


if __name__ == '__main__':
    main()
