#!/usr/bin/env python3
from fractions import Fraction as F
import math

Lam = F(5)
beta = F(3, 10**6)
omega = F(8, 10**6)
lam = F(12, 1000)
p = F(1200)
d = F(4, 100000)
alpha = F(1, 100000)
nu = F(1, 5)
lam0 = F(8, 1000)
r0 = F(5, 1000)
M0 = F(500)

C = nu + alpha + d
b = lam0 + d
q = lam / b
R0 = beta * Lam / (d * C)
h0 = M0 / (p + M0)
R1 = R0 / (1 + q*h0)
kappa = (R0 - 1) / q
Dinf = 1 + alpha/d + C*omega/beta*(1+q)

assert C == F(4001, 20000)
assert b == F(201, 25000)
assert q == F(100, 67)
assert R0 == F(7500, 4001)
assert R1 == F(8542500, 6557639) > 1
assert kappa == F(234433, 400100)
assert h0 < kappa < 1

Minf = p*kappa/(1-kappa)
coef = r0*(Minf-M0)
assert Minf == F(281319600, 165667)
assert coef == F(1984861, 331334)
assert Dinf == F(324073, 125625)

# Exact identity components as floating functions for finite replay.
Cf=float(C); betaf=float(beta); qf=float(q); kappaf=float(kappa)
omegaf=float(omega); alphaf=float(alpha); df=float(d)
pf=float(p); r0f=float(r0); M0f=float(M0)

def h(M):
    return M/(pf+M)

def D(M):
    return 1.0 + alphaf/df + Cf*omegaf/betaf*(1.0+qf*h(M))

def residual_M(M, r):
    I = r0f*(M-M0f)/r
    return I*D(M) - (Cf*qf/betaf)*(kappaf-h(M))

def root_M(r):
    lo=M0f
    hi=float(Minf)
    flo=residual_M(lo,r)
    fhi=residual_M(hi,r)
    assert flo < 0 < fhi
    for _ in range(160):
        mid=(lo+hi)/2
        fm=residual_M(mid,r)
        if fm > 0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

vals=[]
for r in (0.003,0.009,0.1,1.0,10.0,100.0):
    M=root_M(r)
    I=r0f*(M-M0f)/r
    vals.append((r,I,r*I))

assert abs(vals[-1][2]-float(coef)) < 1e-3
assert abs(float(Minf)-1698.102820718666) < 1e-9
assert abs(float(coef)-5.990514103593353) < 1e-12

print('VERIFY_OK')
print('R0', float(R0))
print('R1', float(R1))
print('kappa', float(kappa))
print('M_infinity', float(Minf))
print('rI_limit', float(coef))
for r,I,rI in vals:
    print('r', r, 'I', I, 'rI', rI)
