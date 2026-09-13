"""Corroborating computation for lane-1722 emergent finding (atom mass = 0).

Checks, for the standard semicircular law (var 1) and the var-2 semicircular
law of s1+s2, that t -> log|t| is integrable against the density, so the
Fuglede--Kadison determinants are strictly positive. Uses midpoint/trapezoid
quadrature on a fine grid; the atom conclusion itself follows analytically
from the bounded-density argument in DRAFT.md, this script only corroborates
the numerical values Delta(s1) = e^{-1/2}, Delta(s1+s2) = sqrt(2)*e^{-1/2}.
"""
import numpy as np

print("numpy", np.__version__)

# Standard semicircle density, variance 1, support [-2, 2]
N = 400001
ts = np.linspace(-2.0, 2.0, N)
dt = ts[1] - ts[0]
rho = np.sqrt(np.maximum(0.0, 4.0 - ts**2)) / (2.0 * np.pi)
print("max density rho1:", rho.max(), "(bound 1/pi =", 1.0/np.pi, ")")
l = np.log(np.abs(ts))
l[N // 2] = np.log(dt / 2.0)  # regularize the single grid point at 0
I1 = float(np.sum(l * rho) * dt)
print("I1 = tau(log|s1|) =", I1, " Delta(s1) =", np.exp(I1))
print("conjectured exact: -1/2 =", -0.5, " exp =", np.exp(-0.5))

# Variance-2 semicircle density (law of s1+s2), support [-2*sqrt2, 2*sqrt2]
a = 2.0 * np.sqrt(2.0)
ts2 = np.linspace(-a, a, N)
dt2 = ts2[1] - ts2[0]
rho2 = np.sqrt(np.maximum(0.0, 8.0 - ts2**2)) / (4.0 * np.pi)
print("max density rho2:", rho2.max())
l2 = np.log(np.abs(ts2))
l2[N // 2] = np.log(dt2 / 2.0)
I2 = float(np.sum(l2 * rho2) * dt2)
print("I2 = tau(log|s1+s2|) =", I2, " Delta(s1+s2) =", np.exp(I2))
print("conjectured exact: log(sqrt2)-1/2 =", np.log(np.sqrt(2)) - 0.5)

Ip = I1 + I2
print("log Delta(p1) =", Ip, " Delta(p1) =", np.exp(Ip))
print("conjectured exact: sqrt(2)/e =", np.sqrt(2)/np.e)
assert np.exp(I1) > 0.5 and np.exp(I2) > 0.5 and np.exp(Ip) > 0.5
assert abs(I1 + 0.5) < 1e-3 and abs(I2 - (np.log(np.sqrt(2)) - 0.5)) < 1e-3
print("OK: all determinants strictly positive -> no atom at 0.")
