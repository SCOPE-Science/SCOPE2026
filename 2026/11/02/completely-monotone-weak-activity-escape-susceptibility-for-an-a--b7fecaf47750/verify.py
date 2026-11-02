"""Independent checks for the weak-activity disk exit susceptibility.

Run: python verify.py
Uses scipy, sympy, mpmath.  This is a finite numerical/algebraic
check, not a substitute for the analytic PDE and resolvent proof.
"""
import math
import sympy as sp
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp, quad

mp.mp.dps = 50

def coefficient(g, s):
    g = mp.mpf(g)
    s = mp.mpf(s)
    if g == 0:
        return (1-s*s)**2/128
    k = mp.sqrt(g)
    return ((1-s*s)/2 - (mp.besseli(0,k)-mp.besseli(0,k*s))
            /(k*mp.besseli(1,k)))/(4*g)

def radial_shooting(g):
    """Solve (-Delta_4 + g)v=1/2 with v(1)=0 by independent IVPs."""
    eps = 1.e-6
    def solve(f0):
        a = g*f0-0.5
        # v''(0)=(g*v(0)-1/2)/4 for radial 4D Laplacian
        y0 = [f0+a*eps*eps/8, a*eps/4]
        def ode(t,y):
            return [y[1], g*y[0]-0.5-3*y[1]/t]
        return solve_ivp(ode, (eps,1), y0, rtol=1.e-11,
                         atol=1.e-13, dense_output=True)
    a=solve(0); b=solve(1)
    c = -a.y[0,-1]/(b.y[0,-1]-a.y[0,-1])
    return lambda t: a.sol(t)[0]+c*(b.sol(t)[0]-a.sol(t)[0])

r=sp.symbols('r',positive=True)
u0=r*(1-r*r)/16
assert sp.simplify(-sp.diff(u0,r,2)-sp.diff(u0,r)/r+u0/r**2-r/2)==0
w0=-(1-r*r)**2/128
assert sp.simplify(sp.diff(w0,r,2)+sp.diff(w0,r)/r
                   +(sp.diff(-u0,r)+(-u0)/r)/2)==0
assert u0.subs(r,1)==0 and w0.subs(r,1)==0
print('PASS: zero-angular-diffusion polynomial and second-order PDE')

checks=0
for g in [0.07,0.4,1,3,16]:
    f=radial_shooting(g)
    for s in [0,0.2,0.5,0.75,0.9]:
        approx=quad(lambda t:0.5*t*f(t),s,1,epsabs=5.e-11)[0]
        exact=float(coefficient(g,s))
        assert abs(approx-exact)<3.e-8,(g,s,approx,exact)
        checks+=1
print(f'PASS: {checks} independent four-dimensional radial ODE integral comparisons')

sign_checks=0
for g in ['0.1','1','6','25']:
    for s in ['0','0.2','0.7']:
        f=lambda z: coefficient(z,s)
        for n in range(5):
            d=mp.diff(f,mp.mpf(g),n)
            assert (-1)**n*d > 0, (g,s,n,d)
            sign_checks+=1
print(f'PASS: {sign_checks} complete-monotonicity derivative sign spot-checks')

for s in ['0','0.3','0.8']:
    x=mp.mpf(s)
    assert abs(coefficient(mp.mpf('1.e-8'),x)-coefficient(0,x))<mp.mpf('1.e-8')
    g=mp.mpf(100000)
    assert abs(g*coefficient(g,x)-(1-x*x)/8)<mp.mpf('0.001')
print('PASS: small- and large-angular-diffusion limits')
