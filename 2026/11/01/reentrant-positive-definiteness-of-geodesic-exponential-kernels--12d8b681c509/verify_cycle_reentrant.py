"""Exact rational certificate for reentrant strict kernel positivity on the six-cycle.

This script uses only Python's standard library. For every exponent in the
closed interval [647/300, 653/300], it certifies strict eigenvalue signs at
three specified bandwidths. Its proof ingredients are integer-power root
brackets and signed Taylor remainder bounds for the exponential function.
"""
from fractions import Fraction as Q


P_LO = Q(647, 300)
P_HI = Q(653, 300)
BANDWIDTHS = (Q(7, 25), Q(2, 5), Q(3, 5))
EIGEN_COEFFICIENTS = (
    (2, 2, 1),     # multiplicity one, constant mode
    (1, -1, -1),   # multiplicity two
    (-1, -1, 1),   # multiplicity two
    (-2, 2, -1),   # multiplicity one, alternating mode
)


def power_root_bracket(base, exponent, scale=10**6):
    """Prove two adjacent rational grid points bound base**exponent."""
    numerator, denominator = exponent.numerator, exponent.denominator
    target = base**numerator * scale**denominator
    lower, upper = 0, base**3 * scale
    while lower + 1 < upper:
        middle = (lower + upper) // 2
        if middle**denominator < target:
            lower = middle
        else:
            upper = middle
    assert lower**denominator < target < upper**denominator
    assert upper == lower + 1
    return Q(lower, scale), Q(upper, scale)


def exp_negative_interval(x_lower, x_upper, degree=70):
    """Certified exp(-x) interval from the alternating Taylor polynomials.

    Taylor's Lagrange remainder for exp(-x) is (-1)**(k+1)
    exp(-xi)*x**(k+1)/(k+1)! with 0 <= xi <= x.
    Thus the odd polynomial is a lower bound and the even polynomial an
    upper bound for all x >= 0. Monotonicity brackets uncertain x.
    """
    assert Q(0) <= x_lower <= x_upper and degree % 2 == 0

    def polynomial(x, n):
        value, term = Q(0), Q(1)
        for j in range(n + 1):
            value += term
            term *= -x / Q(j + 1)
        return value

    return polynomial(x_upper, degree + 1), polynomial(x_lower, degree)


def linear_interval(constant, coefficients, intervals):
    lower = upper = Q(constant)
    for coefficient, (a, b) in zip(coefficients, intervals):
        assert a <= b
        if coefficient >= 0:
            lower += coefficient * a
            upper += coefficient * b
        else:
            lower += coefficient * b
            upper += coefficient * a
    return lower, upper


def grid_floor(value, scale=10**9):
    return value.numerator * scale // value.denominator


def main():
    powers = {}
    for base in (2, 3):
        lo = power_root_bracket(base, P_LO)
        hi = power_root_bracket(base, P_HI)
        assert lo[0] < lo[1] < hi[0] < hi[1]
        powers[base] = (lo[0], hi[1])
        print('POWER_BRACKET_OK', base,
              'p_lo', str(P_LO), 'p_hi', str(P_HI),
              'lower', lo[0], 'upper', hi[1])

    expectations = ((+1, +1, +1, +1),
                    (+1, +1, +1, -1),
                    (+1, +1, +1, +1))
    for bandwidth, expected in zip(BANDWIDTHS, expectations):
        intervals = [exp_negative_interval(bandwidth, bandwidth)]
        for base in (2, 3):
            root_lower, root_upper = powers[base]
            intervals.append(exp_negative_interval(
                bandwidth * root_lower, bandwidth * root_upper))
        assert all(0 < lo <= hi < 1 for lo, hi in intervals)
        eigenvalue_intervals = [
            linear_interval(1, coeff, intervals)
            for coeff in EIGEN_COEFFICIENTS
        ]
        for k, ((lo, hi), sign) in enumerate(zip(eigenvalue_intervals,
                                                 expected)):
            assert lo <= hi
            if sign > 0:
                assert lo > 0, (bandwidth, k, lo)
            else:
                assert hi < 0, (bandwidth, k, hi)
            print('EIGEN_SIGN_OK', str(bandwidth), k,
                  'positive' if sign > 0 else 'negative',
                  'rational_grid', grid_floor(lo), grid_floor(hi)+1,
                  'over_1000000000')
    print('ALL_UNIFORM_REENTRANT_C6_CHECKS_OK')


if __name__ == '__main__':
    main()
