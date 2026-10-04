from fractions import Fraction
from math import comb, factorial

EXPECTED = {
    2: Fraction(-1, 3),
    3: Fraction(-1, 2),
    4: Fraction(-5, 8),
    5: Fraction(-2, 3),
    6: Fraction(-239, 384),
    7: Fraction(-29, 60),
    8: Fraction(-5629, 23040),
    9: Fraction(25, 252),
    10: Fraction(1137217, 2064384),
    11: Fraction(40417, 36288),
    12: Fraction(3326800613, 1857945600),
    13: Fraction(3683129, 1425600),
}

def abs_moment(d):
    total = Fraction(0)
    for k in range(d // 2 + 1):
        x = Fraction(d, 2) - k
        total += (-1) ** k * comb(d, k) * x ** (d + 1)
    return Fraction(2, factorial(d + 1)) * total

def direct_distance_identity(n):
    b = [Fraction(2*j - (n + 1), 2) for j in range(1, n + 1)]
    D = sum(abs(b[j] - b[i]) for i in range(n) for j in range(i + 1, n))
    return D == 2 * sum(x*x for x in b)

for n in range(2, 14):
    d = n - 1
    A = abs_moment(d)
    deriv = n * (Fraction(d, 12) - A)
    assert deriv == EXPECTED[n], (n, deriv, EXPECTED[n])
    assert direct_distance_identity(n)
    if n <= 8:
        assert deriv < 0
    else:
        assert deriv > 0

# The remaining dimensions are analytic: for d >= 13,
# E|S_d| <= sqrt(d/12) < d/12 because d/12 > 1.
print('VERIFY_OK')
