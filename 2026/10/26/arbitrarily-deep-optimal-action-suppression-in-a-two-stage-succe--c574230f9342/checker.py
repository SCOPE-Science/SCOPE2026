#!/usr/bin/env python3
"""Exact rational independent recurrence/closed-form comparison for a two-state Markov decision process."""
from fractions import Fraction as F
from itertools import product


def direct_step(p, q, eps, gamma, reward):
    vb = p + (1 - p) * eps
    va = q * gamma * vb + (1 - q) * reward
    return p / vb, q * gamma * vb / va


def closed(k, p0, q0, eps, gamma, reward):
    den = p0 + (1 - p0) * eps**k
    p = p0 / den
    odds = q0 / (1 - q0) * (gamma / reward)**k * den
    return p, odds / (1 + odds)


def value(p, q, eps, gamma, reward):
    vb = p + (1 - p) * eps
    return vb, q * gamma * vb + (1 - q) * reward


checks = 0
for eps, gamma, reward, p0, q0 in product(
    [F(1,5), F(1,3), F(1,2), F(3,4)],
    [F(1,4), F(1,2), F(3,4)],
    [F(1,16), F(1,8), F(1,4), F(3,8), F(1,2), F(3,4), F(7,8)],
    [F(1,100), F(1,20), F(1,4), F(1,2), F(3,4)],
    [F(1,5), F(1,2), F(4,5)],
):
    p, q = p0, q0
    for k in range(0, 21):
        assert (p, q) == closed(k, p0, q0, eps, gamma, reward)
        checks += 1
        pp, qq = direct_step(p, q, eps, gamma, reward)
        assert value(pp, qq, eps, gamma, reward)[0] >= value(p, q, eps, gamma, reward)[0]
        assert value(pp, qq, eps, gamma, reward)[1] >= value(p, q, eps, gamma, reward)[1]
        if reward < gamma and p0 > 0:
            assert closed(k + 1, p0, q0, eps, gamma, reward)[1] > 0
        p, q = pp, qq

family_checks = 0
for n in range(1, 25):
    eps, gamma, reward, q0 = F(1,4), F(3,4), F(3,8), F(1,2)
    p0 = F(1, 1 + 2 * 4**n)
    p, q = p0, q0
    seq = [q]
    for k in range(2*n+6):
        p, q = direct_step(p, q, eps, gamma, reward)
        seq.append(q)
        assert (p, q) == closed(k+1, p0, q0, eps, gamma, reward)
        family_checks += 1
    assert all(seq[j+1] < seq[j] for j in range(n))
    assert seq[n+1] == seq[n]
    assert all(seq[j+1] > seq[j] for j in range(n+1, len(seq)-1))
    exact_trough = F(3*2**n, 1+2*4**n+3*2**n)
    assert seq[n] == exact_trough
    assert seq[n] < F(3,2**(n+1))

print('PASS: exact rational direct/closed comparisons:', checks)
print('PASS: exact rational explicit-family trajectory checks:', family_checks)
for n in [2,5,10,20]:
    p0=F(1,1+2*4**n)
    q_min=F(3*2**n,1+2*4**n+3*2**n)
    print('N=%d  p0=%s  trough q_N=q_(N+1)=%s  decimal=%.12g' % (n,p0,q_min,float(q_min)))
print('All comparisons use Fraction arithmetic; no floating-point steps in assertions.')
