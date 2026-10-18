"""Exact chamber-count checks for star-graph simplex-sum polytopes.

Python standard library only. Finite checks supplement, not replace, proofs.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, exp, factorial, lgamma, log


def vertex_from_winners(n, m, descending_order):
    """Add the exposed vertices of each included coordinate simplex."""
    rank = {x: i for i, x in enumerate(descending_order)}
    coords = [1] * (n + 1)  # singleton simplices
    for length in range(2, min(n + 1, m + 1) + 1):
        for leaves in combinations(range(1, n + 1), length - 1):
            candidates = (0,) + leaves
            winner = min(candidates, key=rank.__getitem__)
            coords[winner] += 1
    return tuple(coords)


def predicted_class(n, m, descending_order):
    higher = descending_order[:descending_order.index(0)]
    return frozenset(higher) if m == 1 else tuple(higher)


def exact_tests():
    cases = 0
    rankings = 0
    for n in range(1, 7):
        for m in range(1, n + 1):
            classes = {}
            counts = Counter()
            seen_vertices = Counter()
            for order in permutations(range(n + 1)):
                key = predicted_class(n, m, order)
                v = vertex_from_winners(n, m, order)
                if key in classes:
                    assert classes[key] == v
                else:
                    classes[key] = v
                counts[key] += 1
                seen_vertices[v] += 1
                rankings += 1
            assert len(classes) == len(seen_vertices)
            expected_vertices = (2 ** n if m == 1 else
                                 sum(factorial(n) // factorial(j) for j in range(n + 1)))
            assert len(classes) == expected_vertices
            for key, actual in counts.items():
                k = len(key)
                expected = factorial(n - k)
                if m == 1:
                    expected *= factorial(k)
                assert actual == expected
            assert sorted(seen_vertices.values()) == sorted(counts.values())
            denom = factorial(n + 1) ** 2
            collision = Fraction(sum(x * x for x in counts.values()), denom)
            if m == 1:
                numerator = factorial(n) * sum(
                    factorial(k) * factorial(n-k) for k in range(n+1))
            else:
                numerator = factorial(n) * sum(factorial(j) for j in range(n+1))
            assert collision == Fraction(numerator, denom)
            assert sum(counts.values()) == factorial(n+1)
            cases += 1
    return cases, rankings


def log_mean_exp(values):
    peak = max(values)
    return peak + log(sum(exp(a - peak) for a in values) / len(values))


def h(x):
    if x == 0 or x == 1:
        return 0.0
    return -x * log(x) - (1 - x) * log(1 - x)


def numerical_tests():
    # Verify both prelimit partition functions converge to the intended
    # Riemann integrals without using the simplex-sum enumeration code.
    for t in (-2.0, -0.5, 0.7, 2.0):
        n = 1500
        left = log_mean_exp([-t * (lgamma(n+1) - lgamma(k+1) - lgamma(n-k+1))/n
                             for k in range(n+1)]) - t*log(n+1)/n
        # Trapezoidal numerical integral for the limiting function.
        slices = 12000
        integral = sum((0.5 if j in (0, slices) else 1) *
                       exp(-t*h(j/slices)) for j in range(slices+1))/slices
        assert abs(exp(left) - integral) < 0.025, (t, exp(left), integral)
        right = log_mean_exp([t * (lgamma(j+1) - lgamma(n+2))/(n*log(n))
                              for j in range(n+1)])
        target = (1-exp(-t))/t
        # The refined-fan prelimit has a slowly decaying O(1/log n)
        # correction. This broad finite-n tolerance is only a sanity check,
        # not a proof or a certified asymptotic error bound.
        assert abs(exp(right) - target) < 0.35, (t, exp(right), target)


if __name__ == '__main__':
    case_count, ranking_count = exact_tests()
    numerical_tests()
    print('PASS: exact all-cutoff chamber/vertex/collision checks',
          case_count, 'parameter cases,', ranking_count, 'rankings')
    print('PASS: finite critical-window partition function checks')
