#!/usr/bin/env python3
"""Check algebraic identities and numerical matrices for helm spectral-gap allocations.

Run: python verify.py (requires numpy and sympy).
Finite tests corroborate but do not prove the infinite-family theorem.
"""
import math
import numpy as np
import sympy as sp

count=0

def check(pred,msg):
    global count
    assert pred,msg
    count+=1

c,a,b,n,t,B=sp.symbols('c a b n t B',real=True)
z=sp.symbols('z')
den=(2*n+1)*c-(n+1)
h=(2*c-1)/den
g=(2*c-1)/(c-1)
rad=sp.Matrix([[n*a,-n*a,0],[-a,a+c,-c],[0,-c,c]])
cp=sp.factor(rad.charpoly(z).as_expr())
check(sp.simplify(cp-z*(z*z-((n+1)*a+2*c)*z+(2*n+1)*a*c))==0,'radial charpoly')
check(sp.simplify(sp.diff(h,c)+1/den**2)==0,'radial derivative')
check(sp.simplify(sp.diff(g,c)+1/(c-1)**2)==0,'transverse derivative')
check(sp.simplify(((n+1)*h+2*c-1)*1-((2*n+1)*h*c))==0,'radial boundary')

rng=np.random.default_rng(20261015)
def critical_delta(k): return 2*(1-math.cos(2*math.pi/k))
def objective(n,t):
    delta=critical_delta(n)
    beta=t/delta
    if beta>=1:
        cc,aa,bb=2.,3.,0.
        low=3/(3*n+1)
    else:
        def derivative(y):
            return 1-beta/(y-1)**2-(1-beta)/(((2*n+1)*y-(n+1))**2)
        lo=1+1e-11;hi=3.
        for _ in range(100):
            mid=(lo+hi)/2
            if derivative(mid)>0:hi=mid
            else:lo=mid
        cc=(lo+hi)/2
        aa=(2*cc-1)/((2*n+1)*cc-(n+1))
        bb=((2*cc-1)/(cc-1)-aa)/delta
        low=aa
        check(abs(derivative(cc))<1e-9,'stationary derivative')
    return (aa,bb,cc,n*(aa+t*bb+cc),low)

def lap(n,aa,bb,cc):
    L=np.zeros((2*n+1,2*n+1))
    def edge(x,y,w):
        L[x,x]+=w;L[y,y]+=w;L[x,y]-=w;L[y,x]-=w
    for j in range(n):
        edge(0,1+j,aa)
        edge(1+j,1+(j+1)%n,bb)
        edge(1+j,1+n+j,cc)
    return L

for nn in range(5,19):
    dd=critical_delta(nn)
    for tt in [0.04*dd,0.2*dd,0.7*dd,0.999*dd,dd,1.001*dd,1.9*dd,3.0*dd]:
        aa,bb,cc,C,low=objective(nn,tt)
        check(abs(nn*(aa+tt*bb+cc)-C)<1e-9,'budget')
        check(aa>0 and cc>1 and bb>=0,'nonnegative weights')
        eig=np.linalg.eigvalsh(lap(nn,aa,bb,cc))
        check(abs(eig[0])<1e-9,'Laplacian zero mode')
        check(abs(eig[1]-1)<1e-9,'predicted spectral gap')
        if tt>dd*(1+1e-10):
            check(bb==0 and aa==3 and cc==2 and abs(C-5*nn)<1e-9,'deleted rim')
        if tt<dd*(1-1e-10):
            check(bb>0 and abs(aa-low)<1e-10,'positive rim')
            check(abs(eig[3]-1)<1e-8,'radial and transverse mode coincidence')
        if abs(tt-dd)<1e-11:
            for frac in [0.,.25,.5,.75,1.]:
                aa2=low+frac*(3-low)
                bb2=(3-aa2)/dd
                ev=np.linalg.eigvalsh(lap(nn,aa2,bb2,2.))
                check(abs(ev[1]-1)<1e-8,'critical continuum')
        # invariant candidates with same budget cannot exceed the constructive optimum;
        # arbitrary asymmetric weights also tested against globally claimed maximum.
        for _ in range(4):
            vals=rng.dirichlet(np.ones(3*nn))*C
            spw=vals[:nn]
            rmw=vals[nn:2*nn]/tt
            lfw=vals[2*nn:]
            Ll=np.zeros_like(lap(nn,aa,bb,cc))
            def ed(x,y,w):
                Ll[x,x]+=w;Ll[y,y]+=w;Ll[x,y]-=w;Ll[y,x]-=w
            for j in range(nn):
                ed(0,1+j,spw[j]);ed(1+j,1+(j+1)%nn,rmw[j]);ed(1+j,1+nn+j,lfw[j])
            ev=np.linalg.eigvalsh(Ll)
            check(ev[1]<=1+1e-9,'asymmetric competitor')
print('PASS',count,'exact-symbolic and numerical assertions')
