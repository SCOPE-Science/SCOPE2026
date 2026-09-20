"""Compact symbolic and numerical checks for the published Goodwin identities."""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
from scipy.signal import find_peaks

b1, b2, b3 = sp.symbols("b1 b2 b3")
a1 = b1 + b2 + b3
a2 = b1*b2 + b1*b3 + b2*b3
a3 = b1*b2*b3
H = (b1+b2)*(b1+b3)*(b2+b3)
print("factorization_residual =", sp.expand(a1*a2-a3-H))

# Example: M'=100/(1+R^12)-M, P'=M-P, R'=P-R.
def rhs(t, u):
    M, P, R = u
    return [100.0/(1.0+R**12)-M, M-P, P-R]

sol = solve_ivp(rhs, (0.0, 500.0), (1.0, 1.0, 1.0),
                rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.02)
t = np.linspace(350.0, 500.0, 150001)
R = sol.sol(t)[2]
peaks, _ = find_peaks(R, distance=2000, prominence=0.01)

def Rdot(s):
    M, P, R = sol.sol(s)
    return P-R

peak_times = [brentq(Rdot, t[p]-0.05, t[p]+0.05, xtol=1e-13)
              for p in peaks[-5:]]
t0, t1 = peak_times[-2], peak_times[-1]
period = t1-t0

def vals(s):
    M, P, R = sol.sol(s)
    v = P-R
    w = (M-P)-(P-R)
    fp = -12.0*R**11/(1.0+R**12)**2
    return v, w, fp

Iv = quad(lambda s: vals(s)[0]**2, t0, t1,
          epsabs=1e-10, epsrel=1e-10, limit=400)[0]
Iw = quad(lambda s: vals(s)[1]**2, t0, t1,
          epsabs=1e-10, epsrel=1e-10, limit=400)[0]
Is = quad(lambda s: (-100.0*vals(s)[2])*vals(s)[0]**2, t0, t1,
          epsabs=1e-10, epsrel=1e-10, limit=400)[0]

print(f"period = {period:.12f}")
print(f"curvature_ratio = {Iw/Iv:.12f}   expected 3")
print(f"weighted_slope = {Is/Iv:.12f}   expected 8")
print(f"known_period_floor = {2*np.pi/np.sqrt(3):.12f}")
