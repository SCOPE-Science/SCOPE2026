"""Exact reproducibility checks for singleton-conditioned richness dominance.

No external dependencies. Run with Python 3.9+.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def parts(n, lo=1):
    if n == 0:
        yield ()
    for a in range(lo, n + 1):
        for tail in parts(n - a, a):
            yield (a,) + tail


def empirical_wor(abundances, m, j):
    items = [i for i, a in enumerate(abundances) for _ in range(a)]
    n = len(items)
    counts = defaultdict(int)
    for sample in combinations(range(n), m):
        by_color = [0] * len(abundances)
        for i in sample:
            by_color[items[i]] += 1
        richness = sum(x > 0 for x in by_color)
        counts[(by_color[j], richness)] += 1
    denominator = comb(n, m)
    return {key: Fraction(ct, denominator) for key, ct in counts.items()}


def check_dominance(tab, j_label=''):
    # Joint mass table (tagged count, observed richness) -> exact probability.
    ys = sorted({y for y, k in tab})
    py1 = sum((p for (y, k), p in tab.items() if y == 1), Fraction())
    if py1 == 0:
        return 0
    ks = sorted({k for y, k in tab})
    tested = 0
    for threshold in ks:
        all_tail = sum((p for (y, k), p in tab.items() if k >= threshold), Fraction())
        one_tail = sum((p for (y, k), p in tab.items() if y == 1 and k >= threshold), Fraction()) / py1
        assert one_tail >= all_tail, (j_label, threshold, one_tail, all_tail)
        # In fact singleton-conditioning dominates every fixed feasible count.
        for y in ys:
            py = sum((p for (z, k), p in tab.items() if z == y), Fraction())
            tail_y = sum((p for (z, k), p in tab.items() if z == y and k >= threshold), Fraction()) / py
            assert one_tail >= tail_y, (j_label, threshold, y)
            tested += 1
    expected_k = sum((k * p for (y, k), p in tab.items()), Fraction())
    expected_tag = py1
    expected_product = sum((k * p for (y, k), p in tab.items() if y == 1), Fraction())
    assert expected_product - expected_k * expected_tag >= 0
    return tested


def multinomial_joint(probs, m, j):
    tab = defaultdict(Fraction)
    for seq in product(range(len(probs)), repeat=m):
        counts = [seq.count(i) for i in range(len(probs))]
        prob = Fraction(1)
        for i in seq:
            prob *= probs[i]
        tab[(counts[j], sum(z > 0 for z in counts))] += prob
    assert sum(tab.values()) == 1
    return tab


def cov_tag_r_wor(a, m, j, r):
    tab = empirical_wor(a, m, j)
    P = sum((w for (y, k), w in tab.items() if y == r), Fraction())
    EK = sum((k*w for (y, k), w in tab.items()), Fraction())
    EKJ = sum((k*w for (y, k), w in tab.items() if y == r), Fraction())
    return EKJ - P * EK


def main():
    checks = 0
    profiles = 0
    for n in range(1, 10):
        for a in parts(n):
            profiles += 1
            for m in range(1, n + 1):
                for j in range(len(a)):
                    tab = empirical_wor(a, m, j)
                    checks += check_dominance(tab, ('finite',a,m,j))
    iid_profiles = ((Fraction(1,3),Fraction(2,3)),
                    (Fraction(1,6),Fraction(2,6),Fraction(3,6)),
                    (Fraction(1,10),Fraction(2,10),Fraction(3,10),Fraction(4,10)))
    for ps in iid_profiles:
        for m in range(1, 8):
            for j in range(len(ps)):
                tab = multinomial_joint(ps, m, j)
                checks += check_dominance(tab, ('iid',ps,m,j))
    comparisons = []
    for r in range(2, 8):
        m=r+1
        plus = cov_tag_r_wor((r+1,r+1),m,0,r)
        minus = cov_tag_r_wor((r,)+(1,)*(r+1),m,0,r)
        C = comb(2*r+2, r+1)
        assert plus == Fraction(2*(r+1)**2, C**2)
        assert plus>0 and minus<0
        comparisons.append((r,str(plus),str(minus)))
    print('PASS: all finite-population tagged-singleton stochastic orders for integer partitions N<=9')
    print('PASS: iid tagged-singleton stochastic orders for 3 nonuniform laws, m<=7')
    print('Number of exact stochastic order inequalities:', checks)
    print('Number of finite population abundance profiles:', profiles)
    print('Higher-frequency opposite-sign witnesses:', comparisons)

if __name__=='__main__':
    main()
