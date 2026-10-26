"""Numerical checks for the strong-detuning maximal-level-spacing limit.

Run with: python3 verify_spacing.py
Requires scipy and numpy. Finite tests corroborate, but do not prove, the limiting theorem.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import ai_zeros

C = 3*np.pi/4
zstar = (3+np.sqrt(3))/4
tstar = zstar**1.5 * np.sqrt(zstar-1)
index_const = tstar / C
spacing_const = C * 2*np.sqrt(zstar-1)/(np.sqrt(zstar)*(4*zstar-3))

def modes(Omega, g, count):
    zeros, deriv, _, _ = ai_zeros((count+1)//2+1)
    roots = np.sort(np.r_[-zeros, -deriv])[:count]
    return np.array([brentq(lambda w: w**3*(w-Omega)-g*g*r**3,
                             Omega, Omega+10*(1+r)*max(1., g)) for r in roots])

print('index constant', format(index_const,'.12f'))
print('spacing constant', format(spacing_const,'.12f'))
for Omega in (5., 10., 15., 20., 30., 40.):
    x = modes(Omega, 1., max(160, int(Omega**2/2)+50))
    gaps = np.diff(x)
    index = int(np.argmax(gaps)) + 1
    scaled_gap = Omega*gaps[index-1]
    assert np.isfinite(scaled_gap) and scaled_gap>0
    print(f'Omega={Omega:.0f}; maximizing index={index}; n/Omega^2={index/Omega**2:.9f}; Omega*gap={scaled_gap:.9f}')
    if Omega >= 20:
        assert abs(index/Omega**2-index_const)<0.005
        assert abs(scaled_gap-spacing_const)<0.001
print('Numerical corroboration passed.')
