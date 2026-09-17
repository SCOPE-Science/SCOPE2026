"""Reproducible greedy search using the neighbourhood matching predicate."""
import itertools
import random


def matching(adj, mask, k):
    if k == 0:
        return True
    if mask.bit_count() < 2 * k:
        return False
    bit = mask & -mask
    v = bit.bit_length() - 1
    rest = mask ^ bit
    if matching(adj, rest, k):
        return True
    neighbours = adj[v] & rest
    while neighbours:
        b = neighbours & -neighbours
        neighbours ^= b
        if matching(adj, rest ^ b, k - 1):
            return True
    return False


def contains(adj, q):
    return any(a.bit_count() >= q + 6 and matching(adj, a, 3) for a in adj)


def toggle(adj, u, v):
    adj[u] ^= 1 << v
    adj[v] ^= 1 << u


def edges(adj):
    return [(u, v) for u in range(len(adj)) for v in range(u + 1, len(adj))
            if adj[u] >> v & 1]


def saturated(adj, q):
    if contains(adj, q):
        return False
    for u, v in itertools.combinations(range(len(adj)), 2):
        if not (adj[u] >> v & 1):
            toggle(adj, u, v)
            found = contains(adj, q)
            toggle(adj, u, v)
            if not found:
                return False
    return True


if __name__ == '__main__':
    rng = random.Random(20260916)
    for q, n in [(1, 8), (1, 9), (1, 10), (1, 12), (2, 9), (3, 10)]:
        best = n * n
        pairs = list(itertools.combinations(range(n), 2))
        for trial in range(2500):
            adj = [0] * n
            rng.shuffle(pairs)
            for u, v in pairs:
                toggle(adj, u, v)
                if contains(adj, q):
                    toggle(adj, u, v)
            size = len(edges(adj))
            if size < best:
                best = size
                assert saturated(adj, q)
                if size < n + 5:
                    print('COUNTEREXAMPLE', q, n, size, edges(adj), flush=True)
                    raise SystemExit
        print('minimum found', q, n, best, 'conjectured', n + 5, flush=True)
