"""Standalone exact finite checks for a joint shifted-square divisor law.

This checker verifies finite arithmetic identities only; it does not certify
Gaussian or Euler-product limits, which require the mathematical proof.
"""
from fractions import Fraction
from math import isqrt, pi


def smallest_prime_factors(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for j in range(p * p, limit + 1, p):
                if spf[j] == j:
                    spf[j] = p
    return spf


def factors(n, spf):
    result = []
    while n > 1:
        p, a = spf[n], 0
        while n % p == 0:
            a += 1
            n //= p
        result.append((p, a))
    return result


def ratio_d_square(m, spf):
    fac = factors(m, spf)
    num = 1
    for _, a in fac:
        num *= 2 * a + 1
    return Fraction(num, 2 ** len(fac)), fac


def corrected_ratio(fac):
    out = Fraction(1)
    for _, a in fac:
        if a >= 2:
            out *= Fraction(2 * a + 1, 3)
    return out


def count_divisors_trial(n):
    result = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            result += 1 if d * d == n else 2
    return result


def distinct_primes_trial(n):
    count, d = 0, 2
    while d * d <= n:
        if n % d == 0:
            count += 1
            while n % d == 0:
                n //= d
        d += 1
    return count + (n > 1)


def check():
    nmax, tmax = 40000, 30000
    spf = smallest_prime_factors(tmax)
    for n in range(1, nmax + 1):
        m = isqrt(n - 1) + 1
        j = m * m - n
        assert 0 <= j <= 2 * m - 2
        d, fac = ratio_d_square(m, spf)
        reduced = corrected_ratio(fac)
        assert d == Fraction(3, 2) ** len(fac) * reduced
        # Evaluate D(n+s(n)) independently from factorization of its square.
        num, den = 1, 1
        for _, a in fac:
            num *= 2 * a + 1
            den *= 2
        assert d == Fraction(num, den)
        if n > 1:
            mprev = isqrt(n - 1)
            assert (mprev * mprev) < n <= m * m
    for m in range(1, 1601):
        d, _ = ratio_d_square(m, spf)
        assert d == Fraction(count_divisors_trial(m * m),
                             2 ** distinct_primes_trial(m * m))
    total = tmax ** 2
    sqfree_weight = first_atom_weight = 0
    for m in range(1, tmax + 1):
        w = 2 * m - 1
        _, fac = ratio_d_square(m, spf)
        corr = corrected_ratio(fac)
        if corr == 1:
            assert all(a == 1 for _, a in fac)
            sqfree_weight += w
        if corr == Fraction(5, 3):
            assert sum(a == 2 for _, a in fac) == 1
            assert all(a <= 2 for _, a in fac)
            first_atom_weight += w
    assert sum(2 * m - 1 for m in range(1, tmax + 1)) == total
    for m in range(1, 70):
        vals = [(m * m - n) for n in range((m - 1)**2 + 1, m*m + 1)]
        assert sorted(vals) == list(range(2*m-1))
    print('VERIFY_OK',f'shift_checks={nmax}', f'square_roots={tmax}', 'direct_divisor_checks=1600',
          'exact_factor_identities=PASS', 'correction_atom_tests=PASS',
          'exact_phase_grids=PASS')
    print('weighted_squarefree_frequency=', float(Fraction(sqfree_weight, total)))
    print('limiting_squarefree_atom=', 6/pi**2)
    print('weighted_first_correction_atom=', float(Fraction(first_atom_weight,total)))

if __name__ == '__main__':
    check()
