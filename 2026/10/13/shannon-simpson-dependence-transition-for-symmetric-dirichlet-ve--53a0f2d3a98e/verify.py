"""Reproducibility checks for Shannon entropy and Simpson concentration of symmetric Dirichlet vectors.

Requires Python 3, numpy, scipy, and sympy. Tests support but do not replace
proofs of the all-parameter formulas.
"""
import math
import numpy as np
import sympy as sp
from scipy.special import polygamma


def formulas(m, alpha):
    A = m * alpha
    cov = -alpha * (m - 1) / ((A + 1) ** 2 * (A + 2))
    vh = (alpha + 1) / (A + 1) * float(polygamma(1, alpha + 1)) - float(polygamma(1, A + 1))
    vq = 2 * (m - 1) * alpha * (alpha + 1) / ((A + 1) ** 2 * (A + 2) * (A + 3))
    return cov, vh, vq


def check_symbolics():
    m, a, d, t, T = sp.symbols('m a d t T', positive=True)
    A = m * a
    # Uncentered second moments from Dirichlet rising factorials.
    eq2 = (a + 1) * ((a + 2) * (a + 3) + (m - 1) * a * (a + 1)) / ((A + 1) * (A + 2) * (A + 3))
    eq = (a + 1) / (A + 1)
    vq = 2 * (m - 1) * a * (a + 1) / ((A + 1)**2 * (A + 2) * (A + 3))
    assert sp.factor(eq2 - eq**2 - vq) == 0
    # Here d = psi(A+1)-psi(a+1), t = psi1(a+1), T = psi1(A+1).
    e_hq = (a + 1) / ((A + 1) * (A + 2)) * (
        (A + 2) * (d + 1/(A + 1) + 1/(A + 2))
        - (a + 2) * (1/(a + 1) + 1/(a + 2)))
    cov = -a * (m - 1) / ((A + 1)**2 * (A + 2))
    assert sp.factor(e_hq - d*eq - cov) == 0
    e_h2 = (a + 1)/(A + 1) * (
        (-d + 1/(a + 1) - 1/(A + 1))**2
        + t - 1/(a + 1)**2 - T + 1/(A + 1)**2)
    e_h2 += (m - 1)*a/(A + 1) * (
        (-d - 1/(A + 1))**2 - T + 1/(A + 1)**2)
    assert sp.factor(e_h2 - d**2 - ((a + 1)/(A + 1)*t - T)) == 0
    print('symbolic Dirichlet cross-moment, entropy variance, concentration variance: PASS')


def check_monte_carlo():
    rng = np.random.default_rng(482731)
    n = 300000
    total = 0
    for m in (2, 3, 7, 20):
        for a in (0.2, 1.0, 3.0):
            sample = rng.dirichlet([a]*m, size=n)
            h = -(sample*np.log(sample)).sum(axis=1)
            q = (sample*sample).sum(axis=1)
            observed = np.cov(h, q, bias=True)[0, 1]
            target, var_h, var_q = formulas(m, a)
            stderr = (var_h*var_q/n)**0.5 * 1.4
            assert abs(observed-target) <= 6 * stderr, (m,a,observed,target,stderr)
            total += 1
    print(f'{total} seeded Monte Carlo cross-covariance comparisons ({n} samples per case): PASS')


def check_asymptotics():
    # Correlation limiting profile for fixed alpha and m growing.
    alphas = (0.05, 0.3, 1, 3, 20)
    limits = []
    for a in alphas:
        z = (a + 1) * float(polygamma(1, a + 1)) - 1
        limit = -1/math.sqrt(2*(a+1)*z)
        limits.append(limit)
        cov, vh, vq = formulas(200000, a)
        measured = cov/math.sqrt(vh*vq)
        assert abs(measured-limit) < 1.0e-4, (a,measured,limit)
    assert all(limits[j] > limits[j+1] for j in range(len(limits)-1)),limits
    sparse = -math.sqrt(3)/(2*math.sqrt(2*float(sp.zeta(3))-math.pi**2/6))
    for m in (2, 3, 10, 100):
        c,vh,vq = formulas(m, 1e-7)
        assert abs(c/math.sqrt(vh*vq)-sparse) < 3e-4
    print('large-dimension correlation, alpha ordering, fixed-dimension sparse limit: PASS')
    print('sparse-limit correlation =',format(sparse,'.12f'))
    print('fixed-alpha limiting correlations =',[(a,round(x,10)) for a,x in zip(alphas,limits)])

if __name__ == '__main__':
    check_symbolics()
    check_monte_carlo()
    check_asymptotics()
    print('ALL CHECKS PASSED')
