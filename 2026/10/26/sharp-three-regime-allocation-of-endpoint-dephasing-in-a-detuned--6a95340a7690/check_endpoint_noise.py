#!/usr/bin/env python3
"""Reproduce the exact three-site source/trap dephasing-allocation theorem.

Dependencies: Python 3.10+, NumPy, SciPy, SymPy. Run: python check_endpoint_noise.py
The tests compare the stated closed form against a separately constructed
complex nine-dimensional Lindblad superoperator; they do not prove the theorem.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar, brentq


def exact_mean(kappa, budget, detuning, allocation):
    x = budget + kappa
    q = 4.0 + allocation * (x - allocation)
    return 3.0 / kappa + (2.0 * x - allocation) / 4.0 + (detuning**2) * (x + allocation) / q


def derivative(kappa, budget, detuning, allocation):
    x = budget + kappa
    u = allocation
    q = 4.0 + u * (x-u)
    return -0.25 + (detuning**2) * (u*u + 2*x*u + 4-x*x) / (q*q)


def convex_second(kappa, budget, detuning, allocation):
    x = budget + kappa
    u = allocation
    q = 4.0 + u * (x-u)
    return (2 * detuning**2 * ((x-u)**3 + 2*u**3 + 12*u)) / q**3


def optimum(kappa, budget, detuning):
    a = derivative(kappa, budget, detuning, 0.0)
    b = derivative(kappa, budget, detuning, budget)
    if a >= 0.0:
        return 0.0
    if b <= 0.0:
        return budget
    return brentq(lambda u: derivative(kappa, budget, detuning, u),
                  0.0, budget, xtol=1e-13)


def direct_lindblad_mean(kappa, budget, detuning, allocation):
    H = np.array([[0, 1, 0], [1, detuning, 1], [0, 1, 0]], dtype=complex)
    proj = [np.diag([1.0 if i == j else 0.0 for i in range(3)])
            for j in range(3)]
    rate = [allocation, 0.0, budget-allocation]
    P = proj[2]
    A = np.zeros((9,9), dtype=complex)
    for col in range(9):
        E = np.zeros((3,3), dtype=complex)
        i, j = col % 3, col // 3
        E[i,j] = 1.0
        LE = -1j*(H@E-E@H) - 0.5*kappa*(P@E+E@P)
        for r, Pr in zip(rate, proj):
            LE += r*(Pr@E@Pr - 0.5*(Pr@E+E@Pr))
        A[:, col] = LE.reshape(-1,order='F')
    rho0 = np.zeros((3,3),dtype=complex)
    rho0[0,0] = 1
    X = np.linalg.solve(-A, rho0.reshape(-1,order='F')).reshape(3,3,order='F')
    assert np.linalg.norm(X-X.conj().T) < 1.e-9*(1+np.linalg.norm(X))
    return np.trace(X).real


def symbolic_check():
    """Exact algebraic residual for the nine integrated-density equations."""
    import sympy as sp
    K, G, D, U = sp.symbols('K G D U', positive=True, real=True)
    x = G + K
    v = x - U
    Q = 4 + U*v
    f = -2*D/Q
    a = v*f/2
    c = -U*f/2
    b = d = sp.Rational(1,2)
    e = sp.Integer(0)
    p3 = 1/K
    p2 = p3 + v/4 + D**2*U/Q
    p1 = p2 + U/4 + D**2*v/Q
    # In integrated order: p1,p2,p3,Re(X12),Im(X12),Re(X23),
    # Im(X23),Re(X13),Im(X13).
    lhs = [
        -2*b,
        2*b-2*d,
        2*d-K*p3,
        -D*b-U*a/2-f,
        D*a-U*b/2+e+p1-p2,
        D*d-v*c/2+f,
        -D*c-v*d/2-e+p2-p3,
        -x*e/2-b+d,
        -x*f/2+a-c,
    ]
    assert all(sp.cancel(y-z) == 0 for y,z in
               zip(lhs,[-1,0,0,0,0,0,0,0,0]))
    T = sp.factor(p1+p2+p3)
    target = 3/K+(2*x-U)/4 + D**2*(x+U)/Q
    assert sp.cancel(T-target)==0
    F = (x+U)/Q
    sec = 2*((x-U)**3+2*U**3+12*U)/Q**3
    assert sp.cancel(sp.diff(F,U,2)-sec)==0
    return 11


def run():
    algebra = symbolic_check()
    rng = np.random.default_rng(20261024)
    lindblad = 0
    for _ in range(900):
        kappa = 10**rng.uniform(-0.7, 0.9)
        budget = 10**rng.uniform(-0.7, 0.9)
        detuning = rng.uniform(0,6)
        allocation = budget*rng.uniform()
        direct = direct_lindblad_mean(kappa,budget,detuning,allocation)
        exact = exact_mean(kappa,budget,detuning,allocation)
        assert abs(direct-exact) < 3e-10*(1+abs(direct)), (kappa,budget,detuning,allocation,direct,exact)
        lindblad += 1
    convexity = 0
    for _ in range(1200):
        kappa = 10**rng.uniform(-1,1)
        budget = 10**rng.uniform(-1,1)
        detuning = 10**rng.uniform(-1,1)
        allocation = rng.uniform()*budget
        assert convex_second(kappa,budget,detuning,allocation) > 0
        step = 1e-5*min(1,budget)
        approx = (derivative(kappa,budget,detuning,allocation+step)-derivative(kappa,budget,detuning,allocation-step))/(2*step)
        assert abs(approx-convex_second(kappa,budget,detuning,allocation)) < 3e-7*(1+abs(approx))
        convexity += 1
    optimality = 0
    for _ in range(650):
        kappa = 10**rng.uniform(-0.8,1.2)
        budget = 10**rng.uniform(-0.8,1.2)
        detuning = 10**rng.uniform(-1,1)
        u = optimum(kappa,budget,detuning)
        vals = [exact_mean(kappa,budget,detuning,z) for z in np.linspace(0,budget,301)]
        assert exact_mean(kappa,budget,detuning,u) <= min(vals) + 1e-9
        if 1e-8 < u < budget-1e-8: assert abs(derivative(kappa,budget,detuning,u)) < 1e-8
        optimality += 1
    kappa,budget = .5,1.0
    assert abs(optimum(kappa,budget,.5)-budget)<1e-14
    assert 0.0 < optimum(kappa,budget,1.2) < budget
    assert optimum(kappa,budget,2.0) == 0.0
    print('PASS:', algebra, 'exact symbolic identities;', lindblad, 'independent Lindblad solves;', convexity,
          'strict-convexity/derivative tests;', optimality,
          'global optimizer tests; three parameter regimes.')
    print('Illustration: kappa=0.5, budget=1, detuning 0.5/1.2/2.0:',
          [round(optimum(.5,1,d),12) for d in (.5,1.2,2.0)])

if __name__ == '__main__':
    run()
