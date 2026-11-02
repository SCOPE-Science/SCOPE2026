"""Reproduce exact and numerical checks for the two-price matching design theorem.
Run: python3 verify.py   (Python 3, NumPy, SciPy).
"""
from fractions import Fraction
from math import sqrt
import numpy as np
from scipy.optimize import minimize


def edges(m):
    return [(i, m + j, i == j) for i in range(m) for j in range(m)]


def laplacian(m, edge_weights, exact=False):
    N = 2 * m
    zero = Fraction(0) if exact else 0.0
    L = [[zero for _ in range(N)] for _ in range(N)]
    for (i, j, _), w in zip(edges(m), edge_weights):
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return L


def determinant_fraction(M):
    a = [list(row) for row in M]
    n = len(a)
    det = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        x = a[k][k]
        det *= x
        for i in range(k + 1, n):
            r = a[i][k] / x
            for j in range(k + 1, n):
                a[i][j] -= r * a[k][j]
            a[i][k] = Fraction(0)
    return det


def tau(m, a, b):
    return (a + (m - 1) * b) * (m * b) ** (m - 1) * (2 * a + (m - 2) * b) ** (m - 1) / m


def critical(m):
    return m * (2*m-3) / ((m-2) * (2*m-1))


def optimum(m, P, Q, B):
    assert m >= 3 and P > 0 and Q > 0 and B > 0
    rho = P/Q
    if rho >= critical(m):
        t = 0.0
    else:
        q = Q/P
        A = 4*(m-1)-2*m*q
        C = (m-2)*(2*m-1)-m*(2*m-3)*q
        assert C < 0
        t = (-A + sqrt(A*A-8*C))/4
    b = B/(m*(P*t+(m-1)*Q))
    return t*b, b


def logdet_for(m, weights):
    A = np.asarray(laplacian(m, weights), dtype=float)[:-1, :-1]
    sign, value = np.linalg.slogdet(A)
    return value if sign > 0 else -1e30


def run():
    exact_checks = 0
    for m in (3, 4):
        for a, b in [(Fraction(0), Fraction(1)), (Fraction(1), Fraction(1)),
                     (Fraction(2, 3), Fraction(7, 5)), (Fraction(3), Fraction(2))]:
            ws = [a if match else b for _, _, match in edges(m)]
            got = determinant_fraction(laplacian(m, ws, exact=True)[:-1])
            expected = tau(m, a, b)
            assert got == expected, (m, a, b, got, expected)
            exact_checks += 1

    rng = np.random.default_rng(20261026)
    determinant_checks = 0
    certificate_checks = 0
    asymmetry_checks = 0
    for m in range(3, 10):
        for _ in range(25):
            a, b = rng.uniform(0, 3, size=2)
            ws = [a if match else b for _, _, match in edges(m)]
            det = np.exp(logdet_for(m, ws))
            assert np.isclose(det, tau(m, a, b), rtol=2e-8, atol=1e-7)
            determinant_checks += 1

            P, Q = np.exp(rng.uniform(-1.2, 1.2, 2))
            B = float(rng.uniform(1, 20))
            a_star, b_star = optimum(m, P, Q, B)
            assert a_star >= 0 and b_star > 0
            assert np.isclose(m*P*a_star + m*(m-1)*Q*b_star, B, rtol=1e-12)
            rho = P/Q
            assert (a_star == 0) == (rho >= critical(m))
            if a_star > 0:
                t = a_star/b_star
                q = Q/P
                polynomial = (2*t*t + (4*(m-1)-2*m*q)*t
                              +(m-2)*(2*m-1)-m*(2*m-3)*q)
                assert abs(polynomial) <= 1e-8 * (1+abs(t)**2+m*m*(1+q))
            certificate_checks += 1
            w_opt = [a_star if match else b_star for _, _, match in edges(m)]
            val_opt = logdet_for(m, w_opt)
            prices = np.array([P if match else Q for _, _, match in edges(m)])
            for _ in range(12):
                shares = rng.dirichlet(np.ones(m*m))
                weights = B*shares/prices
                assert logdet_for(m, weights) <= val_opt + 1e-8
                asymmetry_checks += 1

    local_checks = 0
    for m in [3, 4, 5]:
        for rho in [0.7, 1.0, 1.2, critical(m)*0.999, critical(m)*1.001, 2.2]:
            P, Q, B = rho, 1.0, 8.0
            a, b = optimum(m, P, Q, B)
            vals = [a if match else b for _, _, match in edges(m)]
            prices = np.array([P if match else Q for _, _, match in edges(m)])
            log_opt = logdet_for(m, vals)
            x0 = B / (len(vals) * prices)
            def objective(w):
                return -logdet_for(m, w)
            result = minimize(objective, x0, method='SLSQP',
                              bounds=[(0,None)]*len(vals),
                              constraints=[{'type':'eq','fun':lambda w: prices@w-B,
                                            'jac':lambda w: prices}],
                              options={'ftol':1e-11,'maxiter':500})
            assert result.success, (m, rho, result.message)
            assert -result.fun <= log_opt+2e-7, (m, rho, -result.fun, log_opt)
            local_checks += 1

    critical_checks = 0
    for gamma in (-1.0, 0.0, 0.3, 0.7, 1.0, 1.4):
        for m in (500, 2000, 8000):
            a,b=optimum(m, 1+gamma/m, 1, 1)
            t=a/b
            target=max(0,1-gamma)
            assert abs(t-target) < .03, (m,gamma,t,target)
            critical_checks += 1
    print('EXACT_DETERMINANTS_OK', exact_checks)
    print('DIRECT_DETERMINANTS_OK', determinant_checks)
    print('OPTIMALITY_POLYNOMIAL_AND_BUDGET_OK', certificate_checks)
    print('ASYMMETRIC_FEASIBLE_COMPARISONS_OK', asymmetry_checks)
    print('UNRESTRICTED_SLSQP_COMPARISONS_OK', local_checks)
    print('CRITICAL_WINDOW_CHECKS_OK', critical_checks)
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    run()
