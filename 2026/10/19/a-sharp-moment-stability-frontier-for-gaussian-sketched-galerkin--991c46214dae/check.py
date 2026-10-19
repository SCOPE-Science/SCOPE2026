"""Finite reproducibility checks for a Gaussian-sketch Galerkin rate law.

These numerical checks corroborate, but do not prove, the Student-law and
infinite-moment theorems.  Requires NumPy and SciPy.
"""
from math import isclose, sqrt
import numpy as np
from scipy.special import betainc
from scipy.stats import t


def coefficient(A, u, S):
    g = S @ u
    return float((g @ (S @ (A @ u))) / (g @ g))


def run():
    A = np.diag([1., 9.])
    u = np.array([1., 1.]) / sqrt(2.)
    mu = float(u @ (A @ u))
    beta = float(np.linalg.norm(A @ u - mu * u))
    assert isclose(mu, 5., abs_tol=1e-14)
    assert isclose(beta, 4., abs_tol=1e-14)
    # Deterministic witness: even SPD A admits a negative sketched rate.
    S = np.array([[1., -0.8]])
    assert coefficient(A, u, S) < 0.
    # Algebraic formula for the one-step fresh-sketch mean-square factor.
    h = 0.2
    assert isclose((1-h*mu)**2+h*h*beta**2/(3-2), 0.64, abs_tol=1e-14)
    assert isclose(2*mu/(mu*mu+beta*beta/(3-2)), 10/41, abs_tol=1e-14)
    for ell in [1, 2, 3, 5, 8, 16]:
        z = beta**2/(mu**2+beta**2)
        prob_beta = 0.5*betainc(ell/2, .5, z)
        prob_student = t.cdf(-sqrt(ell)*mu/beta, df=ell)
        assert abs(prob_beta-prob_student) < 2.e-13
        rng = np.random.default_rng(444 + ell)
        N = 120_000
        G = rng.standard_normal((N, ell))
        H = rng.standard_normal((N, ell))
        rates = mu + beta * np.sum(G*H, axis=1)/np.sum(G*G, axis=1)
        # Compare empirical quantiles to exact Student quantiles and mean to mu
        # only where the corresponding population moment exists.
        for q in [.2, .5, .8]:
            actual = np.quantile(rates, q)
            expected = mu+beta/sqrt(ell)*t.ppf(q, ell)
            tol = .13 if ell < 3 else .065
            assert abs(actual-expected) < tol, (ell, q, actual, expected)
        if ell >= 3:
            pop = (1-h*mu)**2 + h*h*beta*beta/(ell-2)
            sample = float(np.mean((1-h*rates)**2))
            # Low-df heavy tails cause high Monte Carlo variance.
            assert abs(sample-pop) < (.4 if ell == 3 else .15 if ell == 5 else .05), (ell, sample, pop)
    print('PASS: deterministic SPD growth witness; Student/beta law for six sketch sizes;')
    print('      18 Monte Carlo quantile comparisons; four finite-second-moment comparisons;')
    print('      exact three-row Euler threshold and stability factor.')
    print('Limits: numerical sampling cannot demonstrate any infinite expectation.')


if __name__ == '__main__':
    run()
