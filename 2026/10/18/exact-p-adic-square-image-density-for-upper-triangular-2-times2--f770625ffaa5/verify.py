"""Exact finite-ring checks for local square-image densities in 2-by-2 triangular matrices."""
from collections import defaultdict
from fractions import Fraction
from math import gcd


def count_square_images(modulus):
    """Count DISTINCT squares, not their preimages, in UT_2(Z/modulus Z)."""
    roots = defaultdict(list)
    for x in range(modulus):
        roots[x * x % modulus].append(x)
    count = 0
    for xs in roots.values():
        for zs in roots.values():
            d = min(gcd(modulus, x + z) for x in xs for z in zs)
            count += modulus // d
    return count


def predicted_density(p):
    if p == 2:
        return Fraction(7, 372)
    return Fraction(p**3 * (p - 1) * (p**2 + 1),
                    4 * (p + 1) * (p**5 - 1))


def independent_series(p, cutoff=25):
    unit_density = Fraction(1, 8) if p == 2 else Fraction(p - 1, 2 * p)
    total = Fraction(0)
    for r in range(cutoff):
        for s in range(cutoff):
            m = min(r, s) + (p == 2 and r == s)
            total += Fraction(1, p**(2 * r + 2 * s + m))
    return unit_density * unit_density * total


def main():
    for p, exponents in [(2, range(1, 9)), (3, range(1, 6)),
                         (5, range(1, 4)), (7, range(1, 3))]:
        limit = predicted_density(p)
        numerical = independent_series(p)
        assert abs(float(numerical - limit)) < 1e-12
        earlier = Fraction(1)
        for k in exponents:
            modulus = p**k
            count = count_square_images(modulus)
            share = Fraction(count, modulus**3)
            assert limit <= share <= earlier, (p, k, limit, share, earlier)
            earlier = share
        print('prime', p, 'finite last modulus', modulus,
              'finite fraction', share, 'limit', limit)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
