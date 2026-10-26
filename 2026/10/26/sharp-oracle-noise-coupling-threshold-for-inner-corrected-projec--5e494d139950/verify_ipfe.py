"""Exact arithmetic checks for the noisy four-stage IPFE stability example.

Python 3 standard library only. This is a finite identity verifier, not an
alternative to the proof of the asymptotic results.
"""
from fractions import Fraction as F
from random import Random


def coefficients(t):
    xi = 1 - 2*t + 2*t*t
    L = 1 + xi/2
    G = t*(1-t)*L
    # Dimensionless coefficients of four stage-oracle errors.
    return xi, L, G, (t*t*L, (1-t)*L, -(1+t)*xi/(2*t), xi/(2*t))


def direct_step(y, e, t):
    # Scalar y'=-y, macrostep h=1, two FE microsteps followed by
    # the IPFE correction with two additional noisy RHS evaluations.
    xi = 1 - 2*t + 2*t*t
    k0 = -y + e[0]
    k1 = -(y + t*k0) + e[1]
    yp = y + t*k0 + (1-t)*k1
    k2 = -yp + e[2]
    k3 = -(yp + t*k2) + e[3]
    return yp + xi/(2*t)*(k3-k2)


def closed_step(y, e, t):
    _, _, G, c = coefficients(t)
    return G*y + sum(v*w for v,w in zip(c,e))


def stationary(t, rho):
    xi, L, G, c = coefficients(t)
    # Independent first two errors and correlated final pair; sigma^2=h^2=1.
    Q = c[0]**2+c[1]**2+c[2]**2+c[3]**2+2*rho*c[2]*c[3]
    Q2 = L*L*(t**4+(1-t)**2)+xi*xi/(4*t*t)*(t*t+2*(1+t)*(1-rho))
    assert Q == Q2
    return Q/(1-G*G)

rng = Random(165060)
trials = 0
for denom in (7, 11, 17, 31, 51):
    for numerator in range(1, denom//2 + 1):
        t = F(numerator, denom)
        if t >= F(1,2):
            continue
        xi,L,G,c=coefficients(t)
        assert 0 < G < F(3,8)
        for _ in range(30):
            y = F(rng.randrange(-30,31), rng.randrange(1,20))
            e = [F(rng.randrange(-20,21),rng.randrange(1,15)) for i in range(4)]
            assert direct_step(y,e,t) == closed_step(y,e,t)
            trials += 1
        for rho in (F(-1),F(-1,3),F(0),F(1,2),F(1)):
            v = stationary(t,rho)
            assert v>0

for m in (3,4,5):
    t=F(1,10**m)
    independent=stationary(t,F(0))
    assert abs(t*t*independent-F(1,2)) < F(3,10**m)
    paired=stationary(t,F(1)-2*t*t)
    assert abs(paired-F(7,2)) < F(30,10**m)

print('VERIFY_OK exact four-stage recurrence:',trials,
      'fractional stage inputs; covariance polynomial and coupling limits')
