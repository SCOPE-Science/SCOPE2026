"""Independent numerical diagnostics for the rectangle translation theorem.
Run: python3 verify.py. Uses only the Python 3 standard library.
All global statements are proved analytically in RESULT.md; the checks are finite.
"""
import math
import random

EPS = 1e-13


def critical(a, b):
    assert a > b > 0.0
    upper = math.sqrt(2.0) - 1.0
    lo, hi = 0.0, upper
    r = a / b
    for _ in range(85):
        z = (lo + hi) / 2.0
        if z**4 - 4*z*z + 4*r*z - 1.0 > 0:
            hi = z
        else:
            lo = z
    z = (lo + hi) / 2.0
    theta = 2 * math.atan(z)
    t0 = (a - b*z) * (1 + z*z) / (1 - z*z)
    return z, theta, t0


def tstationary(a, b, theta):
    return (a*math.cos(theta) - b*math.sin(theta)) / math.cos(2*theta)


def optimum(a, b, t):
    """Theorem's global value and first-quadrant angle."""
    _, theta0, t0 = critical(a, b)
    D = math.hypot(a, b)
    if t <= t0:
        return b*(a-t), 0.0
    if t >= D:
        return 0.0, math.atan2(b, a)
    lo, hi = theta0, math.atan2(b, a)
    for _ in range(85):
        mid = (lo + hi) / 2
        if tstationary(a, b, mid) < t:
            lo = mid
        else:
            hi = mid
    theta = (lo+hi)/2
    return (a - t*math.cos(theta))*(b - t*math.sin(theta)), theta


def area_by_intervals(a, b, dx, dy):
    """Direct intersection of coordinate intervals, without critical formulas."""
    def length(p, q, c, d):
        return max(0.0, min(q, d)-max(p, c))
    return length(-a/2, a/2, dx-a/2, dx+a/2) * length(-b/2, b/2, dy-b/2, dy+b/2)


def brute(a, b, t, count=10000):
    out = (-1, 0.0)
    for k in range(count+1):
        theta = math.pi*k/(2*count)
        area = area_by_intervals(a,b,t*math.cos(theta),t*math.sin(theta))
        if area > out[0]: out = (area, theta)
    return out


def main():
    rg = random.Random(20261015)
    checked = 0
    ratios = [1.00001, 1.01, 1.1, 1.2, 1.5, 2, 3, 7, 30, 100]
    for ratio in ratios:
        b = 0.2 + 2*rg.random()
        a = ratio*b
        z, theta0, t0 = critical(a,b)
        D = math.hypot(a,b)
        assert 0 < z < math.sqrt(2)-1 and 0 < theta0 < math.atan2(b,a)
        assert b < D and 0 < t0 < a
        # Endpoint equality and strict max-angle jump.
        faxis = area_by_intervals(a,b,t0,0)
        foff = area_by_intervals(a,b,t0*math.cos(theta0),t0*math.sin(theta0))
        assert abs(faxis-foff) < 3e-12 * (a*b+1)
        assert abs(tstationary(a,b,theta0)-t0) < 3e-11*a
        checked += 4
        for frac in [0.02, 0.5, 0.999, 1.0, 1.001, 0.5*(1+D/t0), 0.99*D/t0, (D-1e-5*b)/t0]:
            t = min(D-1e-5*b, frac*t0)
            val,theta = optimum(a,b,t)
            vdirect = area_by_intervals(a,b,t*math.cos(theta),t*math.sin(theta))
            assert abs(vdirect-val) < 1e-10*max(a*b,1), (ratio,t,val,vdirect)
            gridval,gridtheta=brute(a,b,t,3500)
            # Grid is a lower bound. Its loss for very localized high-t optima is allowed.
            assert val >= gridval - 3e-11*max(a*b,1), (ratio,t,val,gridval)
            # Angular mesh convergence for non-extreme comparisons.
            if t < D - 0.03*b:
                assert val-gridval < 7e-7*max(a*b,1), (ratio,t,val,gridval)
            checked += 3
    # One-sided derivative jump at the unique transition for three shapes.
    for a,b in [(1.1,1.0),(2.0,1.0),(8.0,1.0)]:
        _,th,t0=critical(a,b)
        dt = 1e-7*b
        v0=optimum(a,b,t0)[0]
        left=(v0-optimum(a,b,t0-dt)[0])/dt
        right=(optimum(a,b,t0+dt)[0]-v0)/dt
        jump=t0*math.sin(th)*math.cos(th)
        assert abs((right-left)-jump) < 1e-5*b, (left,right,jump)
        checked += 1
    # Slender-rectangle asymptotics: critical radius and jump.
    a,b=1000.0,1.0
    _,th,t0=critical(a,b)
    assert abs(th - b/(2*a)) < 2e-9
    assert abs(t0 - (a-b*b/(8*a))) < 3e-9
    checked += 2
    print('RECTANGLE_COVARIOGRAM_CHECK_OK comparisons=%d' % checked)


if __name__ == '__main__':
    main()
