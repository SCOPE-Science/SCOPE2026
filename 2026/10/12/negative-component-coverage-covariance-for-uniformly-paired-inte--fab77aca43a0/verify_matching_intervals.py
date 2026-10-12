#!/usr/bin/env python3
"""Finite exact-rational checks for coverage by uniformly paired intervals.

Uses the Python standard library only. Matching enumeration is exhaustive for
n=2,...,7 but is not the proof for arbitrary n or arbitrary endpoint laws.
"""
from fractions import Fraction
from math import comb


def all_matchings(indices):
    if not indices:
        yield ()
        return
    first = indices[0]
    for j in range(1, len(indices)):
        partner = indices[j]
        for rest in all_matchings(indices[1:j] + indices[j + 1:]):
            yield ((first, partner),) + rest


def cut_probability(a, b):
    return Fraction(comb(a, b), comb(2 * a, 2 * b))


def predicted(n, gaps):
    probabilities = [cut_probability(n, j) for j in range(1, n)]
    c = []
    for j in range(1, n):
        covariance = probabilities[j - 1] * (1 - probabilities[j - 1])
        for i in range(1, n):
            if i == j:
                continue
            small, large = sorted((i, j))
            covariance += cut_probability(n, large) * (
                cut_probability(large, small) - cut_probability(n, small)
            )
        c.append(covariance)
    return 1 + sum(probabilities), sum(c), c, -sum(
        Fraction(gaps[2 * j - 1]) * c[j - 1] for j in range(1, n)
    )


def geometrical_union(pairs, positions):
    intervals = sorted((positions[a], positions[b]) for a, b in pairs)
    count = 0
    length = 0
    left = right = None
    for a, b in intervals:
        if left is None:
            left, right = a, b
        elif a <= right:
            right = max(right, b)
        else:
            count += 1
            length += right - left
            left, right = a, b
    count += 1
    length += right - left
    return count, length


def empirical(n, gaps):
    positions = [0]
    for gap in gaps:
        positions.append(positions[-1] + gap)
    seen = s_k = s_k2 = s_v = s_kv = 0
    s_z = [0] * (n - 1)
    s_zz = [[0] * (n - 1) for _ in range(n - 1)]
    for pairs in all_matchings(tuple(range(2 * n))):
        k, v = geometrical_union(pairs, positions)
        indicators = []
        for j in range(1, n):
            split = 2 * j
            indicators.append(int(all(
                (a < split and b < split) or (a >= split and b >= split)
                for a, b in pairs
            )))
        assert k == 1 + sum(indicators)
        assert v == positions[-1] - positions[0] - sum(
            gaps[2 * j - 1] * indicators[j - 1] for j in range(1, n)
        )
        seen += 1
        s_k += k
        s_k2 += k * k
        s_v += v
        s_kv += k * v
        for j in range(n - 1):
            s_z[j] += indicators[j]
            for i in range(n - 1):
                s_zz[j][i] += indicators[j] * indicators[i]
    ek = Fraction(s_k, seen)
    variance = Fraction(s_k2, seen) - ek * ek
    covariance = Fraction(s_kv, seen) - ek * Fraction(s_v, seen)
    for j in range(1, n):
        assert Fraction(s_z[j - 1], seen) == cut_probability(n, j)
        for i in range(1, j):
            assert Fraction(s_zz[i - 1][j - 1], seen) == (
                cut_probability(n, j) * cut_probability(j, i)
            )
    return seen, ek, variance, covariance


def main():
    checks = 0
    for n in range(2, 8):
        for gaps in ([1] * (2 * n - 1), [2 + j * j for j in range(1, 2 * n)]):
            _, ek, variance, covariance = empirical(n, gaps)
            expected_ek, expected_variance, contributions, expected_covariance = predicted(n, gaps)
            assert ek == expected_ek
            assert variance == expected_variance
            assert covariance == expected_covariance
            assert covariance < 0
            assert all(x > 0 for x in contributions)
            if len(set(gaps)) == 1:
                assert covariance == -variance
            checks += 1
        # Expected spacing of 2n iid uniform observations is 1/(2n+1).
        expected_covariance = predicted(n, [Fraction(1, 2*n+1)] * (2*n-1))[-1]
        assert expected_covariance == -predicted(n, [1] * (2*n-1))[1] / (2*n+1)
    print('VERIFY_OK exhaustive_matching_sizes=2..7 exact_geometric_cases=12 uniform_spacing_identities=6')


if __name__ == '__main__':
    main()
