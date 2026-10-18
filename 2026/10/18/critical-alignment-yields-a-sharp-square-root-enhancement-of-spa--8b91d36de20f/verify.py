"""Standalone finite-precision checks for critical alignment Fourier relaxation.

Requires numpy, scipy and sympy. Numerical integration supports but does not prove
an infinite-time asymptotic statement.
"""
from math import pi, sqrt, log
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

m, k = sp.symbols('m k', positive=True, real=True)
w = sp.sqrt(k*k-1)
disc = 1 + (sp.sinh(m)-sp.I*k)**2
root = sp.I*w*sp.sqrt(1+(disc+w*w)/(-w*w))
series = sp.series(root,m,0,3).removeO().expand()
assert sp.simplify(series.coeff(m,0)-sp.I*w)==0
assert sp.simplify(series.coeff(m,1)+k/w)==0
assert sp.simplify(series.coeff(m,2)-sp.I/(2*w**3))==0
mag_rhs = 2*(sp.sinh(m)-m*sp.cosh(m))
assert sp.simplify(sp.series(mag_rhs,m,0,7).removeO()+2*m**3/3+m**5/15)==0

freq=2*pi
coefficient=sqrt(3)*freq/sqrt(freq*freq-1)

def rhs(t,y):
    magnetization=float(np.real(y[0]))
    zplus,zminus=y[1],y[2]
    em=np.exp(-magnetization)
    ep=np.exp(magnetization)
    # z=e^t w, which removes the overall e^-t decay.
    return np.array([
      2*(np.sinh(magnetization)-magnetization*np.cosh(magnetization)),
      (-1j*freq-em+1)*zplus+ep*zminus,
      em*zplus+(1j*freq-ep+1)*zminus],dtype=complex)

times=[100,250,400,700,1200,2000]
sol=solve_ivp(rhs,(0,times[-1]),np.array([.5,1+0j,1+0j]),
              t_eval=times,rtol=1e-11,atol=1e-12,method='DOP853',max_step=.3)
assert sol.success
res=[]
for t,y in zip(sol.t,sol.y.T):
    mm=float(np.real(y[0]))
    assert abs(mm*sqrt(t)-sqrt(3)/2) < .035
    q=log(np.linalg.norm(y[1:]))-coefficient*sqrt(t)+3*log(t)/8
    res.append(q)
    print(f't={t}: m={mm:.12f}, renormalized log amplitude={q:.12f}')
# Residual changes shrink on the computed late-time intervals.
assert abs(res[-1]-res[-2]) < .04
assert abs(res[-1]-res[-2]) < abs(res[-2]-res[-3])
print('PASS: critical algebra, correct Fourier matrix, asymptotic numerical trend')
