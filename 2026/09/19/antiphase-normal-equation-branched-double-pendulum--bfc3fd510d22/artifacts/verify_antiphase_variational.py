#!/usr/bin/env python3
"""Symbolic and numerical checks for the branched-double-pendulum normal equation."""
import math
import numpy as np
import sympy as sp

# Symbolic second variation of the source Lagrangian in theta_d=x.
t1, tm, x = sp.symbols('theta1 thetam x', real=True)
v1, vm, vx, a1 = sp.symbols('v1 vm vx a1', real=True)
M1, M2, mu, G1, G2 = sp.symbols('M1 M2 mu G1 G2', positive=True, real=True)
delta = tm - t1
c = sp.cos(delta)
s = sp.sin(delta)
K = sp.Rational(1, 2) * (
    M1*v1**2 + 4*mu*c*sp.cos(x)*v1*vm - 4*mu*s*sp.sin(x)*v1*vx
    + 2*M2*vm**2 + 2*M2*vx**2
)
U = G1*(1-sp.cos(t1)) + 2*G2*(1-sp.cos(tm)*sp.cos(x))
L = K-U

L_xx = sp.simplify(sp.diff(L, x, 2).subs({x: 0, vx: 0}))
L_xvx = sp.simplify(sp.diff(sp.diff(L, x), vx).subs({x: 0, vx: 0}))
L_vxvx = sp.simplify(sp.diff(L, vx, 2).subs({x: 0, vx: 0}))
assert sp.simplify(L_vxvx - 2*M2) == 0
assert sp.simplify(L_xx - (-2*G2*sp.cos(tm)-2*mu*c*v1*vm)) == 0
assert sp.simplify(L_xvx - (-2*mu*s*v1)) == 0

# d/dt(-2 mu sin(delta) v1), with delta_dot=vm-v1.
d_Lxvx_dt = -2*mu*(c*(vm-v1)*v1 + s*a1)
kappa_from_jacobi = sp.simplify((d_Lxvx_dt-L_xx)/2)
kappa_target = G2*sp.cos(tm) + mu*c*v1**2 - mu*s*a1
assert sp.simplify(kappa_from_jacobi-kappa_target) == 0

# Physical parameters reported in arXiv:2609.20688v1.
m1 = 0.12880
m2 = 0.10531
lam1 = 0.084
lam2 = 0.043
ell12 = 0.270
I1 = 1.88e-3
I2 = 0.516e-3
g = 9.81
M1n = I1 + m1*lam1**2 + 2*m2*ell12**2
M2n = I2 + m2*lam2**2
mun = m2*ell12*lam2
G1n = (m1*lam1 + 2*m2*ell12)*g
G2n = m2*lam2*g

# Linear symmetric frequencies and antisymmetric frequency.
Mass = np.array([[M1n, 2*mun], [2*mun, 2*M2n]], dtype=float)
Stiff = np.diag([G1n, 2*G2n])
w2 = np.linalg.eigvals(np.linalg.solve(Mass, Stiff))
wlo, whi = np.sqrt(np.sort(w2))
wd = math.sqrt(G2n/M2n)

# Exact release-point normal stiffness and its first zero on (0, pi/2).
D0 = M1n*M2n - 2*mun**2
root_sin2 = G2n*D0/(mun*M2n*G1n - 2*G2n*mun**2)
A_static = math.asin(math.sqrt(root_sin2))

def kappa_release(A):
    den = M1n*M2n - 2*mun**2*math.cos(A)**2
    acc1 = -M2n*G1n*math.sin(A)/den
    return G2n + mun*math.sin(A)*acc1

assert kappa_release(math.radians(47.8)) > 0
assert abs(kappa_release(A_static)) < 1e-12

# Quadratic normal-stiffness spectrum for a parent-only small-amplitude release.
# Eigenvectors are normalized as (theta1, thetam)=(1,r_j).
rlo = mun*wlo**2/(G2n-M2n*wlo**2)
rhi = mun*whi**2/(G2n-M2n*whi**2)
a = -rhi/(rlo-rhi)
b = rlo/(rlo-rhi)
S = (rlo-1)*whi**2 + (rhi-1)*wlo**2
Ksum = a*b*(-G2n*rlo*rhi/2 - mun*wlo*whi + mun*S/2)
Kdiff = a*b*(-G2n*rlo*rhi/2 + mun*wlo*whi + mun*S/2)
K2lo = a*a*(-G2n*rlo**2/4 + mun*(rlo-2)*wlo**2/2)
K2hi = b*b*(-G2n*rhi**2/4 + mun*(rhi-2)*whi**2/2)
Kmean = (
    a*a*(-G2n*rlo**2/4 + mun*rlo*wlo**2/2)
    + b*b*(-G2n*rhi**2/4 + mun*rhi*whi**2/2)
)

# The sum harmonic is the nearest quadratic harmonic to twice the antiphase frequency.
f = lambda w: w/(2*math.pi)
quad = {
    '2*f_low': f(2*wlo),
    '2*f_high': f(2*whi),
    'f_low+f_high': f(wlo+whi),
    'f_high-f_low': f(whi-wlo),
}
target = f(2*wd)
detunings = {name: abs(val-target) for name,val in quad.items()}
nearest = min(detunings, key=detunings.get)
assert nearest == 'f_low+f_high'
assert abs(Ksum) > 1e-10

print('symbolic_normal_equation_check=True')
print(f'M1={M1n:.12g}')
print(f'M2={M2n:.12g}')
print(f'mu={mun:.12g}')
print(f'G1={G1n:.12g}')
print(f'G2={G2n:.12g}')
print(f'f_low={f(wlo):.12f} Hz')
print(f'f_high={f(whi):.12f} Hz')
print(f'f_d={f(wd):.12f} Hz')
print(f'kappa_release_47.8deg={kappa_release(math.radians(47.8)):.12g}')
print(f'release_static_zero={math.degrees(A_static):.12f} deg')
print(f'Kmean={Kmean:.12g}')
print(f'K_2low={K2lo:.12g}')
print(f'K_2high={K2hi:.12g}')
print(f'K_sum={Ksum:.12g}')
print(f'K_diff={Kdiff:.12g}')
print(f'2f_d={target:.12f} Hz')
for name,val in quad.items():
    print(f'{name}={val:.12f} Hz; detuning={detunings[name]:.12f} Hz')
print(f'nearest_quadratic_channel={nearest}')
print('all_checks_passed=True')
