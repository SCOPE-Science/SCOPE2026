import numpy as np


def aca_step(A, i, j):
    a = A[i, j]
    return A - np.outer(A[:, j], A[i, :]) / a


def extremal_family(n, alpha):
    s = n - 1
    B = 1.0 + 2.0 * s * alpha**2
    beta = B / (s**2 * alpha**2)
    A = np.empty((n, n), dtype=float)
    A[0, 0] = 1.0
    A[0, 1:] = alpha
    A[1:, 0] = alpha
    A[1:, 1:] = -beta
    return A, beta


def frob_ratio(A, E):
    return np.linalg.norm(E, 'fro') / np.linalg.norm(A, 'fro')


def change_identity(A, i, j):
    a = A[i, j]
    c = A[:, j]
    r = A[i, :]
    E = aca_step(A, i, j)
    lhs = np.linalg.norm(E, 'fro')**2 - np.linalg.norm(A, 'fro')**2
    rhs = (np.dot(c, c) * np.dot(r, r) - 2.0 * a * (c @ A @ r)) / (a * a)
    return lhs, rhs


def main():
    print(f'numpy_version={np.__version__}')
    print('extremal_family')
    for n in (4, 5, 10, 100):
        alpha = 0.999999
        A, beta = extremal_family(n, alpha)
        E = aca_step(A, 0, 0)
        ratio = frob_ratio(A, E)
        bound = n / np.sqrt(2.0 * n - 1.0)
        unique = np.count_nonzero(np.isclose(np.abs(A), 1.0, rtol=0.0, atol=1e-14)) == 1
        print(f'n={n:3d} beta={beta:.12f} unique_pivot={unique} ratio={ratio:.12f} bound={bound:.12f} gap={bound-ratio:.3e}')

    print('exact_change_identity')
    rng = np.random.default_rng(20260919)
    max_identity_error = 0.0
    max_bound_violation = -np.inf
    for n, m in ((4, 7), (7, 4), (8, 9)):
        bound = np.sqrt(n * m / (n + m - 1.0))
        for _ in range(500):
            A = rng.uniform(-1.0, 1.0, size=(n, m))
            i, j = np.unravel_index(np.argmax(np.abs(A)), A.shape)
            E = aca_step(A, i, j)
            lhs, rhs = change_identity(A, i, j)
            max_identity_error = max(max_identity_error, abs(lhs - rhs))
            max_bound_violation = max(max_bound_violation, frob_ratio(A, E) - bound)
    print(f'max_identity_error={max_identity_error:.3e}')
    print(f'max_random_bound_violation={max_bound_violation:.3e}')

    print('psd_diagonal_pivots')
    max_psd_ratio = 0.0
    for n in (5, 10):
        for _ in range(100):
            G = rng.normal(size=(n, n + 2))
            A = G @ G.T
            i = int(np.argmax(np.diag(A)))
            E = aca_step(A, i, i)
            max_psd_ratio = max(max_psd_ratio, frob_ratio(A, E))
            if np.linalg.eigvalsh((E + E.T) / 2.0).min() < -1e-10:
                raise AssertionError('PSD residual check failed')
    print(f'max_psd_ratio={max_psd_ratio:.12f}')


if __name__ == '__main__':
    main()
