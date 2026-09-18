import math
import sys
import numpy as np


def exact_model(rho):
    # H=[[3,1],[1,1]], A=[1,0]; constrained minimum is lambda_*=1.
    return 0.5 * (rho + 4.0 - math.sqrt((rho + 2.0)**2 + 4.0))


def exact_model_derivative(rho):
    return 0.5 * (1.0 - (rho + 2.0) / math.sqrt((rho + 2.0)**2 + 4.0))


def hermite_two_level(rho):
    f1 = exact_model(rho)
    d1 = exact_model_derivative(rho)
    f2 = exact_model(2.0 * rho)
    d2 = exact_model_derivative(2.0 * rho)
    return 5.0*f1 + rho*d1 - 4.0*f2 + 8.0*rho*d2


def richardson_two_level(rho):
    return 2.0*exact_model(2.0*rho) - exact_model(rho)


def richardson_three_level(rho):
    return exact_model(rho)/3.0 - 2.0*exact_model(2.0*rho) + 8.0*exact_model(4.0*rho)/3.0


def second_coefficient_check(seed=3):
    rng = np.random.default_rng(seed)
    n, m = 6, 2
    M = rng.standard_normal((n, n))
    H = 0.5 * (M + M.T)
    A = rng.standard_normal((m, n))
    # SVD supplies orthonormal bases U for range(A^T) and Z for null(A).
    _, _, vt = np.linalg.svd(A, full_matrices=True)
    Z = vt[m:].T
    U = vt[:m].T
    B = U.T @ H @ U
    E = U.T @ H @ Z
    D = Z.T @ H @ Z
    C = U.T @ A.T @ A @ U
    vals, vecs = np.linalg.eigh(D)
    lam = vals[0]
    v = vecs[:, 0]
    G = E.T @ np.linalg.solve(C, E)
    J = E.T @ np.linalg.solve(C, (B - lam*np.eye(m)) @ np.linalg.solve(C, E))
    # S=(D-lambda I)^dagger from the eigendecomposition.
    S = vecs[:, 1:] @ np.diag(1.0/(vals[1:] - lam)) @ vecs[:, 1:].T
    c = float(v @ G @ v)
    b = float(v @ (J - G @ S @ G) @ v)

    scaled = []
    for rho in (100.0, 200.0, 400.0, 800.0):
        F = H + rho * (A.T @ A)
        f = np.linalg.eigvalsh(F)[0]
        scaled.append((rho, (f - (lam - c/rho + b/rho**2))*rho**3))
    return lam, c, b, scaled


if __name__ == '__main__':
    print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}; NumPy {np.__version__}')
    print('2x2 model: H=[[3,1],[1,1]], A=[1,0], lambda_*=1')
    print('rho    rho*(1-f)    rho^2*(1-R2)    rho^3*(1-R3)    rho^4*(1-H4)')
    for rho in (20.0, 40.0, 80.0, 160.0, 320.0):
        f = exact_model(rho)
        r2 = richardson_two_level(rho)
        r3 = richardson_three_level(rho)
        h4 = hermite_two_level(rho)
        print(f'{rho:5.0f}  {rho*(1-f):.12f}  {rho**2*(1-r2):.12f}  '
              f'{rho**3*(1-r3):.12f}  {rho**4*(1-h4):.12f}')
    print('Expected limits: 1, 1, 3/8, 1/2')
    lam, c, b, scaled = second_coefficient_check()
    print('\nRandom symmetric 6x6 / two-constraint check (seed=3)')
    print(f'lambda_* = {lam:.15g}')
    print(f'c        = {c:.15g}')
    print(f'b        = {b:.15g}')
    print('rho    rho^3 * [f(rho)-(lambda_*-c/rho+b/rho^2)]')
    for rho, val in scaled:
        print(f'{rho:5.0f}  {val:.12f}')
