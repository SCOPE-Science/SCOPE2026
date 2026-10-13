"""Finite checks of the strong-odd coloring enumerator on trees.
Only Python's standard library is needed. Run: python3 verify.py.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import factorial
from fractions import Fraction
from heapq import heapify, heappush, heappop


def tree_from_prufer(seq, n):
    degree = [1] * n
    for v in seq:
        degree[v] += 1
    available = [v for v in range(n) if degree[v] == 1]
    heapify(available)
    edges = []
    for v in seq:
        u = heappop(available)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heappush(available, v)
    edges.append(tuple(available))
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


@lru_cache(None)
def local_factor(d, q):
    assert d >= 1 and q >= 2
    # Vertex color is 0; its fixed distinguished-neighbor color is 1.
    # The other d-1 neighbor colors range over 1,...,q-1.
    count = 0
    for assigned in product(range(1, q), repeat=d - 1):
        counts = Counter((1,) + assigned)
        if all(v % 2 for v in counts.values()):
            count += 1
    return count


def factor_via_series(d, q):
    """Separate exact rational truncated series for (d-1)![z^(d-1)]cosh(z)(1+sinh(z))^(q-2)."""
    m = d - 1
    def multiply(a, b):
        out = [Fraction(0) for _ in range(m + 1)]
        for i, ai in enumerate(a):
            for j, bj in enumerate(b[:m+1-i]):
                out[i+j] += ai*bj
        return out
    cosh = [Fraction(1, factorial(i)) if i % 2 == 0 else Fraction(0) for i in range(m + 1)]
    oddzero = [Fraction(1) if i == 0 else Fraction(1, factorial(i)) if i % 2 == 1 else Fraction(0) for i in range(m+1)]
    power = [Fraction(1)] + [Fraction(0)] * m
    for _ in range(q-2):
        power = multiply(power, oddzero)
    coeff = multiply(cosh, power)[m] * factorial(m)
    assert coeff.denominator == 1
    return int(coeff)


def expected(adj, q):
    ans = q * (q - 1)
    for neigh in adj:
        ans *= local_factor(len(neigh), q)
    return ans


def brute(adj, q):
    n = len(adj)
    colors = [-1] * n
    # Count only proper assignments (faster than all q^n mappings).
    def rec(v):
        if v == n:
            for u in range(n):
                c = Counter(colors[w] for w in adj[u])
                if any(t % 2 == 0 for t in c.values()):
                    return 0
            return 1
        total = 0
        forbidden = {colors[u] for u in adj[v] if colors[u] >= 0}
        for c in range(q):
            if c not in forbidden:
                colors[v] = c
                total += rec(v + 1)
        colors[v] = -1
        return total
    return rec(0)


def run():
    comparisons = 0
    total = 0
    max_n = 0
    for n in range(2, 7):
        for seq in product(range(n), repeat=n-2):
            adj = tree_from_prufer(seq, n)
            for q in range(2, (6 if n <= 5 else 5)):
                e = expected(adj, q)
                b = brute(adj, q)
                assert b == e, (n, seq, q, e, b)
                comparisons += 1
                total += b
            max_n = n
    # Additional larger trees with several branching patterns.
    for n in (7, 8, 9):
        examples = [tuple((i * i + 3 * i + a) % n for i in range(n - 2))
                    for a in range(min(3, n))]
        examples += [tuple((i + a) % n for i in range(n-2))
                     for a in range(min(3, n))]
        for seq in examples:
            adj = tree_from_prufer(seq, n)
            for q in ((2, 3, 4) if n <= 8 else (2, 3)):
                e = expected(adj, q)
                b = brute(adj, q)
                assert b == e, (n, seq, q, e, b)
                comparisons += 1
                total += b
            max_n = n
    # Check the closed 3-color expression separately, for all labeled trees to n=7.
    three_formula = 0
    for n in range(2, 8):
        for seq in product(range(n), repeat=n-2):
            adj = tree_from_prufer(seq, n)
            claimed = 6
            for neigh in adj:
                d = len(neigh)
                if d % 2 == 0:
                    claimed *= 2**(d-2)
            assert claimed == expected(adj, 3), (n, seq)
            three_formula += 1
    for d in range(1, 11):
        for q in range(2, 7):
            assert factor_via_series(d, q) == local_factor(d, q), (d, q)
    print('VERIFY_OK')
    print('full_brute_vs_product_comparisons', comparisons)
    print('full_brute_total_accepted_assignments', total)
    print('closed_3_color_all_labeled_trees', three_formula)
    print('largest_brute_tree_order', max_n)
    print('series_vs_direct_local_factors', 10 * 5)
    print('local_factors_q3_degrees_1_to_12', [local_factor(d,3) for d in range(1,13)])


if __name__ == '__main__':
    run()
