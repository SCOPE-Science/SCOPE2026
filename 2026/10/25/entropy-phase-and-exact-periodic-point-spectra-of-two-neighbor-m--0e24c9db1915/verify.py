#!/usr/bin/env python3
"""Exact finite checks of cyclic-mask and periodic-point identities."""
from math import comb, gcd


def masks(m):
    out = []
    forbidden = {1, 2, m - 1, m - 2}
    for mask in range(1 << m):
        support = [i for i in range(m) if mask & (1 << i)]
        if all((a - b) % m not in forbidden for j, a in enumerate(support)
               for b in support[j + 1:]):
            out.append(mask)
    return out


def shift(mask, m):
    return ((mask << 1) | (mask >> (m - 1))) & ((1 << m) - 1)


def orbit_periods(m):
    valid = masks(m)
    best = max(x.bit_count() for x in valid)
    rem = {x for x in valid if x.bit_count() == best}
    periods = []
    while rem:
        start = next(iter(rem))
        x = start
        orbit = []
        while x not in orbit:
            orbit.append(x)
            x = shift(x, m)
        assert x == start
        rem.difference_update(orbit)
        periods.append(len(orbit))
    return best, sorted(periods)


def theoretical_periods(m):
    k, r = divmod(m, 3)
    if r == 0:
        return k, [3]
    if r == 1:
        return k, [m]
    count = 1 + k // 2
    if k % 2 == 0:
        return k, sorted([m // 2] + [m] * (count - 1))
    return k, [m] * count


def exact_fixed_points(m, n):
    g = gcd(m, n)
    q = (1 << (n // g)) - 1
    return 1 + sum(g * comb(g - 2 * j - 1, j - 1) // j * q**j
                   for j in range(1, g // 3 + 1))


def direct_fixed_points(m, n):
    # Periodic words repeat with common length lcm(m,n); their residue support
    # must avoid all forbidden differences on the full two-sided orbit.
    L = m * n // gcd(m, n)
    bad = {1, 2, m - 1, m - 2}
    count = 0
    for word in range(1 << n):
        positions = [i for i in range(L) if word & (1 << (i % n))]
        occupied = {i % m for i in positions}
        if all((a - b) % m not in bad for a in occupied
               for b in occupied if a != b):
            count += 1
    return count


def main():
    for m in range(3, 17):
        assert orbit_periods(m) == theoretical_periods(m), m
    tested = 0
    for m in range(3, 13):
        for n in range(1, 13):
            left = direct_fixed_points(m, n)
            right = exact_fixed_points(m, n)
            assert left == right, (m, n, left, right)
            tested += 1
    print('VERIFY_OK: 14 mask-orbit moduli and', tested,
          'independent exact periodic-point comparisons')


if __name__ == '__main__':
    main()
