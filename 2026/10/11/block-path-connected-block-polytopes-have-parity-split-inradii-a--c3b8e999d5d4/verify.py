#!/usr/bin/env python3
"""Exact combinatorial facet checks and independent numerical inradius replay."""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def facets(n):
    # Nonnegative facets followed by each odd-length alternating-sign facet.
    normals = [-np.eye(n)[i] for i in range(n)]
    rhs = [0.0] * n
    signs = []
    for k in range(1,n+1,2):
        for ind in combinations(range(n),k):
            a=np.zeros(n)
            for j,i in enumerate(ind):
                a[i]=1 if j%2==0 else -1
            normals.append(a)
            rhs.append(1.0)
            signs.append(a)
    return np.array(normals),np.array(rhs),np.array(signs)


def formula(n):
    if n%2==0:
        return 1.0/(1.0+sqrt(n-1.0))
    return 2.0/(2.0+sqrt(n)+sqrt(n-2.0))


def contact_point(n,rho,epsilon=0.0):
    if n%2==0:
        c=np.full(n,rho)
        if n>=4:
            c[1:-1]+=epsilon
    else:
        m=(n-1)//2
        delta=(sqrt(n)-sqrt(n-2))*rho/(n-1)
        c=np.array([rho+delta if j%2 else rho for j in range(n)])
        if n>=5 and epsilon>0:
            c[2:-2:2]+=epsilon
            c[1:-1:2]+=epsilon*(m-1)/m
    return c


def all_vertices(n):
    vertices=[np.zeros(n)]
    for i in range(n):
        for j in range(i,n):
            v=np.zeros(n)
            v[i:j+1]=1
            vertices.append(v)
    return np.array(vertices)


for n in range(2,15):
    A,b,S=facets(n)
    r=formula(n)
    c=contact_point(n,r)
    distances=b-A@c
    norm=np.linalg.norm(A,axis=1)
    slack=distances-r*norm
    assert slack.min()>-1e-10,(n,slack.min())

    # Independent full inequality LP: maximize r over center and radius.
    lp=linprog(np.r_[np.zeros(n),-1.0],A_ub=np.c_[A,norm],b_ub=b,
               bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert lp.success,(n,lp.message)
    assert abs(lp.x[-1]-r)<2e-9,(n,lp.x[-1],r)

    # The two explicit upper-bound certificates.
    if n>=3:
        a=np.zeros(n)
        bcert=np.zeros(n)
        if n%2==0:
            a[:-1]=[1 if i%2==0 else -1 for i in range(n-1)]
            bcert[1:]=[1 if i%2==0 else -1 for i in range(n-1)]
        else:
            a[:]=[1 if i%2==0 else -1 for i in range(n)]
            bcert[1:-1]=[1 if i%2==0 else -1 for i in range(n-2)]
        assert np.all(a+bcert==np.eye(n)[0]+np.eye(n)[-1])
        assert abs(r*(2+np.linalg.norm(a)+np.linalg.norm(bcert))-2)<1e-12
        assert abs(a@c+r*np.linalg.norm(a)-1)<1e-11
        assert abs(bcert@c+r*np.linalg.norm(bcert)-1)<1e-11
        assert abs(c[0]-r)<1e-11 and abs(c[-1]-r)<1e-11

        if n>=4:
            # Construct strict relative interior at all non-forced facets.
            original_active=np.where(abs(slack)<1e-10)[0]
            slopes=(A@contact_point(n,r,1.0)-A@c)
            epsbound=1.0/200.0
            for idx,s in enumerate(slack):
                if s>1e-10 and slopes[idx]>0:
                    epsbound=min(epsbound,s/(4*slopes[idx]))
            eps=max(1e-12,epsbound)
            c2=contact_point(n,r,eps)
            sl2=b-A@c2-r*norm
            assert sl2.min()>-1e-10,(n,sl2.min())
            forced=[0,n-1]
            for special in [a,bcert]:
                matches=np.where((np.abs(A-special).max(axis=1)<1e-10))[0]
                assert len(matches)==1
                forced.append(int(matches[0]))
            active=np.where(abs(sl2)<1e-9)[0]
            assert set(active)==set(forced),(n,active,forced,original_active)
            assert np.linalg.matrix_rank(A[active])==3,(n,active)

    # Independent facet/convex-hull comparison in all low dimensions.
    if n<=6:
        v=all_vertices(n)
        assert np.max(A@v.T-b[:,None])<1e-10
        hull=ConvexHull(v)
        expected=np.unique(np.c_[A,b],axis=0)
        identified=set()
        for h in hull.equations:
            unit=h[:-1]; offset=h[-1]
            if abs(offset)<1e-8:
                # At origin, the only facets have negative coordinate normals.
                cand=np.r_[unit/np.max(abs(unit)),0.0]
            else:
                cand=np.r_[-unit/offset,1.0]
            matches=np.where(np.max(abs(expected-cand),axis=1)<1e-7)[0]
            assert len(matches)==1,(n,cand)
            identified.add(int(matches[0]))
        assert len(identified)==len(expected),(n,len(identified),len(expected))

print('VERIFY_OK block-path-insphere n=2..14 full_facet_lp=yes center_witnesses=yes incenter_dim=n-3 convex_hull_facets=n2..6')
