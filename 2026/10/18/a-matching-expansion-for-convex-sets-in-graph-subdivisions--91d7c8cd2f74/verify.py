#!/usr/bin/env python3
"""Independent finite checks of P3-convex subdivision counting identities.

All checks are finite; the arguments in RESULT.md prove the general statements.
Run with: python3 verify.py
"""
from itertools import combinations
from collections import Counter, deque
from math import comb, factorial


def expansion(n, edges):
    edges = set(edges)
    result = Counter()
    for amask in range(1 << n):
        A = {v for v in range(n) if (amask >> v) & 1}
        B = set(range(n)) - A
        base = len(A) + sum(u in A and v in A for u, v in edges)
        inner = [(u, v) for u, v in edges if u in B and v in B]
        cross_degree = Counter()
        for u, v in edges:
            if u in A and v in B:
                cross_degree[v] += 1
            elif v in A and u in B:
                cross_degree[u] += 1
        for mmask in range(1 << len(inner)):
            matched = set()
            valid = True
            for j, (u, v) in enumerate(inner):
                if (mmask >> j) & 1:
                    if u in matched or v in matched:
                        valid = False
                        break
                    matched.add(u)
                    matched.add(v)
            if not valid:
                continue
            current = Counter({base + mmask.bit_count(): 1})
            for v in B - matched:
                copies = Counter(current)
                for power, count in current.items():
                    copies[power + 1] += count * cross_degree[v]
                current = copies
            result.update(current)
    return result


def direct(n, edges):
    vertices = n + len(edges)
    neighbors = [[] for _ in range(vertices)]
    for j, (u, v) in enumerate(edges):
        neighbors[u].append(n + j)
        neighbors[v].append(n + j)
        neighbors[n + j].extend((u, v))
    coefficients = Counter()
    for mask in range(1 << vertices):
        if all(((mask >> w) & 1) or
               sum((mask >> t) & 1 for t in neighbors[w]) <= 1
               for w in range(vertices)):
            coefficients[mask.bit_count()] += 1
    return coefficients


def closed_complete(n):
    answer = Counter()
    for a in range(n + 1):
        b = n - a
        base = a * (a + 1) // 2
        for j in range(b // 2 + 1):
            matchings = factorial(b) // (2**j * factorial(j) * factorial(b - 2*j))
            for t in range(b - 2*j + 1):
                answer[base + j + t] += (comb(n, a) * matchings *
                                         comb(b - 2*j, t) * a**t)
    return answer


def connected(n, edges):
    if n == 1:
        return True
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    reached = {0}
    queue = deque([0])
    while queue:
        for w in neighbors[queue.popleft()]:
            if w not in reached:
                reached.add(w)
                queue.append(w)
    return len(reached) == n


def main():
    comparisons = 0
    extrema = 0
    for n in range(1, 6):
        possible = list(combinations(range(n), 2))
        for emask in range(1 << len(possible)):
            E = [e for j, e in enumerate(possible) if (emask >> j) & 1]
            predicted = expansion(n, E)
            observed = direct(n, E)
            assert predicted == observed, (n, E, predicted, observed)
            comparisons += 1
            if n >= 2 and connected(n, E):
                degrees = Counter({v: 0 for v in range(n)})
                for u, v in E:
                    degrees[u] += 1
                    degrees[v] += 1
                total_vertices = n + len(E)
                highest_proper = max(k for k, c in observed.items()
                                     if k < total_vertices and c)
                assert highest_proper == total_vertices - min(degrees.values())
                extrema += 1
    for n in range(2, 26):
        P = closed_complete(n)
        N = n * (n + 1) // 2
        support = set(P)
        asserted = {0}
        for a in range(1, n + 1):
            asserted.update(range(a * (a + 1) // 2,
                                  n + a * (a - 1) // 2 + 1))
        assert support == asserted, (n, support.symmetric_difference(asserted))
        missing = set(range(N + 1)) - support
        assert len(missing) == (n - 1)**2 // 4
        if n >= 3:
            assert P[N - n + 1] == n * (n - 1)
    for n in range(2, 6):
        assert direct(n, list(combinations(range(n), 2))) == closed_complete(n)
    print('PASS: %d exhaustive subdivision graph polynomial comparisons' % comparisons)
    print('PASS: %d connected-graph largest-proper-convex-set checks' % extrema)
    print('PASS: complete-graph coefficient and gap formulas n=2,...,25')
    print('Finite checks corroborate, but do not replace, the general proof.')


if __name__ == '__main__':
    main()
