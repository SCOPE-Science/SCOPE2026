"""Exact scientific checks for the alternating-renewal pair-law aliasing result."""

import json
import sympy as sp

s, a, b = sp.symbols("s a b", positive=True)


def renewal_transform(phi):
    return sp.simplify(phi / (1 - phi))


# Markov comparator.
phi_m1 = a / (s + a)
phi_m0 = b / (s + b)

# Non-Markov alternative.
phi_alt1 = 4 * a**2 / (s + 2 * a) ** 2
phi_alt0 = ((a + b) * s + 4 * a * b) / (s**2 + (5 * a + b) * s + 4 * a * b)

r_m_sum = sp.factor(renewal_transform(phi_m1) + renewal_transform(phi_m0))
r_alt1 = sp.apart(renewal_transform(phi_alt1), s)
r_alt0 = sp.apart(renewal_transform(phi_alt0), s)
r_alt_sum = sp.factor(r_alt1 + r_alt0)

assert sp.simplify(r_m_sum - (a + b) / s) == 0
assert sp.simplify(r_alt1 - (a / s - a / (s + 4 * a))) == 0
assert sp.simplify(r_alt0 - (b / s + a / (s + 4 * a))) == 0
assert sp.simplify(r_alt_sum - (a + b) / s) == 0

M = 1 / a + 1 / b
p = b / (a + b)
H = sp.simplify((1 - phi_alt1) * (1 - phi_alt0) / (1 - phi_alt1 * phi_alt0))
C_laplace = sp.factor(p * (1 - p) / s - H / (M * s**2))
target = sp.factor(a * b / ((a + b) ** 2 * (s + a + b)))
assert sp.simplify(H - s / (s + a + b)) == 0
assert sp.simplify(C_laplace - target) == 0

# Hyperexponential validity: a+b lies strictly between the two positive roots.
x = sp.symbols("x", positive=True)
poly = x**2 - (5 * a + b) * x + 4 * a * b
assert sp.factor(poly.subs(x, a + b)) == -4 * a**2

numeric = []
for av, bv in [(1, 1), (2, 1), (1, 3), (sp.Rational(1, 5), 5), (7, sp.Rational(2, 3))]:
    disc = sp.sqrt((5 * av + bv) ** 2 - 16 * av * bv)
    alpha = sp.N(((5 * av + bv) - disc) / 2, 30)
    beta = sp.N(((5 * av + bv) + disc) / 2, 30)
    weight = sp.N((beta - (av + bv)) / (beta - alpha), 30)
    mean0 = sp.N(weight / alpha + (1 - weight) / beta, 30)
    assert 0 < alpha < av + bv < beta
    assert 0 < weight < 1
    assert abs(float(mean0 - sp.N(1 / bv, 30))) < 1e-12
    numeric.append({
        "a": str(av),
        "b": str(bv),
        "alpha": str(alpha),
        "beta": str(beta),
        "weight_on_alpha": str(weight),
        "mean_state0": str(mean0),
    })

print(json.dumps({
    "symbolic_checks": {
        "markov_renewal_sum": str(r_m_sum),
        "alternative_state1_renewal_transform": str(r_alt1),
        "alternative_state0_renewal_transform": str(r_alt0),
        "alternative_renewal_sum": str(r_alt_sum),
        "correlation_factor_H": str(sp.factor(H)),
        "covariance_laplace": str(C_laplace),
        "root_bracketing_polynomial_at_a_plus_b": str(sp.factor(poly.subs(x, a + b))),
    },
    "numeric_hyperexponential_checks": numeric,
    "status": "all checks passed",
}, indent=2))
