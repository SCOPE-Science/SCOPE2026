#!/usr/bin/env python3
"""Supplementary checks for the centered geodesic-sphere asymptotics."""
import math
import sympy as sp

r, kap = sp.symbols('r kap', positive=True)
series = sp.series((r/sp.tan(r))**kap, r, 0, 6)
quad = sp.expand(series.removeO()).coeff(r, 2)
assert sp.simplify(quad + kap/3) == 0

# Algebraic conversion from E asymptotics to y=(1+E/L)^(-1/a).
a, B, L = sp.symbols('a B L', positive=True)
z = sp.symbols('z')
y_exp = sp.series((1+z)**(-1/a), z, 0, 2).removeO()
assert sp.simplify(y_exp - (1-z/a)) == 0

# Representative numerical integrations with a dependency-free RK4 solver.
def rhs(rho, aa, kkalpha, gamma0=1.0):
    A = (rho / math.tan(rho))**kkalpha
    return -gamma0 * rho**(aa+1) * A

def rk4(r0, aa, kkalpha, tmax, steps):
    h=tmax/steps
    rr=r0
    t=0.0
    for _ in range(steps):
        k1=rhs(rr,aa,kkalpha)
        k2=rhs(rr+0.5*h*k1,aa,kkalpha)
        k3=rhs(rr+0.5*h*k2,aa,kkalpha)
        k4=rhs(rr+h*k3,aa,kkalpha)
        rr += h*(k1+2*k2+2*k3+k4)/6
        t += h
    return rr

def predicted_subcritical(r0, aa, kkalpha, N=300000):
    # Midpoint quadrature for the convergent coefficient integral, aa<2.
    h=r0/N
    s=0.0
    for j in range(N):
        x=(j+0.5)*h
        A=(x/math.tan(x))**kkalpha
        s += ((A-1)/(x**(aa+1)*A))*h
    Einf=r0**(-aa)-1+aa*s
    return -Einf/aa

# a=1: limit lambda^a(y-1)=C(r0).
r0=0.7; aa=1.0; ka=1.3; Bnum=ka/3
rho=rk4(r0,aa,ka,tmax=2500.0,steps=250000)
lam=(1+aa*2500.0)**(1/aa)
y=lam*rho
obs=lam**aa*(y-1)
pred=predicted_subcritical(r0,aa,ka,N=100000)
assert abs(obs-pred) < 3e-3, (obs,pred)

# a=2 resonance: ratio tends to B.
r0=0.9; aa=2.0; ka=1.2; Bnum=ka/3
rho=rk4(r0,aa,ka,tmax=5000.0,steps=250000)
lam=(1+aa*5000.0)**(1/aa)
y=lam*rho
obs=lam**2*(y-1)/math.log(lam)
assert abs(obs-Bnum) < 0.05, (obs,Bnum)

# a=3: lambda^2(y-1) tends to B/(a-2).
r0=0.7; aa=3.0; ka=1.1; Bnum=ka/3
rho=rk4(r0,aa,ka,tmax=5000.0,steps=250000)
lam=(1+aa*5000.0)**(1/aa)
y=lam*rho
obs=lam**2*(y-1)
pred=Bnum/(aa-2)
assert abs(obs-pred) < 0.12, (obs,pred)

print('PASS')
print(series)
print('subcritical observed/predicted', obs if aa<2 else 'see prior assertion')
