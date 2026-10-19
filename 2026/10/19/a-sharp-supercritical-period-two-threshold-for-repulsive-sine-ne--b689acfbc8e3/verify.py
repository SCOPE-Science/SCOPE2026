#!/usr/bin/env python3
"""Independent finite examples for a weighted-graph sinusoidal flip theorem.
Requires NumPy >= 1.24; run `python verify_huygens_flip.py`.
The checks are numerical and do not replace the universal analytic proof.
"""
import math
import numpy as np


def example_graphs():
    return {
        'edge': (2, [(0, 1, 1.4)]),
        'weighted_path_5': (5, [(0, 1, 0.7), (1, 2, 1.2), (2, 3, 1.8), (3, 4, 0.9)]),
        'weighted_star_5': (6, [(0, j, w) for j, w in enumerate((0.8, 1.0, 1.5, 0.6, 1.2), 1)]),
        'even_cycle_6': (6, [(i, (i+1)%6, 0.6 + 0.15*i) for i in range(6)]),
        'complete_bipartite_2_3': (5, [(i, j, 0.5 + 0.12*(i+j)) for i in range(2) for j in range(2, 5)]),
        'complete_bipartite_3_3': (6, [(i, j, 0.5 + 0.09*(i+2*j)) for i in range(3) for j in range(3, 6)]),
        'weighted_path_9': (9, [(i, i+1, 0.7 + 0.1*(i%4)) for i in range(8)]),
    }


def compute(n, edge_list):
    B = np.zeros((n, len(edge_list)))
    a = np.empty(len(edge_list))
    for k, (i, j, w) in enumerate(edge_list):
        B[i, k] = 1.
        B[j, k] = -1.
        a[k] = w
    L = (B*a) @ B.T
    vals, vecs = np.linalg.eigh(L)
    assert abs(vals[0]) < 1e-12
    lam, v = vals[-1], vecs[:, -1]
    if v[0] < 0:
        v = -v
    assert lam-vals[-2] > 1e-8 and vals[1] > 1e-8
    q4 = np.dot(a, (B.T@v)**4)
    assert q4 > 0
    # Orthonormal basis for the sum-zero quotient.
    U = vecs[:, 1:]
    return B, a, L, lam, v, q4, U


def map_and_jac(x, h, B, a):
    d = B.T @ x
    y = x - h* (B @ (a*np.sin(d)))
    jac = np.eye(len(x)) - h*(B*(a*np.cos(d)))@B.T
    return y, jac


def newton_flip(mu, B, a, lam, v, q4, U):
    h = (2+mu)/lam
    guess = math.sqrt(3*lam*mu/q4)*v
    z = U.T @ guess
    for _ in range(30):
        x = U@z
        fx, Df = map_and_jac(x, h, B, a)
        g = U.T@(fx+x)
        if np.linalg.norm(g) < 1e-12:
            break
        step = np.linalg.solve(U.T @ (Df+np.eye(len(x))) @ U, g)
        z -= step
        if np.linalg.norm(step) < 1e-13:
            break
    x = U@z
    fx, Df = map_and_jac(x, h, B, a)
    assert np.linalg.norm(fx+x) < 2e-11
    assert np.linalg.norm(x) > 1e-4
    eigs = np.linalg.eigvalsh(U.T@Df@U)
    assert max(abs(eigs)) < 1-1e-6, (mu, eigs)
    ecrit = eigs[0]
    assert abs(ecrit-(-1+2*mu)) < 14*mu**2, (mu, ecrit)
    leading = math.sqrt(3*lam*mu/q4)
    assert abs((x@v)/leading - 1) < 3*mu
    assert np.linalg.norm(x-np.dot(x,v)*v) < 10.0*mu**1.5
    return x, eigs


def potential(x, B, a):
    return -float(np.dot(a, np.cos(B.T@x)))


def run():
    examples = example_graphs()
    rng = np.random.default_rng(20261011)
    assertions = 0
    for name,(n,edges) in examples.items():
        B,a,L,lam,v,q4,U = compute(n,edges)
        assertions += 3
        # Exact Hessian and (nonlinear) critical supercritical branch.
        for mu in (0.002, 0.005, 0.01, 0.02):
            x, eigs = newton_flip(mu, B,a,lam,v,q4,U)
            assertions += 6
        # Descent at the threshold, though a finite sample alone does not prove it.
        h0 = 2/lam
        for i in range(500):
            x = rng.uniform(-math.pi, math.pi, n)
            y,_ = map_and_jac(x,h0,B,a)
            if np.linalg.norm(B@(a*np.sin(B.T@x))) > 1e-6:
                assert potential(y,B,a) < potential(x,B,a) + 1e-12
                assertions += 1
        print(f'{name}: n={n}, edges={len(edges)}, lambda={lam:.8f}, Q4={q4:.8f}, verified')
    print(f'VERIFY_OK: {len(examples)} connected positive-weight bipartite graphs, {assertions} checks')

if __name__ == '__main__':
    run()
