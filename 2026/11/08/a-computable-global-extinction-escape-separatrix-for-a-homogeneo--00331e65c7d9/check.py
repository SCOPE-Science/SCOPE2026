#!/usr/bin/env python3
"""Reproducible finite checks of a quadratic cone map's radial separatrix.
This checks instances of algebraic identities; it is not a proof of asymptotic claims.
"""
from math import log,exp,isclose
from fractions import Fraction

def project(theta,p):
    vals=[th*t*(2-t) for th,t in zip(theta,p)]
    z=sum(vals)
    return [v/z for v in vals],z/2

def threshold(theta,p,N=90):
    beta=0.0
    for j in range(N):
        p,a=project(theta,p)
        beta+=2**(-j-1)*log(a)
    return exp(-beta)

def theta_q(theta):
    n=len(theta)
    c=(2*n-1)/sum(1/x for x in theta)
    return [2-c/x for x in theta],c

def direct(theta,x):
    t=sum(x)
    return [Fraction(th,2)*xk*(2*t-xk) for th,xk in zip(theta,x)]

for n in (3,4,7):
    theta=[Fraction(100+i%3,100) for i in range(n)]
    x=[Fraction(7+i*i,27+i) for i in range(n)]
    t=sum(x)
    p=[v/t for v in x]
    z=sum(theta[i]*p[i]*(2-p[i]) for i in range(n))
    direct_x=direct(theta,x)
    recovered=[t*t*z/2*(theta[i]*p[i]*(2-p[i])/z) for i in range(n)]
    assert direct_x==recovered
print('EXACT_HOMOGENEOUS_PROJECTIVE_FACTORISATION_OK')

for theta in ([1,1,1],[.9,1.0,1.1],[1.0]*6,[1.2,1.2,1.2,1.2]):
    n=len(theta)
    q,c=theta_q(theta)
    assert min(q)>0 and abs(sum(q)-1)<1e-12
    p=[(i+1)/sum(range(1,n+1)) for i in range(n)]
    radii=[]
    for _ in range(600):
        radii.append(max(pi/qi for pi,qi in zip(p,q))/min(pi/qi for pi,qi in zip(p,q)))
        p,a=project(theta,p)
    assert all(radii[j+1]<=radii[j]*(1+1e-14) for j in range(599))
    assert max(abs(pi-qi) for pi,qi in zip(p,q))<1e-12
    p=[(i+1)/sum(range(1,n+1)) for i in range(n)]
    tc=threshold(theta,p)
    fp,a=project(theta,p)
    assert abs(a*tc*tc-threshold(theta,fp))/tc<2e-13
    assert abs(threshold(theta,q)-2/c)<2e-13
print('PROJECTIVE_CONTRACTION_AND_INVARIANT_THRESHOLD_OK')

for n in (3,4,7):
    th=1.25
    p0=[1/n]*n
    v=[0.0]*n
    v[0]=1
    v[1]=-1
    B=2-1/n
    lam=2*(n-1)/(2*n-1)
    coeff=1/(B*(2-lam*lam))
    tc0=threshold([th]*n,p0)
    for eps in (1e-3,3e-4,1e-4):
        p=[u+eps*w for u,w in zip(p0,v)]
        inferred=(threshold([th]*n,p)/tc0-1)/(eps*eps*sum(w*w for w in v))
        assert abs(inferred/coeff-1)<1e-2,(n,eps,inferred,coeff)
    assert isclose(tc0,2/(th*B),rel_tol=1e-14)
print('SYMMETRIC_THRESHOLD_CURVATURE_AND_EXTREMA_OK')

# High-precision scalar radial checks, avoiding overflow/cancellation.
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec=180
    theta=[Decimal('.9'),Decimal('1'),Decimal('1.1')]
    init=[Decimal('.2'),Decimal('.35'),Decimal('.45')]
    q,c=theta_q(theta)
    pp=init[:]
    beta=Decimal(0)
    a_values=[]
    for j in range(450):
        pp,a=project(theta,pp)
        a_values.append(a)
        beta+=a.ln()/Decimal(2)**(j+1)
    for factor,expected in ((Decimal('.98'),'decay'),(Decimal('1.02'),'growth'),(Decimal('1'),'critical')):
        u=-beta+factor.ln()
        for a in a_values[:200]:
            u=2*u+a.ln()
        if expected=='decay':assert u<Decimal(-1000)
        elif expected=='growth':assert u>Decimal(1000)
        else:assert abs(u.exp()-2/c)<Decimal('1e-5'),(u.exp(),2/c)
print('LOG_RADIUS_TRICHOTOMY_HIGH_PRECISION_CHECKS_OK')
print('ALL_FINITE_CHECKS_PASSED')
