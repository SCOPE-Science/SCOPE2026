#!/usr/bin/env python3
"""Reproducibility checks for quadratic orthogonal projection on weighted balls.

Only finite-dimensional rational identities and finite numerical quadratures are tested.
The dimension-asymptotic theorem is proved analytically in RESULT.md.
Requires Python 3, sympy, scipy and numpy.
"""
from fractions import Fraction
from itertools import combinations_with_replacement
import math
import numpy as np
import sympy as sp
from scipy.special import betainc, roots_jacobi, gamma

assertions = 0

def ck(value, msg):
    global assertions
    assert value, msg
    assertions += 1

def moment(powers, k):
    """A uniform Jacobi-weighted ball moment, exact for rational k."""
    if any(n % 2 for n in powers):
        return sp.Rational(0)
    m = sum(powers)//2
    d = len(powers)
    out = sp.S.One
    for n in powers:
        out *= sp.rf(sp.Rational(1,2), n//2)
    return sp.cancel(out/sp.rf(sp.Rational(d,2)+k,m))

def integrate_poly(poly, ys, k):
    pp = sp.Poly(sp.expand(poly), *ys)
    return sp.factor(sum(coeff*moment(exps,k) for exps,coeff in pp.terms()))

def kernel(x, ys, k):
    d = len(ys)
    D = sp.Integer(d) + 2*k
    m = sp.Rational(d,1)/D
    xx = sum(v*v for v in x)
    yy = sum(v*v for v in ys)
    xy = sum(v*w for v,w in zip(x,ys))
    return (sp.S.One + D*xy + D*(D+2)/2 * (xy**2-xx*yy/d)
            + D**2*(D+2)/(4*d*k)*(xx-m)*(yy-m))

for d in (2,3,4,5):
    ys = sp.symbols('y0:'+str(d))
    xx = [sp.Rational(i+1,i+3) / (2*d) for i in range(d)]
    for k in (sp.Rational(1,4),sp.Rational(1,2),sp.S.One,sp.Rational(5,2)):
        K=kernel(xx,ys,k)
        test_polys = [sp.S.One] + list(ys) + [ys[i]*ys[j] for i in range(d) for j in range(i,d)]
        for p in test_polys:
            observed=integrate_poly(K*p, ys,k)
            expected=sp.expand(p.subs({y:v for y,v in zip(ys,xx)}))
            ck(sp.simplify(observed-expected)==0,(d,k,p,observed,expected))
        s0=(d+2)/(d+2*k+2)
        Bm=(d+2*k)*(d+2*k+2)/(4*k)
        K0=kernel([sp.S.Zero]*d,ys,k)
        ck(sp.expand(K0 - Bm*(s0 -sum(y*y for y in ys))) ==0,(d,k,'center'))

# Compare exact center integral to independent one-dimensional beta quadrature.
from scipy.integrate import quad
for d in (2,3,7,20,80):
    a=d/2
    for k in (.2,.5,1.,2.,4.):
        D=d+2*k
        m=d/D
        s0=(d+2)/(D+2)
        Bm=D*(D+2)/(4*k)
        exact=2*Bm*(s0*betainc(a,k,s0)-m*betainc(a+1,k,s0))-1
        logbeta=math.lgamma(a)+math.lgamma(k)-math.lgamma(a+k)
        def density(s):
            if s<=0 or s>=1: return 0.
            return math.exp((a-1)*math.log(s)+(k-1)*math.log1p(-s)-logbeta)
        num=quad(lambda s: Bm*abs(s0-s)*density(s),0,s0,epsabs=2e-9)[0]
        num+=quad(lambda s: Bm*abs(s0-s)*density(s),s0,1,epsabs=2e-9)[0]
        ck(abs(num-exact)<2e-7,(d,k,num,exact))
        if k==1:
            simple=(d+4)*((d+2)/(d+4))**(d/2+1)-1
            ck(abs(simple-exact)<2e-7,('uniform center',d,simple,exact))

# Radial Gamma absolute-deviation formula, location-phase ordering.
from scipy.integrate import quad
Cb=math.sqrt(2/(math.pi*math.e))
for k in (.1,.2,.3,.5,.75,1,2,5,20):
    Cc=k**k*math.exp(-k)/gamma(k+1)
    if k<.5: ck(Cc>Cb,('center dominated',k,Cc))
    if k>.5: ck(Cc<Cb,('boundary dominated',k,Cc))
    if k==.5: ck(abs(Cc-Cb)<1e-14,('critical equality',Cc,Cb))
    def integrand(t):
        return abs(t-k)*math.exp((k-1)*math.log(t)-t-math.lgamma(k))/(2*k) if t else 0.
    g=quad(integrand,0,k,epsabs=1e-11)[0] + quad(integrand,k,max(50.,k+20*math.sqrt(k)+80),epsabs=1e-11)[0]
    ck(abs(Cc-g)<5e-9,('gamma deviation',k,Cc,g))

# Independent high-dimensional angular/radial Monte Carlo sanity checks.
rng=np.random.default_rng(20261015)
for d in (40,150,500):
    N=60000
    cosangle=rng.choice([-1,1],N)*np.sqrt(rng.beta(.5,(d-1)/2,size=N))
    for k in (.25,.5,1.,2.):
        s=rng.beta(d/2,k,size=N)
        D=d+2*k; m=d/D
        B=D*D*(D+2)/(4*d*k)
        A=D*(D+2)/2
        yy=s*cosangle*cosangle
        norms=[]
        for r in (0.,.5,1.):
            kernelvalues=1+D*r*np.sqrt(s)*cosangle + A*r*r*(yy-s/d)+B*(r*r-m)*(s-m)
            norms.append(float(np.mean(np.abs(kernelvalues)))/d)
        Cc=k**k*math.exp(-k)/gamma(k+1)
        limit=lambda t: (1-t)*Cc+t*Cb
        # Convex endpoint upper bound holds asymptotically, loose finite margin.
        ck(norms[1] < max(Cc,Cb)+.15,('interior upper bound',d,k,norms))
        ck(abs(norms[0]-Cc)<.13,('center convergence sanity',d,k,norms))
        ck(abs(norms[2]-Cb)<.13,('boundary convergence sanity',d,k,norms))

print(f'PASS: {assertions} independent finite/exact computations.')
