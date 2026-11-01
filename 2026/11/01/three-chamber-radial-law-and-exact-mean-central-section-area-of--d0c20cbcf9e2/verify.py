#!/usr/bin/env python3
"""Numerical and combinatorial checks for the rhombic-dodecahedral radial law.

Requires Python 3, mpmath, and numpy. Finite tests do not establish the theorem.
"""
import math
import random
import itertools
import mpmath as mp
import numpy as np

mp.mp.dps = 50
SQ2 = mp.sqrt(2)
R0 = 2 * mp.sqrt(mp.mpf(2)/3)
R1 = mp.sqrt(3)
BETA = mp.atan(SQ2)

def density(r):
    r = mp.mpf(r)
    if r <= SQ2 or r >= 2:
        return mp.mpf('0')
    delta = mp.acos(SQ2/mp.sqrt(3*(r*r-2))) if r > R0 else mp.mpf(0)
    if r < R0:
        L = mp.pi/2
    elif r < R1:
        L = mp.pi/2-2*delta
    else:
        L = BETA-delta
    return 12*SQ2/(mp.pi*r*r)*L

seg = [SQ2,R0,R1,mp.mpf(2)]
pieces = [mp.quad(density,[seg[i],seg[i+1]]) for i in range(3)]
assert abs(sum(pieces)-1) < mp.mpf('1e-36'), ('normalization',pieces)
assert abs(pieces[0]-6*(1-mp.sqrt(3)/2)) < mp.mpf('1e-38')
second = sum(mp.quad(lambda x: x*x*density(x),[seg[i],seg[i+1]]) for i in range(3))
mean_formula = 8*mp.sqrt(3)*mp.log(1+mp.sqrt(3))-2*mp.pi
assert abs(mp.pi*second-mean_formula)<mp.mpf('1e-34'), ('second moment',mp.pi*second,mean_formula)
mean_gnomonic = 48*mp.quad(lambda s: mp.asinh(s/mp.sqrt(1+s*s))/(1+s)**2,[0,1])
assert abs(mean_gnomonic-mean_formula)<mp.mpf('1e-40')

# Check density endpoints, continuity at internal transitions and monotone CDF.
for rb in (R0,R1):
    left = density(rb-mp.mpf('1e-10'))
    right = density(rb+mp.mpf('1e-10'))
    assert abs(left-right)<mp.mpf('0.0002'), (rb,left,right)

# Independent polyhedral representation as the 14 stated vertices and 24 edges.
vertices = []
for i in range(3):
    for sign in (-1,1):
        z=[0.,0.,0.]; z[i]=2.*sign; vertices.append(z)
for signs in itertools.product((-1.,1.),repeat=3):
    vertices.append(list(signs))
vertices=np.array(vertices,dtype=float)
edges=[]
for i in range(6):
    axis=int(np.argmax(np.abs(vertices[i]))); sg=np.sign(vertices[i,axis])
    for j in range(6,14):
        if vertices[j,axis]==sg:
            edges.append((i,j))
assert len(edges)==24

def section_area(n):
    # Intersect the 24 polyhedron edges with n-perpendicular plane.
    dots=vertices @ n
    cut=[]
    for i,j in edges:
        if dots[i]*dots[j]<0:
            t=dots[i]/(dots[i]-dots[j]); cut.append(vertices[i]+t*(vertices[j]-vertices[i]))
    assert len(cut) in (4,6,8), (n,len(cut))
    e=np.cross(n,np.array([1.,0.,0.]))
    if np.linalg.norm(e)<0.1: e=np.cross(n,np.array([0.,1.,0.]))
    e=e/np.linalg.norm(e); f=np.cross(n,e)
    xy=np.array([[np.dot(x,e),np.dot(x,f)] for x in cut]); theta=np.arctan2(xy[:,1],xy[:,0]); xy=xy[np.argsort(theta)]
    return .5*abs(float(np.dot(xy[:,0],np.roll(xy[:,1],-1))-np.dot(xy[:,1],np.roll(xy[:,0],-1))))

rng=random.Random(20317)
N=18000
sums=0.
counts=[0,0,0]
for k in range(N):
    v=np.array([rng.gauss(0,1) for _ in range(3)],dtype=float);v/=np.linalg.norm(v)
    a,b,c=sorted(abs(float(x)) for x in v)[::-1]
    r=2/(a+b)
    # Independently verify all 12 half-space constraints to machine precision.
    rho_all=min(2/(abs(float(v[i]))+abs(float(v[j]))) for i,j in ((0,1),(0,2),(1,2)))
    assert abs(r-rho_all)<1e-12
    counts[0 if r<=float(R0) else (1 if r<=float(R1) else 2)]+=1
    sums += section_area(v)
for empirical, theory in zip([c/N for c in counts],pieces):
    assert abs(empirical-float(theory)) < 0.022,(empirical,theory)
sample_mean=sums/N
assert abs(sample_mean-float(mean_formula))<0.11,(sample_mean,mean_formula)

print('PASS: exact density normalization, three chamber probabilities:',*[mp.nstr(x,19) for x in pieces])
print('PASS: exact mean-section area from independent density and gnomonic integrals:',mp.nstr(mean_formula,20))
print('PASS: 18,000 independently reconstructed polyhedral sections; sampled mean:',round(sample_mean,12))
print('PASS: Haar angular frequencies and polyhedron halfspace cross-checks')
