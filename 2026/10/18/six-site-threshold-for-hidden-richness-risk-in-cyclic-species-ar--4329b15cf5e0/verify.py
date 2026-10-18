"""Exact checks for contiguous-window richness on single-occupancy cyclic landscapes.

Run: python verify.py
No third-party modules or external data are required.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import json


def restricted_growth_words(n):
    """Enumerate all set partitions of n labelled sites as restricted-growth words."""
    if n < 1:
        return
    word = [0]
    def emit():
        if len(word) == n:
            yield tuple(word)
        else:
            for symbol in range(max(word) + 2):
                word.append(symbol)
                yield from emit()
                word.pop()
    yield from emit()


def window_distribution(word, m):
    n = len(word)
    doubled = word + word
    return Counter(len(set(doubled[start:start + m])) for start in range(n))


def species_detection_counts(word, m):
    n = len(word)
    doubled = word + word
    return tuple(sum(symbol in doubled[start:start + m]
                     for start in range(n))
                 for symbol in sorted(set(word)))


def richness_moments(word, m):
    n = len(word)
    h = window_distribution(word, m)
    mean = sum(k * count for k, count in h.items())
    square = sum(k * k * count for k, count in h.items())
    return Fraction(mean, n), Fraction(square, n) - Fraction(mean, n) ** 2


def pair_count(n, m, distance):
    return max(0, m - distance) + max(0, m - (n - distance))


def variance_formula(n, m, distance):
    p = Fraction(m, n)
    q = Fraction(pair_count(n, m, distance), n)
    return 2 * p * (1 - p) + 2 * (q - p * p)


def main():
    bell = {}
    signatures = {}
    for n in range(1, 6):
        found = defaultdict(set)
        total = 0
        for word in restricted_growth_words(n):
            total += 1
            profiles = [window_distribution(word, m) for m in range(1, n + 1)]
            mean_signature = tuple(sum(k * count for k, count in h.items())
                                   for h in profiles)
            distribution_signature = tuple(tuple(sorted(h.items())) for h in profiles)
            found[mean_signature].add(distribution_signature)
        assert all(len(distributions) == 1 for distributions in found.values())
        bell[str(n)] = total
        signatures[str(n)] = len(found)
    assert list(bell.values()) == [1, 2, 5, 15, 52]

    n = 6
    near = tuple('BACAAA')
    far = tuple('BAACAA')
    assert len(near) == len(far) == n
    for m in range(1, n + 1):
        assert species_detection_counts(near, m) == species_detection_counts(far, m)
    assert window_distribution(near, 3) == {1: 1, 2: 4, 3: 1}
    assert window_distribution(far, 3) == {2: 6}
    assert richness_moments(near, 3) == (Fraction(2), Fraction(1, 3))
    assert richness_moments(far, 3) == (Fraction(2), Fraction(0))

    formula_cases = 0
    probability_cases = 0
    for n in range(6, 41):
        for distance in range(2, n - 1):
            landscape = ['A'] * n
            landscape[0] = 'B'
            landscape[distance] = 'C'
            word = tuple(landscape)
            assert species_detection_counts(word, 1) == (n-2, 1, 1)
            for m in range(2, n + 1):
                assert species_detection_counts(word, m) == (n, m, m)
                p = Fraction(m, n)
                q = Fraction(pair_count(n, m, distance), n)
                target = {1: 1 - 2*p + q,
                          2: 2*p - 2*q,
                          3: q}
                empirical = window_distribution(word, m)
                assert all(Fraction(empirical.get(k, 0), n) == v
                           for k, v in target.items()), (n, distance, m)
                probability_cases += 1
                assert richness_moments(word, m)[1] == variance_formula(n, m, distance)
                formula_cases += 1
    differences = {}
    for n in range(6, 61):
        m = n // 2
        v_near = variance_formula(n, m, 2)
        v_far = variance_formula(n, m, m)
        expected = Fraction(2 * (m - 2), n)
        assert v_near - v_far == expected
        all_variances = [variance_formula(n, m, d) for d in range(2, n-1)]
        assert max(all_variances) - min(all_variances) == expected
        differences[str(n)] = [v_near.numerator, v_near.denominator,
                               v_far.numerator, v_far.denominator,
                               expected.numerator, expected.denominator]

    result = {
      'verification': 'PASS',
      'enumerated_site_partition_counts': bell,
      'distinct_mean_curve_counts': signatures,
      'first_witness': {
          'sites': 6,
          'near': ''.join(near),
          'far': ''.join(far),
          'm': 3,
          'near_histogram': dict(sorted(window_distribution(near, 3).items())),
          'far_histogram': dict(sorted(window_distribution(far, 3).items())),
          'variance_difference': '1/3'},
      'probability_distribution_formula_checks': probability_cases,
      'variance_formula_checks': formula_cases,
      'range_extremality_checks': 55,
      'even_60_variance_gap': str(Fraction(2 * (30 - 2), 60)),
      'maximal_full_gap_checked_through_sites': 60
    }
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    main()
