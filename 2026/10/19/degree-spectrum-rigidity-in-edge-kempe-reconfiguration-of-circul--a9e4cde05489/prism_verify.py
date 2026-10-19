"""Exhaustive edge-coloring and Kempe-switch verifier for cubic circular ladders."""
import collections
import itertools
import json


def verify(n):
    edges = sorted({tuple(sorted(e)) for e in
                    [(i, (i + 1) % n) for i in range(n)] +
                    [(i + n, (i + 1) % n + n) for i in range(n)] +
                    [(i, i + n) for i in range(n)]})
    incident = [[] for _ in range(2 * n)]
    for idx, (a, b) in enumerate(edges):
        incident[a].append(idx)
        incident[b].append(idx)
    anchor = sorted(incident[0])
    colors = [-1] * len(edges)
    used = [0] * (2 * n)
    for c, idx in enumerate(anchor):
        colors[idx] = c
        for v in edges[idx]:
            used[v] |= 1 << c
    remaining = [i for i in range(len(edges)) if i not in anchor]
    solutions = []

    def backtrack(i):
        if i == len(remaining):
            solutions.append(tuple(colors))
            return
        e = remaining[i]
        u, v = edges[e]
        for c in range(3):
            bit = 1 << c
            if (used[u] | used[v]) & bit:
                continue
            colors[e] = c
            used[u] |= bit
            used[v] |= bit
            backtrack(i + 1)
            used[u] ^= bit
            used[v] ^= bit
        colors[e] = -1

    backtrack(0)
    positions = {s: i for i, s in enumerate(solutions)}
    assert len(positions) == len(solutions)
    degrees = []
    adjacency = set()
    for i, s in enumerate(solutions):
        successors = set()
        for a, b in itertools.combinations(range(3), 2):
            pending = {j for j, c in enumerate(s) if c in (a, b)}
            while pending:
                stack = [pending.pop()]
                component = []
                while stack:
                    edge = stack.pop()
                    component.append(edge)
                    for v in edges[edge]:
                        for other in incident[v]:
                            if other in pending:
                                pending.remove(other)
                                stack.append(other)
                if any(j in anchor for j in component):
                    continue
                t = list(s)
                for j in component:
                    t[j] = a + b - t[j]
                successor = positions[tuple(t)]
                assert successor != i
                successors.add(successor)
                adjacency.add(tuple(sorted((i, successor))))
        degrees.append(len(successors))
    assert sum(degrees) == 2 * len(adjacency)
    N = (2 ** n - 2) // 6 if n % 2 else (2 ** n + 8) // 6
    expected_counter = collections.Counter({n - 3: N}) if n % 2 else collections.Counter()
    if n % 2 == 0:
        expected_counter[n - 3] += N - 2
        expected_counter[n - 1] += 1
        expected_counter[1] += 1
    expected = dict(sorted(expected_counter.items()))
    observed = dict(sorted(collections.Counter(degrees).items()))
    assert len(solutions) == N, (n, N, len(solutions))
    assert observed == expected, (n, expected, observed)
    return {'n': n, 'vertices': N, 'edges': len(adjacency), 'degree_multiplicities': {str(k): v for k, v in observed.items()}, 'verified': True}


def main():
    print(json.dumps({'method': 'direct exhaustive proper edge coloring and disjoint Kempe cycle switches', 'cases': [verify(n) for n in range(3, 12)]}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
