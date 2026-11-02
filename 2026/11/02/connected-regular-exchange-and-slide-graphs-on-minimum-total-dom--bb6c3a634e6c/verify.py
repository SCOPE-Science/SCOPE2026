"""Deterministic finite checks of a theorem on triangular-graph minimum total-domination exchanges.
Run: python3 verify.py. Uses only Python's standard library.
"""
from itertools import combinations
from math import factorial
from collections import Counter


def instance(n):
    pairs = list(combinations(range(n), 2))
    adj = [sum(1 << j for j, f in enumerate(pairs) if i != j and (e[0] in f or e[1] in f))
           for i, e in enumerate(pairs)]
    return pairs, adj


def exhaustive(n):
    q = (n - 1) // 3
    k = 2 * q
    pairs, adj = instance(n)
    size = len(pairs)
    solutions = set()
    for indices in combinations(range(size), k):
        bits = sum(1 << j for j in indices)
        if all(a & bits for a in adj):
            solutions.add(bits)
    expected = factorial(n) // (2**q * factorial(q))
    assert len(solutions) == expected, (n, len(solutions), expected)
    for sliding in (False, True):
        target_degree = (4 if sliding else 6) * q
        graph = {}
        for bits in solutions:
            occupied = [j for j in range(size) if (bits >> j) & 1]
            vacant = [j for j in range(size) if not (bits >> j) & 1]
            neighbors = {bits ^ (1 << i) ^ (1 << j)
                         for i in occupied for j in vacant
                         if (not sliding or (adj[i] >> j) & 1)
                         and (bits ^ (1 << i) ^ (1 << j)) in solutions}
            assert len(neighbors) == target_degree, (n, sliding, len(neighbors))
            graph[bits] = neighbors
        start = next(iter(solutions))
        seen = {start}
        todo = [start]
        while todo:
            for neighbor in graph[todo.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    todo.append(neighbor)
        assert seen == solutions, (n, sliding, len(seen))
        assert sum(map(len, graph.values())) // 2 == (2 if sliding else 3) * q * expected
    print('EXHAUSTIVE_OK', n, len(solutions))


def canonical(n):
    q = (n - 1) // 3
    pairs, adj = instance(n)
    edge_index = {e: i for i, e in enumerate(pairs)}
    S = set()
    for j in range(q):
        a, b, c = 3*j, 3*j+1, 3*j+2
        S.add(edge_index[(a, b)])
        S.add(edge_index[(b, c)])
    assert all(any((adj[i] >> j) & 1 for j in S) for i in range(len(pairs)))
    for sliding in (False, True):
        neighbors = set()
        for i in S:
            for j in range(len(pairs)):
                if j in S or (sliding and not ((adj[i] >> j) & 1)):
                    continue
                nxt = (S - {i}) | {j}
                if all(any((adj[h] >> t) & 1 for t in nxt) for h in range(len(pairs))):
                    neighbors.add(frozenset(nxt))
        assert len(neighbors) == (4 if sliding else 6)*q, (n, sliding, len(neighbors))
    print('CANONICAL_OK', n)


if __name__ == '__main__':
    for n in (4, 7):
        exhaustive(n)
    for n in (10, 13, 16):
        canonical(n)
    print('VERIFY_OK')
