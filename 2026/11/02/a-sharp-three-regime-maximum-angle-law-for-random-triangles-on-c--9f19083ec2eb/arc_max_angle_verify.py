"""Independent numerical checks for circular-arc random-triangle maximum-angle law.

Run with Python 3 (standard library only): python arc_max_angle_verify.py
Numerical checks corroborate, but do not prove, statements for all parameters.
"""
import math
import random

PI = math.pi


def cdf_closed(L, m):
    h = 2 * m
    if h < max(2*PI/3, 2*PI-L):
        return 0.0
    if h >= 2*PI:
        return 1.0
    a = 2*PI-h
    positive = lambda z: max(0.0, z)
    return (L**3 - 3*L*a*a + 2*a**3
            - 2*positive(L-h)**3 + positive(L-2*h)**3
            + 6*(L-a)*positive(a-h)**2 + 2*positive(a-h)**3) / L**3


def cdf_integral(L, m):
    h = 2*m
    a = 2*PI-h
    if h < max(2*PI/3, 2*PI-L):
        return 0.0
    if h >= 2*PI:
        return 1.0
    cuts = sorted(set([a, L] + [c for c in (h, 2*h) if a < c < L]))
    # Simpson's rule on each polynomial piece: degree at most three, hence exact
    total = 0.0
    for x, y in zip(cuts, cuts[1:]):
        def integrand(r):
            width = r - 2*max(0, r-h) + max(0, r-2*h)
            return (L-r)*width
        total += (y-x)*(integrand(x)+4*integrand((x+y)/2)+integrand(y))/6
    return 6*total/L**3


def run():
    rng = random.Random(20261029)
    for L in [0.55*PI, PI, 1.1*PI, 1.3*PI, 4*PI/3, 1.65*PI, 2*PI]:
        lower = max(PI/3, PI-L/2)
        for m in [lower, (lower+PI)/2, 0.75*PI, 0.95*PI, PI]:
            exact = cdf_closed(L, m)
            integral = cdf_integral(L, m)
            assert abs(exact-integral) < 2e-12, (L, m, exact, integral)
        n = 25000
        count = 0
        target = max(lower, PI/2)
        for _ in range(n):
            x, y, z = sorted(rng.uniform(0, L) for i in range(3))
            mx = max(y-x, z-y, 2*PI-z+x) / 2
            count += mx < target
        assert abs(count/n-cdf_closed(L,target)) < 0.02, (L,count/n,cdf_closed(L,target))
    print('ORDER_STATISTIC_INTEGRAL_AND_MONTE_CARLO_PASSED')

    for L in [0.7*PI, PI, 1.2*PI, 4*PI/3, 1.7*PI, 2*PI]:
        lower = max(PI/3, PI-L/2)
        d = 0.002
        observed = cdf_closed(L,lower+d)
        if abs(L-4*PI/3)<1e-10:
            leading = 64*d**3/L**3
            assert abs(observed/leading-1)<0.02
        elif L <= PI:
            leading = 12*d*d/L**2
            assert abs(observed/leading-1)<0.02
        elif L < 4*PI/3:
            leading = 12*(4*PI-3*L)*d*d/L**3
            assert abs(observed/leading-1)<0.02
        else:
            leading = 108*(L-4*PI/3)*d*d/L**3
            assert abs(observed/leading-1)<0.02
    print('CRITICAL_LOWER_TAIL_EXPONENTS_PASSED')

    for L in [1.001*PI, 1.1*PI, 4*PI/3, 1.9*PI, 2*PI]:
        acute = (L-PI)**2*(4*PI-L)/L**3
        assert abs(cdf_closed(L,PI/2)-acute)<1e-12
    assert abs(cdf_closed(2*PI,PI/2)-0.25)<1e-12
    for L in (0.5*PI, PI):
        assert abs(cdf_closed(L,PI/2))<1e-12
    print('ACUTE_TRANSITION_AND_FULL_CIRCLE_BENCHMARK_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    run()
