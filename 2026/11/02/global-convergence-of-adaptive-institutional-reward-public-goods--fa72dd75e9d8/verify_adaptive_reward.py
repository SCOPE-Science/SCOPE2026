#!/usr/bin/env python3
"""Reproduce exact Lyapunov and linearization identities for adaptive-reward games.

Run: python verify_adaptive_reward.py
Dependencies: sympy>=1.12, scipy>=1.11 (optional for trajectories)
"""
from fractions import Fraction
import math
import sympy as sp

x,a,alpha,beta,u,epsilon,delta,kappa,ss,aa = sp.symbols(
    'x a alpha beta u epsilon delta kappa ss aa',positive=True)
X=x*(1-x)
A=(a-alpha)*(beta-a)
H=u-(u+1)*x
# The symbolic gradient of the Bernoulli relative entropy.
xs=u/(1+u)
p=(a-alpha)/(beta-alpha)
ps=(aa-alpha)/(beta-alpha)
D1=xs*sp.log(xs/x)+(1-xs)*sp.log((1-xs)/(1-x))
D2=ps*sp.log(ps/p)+(1-ps)*sp.log((1-ps)/(1-p))
assert sp.simplify(sp.diff((u+1)*D1,x)+H/X)==0
assert sp.simplify(sp.diff(D2,a)-(a-aa)/A)==0

for N in range(2,13):
    S=sum((1-x)**j for j in range(N))
    dS=sp.diff(S,x)
    assert sp.simplify(dS+sum(j*(1-x)**(j-1) for j in range(1,N)))==0
    xv=sp.Rational(2,3)
    sv=S.subs(x,xv)
    dv=sp.Rational(1,5)
    kv=sp.Rational(2,5)
    av=kv/(dv*sv)
    ev=sp.Rational(3,2)
    uv=sp.Integer(2)
    Vx=-H/X
    Va=delta*ss/epsilon*(a-aa)/A
    dx=X/epsilon*(delta*a*S-kappa)
    da=A*H
    deriv=(Vx*dx+Va*da).subs({u:uv,delta:dv,epsilon:ev,kappa:kv,ss:sv,aa:av})
    target=(dv*a/ev)*H.subs(u,uv)*(sv-S)
    assert sp.simplify(deriv-target)==0, N
print('PASS: exact Bernoulli-relative-entropy gradient and drift identities (N=2,...,12)')

# Source paper's illustrated N=5 reward regime, with all quantities exact.
N=5; S=sum((1-x)**j for j in range(N)); xstar=sp.Rational(2,3)
sv=S.subs(x,xstar); alpha0=sp.Rational(1,2); beta0=sp.Integer(3)
D=sp.Rational(1,5); K=sp.Rational(2,5); U=2
astar=K/(D*sv)
assert alpha0<astar<beta0
P=sp.factor(D*astar*xstar*(1-xstar)*(-sp.diff(S,x).subs(x,xstar)))
Q=sp.factor(D*xstar*(1-xstar)*sv*(U+1)*(astar-alpha0)*(beta0-astar))
ecritical=sp.factor(P**2/(4*Q))
assert P>0 and Q>0 and ecritical>0
assert sp.factor(ecritical-sp.Rational(4176,283745))==0
print('PASS: N=5 example x*=',xstar,'a*=',astar,'P=',P,'Q=',Q,'epsilon_focus=',ecritical)

for E in (sp.Rational(1,1000),sp.Rational(1,100),sp.Rational(1,10),sp.Rational(3,1)):
    discr=sp.sign(P**2-4*Q*E)
    assert (discr>0)==(E<ecritical)
    assert (discr<0)==(E>ecritical)
print('PASS: exact node/focus classification at four adjustment timescales')

try:
    from scipy.integrate import solve_ivp
    from scipy.special import expit, logit
    import numpy as np
    sf=sp.lambdify(x,S,'numpy')
    for ev in (0.001, 0.05, 2.0):
        for x0,a0 in ((0.1,0.6),(0.8,2.8),(0.45,1.0)):
            def g(t,z):
                xx=expit(z[0]); ar=float(alpha0)+(float(beta0)-float(alpha0))*expit(z[1]);
                return [(float(D)*ar*sf(xx)-float(K))/ev,
                        (float(beta0)-float(alpha0))*(U-(U+1)*xx)]
            z0=[logit(x0),logit((a0-float(alpha0))/(float(beta0)-float(alpha0)))]
            sol=solve_ivp(g,[0,4000],z0,method='Radau',rtol=1e-9,atol=1e-11)
            assert sol.success, (ev,x0,a0,sol.message)
            xx=expit(sol.y[0,-1]); ar=float(alpha0)+(float(beta0)-float(alpha0))*expit(sol.y[1,-1]);
            assert max(abs(xx-float(xstar)),abs(ar-float(astar)))<5e-7,(ev,x0,a0,xx,ar)
    print('PASS: 9 numerical log-odds trajectories approach the analytical equilibrium')
except ImportError:
    print('SKIP: scipy optional trajectory illustrations (exact symbolic checks completed)')
