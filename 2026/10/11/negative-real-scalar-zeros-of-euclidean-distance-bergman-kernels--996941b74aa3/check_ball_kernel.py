"""Exact-rational spot checks for Euclidean-distance Bergman kernels.

Run: python3 check_ball_kernel.py
These are finite consistency checks, not substitutes for the proof of the
all-dimensional Jacobi zero theorem.
"""
from fractions import Fraction
from math import comb, factorial


def rising(x, k):
    v = Fraction(1)
    for j in range(k):
        v *= x + j
    return v


def numerator(d, t):
    """Coefficients of normalized polynomial Q_{d,t}(s), ascending."""
    assert isinstance(d, int) and d >= 1
    assert isinstance(t, int) and t >= 0
    m = (t + 1) // 2
    b = -Fraction(2 * (t // 2) + 1, 2)
    return [rising(Fraction(-m), j) * rising(b, j)
            / (rising(Fraction(2 * d + 1, 2), j) * factorial(j))
            for j in range(m + 1)]


def normalized_moment_coefficient(d, t, k):
    """Coefficient from independently integrated spherical and radial moments."""
    result = Fraction(comb(d + k - 1, k))
    for i in range(t + 1):
        result *= Fraction(2 * (d + k) + i, 2 * d + i)
    return result


def coefficient_from_numerator(d, t, k):
    a = numerator(d, t)
    h = d + t + 1
    return sum((a[j] * comb(h + k - j - 1, k - j)
                for j in range(min(len(a) - 1, k) + 1)), Fraction(0))


def exact_zero_count(d, t):
    """Number of scalar kernel roots in (-1,0), via Descartes equality."""
    a = numerator(d, t)
    b = [sum((a[i] * comb(i, j) * ((-1) ** (i - j))
              for i in range(j, len(a))), Fraction(0))
         for j in range(len(a))]
    signs = [1 if x > 0 else -1 for x in b if x]
    return sum(x != y for x, y in zip(signs, signs[1:]))


def verify():
    ncases = 0
    for d in range(1, 17):
        for t in range(19):
            a = numerator(d, t)
            assert a[0] == 1
            assert all(x > 0 for x in a)
            assert len(a) == (t + 1) // 2 + 1
            for k in range(19):
                assert normalized_moment_coefficient(d, t, k) == coefficient_from_numerator(d, t, k), (d, t, k)
                ncases += 1
            cnt = exact_zero_count(d, t)
            assert 0 <= cnt <= (t + 1) // 2
    assert exact_zero_count(1, 2) == 0
    assert exact_zero_count(1, 3) == 1
    assert exact_zero_count(2, 3) == 1
    assert exact_zero_count(3, 3) == 0
    assert exact_zero_count(3, 4) == 1
    assert numerator(2, 3) == [Fraction(1), Fraction(6, 5), Fraction(3, 35)]
    assert numerator(3, 3) == [Fraction(1), Fraction(6, 7), Fraction(1, 21)]
    assert numerator(3, 4) == [Fraction(1), Fraction(10, 7), Fraction(5, 21)]
    print(f'PASS: {ncases} exact independent moment/closed-form coefficient identities; '
          'sample zero counts and numerator normalizations verified.')


if __name__ == '__main__':
    verify()
