"""Deterministic checks of the reciprocal-power omission mechanism theorem.

Run: python3 verify.py
Only finite numerical checks are performed; the mathematical proof is in RESULT.md.
"""
import math
import random
from fractions import Fraction


def root_ratio(n, exponent):
    if n < 3 or exponent <= 1:
        raise ValueError('requires n >= 3 and exponent > 1')
    k = (n - 2) * ((exponent - 1) ** (exponent - 1)) / exponent ** exponent
    lo, hi = 1.0, float(n)
    for _ in range(85):
        r = (lo + hi) / 2
        if 2 * (r - 1) * r ** (exponent - 1) < k:
            lo = r
        else:
            hi = r
    return (lo + hi) / 2


def normalized_social_cost(nearest_distances, exponent):
    minimum = min(nearest_distances)
    a = [d / minimum for d in nearest_distances]
    return sum(v ** (1 - exponent) for v in a) / sum(v ** (-exponent) for v in a)


def nearest_distances(points):
    return [min(abs(points[i] - points[j]) for j in range(len(points)) if i != j)
            for i in range(len(points))]


def expected_true_cost_at_report(true_points, reports, focal, exponent):
    ds = nearest_distances(reports)
    weights = [d ** (-exponent) for d in ds]
    normalizer = sum(weights)
    return sum(weights[omitted] * min(abs(true_points[focal] - reports[j])
                    for j in range(len(reports)) if j != omitted)
                    for omitted in range(len(reports))) / normalizer


def check():
    rnd = random.Random(260822484)
    tests = 0
    equalities = 0
    for n in range(3, 21):
        for q in [1.05, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 7.0]:
            opt = root_ratio(n, q)
            step = q * opt / (q - 1)
            extreme = [0.0, 1.0] + [1 + i * step for i in range(1, n - 1)]
            vals = nearest_distances(extreme)
            observed = normalized_social_cost(vals, q)
            assert abs(observed - opt) < 1e-9 * max(1, opt), (n, q, observed, opt)
            equalities += 1
            for _ in range(125):
                xs = [0.0]
                for _ in range(n-1):
                    xs.append(xs[-1] + math.exp(rnd.uniform(-4, 4)))
                r = normalized_social_cost(nearest_distances(xs), q)
                assert r <= opt * (1 + 1e-11), (n,q,r,opt)
                tests += 1
    # Rational witness for p=4 and 3 collinear agents. A negative gain means no manipulation.
    base = [Fraction(0), Fraction(1), Fraction(2)]
    report = [Fraction(-1,100), Fraction(1), Fraction(2)]
    before = expected_true_cost_at_report(base, base, 0, 4)
    after = expected_true_cost_at_report(base, report, 0, 4)
    assert after < before, (before, after)
    assert before == Fraction(1,3)
    # The p=1 upper bound is approached; p<1 gives unbounded growth.
    for n in [3,5,11]:
        near = [1, 1] + [10**7] * (n-2)
        r1 = normalized_social_cost(near, 1.0)
        assert n/2 - r1 < 1e-4
        rhalf = normalized_social_cost(near, 0.5)
        assert rhalf > 10
    print(f'VERIFY_OK sharp_constructed={equalities} random_profiles={tests} ' +
          f'power4_manipulation_before={before} after={after} ' +
          'phase_q1_and_subcritical=checked')


if __name__ == '__main__':
    check()
