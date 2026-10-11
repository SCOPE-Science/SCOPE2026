"""Reproduce exact finite identities and illustrative numerical checks.

The all-parameter theorem relies on the analytic proof, not these finite cases.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext

getcontext().prec = 65


def squared_norm(x, alpha):
    return max(x[0] * x[0] / (alpha * alpha), x[0] * x[0] + x[1] * x[1])


def transform(x, y, tau):
    first = (x[0] + tau * y[0], x[1] + tau * y[1])
    second = (tau * x[0] - y[0], tau * x[1] - y[1])
    return first, second


def exact_rational_case():
    alpha, beta, tau = Q(4, 5), Q(3, 5), Q(12, 25)
    a, b = Q(3, 5), Q(4, 5)
    x, y = (a, b), (alpha, Q(0))
    assert squared_norm(x, alpha) == squared_norm(y, alpha) == 1
    u, v = transform(x, y, tau)
    assert u == (Q(123, 125), Q(4, 5))
    assert v == (Q(-64, 125), Q(48, 125))
    # On the second output the two defining norm branches tie.
    assert v[0] * v[0] / alpha**2 == v[0] * v[0] + v[1] * v[1]
    assert squared_norm(u, alpha) == u[0] * u[0] + u[1] * u[1]
    value = (squared_norm(u, alpha) + squared_norm(v, alpha)) / 2
    bound = (1 + tau * tau) * (1 + alpha * alpha) / 2
    assert value == bound == Q(31529, 31250)
    # Below the true threshold, the necessary cone inequality is impossible.
    tau_below = Q(2, 5)
    m = 1 / alpha
    assert tau_below * m < beta
    assert tau == beta / m


def other_branch():
    alpha = Decimal(3) / 5
    beta = Decimal(4) / 5
    a = alpha * alpha
    b = (1 - a * a).sqrt()
    tau = (1 + alpha * alpha).sqrt() - alpha
    kappa = beta / alpha
    m = b + kappa * a
    assert abs(tau * m - beta) < Decimal('1e-60')
    x, y = (a, b), (alpha, Decimal(0))
    u, v = transform(x, y, tau)
    bound = (1 + tau * tau) * (1 + alpha * alpha) / 2
    value = (squared_norm(u, alpha) + squared_norm(v, alpha)) / 2
    assert abs(value - bound) < Decimal('1e-55')
    assert abs(b - kappa * (a + tau * alpha)) < Decimal('1e-55')
    # The condition beta>=alpha**2 selects this branch, not the interior one.
    assert beta > alpha**2
    assert tau < beta


if __name__ == '__main__':
    exact_rational_case()
    other_branch()
    print('SKEW_SCHAEFFER_THRESHOLD_EXACT_CHECK_OK')
