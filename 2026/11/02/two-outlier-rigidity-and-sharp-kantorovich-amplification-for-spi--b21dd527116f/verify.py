#!/usr/bin/env python3
"""Finite numerical cross-checks for the rank-one spiked endpoint spectral law.

This is not a proof of the infinite-dimensional or extremal statements.
"""
import math
import numpy as np

rng = np.random.default_rng(20261028)
checks = 0
max_err = 0.0

def check(a, b, tolerance=8e-9):
    global checks, max_err
    if isinstance(a, (bool, np.bool_)) or isinstance(b, (bool, np.bool_)):
        assert bool(a) == bool(b), (a, b)
        checks += 1
        return
    err = float(abs(a - b))
    max_err = max(err, max_err)
    assert err <= tolerance * max(1.0, abs(a), abs(b)), (a, b, err)
    checks += 1

for n in range(2, 9):
    for repeat in range(128):
        values = np.sort(rng.uniform(0.3, 11, n))
        m, M = float(values[0]), float(values[-1])
        U0 = rng.normal(size=n) + 1j*rng.normal(size=n)
        u = U0 / np.linalg.norm(U0)
        alpha, beta = sorted(rng.uniform(0.2, 4, 2), reverse=True)
        A = np.diag(values)
        H = np.diag(1 / np.sqrt(values))
        P = np.outer(u, u.conj())
        Z = beta*np.eye(n) + (alpha-beta)*P
        D = H @ Z @ A @ Z @ H
        D = (D+D.conj().T)/2
        k = float((np.vdot(u, A @ u)*np.vdot(u, np.linalg.solve(A,u))).real)
        T = alpha**2 + beta**2 + (alpha-beta)**2*(k-1)
        roots = sorted([(T+math.sqrt(max(0,T*T-4*alpha**2*beta**2)))/2,
                        (T-math.sqrt(max(0,T*T-4*alpha**2*beta**2)))/2])
        # The subtractive lower-root expression can lose precision; use product.
        roots[0] = alpha**2*beta**2/roots[1]
        expected = np.array([roots[0]]+[beta**2]*(n-2)+[roots[1]])
        observed = np.linalg.eigvalsh(D)
        for x,y in zip(expected, observed):
            check(x,y)
        check(roots[0]*roots[1],alpha**2*beta**2)
        check(k <= (M+m)**2/(4*M*m)+1e-12,True)
        check(k >= 1-1e-12, True)
        check(np.linalg.matrix_rank(D-beta**2*np.eye(n), tol=1e-8)<=2,True)

# Exact spectral endpoint witness: equal weight on two extreme eigenvectors.
for m,M in [(1.,2.),(1.,7.),(.3,10.),(2.,11.)]:
    alpha,beta=3.,1.
    A=np.diag([m,(m+M)/2,M])
    u=np.array([2**-0.5,0,2**-0.5])
    k=float(np.vdot(u,A@u)*np.vdot(u,np.linalg.solve(A,u)))
    check(k,(m+M)**2/(4*m*M))
    Z=beta*np.eye(3)+(alpha-beta)*np.outer(u,u)
    H=np.diag(1/np.sqrt(np.diag(A)))
    obs=np.linalg.eigvalsh(H@Z@A@Z@H)
    check(obs[1],beta**2)
    check(obs[0]*obs[2],alpha**2*beta**2)

print(f'PASS: {checks} deterministic finite assertions, maximum absolute residual {max_err:.3g}')
