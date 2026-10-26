"""Exact check of a joint-law identity for uniformly random recursive trees.

Only standard-library integer arithmetic is used. The exhaustive part does not
establish the general theorem; its analytic proof is supplied separately.
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def direct(n):
    root_leaf = Counter()
    last_depth_complement = Counter()
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        children = [0] * (n + 1)
        depth = [0] * (n + 1)
        for j, parent in enumerate(parents, 2):
            children[parent] += 1
            depth[j] = depth[parent] + 1
        leaves = sum(c == 0 for c in children[1:])
        root_leaf[(children[1], leaves)] += 1
        last_depth_complement[(depth[n], n - leaves)] += 1
    return root_leaf, last_depth_complement


def polynomial(n_max):
    # Unnormalized coefficient tables, with entries indexed by (statistic, leaves).
    trees = {1: Counter({1: 1})}
    root = {1: Counter({(0, 1): 1})}
    newest = {1: Counter({(0, 1): 1})}
    for n in range(2, n_max + 1):
        old = trees[n - 1]
        t = Counter()
        for leaves, c in old.items():
            t[leaves] += leaves * c
            t[leaves + 1] += (n - 1 - leaves) * c
        trees[n] = t

        r = Counter()
        if n == 2:
            r[(1, 1)] = 1
        else:
            for (degree, leaves), c in root[n - 1].items():
                r[(degree + 1, leaves + 1)] += c
                r[(degree, leaves)] += leaves * c
                r[(degree, leaves + 1)] += (n - 2 - leaves) * c
        root[n] = r

        # The maximum-label child decomposition yields
        # H_n = u sum_{k=1}^{n-1} binom(n-2,k-1) H_k B_{n-1-k},
        # with B_0=1 and B_j=T_{j+1} for j>=1.
        h = Counter()
        for k in range(1, n):
            j = n - 1 - k
            forest = Counter({0: 1}) if j == 0 else trees[j + 1]
            for (depth, leaves), c in newest[k].items():
                for other_leaves, d in forest.items():
                    h[(depth + 1, leaves + other_leaves)] += comb(n - 2, k - 1) * c * d
        newest[n] = h

        rr = +r
        hh = Counter({(dep, n - leaves): c for (dep, leaves), c in h.items() if c})
        assert rr == hh, (n, rr, hh)
        assert sum(rr.values()) == factorial(n - 1)
    return root, newest


def run():
    direct_checks = 0
    for n in range(2, 11):
        a, b = direct(n)
        assert a == b, (n, a, b)
        assert sum(a.values()) == factorial(n - 1)
        direct_checks += 1
    root, newest = polynomial(22)
    assert direct_checks == 9
    # The displayed covariance follows from exact integer moments.
    from fractions import Fraction
    for n in range(2, 23):
        a = root[n]
        total = sum(a.values())
        er = Fraction(sum(k * c for (k, leaves), c in a.items()), total)
        el = Fraction(sum(leaves * c for (k, leaves), c in a.items()), total)
        erl = Fraction(sum(k * leaves * c for (k, leaves), c in a.items()), total)
        assert erl - er * el == Fraction(n - 2, 2 * (n - 1))
        h = newest[n]
        ed = Fraction(sum(k * c for (k, leaves), c in h.items()), total)
        edl = Fraction(sum(k * leaves * c for (k, leaves), c in h.items()), total)
        assert edl - ed * el == -Fraction(n - 2, 2 * (n - 1))
    print('PASS: exhaustive labelled-tree equality n=2..10 (9 sizes).')
    print('PASS: independent integer recurrences n=2..22 (21 sizes).')
    print('PASS: exact covariance identities n=2..22 (21 sizes).')
    print('Analytic all-n proof is not inferred from these finite checks.')


if __name__ == '__main__':
    run()
