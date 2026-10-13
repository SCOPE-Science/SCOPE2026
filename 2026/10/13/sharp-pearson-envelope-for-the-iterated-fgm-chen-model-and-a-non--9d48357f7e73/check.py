"""Reproduce Chen--IFGM Pearson extrema using only Python's standard library.

This numerical checker supplements, but does not replace, the analytic proof.
"""
from math import exp, log1p, sqrt, isfinite


def simpson_moments(theta, shape, n=262144, end=48.0):
    """Integrate against Exp(1) using composite Simpson on [0,end]."""
    if n % 2:
        raise ValueError("n must be even")
    h = end / n
    sums = [0.0] * 4
    for k in range(n + 1):
        y = k * h
        q = log1p(y / theta) ** (1.0 / shape)
        e = exp(-y)
        u = 1.0 - e
        values = (q, q*q, q*(1.0-2.0*u), q*u*(2.0-3.0*u))
        wt = (1 if k in (0, n) else 4 if k % 2 else 2) * e
        for j in range(4):
            sums[j] += wt * values[j]
    mean, second, aa, bb = (h * x / 3.0 for x in sums)
    var = second-mean**2
    assert var > 0.0
    a, b = aa**2 / var, bb**2 / var
    assert a > b > 0.0
    return a, b


def upper(ga):
    return (3.0-ga+sqrt(max(0.0,9.0-6.0*ga-3.0*ga*ga))) / 2.0


def optimum(a, b):
    d = sqrt((2*a-b)**2+3*b*b)
    ga = -1.0+2.0*(2*a-b)/d
    om = upper(ga)
    return (-a+2*b+d, ga, om)


def run(theta, shape, reference_corner, reference_max):
    a, b = simpson_moments(theta, shape)
    rho, ga, om = optimum(a, b)
    assert -1.0 < ga < 1.0
    assert om >= -1.0-ga
    assert abs(rho-(a*ga+b*om)) < 2e-13
    assert abs((a+b)-reference_corner) < 1e-5
    assert abs(rho-reference_max) < 1e-5
    assert rho > a+b+0.015
    assert a > 0 and b > 0
    for shift in [-1e-3,-5e-4,5e-4,1e-3]:
        g = ga + shift
        assert a*g+b*upper(g) < rho
    print(f"theta={theta} shape={shape} a={a:.12f} b={b:.12f}")
    print(f"rho(1,1)={a+b:.12f}, rho_max={rho:.12f}")
    print(f"unique maximizing gamma={ga:.12f}, omega={om:.12f}")
    print(f"rho_min={-a:.12f} at (-1,0)")


if __name__ == "__main__":
    run(2.0, 1.5, .41806460619, .44264311920)
    run(1.0, 1.0, .41785652950, .44838065272)
    print("CHECK_OK")
