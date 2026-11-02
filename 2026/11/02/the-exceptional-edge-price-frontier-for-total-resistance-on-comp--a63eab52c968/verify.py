"""Reproducibility checks for exceptional-edge resistance design on complete graphs."""
import math
import itertools
import numpy as np
import sympy as sp
from scipy.optimize import minimize


def formula(n, tau, budget):
    assert n >= 4 and tau > 0 and budget > 0
    m = n - 2
    critical = n / m
    if tau <= critical:
        c = m + 1 - m * tau / 2
        S = math.sqrt(tau / 2) + (m - 1) / math.sqrt(2) + math.sqrt(c / n)
        z = budget / S
        x = z / math.sqrt(n * c)
        w = z * (math.sqrt(2 / tau) - m / math.sqrt(n * c)) / 2
        y = z * (math.sqrt(2) - 2 / math.sqrt(n * c)) / m
        value = n * S * S / budget
    else:
        alpha = 1 / m + 1 / n
        T = math.sqrt((m + 1) * alpha) + (m - 1) / math.sqrt(2)
        z = budget / T
        w = 0.0
        x = z * math.sqrt(alpha / (m + 1))
        y = z * (math.sqrt(2) - 2 * math.sqrt(alpha / (m + 1))) / m
        value = n * T * T / budget
    return np.array([w, x, y]), value


def edges(n):
    return list(itertools.combinations(range(n), 2))


def expand(n, groups):
    w, x, y = groups
    return np.asarray([w if (i, j) == (0, 1) else x if (i <= 1 or j <= 1) else y
                       for i, j in edges(n)], dtype=float)


def laplacian(n, weights):
    L = np.zeros((n, n))
    for (i, j), g in zip(edges(n), weights):
        L[i, i] += g
        L[j, j] += g
        L[i, j] -= g
        L[j, i] -= g
    return L


def resistance(n, weights):
    eigenvalues = np.linalg.eigvalsh(laplacian(n, weights))
    if eigenvalues[1] <= 1e-12:
        return 1e30
    return float(n * np.sum(1 / eigenvalues[1:]))


def verify_one(n, tau, budget, rng):
    groups, claimed = formula(n, tau, budget)
    vector = expand(n, groups)
    prices = np.ones(len(vector))
    prices[0] = tau
    assert min(groups) >= -2e-13
    assert abs(prices @ vector - budget) < 4e-11 * max(1, budget)
    actual = resistance(n, vector)
    assert abs(actual - claimed) < 3e-10 * max(1, claimed)

    # Independent full-matrix sensitivity, including the omitted-edge KKT inequality.
    M = laplacian(n, vector) + np.ones((n, n)) / n
    inv = np.linalg.inv(M)
    marginal_benefits = []
    for (i, j) in edges(n):
        e = np.zeros(n)
        e[i], e[j] = 1, -1
        marginal_benefits.append(n * float(np.dot(inv @ e, inv @ e)))
    scaled = np.asarray(marginal_benefits) / prices
    positive = vector > 1e-10
    lam = float(np.mean(scaled[positive]))
    assert max(abs(scaled[positive] - lam)) <= 3e-9 * max(1, lam)
    assert np.all(scaled[~positive] <= lam + 3e-9 * max(1, lam))

    for _ in range(80):
        # Each edge is free to choose its own conductance; no orbit reduction here.
        trial = rng.dirichlet(np.ones(len(vector))) * budget / prices
        assert resistance(n, trial) >= claimed - 1e-8 * max(1, claimed)
    return 80


def check_exact_four_vertex_case():
    q = sp.sqrt(2)
    x = (3-q) / 7
    y = (4*q-5) / 7
    assert sp.simplify(4*x+y-1) == 0
    val = sp.simplify(4 * (1/(2*x) + 1/(2*x+2*y) + 1/(4*x)))
    assert sp.simplify(val-(11+6*q)) == 0
    assert sp.simplify(x)>0 and sp.simplify(y)>0


def check_direct_constrained_optimizations():
    checked = 0
    for n in [4, 5, 6]:
        for tau in [0.25, 1, .92*n/(n-2), 1.01*n/(n-2), 4]:
            groups, claimed = formula(n, tau, 1)
            c = np.ones(len(edges(n)))
            c[0] = tau
            initial = np.ones(len(c)) / (len(c)*c)
            out = minimize(lambda v: resistance(n, v), initial,
                           bounds=[(0, None)]*len(c),
                           constraints=[{'type':'eq','fun':lambda v,c=c:float(c@v-1)}],
                           method='SLSQP',
                           options={'ftol':1e-10,'maxiter':800})
            assert out.success, (n,tau,out.message)
            assert abs(out.fun-claimed) < 2e-6 * max(1,claimed)
            checked+=1
    return checked


def main():
    rng = np.random.default_rng(782781)
    check_exact_four_vertex_case()
    spectral_cases = 0
    random_comparisons = 0
    for n in [4,5,6,8,12]:
        critical = n/(n-2)
        for tau in [0.08,0.5,1,.75*critical,critical,1.01*critical,3*critical]:
            for budget in [0.4,1,2.2]:
                random_comparisons+=verify_one(n,tau,budget,rng)
                spectral_cases+=1
    numerical_optimizations = check_direct_constrained_optimizations()
    print('EXACT_SYMPY_EXAMPLE: passed')
    print(f'FULL_SPECTRUM_AND_KKT_CASES: {spectral_cases}')
    print(f'ASYMMETRIC_FEASIBLE_COMPARISONS: {random_comparisons}')
    print(f'FULL_CONSTRAINED_OPTIMIZATIONS: {numerical_optimizations}')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
