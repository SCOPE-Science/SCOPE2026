#!/usr/bin/env python3
"""Finite consistency checks for the three-period shadowing formula; not a substitute for proof."""
from fractions import Fraction as Q
from math import sqrt
from random import Random
from itertools import combinations
import numpy as np
import sympy as S

def edge_max(points):
    vals=[]
    for i,j in combinations(range(3),2):
        Ai,Bi=points[i];Aj,Bj=points[j]
        vals.extend([sqrt(Ai)+sqrt(Bi),sqrt(Aj)+sqrt(Bj)])
        a=Ai-Aj;b=Bj-Bi
        if a<0 and b<0:
            i,j=j,i; Ai,Bi=points[i];Aj,Bj=points[j]
            a=Ai-Aj;b=Bj-Bi
        if a>0 and b>0:
            t=(a*a*Bj-b*b*Aj)/(a*b*(a+b))
            if 0<t<1: vals.append(sqrt((a+b)*(a*Bj+b*Aj)/(a*b)))
    return max(vals)

def data(weights):
    c=float(np.prod(weights))
    if c<1:
        a=[(weights[(i-1)%3]**2,(weights[(i-1)%3]*weights[(i-2)%3])**2) for i in range(3)]
        scalar=1;factor=1/(1-c)
    elif c>1:
        a=[(weights[i]**-2,(weights[i]*weights[(i+1)%3])**-2) for i in range(3)]
        scalar=1/c;factor=1/(1-1/c)
    else: raise ValueError('critical product')
    return a,scalar,factor

def main():
    t=S.Rational(1724711,3489255)
    g=S.sqrt(1+99*t)+S.sqrt(100-S.Rational(399,4)*t)
    assert S.simplify(g**2-S.Rational(3533245,17556))==0
    assert S.simplify(g-S.sqrt(S.Integer(15507412305))/8778)==0
    constant=2*(1+g)
    assert S.simplify(constant-(2+S.sqrt(S.Integer(15507412305))/4389))==0
    assert 0<t<1
    assert float(constant)>30 and float(constant)>24
    w=(10.,1.,.05)
    pts,scalar,factor=data(w)
    assert abs((scalar+edge_max(pts))*factor-float(constant))<1.e-10
    assert max((scalar+sqrt(A)+sqrt(B))*factor for A,B in pts)==24
    rng=Random(240719)
    checks=7
    for trial in range(80):
        w=tuple(10**rng.uniform(-0.9,0.9) for j in range(3))
        if abs(np.prod(w)-1)<.05: continue
        pts,scalar,factor=data(w)
        e=edge_max(pts)
        grid=max(sqrt(sum(pts[j][0]*x[j] for j in range(3)))+sqrt(sum(pts[j][1]*x[j] for j in range(3))) for a in range(61) for b in range(61-a) for x in [(a/60,b/60,1-(a+b)/60)])
        assert e>=grid-1e-10
        assert e-grid<.025*max(1.,e)
        checks+=2
    # Explicit finite Green truncations demonstrate convergence of the geometric grouping.
    from numpy.linalg import norm
    p=(np.array([.0,float(t),1-float(t)]))
    v=np.sqrt(p)
    w=np.array([10,1,.05]); c=np.prod(w)
    residues=[]
    for r in range(3):
        product=np.ones(3)
        for s in range(1,r+1):product*=w[(np.arange(3)-s)%3]
        residues.append(norm(product*v))
    exact=sum(residues)/(1-c)
    for terms in [9,18,30,48]:
        partial=sum(c**k*sum(residues) for k in range(terms//3))
        assert abs(partial-exact)<sum(residues)*c**(terms//3)/(1-c)+1e-12
        checks+=1
    print('PASS',checks,'finite exact/consistency assertions; example constant',float(constant))
if __name__=='__main__':main()
