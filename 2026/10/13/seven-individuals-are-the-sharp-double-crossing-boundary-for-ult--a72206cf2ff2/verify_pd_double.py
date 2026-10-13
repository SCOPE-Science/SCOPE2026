"""Exact census of double reversals in three-tip ultrametric PD rarefaction.

Python 3 standard library only; no floating-point comparisons.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def profiles_by_sisters(n):
    """Positive counts, sister leaves unordered, outgroup leaf distinguished."""
    return tuple((a, b, n - a - b)
                 for a in range(1, n)
                 for b in range(a, n)
                 if n - a - b >= 1)


def profiles_independently(n):
    """Independent generator via every ordered positive composition."""
    return tuple(sorted({(min(a, b), max(a, b), c)
                         for a in range(1, n)
                         for b in range(1, n)
                         for c in range(1, n)
                         if a + b + c == n}))


def affine_missing(n, p, m):
    """Missing branch-length numerator: H*A + h*B."""
    a, b, c = p
    q1, q2, q3 = (choose(n - v, m) for v in p)
    return q1 + q2 + q3, choose(c, m) - q1 - q2


def diff_affine(n, x, y):
    xx = [affine_missing(n, x, m) for m in range(2, n)]
    yy = [affine_missing(n, y, m) for m in range(2, n)]
    return tuple((a - c, b - d) for (a, b), (c, d) in zip(xx, yy))


def sign_changes(coeffs, t):
    signs = []
    for a, b in coeffs:
        v = Fraction(a) + t * b
        if v > 0:
            signs.append(1)
        elif v < 0:
            signs.append(-1)
    return sum(u != v for u, v in zip(signs, signs[1:]))


def sample_positions(coeffs):
    """All real t in (0,1) are covered by affine sign cells and roots."""
    roots = {Fraction(0), Fraction(1)}
    for a, b in coeffs:
        if b:
            z = -Fraction(a, b)
            if 0 < z < 1:
                roots.add(z)
    roots = sorted(roots)
    result = []
    for lo, hi in zip(roots, roots[1:]):
        result.append((lo + hi) / 2)
    result.extend(t for t in roots if 0 < t < 1)
    return tuple(result)


def expected_pd(n, p, m, height, internal):
    # Rooted three-tip tree ((1,2),3), root-to-sister-ancestor internal,
    # two sister pendant edges height-internal, outgroup edge height.
    a, b, c = p
    branches = ((a, height-internal), (b, height-internal),
                (c, height), (a+b, internal))
    return sum(Fraction(length * (choose(n, m) - choose(n-count, m)),
                        choose(n, m)) for count, length in branches)


def direct_pd(n, p, m, height, internal):
    taxa = (0,)*p[0] + (1,)*p[1] + (2,)*p[2]
    total = 0
    for positions in combinations(range(n), m):
        selected = {taxa[i] for i in positions}
        total += (height-internal) * (int(0 in selected) + int(1 in selected))
        total += height * int(2 in selected)
        total += internal * int(bool(selected & {0, 1}))
    return Fraction(total, choose(n, m))


def verify():
    expected_intervals = {
        ((1, 1, 5), (3, 3, 1)): (Fraction(1, 2), Fraction(13, 23)),
        ((1, 2, 4), (3, 3, 1)): (Fraction(1, 7), Fraction(3, 17)),
        ((1, 4, 2), (3, 3, 1)): (Fraction(1, 5), Fraction(3, 13)),
    }
    expected_sizes = {3: 1, 4: 2, 5: 4, 6: 6, 7: 9}
    pairs_checked = 0
    param_cells_checked = 0
    observed_first = {}
    direct_checks = 0

    for n in range(3, 8):
        profiles = tuple(sorted(profiles_by_sisters(n)))
        assert profiles == profiles_independently(n)
        assert len(profiles) == expected_sizes[n]

        # Independent microscopic outcome enumeration validates the edge method.
        for profile in profiles:
            for m in range(1, n+1):
                assert expected_pd(n, profile, m, 9, 2) == direct_pd(n, profile, m, 9, 2)
                direct_checks += 1

        for x, y in combinations(profiles, 2):
            pairs_checked += 1
            coeffs = diff_affine(n, x, y)
            goal = expected_intervals.get((x, y)) if n == 7 else None
            for t in sample_positions(coeffs):
                param_cells_checked += 1
                actual = sign_changes(coeffs, t) >= 2
                predicted = goal is not None and goal[0] < t < goal[1]
                assert actual == predicted, (n, x, y, t, coeffs, actual, predicted)
                if actual:
                    observed_first[(x, y)] = goal

    assert observed_first == expected_intervals
    witness_a, witness_b = (1, 4, 2), (3, 3, 1)
    assert diff_affine(7, witness_a, witness_b) == (
        (1, -5), (3, -13), (3, -13), (1, -6), (0, -1))
    expected_diff = (Fraction(1, 21), Fraction(-1, 35),
                     Fraction(-1, 35), Fraction(1, 7), Fraction(2, 7))
    observed_diff = tuple(expected_pd(7, witness_a, m, 9, 2)
                          - expected_pd(7, witness_b, m, 9, 2)
                          for m in range(2, 7))
    assert observed_diff == expected_diff
    assert expected_pd(7, witness_a, 1, 9, 2) == 9
    assert expected_pd(7, witness_b, 1, 9, 2) == 9
    assert expected_pd(7, witness_a, 7, 9, 2) == 25
    assert expected_pd(7, witness_b, 7, 9, 2) == 25

    print('VERIFY_OK')
    print('profile_counts=', expected_sizes)
    print('unordered_pairs=', pairs_checked)
    print('real_parameter_cells=', param_cells_checked)
    print('direct_subset_checks=', direct_checks)
    print('crossing_type_intervals=', observed_first)
    print('witness_PD_differences_m2_to_m6=', expected_diff)


if __name__ == '__main__':
    verify()
