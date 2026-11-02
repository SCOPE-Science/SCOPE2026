"""Supplementary numerical checks for a qubit–qudit correlation projection."""
import math
import numpy as np


def project(X, n):
    X = np.asarray(X)
    Y = X.reshape((2, n, 2, n))
    marginal_a = np.trace(Y, axis1=1, axis2=3)
    marginal_b = np.trace(Y, axis1=0, axis2=2)
    return (X - np.kron(marginal_a, np.eye(n) / n)
            - np.kron(np.eye(2) / 2, marginal_b)
            + np.trace(X) * np.eye(2 * n) / (2 * n))


def norm1_herm(X):
    return float(np.abs(np.linalg.eigvalsh(X)).sum())


def constants(n):
    c = (n - 2) / n
    b = 1 - c * c / 4
    u = c / math.sqrt(b * (b + c * c))
    best = 0.5 + math.sqrt((4 + 3 * c * c) / (4 - c * c))
    return c, b, u, best


def schmidt(n, u):
    v = np.zeros(2 * n, dtype=complex)
    v[0] = math.sqrt((1 + u) / 2)
    v[n + 1] = math.sqrt((1 - u) / 2)
    return v


def main():
    rng = np.random.default_rng(704211)
    count = 0
    for n in range(2, 14):
        c, b, u_star, best = constants(n)
        assert 0 <= u_star < 1
        assert best > 1 + c
        count += 2
        for u in sorted(set([0.0, u_star, 1.0] + [j / 19 for j in range(20)])):
            v = schmidt(n, u)
            out = project(np.outer(v, v.conj()), n)
            actual = norm1_herm(out)
            predicted = 0.5 + c * u + max(0.5, math.sqrt(1 - b * u * u))
            assert abs(actual - predicted) < 1e-11, (n, u, actual, predicted)
            assert actual < best + 1e-11
            count += 2
        assert abs(norm1_herm(project(np.outer(schmidt(n, u_star), schmidt(n, u_star).conj()), n)) - best) < 1e-11
        count += 1
        for _ in range(20):
            v = rng.normal(size=2 * n) + 1j * rng.normal(size=2 * n)
            v /= np.linalg.norm(v)
            assert norm1_herm(project(np.outer(v, v.conj()), n)) < best + 1e-11
            count += 1
        for _ in range(10):
            v = rng.normal(size=2) + 1j * rng.normal(size=2)
            w = rng.normal(size=n) + 1j * rng.normal(size=n)
            v /= np.linalg.norm(v)
            w /= np.linalg.norm(w)
            q = np.kron(v, w)
            assert abs(norm1_herm(project(np.outer(q, q.conj()), n)) - (1 + c)) < 1e-11
            count += 1
        for _ in range(5):
            R = rng.normal(size=(2 * n, 2 * n)) + 1j * rng.normal(size=(2 * n, 2 * n))
            H = (R + R.conj().T) / 2
            S = rng.normal(size=(2 * n, 2 * n)) + 1j * rng.normal(size=(2 * n, 2 * n))
            K = (S + S.conj().T) / 2
            assert abs(np.trace(H @ project(K, n)) - np.trace(project(H, n) @ K)) < 1e-9
            count += 1
    print('CHECKER_OK', count, 'finite supplementary assertions')


if __name__ == '__main__':
    main()
