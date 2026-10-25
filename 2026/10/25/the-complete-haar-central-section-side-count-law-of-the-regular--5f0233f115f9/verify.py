#!/usr/bin/env python3
"""Independent numerical corroboration of an exact spherical chamber formula.
No external data or unpublished inputs are required. Python 3, numpy, scipy.
"""
import itertools, math
from collections import Counter
import numpy as np
from scipy.integrate import dblquad

A=math.sqrt(2)-1
O=(0.,0.); J=(A,0.); B=(A/2,A/2); H=(1.,0.)
T=(2*A,A); E=(1/math.sqrt(2),1/math.sqrt(2))
F=(1.,1-A); G=(1.,1.)

# The six spherical tiles of one signed/permuted fundamental chamber.
tiles=((4,(O,J,B)),(6,(J,B,E,T)),(6,(E,G,F)),
       (8,(H,J,T)),(8,(T,E,F)),(10,(H,T,F)))

def spherical_triangle(points):
    v=[np.array([1.,*z]) for z in points]
    m=[float(np.linalg.norm(z)) for z in v]
    det=abs(float(np.linalg.det(np.stack(v))))
    denom=m[0]*m[1]*m[2]+sum(float(v[i]@v[(i+1)%3])*m[(i+2)%3] for i in range(3))
    return 2*math.atan2(det,denom)

def poly_omega(p):
    return sum(spherical_triangle((p[0],p[i],p[i+1])) for i in range(1,len(p)-1))

probs={k:sum(12/math.pi*poly_omega(poly) for n,poly in tiles if n==k) for k in (4,6,8,10)}
assert abs(sum(probs.values())-1)<3e-14
assert all(v>0 for v in probs.values())
print('EXACT_SPHERICAL_CHAMBER_PROBABILITIES_OK',probs)

# Independent facet geometry: each of 6 planes |x_i|=1 and 8 signed corner faces.
V=np.unique(np.array([tuple(sign[i]*q[i] for i in range(3))
                     for q in set(itertools.permutations((1.,1.,A)))
                     for sign in itertools.product((-1.,1.),repeat=3)]),axis=0)
assert len(V)==24
edges=[(i,j) for i in range(24) for j in range(i+1,24)
       if abs(np.linalg.norm(V[i]-V[j])-2*A)<1e-10]
assert len(edges)==36
facets=[]
for i in range(3):
    for s in (-1.,1.):
        ids=[k for k,v in enumerate(V) if abs(v[i]-s)<1e-9]
        assert len(ids)==8
        facets.append(ids)
for s in itertools.product((-1.,1.),repeat=3):
    ids=[k for k,v in enumerate(V) if abs(np.dot(s,v)-(2+A))<1e-9]
    assert len(ids)==3
    facets.append(ids)
assert len(facets)==14

def direct_side_count(u):
    signs=V@u
    edge_cross=sum(signs[i]*signs[j]<0 for i,j in edges)
    facet_cross=sum(min(signs[j] for j in f)<0<max(signs[j] for j in f)
                    for f in facets)
    assert edge_cross==facet_cross
    return edge_cross

def cell_count(u):
    p,q,r=sorted(np.abs(u),reverse=True)
    x=q/p; y=r/p
    return 4+2*int(x+A*y>1)+2*int(x+y>A and y<1-A*x)+2*int(y<x-A)

rng=np.random.default_rng(10827)
for _ in range(4000):
    u=rng.normal(size=3)
    assert direct_side_count(u)==cell_count(u)
print('INDEPENDENT_24_VERTEX_36_EDGE_14_FACET_CONSTRUCTION_OK 4000')

# Independent integral: radial gnomonic Jacobian over each Euclidean triangle.
def integrate_triangle(t):
    p0,p1,p2=np.array(t,dtype=float)
    d1=p1-p0;d2=p2-p0
    det=abs(float(np.linalg.det(np.stack([d1,d2]))))
    def g(w,v):
        x,y=p0+v*d1+w*d2
        return det/(1+x*x+y*y)**1.5
    return dblquad(g,0.,1.,lambda v:0.,lambda v:1.-v,epsabs=2e-11,epsrel=2e-11)[0]
for n,polygon in tiles:
    for i in range(1,len(polygon)-1):
        tri=(polygon[0],polygon[i],polygon[i+1])
        assert abs(spherical_triangle(tri)-integrate_triangle(tri))<3e-12
print('ANALYTIC_SOLID_ANGLES_AGREE_WITH_INDEPENDENT_GNOMONIC_QUADRATURE_OK')

# Mean section count from crossing probability of each 3-dimensional edge.
angle=2*math.asin(A/math.sqrt(2+A*A))
mean=36*angle/math.pi
assert abs(sum(n*probs[n] for n in probs)-mean)<1e-13
print('INDEPENDENT_EDGE_CROSSING_MEAN_IDENTITY_OK',mean)

# Independently sampled Haar normal vectors against exact tile probabilities.
N=450000
normals=rng.normal(size=(N,3))
counts=Counter(direct_side_count(normals[i]) for i in range(N) if i<2000)
# The rest uses direct vectorized edge incidence, not cell classification.
dots=normals@V.T
raw=np.zeros(N,dtype=np.int16)
for i,j in edges: raw+=(dots[:,i]*dots[:,j]<0)
assert set(np.unique(raw))==set(probs)
for n,p in probs.items():
    f=float(np.mean(raw==n)); tol=5*math.sqrt(p*(1-p)/N)+0.0006
    assert abs(f-p)<tol,(n,f,p,tol)
print('INDEPENDENT_HAAR_RANDOM_3D_EDGE_COUNT_DISTRIBUTIONS_OK',N,
      {k:float(np.mean(raw==k)) for k in probs})
print('ALL_REGULAR_TRUNCATED_CUBE_CENTRAL_SECTION_CHECKS_OK')
