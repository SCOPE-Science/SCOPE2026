#!/usr/bin/env python3
"""Exact independent checks for metric-product double-point quotients.
Run with: python verify_dp_product.py
"""
from fractions import Fraction as Q
from itertools import product, combinations
from math import prod, comb
import random
import sympy as S

def eqdist(q, length=1):
    return tuple(tuple(Q(0 if i==j else length) for j in range(q)) for i in range(q))

def line3(a=1,b=2):
    return ((Q(0),Q(a),Q(a+b)),(Q(a),Q(0),Q(b)),(Q(a+b),Q(b),Q(0)))

def product_dist(matrices):
    sizes=[len(a) for a in matrices]
    xs=list(product(*(range(k) for k in sizes)))
    mat=tuple(tuple(sum(matrices[i][x[i]][y[i]] for i in range(len(sizes))) for y in xs) for x in xs)
    return xs,mat

def dp(z,dist):
    d=[sum(z[j]*dist[i][j] for j in range(len(z))) for i in range(len(z))]
    return (max(d)-min(d))/2

def marginals(z,xs,sizes):
    return [tuple(sum(z[h] for h,x in enumerate(xs) if x[i]==a) for a in range(sizes[i]))
            for i in range(len(sizes))]

def all_test(mats,exhaustive=False):
    xs,D=product_dist(mats); n=len(xs)
    zlist=[]
    if exhaustive:
        zlist=(v for v in product((-1,0,1),repeat=n) if sum(v)==0)
    else:
        rng=random.Random(92743+n)
        zlist=[]
        for h in range(350):
            v=[rng.randrange(-5,6) for _ in range(n-1)]
            zlist.append((*v,-sum(v)))
    count=0
    for z in zlist:
        mar=marginals(z,xs,[len(a) for a in mats])
        a=dp(z,D)
        b=sum(dp(mar[i],mats[i]) for i in range(len(mats)))
        assert a==b,('norm identity',len(mats),z,a,b)
        count+=1
    # independently compare ranks of restricted distance-map on both sides
    Qn=S.eye(n)-S.ones(n,n)/n
    DM=S.Matrix(D)
    r=(Qn*DM*Qn).rank()
    rs=[]
    for A in mats:
        m=len(A); P=S.eye(m)-S.ones(m,m)/m
        rs.append((P*S.Matrix(A)*P).rank())
    assert r==sum(rs),(r,rs)
    # Verify a nonzero interaction kernel explicitly via 2x2 rectangle if at least two factors.
    if len(mats)>=2:
        iv={x:i for i,x in enumerate(xs)}
        base=[0]*n
        for a,b,s in [(0,0,1),(1,1,1),(0,1,-1),(1,0,-1)]:
            x=[0]*len(mats);x[0]=a;x[1]=b
            base[iv[tuple(x)]]=s
        assert sum(base)==0 and dp(base,D)==0
    print('product', [len(m) for m in mats],'samples',count,'ranks',r,rs,'OK')

def enumerate_vertex_count(q):
    # Coordinates z0,...,z_{q-2}, zlast=-sum previous. Inequalities z_i-z_j<=2.
    dim=q-1
    E=[]
    for i in range(q):
        v=[Q(0)]*dim
        if i<dim:v[i]=Q(1)
        else:v=[Q(-1)]*dim
        E.append(S.Matrix([int(x) for x in v]))
    inequalities=[list(E[a]-E[b]) for a in range(q) for b in range(q) if a!=b]
    verts=set()
    for inds in combinations(range(len(inequalities)),dim):
        A=S.Matrix([inequalities[i] for i in inds])
        if A.det()==0:continue
        sol=A.inv()*S.ones(dim,1)*2
        if all((S.Matrix(row).dot(sol)<=2) for row in inequalities):
            verts.add(tuple(sol))
    expect={tuple(S.Rational(2)*(int(i in U)-S.Rational(len(U),q)) for i in range(q-1)) for k in range(1,q) for U in combinations(range(q),k)}
    assert verts==expect,(q,len(verts),len(expect))
    assert len(verts)==2**q-2
    print('equilateral',q,'vertices',len(verts),'facets',q*(q-1),'OK')

def main():
    all_test([eqdist(2),eqdist(2)],True)
    all_test([eqdist(2),eqdist(3)],True)
    all_test([eqdist(3),eqdist(3)],True)
    all_test([eqdist(2),eqdist(2),eqdist(2)],True)
    all_test([eqdist(2,2),line3(2,3)],True)
    all_test([line3(),line3(3,1)],False)
    all_test([eqdist(2),eqdist(3),eqdist(2)],False)
    all_test([eqdist(2),eqdist(2),eqdist(2),eqdist(2)],False)
    for q in (2,3,4,5):enumerate_vertex_count(q)
    print('ALL EXACT PRODUCT-NORM, NULLITY, AND FACTOR-VERTEX TESTS PASSED')

if __name__=='__main__':main()
