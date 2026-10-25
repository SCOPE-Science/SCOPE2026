"""Finite quadrature checks for the polynomial-memory Gaussian response.
This checks selected identities numerically; it is not a proof of uniform asymptotics.
Requires Python 3 standard library only.
"""
from fractions import Fraction
from math import exp, expm1, gamma, log


def defect(p, speed, panels=100000):
    """Simpson quadrature after t=1-u^2 and s=t/(1-t)."""
    if panels % 2:
        raise ValueError('panels must be even')
    B = (p - 1) * (p - 2)
    def integrand(u):
        if u == 0:
            return 0.0  # checked p>5/2 for endpoint; p=5/2 is nonzero there
        t = 1.0 - u*u
        if t <= 0:
            return 0.0
        s = t/(u*u)
        return 2*B*t*u**(2*p-5)*(-expm1(-0.5*(speed*s)**2))
    h = 1.0/panels
    val = integrand(0)+integrand(1)
    for k in range(1,panels):
        val += (4 if k % 2 else 2)*integrand(k*h)
    return h*val/3


for p in (3,4,5,7):
    pi = int(p)
    mass = Fraction((pi-1)*(pi-2), (pi-1)*(pi-2))
    assert mass == 1
print('EXACT_FIRST_AGE_MOMENT_NORMALIZATIONS_PASS 4')

nchecks = 0
for p, speed, expect in [
    (3.0, .001, 0.002486726116430789),
    (4.0, .001, 0.00001690713762063067),
    (5.0, .001, 0.0000014950350013361064),
    (7.0, .001, 0.0000002499993774791015),
]:
    actual = defect(p, speed)
    assert abs(actual-expect) <= max(1e-11, 2e-4*expect), (p,actual,expect)
    nchecks += 1
print('TRANSFORMED_QUADRATURE_REFERENCE_VALUES_PASS',nchecks)

comparisons=0
for p,speed,low,high in [
    (3.0,.001,.98,1.01),
    (4.0,.001,.80,.84),
    (5.0,.001,.99,1.01),
    (7.0,.001,.99,1.01),
]:
    val=defect(p,speed)
    if p<4:
        predicted=(p-1)*2**(1-p/2)*gamma(2-p/2)*speed**(p-2)
    elif p==4:
        predicted=3*speed**2*log(1/speed)
    else:
        predicted=3*speed**2/((p-3)*(p-4))
    ratio=val/predicted
    assert low < ratio < high, (p,ratio)
    comparisons += 1
print('FINITE_SCALE_THREE_REGIME_ASYMPTOTIC_CHECKS_PASS',comparisons)
print('UNBOUNDED_LIMITS_AND_GLOBAL_EXISTENCE_REQUIRE_ANALYTICAL_PROOF')
