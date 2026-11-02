"""Finite checks for the intrinsic eccentricity theorem on a unit tetrahedron.

Requires numpy and scipy; this is corroboration, not a proof of all-point claims.
Coordinates use the flat-torus half-turn model and Voronoi circumcenters.
"""
from __future__ import annotations
import math
import random
import numpy as np
from scipy.spatial import Voronoi

root3=math.sqrt(3)
a=np.array([2.,0.]); b=np.array([1.,root3]); basis=np.stack((a,b),axis=1)
inv=np.linalg.inv(basis)
shifts=np.array([i*a+j*b for i in range(-3,4) for j in range(-3,4)])

def covering_radius(p):
    p=np.asarray(p, dtype=float)
    centers=np.vstack((shifts,shifts+p))
    vertices=Voronoi(centers).vertices
    coords=vertices@inv.T
    valid=(np.all(coords>=-1e-8,axis=1) & np.all(coords<=1+1e-8,axis=1))
    verts=vertices[valid]
    if not len(verts): raise AssertionError('No Voronoi vertices')
    d2=((verts[:,None,:]-centers[None,:,:])**2).sum(axis=2).min(axis=1)
    return math.sqrt(float(d2.max()))

def main():
    zero=covering_radius([0,0]); assert abs(zero-2/root3)<1e-8,zero
    for p in (np.array([1.,0.]),np.array([0.5,root3/2]),np.array([1.5,root3/2])):
        r=covering_radius(p)
        assert abs(r-1)<1e-8,(p,r)
    rng=random.Random(20261028)
    mn,mx=2.,0.
    n=250
    for i in range(n):
        x,y=rng.random(),rng.random()
        r=covering_radius(x*a+y*b)
        assert 1-1e-7<=r<=2/root3+1e-7,(i,x,y,r)
        mn=min(mn,r);mx=max(mx,r)
    print('vertex eccentricity:',repr(zero))
    print('all three nontrivial half-period two-center coverings: radius 1')
    print(f'{n} interior random source radii in [{mn:.12f},{mx:.12f}]')
    print('PASSED (finite checks only; theorem proven analytically)')

if __name__=='__main__':main()
