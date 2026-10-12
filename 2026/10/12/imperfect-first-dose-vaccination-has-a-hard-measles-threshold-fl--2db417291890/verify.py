#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

# Exact rational forms of the printed source parameters.
mu = F(1,1)/(F('72.67')*12)
A = F(10467629,1)/(F('72.67')*12)
beta = F('0.00000302513594')
eps = F('0.07')
eta = F(30,11)
gamma = F('1.579')

K = eta*A*beta/(mu*(mu+gamma)*(mu+eta))
floor_R = K*eps
u1crit = (1-F(1,1)/K)/(1-eps)

assert floor_R > 1
assert u1crit > 1

# Source rounded relation -18.63 u1 + 20.03 = 1.
intercept = K
slope = K*(1-eps)
assert abs(float(intercept)-20.03) < 0.01
assert abs(float(slope)-18.63) < 0.01

u1,u2,smu,seps,sK = sp.symbols('u1 u2 mu eps K', positive=True)
Rfact = sK*(seps + (1-seps)*smu*(1-u1)/(u2+smu))
Rraw = sK*(seps*(u1*smu+u2)+smu*(1-u1))/(u2+smu)
assert sp.simplify(Rfact-Rraw) == 0

du1 = sp.factor(sp.diff(Rfact,u1))
du2 = sp.factor(sp.diff(Rfact,u2))
assert sp.simplify(du1 + sK*(1-seps)*smu/(u2+smu)) == 0
assert sp.simplify(du2 + sK*(1-seps)*smu*(1-u1)/(u2+smu)**2) == 0

# Concrete checks on admissible source-like controls.
def R(u1q,u2q):
    return K*(eps+(1-eps)*mu*(1-u1q)/(u2q+mu))
for a,b in [(F(0),F(0)),(F('0.85'),F(0)),(F('0.999'),F(0)),(F('0.85'),F('0.005')), (F('0.999'),F(1000))]:
    assert R(a,b) > floor_R > 1

print('VERIFY_OK')
print('K', float(K))
print('floor_K_epsilon', float(floor_R))
print('u1_critical_u2_zero', float(u1crit))
print('rounded_intercept', float(intercept))
print('rounded_slope', float(slope))
print('dR_du1', du1)
print('dR_du2', du2)
