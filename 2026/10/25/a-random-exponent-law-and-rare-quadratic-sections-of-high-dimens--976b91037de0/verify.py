"""Independent finite checks for affine sections of regular simplices.

Run: python3 verify.py
Standard library only. These numerical checks are not infinite proofs.
"""
import math
import random
from statistics import NormalDist

RNG = random.Random(24010246)
PHI = NormalDist()


def simpson(f, lo, hi, steps=20000):
    assert steps % 2 == 0
    h = (hi-lo)/steps
    total = f(lo) + f(hi)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * f(lo+j*h)
    return total*h/3


def gaussian_max(m):
    def integrand(z):
        return m*z*PHI.pdf(z)*(PHI.cdf(z)**(m-1))
    return simpson(integrand, -12., 12., 20000)


def sample(m):
    z = [RNG.gauss(0., 1.) for _ in range(m)]
    center = sum(z)/m
    r = math.sqrt(sum((x-center)**2 for x in z))
    width = max(z)-min(z)
    s = min(z)+RNG.random()*width
    count = sum(x < s for x in z)
    fast = count*(m-count)
    direct = sum((z[i]-s)*(z[j]-s) < 0 for i in range(m) for j in range(i+1,m))
    assert fast == direct
    return fast,width/r


def checks():
    # Exhaustively compare all pairs against the edge-crossing formula
    # for each generated configuration.
    tests = 0
    for m in range(3,24):
        for _ in range(110):
            sample(m)
            tests += 1

    # Numerical check of the Gaussian mean-maximum identity and the
    # geometry-to-Gaussian expectation, using two independent procedures.
    estimates = []
    for m in (3,4,6,10):
        total_w = 0.
        total_vw = 0.
        for _ in range(75000):
            v,w = sample(m)
            total_w += w
            total_vw += w*v
        empirical = total_vw / total_w
        expected = (m*(m-1)/2)/(math.sqrt(math.pi)*gaussian_max(m))
        assert abs(empirical-expected) < 0.08, (m,empirical,expected)
        estimates.append((m,round(empirical,4),round(expected,4)))

    # Analytic constant in the exact expectation asymptotic is independently
    # checked as a one-dimensional Gaussian integral.
    integral = simpson(lambda s: PHI.cdf(s)*(1-PHI.cdf(s)), -11., 11.)
    assert abs(integral-1/math.sqrt(math.pi)) < 1e-11
    # End-to-end consistency of the Gaussian-quantile rare-event constant.
    for a in (.05,.1,.2):
        q = PHI.inv_cdf((1+math.sqrt(1-4*a))/2)
        assert abs(PHI.cdf(q)*(1-PHI.cdf(q))-a) < 1e-12
    print('PASS: %d direct edge counts; four weighted finite-sample expectation checks' % tests)
    print('Mean checks: (m, empirical, exact):',estimates)
    print('PASS: Gaussian integral and three threshold-quantile identities')
    print('LIMITATION: finite tests do not establish asymptotic claims')

if __name__ == '__main__':
    checks()
