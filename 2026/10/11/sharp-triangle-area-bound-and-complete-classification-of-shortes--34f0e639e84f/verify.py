#!/usr/bin/env python3
"""Reproducible finite checks for the triangle area/halving-chord theorem.

Uses only Python's standard library. The analytic proof is in RESULT.md;
these computations are supplementary, not an exhaustive proof.
"""
from fractions import Fraction as F
import math
import random


def pt_at(t, sides, vertices):
    a,b,c=sides
    edges=((vertices[0],vertices[1],c),(vertices[1],vertices[2],a),(vertices[2],vertices[0],b))
    L=a+b+c
    t=t%L
    for p,q,length in edges:
        if t <= length+1e-13:
            f=min(1.0,max(0.0,t/length))
            return (p[0]+f*(q[0]-p[0]),p[1]+f*(q[1]-p[1]))
        t -= length
    return vertices[0]


def halving_distance_by_independent_piecewise_minimization(a,b,c):
    # a=|BC|, b=|CA|, c=|AB|, strict triangle inequalities.
    coord=(b*b+c*c-a*a)/(2.0*c)
    altitude=math.sqrt(max(0,b*b-coord*coord))
    vertices=((0.,0.),(c,0.),(coord,altitude))
    s=(a+b+c)/2.0
    split=[0.,s]
    for t in (c,c+a,c-s,c+a-s):
        if 0<t<s: split.append(t)
    split=sorted(set(split))
    candidates=[]
    for low,high in zip(split[:-1],split[1:]):
        mid=(low+high)/2
        def delta(t):
            p=pt_at(t,(a,b,c),vertices)
            q=pt_at(t+s,(a,b,c),vertices)
            return (p[0]-q[0],p[1]-q[1])
        dm=delta(mid)
        eps=(high-low)*.25
        left=delta(mid-eps)
        right=delta(mid+eps)
        vel=((right[0]-left[0])/(2*eps),(right[1]-left[1])/(2*eps))
        den=vel[0]**2+vel[1]**2
        tstar=mid-(dm[0]*vel[0]+dm[1]*vel[1])/den if den>1.e-20 else mid
        for t in (low,high,min(high,max(low,tstar))):
            d=delta(t)
            candidates.append(math.hypot(d[0],d[1]))
    return min(candidates)


def run():
    # Exact-rational verification of the two independent nonnegative steps
    # on a nonuniform finite grid of tangent lengths, including equality.
    checked=0
    for X in range(1,22):
        for Y in range(1,X+1):
            for Z in range(1,Y+1):
                x,y,z=F(X),F(Y),F(Z)
                s=x+y+z
                m=(x+y)*(x+z)/(s*s)
                n=s*x/(y*z)
                assert m>=F(4,9)
                assert n>=3
                u,v,t=y-z,x-y,z
                defect=(9*(x+y)*(x+z)-4*s*s)
                assert defect==6*t*u+12*t*v+2*u*u+11*u*v+5*v*v
                if m==F(4,9) or n==3:
                    assert x==y==z
                checked+=1
    rng=random.Random(17041)
    cases=[(1.,1.,1.),(1.,1.,math.sqrt(2)),(1.,1.,1.99),(1.,2.,2.99),(.1,1,1),(1.,2.,2.)]
    for i in range(1200):
        x=math.exp(rng.uniform(-4,4))
        y=math.exp(rng.uniform(-4,4))
        z=math.exp(rng.uniform(-4,4))
        a=y+z;b=x+z;c=x+y
        cases.append((a,b,c))
    tol=3e-7
    for a,b,c in cases:
        s=(a+b+c)/2
        A=math.sqrt(s*(s-a)*(s-b)*(s-c))
        # Heron half-angle formula at smallest angle, independent of minimizer search.
        aa,bb,cc=sorted((a,b,c))
        h_expected=s*math.sqrt((s-bb)*(s-cc)/(bb*cc))
        h_observed=halving_distance_by_independent_piecewise_minimization(a,b,c)
        assert abs(h_expected-h_observed)<=tol*max(1.,s),(a,b,c,h_expected,h_observed)
        assert A/h_observed**2>=4/(3*math.sqrt(3))-2e-7,(a,b,c,A/h_observed**2)
    print('VERIFY_OK',checked,'exact-rational triples;',len(cases),'independent halving-chord minimizations')

if __name__=='__main__':
    run()
