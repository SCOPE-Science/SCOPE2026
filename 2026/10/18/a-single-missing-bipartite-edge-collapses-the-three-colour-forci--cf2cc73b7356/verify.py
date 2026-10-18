"""Reproduce the three-seed crown-graph census and the matching-deletion comparison.

Run with Python 3.9+; no external packages. Finite tests supplement the written proof.
"""
from itertools import combinations, product


def adjacency(n, deleted_matching_size=0):
    adj = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i == j and i < deleted_matching_size:
                continue
            adj[i].append(n+j)
            adj[n+j].append(i)
    return adj


def proper(values, adj):
    for i, ns in enumerate(adj):
        if values[i] < 0:
            return False
        if any(values[j] == values[i] for j in ns):
            return False
    return True


def completes_by_forcing(partial, adj):
    """Simultaneous closure of all currently forced vertices."""
    vals = list(partial)
    while True:
        step = []
        for i, neighbors in enumerate(adj):
            if vals[i] != -1:
                continue
            seen = {vals[j] for j in neighbors if vals[j] != -1}
            if len(seen) == 2:
                forced_color = (set(range(3)) - seen).pop()
                step.append((i, forced_color))
        if not step:
            break
        for i, c in step:
            vals[i] = c
    return proper(vals, adj)


def canonical_three_seed(n, t, vertices, colors):
    # The only predicted minima: one deleted-matching pair uses one color;
    # its third seed lies at a different index and has a different color.
    seeds = dict(zip(vertices, colors))
    for i in range(t):
        if i in seeds and i+n in seeds and seeds[i] == seeds[i+n]:
            others = [v for v in vertices if v not in (i, i+n)]
            if len(others) == 1 and others[0] % n != i:
                return seeds[others[0]] != seeds[i]
    return False


def check_matching_deletions():
    checks = 0
    for n in range(4, 8):
        for t in range(1, n+1):
            adj = adjacency(n, t)
            count = [0, 0, 0, 0]
            for k in range(4):
                for vertices in combinations(range(2*n), k):
                    for colors in product(range(3), repeat=k):
                        values = [-1]*(2*n)
                        for v, c in zip(vertices, colors):
                            values[v] = c
                        actual = completes_by_forcing(values, adj)
                        if k == 3:
                            expected = canonical_three_seed(n, t, vertices, colors)
                            assert actual == expected, (n, t, vertices, colors, actual, expected)
                        if actual:
                            count[k] += 1
                        checks += 1
            assert count == [0, 0, 0, 12*t*(n-1)], (n, t, count)
            print('side size', n, 'deleted pairs',t,'successful k=0..3:', count)
    return checks


def check_complete_bipartite_bound():
    checks = 0
    for n in range(4, 7):
        adj = adjacency(n, 0)
        for k in range(n):
            successes = 0
            for vertices in combinations(range(2*n), k):
                for colors in product(range(3), repeat=k):
                    values = [-1]*(2*n)
                    for v, c in zip(vertices, colors):
                        values[v] = c
                    successes += completes_by_forcing(values, adj)
                    checks += 1
            assert successes == 0, (n, k, successes)
        # A fully seeded side with both colours 0,1 forces the other side to 2.
        values = [0, 1] + [0]*(n-2) + [-1]*n
        assert completes_by_forcing(values, adj)
        print('complete bipartite side size', n, 'minimum seed size:', n)
    return checks


if __name__ == '__main__':
    total = check_matching_deletions() + check_complete_bipartite_bound()
    print('ALL CHECKS PASSED; partial assignments tested:', total)
