"""Exact arithmetic checks for affine projection on cross-polytope face skeleta.

This finite checker tests identities and examples; the proof of the all-dimension
statement uses the covariance, convexity, and beta-law arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import comb


def formula(d, s):
    assert d >= 2 and 1 <= s <= d
    return F(1) + F(s + 1, 2) * (F(1) - F(2, d * (s + 1))) ** s


def beta_integral_by_polynomial(d, s):
    """Integrate (c*u-1)_+ against Beta(1,s-1), term by term."""
    c = F(d * (s + 1), 2)
    if s == 1:
        return c - 1
    t = 1 / c
    ans = F(0)
    for k in range(s - 1):
        b = F((-1)**k * comb(s - 2, k))
        ans += b * (c * (1 - t ** (k + 2)) / (k + 2)
                    - (1 - t ** (k + 1)) / (k + 1))
    return (s - 1) * ans


def vertex_row_norm_by_marginal(d, s):
    return 1 + F(s, d) * beta_integral_by_polynomial(d, s)


checks = 0
for d in range(2, 32):
    previous = None
    for s in range(1, d + 1):
        c = F(d * (s + 1), 2)
        # The signed coordinate is zero with probability 1-s/d;
        # otherwise its magnitude is Beta(1,s-1).
        assert F(s, d) * F(2, s * (s + 1)) == F(2, d * (s + 1))
        checks += 1
        exact = formula(d, s)
        assert vertex_row_norm_by_marginal(d, s) == exact
        checks += 1
        if previous is not None:
            assert exact > previous
            checks += 1
        previous = exact
        # The two-sided finite-dimension remainder bound.
        baseline = F(s + 3, 2) - F(s, d)
        assert baseline <= exact <= baseline + F(1, d)
        checks += 1
    # Covered full-facet endpoint: radial volume-weight limiting value.
    m = F(d - 1)
    old_endpoint = (F(1) + (m * (m + 3) / (2 * (m + 1)))
                    * (m * (m + 3) / ((m + 1) * (m + 2))) ** (d - 1))
    assert formula(d, d) == old_endpoint
    checks += 1

assert formula(3, 2) == F(103, 54)
checks += 1
assert formula(4, 2) == F(49, 24)
checks += 1
assert formula(4, 3) == F(599, 256)
checks += 1
assert formula(2, 2) == F(5, 3)
checks += 1
print(f"PASS: {checks} exact checks")
