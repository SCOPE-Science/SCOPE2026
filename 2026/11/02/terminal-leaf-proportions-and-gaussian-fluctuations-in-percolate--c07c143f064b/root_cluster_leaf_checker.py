"""Standalone checks for root-cluster terminal leaves in percolated recursive trees.

Run with Python 3: python root_cluster_leaf_checker.py
Only finite checks and diagnostics are claimed; infinite-limit proofs are analytical.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, gamma, sqrt
from random import Random


def exact_dp(n, p):
    """Forward Markov recursion on component size and ORIGINAL-tree leaf count."""
    law = {(1, 1): Fraction(1)}
    for j in range(1, n):
        nxt = defaultdict(Fraction)
        for (c, l), w in law.items():
            nxt[(c, l)] += w * Fraction(j-c, j)
            nxt[(c+1, l)] += w * Fraction(l, j) * p
            nxt[(c, l-1)] += w * Fraction(l, j) * (1-p)
            nxt[(c+1, l+1)] += w * Fraction(c-l, j) * p
            nxt[(c, l)] += w * Fraction(c-l, j) * (1-p)
        law = {key: value for key, value in nxt.items() if value}
    assert sum(law.values()) == 1
    return law


def enumerate_full(n, p):
    """Independent enumeration of all recursive-tree parent lists and edge flags."""
    law = defaultdict(Fraction)
    for parents in product(*(range(i) for i in range(1, n))):
        inv_tree = Fraction(1, factorial(n-1))
        for retained in product((0, 1), repeat=n-1):
            component = [True] + [False]*(n-1)
            child_count = [0]*n
            w = inv_tree
            for i, (par, mark) in enumerate(zip(parents, retained), start=1):
                child_count[par] += 1
                component[i] = component[par] and bool(mark)
                w *= p if mark else 1-p
            c = sum(component)
            l = sum(1 for i in range(n) if component[i] and child_count[i] == 0)
            law[c, l] += w
    return {key: value for key, value in law.items() if value}


def verify_exact():
    assertions = 0
    ps = [Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1)]
    for p in ps:
        theta = p/(1+p)
        variance_coefficient = p*(2-p)/((1+p)**2*(p+2))
        mean_c = Fraction(1)
        for n in range(1, 11):
            if n > 1:
                mean_c *= (1 + p/Fraction(n-1))
            law = exact_dp(n, p)
            expected_c = sum(w*c for (c,l), w in law.items())
            expected_l = sum(w*l for (c,l), w in law.items())
            residual_mean = sum(w*(l-theta*c) for (c,l), w in law.items())
            residual_second = sum(w*(l-theta*c)**2 for (c,l), w in law.items())
            assert expected_c == mean_c
            assertions += 1
            if n >= 2:
                assert expected_l == theta*mean_c and residual_mean == 0
                assertions += 2
            if n >= 3:
                assert residual_second == variance_coefficient*mean_c
                assertions += 1
            if n <= 6:
                assert law == enumerate_full(n, p), (n,p)
                assertions += len(law)
    return assertions


def monte_carlo(p=0.7, n=6000, trials=1000, seed=1789):
    """Independent full-tree simulation; asymptotic diagnostics, not proof."""
    rng = Random(seed)
    theta = p/(1+p)
    coef = p*(2-p)/((p+1)**2*(p+2))
    zs = []
    ratios = []
    sizes = []
    for _ in range(trials):
        in_root = [True] + [False]*(n-1)
        has_child = [False]*n
        c = 1
        for i in range(1,n):
            j = rng.randrange(i)
            has_child[j] = True
            if in_root[j] and rng.random() < p:
                in_root[i] = True
                c += 1
        l = sum(int(in_root[k] and not has_child[k]) for k in range(n))
        zs.append((l-theta*c)/sqrt(c))
        ratios.append(l/c)
        sizes.append(c)
    mean = sum(zs)/trials
    var = sum((z-mean)**2 for z in zs)/trials
    mean_ratio = sum(ratios)/trials
    return {'n':n,'p':p,'trials':trials,'mean_component_size':sum(sizes)/trials,
            'mean_leaf_fraction':mean_ratio,'theory_fraction':theta,
            'scaled_residual_mean':mean,'scaled_residual_variance':var,
            'theory_residual_variance':coef}

if __name__ == '__main__':
    print('EXACT_ASSERTIONS',verify_exact())
    print('SIMULATION_DIAGNOSTIC',monte_carlo())
