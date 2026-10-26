#!/usr/bin/env python3
"""Exhaustive finite checks for thin modules over small radical-square-zero quivers."""
from itertools import product

QUIVERS = [
    # parallel arrows and a reverse arrow
    (2, [(0, 1), (0, 1), (1, 0)]),
    # bipartite directed four-cycle (an undirected cycle in the support)
    (4, [(0, 1), (0, 3), (2, 1), (2, 3)]),
    # directed three-cycle
    (3, [(0, 1), (1, 2), (2, 0)]),
    # a loop, a chain, and a reverse arrow
    (3, [(0, 0), (0, 1), (1, 2), (2, 1)]),
]


def inv(a, q):
    return pow(a, -1, q)


def components(n, arrows, support):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x
    for i in support:
        s, t = arrows[i]
        union(s, t)
    return len({find(i) for i in range(n)})


def admissible(arrows, values, q):
    for i, (s, t) in enumerate(arrows):
        if values[i] == 0:
            continue
        for j, (u, v) in enumerate(arrows):
            if values[j] and t == u and values[i] * values[j] % q != 0:
                return False
    return True


def canonical(values, n, arrows, q):
    best = None
    for g in product(range(1, q), repeat=n):
        transformed = tuple(values[i] * g[t] * inv(g[s], q) % q
                            for i, (s, t) in enumerate(arrows))
        if best is None or transformed < best:
            best = transformed
    return best


def check(q, n, arrows):
    orbit_reps = set()
    orbit_reps_by_support = {}
    for values in product(range(q), repeat=len(arrows)):
        if not admissible(arrows, values, q):
            continue
        support = tuple(i for i, x in enumerate(values) if x)
        rep = canonical(values, n, arrows, q)
        orbit_reps.add(rep)
        orbit_reps_by_support.setdefault(support, set()).add(rep)
        c = components(n, arrows, support)
        # Endomorphisms are vertex scalars constant across active edges.
        end_count = 0
        aut_count = 0
        for lam in product(range(q), repeat=n):
            if all((lam[t] * values[i] - values[i] * lam[s]) % q == 0
                   for i, (s, t) in enumerate(arrows)):
                end_count += 1
                if all(lam[v] != 0 for v in range(n)):
                    aut_count += 1
        assert end_count == q ** c, (q, n, arrows, support, end_count, c)
        assert aut_count == (q - 1) ** c, (q, n, arrows, support, aut_count, c)
    for support, reps in orbit_reps_by_support.items():
        c = components(n, arrows, support)
        beta = len(support) - n + c
        assert beta >= 0
        assert len(reps) == (q - 1) ** beta, (q, n, arrows, support, len(reps), beta)
    # Empty support is always admissible and represented exactly once.
    assert () in orbit_reps_by_support
    return len(orbit_reps)


if __name__ == '__main__':
    cases = 0
    for q in (2, 3):
        for n, arrows in QUIVERS:
            total = check(q, n, arrows)
            print(f'q={q}, vertices={n}, arrows={len(arrows)}: {total} isomorphism classes checked')
            cases += 1
    print(f'VERIFY_OK: {cases} exhaustive finite-field/quiver cases')
