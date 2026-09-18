#!/usr/bin/env python3
"""Numerically verify the cubic-counterterm identity for the three-node formula."""

import cmath
import itertools
import math

a = 1.7
rho = 0.43
w = [
    [0.0, 0.7, -0.4],
    [1.1, 0.0, 0.6],
    [-0.3, 0.9, 0.0],
]

def source_f2(theta, i):
    j, k = [q for q in range(3) if q != i]
    ti, tj, tk = theta[i], theta[j], theta[k]
    wij, wik = w[i][j], w[i][k]
    S = (
        wij*w[j][i]*(math.sin(2*rho) + math.sin(2*(tj-ti)))
        + wij*w[j][k]*(math.sin(tk-ti+2*rho) + math.sin(2*tj-tk-ti))
        + wik*w[k][i]*(math.sin(2*rho) + math.sin(2*(tk-ti)))
        + wik*w[k][j]*(math.sin(tj-ti+2*rho) + math.sin(2*tk-tj-ti))
        - wij**2*math.sin(2*(tj-ti)+2*rho)
        - 2*wij*wik*math.sin(tj+tk-2*ti+2*rho)
        - wik**2*math.sin(2*(tk-ti)+2*rho)
    )
    return S/(4*a)

def Q(z, i):
    j, k = [q for q in range(3) if q != i]
    zi, zj, zk = z[i], z[j], z[k]
    wij, wik = w[i][j], w[i][k]
    e2r = cmath.exp(2j*rho)
    return (
        e2r*(
            wij*w[j][i]*abs(zj)**2*zi
            + wik*w[k][i]*abs(zk)**2*zi
            + wij*w[j][k]*abs(zi)**2*zk
            + wik*w[k][j]*abs(zi)**2*zj
            - 2*wij*wik*zj*zk*zi.conjugate()
        )
        + (wij*w[j][i] - wij**2*e2r)*zj**2*zi.conjugate()
        + (wik*w[k][i] - wik**2*e2r)*zk**2*zi.conjugate()
        + wij*w[j][k]*zj**2*zk.conjugate()
        + wik*w[k][j]*zk**2*zj.conjugate()
    )

def counterterm_phase(theta, i):
    R = math.sqrt(a)
    z = [R*cmath.exp(1j*t) for t in theta]
    H = -Q(z, i)/(4*a*a)
    return (cmath.exp(-1j*theta[i])*H).imag/R

grid = [-2.1, -0.7, 0.2, 1.4, 2.6]
residuals = []
for theta in itertools.product(grid, repeat=3):
    for i in range(3):
        residuals.append(abs(source_f2(theta, i) + counterterm_phase(theta, i)))

print(f"max_abs_residual={max(residuals):.3e}")
print(f"checks={len(residuals)}")
