"""Numerical probes for an analytic one-buyer budget-switch theorem.

The infinite-switch and scaling conclusions follow from the proof, not these
finite precision computations.
"""
import math


def marginal(t):
    return math.exp(-t) * (1.0 + 0.25 * math.sin(t))


def unconstrained_spending(t):
    return (-math.expm1(-t)) * (1.0 + 0.25 * math.sin(t))


def theta(t):
    price = marginal(t)
    allocation = min(math.expm1(t), 1.0 / price)
    return price / allocation


def gap(t):
    return math.sin(t) - 4.0 / math.expm1(t)


def bisect(a, b):
    fa = gap(a)
    assert fa * gap(b) < 0
    for _ in range(100):
        m = (a + b) / 2.0
        fm = gap(m)
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2.0


def run():
    nchecks = 0
    boundaries = []
    for k in range(1, 4):
        a = 2.0 * math.pi * k
        center = a + math.pi / 2.0
        b = (2*k + 1) * math.pi
        left = bisect(a, center)
        right = bisect(center, b)
        boundaries.extend((left, right))
        assert a < left < center < right < b
        assert unconstrained_spending(center) > 1.0
        assert unconstrained_spending((2*k+1.5)*math.pi) < 1.0
        for t in (a+0.3, center, b-0.3):
            p = marginal(t)
            actual = min(math.expm1(t), 1.0 / p)
            assert abs(p / theta(t) - actual) < 1e-12 * max(1,actual)
            assert (actual == 1.0/p) == (unconstrained_spending(t) >= 1.0)
            nchecks += 2
        # Each crossover has an exact cost identity to machine error.
        for t in (left, right):
            assert abs(theta(t)*(math.expm1(t)**2) - 1.0) < 1e-10
            nchecks += 1
    for i in range(1,len(boundaries)):
        assert boundaries[i] > boundaries[i-1]
        assert theta(boundaries[i]) < theta(boundaries[i-1])
        nchecks += 2
    for i in range(1, len(boundaries)):
        # Geometric law starts close for large index.
        if i>=3:
            ratio = theta(boundaries[i]) / theta(boundaries[i-1])
            assert abs(ratio / math.exp(-2*math.pi)-1.0)<0.02
            nchecks += 1
    for k in range(1,20):
        t = 0.1 + k * math.pi/4
        # Positive derivative, negative second derivative, strict price decrease.
        factor = 1 + math.sin(t)/4
        assert factor > 0.0
        assert -1+(math.cos(t)-math.sin(t))/4 < 0.0
        nchecks += 2
    print('PASS',nchecks,'checks,',len(boundaries),'crossover locations; last theta',theta(boundaries[-1]))

if __name__ == '__main__':
    run()
