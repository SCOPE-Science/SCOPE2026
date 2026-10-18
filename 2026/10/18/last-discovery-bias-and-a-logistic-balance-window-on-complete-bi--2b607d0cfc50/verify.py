"""Independent finite-state checks for the last-discovery side of a walk on K_{a,b}."""
from fractions import Fraction
from functools import lru_cache
from math import comb


def coupon_formula(a, b):
    """Exact probability that the last visited vertex is in the b-part."""
    out = Fraction(0)
    for j in range(1, b + 1):
        z = Fraction(b - j, b)
        pgf = Fraction(1)
        for k in range(1, a):
            pgf *= (Fraction(k, a) * z) / (1 - Fraction(a - k, a) * z)
        out += (-1) ** (j + 1) * comb(b, j) * pgf
    return out


def first_step_recursion(a, b):
    """Solve coupled first-step equations over the two visited-count coordinates."""
    @lru_cache(None)
    def pair(u, v):
        if (u, v) == (a, b):
            return Fraction(0), Fraction(1)
        p_new_b, p_old_b = Fraction(b - v, b), Fraction(v, b)
        p_new_a, p_old_a = Fraction(a - u, a), Fraction(u, a)
        tail_b = pair(u, v + 1)[1] if v < b else Fraction(0)
        tail_a = pair(u + 1, v)[0] if u < a else Fraction(0)
        p_a = (p_new_b * tail_b + p_old_b * p_new_a * tail_a) / (1 - p_old_b * p_old_a)
        p_b = p_new_a * tail_a + p_old_a * p_a
        return p_a, p_b
    return pair(1, 0)[0]


def run():
    count = 0
    for a in range(1, 11):
        for b in range(1, 11):
            actual = coupon_formula(a, b)
            expected = first_step_recursion(a, b)
            assert actual == expected, (a, b, actual, expected)
            assert (actual > Fraction(1, 2)) == (b >= a), (a, b, actual)
            assert (actual < Fraction(1, 2)) == (b < a), (a, b, actual)
            count += 3
    for a in range(2, 12):
        assert coupon_formula(a, a) > Fraction(1, 2)
        count += 1
    assert coupon_formula(2, 2) == Fraction(2, 3)
    assert coupon_formula(3, 3) == Fraction(81, 140)
    assert coupon_formula(3, 2) == Fraction(1, 5)
    assert coupon_formula(4, 4) == Fraction(50, 91)
    count += 4
    print(f"PASS: {count} independent exact-rational assertions")

if __name__ == '__main__':
    run()
