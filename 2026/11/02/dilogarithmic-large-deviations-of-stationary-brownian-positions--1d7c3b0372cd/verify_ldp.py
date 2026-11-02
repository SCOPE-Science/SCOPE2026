"""Independent numerical checks for a weak-rescaling Brownian stationary LDP.

Standard-library-only. The analytic proof does not rely on these calculations.
"""
import math


def dilog_unit(z):
    assert 0 <= z < 1
    s = 0.0
    p = z
    for n in range(1, 100000):
        term = p / (n*n)
        s += term
        if term < 1e-15:
            break
        p *= z
    return s


def log_mgf(eps, t):
    q = math.exp(-eps)
    z = t*t
    s = 0.0
    p = z
    for n in range(200000):
        value = -math.log1p(-p)
        s += value
        if value < 1e-15:
            break
        p *= q
    return s


def lam(t):
    return dilog_unit(t*t)


def derivative(t):
    if abs(t) < 1e-8:
        return 2*t + t**3
    return -2*math.log1p(-t*t)/t


def opt_theta(y):
    if y < 0:
        return -opt_theta(-y)
    if y == 0:
        return 0.0
    left, right = 0.0, 1.0-1e-14
    for _ in range(90):
        mid = (left+right)/2
        if derivative(mid) > y:
            right = mid
        else:
            left = mid
    return (left+right)/2


def rate(y):
    t = opt_theta(y)
    return t*y - lam(t)


def main():
    count = 0
    # Exact stationary moment generating function and dilogarithm Riemann limit.
    for theta in [0.12, 0.37, 0.71, 0.89]:
        approximations = [eps*log_mgf(eps, theta) for eps in (0.12, 0.06, 0.024, 0.009)]
        err = [abs(v-lam(theta)) for v in approximations]
        assert err[-1] < err[-2] < err[-3] < err[-4]
        assert err[-1] < 0.012
        count += 1
    # Legendre duality, strict convexity and evenness.
    for y in [0.04, 0.2, 0.8, 2.5, 6.0, 12.0]:
        t = opt_theta(y)
        assert abs(derivative(t)-y) < 1e-9
        assert abs(rate(y)-rate(-y)) < 1e-12
        assert 0 < t < 1 and rate(y) > 0
        count += 1
    # Quadratic center, including nontrivial negative quartic correction.
    for y in [0.025, 0.05, 0.1]:
        approx = y*y/4-y**4/64
        assert abs(rate(y)-approx) < y**6
        count += 1
    # Linear far-tail with universal dilogarithm endpoint constant.
    pi2over6 = math.pi**2/6
    for y in [12.0, 18.0, 24.0]:
        defect = rate(y)-(y-pi2over6)
        assert defect > 0
        assert defect < 5*math.exp(-y/2)
        count += 1
    # Exact normalized stationary variance: 2/(1-exp(-eps)).
    for eps in [0.2, 0.05, 0.01]:
        variance_scaled = 2*eps/(1-math.exp(-eps))
        assert abs(variance_scaled-2.0) < 1.2*eps
        count += 1
    print(f"PASS: {count} independent analytic/numerical checks")
    for y in [0.2, 1, 2, 5, 12]:
        print('y={:.1f}; theta*={:.9f}; I={:.10f}'.format(y,opt_theta(y),rate(y)))


if __name__ == '__main__':
    main()
