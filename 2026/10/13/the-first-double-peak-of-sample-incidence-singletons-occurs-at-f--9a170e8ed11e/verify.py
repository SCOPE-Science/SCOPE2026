"""Exact finite certificate for sample-incidence singleton peak threshold.

Run: python3 verify_unique_peaks.py
Uses Python's standard library only. All equality and order comparisons are exact.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def species_profile(n, d):
    """Expected exactly-one appearance of a species occupying d sites."""
    assert 1 <= d <= n
    return tuple(
        Fraction(d * comb(n - d, k - 1), comb(n, k))
        if k - 1 <= n - d else Fraction(0)
        for k in range(1, n + 1)
    )


def strict_peaks(values):
    """Interior strict local maxima, with indices in 1-based sample size."""
    return tuple(
        k for k in range(2, len(values))
        if values[k - 2] < values[k - 1] > values[k]
    )


def full_census():
    examined = 0
    many = []
    monotone_cases = 0
    per_size = []
    for n in range(2, 16):
        profiles = {d: species_profile(n, d) for d in range(1, n + 1)}
        size_many = []
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                examined += 1
                values = tuple(x + y for x, y in zip(profiles[a], profiles[b]))
                peaks = strict_peaks(values)
                if len(peaks) >= 2:
                    item = (n, a, b, peaks)
                    many.append(item)
                    size_many.append(item)
                assert all(values[k - 1] / k >= values[k] / (k + 1)
                           for k in range(1, n)), (n, a, b, 'scaled')
                monotone_cases += 1
        per_size.append((n, n * (n + 1) // 2, len(size_many)))
    expected = [(n, n * (n + 1) // 2, (1 if n == 15 else 0))
                for n in range(2, 16)]
    assert per_size == expected, (per_size, expected)
    assert many == [(15, 2, 9, (2, 7))], many
    return examined, monotone_cases, per_size


def direct_witness_checks():
    """Independent exact subset census, for both disjoint and nested supports."""
    n, a, b = 15, 2, 9
    pred = tuple(x + y for x, y in zip(species_profile(n, a),
                                         species_profile(n, b)))
    expected = tuple(map(Fraction, [
        Fraction(11, 15), Fraction(16, 21), Fraction(291, 455),
        Fraction(752, 1365), Fraction(1565, 3003),
        Fraction(2628, 5005), Fraction(1147, 2145), Fraction(8, 15),
        Fraction(18, 35), Fraction(10, 21), Fraction(44, 105),
        Fraction(12, 35), Fraction(26, 105), Fraction(2, 15),
        Fraction(0)
    ]))
    assert pred == expected
    arrangements = [
        ((0, 1), tuple(range(2, 11))),
        ((0, 1), tuple(range(9))),
    ]
    examined = 0
    for first, second in arrangements:
        p = sum(1 << i for i in first)
        q = sum(1 << i for i in second)
        totals = [0] * (n + 1)
        counts = [0] * (n + 1)
        for mask in range(1 << n):
            k = mask.bit_count()
            counts[k] += 1
            totals[k] += ((mask & p).bit_count() == 1) + ((mask & q).bit_count() == 1)
            examined += 1
        assert tuple(Fraction(totals[k], counts[k])
                     for k in range(1, n + 1)) == pred
    assert strict_peaks(pred) == (2, 7)
    assert pred[3] > pred[4] < pred[5]
    assert pred[5] < pred[6] > pred[7]
    return examined


if __name__ == '__main__':
    pair_count, scale_count, table = full_census()
    subset_count = direct_witness_checks()
    print('VERIFY_OK census_pairs=%d scaled_profiles=%d direct_subsets=%d '
          'sole_two_peak_profile=(15,2,9) peaks=(2,7)' %
          (pair_count, scale_count, subset_count))
    print('SIZE_COUNTS', table)
