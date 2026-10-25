#!/usr/bin/env python3
"""Standalone finite diagnostics for cross-polytope projection moments.

Run: python3 verify.py. Standard library only. Diagnostics do not certify the
asymptotic theorem; its proof is the expansion in RESULT.md.
"""
import itertools
import math
import random


def moment_formula(d):
    assert d >= 2 and d <= 1000
    # Binomial law of disagreements between two independent facet signs.
    weights = []
    p = 2.0 ** (-d)
    for k in range(d + 1):
        rho = 1.0 - 2.0 * k / d
        f = math.sqrt(max(0.0, 1.0 - rho*rho)) + rho * math.asin(rho)
        weights.append(p*f)
        if k < d:
            p *= (d-k)/(k+1)
    m2 = (2/math.pi)*math.fsum(weights)
    mean = math.sqrt(d/math.pi)*math.exp(math.lgamma(d/2)-math.lgamma((d+1)/2))
    return mean, m2


def direct_b(u):
    d = len(u)
    return math.fsum(abs(sum(s*x for s,x in zip(signs,u)))
                     for signs in itertools.product([-1.0,1.0], repeat=d))/(2**d)


def hull_area(points):
    pts = sorted(set((round(x,14),round(y,14)) for x,y in points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    hull=lo[:-1]+hi[:-1]
    return abs(math.fsum(a[0]*b[1]-a[1]*b[0] for a,b in zip(hull,hull[1:]+hull[:1])))/2


def shadow_area_3(u):
    # Construct the actual planar shadow of the six vertices ±e_i.
    d=(u[0]**2+u[1]**2+u[2]**2)**0.5
    u=[x/d for x in u]
    ref=[1.,0.,0.] if abs(u[0])<.8 else [0.,1.,0.]
    a=[ref[i]-sum(ref[j]*u[j] for j in range(3))*u[i] for i in range(3)]
    an=math.sqrt(sum(x*x for x in a)); a=[x/an for x in a]
    b=[u[1]*a[2]-u[2]*a[1],u[2]*a[0]-u[0]*a[2],u[0]*a[1]-u[1]*a[0]]
    pts=[]
    for i in range(3):
        for sign in (-1,1):pts.append((sign*a[i],sign*b[i]))
    return hull_area(pts)


def check():
    checks=0
    # Exact two-dimensional angular integrals of max(|cos|,|sin|).
    m,m2=moment_formula(2)
    assert abs(m-2*math.sqrt(2)/math.pi)<1e-13
    assert abs(m2-(.5+1/math.pi))<1e-13
    checks += 2
    # Algebraic Rademacher moment identities with exact integer arithmetic.
    for d in (2,3,4,5,8,10,16,20):
        den=2**d
        for q,want in ((2,d),(4,3*d*d-2*d),(6,15*d**3-30*d*d+16*d)):
            num=sum(math.comb(d,k)*(d-2*k)**q for k in range(d+1))
            assert num==den*want,(d,q,num,den*want)
            checks+=1
    # Direct geometric construction, not a reuse of the facet-sum formula.
    rng=random.Random(9217)
    for _ in range(100):
        u=[rng.gauss(0,1) for _ in range(3)]
        norm=math.sqrt(sum(x*x for x in u));u=[x/norm for x in u]
        geom=shadow_area_3(u)
        pred=2*direct_b(u)  # facet-normal normalization in dimension three.
        assert abs(geom-pred)<2e-12,(geom,pred,u)
        checks+=1
    # Sharp variance scale; finite d need not hit their asymptotic constant.
    for d,tol in ((32,.08),(64,.04),(100,.025),(200,.012),(500,.005),(1000,.003)):
        m,m2=moment_formula(d)
        v=m2-m*m
        assert v>0
        target=1/(3*math.pi)
        assert abs(d**3*v-target)/target<tol,(d,v,d**3*v,target)
        checks+=1
    print('PASS',checks,'finite diagnostics')
    for d in (2,3,8,32,100,500):
        m,m2=moment_formula(d)
        print('dimension',d,'mean',format(m,'.12g'),'variance',format(m2-m*m,'.12g'),
              'scaled_variance',format(d**3*(m2-m*m),'.12g'))

if __name__=='__main__':check()
