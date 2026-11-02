"""Independent finite and algebraic checks for the stated zeroth-order descent example.

Requires only Python 3 standard library. Numerical checks are diagnostic; the
infinite-dimensional support and limiting distribution statements use proofs.
"""
from fractions import Fraction as F
import math
import random


def radii(gamma, h=F(1), dimension=2):
    g=F(gamma); h=F(h)
    assert 0<g<2 and dimension>=2
    q=abs(1-g)
    a=g*h*F(dimension,1) # a = gamma*h*sqrt(d)/2; work with normalized radii
    # Return radii multiplied by 2/(h*sqrt(d)): amplitude=gamma.
    outer=g/(1-q)
    inner=g*max(F(0), 1-2*q)/(1-q)
    return (inner,outer)


def finite_support_radii(gamma, n):
    g=F(gamma); q=abs(1-g)
    assert n>=1 and 0<g<2
    total=sum((q**i for i in range(n)),F(0))
    # directions lie on a sphere with d>=2; polygon inequality is exact.
    return (g*max(F(0),2-total),g*total)


def stationary_second_moment(gamma, dim, h=F(1)):
    g=F(gamma); h=F(h)
    return dim*g*h*h/(4*(2-g))


numchecks=0
for dim in (2,3,4,9):
    for gi in range(1,40):
        g=F(gi,20)
        if g==2: continue
        q=abs(1-g)
        inner,outer=radii(g,dimension=dim)
        assert outer==g/(1-q)
        assert inner==max(F(0),g*(1-2*q)/(1-q))
        if g<=1:
            assert outer==1
        if g>1:
            assert outer==g/(2-g)
        assert (inner>0)==(F(1,2)<g<F(3,2))
        assert stationary_second_moment(g,dim)==(g*g*F(dim,4))/(1-q*q)
        for n in (2,3,5,20,75):
            lo,hi=finite_support_radii(g,n)
            assert lo>=inner and hi<=outer
            assert hi<=g/(1-q)
            # Uniform geometric convergence bounds truncation of support.
            error=g*q**n/(1-q)
            assert abs(hi-outer)<=error
            assert abs(lo-inner)<=error
            numchecks+=1
print('Exact rational support/moment/geometric-tail tests:',numchecks)

# Verify actual forward finite-difference update in an independently rotated
# orthonormal basis. This does not replace the exact calculation in the proof.
rng=random.Random(73519)
for dim in (2,3,5):
    for gamma in (0.25,0.7,1.0,1.2,1.75):
        delta=0.43; lam=1.7; alpha=gamma/lam
        for t in range(50):
            cols=[]
            for j in range(dim):
                while True:
                    v=[rng.gauss(0,1) for _ in range(dim)]
                    for u in cols:
                        s=sum(v[k]*u[k] for k in range(dim))
                        v=[v[k]-s*u[k] for k in range(dim)]
                    size=math.sqrt(sum(y*y for y in v))
                    if size>1e-6: break
                cols.append([v[k]/size for k in range(dim)])
            x=[rng.uniform(-1,1) for _ in range(dim)]
            f=lambda z:lam/2*sum(w*w for w in z)
            fd=[0.0]*dim
            for u in cols:
                z=[x[i]+delta*u[i] for i in range(dim)]
                deriv=(f(z)-f(x))/delta
                fd=[fd[i]+deriv*u[i] for i in range(dim)]
            summed=[sum(u[i] for u in cols) for i in range(dim)]
            direct=[lam*x[i]+lam*delta/2*summed[i] for i in range(dim)]
            assert max(abs(fd[i]-direct[i]) for i in range(dim))<2e-13
            updated=[x[i]-alpha*fd[i] for i in range(dim)]
            linear=[(1-gamma)*x[i]-gamma*delta/2*summed[i] for i in range(dim)]
            assert max(abs(updated[i]-linear[i]) for i in range(dim))<2e-13
            assert abs(sum(y*y for y in summed)-dim)<2e-12
            numchecks+=1
print('Including direct finite-difference identity tests:',numchecks)

# Independent stationary-sampling consistency check: finite series of
# independent random directions, at four regimes. Sampling is not proof.
for gamma in (0.25,0.75,1.0,1.25,1.75):
    d=3; delta=0.43
    q=abs(1-gamma)
    aa=gamma*delta*math.sqrt(d)/2
    lo,hi=radii(F(str(gamma)),dimension=d)
    factor=delta*math.sqrt(d)/2
    expected= float(stationary_second_moment(F(str(gamma)),d,F(str(delta))))
    m=16000; n=280
    acc=0.0
    for j in range(m):
        z=[0.0,0.0,0.0]; weight=1.0
        for k in range(n):
            v=[rng.gauss(0,1) for _ in range(d)]
            vn=math.sqrt(sum(w*w for w in v))
            for t in range(d): z[t]+=aa*weight*v[t]/vn
            weight*=q
            if weight<1e-15: break
        radius=math.sqrt(sum(t*t for t in z))
        assert factor*float(lo)-1e-8 <= radius <= factor*float(hi)+1e-8
        acc+=radius*radius
    empirical=acc/m
    assert abs(empirical/expected-1)<0.08,(gamma,empirical,expected)
    print('gamma, observed/predicted second moment:',gamma,empirical/expected)
print('PASS: finite checks support the analytic theorem; no simulation used as proof.')
