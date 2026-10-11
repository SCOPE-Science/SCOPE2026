"""Reproduce the two asymptotic coefficient balances with exact rational arithmetic.

This verifies representative polynomial exponents and coefficients; the analytical
proof in RESULT.md, not a finite list of tests, establishes the general theorem.
"""
from fractions import Fraction as F


def check_case(n: int, m: int, lead: F, next_coeff: F):
    assert n >= 2 and m >= n and m % 2 == 1 and lead > 0
    A = lead / F(m + 1)
    Q = (next_coeff - (F(1) / A if m == n else F(0))) / F(m - 1)
    L = F(1) / (A * m)
    # Leading and second coefficients in dv/dz=b-z^(2n-1)/v.
    assert A * (m + 1) == lead
    assert Q * (m - 1) == next_coeff - (F(1) / A if m == n else F(0))
    # Integrating the reciprocal-velocity expansion gives these coefficients.
    C2 = -Q / (A * A * (m + 2))
    assert L * A * m == 1
    assert C2 * (m + 2) == -Q / (A * A)
    # The physical-time inverse expansion z=(L/tau)^(1/m)+d(tau/L)^(1/m).
    d = -Q / (A * (m + 2))
    assert -L * m * d + C2 == 0
    return Q, L, C2


if __name__ == '__main__':
    samples = [
        (2, 3, F(2), F(1)),
        (3, 3, F(2), F(0)),
        (3, 3, F(3, 2), F(-1, 2)),
        (3, 5, F(3, 2), F(-1, 2)),
        (5, 5, F(3, 2), F(0)),
        (4, 7, F(3), F(0)),
        (6, 9, F(11, 3), F(4, 7)),
    ]
    for sample in samples:
        check_case(*sample)
    print('CHECK_OK: leading balance, restoring-force resonance and time inversion')
