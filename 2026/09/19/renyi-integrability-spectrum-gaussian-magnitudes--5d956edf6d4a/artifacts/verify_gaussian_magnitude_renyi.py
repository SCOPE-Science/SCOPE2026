import itertools
import math
import numpy as np


def sign_group(n):
    for tail in itertools.product((-1.0, 1.0), repeat=max(0, n - 1)):
        yield np.diag((1.0,) + tail)


def j_integer(R, m):
    R = np.asarray(R, dtype=float)
    n = R.shape[0]
    inv = np.linalg.inv(R)
    det_r = np.linalg.det(R)
    group = list(sign_group(n))
    total = 0.0
    for rel in itertools.product(group, repeat=m - 1):
        B = inv.copy()
        for S in rel:
            B = B + S @ inv @ S
        B = B - (m - 1) * np.eye(n)
        eig = np.linalg.eigvalsh(B)
        if eig[0] <= 0.0:
            return math.inf
        total += np.linalg.det(B) ** (-0.5)
    return (len(group) ** (1 - m)) * (det_r ** (-m / 2.0)) * total


def d_integer(R, m):
    J = j_integer(R, m)
    return math.inf if math.isinf(J) else math.log(J) / (m - 1)


def equicorr(n, rho):
    R = np.full((n, n), rho, dtype=float)
    np.fill_diagonal(R, 1.0)
    return R


def check_bivariate_order_two():
    print('Bivariate D2 identity')
    for rho in (0.1, 0.4, 0.8):
        R = np.array([[1.0, rho], [rho, 1.0]])
        J = j_integer(R, 2)
        target = 1.0 / (1.0 - rho**4)
        print(f'rho={rho:.1f} J2={J:.15f} target={target:.15f} error={J-target:+.3e}')


def check_integrability_thresholds():
    print('\nInteger-order finiteness thresholds')
    for n, rho, m in ((3, 0.40, 2), (3, 0.40, 3), (3, 0.20, 3), (3, 0.20, 4)):
        R = equicorr(n, rho)
        lam = np.linalg.eigvalsh(R)[-1]
        critical = m / (m - 1)
        J = j_integer(R, m)
        state = 'finite' if math.isfinite(J) else 'infinite'
        print(f'n={n} rho={rho:.2f} m={m} lambda_max={lam:.12f} threshold={critical:.12f} -> {state}')


def check_weak_dependence():
    print('\nWeak-dependence coefficients')
    A = np.array([[0.0, 0.4, -0.3], [0.4, 0.0, 0.2], [-0.3, 0.2, 0.0]])
    pair = sum(A[i, j] ** 4 for i in range(3) for j in range(i + 1, 3))
    tri = 8.0 * (A[0, 1] * A[0, 2] * A[1, 2]) ** 2
    print(f'pair coefficient={pair:.15f}')
    print(f'triangle coefficient={tri:.15f}')
    for eps in (0.12, 0.08, 0.05, 0.03):
        R = np.eye(3) + eps * A
        D2 = d_integer(R, 2)
        fourth = D2 / eps**4
        sixth = (D2 - pair * eps**4) / eps**6
        print(f'eps={eps:.2f} D2/eps^4={fourth:.12f} sixth_residual={sixth:.12f}')


def check_pair_triangle_lower_bound():
    print('\nPair-triangle lower bound')
    R = np.array([[1.0, 0.30, -0.20], [0.30, 1.0, 0.25], [-0.20, 0.25, 1.0]])
    J = j_integer(R, 2)
    pair = sum(R[i, j] ** 4 for i in range(3) for j in range(i + 1, 3))
    tri = 8.0 * (R[0, 1] * R[0, 2] * R[1, 2]) ** 2
    print(f'chi2_exact={J-1.0:.15f}')
    print(f'pair_plus_triangle={pair+tri:.15f}')
    print(f'margin={(J-1.0)-(pair+tri):.15f}')


if __name__ == '__main__':
    print('NumPy', np.__version__)
    check_bivariate_order_two()
    check_integrability_thresholds()
    check_weak_dependence()
    check_pair_triangle_lower_bound()
