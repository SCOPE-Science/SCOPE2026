#!/usr/bin/env python3
"""Diagnostic checks for the ellipsoid section formula.

This script does not certify the quantified theorem.  It independently checks the
linear-algebra slice Jacobian and the odd/even transform identities on deterministic
examples.
"""
import math
import numpy as np


def kappa(m):
    return math.pi ** (m / 2) / math.gamma(m / 2 + 1)


def formula_volume(u, c, Q, r):
    n = len(u)
    s = float(u @ Q @ u)
    y = float(u @ c)
    D = float(np.linalg.det(Q))
    q = s - (r - y) ** 2
    assert q > 0
    return kappa(n - 1) * math.sqrt(D) * q ** ((n - 1) / 2) / s ** (n / 2)


def direct_affine_slice_volume(u, c, Q, r):
    # Pull H_u back by x=c+A z, then use an orthonormal basis of the slice
    # together with the Gram determinant of A restricted to that basis.
    n = len(u)
    w, U = np.linalg.eigh(Q)
    A = U @ np.diag(np.sqrt(w)) @ U.T
    a = A.T @ u
    an = np.linalg.norm(a)
    tau = (r - u @ c) / an
    assert abs(tau) < 1
    # Nullspace basis for a^T z=0 from SVD.
    _, _, VT = np.linalg.svd(a.reshape(1, -1))
    B = VT[1:].T
    G = (A @ B).T @ (A @ B)
    jac = math.sqrt(float(np.linalg.det(G)))
    return kappa(n - 1) * (1 - tau * tau) ** ((n - 1) / 2) * jac


def transformed(u, c, Q, r):
    n = len(u)
    V = formula_volume(u, c, Q, r)
    return (V / kappa(n - 1)) ** (2 / (n - 1))


def run():
    rng = np.random.default_rng(20261003)
    for n in range(3, 7):
        A = rng.normal(size=(n, n))
        Q = A @ A.T + 5.0 * np.eye(n)
        c = rng.normal(size=n) * 0.08
        r = 0.4
        for _ in range(20):
            u = rng.normal(size=n)
            u /= np.linalg.norm(u)
            v1 = formula_volume(u, c, Q, r)
            v2 = direct_affine_slice_volume(u, c, Q, r)
            if not math.isclose(v1, v2, rel_tol=3e-12, abs_tol=3e-12):
                raise AssertionError((n, v1, v2))
            s = float(u @ Q @ u)
            y = float(u @ c)
            D = float(np.linalg.det(Q))
            fplus = transformed(u, c, Q, r)
            fminus = transformed(-u, c, Q, r)
            odd = 4 * r * D ** (1 / (n - 1)) * y / s ** (n / (n - 1))
            even = D ** (1 / (n - 1)) * (s - r*r - y*y) / s ** (n / (n - 1))
            if not math.isclose(fplus - fminus, odd, rel_tol=4e-12, abs_tol=4e-12):
                raise AssertionError('odd')
            if not math.isclose((fplus + fminus)/2, even, rel_tol=4e-12, abs_tol=4e-12):
                raise AssertionError('even')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
