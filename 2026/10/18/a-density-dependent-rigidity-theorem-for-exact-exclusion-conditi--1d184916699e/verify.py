"""Finite arithmetic checks for a collision-conditioning classification.
Only checks, not a substitute for the general proof.
"""
from itertools import combinations, product
from random import Random
from math import comb


def connected(n, w):
    reached = {0}
    frontier = [0]
    while frontier:
        a = frontier.pop()
        for b in range(n):
            if b not in reached and w.get(tuple(sorted((a, b))), 0) > 0:
                reached.add(b)
                frontier.append(b)
    return len(reached) == n


def capacities(n, k, w):
    return [sum(w.get(p, 0) for p in combinations(S, 2))
            for S in combinations(range(n), k)]


def predicted(n, k, w):
    if k == n - 1:
        return len({sum(w.get(tuple(sorted((u, v))), 0)
                        for u in range(n) if u != v)
                    for v in range(n)}) == 1
    vals = [w.get((u, v), 0) for u, v in combinations(range(n), 2)]
    return len(set(vals)) == 1


def main():
    checks = 0
    for n in (3, 4):
        pairs = list(combinations(range(n), 2))
        for values in product(range(3), repeat=len(pairs)):
            w = dict(zip(pairs, values))
            if not connected(n, w):
                continue
            for k in range(2, n):
                c = capacities(n, k, w)
                assert (len(set(c)) == 1) == predicted(n, k, w), (n, k, w)
                checks += 1
    rng = Random(2053)
    for n in (5, 6, 7):
        pairs = list(combinations(range(n), 2))
        for i in range(1800):
            # Mix complete, sparse, nearly regular, and random positive weights.
            mode = i % 4
            if mode == 0:
                values = [rng.randint(1, 4) for _ in pairs]
            elif mode == 1:
                values = [rng.randint(0, 3) for _ in pairs]
            elif mode == 2:
                values = [int((v-u) % n in (1, n-1)) for u, v in pairs]
            else:
                values = [1 + ((u+v) % 3) for u, v in pairs]
            w = dict(zip(pairs, values))
            if not connected(n, w):
                continue
            for k in range(2, n):
                c = capacities(n, k, w)
                assert (len(set(c)) == 1) == predicted(n, k, w), (n, k, w)
                checks += 1
    # Explicit strict separation at the one-hole layer for four-cycle.
    n = 4
    w = {p: int((p[1] - p[0]) in (1, 3)) for p in combinations(range(n), 2)}
    assert set(capacities(4, 2, w)) == {0, 1}
    assert set(capacities(4, 3, w)) == {2}
    checks += 2
    # Every complete constant-symmetrized-rate graph obeys all-density equality,
    # and the rate split may be nonreversible.
    for n in range(3, 10):
        q = {(u, v): 0 for u in range(n) for v in range(n) if u != v}
        for u, v in combinations(range(n), 2):
            q[(u,v)] = 0.2 + 0.02 * (u + 1) / n
            q[(v,u)] = 1.0 - q[(u,v)]
        w = {(u,v): round(q[(u,v)] + q[(v,u)], 12)
             for u,v in combinations(range(n), 2)}
        for k in range(2, n):
            assert set(capacities(n, k, w)) == {comb(k, 2)}
            checks += 1
    print('PASS:', checks, 'finite capacity/classification checks')


if __name__ == '__main__':
    main()
