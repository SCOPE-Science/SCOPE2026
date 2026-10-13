#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

# Functional ranking reversal under pointwise squaring.
J_A = F(1,2)
J_B = F(3,5)
Q_A = F(1,2)
Q_B = F(9,25)
assert J_A < J_B
assert Q_A > Q_B

S,S1,S2,I = sp.symbols('S S1 S2 I', nonnegative=True)
w3,w4,B0,B1,B2,beta,eps = sp.symbols('w3 w4 B0 B1 B2 beta eps', positive=True)
l1,l3,l4,l5,l7,l8 = sp.symbols('l1 l3 l4 l5 l7 l8')
th,ph1,ph2 = sp.symbols('theta phi1 phi2')

# Control-dependent part of true weighted-sum Hamiltonian.
Hws = (
    w3*B0*S*th
    + w4*B1*S1*ph1 + w4*B2*S2*ph2
    + l1*(-th*S) + l3*(th*S)
    + l4*(beta*ph1*S1*I) + l5*(-beta*ph1*S1*I)
    + l7*(eps*beta*ph2*S2*I) + l8*(-eps*beta*ph2*S2*I)
)

sw_th = sp.factor(sp.diff(Hws, th))
sw_1 = sp.factor(sp.diff(Hws, ph1))
sw_2 = sp.factor(sp.diff(Hws, ph2))
assert sp.simplify(sw_th - S*(w3*B0-l1+l3)) == 0
assert sp.simplify(sw_1 - S1*(w4*B1+beta*I*(l4-l5))) == 0
assert sp.simplify(sw_2 - S2*(w4*B2+eps*beta*I*(l7-l8))) == 0

# Source quadratic vaccination term generates an interior first-order formula.
Hq_th = w3*(B0*S*th)**2 + l1*(-th*S) + l3*(th*S)
dq = sp.factor(sp.diff(Hq_th, th))
sol = sp.solve(sp.Eq(dq,0), th)[0]
expected = (l1-l3)/(2*w3*B0**2*S)
assert sp.simplify(sol-expected) == 0

print('VERIFY_OK')
print('linear_costs', J_A, J_B)
print('quadratic_costs', Q_A, Q_B)
print('switch_theta', sw_th)
print('switch_phi1', sw_1)
print('switch_phi2', sw_2)
print('quadratic_theta_stationary', sol)
