"""Finite exact checks for a prime-index Apéry-polynomial Eisenstein theorem.

All arithmetic uses Python integers.  This is supporting evidence, not a proof
of the quantified theorem over all odd primes and all allowed exponents.
"""
from math import comb


def primes_up_to(n):
    return [p for p in range(3, n + 1, 2)
            if all(p % d for d in range(3, int(p**0.5) + 1, 2))]


def coefficients(p, r, s):
    q = 2**s
    b = [comb(p, k)**r * comb(p + k, k)**s for k in range(p + 1)]
    translated = [0] * (p + 1)
    for k, bk in enumerate(b):
        scale = bk * q**(p - k)
        for j in range(k + 1):
            translated[j] += scale * comb(k, j) * (-1)**(k - j)
    return b, translated


def run():
    cases = 0
    coeff_tests = 0
    point_tests = 0
    for p in primes_up_to(43):
        if pow(2, p - 1, p*p) == 1:
            continue
        for r in (2, 3, 4):
            for s in (1, 2, 3, 4, 5):
                if s % p == 0:
                    continue
                q = 2**s
                original, transformed = coefficients(p, r, s)
                assert original[0] == 1
                assert transformed[p] == comb(2*p, p)**s
                assert transformed[p] % p == q % p
                for j, value in enumerate(transformed):
                    assert value % p == (q if j == p else 0) % p
                    coeff_tests += 1
                assert transformed[0] % (p*p) == (q**p - q) % (p*p)
                assert transformed[0] % (p*p) != 0
                for y in (-2, -1, 0, 1, 2):
                    left = sum(transformed[j]*y**j for j in range(p + 1))
                    right = sum(original[k] * q**(p-k) * (y-1)**k
                                for k in range(p + 1))
                    assert left == right
                    point_tests += 1
                cases += 1
    # Known arithmetic boundary: 1093 is a base-two Wieferich prime.
    assert pow(2, 1092, 1093**2) == 1
    print(f'CHECK_OK cases={cases} coefficients={coeff_tests} evaluation_identities={point_tests} '
          'Wieferich_boundary_1093=confirmed')

if __name__ == '__main__':
    run()
