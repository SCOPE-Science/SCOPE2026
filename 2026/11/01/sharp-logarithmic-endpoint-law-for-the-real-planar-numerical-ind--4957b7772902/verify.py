"""Deterministic numerical sanity checks for the explicit real planar numerical-index profile.
These finite tests do not establish the asymptotic theorem or originality.
Run: python verify.py
"""
from math import exp, log, sinh, cosh, tanh


def z_opt(eta):
    if not (0.0 < eta < 1.0):
        raise ValueError('0 < eta < 1 required')
    low, high = 0.0, max(2.0, log(4.0 / (1.0 - eta)))
    while tanh(eta * high) * tanh(high) < eta:
        high *= 2.0
    for _ in range(150):
        mid = (low + high) / 2.0
        if tanh(eta * mid) * tanh(mid) < eta:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def value(eta):
    z = z_opt(eta)
    return exp(-(1.0 - eta) * z) * (1.0 - exp(-2.0 * eta * z)) / (1.0 + exp(-2.0 * z))


def original(p, z):
    t = exp(-2.0 * z / p)
    return abs(t ** (p - 1.0) - t) / (1.0 + t ** p)


count = 0
eta_list = [.01, .03, .1, .2, .4, .6, .8, .93, .99, .999]
prev_z, prev_value = 0.0, 0.0
for eta in eta_list:
    z = z_opt(eta)
    v = value(eta)
    assert z > prev_z and v > prev_value
    assert abs(tanh(eta * z) * tanh(z) - eta) < 1e-12
    for p in (2.0 / (1.0 - eta), 2.0 / (1.0 + eta)):
        assert abs(original(p, z) - v) < 2e-12
        count += 1
    prev_z, prev_value = z, v
    count += 3

for i in range(1, 10):
    left, right = i / 11.0, (i+1) / 11.0
    middle = .5 * (left + right)
    assert value(middle) < .5 * (value(left) + value(right))
    count += 1

low, high = .5, 2.0
for _ in range(140):
    mid = (low + high) / 2.0
    if mid * tanh(mid) < 1.0:
        low = mid
    else:
        high = mid
z0 = (low + high) / 2.0
c0 = z0 / cosh(z0)
assert abs(c0 - 0.66274341934918158) < 2e-15
count += 1
for eta in (0.08, .04, .02):
    cubic = c0 * eta + c0 * (z0*z0 / 6.0) * eta**3
    assert abs(value(eta) - cubic) < 0.1 * eta**5
    count += 1

for eps in (0.05, 0.02, 0.01, 0.003, 0.001):
    eta = 1.0 - eps
    L = log(4.0 / eps)
    z_pred = .5*L + .25*eps*(L-1.0)
    n_pred = .5*eps*(L+1.0) - .125*eps**2*(L*L+1.0)
    assert abs(z_opt(eta) - z_pred) < .15 * eps**2 * L**2
    assert abs((1.0 - value(eta)) - n_pred) < .06 * eps**3 * L**3
    count += 2

print(f'PASS: {count} deterministic checks for direct formula, duality, shape, and asymptotic scales.')
print(f'z0 = {z0:.15g}, c0 = {c0:.15g}')
