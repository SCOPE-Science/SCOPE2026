"""Standalone finite-horizon checks for a near-neutral competitive map.

The asymptotic results require the analytic estimates in RESULT.md; this
program only tests finite rational identities and representative trajectories.
"""
from fractions import Fraction as F
import math


def step(a, eps, x, y):
    return (a*x/(1+x+(1+eps)*y),
            a*y/(1+y+(1+eps)*x))


def imbalance(x, y):
    return (x-y)**2/(4*x*y)


count = 0
for a in (F(3, 2), F(2), F(7, 3)):
    for eps in (F(1, 2), F(1, 5), F(1, 10), -F(1, 5), -F(1, 3)):
        for x, y in ((F(1), F(2)), (F(3, 7), F(4, 5)),
                     (F(6, 5), F(2, 3)), (F(1, 4), F(7, 2))):
            newx, newy = step(a, eps, x, y)
            A, s = 1+x+y, x+y
            multiplier = (A+eps*s)**2/((A+eps*x)*(A+eps*y))
            assert imbalance(newx, newy) == imbalance(x, y)*multiplier
            assert (multiplier > 1) == (eps > 0)
            count += 1

# Verify the uniform log-imbalance estimate on representative finite orbits.
bound_count = 0
for a in (1.2, 1.7, 2.4, 4.0):
    c = (a-1)/a
    for eps in (0.02, 0.05, -0.02, -0.05):
        for x0, y0 in ((0.35, 0.67), (1.8, 0.7), (3.5, 0.2)):
            x, y = x0, y0
            h0 = math.log(imbalance(x, y))
            C0 = a/(a-1)*abs(1/(x0+y0)-1/(a-1))
            C1 = 4+1/(a-1)
            for n in range(301):
                err = abs(math.log(imbalance(x, y))-h0-c*eps*n)
                assert err < C0*abs(eps)+C1*n*eps*eps+1e-11
                if n < 300:
                    x, y = step(a, eps, x, y)
            bound_count += 301

# Independent iteration at three near-critical scales, compared with the
# analytically predicted centered first-passage law.
slow_count = 0
for a, s0, gamma, delta, target in (
    (2.3, 1.4, 0.75, 0.8, 0.65),
    (1.8, 2.5, 0.6, 0.9, 0.55),
):
    c = (a-1)/a
    threshold = target*target/(1-target*target)
    errs = []
    for eps in (0.02, 0.01, 0.005, 0.002):
        w0 = delta*eps**gamma
        x, y = s0*(1+w0)/2, s0*(1-w0)/2
        n = 0
        while abs((x-y)/(x+y)) < target:
            x, y = step(a, eps, x, y)
            n += 1
            assert n < 200000
        forecast = (2*gamma*math.log(1/eps)
                    +math.log(threshold/(delta*delta)))/c
        errs.append(abs(eps*n-forecast))
        slow_count += 1
    assert errs[-1] < errs[0]/3, errs

# Weak mutualism on the other side of the neutral competition threshold:
# threshold-passage errors diminish as the perturbation shrinks.
negative_count = 0
for a, s0, gamma, delta, initial_w in (
    (2.3, 1.4, 0.75, 0.8, 0.6),
    (1.8, 2.5, 0.6, 0.9, 0.4),
):
    c = (a-1)/a
    chi0 = initial_w**2/(1-initial_w**2)
    discrepancies = []
    for h in (0.02, 0.01, 0.005, 0.002):
        x, y = s0*(1+initial_w)/2, s0*(1-initial_w)/2
        n = 0
        while (x-y)/(x+y) > delta*h**gamma:
            x, y = step(a, -h, x, y)
            n += 1
            assert n < 200000
        forecast = (2*gamma*math.log(1/h)
                    +math.log(chi0/(delta*delta)))/c
        discrepancies.append(abs(h*n-forecast))
        negative_count += 1
    assert discrepancies[-1] < discrepancies[0]/3, discrepancies

print(f'VERIFY_OK: {count} exact rational multiplier/sign identities; ' 
      f'{bound_count} finite drift-bound checks; '
      f'{slow_count+negative_count} crossover first-passage trajectories')
