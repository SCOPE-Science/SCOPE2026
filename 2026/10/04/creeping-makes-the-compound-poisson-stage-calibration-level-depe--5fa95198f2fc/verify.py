from math import exp, isclose


def continuous_passage_probability(c, lam, theta, x):
    kappa = (c + lam * theta) / (c * theta)
    return c / (c + lam * theta) + (lam * theta) / (c + lam * theta) * exp(-kappa * x)


def mean_overshoot(c, lam, theta, x):
    return theta * (1.0 - continuous_passage_probability(c, lam, theta, x))


def mean_hitting_time(c, lam, theta, x):
    return (x + mean_overshoot(c, lam, theta, x)) / (c + lam * theta)


c = lam = theta = 1.0
a, b = 1.0, 2.0
kappa = (c + lam * theta) / (c * theta)

tau_gap = mean_hitting_time(c, lam, theta, b) - mean_hitting_time(c, lam, theta, a)
correction = lam * theta**2 / (c + lam * theta) * (exp(-kappa * a) - exp(-kappa * b))
lhs = (c + lam * theta) * tau_gap
rhs = (b - a) + correction
expected_gap = 0.5 + 0.25 * (exp(-2.0) - exp(-4.0))

assert correction > 0.0
assert isclose(lhs, rhs, rel_tol=0.0, abs_tol=1e-14)
assert isclose(tau_gap, expected_gap, rel_tol=0.0, abs_tol=1e-14)
assert tau_gap > (b - a) / (c + lam * theta)
print('VERIFY_OK')
