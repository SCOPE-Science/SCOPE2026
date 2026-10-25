"""Supplementary finite checks for the regular-polytope squared-distance gap.
Run: python verify.py (requires numpy and scipy). Numerical samples do not prove the theorem.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.stats import kstest

RNG = np.random.default_rng(20261022)
N = 120000

def report(name, points, vertices, edge_squared, d):
    dist_sq = np.sum((points[:, None, :] - vertices[None, :, :])**2, axis=2)
    two = np.partition(dist_sq, 1, axis=1)[:, :2]
    gap = (two[:, 1] - two[:, 0]) / edge_squared
    assert float(gap.min()) >= -1e-10 and float(gap.max()) <= 1+1e-10
    exact_cdf = lambda z: 1 - (1 - np.clip(z, 0., 1.))**d
    statistic, pvalue = kstest(gap, exact_cdf)
    theoretical_mean = 1. / (d + 1)
    tail = (1-.5)**d
    assert abs(float(gap.mean()) - theoretical_mean) < .012
    assert abs(float(np.mean(gap > .5)) - tail) < .012
    print('%-23s d=%d  mean=%.6f  P(gap>.5)=%.6f  KS=%.5f  KS_p=%.4f'
          % (name, d, gap.mean(), np.mean(gap>.5), statistic, pvalue))

def regular_ngon(n):
    ang = 2*np.pi*np.arange(n)/n
    v = np.stack([np.cos(ang),np.sin(ang)], axis=1)
    index = RNG.integers(n, size=N)
    bary = RNG.dirichlet([1,1,1], size=N)
    x = bary[:,1,None]*v[index] + bary[:,2,None]*v[(index+1)%n]
    report('regular %d-gon'%n, x, v, 4*np.sin(np.pi/n)**2, 2)

def regular_simplex(d):
    m=d+1
    v=np.eye(m)-np.ones((m,m))/m
    bary=RNG.dirichlet(np.ones(m),size=N)
    x=bary@v
    report('regular %d-simplex'%d,x,v,2.,d)

def cube(d):
    from itertools import product
    v=np.array(list(product([-1.,1.],repeat=d)))
    x=RNG.uniform(-1.,1.,size=(N,d))
    report('%d-cube'%d,x,v,4.,d)

def crosspolytope(d):
    v=np.concatenate([np.eye(d),-np.eye(d)],axis=0)
    weights=RNG.dirichlet(np.ones(d+1),size=N)[:,:d]
    x=weights*RNG.choice([-1.,1.],size=(N,d))
    report('%d-crosspolytope'%d,x,v,2.,d)

def regular_3poly(name,vertices):
    v=np.array(vertices,dtype=float)
    hull=ConvexHull(v)
    tris=v[hull.simplices]
    vols=np.abs(np.linalg.det(tris))/6
    face=RNG.choice(len(tris),size=N,p=vols/vols.sum())
    weights=RNG.dirichlet(np.ones(4),size=N)[:,1:]
    x=np.sum(tris[face]*weights[:,:,None],axis=1)
    dist_sq=np.sum((v[:,None,:]-v[None,:,:])**2,axis=2)
    np.fill_diagonal(dist_sq,np.inf)
    edge_sq=float(dist_sq.min())
    report(name,x,v,edge_sq,3)

if __name__=='__main__':
    for n in [3,4,5,6,7,8,9,12,17,29]: regular_ngon(n)
    for d in [2,3,4,5,6]: regular_simplex(d)
    for d in [2,3,4,5]: cube(d); crosspolytope(d)
    phi=(1+math.sqrt(5))/2
    ico = [(0,a,b*phi) for a in [-1,1] for b in [-1,1]] + [(a,b*phi,0) for a in [-1,1] for b in [-1,1]] + [(a*phi,0,b) for a in [-1,1] for b in [-1,1]]
    dod = [(a,b,c) for a in [-1,1] for b in [-1,1] for c in [-1,1]] + [(0,a/phi,b*phi) for a in [-1,1] for b in [-1,1]] + [(a/phi,b*phi,0) for a in [-1,1] for b in [-1,1]] + [(a*phi,0,b/phi) for a in [-1,1] for b in [-1,1]]
    regular_3poly('icosahedron',ico)
    regular_3poly('dodecahedron',dod)
