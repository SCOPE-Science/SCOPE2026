#!/usr/bin/env python3
"""Standalone exact-arithmetic finite checks of spoke-weighted wheel equilibria.

For every listed rational spoke weight and each m in 3..14, enumerate every
binary action profile on the wheel (including both choices of the hub).
Compare Nash equilibrium multiplicities, strict Nash counts, realized
welfare levels, and global weighted-cut maxima with closed formulas.
Finite verification supports, but does not replace, the general proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def perrin(m):
    p = [3, 0, 2]
    for j in range(3, m + 1):
        p.append(p[j - 2] + p[j - 3])
    return p[m]


def lucas(m):
    l = [2, 1]
    for j in range(2, m + 1):
        l.append(l[j - 1] + l[j - 2])
    return l[m]


def multiplicity(m, lam):
    if lam < 2:
        return {
            z: 2 * m * comb(z, m - 2 * z) // z
            for z in range((m + 2) // 3, m // 2 + 1)
        }
    if lam == 2:
        return {
            z: 2 * m * comb(m - z, z) // (m - z)
            for z in range(0, m // 2 + 1)
        }
    return {0: 2}


def optimum(m, lam):
    return lam * m + max(Fraction(0), Fraction(2) - lam) * (m // 2)


def brute_force(m, lam):
    levels = Counter()
    strict_count = 0
    all_max = Fraction(0)
    equilibria_cuts = set()
    for hub in (0, 1):
        for mask in range(1 << m):
            bits = [(mask >> i) & 1 for i in range(m)]
            x = [int(bit != hub) for bit in bits]
            ones = sum(x)
            zeros = m - ones
            rim_cut = sum(x[i] != x[(i + 1) % m] for i in range(m))
            cut = lam * ones + rim_cut
            all_max = max(all_max, cut)
            hub_strict = ones > zeros
            if ones < zeros:
                continue
            margins = []
            for i in range(m):
                left, right = x[(i - 1) % m], x[(i + 1) % m]
                opposite = (left != x[i]) + (right != x[i])
                current = opposite + (lam if x[i] else 0)
                changed = 2 - opposite + (0 if x[i] else lam)
                margins.append(current - changed)
            if any(a < 0 for a in margins):
                continue
            levels[zeros] += 1
            strict_count += int(hub_strict and all(a > 0 for a in margins))
            equilibria_cuts.add(cut)

    expected = multiplicity(m, lam)
    assert dict(levels) == expected, (m, lam, dict(levels), expected)
    if lam < 2:
        assert sum(levels.values()) == 2 * perrin(m)
        expected_strict = 2 * (perrin(m) - (2 if m % 2 == 0 else 0))
        assert equilibria_cuts == {
            lam * m + (2 - lam) * z for z in expected
        }
    elif lam == 2:
        assert sum(levels.values()) == 2 * lucas(m)
        expected_strict = 0
        assert equilibria_cuts == {2 * m}
    else:
        assert sum(levels.values()) == 2
        expected_strict = 2
        assert equilibria_cuts == {lam * m}
    assert strict_count == expected_strict, (m, lam, strict_count, expected_strict)
    assert all_max == optimum(m, lam), (m, lam, all_max, optimum(m, lam))
    assert all_max in equilibria_cuts
    minimum_cut = min(equilibria_cuts)
    if lam < 2:
        assert minimum_cut == lam * m + (2 - lam) * ((m + 2) // 3)
    else:
        assert minimum_cut == all_max
    return (2 << m)


def main():
    cases = 0
    profiles = 0
    for m in range(3, 15):
        for lam in (Fraction(1, 2), Fraction(1), Fraction(199, 100),
                    Fraction(2), Fraction(201, 100), Fraction(5)):
            profiles += brute_force(m, lam)
            cases += 1
    # A second exact check on counts far beyond enumeration range.
    for m in range(3, 300):
        assert sum(multiplicity(m, Fraction(1)).values()) == 2 * perrin(m)
        assert sum(multiplicity(m, Fraction(2)).values()) == 2 * lucas(m)
    print(f'PASS {cases} wheel/weight cases; {profiles} full profiles;')
    print('PASS exact multiplicity/Perrin/Lucas recurrences through m=299;')
    print('PASS equilibrium welfare spectra, maximum cut, strict equilibria.')


if __name__ == '__main__':
    main()
