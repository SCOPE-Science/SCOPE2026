"""Reproduce deterministic analytic and numerical checks for the strong-drift theorem.

Run with: python check.py
Requires: Python 3, sympy, scipy, numpy.
All rate and time units are consistent with the stated diffusion generator.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar

E, t, eta = sp.symbols('E t eta', positive=True)
F = ((E + eta*(1+E*t))*sp.exp(t)-E)/(t*(2+E*t))
series = sp.series(F, E, 0, 3).removeO().expand()
f = sp.simplify(series.coeff(E, 0))
g = sp.simplify(series.coeff(E, 1))
assert sp.simplify(f - eta*sp.exp(t)/(2*t)) == 0
assert sp.simplify(g - (sp.exp(t)*(1+eta*t/2)-1)/(2*t)) == 0
c = sp.simplify(-sp.diff(g,t).subs(t,1) / sp.diff(f,t,2).subs(t,1))
assert sp.simplify(c+sp.Rational(1,2)+sp.exp(-1)/eta) == 0
assert sp.simplify(g.subs(t,1) - (sp.E*(1+eta/2)-1)/2) == 0

assertions = 4
for D,L,k in ((1.,1.,2.), (0.7,1.3,4.), (1.,2.,0.6), (2.1,0.8,1.7)):
    dimensionless_eta=2*D/(k*L)
    for U in (5.,10.,20.,40.,80.,160.,320.,640.,1280.):
        M=U*L/(2*D)
        def tau(z):
            return math.expm1(z)/(z*(2*M+z)) + dimensionless_eta*(M+z)*math.exp(z)/(z*(2*M+z))
        result=minimize_scalar(tau,bounds=(0.03,4.),method='bounded',options={'xatol':1e-14})
        assert result.success
        z=result.x
        r=D*z*(2*M+z)/(L*L)
        T=L*L*result.fun/D
        # Independent one-excursion killed resolvent, then Poisson-renewal mean.
        Q=k*math.exp(-z)/(k+math.sqrt(U*U+4*D*r))
        mean_renewal=(1/Q-1)/r
        assert abs(mean_renewal-T)<1e-8*max(1.,T); assertions+=1
        assert T>math.e*L/k; assertions+=1
        rate_asym=U/L-k/(math.e*L)
        time_asym=math.e*L/k + ((math.e-1)*L+math.e*D/k)/U
        if U>=320:
            assert abs(r-rate_asym)<max(0.2,3*D/(L*L*M)); assertions+=1
            assert abs(T-time_asym)<0.08*L*L/D/M; assertions+=1
        if U>=160:
            assert abs(z-1)<max(0.3,8./M); assertions+=1
    # Verify the global bound at independent, nonoptimal rates.
    for U in (0.25,2.5,25.):
        M=U*L/(2*D)
        for z in np.geomspace(0.02,25.,30):
            obj=((1+dimensionless_eta*(M+z))*math.exp(z)-1)/(z*(2*M+z))
            assert obj > dimensionless_eta*math.e/2; assertions+=1
print('PASS:',assertions,'symbolic, independent-resolvent, optimization, and bound checks')
