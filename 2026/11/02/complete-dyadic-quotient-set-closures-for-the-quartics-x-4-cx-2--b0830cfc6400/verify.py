"""Finite modular consistency checks for a quartic polynomial quotient theorem.

The infinite theorem follows from the proof by dyadic ball isometries;
no finite verification by itself certifies an infinite quantifier.
"""
from collections import defaultdict

COEFFICIENTS = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15]


def finite_square_and_image_checks():
    checks = 0
    for n in range(4, 11):
        modulus = 1 << n
        square_residues = {x*x % modulus for x in range(1, modulus, 2)}
        expected_square = set(range(1, modulus, 8))
        assert square_residues == expected_square, ('squares', n)
        checks += 1
        for c in COEFFICIENTS:
            for k in range(6):
                actual = {t*(c+(1 << (2*k))*t) % modulus for t in expected_square}
                expected = {(c+(1 << (2*k))+8*j) % modulus
                            for j in range(modulus//8)}
                assert actual == expected, ('ball', n, c, k)
                checks += 1
    return checks


def finite_quotient_checks():
    checks = 0
    for c in COEFFICIENTS:
        by_valuation = defaultdict(set)
        for x in range(1, 1025):
            f = x*x*(x*x+c)
            if f == 0:
                continue
            valuation = (abs(f) & -abs(f)).bit_length()-1
            by_valuation[valuation].add((f >> valuation) % 16)
        for j in range(-5, 6):
            actual = set()
            for v, numerators in by_valuation.items():
                denominators = by_valuation.get(v-j, set())
                for num in numerators:
                    for den in denominators:
                        actual.add(num * pow(den, -1, 16) % 16)
            expected = set()
            for unit in range(1, 16, 2):
                r = c % 8
                permitted = (r == 7 or
                    (r == 3 and j % 2 == 0) or
                    (r == 1 and unit % 4 == 1) or
                    (r == 5 and unit % 4 == (3 if j % 2 else 1)))
                if permitted:
                    expected.add(unit)
            assert actual == expected, ('ratios', c, j, actual, expected)
            checks += 1
    return checks


if __name__ == '__main__':
    image_checks = finite_square_and_image_checks()
    ratio_checks = finite_quotient_checks()
    print(f'VERIFY_OK: {image_checks} finite dyadic square/image checks; '
          f'{ratio_checks} finite normalized-quotient checks')
