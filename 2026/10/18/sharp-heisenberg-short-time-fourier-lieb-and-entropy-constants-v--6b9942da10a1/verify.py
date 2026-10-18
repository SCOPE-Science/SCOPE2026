"""Supplementary numerical and algebraic checks for Gaussian Heisenberg-STFT moments.

Scientific object: the transform with right Heisenberg translations and Euclidean modulations.
The infinite-dimensional statements are proved analytically in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln


def matrix_values(n, epsilon, v, c):
    """Return exact Gaussian Hessian and its minimum for a fixed translation."""
    d = 2 * n + 1
    Jv = np.concatenate((v[n:], -v[:n]))
    u = (epsilon / 2.0) * Jv
    L = np.eye(d)
    L[-1, :-1] = u
    shift = np.concatenate([v, [c]])
    M = np.eye(d) + L.T @ L
    b = L.T @ shift
    minimum = float(shift @ shift - b @ np.linalg.solve(M, b))
    return M, minimum


def moment_ratio(n, exponent, epsilon):
    assert n >= 1 and exponent > 1 and epsilon > 0
    r = epsilon * epsilon / (8.0 * math.pi * exponent)
    integrand = lambda y: math.exp((n - 1) * math.log(y) - y +
                                   (1.0 - exponent / 2.0) * math.log1p(r * y) - gammaln(n)) if y > 0 else 0.0
    return quad(integrand, 0, math.inf, epsabs=2e-12, epsrel=2e-12)[0]


def entropy_excess(n, epsilon):
    r = epsilon * epsilon / (16.0 * math.pi)
    fun = lambda y: math.exp((n - 1) * math.log(y) - y - gammaln(n)) * math.log1p(r * y) if y > 0 else 0.0
    return quad(fun, 0, math.inf, epsabs=2e-12, epsrel=2e-12)[0]


def main():
    rng = np.random.default_rng(2026)
    # Matrix determinant and completed-square identities, without assuming any dimension.
    count = 0
    for n in range(1, 6):
        d = 2 * n + 1
        for _ in range(25):
            epsilon = float(np.exp(rng.uniform(-2, 2)))
            v = rng.normal(size=2*n)
            c = float(rng.normal())
            M, minimum = matrix_values(n, epsilon, v, c)
            H = 1.0 + epsilon**2 * (v @ v) / 16.0
            expected_det = (2.0 ** d) * H
            expected_min = (v @ v) / 2.0 + c*c / (2.0 * H)
            assert math.isclose(np.linalg.det(M), expected_det, rel_tol=2e-12, abs_tol=2e-12)
            assert math.isclose(minimum, expected_min, rel_tol=2e-12, abs_tol=2e-12)
            count += 1
    print('Gaussian Hessian checks:', count)
    # Sharp upper constant: the exact Gamma expectation is strict for any epsilon>0,
    # and approaches unity at the Euclidean contraction epsilon -> 0.
    for n in (1,2,3,5):
        for p in (2.0, 2.5, 3.0, 4.0, 6.0):
            vals = [moment_ratio(n,p,e) for e in (0.05,0.2,1.0,3.0)]
            assert abs(vals[0]-1) < 0.01
            assert all(vals[i] >= vals[i+1]-1e-12 for i in range(3))
            if p==2: assert all(abs(x-1)<1e-11 for x in vals)
            else: assert all(x < 1 for x in vals)
    print('Gamma moment monotonicity and q=2 checks: 20')
    # Asymptotic coefficient independent of numerical differentiation of the STFT.
    for n,p in ((1,3.0),(2,4.0),(4,7.0)):
        eps=0.01
        defect = 1-moment_ratio(n,p,eps)
        theoretical=n*(p-2)*eps**2/(16*math.pi*p)
        assert abs(defect/theoretical-1)<1e-4, (n,p,defect/theoretical)
    print('Quadratic sharpness coefficients: 3')
    # Shannon entropy is independently recovered as -2d/dp of the p-th moment at p=2.
    for n,eps in ((1,.3),(1,2.),(2,1.),(4,.4)):
        step=1e-3
        diff= -(math.log(moment_ratio(n,2+step,eps))-math.log(moment_ratio(n,2-step,eps))) / step
        # log(moment) has known Euclidean component d*log(2/p).
        euclidean= -(2*n+1)*(math.log(2/(2+step))-math.log(2/(2-step)))/step
        exact = (2*n+1)+entropy_excess(n,eps)
        assert abs((diff+euclidean)-exact)<3e-6, (n,eps,diff+euclidean,exact)
    print('Independent entropy derivatives: 4')
    print('PASS')


if __name__ == '__main__':
    main()
