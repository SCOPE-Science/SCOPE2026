"""Self-contained checks for the variance-optimal cyclic-polygon mixture.
Run: python3 verify.py [--simulation]
"""
import math
import random
import sys
from fractions import Fraction


def sigma(k, l):
    return math.factorial(k + l) - (1 + k * l) * math.factorial(k) * math.factorial(l)


def rising(n, k):
    v = 1
    for j in range(k):
        v *= n + j
    return v


def exact_cov(n, k, l):
    # Dirichlet(1,...,1) exact moment, rational arithmetic.
    m_k = Fraction(n * math.factorial(k), rising(n, k))
    m_l = Fraction(n * math.factorial(l), rising(n, l))
    cross = Fraction(n * math.factorial(k + l) + n * (n - 1) * math.factorial(k) * math.factorial(l), rising(n, k + l))
    return cross - m_k * m_l


def analytic_checks():
    v33, v35, v55 = sigma(3, 3), sigma(3, 5), sigma(5, 5)
    assert (v33, v35, v55) == (360, 28800, 3254400)
    residual = Fraction(v55) - Fraction(v35 * v35, v33)
    assert residual == 950400
    # c/a = (pi^5/10)/(pi^3/6) = 3*pi^2/5.
    opt_coefficient_over_pi2 = Fraction(3, 5) * Fraction(v35, 9 * v33)
    assert opt_coefficient_over_pi2 == Fraction(16, 3)
    fixed_variance_over_pi10 = Fraction(v55, 900)
    best_variance_over_pi10 = residual / 900
    assert (fixed_variance_over_pi10, best_variance_over_pi10) == (3616, 1056)
    corr_defect_over_pi4 = Fraction(9, 800) * (Fraction(v55 * v33 - v35 * v35, v33 * v33))
    assert corr_defect_over_pi4 == Fraction(297, 10)
    assert Fraction(best_variance_over_pi10, fixed_variance_over_pi10) == Fraction(66, 226)
    print('EXACT_FACTORIAL_INFLUENCE_COVARIANCE_PASSED')
    print('SHARP_SECOND_ORDER_WEIGHT_AND_1056_VARIANCE_PASSED')
    print('EXACT_CORRELATION_DEFECT_297_OVER_10_PASSED')

    for n in (30, 100, 300, 1000):
        for k, l in ((3, 3), (3, 5), (5, 5)):
            value = exact_cov(n, k, l)
            assert value > 0
            scaled = float(value * (n ** (k + l - 1)))
            target = sigma(k, l)
            assert 0 < scaled < target
        print('EXACT_FINITE_DIRICHLET_MOMENTS_PASSED', n)


def simulation():
    rng = random.Random(20261029)
    for n in (40, 80):
        vals = []
        for _ in range(22000):
            w = [rng.expovariate(1.0) for _ in range(n)]
            z = sum(w)
            S = sum(math.sin(math.pi * v / z) for v in w)
            A = sum(0.5 * math.sin(2.0 * math.pi * v / z) for v in w)
            vals.append((S, A))
        sm = sum(v[0] for v in vals) / len(vals)
        am = sum(v[1] for v in vals) / len(vals)
        covSB = sum((s-sm) * ((a-s)-(am-sm)) for s,a in vals) / len(vals)
        varB = sum(((a-s)-(am-sm))**2 for s,a in vals) / len(vals)
        lam = covSB/varB
        weights = [((1.0 + lam) * s - lam * a) for s,a in vals]
        fixed = [(4*s-a)/3 for s,a in vals]
        def vvar(v):
            m = sum(v) / len(v)
            return sum((x-m)**2 for x in v)/len(v)
        assert lam > 1.0/3
        assert vvar(weights) < vvar(fixed)
        print('INDEPENDENT_CIRCLE_ENDPOINT_MONTE_CARLO_PASSED', n,
              'n2_delta=%.6f' % (n*n*(lam-1.0/3)),
              'variance_ratio=%.6f' % (vvar(weights)/vvar(fixed)))


if __name__ == '__main__':
    analytic_checks()
    if '--simulation' in sys.argv:
        simulation()
    print('ALL_CHECKS_PASSED')
