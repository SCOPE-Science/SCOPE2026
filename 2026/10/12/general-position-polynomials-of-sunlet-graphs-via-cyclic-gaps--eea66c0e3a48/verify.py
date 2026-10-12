"""Reproduce the cardinality enumerator of general-position sets of sunlets.

Python 3.9+; standard library only. The direct verifier uses independent
all-pairs shortest paths and tests every subset for the stated finite orders.
"""
from collections import deque
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def distances(n):
    graph = [set() for _ in range(2 * n)]
    for i in range(n):
        for j in ((i + 1) % n, i + n):
            graph[i].add(j)
            graph[j].add(i)
    result = []
    for origin in range(2 * n):
        row = [-1] * (2 * n)
        row[origin] = 0
        queue = deque([origin])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if row[v] == -1:
                    row[v] = row[u] + 1
                    queue.append(v)
        result.append(row)
    return result


def independent_direct_coefficients(n):
    dist = distances(n)
    answer = [0] * (n + 1)
    checked = 0
    for mask in range(1 << (2 * n)):
        vertices = [v for v in range(2 * n) if mask & (1 << v)]
        checked += 1
        admissible = True
        for a, b, c in combinations(vertices, 3):
            if (dist[a][b] + dist[b][c] == dist[a][c]
                    or dist[a][c] + dist[c][b] == dist[a][b]
                    or dist[b][a] + dist[a][c] == dist[b][c]):
                admissible = False
                break
        if admissible:
            assert len(vertices) <= n
            answer[len(vertices)] += 1
    return answer, checked


def cyclic_gap_coefficients(n):
    answer = [0] * (n + 1)
    answer[:3] = [1, 2 * n, 4 * choose(n, 2) + n]
    for mask in range(1 << n):
        sites = [i for i in range(n) if mask & (1 << i)]
        k = len(sites)
        if k < 3:
            continue
        gaps = [(sites[(i + 1) % k] - sites[i]) % n for i in range(k)]
        eligible = sum(2 * (gaps[i - 1] + gaps[i]) > n for i in range(k))
        answer[k] += 1 << eligible
    return answer


def closed_coefficients(n):
    a = [0] * (n + 1)
    a[:3] = [1, 2 * n, 4 * choose(n, 2) + n]
    for k in range(3, n + 1):
        h = (n - 1) // 2
        marked_roots = n * sum((n - 1 - d) * choose(d - 1, k - 3)
                               for d in range(k - 2, h + 1))
        adjacent_pairs = 0
        if k == 3:
            for p in range(1, n - 1):
                for q in range(1, n - p):
                    r = n - p - q
                    if 2 * (p + q) > n and 2 * (p + r) > n:
                        adjacent_pairs += n
            eligible_triples_num = n * (choose(n - 1, 2)
                                         - 3 * choose(n // 2, 2))
            assert eligible_triples_num % 3 == 0
            eligible_triples = eligible_triples_num // 3
        else:
            for p in range(1, n + 1):
                for q in range(1, n - p + 1):
                    if 2 * (p + q) <= n:
                        continue
                    for r in range(1, n - p - q + 1):
                        if 2 * (p + r) <= n:
                            continue
                        leftover = n - p - q - r
                        adjacent_pairs += n * choose(leftover - 1, k - 4)
            eligible_triples = 0
        a[k] = choose(n, k) + marked_roots + adjacent_pairs + eligible_triples
    return a


def verify():
    direct_checks = 0
    for n in range(3, 10):
        direct, tested = independent_direct_coefficients(n)
        gaps = cyclic_gap_coefficients(n)
        closed = closed_coefficients(n)
        assert direct == gaps == closed, (n, direct, gaps, closed)
        direct_checks += tested
        print(f"n={n}: coefficients={direct}, direct_subsets={tested}: PASS")
    for n in range(10, 17):
        gaps = cyclic_gap_coefficients(n)
        closed = closed_coefficients(n)
        assert gaps == closed, (n, gaps, closed)
        assert closed[-1] == 1
        print(f"n={n}: cyclic_sites={1 << n}, all_coefficients_agree: PASS")
    for n in range(17, 33):
        c = closed_coefficients(n)
        assert all(x >= 0 for x in c)
        assert c[-1] == 1
        print(f"n={n}: binomial_formula_integrality_and_top_degree: PASS")
    print("All checks PASS; direct vertex-subset count:", direct_checks)
    print("Finite checks support but do not replace the proof for arbitrary n.")


if __name__ == "__main__":
    verify()
