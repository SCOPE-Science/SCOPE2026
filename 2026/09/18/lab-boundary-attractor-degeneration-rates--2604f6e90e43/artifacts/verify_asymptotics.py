#!/usr/bin/env python3
"""Exact/algebraic and high-precision checks for the LAB boundary attractor.

Requires Python 3 and SymPy. Symbolic lines are exact. Numerical iteration is
only a check of the analytic statements in RESULT.md.
"""
import sympy as sp
from mpmath import mp

mp.dps = 80

t, c = sp.symbols('t c', positive=True)
p = 2*c*t**3 - 3*t**2 + 1
q = (1-t**2)/t
x = (1-c*t)/q
y = (t-c)/q
print("fixed_point_squared_residual =", sp.factor((1/t-t)**2-(1+t**2-2*c*t)))
print("angle_double_residual =", sp.factor(y-(2*x**2-1)))
print("angle_double_residual_div_p =", sp.factor((y-(2*x**2-1))/p))

# Source choice c=7/8.
c0 = sp.Rational(7,8)
p0 = sp.factor(p.subs(c,c0))
print("source_fixed_polynomial =", p0)
roots = sp.nroots(sp.together(4*p0), n=70, maxsteps=100)
tau_sp = [r for r in roots if abs(sp.im(r)) < sp.Float('1e-60') and sp.Rational(3,4) < sp.re(r) < sp.Rational(4,5)][0]
tau = mp.mpf(str(sp.N(sp.re(tau_sp), 70)))
s = mp.sqrt(15)/8
print("tau =", mp.nstr(tau, 40))
print("1/tau =", mp.nstr(1/tau, 40))
print("tau^2 =", mp.nstr(tau*tau, 40))


def F(tv, bv, cv=mp.mpf(7)/8):
    sv2 = 1-cv*cv
    Q = mp.sqrt(1+tv*tv-2*cv*tv+sv2*tv*tv*bv*bv)
    return 1/(tv+Q)


def iterate(t0, b0, cv=mp.mpf(7)/8, N=180):
    sv = mp.sqrt(1-cv*cv)
    tv, bv = mp.mpf(t0), mp.mpf(b0)
    rows=[]
    for n in range(N+1):
        Q = mp.sqrt(1+tv*tv-2*cv*tv+(1-cv*cv)*tv*tv*bv*bv)
        a = tv*bv
        W = bv*Q
        rin = a*bv*sv/(a+bv+a*bv*sv+W)
        h = mp.sqrt(1+bv*bv)
        phi = mp.atan(a)
        rows.append((n,tv,bv,a,rin,h,phi))
        tv,bv = F(tv,bv,cv), tv*bv
    return rows

rows = iterate(mp.mpf(3)/4, mp.mpf(1)/4)
C = rows[-1][2]/tau**rows[-1][0]
q0 = 1/tau-tau
K = -(mp.mpf(15)/64)*tau**4/(q0*(2*tau**2+1))
kin = tau*tau*s/(1+tau)
print("source_C =", mp.nstr(C, 40))
print("K_for_(t-tau)/b^2 =", mp.nstr(K, 40))
print("inradius_coefficient_r_over_b =", mp.nstr(kin, 40))
print("aspect_prefactor =", mp.nstr(1/(C*kin), 40))
for n in (20,40,80,160):
    _,tv,bv,a,rin,h,phi=rows[n]
    print(
        "n=%3d  b/tau^n=%s  (t-tau)/b^2=%s  phi/(C*tau^(n+1))=%s  "
        "r/(C*kin*tau^n)=%s  (h-1)/(0.5*C^2*tau^(2n))=%s"
        % (n, mp.nstr(bv/tau**n,16), mp.nstr((tv-tau)/(bv*bv),16),
           mp.nstr(phi/(C*tau**(n+1)),16), mp.nstr(rin/(C*kin*tau**n),16),
           mp.nstr((h-1)/(mp.mpf('0.5')*C*C*tau**(2*n)),16))
    )

cos_pb=(1-mp.mpf(7)/8*tau)/q0
cos_pa=(tau-mp.mpf(7)/8)/q0
th_pb=mp.acos(cos_pb); th_pa=mp.acos(cos_pa)
print("theta_PB_limit_deg =", mp.nstr(th_pb*180/mp.pi,30))
print("theta_PA_limit_deg =", mp.nstr(th_pa*180/mp.pi,30))
print("theta_PA_minus_2theta_PB =", mp.nstr(th_pa-2*th_pb,20))

# General-rate examples: choose tau, recover c=(3 tau^2-1)/(2 tau^3),
# and perturb a small-b initial condition near the boundary fixed point.
for target_tau in [mp.mpf('0.72'), mp.mpf('0.85'), mp.mpf('0.95')]:
    cv=(3*target_tau**2-1)/(2*target_tau**3)
    rr=iterate(target_tau+mp.mpf('0.01')*(1-target_tau),mp.mpf('0.02'),cv,140)
    print("general tau,c,t_140 =", mp.nstr(target_tau,12), mp.nstr(cv,12), mp.nstr(rr[-1][1],30))
