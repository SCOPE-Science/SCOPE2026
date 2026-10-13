"""Reproduce the spherical rank-one RCGLS identities on identity least squares.
Standard-library only; numerical experiments corroborate, not prove the theorem.
"""
from fractions import Fraction as F
from math import sqrt
import random

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return [x-y for x,y in zip(a,b)]

def add(a,b):
    return [x+y for x,y in zip(a,b)]

def scale(a,c):
    return [c*x for x in a]

def exact_step(e,s,p_prev=None):
    # A=I, residual=e, sketched gradient g=(s.e)s.
    raw=scale(s,dot(s,e))
    if p_prev is None:
        p=raw
    else:
        p=sub(raw,scale(p_prev,dot(raw,p_prev)/dot(p_prev,p_prev)))
    assert dot(p,p)!=0
    mu=dot(e,p)/dot(p,p)
    return sub(e,scale(p,mu)),p

# Exact rational test checks RCGLS recursion and geometric projection form.
checks=0
for d in (2,3,4,5):
    starts=[[F(j+1) for j in range(d)],[F((-1)**j*(j+2)) for j in range(d)]]
    sketches=[[F(j+1+(r+j*j)%5) for j in range(d)] for r in range(15)]
    for e0 in starts:
        for u in sketches:
            if dot(u,e0)==0:continue
            e1,p0=exact_step(e0,u)
            for v in sketches:
                proj=sub(v,scale(p0,dot(v,p0)/dot(p0,p0)))
                if dot(proj,proj)==0 or dot(proj,e1)==0:continue
                e2,p1=exact_step(e1,v,p0)
                geometric=sub(e1,scale(proj,dot(e1,proj)/dot(proj,proj)))
                assert e2==geometric and dot(e2,p1)==0
                if d==2: assert all(x==0 for x in e2)
                checks+=1
assert checks>500

# Independent simulation: draw each new spherical direction via rank-one
# Gaussian sketches, apply the exact RCGLS update including the correction.
rg=random.Random(20261010)
N=18000
counts=0
for d in (3,5,9):
    first=[]; later=[]; lag=[]
    for rep in range(N):
        e=[1.0]+[0.0]*(d-1)
        prev=None; factors=[]
        for k in range(4):
            v=[rg.gauss(0,1) for _ in range(d)]
            if prev is None:
                p=v
            else:
                c=dot(v,prev)/dot(prev,prev)
                p=sub(v,scale(prev,c))
            norm=dot(p,p)
            ratio=1-dot(e,p)**2/(dot(e,e)*norm)
            e=sub(e,scale(p,dot(e,p)/norm))
            prev=p
            factors.append(ratio)
        first.append(factors[0]); later.extend(factors[1:]);lag.append(factors[1]*factors[2]);counts+=4
    mu0=(d-1)/d;mu=(d-2)/(d-1)
    # Moments of Beta((dimension-1)/2, 1/2) in active subspace.
    alpha0=(d-1)/2; alpha=(d-2)/2
    m20=alpha0*(alpha0+1)/((alpha0+.5)*(alpha0+1.5))
    m2=alpha*(alpha+1)/((alpha+.5)*(alpha+1.5))
    sample=lambda z:sum(z)/len(z)
    for sample_val,target in ((sample(first),mu0),(sample(later),mu),(sample([x*x for x in first]),m20),(sample([x*x for x in later]),m2),(sample(lag),mu*mu)):
        assert abs(sample_val-target)<.022,(d,sample_val,target)
print('VERIFY_OK exact_fraction_identities=',checks,'gaussian_steps=',counts)
