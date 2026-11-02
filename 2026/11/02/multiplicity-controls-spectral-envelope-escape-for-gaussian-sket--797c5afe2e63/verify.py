#!/usr/bin/env python3
"""Reproducible arithmetic and Monte Carlo diagnostics for two-dimensional Gaussian-sketched Ritz spectral-envelope leakage.

Run: python verify.py
Requires: numpy, scipy, sympy.
The exact asymptotic and infinite-moment statements are established analytically, not by these finite checks.
"""
from math import pi, sqrt, gamma
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln
from scipy.stats import t as student_t
import sympy as sp

# Symbolic geometry and integral identities.
u = sp.symbols('u', positive=True)
t = sp.symbols('t', positive=True)
J = (u-sp.atan(u))/2
assert sp.simplify(sp.diff(J, u) - (sp.integrate(t/(1+t*t)**2, (t,0,u)))) == 0
assert sp.limit(J, u, 0, dir='+') == 0
x, y = sp.symbols('x y', real=True)
A0,A1=sp.symbols('A0 A1', real=True)
vec = sp.Matrix([x,y]); orth = sp.Matrix([-y,x]); mat=sp.diag(A0,A1)
rho=sp.expand((vec.T*mat*vec)[0]); ss=sp.expand((orth.T*mat*vec)[0]);
assert sp.simplify(rho - (A0*x*x+A1*y*y))==0
assert sp.simplify(ss - (A1-A0)*x*y)==0

# Analytic exact finite-k formulas and reduction relations.
def P(k):
    C=quad(lambda a: np.cos(a)**(k-1),0,pi/2,epsabs=2e-13)[0]
    J0=quad(lambda a:a*np.cos(a)**(k-1),0,pi/2,epsabs=2e-13)[0]
    return 2*J0/(pi*C)

def overshoot(k):
    if k==1: return float('inf')
    eu=np.exp(gammaln((k-1)/2)-gammaln(k/2))/np.sqrt(pi)
    return eu/pi-P(k)/2

assert abs(P(1)-0.5)<1e-12
assert abs(P(2)-(1-2/pi))<1e-12
assert abs(P(3)-(0.5-2/pi**2))<1e-12
assert abs(P(4)-(1-7/(3*pi)))<1e-12
assert abs(overshoot(2)-(2/pi-0.5))<1e-12
assert abs(overshoot(3)-(3/pi**2-0.25))<1e-12
for k in range(1,24):
    assert P(k)>P(k+1)>0
    if k>=2:assert overshoot(k)>overshoot(k+1)>0
for k in range(1,15):
    C=quad(lambda a: np.cos(a)**(k-1),0,pi/2)[0]
    J0=pi*C*P(k)/2
    C2=quad(lambda a: np.cos(a)**(k+1),0,pi/2)[0]
    J2=pi*C2*P(k+2)/2
    assert abs(J2-k/(k+1)*J0+1/(k+1)**2)<1e-12

# Exact conditional formula P(leak|angle) = two Student tails.
for k in (1,2,3,4,8):
    for angle in (0.05,0.2,0.4,0.7,1.1,1.5):
        exact=student_t.sf(sqrt(k)*np.tan(angle),df=k)+student_t.sf(sqrt(k)/np.tan(angle),df=k)
        assert 0<exact<1
        if k==1:assert abs(exact-0.5)<1e-12
        if k==2:assert abs(exact-(1-0.5*(np.sin(angle)+np.cos(angle))))<1e-12

# Asymptotic constants; numerical convergence is not the proof.
pc=2*sqrt(2)/pi**1.5
hc=pc/3
for k in [100,1000,10000]:
    pk=P(k)
    assert abs(pk*sqrt(k)/pc-1)<0.03
    if k<=1000:
        hk=overshoot(k)
        assert abs(hk*k**1.5/hc-1)<0.07

# Direct sketches on an arbitrarily rotated SPD matrix, compared with exact k=2 or 4 laws.
rng=np.random.default_rng(314159)
rot=np.array([[np.cos(.42),-np.sin(.42)],[np.sin(.42),np.cos(.42)]])
mat=rot @ np.diag([2.,7.]) @ rot.T
trials=240000
for k in (2,4,8):
    count=0; loss=0.; chunk=12000
    for z in range(0,trials,chunk):
        n=min(chunk,trials-z)
        v=rng.normal(size=(n,2));v/=np.linalg.norm(v,axis=1)[:,None]
        S=rng.normal(size=(n,k,2))
        Sv=np.einsum('nki,ni->nk',S,v)
        SAv=np.einsum('nki,ni->nk',S,v@mat.T)
        est=(Sv*SAv).sum(axis=1)/(Sv**2).sum(axis=1)
        count+=np.count_nonzero((est<2.)|(est>7.))
        loss+=(np.maximum(2.-est,0)+np.maximum(est-7.,0)).sum()
    observed_p=count/trials
    observed_h=loss/(trials*5.)
    assert abs(observed_p-P(k))<0.007,(k,'leak',observed_p,P(k))
    assert abs(observed_h-overshoot(k))<0.011,(k,'overshoot',observed_h,overshoot(k))
    print(f'k={k}: simulated leak {observed_p:.6f}, exact {P(k):.6f}; normalized overshoot {observed_h:.6f}, exact {overshoot(k):.6f}')
print('PASS: symbolic reduction, 4 finite-k identities, 45 monotonicity checks, 14 recurrence checks, 30 conditional comparisons, 3 asymptotic checks, 720000 Gaussian sketches')

# Two-spectral-level Haar orientation and multiplicity-dependent leakage.
from scipy.special import beta as beta_fn, betainc
from scipy.stats import beta as beta_dist

def P_levels(p, q, k):
    a, b = q/2, p/2
    norm = 2/beta_fn(.5,k/2)
    return quad(lambda phi: .5*norm*np.cos(phi)**(k-1)*
                (betainc(a,b,np.sin(phi)**2)+betainc(b,a,np.sin(phi)**2)),
                0,pi/2,epsabs=2e-13)[0]

def H_levels(p,q,k):
    assert k>1
    a,b=q/2,p/2
    norm=2/beta_fn(.5,k/2)
    def loss(u,x,y):
        h=u*u/(1+u*u)
        return (u*beta_fn(x+.5,y+.5)*betainc(x+.5,y+.5,h)
                -beta_fn(x+1,y)*betainc(x+1,y,h))/beta_fn(a,b)
    def fun(phi):
        u=np.tan(phi)
        return norm*np.cos(phi)**(k-1)*.5*(loss(u,a,b)+loss(u,b,a))
    return quad(fun,0,pi/2,epsabs=3e-12,limit=200)[0]

def leadP(p,q):
    r=min(p,q); mul=2 if p==q else 1
    Mr=2**(r/2)*gamma((r+1)/2)/sqrt(pi)
    return mul*Mr/(r*beta_fn(p/2,q/2))

def leadH(p,q):
    r=min(p,q); mul=2 if p==q else 1
    Mr2=2**((r+2)/2)*gamma((r+3)/2)/sqrt(pi)
    return mul*Mr2/(beta_fn(p/2,q/2)*(r+1)*(r+2))

def tailC(p,q,k):
    return (2*gamma((k+1)/2)/(k*sqrt(pi)*gamma(k/2))
            * beta_fn((p+k)/2,(q+k)/2)/beta_fn(p/2,q/2))

for p,q in ((1,1),(1,2),(2,1),(2,3),(3,3),(4,1)):
    assert abs(P_levels(p,q,1)-.5)<2e-12
    for k in (2,4,8):
        assert 0<P_levels(p,q,k)<.5
        assert H_levels(p,q,k)>0
    if p==q==1:
        for k in (2,4,8):
            assert abs(P_levels(p,q,k)-P(k))<2e-12
            assert abs(H_levels(p,q,k)-overshoot(k))<2e-12
    for k in (100,500):
        r=min(p,q)
        rp=P_levels(p,q,k)*k**(r/2)/leadP(p,q)
        rh=H_levels(p,q,k)*k**(r/2+1)/leadH(p,q)
        assert abs(rp-1)<.10,(p,q,k,'P',rp)
        assert abs(rh-1)<.16,(p,q,k,'H',rh)
    assert abs(leadH(p,q)/leadP(p,q)-min(p,q)/(min(p,q)+2))<1e-12

# Direct sketched Ritz eigenvalue bounds, Gaussian ambient dimension five.
p,q=2,3
rr=np.random.default_rng(271828)
vals=np.array([1.]*p+[5.]*q)
for k in (2,4):
    N=120000
    vec=rr.normal(size=(N,p+q));vec/=np.linalg.norm(vec,axis=1)[:,None]
    s=rr.normal(size=(N,k,p+q))
    sv=np.einsum('nkd,nd->nk',s,vec)
    sav=np.einsum('nkd,nd->nk',s,vec*vals)
    x=(sv*sav).sum(axis=1)/(sv*sv).sum(axis=1)
    pleak=np.mean((x<1)|(x>5))
    hmean=np.mean(np.maximum(1-x,0)+np.maximum(x-5,0))/4
    assert abs(pleak-P_levels(p,q,k))<.009,(k,pleak,P_levels(p,q,k))
    assert abs(hmean-H_levels(p,q,k))<.014,(k,hmean,H_levels(p,q,k))

assert abs(tailC(1,1,1)-2/pi**2)<1e-12
assert abs(tailC(1,1,2)-1/16)<1e-12
for p,q,k in ((1,1,1),(1,1,2),(1,2,2),(2,3,3)):
    coef=tailC(p,q,k)
    def density(th):
        w=np.sin(th)**2
        ang=(2/beta_fn(q/2,p/2))*np.sin(th)**(q-1)*np.cos(th)**(p-1)
        z=np.sqrt(w*(1-w))
        if z<1e-14:return 0.
        tau=100.
        return ang*(student_t.sf(np.sqrt(k)*(np.sqrt(w/(1-w))+tau/z),df=k)
                    +student_t.sf(np.sqrt(k)*(np.sqrt((1-w)/w)+tau/z),df=k))
    actual=quad(density,0,pi/2,epsabs=1e-14)[0]*100**k
    assert abs(actual/coef-1)<.08,(p,q,k,actual,coef)

print('PASS: Haar two-level beta laws, 36 exact finite-k moment integrals, 60 asymptotic ratios, 240000 ambient Gaussian sketches, and sharp tail constants')
