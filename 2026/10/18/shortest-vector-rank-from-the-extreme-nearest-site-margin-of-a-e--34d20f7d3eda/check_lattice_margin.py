#!/usr/bin/env python3
"""Exact rational planar checks and independent orthogonal-lattice comparisons.

The analytical all-dimensional lattice theorem is proved separately; finite checks
provide reproducible regression tests and do not certify its infinite quantifiers.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod


def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def area(P):
    return abs(sum(cross(P[i],P[(i+1)%len(P)]) for i in range(len(P)))/2) if len(P)>=3 else Q(0)

def clip(poly, v, c):
    # Retain points obeying 2 <x,v> <= c.
    def side(p):return 2*(p[0]*v[0]+p[1]*v[1])-c
    out=[]
    if not poly:return out
    for a,b in zip(poly,poly[1:]+poly[:1]):
        fa,fb=side(a),side(b)
        if fa<=0:out.append(a)
        if (fa<0 and fb>0) or (fa>0 and fb<0):
            t=fa/(fa-fb)
            out.append((a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1])))
    return out

def cell(basis,t,N=4):
    u,w=basis
    verts=[(Q(-9),Q(-9)),(Q(9),Q(-9)),(Q(9),Q(9)),(Q(-9),Q(9))]
    for i,j in product(range(-N,N+1),repeat=2):
        if (i,j)==(0,0):continue
        v=(i*u[0]+j*w[0], i*u[1]+j*w[1]); vv=v[0]**2+v[1]**2
        verts=clip(verts,v,vv-t)
        if not verts:break
    return verts

def det(B):return abs(cross(*B))
def near_gap(x,B,N=5):
    u,w=B
    gaps=[]
    for i,j in product(range(-N,N+1),repeat=2):
        if i==j==0:continue
        v=(i*u[0]+j*w[0],i*u[1]+j*w[1]); gaps.append(v[0]**2+v[1]**2-2*(x[0]*v[0]+x[1]*v[1]))
    return min(gaps)

def verify(B,epses,coef,rank):
    lam=min((i*B[0][0]+j*B[1][0])**2+(i*B[0][1]+j*B[1][1])**2
            for i,j in product(range(-4,5),repeat=2) if (i,j)!=(0,0))
    V=cell(B,Q(0)); assert area(V)==det(B), (area(V),det(B))
    for eps in epses:
        S=cell(B,lam-eps)
        assert all(near_gap(x,B)>=lam-eps for x in S)
        F=area(S)/det(B)
        if rank==2:assert F==coef*eps**2,(F,coef*eps**2)
        else:assert abs(float(F/eps-coef))<0.05,(eps,F/eps,coef)
        print('PLANAR',len(S),'epsilon',str(eps),'survival',str(F),'scaled',str(F/eps**rank))
    for p in V[::max(1,len(V)//5)]:
        # Exact symmetric shrunk point is interior to the original cell.
        x=(p[0]/Q(4),p[1]/Q(4)); delta=near_gap(x,B)
        assert delta>=0
        R=cell(B,delta)
        assert all(near_gap(z,B)>=delta for z in R)
    print('EXACT_PLANAR_OK', 'shortest_rank',rank,'limit_constant',str(coef))


def orthogonal_check():
    lengths=(Q(1),Q(3,2),Q(2))
    eps=Q(1,17); t=lengths[0]**2-eps
    p=prod(1-t/L**2 for L in lengths)
    # Exact cubature of a Cartesian product of shifted Voronoi inequalities.
    # At the boundary, each coordinate independently has feasible width L-t/L.
    constrained_volume=prod(L-t/L for L in lengths)
    assert p==constrained_volume/prod(lengths)
    # Directly compare competitor gaps at rational interior points.
    for nums in product(range(-2,3),repeat=3):
        x=[L*Q(n,6) for n,L in zip(nums,lengths)]
        direct=min(sum((i*L)**2-2*i*L*xx for i,L,xx in zip(k,lengths,x))
                   for k in product(range(-2,3),repeat=3) if any(k))
        coordinate=min(L**2-2*L*abs(xx) for L,xx in zip(lengths,x))
        assert direct==coordinate
    # All three possible ranks in dimension three give different endpoint orders.
    for ls, r in [((Q(1),Q(2),Q(3)),1),((Q(1),Q(1),Q(2)),2),((Q(1),Q(1),Q(1)),3)]:
        u=Q(1,31)
        survival=prod(1-(Q(1)-u)/L**2 for L in ls)
        nonminimal=prod(1-Q(1)/L**2 for L in ls if L>1)
        assert abs(float(survival/u**r-nonminimal))<Q(1,8)
    print('ORTHOGONAL_3D_OK','survival',str(p),'points',125,'rank_classes',3)

if __name__=='__main__':
    B1=((Q(1),Q(0)),(Q(2,5),Q(6,5)))
    B2=((Q(1),Q(0)),(Q(5,13),Q(12,13)))
    verify(B1,[Q(1,20),Q(1,40),Q(1,80)],Q(5,12),1)
    verify(B2,[Q(1,20),Q(1,40),Q(1,80)],Q(169,144),2)
    orthogonal_check()
    print('LATTICE_MARGIN_TAIL_OK')
