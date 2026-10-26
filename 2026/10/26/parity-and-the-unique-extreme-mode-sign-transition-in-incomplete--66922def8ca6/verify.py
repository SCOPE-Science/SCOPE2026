"""Numerical checks for the exact-arithmetic extreme-mode Lanczos theorem.

Requires numpy and scipy. The theorem is established analytically in RESULT.md.
"""
import numpy as np
from scipy.optimize import brentq


def check_case(n):
    lam = np.arange(1, n + 1, dtype=float) ** 1.15
    b = 1 + .17 * np.arange(n)
    for m in range(1, n):
        cols = []
        v = b / np.linalg.norm(b)
        for j in range(m):
            for q in cols:
                v -= np.dot(q, v) * q
            v /= np.linalg.norm(v)
            cols.append(v)
            v = lam * v
        V = np.array(cols).T
        T = V.T @ (lam[:, None] * V)
        th = np.linalg.eigvalsh(T)
        assert th[-1] < lam[-1] - 1e-8
        ell = np.array([
            np.prod([(lam[-1] - th[k]) / (th[j] - th[k])
                     for k in range(m) if k != j])
            for j in range(m)
        ])
        assert np.sign(ell[0]) == (1 if m % 2 else -1)

        def scaled_p(t):
            return np.dot(ell, np.exp(-t * (th - th[0])))

        assert abs(scaled_p(0.) - 1.) < 1e-7
        if m % 2:
            assert all(scaled_p(t) > 0 for t in np.linspace(.02, 40, 240))
        else:
            root = brentq(scaled_p, 0., 60., xtol=1e-12)
            assert scaled_p(root * .8) > 0
            assert scaled_p(root * 1.2) < 0
            assert scaled_p(60.) < 0

    return n - 1


if __name__ == '__main__':
    count = sum(check_case(n) for n in (5, 6, 8))
    print('VERIFY_OK', count)
