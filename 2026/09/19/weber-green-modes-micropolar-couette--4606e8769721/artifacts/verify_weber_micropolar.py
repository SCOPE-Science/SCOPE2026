#!/usr/bin/env python3
"""Verify the Weber reduction for the balanced-viscosity micropolar Couette mode."""

import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.special import pbdv
import scipy

print(f"numpy={np.__version__}")
print(f"sympy={sp.__version__}")
print(f"scipy={scipy.__version__}")

def qfun(A, xi, eta0, t):
    return xi*xi + (eta0 - A*t*xi)**2

def Qfun(A, xi, eta0, t):
    return (xi*xi + 1 + eta0*eta0)*t - A*xi*eta0*t*t + (A*A*xi*xi)*t**3/3

def exact_phi(A, xi, eta0, t):
    rho = abs(A*xi)
    if rho == 0:
        q = xi*xi + eta0*eta0
        C = np.array([[1.0, q], [1.0, -1.0]])
        lam = math.sqrt(q + 1.0)
        I = np.eye(2)
        return math.exp(-(q+1.0)*t) * (
            math.cosh(lam*t)*I + math.sinh(lam*t)*C/lam
        )
    tc = eta0/(A*xi)
    nu = -0.5 - (xi*xi + 1.0)/(2.0*rho)
    root = math.sqrt(2.0*rho)

    def Y(s):
        z = root*(s-tc)
        Dp, dDp = pbdv(nu, z)
        Dm, dDm = pbdv(nu, -z)
        return np.array([[Dp, Dm], [root*dDp, -root*dDm]])

    R = np.array([[1.0, 1.0], [1.0, 0.0]])
    return math.exp(-Qfun(A,xi,eta0,t)) * R @ Y(t) @ np.linalg.inv(Y(0.0)) @ np.linalg.inv(R)

def numerical_phi(A, xi, eta0, T):
    def rhs(t, flat):
        q = qfun(A,xi,eta0,t)
        B = np.array([[-q,q],[1.0,-q-2.0]])
        return (B @ flat.reshape(2,2)).ravel()
    sol = solve_ivp(
        rhs, (0.0,T), np.eye(2).ravel(),
        method="DOP853", rtol=1e-12, atol=1e-14
    )
    return sol.y[:,-1].reshape(2,2)

# Symbolic reduction.
t = sp.symbols("t", real=True)
q = sp.Function("q")(t)
Q = sp.Function("Q")(t)
y = sp.Function("y")(t)
omega = sp.exp(-Q)*y
m = sp.exp(-Q)*(sp.diff(y,t)+y)
subsQ = {sp.diff(Q,t): q+1}
r1 = sp.factor((sp.diff(m,t)-(-q*m+q*omega)).subs(subsQ))
r2 = sp.factor((sp.diff(omega,t)-(m-(q+2)*omega)).subs(subsQ))
target = sp.exp(-Q)*(sp.diff(y,t,2)-(q+1)*y)
assert sp.simplify(r1-target) == 0
assert sp.simplify(r2) == 0
print("symbolic_reduction=passed")

# Nonzero-frequency special-function formula.
samples = [
    (3.0, 0.7, 1.2, 2.0),
    (2.0, -0.8, 0.4, 1.7),
    (1.5, 1.1, -0.9, 1.4),
]
for j, par in enumerate(samples, 1):
    A, xi, eta0, T = par
    pe = exact_phi(*par)
    pn = numerical_phi(*par)
    err = np.max(np.abs(pe-pn))
    derr = abs(np.linalg.det(pe)-math.exp(-2*Qfun(A,xi,eta0,T)))
    print(f"sample{j}_matrix_max_error={err:.3e}")
    print(f"sample{j}_det_error={derr:.3e}")
    assert err < 2e-11
    assert derr < 2e-14

# Streamwise-zero elementary formula.
A, xi, eta0, T = 3.0, 0.0, 0.6, 1.3
q0 = eta0*eta0
B0 = np.array([[-q0,q0],[1.0,-q0-2.0]])
zero_err = np.max(np.abs(exact_phi(A,xi,eta0,T)-expm(T*B0)))
print(f"zero_mode_max_error={zero_err:.3e}")
assert zero_err < 2e-14

# The logarithmic remainder in the largest-singular-value asymptotic stays bounded
# and approaches a constant for a representative nonzero mode.
A, xi, eta0 = 3.0, 0.7, 1.2
rho = abs(A*xi)
tc = eta0/(A*xi)
nu = -0.5-(xi*xi+1.0)/(2*rho)
for T in (2.0, 2.5, 3.0, 3.5):
    P = exact_phi(A,xi,eta0,T)
    smax = np.linalg.svd(P, compute_uv=False)[0]
    z = math.sqrt(2*rho)*(T-tc)
    rem = math.log(smax)+Qfun(A,xi,eta0,T)-z*z/4+nu*math.log(z)
    print(f"asymptotic_remainder_t{T:.1f}={rem:.9f}")

print("all_checks_passed=True")
