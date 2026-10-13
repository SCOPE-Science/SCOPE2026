#!/usr/bin/env python3
"""Recompute the sharp two-species zeta-retention turning threshold exactly.

Requires only Python 3 standard library. All comparisons are integer or rational.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def zeta_num(r, s, k):
    return (comb(r, k) if k <= r else 0) + (comb(s, k) if k <= s else 0)


def turn_signs(n, r, s):
    a = [zeta_num(r, s, k) for k in range(s + 1)]
    b = [comb(n, k) for k in range(s + 1)]
    signs = []
    for k in range(1, s - 1):
        # Sign of R_(k+1)-R_k, all cleared denominators positive.
        certificate = a[k] * a[k + 2] * b[k + 1] ** 2 - a[k + 1] ** 2 * b[k] * b[k + 2]
        signs.append((certificate > 0) - (certificate < 0))
    return signs


def turn_count(signs):
    nonzero = [t for t in signs if t]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def fraction_ratios(n, r, s):
    zeta = [Fraction(zeta_num(r, s, k), comb(n, k)) for k in range(1, s + 1)]
    return [zeta[k + 1] / zeta[k] for k in range(s - 1)]


def main():
    total_lower, total_at29 = 0, 0
    winners = []
    for n in range(2, 30):
        for s in range(2, n + 1):
            for r in range(1, s):
                signs = turn_signs(n, r, s)
                count = turn_count(signs)
                if n < 29:
                    total_lower += 1
                    assert count <= 1, (n, r, s, count)
                else:
                    total_at29 += 1
                    if count >= 2:
                        winners.append((r, s, count))
        
    assert total_lower == comb(29, 3) == 3654
    assert total_at29 == comb(29, 2) == 406
    assert winners == [(22, 26, 2)]

    n, r, s = 29, 22, 26
    ratios = fraction_ratios(n, r, s)
    assert ratios[:5] == [
        Fraction(139, 168), Fraction(115, 139), Fraction(4453, 5382),
        Fraction(92114, 111325), Fraction(27713, 33496),
    ]
    differences = [ratios[k + 1] - ratios[k] for k in range(4)]
    assert differences == [
        Fraction(-1, 23352), Fraction(37, 748098),
        Fraction(27323, 599151150), Fraction(-300819, 3728942200),
    ]
    for k, diff in enumerate(differences, 1):
        assert ((diff > 0) - (diff < 0)) == turn_signs(n, r, s)[k - 1]

    # Direct incidence-subset recount independent of the choose(r,k) formula.
    habitats = set(range(1, 30))
    species_a = set(range(1, 23))
    species_b = set(range(4, 30))
    assert species_a | species_b == habitats
    counted = 0
    for k in range(1, 6):
        numerator = 0
        for sample in combinations(range(1, n + 1), k):
            counted += 1
            subset = set(sample)
            numerator += (subset <= species_a) + (subset <= species_b)
        assert numerator == zeta_num(r, s, k)

    # Independently verify the general weighted-variance identity on
    # several multispecies occupancy profiles, including singleton coverage.
    profiles = [
        (29, [22, 26]), (17, [2, 9, 11, 14]),
        (10, [1, 1, 1, 10]), (12, [3, 3, 6, 9, 12]),
    ]
    verified_curvatures = 0
    for n, occ in profiles:
        z = [Fraction(sum(comb(t, k) if t >= k else 0 for t in occ), comb(n, k))
             for k in range(1, min(n, max(occ) + 1) + 1)]
        for k in range(1, min(n - 2, max(occ) - 1) + 1):
            if z[k] == 0:
                continue
            active = [(t, comb(t, k) if t >= k else 0) for t in occ]
            total = sum(w for _, w in active)
            mu = Fraction(sum(t * w for t, w in active), total)
            var = sum(Fraction(w, total) * (t - mu) ** 2 for t, w in active)
            assert mu > k
            lhs = z[k + 1] / z[k] - z[k] / z[k - 1]
            rhs = ((n - k) * var - (mu - k) * (n - mu)) / ((n - k) * (mu - k) * (n - k - 1))
            assert lhs == rhs, (n, occ, k, lhs, rhs)
            verified_curvatures += 1

    print(f'VERIFY_OK lower_pairs={total_lower} boundary_pairs={total_at29} '
          f'unique_pair={winners[0][:2]} direct_subsets={counted} '
          f'weighted_curvature_identities={verified_curvatures}')


if __name__ == '__main__':
    main()
