"""Finite numerical diagnostics for the hollow-symmetric Monge simplex.

Requires NumPy. Mathematical proofs are independent of these diagnostics.
"""
from __future__ import annotations
import math
import numpy as np


def vertices(n: int):
    for a in range(1, n):
        for b in range(1, n - a + 1):
            v = np.zeros((n, n), dtype=float)
            v[:a, n-b:] = 1.0/(2*a*b)
            v[n-b:, :a] = 1.0/(2*a*b)
            assert abs(v.sum()-1.0)<1.e-12
            assert np.array_equal(v, v.T)
            assert np.all(np.diag(v)==0)
            yield (a,b), v


def rectangle_scores(x: np.ndarray, n: int):
    """x[i,k] is a corner-indexed independent Gaussian coordinate."""
    s = x.cumsum(axis=0).cumsum(axis=1)
    return {(a,b):s[a-1,b-1]/(a*b)
            for a in range(1,n) for b in range(1,n-a+1)}


def gaussian_from_corner(x: np.ndarray, n: int):
    g = np.zeros((n,n), dtype=float)
    for i in range(n-1):
        for k in range(n-i-1):
            j=n-1-k
            assert i<j
            g[i,j]=g[j,i]=x[i,k]/math.sqrt(2)
    return g


def checks(seed=1739):
    rng=np.random.default_rng(seed)
    checked=0
    for n in range(3,11):
        vs=list(vertices(n))
        assert len(vs)==n*(n-1)//2
        for _ in range(72):
            x=rng.standard_normal((n-1,n-1))
            g=gaussian_from_corner(x,n)
            scores=rectangle_scores(x,n)
            direct={idx:float((g*v).sum()) for idx,v in vs}
            assert all(abs(direct[idx]-scores[idx]/math.sqrt(2))<1e-12 for idx in direct)
            cen=np.ones((n,n))-np.eye(n)
            gp=g-(g*cen).sum()/(cen*cen).sum()*cen
            s=np.array([float((gp*v).sum()) for _,v in vs])
            ran=(max(scores.values())-min(scores.values()))/math.sqrt(2)
            assert abs(s.max()-s.min()-ran)<1e-11
            norm=np.linalg.norm(gp)
            assert norm>0
            u=gp/norm
            width_direct=max(float((u*v).sum()) for _,v in vs)-min(float((u*v).sum()) for _,v in vs)
            assert abs(width_direct-ran/norm)<1e-11
            checked+=1
    print(f"Exact Gaussian/vertex/support/projected-sphere checks: {checked} passed")

    # An increasing triangular cutoff approximates the infinite rectangle field.
    cutoff=95
    repetitions=4800
    ranges=np.empty(repetitions)
    plus_11=0
    minus_11=0
    perimeters=np.empty(repetitions)
    for j in range(repetitions):
        x=rng.standard_normal((cutoff-1,cutoff-1))
        s=x.cumsum(axis=0).cumsum(axis=1)
        a=np.arange(1,cutoff)[:,None]
        b=np.arange(1,cutoff)[None,:]
        mask=a+b<=cutoff
        z=np.where(mask,s/(a*b),np.nan)
        mx=np.nanargmax(z); mn=np.nanargmin(z)
        ra,rb=np.unravel_index(mx,z.shape)
        sa,sb=np.unravel_index(mn,z.shape)
        ranges[j]=float(np.nanmax(z)-np.nanmin(z))
        perimeters[j]=max(ra+rb+2,sa+sb+2)
        plus_11+=(ra==0 and rb==0)
        minus_11+=(sa==0 and sb==0)
    print(f"Triangle cutoff {cutoff} and samples {repetitions}: mean range = {ranges.mean():.6f}; SD = {ranges.std(ddof=1):.6f}")
    print(f"Observed (1,1) maximum fraction = {plus_11/repetitions:.6f}; minimum fraction = {minus_11/repetitions:.6f}")
    print(f"Observed max winning perimeter: {int(perimeters.max())}; 95th percentile: {np.quantile(perimeters,.95):.1f}")
    print("Finite simulations do not certify limit laws or infinite-index stabilization.")


if __name__ == '__main__':
    checks()
