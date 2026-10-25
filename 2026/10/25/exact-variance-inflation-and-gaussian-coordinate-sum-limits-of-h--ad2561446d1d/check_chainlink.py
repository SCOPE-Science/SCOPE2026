"""Reproducibility checks for homogeneous chainlink-polytope coordinate-sum laws.
Requires Python 3 and NumPy. No external data or services.
"""
import itertools
import math
from fractions import Fraction
from math import comb
import numpy as np


def cycle_matching_counts(n):
    counts = [0] * (n // 2 + 1)
    for mask in range(1 << n):
        edges = [i for i in range(n) if (mask >> i) & 1]
        if any(((i + 1) % n) in edges for i in edges):
            continue
        counts[len(edges)] += 1
    return counts


def rational_moments(n, a, ell):
    a, ell = Fraction(a), Fraction(ell)
    counts = cycle_matching_counts(n)
    d = ell * ell / 2
    Z = Fraction(0)
    numerator = Fraction(0)
    for k, count in enumerate(counts):
        weight = Fraction(count) * (-1) ** k * a ** (n - 2 * k) * d ** k
        Z += weight
        numerator += weight * ((n - 2 * k) * a * a / 12 + k * ell * ell / 6)
    return Z, numerator / Z


def eigen_formula(n, a, ell):
    D = math.sqrt(a * a - 2 * ell * ell)
    rho = (a - D) / (a + D)
    eta = ell ** 2 * (a * a - ell * ell) / (6 * D * (a + D))
    vol = ((a + D) / 2) ** n + ((a - D) / 2) ** n
    variance = n * (a * a / 12 + eta * (1 - rho ** (n - 1)) / (1 + rho ** n))
    return vol, variance


def tilted_integral(n, a, ell, t, m=28):
    # Tensor Gaussian quadrature; independent integration across the full box.
    # The characteristic function of the excluded region is discontinuous,
    # so this is a broad diagnostic, not a numerical certificate.
    grid, wgts = np.polynomial.legendre.leggauss(m)
    grid = (grid + 1) * a / 2
    wgts = wgts * a / 2
    arr = np.zeros((m,) * n, dtype=float)
    for ix in itertools.product(range(m), repeat=n):
        x = [grid[j] for j in ix]
        if all(x[i] - x[(i + 1) % n] <= a - ell for i in range(n)):
            arr[ix] = math.exp(t * sum(x)) * math.prod(wgts[j] for j in ix)
    return float(arr.sum())


def eigen_tilt(n, a, ell, t):
    if abs(t) < 1e-9:
        b, d = a, ell * ell / 2
    else:
        b = math.expm1(a * t) / t
        d = math.exp(a * t) * (math.cosh(ell * t) - 1) / t ** 2
    D = math.sqrt(b*b-4*d)
    return ((b + D)/2)**n + ((b-D)/2)**n


def main():
    count_cases = 0
    exact_cases = 0
    for n in range(3, 11):
        counts = cycle_matching_counts(n)
        for k, v in enumerate(counts):
            target = n * comb(n-k, k) // (n-k) if k <= n//2 else 0
            assert v == target, (n, k, v, target)
            count_cases += 1
        for a, ell in [(Fraction(1), Fraction(1, 2)), (Fraction(3,2), Fraction(1, 4)),
                       (Fraction(2),Fraction(1)), (Fraction(2), Fraction(1, 3))]:
            vol, var = rational_moments(n, a, ell)
            vf, wv = eigen_formula(n, float(a), float(ell))
            assert math.isclose(float(vol), vf, rel_tol=2e-12,abs_tol=2e-12), (n,a,ell,vol,vf)
            assert math.isclose(float(var), wv, rel_tol=2e-12,abs_tol=2e-12), (n,a,ell,var,wv)
            assert var > n*a*a/12
            exact_cases += 1
    tilt_cases = 0
    for n in [3]:
        for t in [-0.35, 0., 0.55]:
            estimate=tilted_integral(n, 1., .5, t, m=46)
            theory=eigen_tilt(n, 1., .5, t)
            assert abs(estimate/theory-1)<.007, (n,t,estimate,theory)
            tilt_cases += 1
    # Independent Monte Carlo check of conditional moments in 3 dimensions.
    rng=np.random.default_rng(20261018)
    cube=rng.random((750000,3))
    good=np.all(cube-np.roll(cube,-1,axis=1)<=.5,axis=1)
    assert abs(good.mean()-.625)<.003
    values=cube[good].sum(axis=1)
    assert abs(values.mean()-1.5)<.008
    assert abs(values.var()-.325)<.008
    print(f'CHECK_OK matching_counts={count_cases} exact_rational_moments={exact_cases} tilted_quadrature={tilt_cases} monte_carlo=750000')

if __name__=='__main__': main()
