"""Direct finite tests for outcome fibers of farthest-free parking.

Run with Python 3: python verify.py
This is finite corroboration; the unrestricted theorem is proved separately.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial, prod


def direct_outcome(preferences):
    """Simulate the parking rule literally, independently of the fiber formula."""
    available = set(range(1, len(preferences) + 1))
    outcome = []
    for preferred in preferences:
        if preferred in available:
            destination = preferred
        else:
            higher_open = [v for v in available if v > preferred]
            if not higher_open:
                return None
            destination = max(higher_open)
        available.remove(destination)
        outcome.append(destination)
    return tuple(outcome)


def predicted_fiber(outcome):
    n = len(outcome)
    multiplier = 1
    suffix_max = 0
    right_maxima = 0
    for i in range(n-1, -1, -1):
        value = outcome[i]
        if value > suffix_max:
            multiplier *= value - n + i + 1
            suffix_max = value
            right_maxima += 1
    return multiplier, right_maxima


def odd_double_factorial(n):
    return prod(range(1, 2 * n, 2))


for n in range(1, 8):
    direct = Counter()
    successful = 0
    for preferences in product(range(1, n + 1), repeat=n):
        outcome = direct_outcome(preferences)
        if outcome is not None:
            direct[outcome] += 1
            successful += 1
    assert len(direct) == factorial(n), (n, len(direct))
    assert successful == odd_double_factorial(n), (n, successful)

    maximum = max((k + 1) ** (n - k) for k in range(n))
    predicted_maximizers = set()
    for k in range(n):
        if (k + 1) ** (n - k) == maximum:
            for first in permutations(range(1, k + 1)):
                predicted_maximizers.add(first + tuple(range(n, k, -1)))

    actual_maximizers = set()
    for outcome in permutations(range(1, n + 1)):
        factor, records = predicted_fiber(outcome)
        assert direct[outcome] == factor, (n, outcome, direct[outcome], factor)
        k = n - records
        assert factor <= (k + 1) ** records
        extremal_at_records = (factor == (k + 1) ** records)
        has_required_shape = (
            set(outcome[:k]) == set(range(1, k + 1))
            and outcome[k:] == tuple(range(n, k, -1))
        )
        assert extremal_at_records == has_required_shape, (n, outcome)
        if factor == maximum:
            actual_maximizers.add(outcome)
    assert predicted_maximizers == actual_maximizers
    print('n=%d successful=%d distinct_outcomes=%d maximum_fiber=%d maximal_outcomes=%d OK' % (
        n, successful, len(direct), maximum, len(actual_maximizers)))
print('VERIFY_OK')
