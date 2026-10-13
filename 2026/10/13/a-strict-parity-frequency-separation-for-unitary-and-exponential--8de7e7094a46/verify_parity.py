"""Exact rational certificate for parity-separated divisor-sum frequencies.

Python 3, standard library only.  The finite cylinder computations certify
explicit rational densities; infinite-tail estimates are proved symbolically
in RESULT.md.
"""
from fractions import Fraction
from itertools import product

PRIMES = (3, 5, 7, 11, 13, 17, 19)
ODD_MAX = (9, 5, 4, 3, 3, 2, 2)
EVEN_MAX = (7, 4, 3, 2, 2, 1, 1)


def local_ratio(p, a):
    if a == 0:
        return 1, 1
    return p**a + 1, sum(p**d for d in range(1, a + 1) if a % d == 0)


def valuation_cache(maxima):
    denom = 1
    blocks = []
    for p, top in zip(PRIMES, maxima):
        denom *= p ** (top + 1)
        block = []
        for a in range(top + 1):
            numerator, denominator = local_ratio(p, a)
            block.append((a, numerator, denominator, (p - 1) * p ** (top - a)))
        blocks.append(block)
    return blocks, denom


def cylinder_masses():
    blocks, denominator = valuation_cache(ODD_MAX)
    count, mass = 0, 0
    for vector in product(*blocks):
        num, den, weight = 1, 1, 1
        for a, nu, de, w in vector:
            num *= nu
            den *= de
            weight *= w
        if num > den or all(item[0] == 0 for item in vector):
            count += 1
            mass += weight
    odd_mass = Fraction(mass, denominator)

    blocks, denominator = valuation_cache(EVEN_MAX)
    count, mass = 0, 0
    for vector in product(*blocks):
        num, den, weight = 1, 1, 1
        for a, nu, de, w in vector:
            num *= nu
            den *= de
            weight *= w
        for a in range(2, 15):
            nu, de = local_ratio(2, a)
            if 12 * num * nu < 11 * den * de:
                count += 1
                mass += weight * 2 ** (14 - a)
    even_mass = Fraction(mass, denominator * 2**14)
    return count, even_mass, odd_mass


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b'\x00' * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def main():
    even_count, even_mass, odd_mass = cylinder_masses()
    # Independently recompute the odd-vector count at exactly this cutoff.
    odd_blocks, _ = valuation_cache(ODD_MAX)
    odd_count = 0
    for vector in product(*odd_blocks):
        num = den = 1
        for a, nu, de, w in vector:
            num *= nu
            den *= de
        odd_count += int(num > den or all(item[0] == 0 for item in vector))

    assert odd_count == 18058
    assert odd_mass == Fraction(31076642675170427132493824,
                                35968987080950832137604375)
    assert even_count == 32591
    assert even_mass == Fraction(38646621072482317819,
                                 148330460379458857500)
    factor = Fraction(1)
    for p in PRIMES:
        factor *= Fraction(p * p - 1, p * p)
    assert factor == Fraction(12230590464, 14933966047)
    odd_lower = odd_mass * Fraction(8 * 7 * 7, 22 * 22) / factor
    assert odd_lower == Fraction(1896767741404445015411,
                                 2219932798988224320000)
    assert odd_lower > Fraction(17, 20)
    assert even_mass > Fraction(13, 50)

    # Tail primes greater than 1000 are bounded by exp(1/9) < 9/8.
    s = 100
    moment_bound = Fraction(11, 12)**s * Fraction(9, 8)
    finite_prime_count = 0
    for p in primes_upto(1000):
        if p > 19:
            moment_bound *= 1 + (Fraction(p + 1, p)**s - 1) / p
            finite_prime_count += 1
    assert finite_prime_count == 160  # primes <=1000 minus the first 8
    assert moment_bound < Fraction(1, 70)
    even_upper = 1 - Fraction(13, 50) * Fraction(69, 70)
    assert even_upper == Fraction(2603, 3500) < Fraction(3, 4)
    print('EXACT_CERTIFICATE_OK')
    print(f'odd_selected={odd_count}, odd_conditional_lower>{odd_lower}')
    print(f'even_selected={even_count}, even_bad_cylinder_mass={even_mass}')
    print(f'finite_prime_moment_terms={finite_prime_count}, markov_bound<1/70')
    print(f'odd_good_lim_inf>17/20; even_good_lim_sup<3/4')


if __name__ == '__main__':
    main()
