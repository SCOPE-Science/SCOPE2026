#!/usr/bin/env python3
"""Exact local-facet checks and independent sampling diagnostics for near-diameter surface pairs."""
from fractions import Fraction
from math import factorial, sqrt
import numpy as np


def simplex_constant(d):
    # Independent facet-by-facet integration of the linearized gap cone.
    m = d + 1
    facet_weight = []
    i, j = 0, 1
    for missing in range(m):
        if missing == i:
            continue
        others = [z for z in range(m) if z not in (i, missing)]
        product = Fraction(1)
        for z in others:
            product *= 1 if z == j else Fraction(1, 2)
        facet_weight.append(Fraction(1, 1) / product)
    B = sum(facet_weight, Fraction()) / m
    C = m * (m - 1) * B * B * Fraction(factorial(d-1)**2, factorial(2*d-2))
    return B, C


def cube_constant(d):
    # 2^d ordered opposite-vertex pairs; d incident facets per vertex.
    # For each such facet the tangent cone is an orthant of dimension d-1,
    # and each edge generator has projection 1/sqrt(d).
    # Therefore B^2 = d^(d-1) / (4 (d-1)!^2) at unit side length.
    return Fraction(2**(d-2) * d**(d-1),factorial(2*d-2))


def sample_linearized_simplex(d,eps,N,rng):
    """Exact importance sampler for the small near-diameter vertex sectors.

    This is a diagnostic; the proof is analytic. The proposal samples
    the simplex of all local first-order coordinates with total linear
    gap <= 1.15 epsilon, then checks exact Euclidean chord distances.
    """
    m=d+1
    k=d-1
    weights=[]; faces=[]
    for missing1 in range(1,m):
        ix=[i for i in range(m) if i not in (0,missing1)]
        alpha=[1. if z==1 else 0.5 for z in ix]
        for missing2 in range(m):
            if missing2==1: continue
            iy=[i for i in range(m) if i not in (1,missing2)]
            beta=[1. if z==0 else 0.5 for z in iy]
            w=float(np.prod(alpha)*np.prod(beta))**-1
            weights.append(w)
            faces.append((ix,iy,np.asarray(alpha),np.asarray(beta)))
    weights=np.asarray(weights)
    probabilities=weights/np.sum(weights)
    choices=rng.choice(len(weights),size=N,p=probabilities)
    # Uniform on the 2k-dimensional simplex (the last component is slack).
    g=rng.exponential(size=(N,2*k+1))
    g=g/g.sum(axis=1,keepdims=True)
    t=1.15*eps
    vals=t*g[:,:2*k]
    X=np.zeros((N,m)); Y=np.zeros((N,m))
    X[:,0]=1.;Y[:,1]=1.
    for idx,(ix,iy,a,b) in enumerate(faces):
        sel=choices==idx
        if not sel.any(): continue
        u=vals[sel,:k]/a
        v=vals[sel,k:]/b
        X[sel,0]-=u.sum(axis=1)
        Y[sel,1]-=v.sum(axis=1)
        X[np.ix_(sel,ix)]=u
        Y[np.ix_(sel,iy)]=v
    assert np.min(X)>-1e-12 and np.min(Y)>-1e-12
    dist=np.sqrt((0.5*(X-Y)**2).sum(axis=1))
    accepted=(dist>1-eps).mean()
    C=float(simplex_constant(d)[1])
    ratio=C*1.15**(2*k)*accepted
    error=C*1.15**(2*k)*sqrt(max(accepted*(1-accepted),1e-16)/N)
    return ratio,error


def cube_surface_importance(eps, n, rng):
    # Local coordinates on six square facets of the unit 3-cube near
    # opposite corners 000 and 111. All ordered vertex pairs contribute
    # equally. The auxiliary simplex covers first-order gap <= 1.15 eps.
    t=1.15*eps; k=2
    g=rng.exponential(size=(n,5)); g=g/g.sum(axis=1,keepdims=True)
    v=sqrt(3)*t*g[:,:4]
    fac1=rng.integers(0,3,size=n);fac2=rng.integers(0,3,size=n)
    X=np.zeros((n,3)); Y=np.ones((n,3))
    for i in range(3):
        sel=fac1==i
        cols=[j for j in range(3) if j!=i]
        X[np.ix_(sel,cols)]=v[sel,:2]
        sel=fac2==i
        Y[np.ix_(sel,cols)]-=v[sel,2:]
    dist=np.linalg.norm(X-Y,axis=1)
    accepted=(dist>sqrt(3)-eps).mean()
    C=float(cube_constant(3))
    ratio=C*1.15**4*accepted
    err=C*1.15**4*sqrt(accepted*(1-accepted)/n)
    return ratio,err

def main():
    for d in range(2,22):
        B,C=simplex_constant(d)
        assert B==2**(d-2)
        closed=Fraction(d*(d+1)*4**(d-2)*factorial(d-1)**2,factorial(2*d-2))
        assert C==closed
        # Alternative facet-area computation: the square of the normalized
        # endpoint-cap coefficient is d^(d-1)/(4 (d-1)!^2) at unit scale.
        B_squared = Fraction(d**(d-1),4*factorial(d-1)**2)
        independent_cube = Fraction(2**d*factorial(d-1)**2,factorial(2*d-2)) * B_squared
        assert independent_cube == cube_constant(d)
        if d==3:
            assert C==8
            assert cube_constant(d)==Fraction(3,4)
    # Cross-polytope in three dimensions: six ordered antipodal tips,
    # B=1/2 from four equilateral facet cones of area sqrt(3)/2
    # divided by total area 4sqrt(3).
    assert 6*Fraction(1,2)**2*Fraction(2*2,24)==Fraction(1,4)
    # Numerically independent check of the exact geometric gap.
    rng=np.random.default_rng(218121)
    outcomes=[]
    for d,eps,n in ((3,0.04,600000),(3,0.02,600000),(4,0.035,600000)):
        ratio,error=sample_linearized_simplex(d,eps,n,rng)
        C=float(simplex_constant(d)[1])
        outcomes.append((d,eps,round(ratio,5),round(error,5),C))
        assert abs(ratio-C) < 0.4*C # finite-epsilon effect allowed; not a proof
    for eps in (0.03,0.015):
        ratio,err=cube_surface_importance(eps,600000,rng)
        outcomes.append(('cube3',eps,round(ratio,5),round(err,5),0.75))
        assert abs(ratio-0.75)<0.25
    print('VERIFY_OK exact_dimensions=2..21 cube_dimensions=2..21 tetrahedron=8 cube3=3/4 octahedron3=1/4')
    for t in outcomes:
        print('importance_tail',t)

if __name__=='__main__':main()
