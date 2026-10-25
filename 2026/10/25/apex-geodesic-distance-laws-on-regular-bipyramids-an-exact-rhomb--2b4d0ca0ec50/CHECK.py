"""Reproduce numerical checks for the exact apex-distance law.

Python 3 with scipy and numpy. This finite test is not a universal proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def cdf(alpha, t):
    b, L = math.sin(alpha), 2 * math.cos(alpha / 2)
    if t <= 0:
        return 0.0
    if t >= L:
        return 1.0
    if (alpha <= math.pi / 2 and t <= 1) or (alpha > math.pi / 2 and t <= b):
        return alpha * t * t / (2 * b)
    u = math.asin(min(1.0, b / t))
    if alpha > math.pi / 2 and t <= 1:
        return (t * t * (alpha / 2 - math.pi + 2 * u) + 2 * b * b / math.tan(u)) / b
    return b * (1 / math.tan(u) - 1 / math.tan(alpha)) + t * t * (u - alpha / 2) / b


def cdf_integral(alpha, t):
    b, hi = math.sin(alpha), alpha / 2
    if t <= 0:
        return 0.0
    if t >= 2 * math.cos(hi):
        return 1.0
    breaks = []
    if t > 0 and t >= min(1.0, b):
        u = math.asin(min(1.0, b / t))
        breaks = [v for v in (alpha - u, alpha - math.pi + u) if 0 < v < hi]
    val = quad(lambda th: min(t*t, (b/math.sin(alpha-th))**2),
               0, hi, points=breaks, epsabs=1e-12, epsrel=1e-12)[0] / b
    return val


def test():
    cases = [0.25, 0.72, math.pi/3, 1.4, math.pi/2, 1.7, 1.9, 2.05]
    count = 0
    for alpha in cases:
        L = 2 * math.cos(alpha / 2)
        values = []
        for t in np.linspace(0.005, L * 0.999, 80):
            f = cdf(alpha, t)
            i = cdf_integral(alpha, t)
            assert abs(f-i) < 2e-11, (alpha,t,f,i)
            assert -1e-10 <= f <= 1+1e-10
            values.append(f)
            count += 1
        assert all(y >= x-1e-11 for x,y in zip(values,values[1:]))
        for endpoint in (1., math.sin(alpha)):
            if 0 < endpoint < L:
                assert abs(cdf(alpha,endpoint-1e-7) - cdf(alpha,endpoint+1e-7)) < 1e-5
    rng = np.random.default_rng(42038)
    uv = rng.random((320_000,2))
    for alpha in [math.pi/3, 1.9]:
        q = np.sum(uv**2,axis=1) + 2*math.cos(alpha)*uv[:,0]*uv[:,1]
        assert abs(np.mean(q)-(2/3+math.cos(alpha)/2)) < 0.004
        assert abs(np.mean(q**2)-(28/45+math.cos(alpha)+4*math.cos(alpha)**2/9)) < 0.009
        for t in [0.5,0.85,1,1.2]:
            if t<2*math.cos(alpha/2):
                assert abs(np.mean(q<=t*t)-cdf(alpha,t)) < 0.008
    for alpha, power, coefficient in [
        (math.pi/3, 2, 2.0),
        (math.pi/2, 1.5, 4*math.sqrt(2)/3),
        (1.9, 1.5, (8/3)*math.sqrt(2/math.sin(1.9))),
    ]:
        first = 1 if alpha <= math.pi/2 else math.sin(alpha)
        eps = 0.002
        cone = alpha * (first+eps)**2 / (2*math.sin(alpha))
        ratio = (cone-cdf(alpha,first+eps))/eps**power
        assert abs(ratio/coefficient - 1) < 0.008, (alpha,ratio,coefficient)
    print(f"PASS: {count} exact-form/integral comparisons; 2 distribution simulations; 3 cusp coefficients")


if __name__ == '__main__':
    test()
