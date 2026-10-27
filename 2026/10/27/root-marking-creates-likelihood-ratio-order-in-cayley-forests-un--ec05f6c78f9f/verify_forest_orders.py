"""Exact reproducibility checks for tagged-component likelihood-ratio comparisons.

Uses only Python's standard library and integer/rational arithmetic.
Run: python verify_forest_orders.py
"""
from functools import lru_cache
from fractions import Fraction
from math import comb

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def tree_count(size, rooted=False):
    if size == 1:
        return 1
    return size ** (size - (1 if rooted else 2))


@lru_cache(None)
def unrooted_total(n, k):
    if n == 0:
        return int(k == 0)
    if not 1 <= k <= n:
        return 0
    return sum(comb(n - 1, s - 1) * tree_count(s)
               * unrooted_total(n - s, k - 1)
               for s in range(1, n - k + 2))


def rooted_total(n, k):
    if n == 0:
        return int(k == 0)
    if not 1 <= k <= n:
        return 0
    return comb(n - 1, k - 1) * n ** (n - k)


def tagged_count(n, k, s, rooted=False):
    if not 1 <= s <= n - k + 1:
        return 0
    if rooted:
        return (comb(n - 1, s - 1) * tree_count(s, rooted=True)
                * rooted_total(n - s, k - 1))
    return (comb(n - 1, s - 1) * tree_count(s)
            * unrooted_total(n - s, k - 1))


def tagged_pmf(n, k, rooted=False):
    total = rooted_total(n, k) if rooted else unrooted_total(n, k)
    return [Fraction(tagged_count(n, k, s, rooted), total)
            for s in range(1, n + 1)]


def exact_forest_enumeration(n):
    """Enumerate every acyclic graph on n vertices, no formula assumptions."""
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    unlabeled_counts = [[0] * (n + 1) for _ in range(n + 1)]
    root_marked_counts = [[0] * (n + 1) for _ in range(n + 1)]
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        sizes = [1] * n
        def root(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        valid = True
        for e, (u, v) in enumerate(edges):
            if mask & (1 << e):
                ru, rv = root(u), root(v)
                if ru == rv:
                    valid = False
                    break
                parent[ru] = rv
                sizes[rv] += sizes[ru]
        if not valid:
            continue
        component_sizes = [sizes[u] for u in range(n) if root(u) == u]
        k = len(component_sizes)
        s = sizes[root(0)]
        weight = 1
        for item in component_sizes:
            weight *= item
        unlabeled_counts[k][s] += 1
        root_marked_counts[k][s] += weight
    return unlabeled_counts, root_marked_counts


def main():
    for n in range(1, 7):
        u_obs, r_obs = exact_forest_enumeration(n)
        for k in range(1, n + 1):
            check(sum(u_obs[k]) == unrooted_total(n, k), ('unrooted total', n, k))
            check(sum(r_obs[k]) == rooted_total(n, k), ('rooted total', n, k))
            for s in range(1, n + 1):
                check(u_obs[k][s] == tagged_count(n, k, s), ('unrooted tagged', n, k, s))
                check(r_obs[k][s] == tagged_count(n, k, s, rooted=True), ('rooted tagged', n, k, s))

    for n in range(2, 42):
        for k in range(1, n):
            p = tagged_pmf(n, k, rooted=True)
            q = tagged_pmf(n, k + 1, rooted=True)
            for s in range(n):
                check(sum(q[s:]) <= sum(p[s:]), ('rooted stochastic', n, k, s))
            for s in range(n):
                for t in range(s + 1, n):
                    check(q[s] * p[t] >= q[t] * p[s], ('rooted likelihood ratio', n, k, s, t))
            if 2 <= k <= n - 2:
                const = Fraction(k * n, (k - 1) * (n - k))
                for s in range(1, n - k + 1):
                    actual = q[s - 1] / p[s - 1]
                    desired = const * Fraction(n - s - k + 1, n - s)
                    check(actual == desired, ('rooted exact adjacent ratio', n, k, s))
                for s in range(1, n - k):
                    check(q[s - 1] / p[s - 1] > q[s] / p[s], ('strict interior', n, k, s))

    for m in range(2, 85):
        F2 = unrooted_total(m, 2)
        F1 = unrooted_total(m, 1)
        check(Fraction(F2, F1) == Fraction((m - 1) * (m + 6), 2 * m * m), ('two-forest ratio', m))
    for m in range(3, 83):
        hm = Fraction(unrooted_total(m, 2), unrooted_total(m, 1))
        hn = Fraction(unrooted_total(m + 1, 2), unrooted_total(m + 1, 1))
        check(hm - hn == Fraction((m - 2) * (5 * m + 3), 2 * m * m * (m + 1) ** 2), ('gap', m))

    for n in range(3, 55):
        p = tagged_pmf(n, 2, rooted=False)
        q = tagged_pmf(n, 3, rooted=False)
        def lr_le(a, b):
            return all(a[s] * b[t] >= a[t] * b[s]
                       for s in range(n) for t in range(s + 1, n))
        if n < 5:
            check(lr_le(q, p), ('small n monotonic', n))
        else:
            check(not lr_le(q, p), ('large n LR failure one', n))
            check(not lr_le(p, q), ('large n LR failure two', n))
            check(q[1] / p[1] > q[0] / p[0], ('initial reversal', n))
            check(p[n - 2] > 0 and q[n - 2] == 0, ('terminal support drop', n))
    check(tagged_pmf(5, 2)[:4] == [Fraction(8, 55), Fraction(6, 55), Fraction(9, 55), Fraction(32, 55)], 'five vertex 2')
    check(tagged_pmf(5, 3)[:4] == [Fraction(1, 3), Fraction(4, 15), Fraction(2, 5), Fraction(0)], 'five vertex 3')
    print('PASS:', CHECKS, 'exact integer/fraction assertions; graph-enumeration n<=6; formula n<=84')


if __name__ == '__main__':
    main()
