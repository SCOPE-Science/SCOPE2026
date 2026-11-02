"""Exact-rational checks for paired-seat variance-optimal apportionment.

Run: python verify.py
Optional independent floating-point LP benchmark: python verify.py --lp
The exact all-population optimality and uniqueness are proved algebraically
in RESULT.md; finite computation is not a substitute for that proof.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import sys


def optimal_lottery(n):
    assert n >= 3
    probabilities = {}
    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            probabilities[(i, n + 1 - i)] = Q(2, n)
    else:
        h = n // 2
        for i in range(1, h):
            probabilities[(i, n + 1 - i)] = Q(2, n)
        for ij in ((h, h + 1), (h, h + 2), (h + 1, h + 2)):
            probabilities[ij] = Q(1, n)
    return probabilities


def envy(n, pair):
    a, b = pair
    assert 1 <= a < b <= n
    direct = sum(i > j and i not in pair
                 for j in pair for i in range(1, n + 1))
    formula = 2 * n - a - b - 1
    assert direct == formula
    return formula


def verify(n):
    lottery = optimal_lottery(n)
    assert sum(lottery.values(), Q()) == 1
    assert all(sum((prob for pair, prob in lottery.items() if i in pair), Q())
               == Q(2, n) for i in range(1, n + 1))
    mean = sum((p * envy(n, ij) for ij, p in lottery.items()), Q())
    assert mean == n - 2
    distribution = defaultdict(lambda: Q())
    for pair, prob in lottery.items():
        distribution[envy(n, pair)] += prob
    variance = sum((p * (envy(n, ij) - mean) ** 2
                    for ij, p in lottery.items()), Q())
    predicted = Q(0) if n % 2 == 0 else Q(2, n)
    assert variance == predicted
    if n % 2 == 0:
        assert dict(distribution) == {n - 2: Q(1)}
    else:
        assert dict(distribution) == {
            n - 3: Q(1, n),
            n - 2: Q(n - 2, n),
            n - 1: Q(1, n),
        }
    # Dual lower-bound certificate: each pair involving the center
    # has squared deviation at least one; all other pairs have nonnegative
    # squared deviation. The center's inclusion marginal is 2/n.
    center = (n + 1) // 2 if n % 2 else None
    all_pairs = list(combinations(range(1, n + 1), 2))
    if center is not None:
        assert all((a + b - n - 1) ** 2 >= int(center in (a, b))
                   for a, b in all_pairs)
    uniform_probability = Q(1, comb(n, 2))
    anonymous_variance = sum((uniform_probability *
                              (envy(n, pair) - mean) ** 2
                              for pair in all_pairs), Q())
    assert anonymous_variance == Q((n + 1) * (n - 2), 6)
    return len(lottery), variance, anonymous_variance


def lp_benchmark():
    import numpy as np
    from scipy.optimize import linprog
    for n in range(3, 19):
        pairs = list(combinations(range(1, n + 1), 2))
        costs = [(a + b - n - 1) ** 2 for a, b in pairs]
        matrix = np.zeros((n, len(pairs)))
        for j, (a, b) in enumerate(pairs):
            matrix[a - 1, j] = matrix[b - 1, j] = 1
        result = linprog(costs, A_eq=matrix,
                         b_eq=np.full(n, 2.0 / n),
                         bounds=(0, None), method='highs')
        assert result.success
        target = 0 if n % 2 == 0 else 2 / n
        assert abs(result.fun - target) < 1e-8
    print('independent LP optimum checks: n=3..18 passed')


def main():
    for n in range(3, 101):
        verify(n)
    print('exact-rational feasibility, moments, distributions, dual checks, '
          'and anonymity benchmarks: n=3..100 passed')
    for n in (3, 4, 5, 6, 7, 10, 11):
        print('n=%d support=%d optimum_variance=%s anonymous_variance=%s' %
              ((n,) + (verify(n)[0], str(verify(n)[1]), str(verify(n)[2]))))
    if '--lp' in sys.argv:
        lp_benchmark()


if __name__ == '__main__':
    main()
