"""Reproduce exact polynomial identities and rational small-parameter spot checks.

Requires Python 3.10+ and SymPy. The all-n theorem is proved in RESULT.md;
finite evaluations in this script are independent sanity tests, not an infinite proof.
"""

from fractions import Fraction
from math import comb
from sympy import symbols, prod, factorial, factor, expand, simplify, sqrt


def binpoly(n, t):
    """Unnormalized positive coefficients for floor(2 Bin(n,p)/3)."""
    out = [0] * (2 * n // 3 + 1)
    for k in range(n + 1):
        out[2 * k // 3] += comb(n, k) * t ** k
    return out


def symbolic_checks():
    n, t, m = symbols('n t m', integer=True)
    choose = lambda j: prod(n - i for i in range(j)) / factorial(j)
    f = expand(choose(2) ** 2 * t - (1 + n * t) * (choose(3) + choose(4) * t))
    assert simplify(f.subs(n, 3) - (6 * t - 1)) == 0
    assert simplify(f.subs(n, 4) - (-4 * t ** 2 + 19 * t - 4)) == 0
    assert simplify(f.subs(n, 5) - (-5 * (5 * t ** 2 - 9 * t + 2))) == 0
    assert simplify(f.subs(n, 6) - (-10 * (3 * t - 1) * (3 * t - 2))) == 0
    a, b, c = (expand(f).coeff(t, power) for power in (2, 1, 0))
    q = 5 * n**4 - 42 * n**3 + 73 * n**2 - 36 * n - 12
    assert simplify(b**2 - 4 * a * c + n**2 * (n - 1)**2 * q / 192) == 0
    assert expand(q.subs(n, m + 7)) == (5 * m**4 + 98 * m**3 + 661 * m**2 + 1672 * m + 912)
    for nn in range(3, 7):
        arr = binpoly(nn, t)
        assert simplify(arr[1]**2-arr[0]*arr[2]-t**3*f.subs(n, nn)) == 0
    from sympy import Rational
    for trial, endpoints in ((4, ((9-sqrt(33))/18, (9+sqrt(33))/18)),
                             (5, ((13-sqrt(41))/32, (13+sqrt(41))/32))):
        for prob in endpoints:
            odds = prob / (1-prob)
            assert simplify(f.subs(n, trial).subs(t, odds)) == 0
    assert simplify(f.subs(n, 3).subs(t, Rational(1,6))) == 0
    arr = binpoly(5, t)
    assert factor(arr[2]**2-arr[1]*arr[3]) == 5*t**6*(5*t**2+18*t+20)
    arr = binpoly(6, t)
    assert factor(arr[3]**2-arr[2]*arr[4]) == t**9*(21*t-20)
    print('SYMBOLIC_IDENTITIES_PASS')


def grid_checks():
    """A rational grid of positive odds: smoke test, not the general proof."""
    successes = {n: 0 for n in range(1, 31)}
    for n in range(1, 31):
        for numerator in range(1, 41):
            t = Fraction(numerator, 20)
            a = binpoly(n, t)
            valid = all(a[k]**2 >= a[k - 1]*a[k + 1]
                        for k in range(1, len(a)-1))
            # Exact root barriers without floating point.
            f = comb(n, 2)**2*t - (1+n*t) * (comb(n,3)+comb(n,4)*t)
            predicted = n <= 2 or (n == 3 and f >= 0) or (
                n in (4,5) and f >= 0)
            assert valid == predicted, (n, t, valid, predicted)
            successes[n] += int(valid)
    assert all(successes[n] == 0 for n in range(6, 31))
    assert all(successes[n] > 0 for n in range(1, 6))
    print('EXACT_RATIONAL_GRID_PASS trial_counts=30 odds_grid=40 tests=1200')


if __name__ == '__main__':
    symbolic_checks()
    grid_checks()
