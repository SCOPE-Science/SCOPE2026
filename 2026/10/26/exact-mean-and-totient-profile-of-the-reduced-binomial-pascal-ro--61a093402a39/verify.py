#!/usr/bin/env python3
"""Exact checks for reduced-binomial row deficit and its totient approximation."""
from fractions import Fraction
from math import comb, gcd, isqrt, pi


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def tau(n):
    return sum(n % d == 0 for d in range(1, n + 1))


def reduced_row_sum(n):
    return sum(comb(n // gcd(n, k), k // gcd(n, k)) for k in range(n + 1))


def coprime_binomial_weight(n):
    return sum(comb(n, k) for k in range(n + 1) if gcd(n, k) == 1)


def main():
    expected = [0, 0, 0, 4, 0, 42, 0, 116, 162, 730, 0, 2458, 0, 11494, 16890]
    values = []
    residue_checks = 0
    for n in range(1, 321):
        total = 1 << n
        reduced = reduced_row_sum(n)
        deficit = total - reduced
        if n <= len(expected):
            assert deficit == expected[n - 1], (n, deficit, expected[n - 1])
        assert 0 <= deficit < total
        r = Fraction(deficit, total)
        totient_model = Fraction(n - phi(n), n)
        coprime_mass = Fraction(coprime_binomial_weight(n), total)
        replacement_mass = Fraction(sum(comb(n // gcd(n, k), k // gcd(n, k))
                    for k in range(n + 1) if gcd(n, k) > 1), total)
        assert r == 1 - coprime_mass - replacement_mass
        assert replacement_mass <= Fraction(n + 1, 1 << (n // 2))
        mode_mass = Fraction(comb(n, n // 2), total)
        assert abs(coprime_mass - Fraction(phi(n), n)) <= 2 * tau(n) * mode_mass
        assert abs(r - totient_model) <= 2 * tau(n) * mode_mass + Fraction(n + 1, 1 << (n // 2))
        values.append(float(r))
        for d in range(1, n + 1):
            if n % d != 0:
                continue
            p = Fraction(sum(comb(n, k) for k in range(0, n + 1, d)), total)
            assert abs(p - Fraction(1, d)) <= 2 * mode_mass, (n, d)
            residue_checks += 1
    reference = 1 - 6 / pi**2
    print('VERIFY_OK: 320 exact reduced-binomial rows; '
          f'{residue_checks} residue-class inequalities; 15 OEIS initial values; '
          f'mean through 320 = {sum(values)/320:.12f}; '
          f'proposed exact limit = {reference:.12f}')


if __name__ == '__main__':
    main()
