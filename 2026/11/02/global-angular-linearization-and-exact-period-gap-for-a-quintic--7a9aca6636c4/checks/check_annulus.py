#!/usr/bin/env python3
"""Reproduce symbolic drift and benchmark physical-time periods."""
import sympy as s
import mpmath as mp
x, y, a, b, lam = s.symbols('x y a b lam', nonzero=True, real=True)
S = x*x+y*y
E = x*x/a+y*y/b-1
R = (1-S)*(-lam*E+2*(a-b)*x*y)
Omega = -2*a*b*(S*E-S+1)
P = x*R-y*Omega
Q = y*R+x*Omega
DS = s.diff(S,x)*P+s.diff(S,y)*Q
DE = s.diff(E,x)*P+s.diff(E,y)*Q
Dlogrho = s.cancel(DS*(1/S+1/(S-1))-DE/E)
assert s.factor(Dlogrho + lam*Omega/(a*b)) == 0
assert s.factor(DS-2*S*(S-1)*(lam*E-2*(a-b)*x*y))==0
assert s.factor(DE-E*(-2*lam*(E+1)*(1-S)+4*(a-b)*x*y*(1-2*S)))==0
print('SYMBOLIC_POLYNOMIAL_DRIFT_IDENTITIES_PASS')
assert s.factor(s.diff((2*s.Symbol('t')-1)*s.Symbol('t') - s.Symbol('d')*s.Symbol('t')**2,s.Symbol('t'))) is not None
mp.mp.dps = 70
for aa,bb in [(mp.mpf(2),mp.mpf(3)),(mp.mpf('1.12'),mp.mpf('5.3')),(mp.mpf(10),mp.mpf(10))]:
    period_C=mp.quad(lambda th: 1/(2*aa*bb*(1-mp.cos(th)**2/aa-mp.sin(th)**2/bb)), [0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])
    period_E=mp.quad(lambda th: 1/(2*mp.sqrt(aa*bb)*(aa*mp.cos(th)**2+bb*mp.sin(th)**2)*(aa*mp.cos(th)**2+bb*mp.sin(th)**2-1)), [0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])
    formula_C=mp.pi/mp.sqrt(aa*bb*(aa-1)*(bb-1))
    formula_E=formula_C-mp.pi/(aa*bb)
    assert abs(period_C-formula_C) < mp.mpf('1e-63')
    assert abs(period_E-formula_E) < mp.mpf('1e-63')
print('PHYSICAL_TIME_PERIOD_FORMULAS_TESTED_3_PARAMETER_PAIRS_PASS')
print('GLOBAL_RETURN_AND_BASIN_ASSERTIONS_REQUIRE_ANALYTIC_ARGUMENT')
