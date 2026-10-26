"""Direct finite checks for geometric resetting on transitive networks.

Requirements: Python 3, numpy, scipy, sympy.
Run: python verify.py
Tests support, but do not replace, the analytic proof.
"""
import numpy as np
from scipy.optimize import brentq
import sympy as sp


def cycle(n):
    p = np.zeros((n, n))
    for i in range(n):
        p[i, (i - 1) % n] = 0.5
        p[i, (i + 1) % n] = 0.5
    return p


def complete(n):
    return (np.ones((n, n)) - np.eye(n)) / (n - 1)


def hypercube(dim):
    n = 2**dim
    p = np.zeros((n, n))
    for i in range(n):
        for bit in range(dim):
            p[i, i ^ (1 << bit)] = 1 / dim
    return p


def exact_backward_means(p, rho, gamma):
    n = len(rho)
    trans = (1 - gamma) * p + gamma * np.outer(np.ones(n), rho)
    vals = []
    for j in range(n):
        outside = [k for k in range(n) if k != j]
        sub = np.ix_(outside, outside)
        h = np.linalg.solve(np.eye(n - 1) - trans[sub], np.ones(n - 1))
        vals.append(float(np.dot(rho[outside], h)))
    return np.array(vals)


def verify_finite():
    for p in [cycle(n) for n in (3, 4, 5, 6, 8, 10)] + [complete(6), hypercube(3)]:
        n = p.shape[0]
        for gamma in (0.07, 0.29, 0.75, 0.96):
            z = 1 - gamma
            q = np.linalg.inv(np.eye(n) - z * p)
            c = q[0, 0]
            u = np.full(n, 1 / n)
            rho_options = (
                u, np.arange(1, n + 1, dtype=float) / (n * (n + 1) / 2),
                np.eye(n)[0],
            )
            for rho in rho_options:
                r = rho @ q
                from_green = (c / r - 1) / gamma
                backward = exact_backward_means(p, rho, gamma)
                assert np.allclose(from_green, backward, rtol=2e-7, atol=2e-7)
                regret = backward.mean() - (n * c - 1 / gamma)
                claimed = c * gamma * n * np.sum((r - 1 / (n * gamma))**2 / r)
                assert np.isclose(regret, claimed, rtol=3e-7, atol=1e-7)
                assert regret > -1e-7
                if not np.allclose(rho, u):
                    assert regret > 1e-9
                    assert backward.max() > n * c - 1 / gamma


def verify_cycle_thresholds():
    for n in range(3, 34):
        lam = np.cos(2 * np.pi * np.arange(1, n) / n)
        derivative = lambda z: sum(lam / (1 - z * lam)**2)
        exact_edge = (n*n - 1) * (n*n - 19) / 180
        assert np.isclose(derivative(1), exact_edge, rtol=5e-9, atol=5e-9)
        root = brentq(derivative, 0, 1) if n >= 5 else 1
        assert (root < 1) == (n >= 5)
        if n >= 5:
            assert derivative(root) < 1e-8
            assert abs(derivative(root)) < 1e-8
    z = sp.symbols('z', real=True)
    a = (sp.sqrt(5) - 1) / 4
    b = -(sp.sqrt(5) + 1) / 4
    f = 2 / (1-a*z) + 2 / (1-b*z)
    zstar = 2*sp.sqrt(5) - 4
    assert sp.simplify(sp.diff(f, z).subs(z, zstar)) == 0
    assert sp.simplify(f.subs(z, zstar) - (2 + 4 / sp.sqrt(5))) == 0


def verify_large_cycles():
    for n in (30, 60, 120, 240, 480):
        lam = np.cos(2*np.pi*np.arange(1, n)/n)
        derivative = lambda z: np.sum(lam/(1-z*lam)**2)
        zstar = brentq(derivative, 0, 2/n)
        loss = n-1-np.sum(1/(1-zstar*lam))
        assert 0.8 < n*zstar < 1.1
        assert 0.8 < 2*n*loss < 1.2


if __name__ == '__main__':
    verify_finite()
    verify_cycle_thresholds()
    verify_large_cycles()
    print('PASS: backward equations, resolvent identity, regret, sharp cycle threshold, radicals and large-cycle checks')
