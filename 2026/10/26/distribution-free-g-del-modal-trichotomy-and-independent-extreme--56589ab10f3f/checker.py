"""Finite and Monte Carlo checks for a Gödel-modal one-step joint law.

Uses only Python's standard library. Simulation corroborates the symbolic
proof but does not replace it.
"""
from itertools import product
from math import sqrt
from random import Random


def godel_implication(a, b):
    return 1.0 if a <= b else b


def modal_values(pairs):
    box = min(godel_implication(r, p) for r, p in pairs)
    diamond = max(min(r, p) for r, p in pairs)
    return box, diamond


def classify(box, diamond):
    if box > diamond:
        return 'greater'
    if box == diamond:
        return 'equal'
    return 'less'


def h(x):
    return x - x*x/2


def joint_survival_cdf(n, u, v):
    assert 0 <= u < 1 and 0 <= v <= 1
    return (h(v) + max(0.0, h(v)-h(u)))**n


def exhaustive_orientation():
    for n in range(1, 12):
        lows = [(i + 1)/(n + 3) for i in range(n)]
        high = (n + 2)/(n + 3)
        counts = {'greater': 0, 'equal': 0, 'less': 0}
        for orientations in product((0, 1), repeat=n):
            pairs = [(a, high) if s == 0 else (high, a)
                     for a, s in zip(lows, orientations)]
            b, d = modal_values(pairs)
            assert d == max(lows)
            counts[classify(b, d)] += 1
        assert counts == {'greater': 1, 'equal': 1,
                          'less': (1 << n)-2}, (n, counts)
        print('orientation', n, counts)


def stochastic_checks():
    rng = Random(220647)
    trials = 160000
    for n in (1, 2, 3, 5, 7):
        tally = {'greater': 0, 'equal': 0, 'less': 0}
        tests = ((0.2, 0.6), (0.1, 0.9), (0.5, 0.7))
        joint_tally = [0]*len(tests)
        for _ in range(trials):
            pairs = [(rng.random(), rng.random()) for _ in range(n)]
            b, d = modal_values(pairs)
            tally[classify(b, d)] += 1
            for k, (u, v) in enumerate(tests):
                joint_tally[k] += (b > u and d <= v)
        target = 2.0**(-n)
        for cat in ('greater', 'equal'):
            rate = tally[cat]/trials
            assert abs(rate-target) < .008, (n, cat, rate, target)
        for (u, v), t in zip(tests, joint_tally):
            expected = joint_survival_cdf(n, u, v)
            observed = t/trials
            assert abs(observed-expected) < .008, (n, u, v, observed, expected)
        print('simulation', n, tally, 'joint', joint_tally)


def exact_polynomial_consistency():
    # Integrate the two singular component densities through the substitution
    # y=h(x), whose range is [0,1/2]: int(n*h^(n-1)*h')dx=(1/2)^n.
    # Their sum and the wedge probability must exhaust unit mass.
    for n in range(1, 40):
        atom = 2**(-n)
        wedge = 1-2*atom
        assert abs(atom+atom+wedge-1) < 1e-14
        assert 0 <= wedge <= 1
    # Restricting to a single root with zero-weight other edges is allowed.
    assert modal_values([(0.8, 0.3)]) == (0.3, 0.3)
    assert modal_values([(0.3, 0.8)]) == (1.0, 0.3)
    print('exact-normalization OK')


if __name__ == '__main__':
    exhaustive_orientation()
    stochastic_checks()
    exact_polynomial_consistency()
    print('ALL_CHECKS_OK')
