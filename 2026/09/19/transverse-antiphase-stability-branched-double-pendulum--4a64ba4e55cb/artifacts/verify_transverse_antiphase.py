"""Verification for the transverse antiphase equation of the branched double pendulum.

The script checks three claims:
1. the quadratic transverse Euler--Lagrange equation;
2. the acceleration-free expression for its stiffness along the symmetric manifold;
3. the O(A^2) Fourier decomposition obtained from the two linear in-phase modes.
"""

import math
import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# 1. Exact normal variational equation from the quadratic transverse Lagrangian
# ---------------------------------------------------------------------------
t = sp.symbols("t", real=True)
M1, M2, mu, G1, G2 = sp.symbols("M1 M2 mu G1 G2", positive=True)
x = sp.Function("x")(t)
y = sp.Function("y")(t)
d = sp.Function("d")(t)
Delta = y - x

L2 = (
    M2 * sp.diff(d, t) ** 2
    - 2 * mu * sp.sin(Delta) * sp.diff(x, t) * d * sp.diff(d, t)
    - mu * sp.cos(Delta) * sp.diff(x, t) * sp.diff(y, t) * d**2
    - G2 * sp.cos(y) * d**2
)
EL = sp.diff(sp.diff(L2, sp.diff(d, t)), t) - sp.diff(L2, d)
K = (
    G2 * sp.cos(y)
    + mu * sp.cos(Delta) * sp.diff(x, t) ** 2
    - mu * sp.sin(Delta) * sp.diff(x, t, 2)
)
normal_form = 2 * (M2 * sp.diff(d, t, 2) + K * d)
nve_residual = sp.simplify(sp.expand_trig(EL - normal_form))
assert nve_residual == 0

# ---------------------------------------------------------------------------
# 2. Eliminate x'' using the exact symmetric-manifold equations
# ---------------------------------------------------------------------------
xs, ys, xdot, ydot = sp.symbols("x y xdot ydot", real=True)
s = sp.sin(ys - xs)
c = sp.cos(ys - xs)
Den = M1 * M2 - 2 * mu**2 * c**2
xdd = (
    -G1 * M2 * sp.sin(xs)
    + 2 * G2 * mu * c * sp.sin(ys)
    + 2 * M2 * mu * s * ydot**2
    + 2 * mu**2 * s * c * xdot**2
) / Den
Q_acc = (G2 * sp.cos(ys) + mu * c * xdot**2 - mu * s * xdd) / M2
Q_first = (
    (G2 / M2) * sp.cos(ys)
    + mu * c * (M1 * M2 - 2 * mu**2) * xdot**2 / (M2 * Den)
    + mu * G1 * s * sp.sin(xs) / Den
    - 2 * G2 * mu**2 * s * c * sp.sin(ys) / (M2 * Den)
    - 2 * mu**2 * s**2 * ydot**2 / Den
)
accel_free_residual = sp.trigsimp(sp.cancel(sp.together(Q_acc - Q_first)))
accel_free_residual = sp.simplify(
    accel_free_residual.subs(sp.sin(ys - xs) ** 2, 1 - sp.cos(ys - xs) ** 2)
)
assert accel_free_residual == 0

# ---------------------------------------------------------------------------
# 3. Printed source parameters and the O(A^2) modulation spectrum
# ---------------------------------------------------------------------------
g = 9.81
lam1 = 0.084
lam2 = 0.043
ell12 = 0.270
m1 = 0.12880
m2 = 0.10531
I1 = 1.88e-3
I2 = 0.516e-3

M1n = I1 + m1 * lam1**2 + 2 * m2 * ell12**2
M2n = I2 + m2 * lam2**2
mun = m2 * ell12 * lam2
G1n = m1 * g * lam1 + 2 * m2 * g * ell12
G2n = m2 * g * lam2

Mass = np.array([[M1n, 2 * mun], [2 * mun, 2 * M2n]], dtype=float)
Stiff = np.array([[G1n, 0.0], [0.0, 2 * G2n]], dtype=float)
vals, vecs = np.linalg.eig(np.linalg.solve(Mass, Stiff))
order = np.argsort(vals)
vals = vals[order]
vecs = vecs[:, order]
omega = np.sqrt(vals)
r = np.array([vecs[1, j] / vecs[0, j] for j in range(2)])
# x(0)=A, y(0)=0, zero initial velocities
aL = -r[1] / (r[0] - r[1])
aH = 1.0 - aL
amps = np.array([aL, aH])
omega_d = math.sqrt(G2n / M2n)

q0 = 0.0
q2 = []
for aj, rj, wj in zip(amps, r, omega):
    q0 += aj**2 * (
        -omega_d**2 * rj**2 / 4
        + (mun / M2n) * rj * wj**2 / 2
    )
    q2.append(
        aj**2
        * (
            -omega_d**2 * rj**2 / 4
            + (mun / M2n) * wj**2 * (rj - 2) / 2
        )
    )
common = 0.5 * ((r[0] - 1) * omega[1] ** 2 + (r[1] - 1) * omega[0] ** 2)
q_sum = aL * aH * (
    -omega_d**2 * r[0] * r[1] / 2
    + (mun / M2n) * (-omega[0] * omega[1] + common)
)
q_diff = aL * aH * (
    -omega_d**2 * r[0] * r[1] / 2
    + (mun / M2n) * (+omega[0] * omega[1] + common)
)

# Compare the coefficient formula with the direct quadratic expansion at many times.
def q2_direct(tt):
    cL, cH = math.cos(omega[0] * tt), math.cos(omega[1] * tt)
    sL, sH = math.sin(omega[0] * tt), math.sin(omega[1] * tt)
    x1 = aL * cL + aH * cH
    y1 = aL * r[0] * cL + aH * r[1] * cH
    xd1 = -aL * omega[0] * sL - aH * omega[1] * sH
    xdd1 = -aL * omega[0] ** 2 * cL - aH * omega[1] ** 2 * cH
    return -0.5 * omega_d**2 * y1**2 + (mun / M2n) * (
        xd1**2 - (y1 - x1) * xdd1
    )

def q2_fourier(tt):
    return (
        q0
        + q2[0] * math.cos(2 * omega[0] * tt)
        + q2[1] * math.cos(2 * omega[1] * tt)
        + q_diff * math.cos((omega[1] - omega[0]) * tt)
        + q_sum * math.cos((omega[1] + omega[0]) * tt)
    )

test_times = np.linspace(0.0, 5.0, 101)
max_fourier_residual = max(abs(q2_direct(tt) - q2_fourier(tt)) for tt in test_times)
assert max_fourier_residual < 1e-10

print("nve_symbolic_residual = 0")
print("acceleration_free_symbolic_residual = 0")
print(f"max_fourier_residual = {max_fourier_residual:.3e}")
print(f"f_low = {omega[0]/(2*math.pi):.12f} Hz")
print(f"f_high = {omega[1]/(2*math.pi):.12f} Hz")
print(f"f_antiphase = {omega_d/(2*math.pi):.12f} Hz")
print(f"f_sum = {(omega[0]+omega[1])/(2*math.pi):.12f} Hz")
print(f"2f_antiphase = {2*omega_d/(2*math.pi):.12f} Hz")
print(f"q0/A^2 = {q0:.12f} s^-2")
print(f"q_2low/A^2 = {q2[0]:.12f} s^-2")
print(f"q_2high/A^2 = {q2[1]:.12f} s^-2")
print(f"q_difference/A^2 = {q_diff:.12f} s^-2")
print(f"q_sum/A^2 = {q_sum:.12f} s^-2")
print("all_checks_passed = True")
