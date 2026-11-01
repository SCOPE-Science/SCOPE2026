"""Independent numerical checks for flat inversion-quotient distance laws.

Requires Python 3, NumPy, and SciPy. No data files or network access.
Run: python verify.py
"""
import math
import numpy as np
from scipy.integrate import quad


def torus_cdf_rect(r, a, b):
    """Exact ball intersection area fraction of a rectangular 2-torus."""
    assert a > 0 and b > 0
    h, k = a / 2, b / 2
    end = math.hypot(h, k)
    if r <= 0:
        return 0.0
    if r >= end:
        return 1.0
    area = math.pi * r * r
    for z in (h, k):
        if r > z:
            area -= 2 * (r * r * math.acos(z / r) - z * math.sqrt(r * r - z * z))
    return max(0.0, min(1.0, area / (a * b)))


def pillow_cdf_rect(r, a, b):
    f = torus_cdf_rect(r, a, b)
    return 1 - (1 - f) ** 2


def pair_distances_by_lifts(a, b, number, seed):
    rng = np.random.default_rng(seed)
    x, y = rng.random((2, number, 2))
    z1 = (x - y + 0.5) % 1.0 - 0.5
    z2 = (x + y + 0.5) % 1.0 - 0.5
    scale = np.array([a, b])
    return np.minimum(np.linalg.norm(z1 * scale, axis=1),
                      np.linalg.norm(z2 * scale, axis=1))


def analytic_mean_squared(a, b):
    points = sorted(set([0., min(a,b)/2, max(a,b)/2, math.hypot(a,b)/2]))
    return sum(quad(lambda r: 2*r*(1-torus_cdf_rect(r,a,b))**2,
                    left, right, epsabs=1e-12)[0]
               for left,right in zip(points[:-1], points[1:]))


def run():
    checks = 0
    for a,b in [(1.,1.), (2.,1.), (1.1,0.3), (0.2,3.0)]:
        d = pair_distances_by_lifts(a,b,150000, int(a*10000+b*1000))
        for r in np.linspace(0,math.hypot(a,b)/2,31):
            empirical = np.mean(d <= r)
            theory = pillow_cdf_rect(r,a,b)
            if abs(empirical-theory) > 0.010:
                raise AssertionError((a,b,r,empirical,theory))
            checks += 1
        emp_mean = np.mean(d*d)
        ana_mean = analytic_mean_squared(a,b)
        if abs(emp_mean-ana_mean) > 0.008*max(ana_mean,1e-3):
            raise AssertionError((a,b,emp_mean,ana_mean))
        checks += 1
    # Fixed-area square stochastic dominance at 300 intermediate distances.
    for ratio in [1.05,1.2,1.5,2,3,5,10]:
        a,b=math.sqrt(ratio),1/math.sqrt(ratio)
        for r in np.linspace(0,max(math.hypot(a,b),math.sqrt(2))/2,300):
            if pillow_cdf_rect(r,1.,1.)+3e-14 < pillow_cdf_rect(r,a,b):
                raise AssertionError((ratio,r))
            checks += 1
    # Exact local polynomial and far tail asymptotics.
    for a,b in [(1.,1.), (2.,1.)]:
        R=math.hypot(a,b)/2
        for r in [0.001*min(a,b),0.1*min(a,b),0.49*min(a,b)]:
            expected=2*math.pi*r*r/(a*b)-(math.pi*r*r/(a*b))**2
            assert abs(pillow_cdf_rect(r,a,b)-expected) < 1e-14
            checks+=1
        C=((4*R)**2/(2*(a*b)**2))**2
        for epsilon in [1e-3,3e-4,1e-4]:
            ratio=(1-torus_cdf_rect(R-epsilon,a,b))**2/(C*epsilon**4)
            if abs(ratio-1)>.02:
                raise AssertionError((a,b,epsilon,ratio))
            checks+=1
    # A finite even-order group does not satisfy independent sum/difference.
    # For Z/2 the quotient is itself; the claimed squared survival formula fails.
    assert 0.5 != 1-(1-0.5)**2
    checks+=1
    print(f'PASS: {checks} deterministic threshold checks and four Monte Carlo distance ensembles')
    print('square pillowcase mean squared intrinsic distance:',f'{analytic_mean_squared(1.,1.):.15f}')
    print('fixed-area square comparison, a:b=2:1:',f'{analytic_mean_squared(math.sqrt(2),1/math.sqrt(2)):.15f}')
    print('square pillowcase fourth-power terminal tail constant:',16.)

if __name__=='__main__':
    run()
