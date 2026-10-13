#!/usr/bin/env python3
"""Exact rational checks for a normalized five-compartment epidemic update."""
from fractions import Fraction as Q


def original(state, rates, h):
    s, e, i, r, d = state
    beta, sigma, gamma, mu, alpha = rates
    assert sum(state) == 1 and all(v >= 0 for v in state) and 1 - d > 0
    assert h > 0 and beta > 0 and sigma > 0 and gamma > 0 and mu > 0 and alpha >= 0
    q = beta * i / (1 - d)
    sn = (s + alpha * h * r) / (1 + h * q)
    en = (e + h * q * sn) / (1 + sigma * h)
    inn = (i + sigma * h * en) / (1 + (gamma + mu) * h)
    rn = (r + gamma * h * inn) / (1 + alpha * h)
    dn = 1 - sn - en - inn - rn
    return (sn, en, inn, rn, dn)


def balanced(state, rates, h):
    s, e, i, r, d = state
    beta, sigma, gamma, mu, alpha = rates
    assert sum(state) == 1 and all(v >= 0 for v in state) and 1 - d > 0
    assert h > 0 and beta > 0 and sigma > 0 and gamma > 0 and mu > 0 and alpha >= 0
    q = beta * i / (1 - d)
    w = alpha * h * r / (1 + alpha * h)
    rs = r - w
    ss = s + w
    sn = ss / (1 + h * q)
    en = (e + h * q * sn) / (1 + sigma * h)
    inn = (i + sigma * h * en) / (1 + (gamma + mu) * h)
    rn = rs + gamma * h * inn
    dn = d + mu * h * inn
    return (sn, en, inn, rn, dn)


state = (Q(1, 4), Q(1, 100), Q(1, 100), Q(73, 100), Q(0))
rates = (Q(1), Q(1), Q(1, 10), Q(1, 10), Q(1))
h = Q(1)
s, e, i, r, d = state
beta, sigma, gamma, mu, alpha = rates
out = original(state, rates, h)
assert out == (Q(98, 101), Q(199, 20200), Q(401, 24240),
               Q(177353, 484800), -Q(58583, 161600))
assert out[-1] < 0 and sum(out) == Q(1)
assert out[-1] - d == h * (mu * out[2] + alpha * (out[3] - r))
assert (1 + alpha * h) * out[-1] == ((1 + alpha * h) * d
            + h * (mu * (1 + alpha * h) + alpha * gamma * h) * out[2]
            - alpha * alpha * h * h * r)
assert (1 + alpha * h) * d + h * (mu * (1 + alpha * h)
            + alpha * gamma * h) * out[2] < alpha * alpha * h * h * r

fixed = balanced(state, rates, h)
assert fixed == (Q(123, 202), Q(13, 1616), Q(243, 16160),
                 Q(59227, 161600), Q(243, 161600))
assert all(z >= 0 for z in fixed) and sum(fixed) == Q(1)
assert fixed[-1] >= d

# Finite tests are checks, not a substitute for the general algebraic proof.
for hh in [Q(1, 200), Q(1, 10), Q(1), Q(37)]:
    for a in [Q(0), Q(1, 13), Q(3, 2)]:
        rr = (Q(7, 5), Q(13, 7), Q(3, 17), Q(5, 11), a)
        bb = balanced(state, rr, hh)
        assert all(z >= 0 for z in bb) and sum(bb) == Q(1)
        assert bb[-1] >= state[-1]
        if a == 0:
            assert original(state, rr, hh) == bb

# Arbitrarily small step sizes admit positive-seed counterexamples
# after the seeds are chosen small relative to that step.
for hh in [Q(1), Q(1, 10), Q(1, 100), Q(1, 1000)]:
    epsilon = hh**3 / Q(10000)
    init = (Q(1, 2) - 2 * epsilon, epsilon, epsilon, Q(1, 2), Q(0))
    oo = original(init, rates, hh)
    assert all(x > 0 for x in init[:4]) and oo[-1] < 0

print('VERIFY_OK')
