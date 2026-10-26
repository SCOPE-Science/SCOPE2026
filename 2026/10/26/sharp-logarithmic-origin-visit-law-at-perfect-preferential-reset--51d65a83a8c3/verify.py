"""Standalone arithmetic checks for the perfect-relocation impurity walk.
Python 3 standard library only. These finite checks supplement a proof of asymptotics.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import log


def steps(t, c, last, p):
    """At time t=n+1, c origin visits and last=1 if current site is origin."""
    assert 1 <= c <= t and last in (0, 1) and 0 < p < 1
    q = F(c, t) * (1 - p * last)
    assert 0 <= q <= 1
    return q


def test_conditional_identities():
    checked = 0
    for p in (F(1, 5), F(1, 3), F(2, 3), F(4, 5)):
        for t in range(1, 83):
            for c in range(1, t + 1):
                for last in (0, 1):
                    q = steps(t, c, last, p)
                    a = F(c, t)
                    next_a = (1 - q) * F(c, t + 1) + q * F(c + 1, t + 1)
                    assert next_a - a == -p * a * last / (t + 1)
                    Q = F(t, c)
                    next_Q = (1 - q) * F(t + 1, c) + q * F(t + 1, c + 1)
                    correction = (1 - p * last) * (t - c) / (t * c * (c + 1))
                    assert next_Q - Q == p * last / c + correction
                    variation = q * (1 - q) * F((t + 1)**2, c*c*(c+1)*(c+1))
                    assert variation <= F(4*t, c**3)
                    checked += 1
    return checked


def test_finite_laws():
    # Exact rational distribution for (number of zeroes, current-zero flag).
    # The dynamics depends on no other spatial information when off-origin relocation is certain.
    tested = 0
    for p in (F(1, 4), F(1, 2), F(3, 4)):
        distribution = {(1, 1): F(1)}
        for t in range(1, 24):
            assert sum(distribution.values()) == 1
            assert all(c >= 1 and c <= t for c, last in distribution)
            current_Q = sum(w * F(t, c) for (c, last), w in distribution.items())
            drift = sum(w * (p * last / c + (1-p*last)*(t-c)/F(t*c*(c+1)))
                        for (c, last), w in distribution.items())
            nxt = defaultdict(F)
            for (c, last), prob in distribution.items():
                q = steps(t, c, last, p)
                nxt[c + 1, 1] += prob * q
                nxt[c, 0] += prob * (1 - q)
                tested += 1
            distribution = nxt
            next_Q = sum(w * F(t+1, c) for (c, last), w in distribution.items())
            assert next_Q - current_Q == drift
    return tested


def sample_path(seed=1931, n=900_000, p=0.4):
    import random
    rng = random.Random(seed)
    c = 1
    last = 1
    estimates = []
    for t in range(1,n+1):
        q = c/t * (1-p*last)
        last = int(rng.random() < q)
        c += last
        if t in (1000, 10000, 100000, 900000):
            tt=t+1
            Q=tt/c
            estimates.append((tt,c,Q,Q-p*log(tt)+p*log(log(tt))))
    assert all(z[1] > 0 for z in estimates)
    return estimates


if __name__ == '__main__':
    c1=test_conditional_identities()
    c2=test_finite_laws()
    print('EXACT_IDENTITIES_OK',c1)
    print('EXACT_DISTRIBUTIONS_OK',c2)
    print('SAMPLE_PATH',sample_path())
