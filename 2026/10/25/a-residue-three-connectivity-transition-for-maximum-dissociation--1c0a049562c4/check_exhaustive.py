"""Exhaustive vertex-set test for maximum dissociation exchanges in T(n)."""
from collections import Counter, deque
from itertools import combinations
from math import factorial


def predicted(n):
    k, r = divmod(n, 3)
    if r == 0:
        return 2 * k, factorial(n) // (2 ** k * factorial(k)), factorial(n) // (6 ** k * factorial(k))
    if r == 1:
        a = factorial(n) // (2 ** k * factorial(k))
        b = 0 if k == 0 else factorial(n) // (2 ** (k + 2) * factorial(k - 1))
        return 2 * k, a + b, 1
    return 2 * k + 1, factorial(n) // (2 ** (k + 1) * factorial(k)), 1


def analyze(n):
    edges = list(combinations(range(n), 2))
    ecount = len(edges)
    # Each chosen edge has at most one selected edge sharing an endpoint.
    def feasible(chosen):
        deg = [0] * n
        for i in chosen:
            x, y = edges[i]
            deg[x] += 1
            deg[y] += 1
        return all(deg[x] + deg[y] <= 3 for i in chosen for x, y in [edges[i]])

    layers = [frozenset()]
    for i in range(ecount):
        layers.extend([s | {i} for s in layers if feasible(s | {i})])
    optimum = max(map(len, layers))
    sets = [s for s in layers if len(s) == optimum]
    loc = {frozenset(s): i for i, s in enumerate(sets)}
    assert len(loc) == len(sets)
    neighbors = []
    for s in sets:
        adj = set()
        for removed in s:
            base = s - {removed}
            for inserted in range(ecount):
                if inserted not in s:
                    new = base | {inserted}
                    if new in loc:
                        adj.add(loc[new])
        neighbors.append(adj)
    seen = set()
    sizes = []
    for i in range(len(sets)):
        if i in seen:
            continue
        seen.add(i)
        q = deque([i]); count = 0
        while q:
            u = q.popleft(); count += 1
            for v in neighbors[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        sizes.append(count)
    predicted_size, predicted_count, predicted_components = predicted(n)
    assert (optimum, len(sets), len(sizes)) == (predicted_size, predicted_count, predicted_components)
    k, r = divmod(n, 3)
    assert set(map(len, neighbors)) == ({2 * k} if r == 0 else ({6 * k} if r == 2 else {8 * k, 10 * k - 2}))
    if r == 0:
        assert set(sizes) == {3 ** k}
    else:
        assert sizes == [len(sets)]
    return dict(n=n, maximum=optimum, vertices=len(sets), components=len(sizes), component_sizes=dict(sorted(Counter(sizes).items())), degrees=dict(sorted(Counter(map(len, neighbors)).items())))


if __name__ == '__main__':
    for n in range(3, 10):
        print(analyze(n))
    print('EXHAUSTIVE_PASS')
