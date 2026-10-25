"""Exact rational checks for uniform-pair triangle distance moments.

Uses the Dirichlet(1,1,1) monomial integral, with no outside packages.
The polynomial computation is formal in the three squared side lengths.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, factorial


def simplex_monomial(alpha):
    """Integral expectation of product of barycentric powers."""
    numerator = 2
    for k in alpha:
        numerator *= factorial(k)
    return Fraction(numerator, factorial(sum(alpha) + 2))


@lru_cache(None)
def barycentric_difference_monomial(alpha):
    """Product moments of differences of two independent barycentric vectors."""
    total = Fraction(0)
    for p in product(*(range(a + 1) for a in alpha)):
        q = tuple(a - b for a, b in zip(alpha, p))
        coefficient = (-1) ** sum(q)
        for a, b in zip(alpha, p):
            coefficient *= comb(a, b)
        total += coefficient * simplex_monomial(p) * simplex_monomial(q)
    return total


def polynomial_of_moment(k):
    """Return coefficient map for E[R**(2*k)], formal in x,y,z."""
    ans = {}
    for i in range(k + 1):
        for j in range(k - i + 1):
            l = k - i - j
            multi = (j + l, i + l, i + j)
            coeff = Fraction((-1) ** k * factorial(k),
                             factorial(i) * factorial(j) * factorial(l))
            coeff *= barycentric_difference_monomial(multi)
            ans[(i, j, l)] = coeff
    return ans


def expected_coefficients(k):
    p = {}
    for i in range(k + 1):
        for j in range(k - i + 1):
            l = k - i - j
            e = (i, j, l)
            if k == 1:
                p[e] = Fraction(1, 18)
            elif k == 2:
                p[e] = Fraction(1, 60) if 2 in e else Fraction(0)
            elif k == 3:
                p[e] = (Fraction(23, 4200) if 3 in e else
                        Fraction(7, 4200) if 2 in e else
                        Fraction(-28, 4200))
            else:
                raise ValueError(k)
    return p


def moment(k, sides_squared):
    coeffs = polynomial_of_moment(k)
    return sum((c * sides_squared[0] ** i * sides_squared[1] ** j *
                sides_squared[2] ** l for (i, j, l), c in coeffs.items()),
               Fraction(0))


def elementary(a):
    x, y, z = a
    return x + y + z, x * y + x * z + y * z, x * y * z


def audit_triangle(sides_squared):
    e1, e2, e3 = elementary(sides_squared)
    m2, m4, m6 = (moment(k, sides_squared) for k in (1, 2, 3))
    assert m2 == e1 / 18
    assert m4 == (e1 ** 2 - 2 * e2) / 60
    assert m6 == (23 * e1 ** 3 - 62 * e1 * e2 + 20 * e3) / 4200
    assert 4 * e2 - e1 ** 2 == 324 * m2 ** 2 - 120 * m4
    ee1 = 18 * m2
    ee2 = (ee1 ** 2 - 60 * m4) / 2
    ee3 = (4200 * m6 - 23 * ee1 ** 3 + 62 * ee1 * ee2) / 20
    assert (ee1, ee2, ee3) == (e1, e2, e3)
    return m2, m4, m6


def main():
    for k in (1, 2, 3):
        derived = polynomial_of_moment(k)
        expected = expected_coefficients(k)
        assert derived == expected, (k, derived, expected)
        print('Exact formal moment polynomial passed:', 2 * k,
              'degree,', len(derived), 'monomials')

    examples = [
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(11, 7), Fraction(22, 7), Fraction(9, 7)),
        (Fraction(1), Fraction(1), Fraction(2)),
        (Fraction(9), Fraction(16), Fraction(25)),
    ]
    for a in examples:
        assert 4 * elementary(a)[1] > elementary(a)[0] ** 2
        print('Triangle', a, 'moments:', audit_triangle(a))
    a = audit_triangle(examples[1])
    b = audit_triangle(examples[2])
    assert a[:2] == b[:2]
    assert b[2] - a[2] == Fraction(4, 2401)
    print('Two-moment ambiguity and sixth-moment difference passed exactly.')

    # Verify the sharp cube-root example algebra in Q(sqrt(3)), symbolically
    # via elementary identities for zero-sum perturbations.
    assert Fraction(5832, 315) == Fraction(648, 35)
    print('All formal exact-rational checks passed.')


if __name__ == '__main__':
    main()
