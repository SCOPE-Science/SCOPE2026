#!/usr/bin/env python3
"""Symbolic verification of triplet cancellation and the sync–splay identity."""

import sympy as sp

a, eps, rho = sp.symbols("a eps rho", positive=True, real=True)
t0, t1, t2 = sp.symbols("t0 t1 t2", real=True)
theta = [t0, t1, t2]


def first_order(i, j, k):
    ti, tj, tk = theta[i], theta[j], theta[k]
    return sp.sin(tj - ti + rho) + sp.sin(tk - ti + rho)


def second_order(i, j, k):
    ti, tj, tk = theta[i], theta[j], theta[k]
    c_jji = sp.sin(2*rho) + sp.sin(2*(tj-ti))
    c_jjk = sp.sin(tk-ti+2*rho) + sp.sin(2*tj-tk-ti)
    c_kki = sp.sin(2*rho) + sp.sin(2*(tk-ti))
    c_kkj = sp.sin(tj-ti+2*rho) + sp.sin(2*tk-tj-ti)
    d_jj = sp.sin(2*(tj-ti)+2*rho)
    d_jk = sp.sin(tj+tk-2*ti+2*rho)
    d_kk = sp.sin(2*(tk-ti)+2*rho)
    return (c_jji+c_jjk+c_kki+c_kkj-d_jj-2*d_jk-d_kk)/(4*a)


def physical_nonpairwise(i, j, k):
    ti, tj, tk = theta[i], theta[j], theta[k]
    return (
        -sp.sin(2*tj-tk-ti)
        -sp.sin(2*tk-tj-ti)
        +2*sp.sin(tj+tk-2*ti+2*rho)
    )


orders = [(0, 1, 2), (1, 0, 2), (2, 0, 1)]
# Divide the phase vector field by eps.  The physical scale is eta=eps**2/(4*a).
field = sp.Matrix([
    sp.simplify(
        first_order(i, j, k)
        + eps*second_order(i, j, k)
        + eps/(4*a)*physical_nonpairwise(i, j, k)
    )
    for i, j, k in orders
])


def H_over_eps(phi):
    return (
        sp.sin(phi+rho)
        + eps/(4*a) * (
            sp.sin(2*rho)
            + sp.sin(2*phi)
            + sp.sin(phi+2*rho)
            - sp.sin(2*phi+2*rho)
        )
    )


for i, j, k in orders:
    residual = sp.simplify(sp.trigsimp(
        field[i] - (H_over_eps(theta[j]-theta[i]) + H_over_eps(theta[k]-theta[i]))
    ))
    assert residual == 0

J = field.jacobian(theta)
J_sync = sp.simplify(sp.trigsimp(J.subs({t0: 0, t1: 0, t2: 0})))
lambda_sync_over_eps = sp.simplify(J_sync[0, 0] - J_sync[0, 1])

J_splay = sp.simplify(sp.trigsimp(
    J.subs({t0: 0, t1: 2*sp.pi/3, t2: 4*sp.pi/3})
))
d, p, q = J_splay[0, 0], J_splay[0, 1], J_splay[0, 2]
zeta = -sp.Rational(1, 2) + sp.I*sp.sqrt(3)/2
lambda_splay_over_eps = sp.simplify(sp.expand_complex(d + p*zeta + q*zeta**2))
real_splay_over_eps = sp.simplify(sp.re(lambda_splay_over_eps))

critical_factor = 4*a*sp.cos(rho) + 3*eps - 2*eps*sp.cos(rho)**2
assert sp.simplify(lambda_sync_over_eps + 3*critical_factor/(4*a)) == 0
assert sp.simplify(real_splay_over_eps - 3*critical_factor/(8*a)) == 0
assert sp.simplify(lambda_sync_over_eps + 2*real_splay_over_eps) == 0

print("pairwise_residual_identity: PASS")
print("lambda_sync / eps =", sp.factor(lambda_sync_over_eps))
print("Re(lambda_splay) / eps =", sp.factor(real_splay_over_eps))
print("lambda_sync + 2 Re(lambda_splay) = 0: PASS")
print("critical_factor =", critical_factor)
