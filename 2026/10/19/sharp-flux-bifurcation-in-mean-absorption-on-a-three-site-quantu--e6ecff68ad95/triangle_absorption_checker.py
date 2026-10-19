"""Standalone symbolic and numerical checks for a chiral three-site absorbing walk.

Requirements: Python 3, SymPy, NumPy, SciPy.
Run: python triangle_absorption_checker.py
"""
from __future__ import annotations

import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.optimize import minimize_scalar

checks = 0

def require(ok, message):
    global checks
    assert ok, message
    checks += 1

k, c, s = sp.symbols('k c s', real=True, nonzero=True)
I = sp.I
H = sp.Matrix([[0,1,1], [1,0,c+I*s], [1,c-I*s,0]])
P = sp.diag(1,0,0)
A = -I*H-k*P/2
X = sp.Matrix([
    [1/k, c/(4*s)-I/4, -c/(4*s)-I/4],
    [c/(4*s)+I/4, 1/k+k/(8*s**2), -k*c**2/(8*s**2)-1/(4*s)-I*k*c/(8*s)],
    [-c/(4*s)+I/4, -k*c**2/(8*s**2)-1/(4*s)+I*k*c/(8*s), 1/k+k/(8*s**2)+1/(2*s)],
])
R = A*X + X*A.conjugate().T + sp.diag(0,1,0)
for i in range(3):
    for j in range(3):
        polynomial = sp.together(R[i,j] * 8*s**2).expand()
        # Evaluate on the unit circle by reducing powers of c modulo c*c+s*s-1.
        num = sp.Poly(sp.factor(polynomial), c, s)
        q, rem = sp.div(num, sp.Poly(c*c+s*s-1, c,s))
        require(rem.is_zero, f'Lyapunov equation failed at ({i},{j}): {rem}')
require(sp.simplify(sum(X[i,i] for i in range(3)) - (3/k+1/(2*s)+k/(4*s*s))) == 0,
        'trace formula')

rng = np.random.default_rng(314159265)

def model(kappa, phi):
    hh = np.array([[0,1,1], [1,0,np.exp(1j*phi)],
                   [1,np.exp(-1j*phi),0]], dtype=np.complex128)
    aa = -1j*hh - 0.5*kappa*np.diag([1.,0.,0.])
    return aa

def formula(kappa, phi):
    sn = math.sin(phi)
    return 3/kappa + 1/(2*sn) + kappa/(4*sn*sn)

def exact_integral_matrix(kappa, phi):
    sn = math.sin(phi)
    cs = math.cos(phi)
    return np.array([
      [1/kappa, cs/(4*sn)-0.25j, -cs/(4*sn)-0.25j],
      [cs/(4*sn)+0.25j, 1/kappa+kappa/(8*sn*sn),
       -kappa*cs*cs/(8*sn*sn)-1/(4*sn)-1j*kappa*cs/(8*sn)],
      [-cs/(4*sn)+0.25j, -kappa*cs*cs/(8*sn*sn)-1/(4*sn)+1j*kappa*cs/(8*sn),
       1/kappa+kappa/(8*sn*sn)+1/(2*sn)]],dtype=complex)

rho = np.diag([0.,1.,0.])
for _ in range(110):
    kappa = float(np.exp(rng.uniform(-2,2)))
    phi = float(rng.uniform(-math.pi,math.pi))
    if abs(math.sin(phi))<0.12:
        phi += 0.25
    aa = model(kappa, phi)
    xx = solve_continuous_lyapunov(aa,-rho)
    ref = exact_integral_matrix(kappa, phi)
    require(np.linalg.norm(xx-ref) < 3e-9 * max(1.,np.linalg.norm(ref)),
            'matrix integral comparison')
    require(abs(xx.trace().real - formula(kappa, phi)) < 3e-9 * max(1.,abs(formula(kappa,phi))),
            'mean-time comparison')
    require(np.max(np.real(np.linalg.eigvals(aa))) < -1e-10,
            'strict decay for nonzero flux')

for kappa, phi in [(0.3,-0.8),(0.6,-1.3),(1.,-math.pi/2),
                    (1.8,0.9),(2.4,-0.6),(3.5,1.9),(.5,2.3),(4.,-2.1)]:
    aa = model(kappa,phi)
    rate = -2*max(np.real(np.linalg.eigvals(aa)))
    cutoff = max(30., 50./rate)
    def survival(t):
        state = expm(t*aa) @ np.array([0.,1.,0.])
        return float(np.real(np.vdot(state,state)))
    numeric,err = quad(survival,0.,cutoff,epsabs=1e-10,epsrel=1e-10,limit=150)
    require(abs(numeric-formula(kappa,phi)) < 2e-8 * max(1.,abs(formula(kappa,phi))),
            f'independent time quadrature k={kappa} phi={phi}')

for kappa in [0.15,0.3,0.65,0.95,1.,1.05,1.6,3.,9.]:
    s_opt = -min(kappa,1.)
    minimum = (11/(4*kappa) if kappa<=1 else 3/kappa-0.5+kappa/4)
    require(abs((3/kappa+1/(2*s_opt)+kappa/(4*s_opt*s_opt))-minimum) < 1e-12,
            'analytic optimal value')
    for lo,hi in [(-1.,-1e-6),(1e-6,1.)]:
        res = minimize_scalar(lambda sn: 3/kappa+1/(2*sn)+kappa/(4*sn*sn),
                              bounds=(lo,hi),method='bounded',options={'xatol':1e-12})
        require(res.fun>=minimum-1e-9,'global optimality')
    neg = minimize_scalar(lambda sn: 3/kappa+1/(2*sn)+kappa/(4*sn*sn),
                          bounds=(-1.,-1e-6),method='bounded',options={'xatol':1e-12})
    require(abs(min(neg.fun, formula(kappa,-math.pi/2))-minimum)<3e-8,'attained optimum including endpoint')

for phi in [0.,math.pi]:
    aa = model(1.,phi)
    for t in [60.,90.,120.]:
        state = expm(t*aa)@np.array([0.,1.,0.])
        require(abs(np.vdot(state,state).real-0.5)<1e-8,'dark flux survival probability')

print(f'PASS: {checks} independent symbolic/numeric assertions')
