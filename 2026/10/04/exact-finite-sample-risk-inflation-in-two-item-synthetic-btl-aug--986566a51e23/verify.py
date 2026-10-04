from fractions import Fraction
from math import comb, pi, sin, sqrt


def binom_prob(m, s, p):
    return Fraction(comb(m, s), 1) * p**s * (1-p)**(m-s)


def propagate_unconditional(m, q, tmax):
    # State after round 0: total successes among m observations.
    dist = {s: binom_prob(m, s, q) for s in range(m+1)}
    check(dist, m, q, 1)
    for t in range(1, tmax):
        nxt = {}
        for total, mass in dist.items():
            p = Fraction(total, m*t)
            for s in range(m+1):
                z = total + s
                nxt[z] = nxt.get(z, Fraction(0)) + mass * binom_prob(m, s, p)
        dist = nxt
        check(dist, m*(t+1), q, t+1)


def finite_product(m, t, start=1):
    out = Fraction(1)
    for k in range(start, t+1):
        out *= Fraction(m*k*k - 1, m*k*k)
    return out


def check(dist, nobs, q, t):
    mean = sum(Fraction(total, nobs)*mass for total, mass in dist.items())
    second = sum(Fraction(total, nobs)**2*mass for total, mass in dist.items())
    var = second - mean*mean
    expected = q*(1-q)*(1-finite_product(nobs//t, t))
    assert mean == q
    assert var == expected


def propagate_conditional(m, s0, tmax):
    x = Fraction(s0, m)
    dist = {s0: Fraction(1)}
    for t in range(1, tmax):
        nxt = {}
        for total, mass in dist.items():
            p = Fraction(total, m*t)
            for s in range(m+1):
                z = total+s
                nxt[z] = nxt.get(z, Fraction(0)) + mass*binom_prob(m, s, p)
        dist = nxt
        nobs = m*(t+1)
        mean = sum(Fraction(total,nobs)*mass for total,mass in dist.items())
        second = sum(Fraction(total,nobs)**2*mass for total,mass in dist.items())
        var = second-mean*mean
        expected = x*(1-x)*(1-finite_product(m,t+1,start=2))
        assert mean == x
        assert var == expected


for m in (1,2,3,4):
    propagate_unconditional(m, Fraction(2,5), 5)
for m,s0 in ((2,1),(3,1),(3,2),(4,1),(4,2)):
    propagate_conditional(m,s0,5)

for m in (1,2,3,5,10,50,200):
    x = pi/sqrt(m)
    R = m*(1-sin(x)/x)
    assert R < pi*pi/6
    prod = 1.0
    for k in range(1,200000):
        prod *= 1 - 1/(m*k*k)
    target = sin(x)/x
    assert abs(prod-target) < 1e-5

print('VERIFY_OK')
