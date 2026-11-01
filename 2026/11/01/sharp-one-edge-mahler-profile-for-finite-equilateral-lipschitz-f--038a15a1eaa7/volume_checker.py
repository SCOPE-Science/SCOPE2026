#!/usr/bin/env python3
"""Checks exact volume formulas and optional independent convex-hull volumes.

Run: python volume_checker.py
Requires Python 3; the geometric cross-check also requires numpy and scipy.
Finite checks corroborate but do not prove the all-dimensional theorem.
"""
from fractions import Fraction as F
from math import comb, factorial


def beta_cdf_int(s, N, r):
    """Regularized beta CDF with integer parameters s,N-s, as a binomial tail."""
    return sum(F(comb(N - 1, j)) * r**j * (1 - r)**(N - 1 - j)
               for j in range(s, N))


def independent_volume_sums(N, r):
    # Each order chamber of the Lipschitz ball is a unit simplex.
    p = F(2, N - 1) * sum((N - s) * beta_cdf_int(s, N, r)
                            for s in range(1, N))
    # The root polytope facets are products of two simplices.
    d = N - 1
    root = F(sum(comb(N, k) * comb(N - 2, k - 1)
                 for k in range(1, N)), factorial(d))
    cap = F(sum(comb(N - 2, k - 1)**2
                for k in range(1, N)), factorial(d))
    q = root + 2 * (1 / r - 1) * cap
    return p, q


def closed_volumes(N, r):
    b = F(2 * comb(2*N - 4, N - 2), factorial(N - 1))
    return r*(2*(N-1)-(N-2)*r), b*(1/r+F(N-2,N-1))


def exact_checks():
    count = 0
    for N in range(3, 41):
        for r in [F(1,6), F(1,3), F(1,2), F(2,3), F(5,6), F(1,1)]:
            p,q = independent_volume_sums(N,r)
            P,Q = closed_volumes(N,r)
            assert p == P and q == Q, (N,r,p,q,P,Q)
            count += 2
        if N >= 4:
            rstar = F(N-1,2*(N-2))
            b=F(2*comb(2*N-4,N-2),factorial(N-1))
            p,q=closed_volumes(N,rstar)
            _,qe=closed_volumes(N,F(1))
            pe=F(N)
            ratio=(p*q)/(pe*qe)
            assert ratio == F(9*(N-1)**2,4*N*(2*N-3))
            assert F(0)<rstar<F(1)
            assert p*q == b*F(9*(N-1),4)
            count += 3
    return count


def geometric_checks():
    import numpy as np
    from scipy.spatial import ConvexHull, HalfspaceIntersection
    count=0
    for N in range(3,8):
        d=N-1
        for r0 in (0.3,0.7,1.0):
            normals=[]
            for i in range(N):
                for j in range(i+1,N):
                    v=np.zeros(d)
                    if i: v[i-1] += 1.
                    if j: v[j-1] -= 1.
                    if (i,j)==(1,2): v/=r0
                    normals.extend((v,-v))
            E=np.array(normals)
            Qh=ConvexHull(E).volume
            hs=np.column_stack([E,-np.ones(len(E))])
            H=HalfspaceIntersection(hs,np.zeros(d))
            Ph=ConvexHull(H.intersections).volume
            P,Q=closed_volumes(N,F(str(r0)))
            assert abs(Qh-float(Q))<1e-8, (N,r0,Qh,Q)
            assert abs(Ph-float(P))<1e-8, (N,r0,Ph,P)
            count+=2
    return count


if __name__=='__main__':
    ex=exact_checks()
    geo=geometric_checks()
    print(f'CHECK_OK exact_volume_identities={ex} independently_computed_convex_hull_volumes={geo} parameter_N=3..40')
