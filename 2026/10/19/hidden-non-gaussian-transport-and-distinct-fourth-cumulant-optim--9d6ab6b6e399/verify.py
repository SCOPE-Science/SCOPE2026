#!/usr/bin/env python3
"""Algebraic and renewal-quadrature checks for Maxwellian velocity refresh."""
import math
import sympy as sp
from scipy.integrate import quad, solve_ivp

r, g, s2, t = sp.symbols('r g s2 t', positive=True)
a1, a2 = g+r, 2*g+r
K = 24*s2**2*r/(a1**3*a2)
L = 6*r/(a1*a2)
checks = 0

def ok(condition, name):
    global checks
    assert bool(condition), name
    checks += 1

# Exact exponential-cycle renewal reward: E[T]=1/r and
# q(T)/2 = s2*(T/g-(1-exp(-g*T))/g**2).
A = r/(g*(g+r)); B = 1/g**2
ET2 = 2/r**2
ET = 1/r
ETexp = r/(r+g)**2
E1exp = 1-r/(r+g)
E1exp2 = 1-2*r/(r+g)+r/(r+2*g)
EQ2centered = sp.factor(A*A*ET2 - 2*A*B*(ET-ETexp)+B*B*E1exp2)
ok(sp.simplify(EQ2centered - 2/(a1**3*a2)) == 0, 'renewal square')
ok(sp.simplify(12*r*s2**2*EQ2centered-K) == 0, 'renewal cumulant rate')
ok(sp.simplify(K/(2*s2/a1)**2-L) == 0, 'standardized coefficient')

# Hermite spectral relaxation and cumulant expansion.
b1 = sp.sqrt(s2)/a1
b2 = sp.sqrt(s2)**2/(a1*a2)
lambda2 = s2/a1
b3 = sp.factor((2*sp.sqrt(s2)*b2-lambda2*b1)/a1)
ok(sp.simplify(24*sp.sqrt(s2)*b3-K) == 0,'Hermite fourth cumulant')
ok(sp.factor(sp.diff(K,r)*a1**4*a2**2/(24*s2**2)) == (2*g**2-4*g*r-3*r**2), 'absolute optimum derivative')
ok(sp.factor(sp.diff(L,r)*a1**2*a2**2/6) == (2*g**2-r**2), 'normalized optimum derivative')
r_abs = g*(sp.sqrt(10)-2)/3
r_std = sp.sqrt(2)*g
ok(sp.simplify(sp.diff(K,r).subs(r,r_abs)) == 0,'absolute optimal point')
ok(sp.simplify(sp.diff(L,r).subs(r,r_std)) == 0,'normalized optimal point')
ok(float((r_std-r_abs).subs(g,1))>0, 'distinct ordered optima')

# Independent numeric quadrature of the stochastic-cycle square.
for gg, rr, ss in [(0.5,0.25,1),(1,2,0.3),(2,0.1,4),(3,5,0.8)]:
    aa=rr/(gg*(rr+gg)); bb=1/(gg*gg)
    integral,_=quad(lambda x:rr*math.exp(-rr*x)*(aa*x-bb*(-math.expm1(-gg*x)))**2,
                   0, math.inf,epsabs=2e-11,epsrel=2e-11)
    expected=2/((rr+gg)**3*(rr+2*gg))
    ok(abs(integral-expected)<=4e-9*max(expected,0.001),'cycle quadrature')

# Direct ODE of polynomial moments of the marked-velocity process.
# State (A=E[XV], B=E[X²(V²-s2)], M=E[X²],
#        D=E[X³V], F=E[X⁴]).
for gg, rr, ss in [(1,1,1),(2,0.2,0.8),(0.7,4,3)]:
    aa1=gg+rr;aa2=2*gg+rr
    def ode(tt,y):
        A,B,M,D,F=y
        return (ss-aa1*A, 4*ss*A-aa2*B, 2*A,3*ss*M+3*B-aa1*D,4*D)
    for tt in [0.2, 1.0,3.0,8.0]:
        sol=solve_ivp(ode,(0,tt),[0]*5,rtol=2e-11,atol=2e-12)
        A,B,M,D,F=sol.y[:,-1]
        q4=F-3*M*M
        var_exact=2*ss*(tt/aa1+math.expm1(-aa1*tt)/aa1**2)
        ok(abs(M-var_exact)<2e-8*max(1,M),'variance by moments')
        ok(q4>1e-10,'finite-time positive fourth cumulant')

# Conditional covariance within a segment is Gaussian; splitting strictly lowers
# integrated variance for every interior split.
for gg in [0.3,1,3]:
    def q(l):return 2*(l/gg+math.expm1(-gg*l)/(gg*gg))
    for tt in [0.2,1,5]:
        for frac in [0.1,0.37,0.8]:
            ok(q(tt)>q(frac*tt)+q((1-frac)*tt),'strict variance splitting')
print(f'{checks} reproducibility assertions passed')
