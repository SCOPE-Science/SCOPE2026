#!/usr/bin/env python3
"""Self-contained symbolic and numerical verification of a quintic oscillator crossover."""
import math
from scipy.integrate import quad
import sympy as sp

x,y,a,b=sp.symbols('x y a b',real=True)
# log-derivative of the Jacobi multiplier and potential derivative
assert sp.simplify(sp.diff(a*x**4/4,x)-a*x**3)==0
# d/dt [ exp(a*x^4/2)*y^2/2 + int_0^x exp(a*s^4/2)*(s+b*s^5)ds ] =0
# with xdot=y, ydot=-x-a*x^3*y^2-b*x^5
assert sp.simplify(sp.exp(a*x**4/2)*y*(-x-a*x**3*y**2-b*x**5)
                        +a*x**3*sp.exp(a*x**4/2)*y**3
                        +sp.exp(a*x**4/2)*(x+b*x**5)*y)==0

# In the large-amplitude scaled identity, eps=1/(b*A^4) and lambda=a*A^4.
def I(k,u,L):
    return quad(lambda v:v**k*math.exp(L*(v**4-1)/2),u,1,epsabs=3e-12,epsrel=3e-12)[0]

def period_scaled(L,epsilon):
    def ft(t):
        u=1-t*t
        return 4*math.sqrt(2)*t*math.exp(L*(u**4-1)/4)/math.sqrt(I(5,u,L)+epsilon*I(1,u,L))
    return quad(ft,0,1,epsabs=2e-9,epsrel=2e-9,limit=180)[0]

def crossover(L):return period_scaled(L,0)

lambdas=(0,0.1,0.5,1.5,5,15,35)
for L in lambdas:
    for u in (0,0.01,0.25,0.5,0.875,0.98):
        i1=I(1,u,L); i5=I(5,u,L)
        assert 0<i1<=3*i5*(1+1e-10),(L,u,i1/i5)
for L in lambdas:
    psi=crossover(L)
    for eps in (.00001,.01,.25,2):
        raw=period_scaled(L,eps)
        assert psi/math.sqrt(1+3*eps)-2e-7 <raw <psi+2e-7,(L,eps,raw,psi)
    print('L=',L,'crossover=',round(psi,10),'relative_large_alpha=',round(psi*math.sqrt(L)/(2*math.pi),8) if L else None)
assert all(crossover(s)>crossover(t) for s,t in zip(lambdas,lambdas[1:]))
psi0=2*math.sqrt(3)/3*float(sp.beta(sp.Rational(1,6),sp.Rational(1,2)))
assert abs(crossover(0)-psi0)<1e-7,(crossover(0),psi0)
print('psi_zero=',psi0)
print('CHECK_OK')
