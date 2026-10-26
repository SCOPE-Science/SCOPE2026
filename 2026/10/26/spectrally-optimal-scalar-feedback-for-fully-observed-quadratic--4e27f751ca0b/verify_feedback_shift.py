"""Finite reproducibility checks for an optimal scalar-feedback shift theorem.

Run: python3 verify_feedback_shift.py. These numerical checks supplement,
not replace, the algebraic proof in RESULT.md.
"""
import math
import random


def root_condition(alpha, lam, k):
    return math.hypot(1.0, math.sqrt(alpha)*lam)/(lam+k)


def optimum(alpha, a, b):
    wa = math.hypot(1., math.sqrt(alpha)*a)
    wb = math.hypot(1., math.sqrt(alpha)*b)
    k = (wa + wb) / (alpha*(b*wa+a*wb))
    midpoint = (b*wa+a*wb)/(wa+wb)
    theta = math.atan(math.sqrt(alpha)*b)-math.atan(math.sqrt(alpha)*a)
    upper = 1.0 / math.cos(theta/2)**2
    return k, midpoint, upper


def condition(alpha, eigenvalues, k):
    vals = [root_condition(alpha, x, k) for x in eigenvalues]
    return (max(vals)/min(vals))**2


cases = [(1., 0., 3.), (1., 1., 3.), (1., 0.01, 100.), (.001, .0001, 1e5),
         (15., .5, 8.), (.004, 2., 20.), (100., 1., 1.1)]
for alpha, a, b in cases:
    k, m, upper = optimum(alpha, a, b)
    assert a < m < b
    assert math.isclose(root_condition(alpha, a, k),
                        root_condition(alpha, b, k), rel_tol=5e-13)
    exact = condition(alpha, [a, m, b], k)
    assert math.isclose(exact, upper, rel_tol=2e-12)
    assert 1 <= exact < 2
    assert condition(alpha, [a, b], k) < 1+2e-12
    for s in (.001, .1, .5, 1.1, 2., 10., 100.):
        assert condition(alpha, [a, m, b], k*s) > exact + 1e-14
    print(f'alpha={alpha:g} endpoints=({a:g},{b:g}) optimal_shift={k:.12g} '
          f'interior={m:.12g} sharp_kappa={exact:.12g} bounded_by={upper:.12g}')

rng = random.Random(20261022)
for trial in range(500):
    alpha = math.exp(rng.uniform(-7,7))
    a = 0. if trial % 20 == 0 else math.exp(rng.uniform(-4,0))
    b = a+math.exp(rng.uniform(-3,5))
    eigenvalues = [a, b]+[rng.uniform(a,b) for _ in range(rng.randint(0,20))]
    k, m, upper = optimum(alpha,a,b)
    measured = condition(alpha,eigenvalues,k)
    assert 1-1e-12 <= measured <= upper*(1+3e-12)
    for s in (.02,.1,.5,.9,1.1,2.,10.,40.):
        assert condition(alpha,eigenvalues,k*s) > measured-1e-12
print('PASS: 7 sharp examples including a singular mode, 500 random finite spectra, boundary/matching checks')
