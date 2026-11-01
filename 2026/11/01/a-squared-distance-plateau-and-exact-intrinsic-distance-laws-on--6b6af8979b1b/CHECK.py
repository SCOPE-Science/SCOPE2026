#!/usr/bin/env python3
"""Reproducible checks for the tetrahedral surface geodesic dispersion plateau.
Python 3 with numpy and sympy; all exact moment identities use symbolic rational algebra.
"""
import math
import numpy as np
import sympy as sp

u, v = sp.symbols('u v', real=True)
w = sp.Rational(1,2)+6*u*v
ysq = 3*(v-u)**2
integrands = [2*w, 2*w**3/sp.Integer(3)+2*ysq*w,
              2*w**5/sp.Integer(5)+sp.Rational(4,3)*ysq*w**3+2*ysq**2*w]
values = [sp.factor(sp.integrate(p,(v,sp.Rational(-1,2),sp.Rational(1,2)))) for p in integrands]
expected = [sp.Integer(1), sp.Rational(1,3), (1+12*u**2)*(5-36*u**2)/30]
for got, want in zip(values,expected):
    assert sp.simplify(got-want)==0, (got,want)
print('PASS exact polynomial identities: mass, quadratic and quartic moments', values)

SQRT3 = math.sqrt(3)
def candidates(s):
    q=np.array([.5,SQRT3*s])
    vs=[]
    for m in range(-2,3):
      for n in range(-2,3):
        lattice=np.array([2*m+n,SQRT3*n])
        for eps in (1,-1):
          site=lattice+(eps-1)*q
          if np.linalg.norm(site)>1e-8: vs.append(site)
    return vs

def clip(poly, z):
    c = float(z@z)/2
    out=[]
    for p,r in zip(poly,poly[1:]+poly[:1]):
        a=float(p@z-c); b=float(r@z-c)
        if a <=1e-10:out.append(p)
        if (a < -1e-10 and b > 1e-10) or (a > 1e-10 and b < -1e-10):
            out.append(p+(r-p)*(-a)/(b-a))
    return out

def dedupe(poly):
    out=[]
    for pt in poly:
        if not out or np.linalg.norm(pt-out[-1])>1e-8:out.append(pt)
    if len(out)>1 and np.linalg.norm(out[0]-out[-1])<1e-8:out.pop()
    return out

def actual_cell(s):
    poly=[np.array([-20.,-20.]),np.array([20.,-20.]),np.array([20.,20.]),np.array([-20.,20.])]
    for z in candidates(s):poly=clip(poly,z)
    return dedupe(poly)

def target_cell(s):
    return [np.array([ .5+3*s,SQRT3*(.5-s)]),
            np.array([-.5-3*s,SQRT3*(.5-s)]),
            np.array([-.5+3*s,-SQRT3*(.5+s)]),
            np.array([ .5-3*s,-SQRT3*(.5+s)])]

def polygon_area(poly):
    return abs(sum(float(np.linalg.det(np.stack([a,b])))/2 for a,b in zip(poly,poly[1:]+poly[:1])))

for s in np.linspace(0,1/6,61):
    observed=actual_cell(s)
    target=dedupe(target_cell(s))
    assert len(observed)==len(target),(s,len(observed),len(target))
    for a in observed:
        assert min(np.linalg.norm(a-b) for b in target)<2e-8,(s,a,target)
    assert abs(polygon_area(observed)-SQRT3)<1e-8
    for a in target:
        assert abs(float(a@a)-(1+12*s*s))<1e-8
print('PASS exact-Voronoi-vertex numerical comparisons for 61 parameter values (including endpoints)')

def seg(r,d):
    if r<=d:return 0.
    return r*r*math.acos(d/r)-d*math.sqrt(max(0.,r*r-d*d))

def cdf(s,r):
    R=math.sqrt(1+12*s*s)
    if r<0:return 0.
    if r>=R:return 1.
    return (math.pi*r*r-2*seg(r,R/2)
            -seg(r,SQRT3*(.5-s))-seg(r,SQRT3*(.5+s)))/SQRT3

for s in np.linspace(0,1/6,53):
    R=math.sqrt(1+12*s*s)
    grid=np.linspace(0,R,241)
    vals=[cdf(s,float(r)) for r in grid]
    assert vals[0]>=-1e-12 and max(vals)<1+1e-10
    assert min(b-a for a,b in zip(vals,vals[1:])) >= -1e-10
    assert abs(vals[-1]-1)<1e-12
print('PASS CDF numerical support, normalization, monotonicity over 53 configurations')

rng=np.random.default_rng(734199)
N=110000
UV=rng.random((N,2))
Z=np.column_stack([2*UV[:,0]+UV[:,1],SQRT3*UV[:,1]])
MS=[];max_cdf_dev=0.
for s in [0.,1/36,1/12,1/8,1/6]:
    q=np.array([.5,SQRT3*s])
    dist2=np.full(N,np.inf)
    for m in range(-1,3):
      for n in range(-1,3):
        lattice=np.array([2*m+n,SQRT3*n])
        for eps in (1,-1):
          shifted=Z-(lattice+eps*q)
          ds=np.sum(shifted**2,axis=1)
          np.minimum(dist2,ds,out=dist2)
    R=math.sqrt(1+12*s*s)
    assert dist2.max()<=R*R+1e-8
    for r in np.linspace(.15*R,.95*R,11):
        dev=abs(float(np.mean(dist2<=r*r))-cdf(s,float(r)))
        max_cdf_dev=max(max_cdf_dev,dev)
        assert dev<.012,(s,r,dev)
    mean2=float(np.mean(dist2));mean4=float(np.mean(dist2**2))
    exp4=(1+12*s*s)*(5-36*s*s)/30
    assert abs(mean2-1/3)<.009,(s,mean2)
    assert abs(mean4-exp4)<.012,(s,mean4,exp4)
    MS.append([s,mean2,mean4])
print('PASS direct periodic-orbit distance samples: 5*110000 uniform torus targets, 55 CDF checks')
print('maximum sampled CDF deviation:',max_cdf_dev)
for s,m2,m4 in MS: print('s=',round(s,8),'moment2=',round(m2,8),'moment4=',round(m4,8))
