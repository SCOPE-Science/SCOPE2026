"""Reproducible exact geometric checks for the uniform root-polytope moment law.
Dependencies for the independent hull tests: numpy >=1.24, scipy >=1.10.
The moment algebra and random-sampler tests otherwise use Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, sqrt, isclose
import random


def det(A):
    """Exact rational determinant by fraction-preserving elimination."""
    A = [[F(z) for z in row] for row in A]
    n = len(A)
    if n == 0: return F(1)
    result=F(1)
    for i in range(n):
        j=next((j for j in range(i,n) if A[j][i]),None)
        if j is None:return F(0)
        if j!=i:A[j],A[i]=A[i],A[j];result=-result
        p=A[i][i];result*=p
        for j in range(i+1,n):
            a=A[j][i]/p
            for k in range(i+1,n):A[j][k]-=a*A[i][k]
            A[j][i]=F(0)
    return result


def claimed_trace(n):return F(4*(n-1)*(2*n-1),n*(n+1)**2)
def claimed_gram_cov(n):return F(4*(2*n-1),n*(n+1)**2)
def claimed_coordinate_vol(n):return F(comb(2*n-2,n-1),factorial(n-1))


def chamber_moment(n):
    # Formula obtained independently by Beta-Dirichlet integration.
    z=comb(2*n-2,n-1)
    check=sum(comb(n,k)*comb(n-2,k-1) for k in range(1,n))
    assert z==check
    result=F(0)
    for k in range(1,n):
        p=F(comb(n,k)*comb(n-2,k-1),z)
        result+=p*F(n-1,n+1)*(F(2,k+1)+F(2,n-k+1))
    return result


def hull_integration(n):
    """Independent simplex coning of a numerical convex hull, exact integral on each cone."""
    import numpy as np
    from scipy.spatial import ConvexHull
    d=n-1
    vertices=[]
    for i in range(n):
        for j in range(n):
            if i==j:continue
            v=[(int(i==r)-int(j==r)) for r in range(d)]
            vertices.append(v)
    hull=ConvexHull(np.array(vertices,dtype=float))
    volume=F(0);moment=F(0)
    for inds in hull.simplices:
        Vs=[vertices[i] for i in inds]
        if len(Vs)!=d:raise RuntimeError('incorrect simplex facet rank')
        determinant=abs(det(list(zip(*Vs))))
        # facet triangulation of convex hull with origin in interior
        simplex_volume=determinant/F(factorial(d))
        s=[sum(v[i] for v in Vs) for i in range(d)]
        def gram(v,w):return sum(v[i]*w[i] for i in range(d))+sum(v)*sum(w)
        expectation=F(sum(gram(v,v) for v in Vs)+gram(s,s),(d+1)*(d+2))
        volume+=simplex_volume
        moment+=simplex_volume*expectation
    moment/=volume
    print('n',n,'simplex count',len(hull.simplices),'coord-volume',volume,
          'trace-cov',moment,'target',claimed_trace(n))
    assert volume==claimed_coordinate_vol(n)
    assert moment==claimed_trace(n)


def sampler_radii(n, samples=10000, seed=1251):
    # Independent Monte Carlo diagnostic; never an infinite-dimensional proof.
    rng=random.Random(seed+n)
    weights=[comb(n,k)*comb(n-2,k-1) for k in range(1,n)]
    cum=[];z=0
    for w in weights:z+=w;cum.append(z)
    assert z==comb(2*n-2,n-1)
    total=0;total_sq=0;fluct=0;fluct_sq=0
    for _ in range(samples):
        r=rng.randrange(z)
        k=next(i+1 for i,v in enumerate(cum) if r<v)
        a=[rng.expovariate(1.0) for _ in range(k)]
        b=[rng.expovariate(1.0) for _ in range(n-k)]
        asu=sum(a);bsu=sum(b)
        radius=rng.random()**(1/(n-1))
        normsq=radius*radius*(sum((x/asu)**2 for x in a)+sum((x/bsu)**2 for x in b))
        total+=normsq;total_sq+=normsq*normsq
        fluctn=sqrt(n)*(n*normsq/8-1)
        fluct+=fluctn;fluct_sq+=fluctn**2
    print('sampler',n,'E-radius-squared',total/samples,'target',float(claimed_trace(n)),
          'CLT normalized mean/second moment',fluct/samples,fluct_sq/samples)
    assert abs(total/samples-float(claimed_trace(n)))<0.015*float(claimed_trace(n))


def main():
    for n in range(2,24):assert chamber_moment(n)==claimed_trace(n)
    for n in range(3,7):hull_integration(n)
    for n in (40,160,400):sampler_radii(n,3000)
    print('ALL ROOT-POLYTOPE MOMENT IDENTITIES AND INDEPENDENT HULL CHECKS PASSED')
if __name__=='__main__':main()
