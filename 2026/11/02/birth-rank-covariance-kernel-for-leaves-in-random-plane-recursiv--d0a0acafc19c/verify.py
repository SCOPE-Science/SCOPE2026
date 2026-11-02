"""Exact independent checks of birth-label leaf moments in ordered recursive trees.

Uses the standard library only. Run: python verify.py
Finite checks corroborate the separate all-size proof; they are not that proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, prod

checks = 0

def require(statement):
    global checks
    assert statement
    checks += 1


def odd_double_factorial(n):
    return prod(2 * k - 1 for k in range(1, n + 1))


def leaf_masks_from_stirling(n):
    words = [(1, 1)]
    for label in range(2, n + 1):
        words = [w[:gap] + (label, label) + w[gap:]
                 for w in words for gap in range(2 * label - 1)]
    counts = Counter()
    for w in words:
        mask = 0
        for i in range(1, n + 1):
            if any(w[k] == i == w[k + 1] for k in range(2 * n - 1)):
                mask |= 1 << (i - 1)
        counts[mask] += 1
    require(sum(counts.values()) == odd_double_factorial(n))
    return counts


def leaf_masks_from_parent_arrays(n):
    # Each increasing parent array supports exactly prod_v degree(v)! orderings.
    counts = Counter()
    for parents in product(*(range(i) for i in range(1, n + 1))):
        degrees = [0] * (n + 1)
        for parent in parents:
            degrees[parent] += 1
        weight = prod(factorial(deg) for deg in degrees)
        mask = sum(1 << (i - 1) for i in range(1, n + 1)
                   if degrees[i] == 0)
        counts[mask] += weight
    require(sum(counts.values()) == odd_double_factorial(n))
    return counts


def predicted_joint(n, subset):
    value = Fraction(1)
    for t in range(2, n + 1):
        active = sum(i < t for i in subset)
        value *= Fraction(2 * t - 1 - active, 2 * t - 1)
    return value


def predicted_single(n, i):
    return prod((Fraction(2 * t - 2, 2 * t - 1)
                 for t in range(i + 1, n + 1)), start=Fraction(1))


def predicted_pair_cov(n, i, j):
    assert 1 <= i < j <= n
    r = prod((Fraction(4 * k * k - 1, 4 * k * k)
              for k in range(j, n)), start=Fraction(1))
    return predicted_single(n, i) * predicted_single(n, j) * (r - 1)


for n in range(1, 8):
    stirling = leaf_masks_from_stirling(n)
    parents = leaf_masks_from_parent_arrays(n)
    require(stirling == parents)
    den = odd_double_factorial(n)
    probabilities = {m: Fraction(weight, den) for m, weight in stirling.items()}
    for subset_mask in range(1 << n):
        subset = [i for i in range(1, n + 1) if subset_mask & (1 << (i - 1))]
        actual = sum((v for m, v in probabilities.items()
                      if (m & subset_mask) == subset_mask), Fraction(0))
        require(actual == predicted_joint(n, subset))
    for i in range(1, n + 1):
        actual_i = sum((v for m, v in probabilities.items()
                        if (m & (1 << (i - 1)))), Fraction(0))
        require(actual_i == predicted_single(n, i))
        for j in range(i + 1, n + 1):
            actual_both = sum((v for m, v in probabilities.items()
                               if (m & (1 << (i - 1))) and
                               (m & (1 << (j - 1)))), Fraction(0))
            actual_j = sum((v for m, v in probabilities.items()
                            if (m & (1 << (j - 1)))), Fraction(0))
            require(actual_both - actual_i * actual_j ==
                    predicted_pair_cov(n, i, j))
            require((actual_both < actual_i * actual_j) == (j < n))
    mean = sum((v * m.bit_count() for m, v in probabilities.items()), Fraction(0))
    second = sum((v * m.bit_count() ** 2 for m, v in probabilities.items()), Fraction(0))
    require(mean == Fraction(2 * n + 1, 3))
    require(second - mean * mean == Fraction(2 * (n * n - 1), 9 * (2 * n - 1)))
    print(f"n={n}: {den} plane recursive trees; independent models and exact moments agree")

# Additional all-parameter exact finite-n comparisons of the product formulas.
for n in range(8, 41):
    marginals = [predicted_single(n, i) for i in range(1, n + 1)]
    require(marginals[-1] == 1)
    require(sum(marginals) == Fraction(2 * n + 1, 3))
    # Check covariance-based variance against the established exact leaf variance.
    variance = sum((p * (1 - p) for p in marginals), Fraction(0))
    variance += 2 * sum((predicted_pair_cov(n, i, j)
                         for i in range(1, n + 1)
                         for j in range(i + 1, n + 1)), Fraction(0))
    require(variance == Fraction(2 * (n * n - 1), 9 * (2 * n - 1)))

print(f"PASS: {checks} independently cross-checked exact assertions")
