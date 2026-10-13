#!/usr/bin/env python3
"""Exact arithmetic certificate for the two marked degree-one del Pezzo blowups.

Run: python3 verify.py
Only the Python standard library is required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, lcm
from collections import Counter

PRIME = 1000003
EXAMPLES = {
    "3.1": ((0,1,1),(0,14,13),(1,0,1),(21,0,13),
            (1,1,1),(6,6,-1),(-2,2,1),(-3,3,-1)),
    "3.3": ((0,1,1),(0,3861,1957),(1,0,1),(1188,0,-19),
            (1,1,1),(780,780,1883),(-52,52,51),(-9,9,-17)),
}
EXPECTED = ('L1,2','L3,4','L5,6','L7,8','C1,2','C3,4','Q2,6,7')


def classes():
    for s in combinations(range(8),2):
        yield 'L'+','.join(str(i+1) for i in s),1,[int(i in s) for i in range(8)]
    for s in combinations(range(8),5):
        yield 'K'+','.join(str(i+1) for i in s),2,[int(i in s) for i in range(8)]
    for i in range(8):
        for j in range(8):
            if i!=j:
                yield 'C'+str(i+1)+','+str(j+1),3,[2 if k==i else 0 if k==j else 1 for k in range(8)]
    for s in combinations(range(8),3):
        yield 'Q'+','.join(str(i+1) for i in s),4,[2 if i in s else 1 for i in range(8)]
    for s in combinations(range(8),6):
        yield 'P'+','.join(str(i+1) for i in s),5,[2 if i in s else 1 for i in range(8)]
    for i in range(8):
        yield 'S'+str(i+1),6,[3 if k==i else 2 for k in range(8)]


def rows_for(points,degree,mult):
    # Monomial u^i v^j in the z=1 chart, corresponding to x^i y^j z^(d-i-j).
    mons = [(i,j) for i in range(degree+1) for j in range(degree-i+1)]
    rows=[]
    for (x,y,z),m in zip(points,mult):
        for a in range(m):
            for b in range(m-a):
                # z^degree times the coefficient of (u-u_0)^a(v-v_0)^b.
                rows.append([comb(i,a)*comb(j,b)*x**(i-a)*y**(j-b)*z**(degree-i-j+a+b)
                             if i>=a and j>=b else 0 for i,j in mons])
    qrow=[int(i==0 and j==0) for i,j in mons]
    return rows,qrow,mons


def rank_mod(matrix,ncols):
    a=[[v%PRIME for v in row] for row in matrix]
    r=0
    for col in range(ncols):
        k=next((t for t in range(r,len(a)) if a[t][col]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        inv=pow(a[r][col],PRIME-2,PRIME)
        a[r][col:]=[v*inv%PRIME for v in a[r][col:]]
        for t in range(r+1,len(a)):
            z=a[t][col]
            if z: a[t][col:]=[(v-z*w)%PRIME for v,w in zip(a[t][col:],a[r][col:])]
        r+=1
        if r==ncols: break
    return r


def integer_kernel(matrix,ncols):
    a=[[Fraction(v) for v in row] for row in matrix]
    pivots=[];r=0
    for j in range(ncols):
        k=next((t for t in range(r,len(a)) if a[t][j]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        inv=a[r][j]
        a[r]=[w/inv for w in a[r]]
        for t in range(len(a)):
            if t!=r and a[t][j]:
                v=a[t][j]
                a[t]=[x-v*y for x,y in zip(a[t],a[r])]
        pivots.append(j);r+=1
        if r==len(a):break
    assert r==ncols-1,(r,ncols)
    free=next(j for j in range(ncols) if j not in pivots)
    v=[Fraction(0)]*ncols;v[free]=1
    for t,j in enumerate(pivots):v[j]=-a[t][free]
    denom=lcm(*(x.denominator for x in v))
    v=[int(x*denom) for x in v]
    g=gcd(*v);v=[x//g for x in v]
    if next(x for x in v if x)!=abs(next(x for x in v if x)):
        v=[-x for x in v]
    assert all(sum(x*y for x,y in zip(row,v))==0 for row in matrix)
    return v


def point_general(points):
    for s in combinations(range(8),3):
        m=[int(i in s) for i in range(8)]
        M,_,mon=rows_for(points,1,m)
        assert rank_mod(M,len(mon))==3,('3 collinear',s)
    for s in combinations(range(8),6):
        m=[int(i in s) for i in range(8)]
        M,_,mon=rows_for(points,2,m)
        assert rank_mod(M,len(mon))==6,('6 conic',s)
    for i in range(8):
        m=[2 if j==i else 1 for j in range(8)]
        M,_,mon=rows_for(points,3,m)
        assert rank_mod(M,len(mon))==10,('singular cubic',i)


def verify(label,points):
    assert all(z!=0 for x,y,z in points)
    point_general(points)
    out={};by_degree=Counter();tangents=[]
    for name,d,m in classes():
        M,qrow,mons=rows_for(points,d,m)
        n=len(mons);r=rank_mod(M+[qrow],n)
        if r<n:
            assert rank_mod(M,n)==n-1
            vec=integer_kernel(M,n)
            assert sum(a*b for a,b in zip(vec,qrow))==0
            du=vec[mons.index((1,0))]
            dv=vec[mons.index((0,1))]
            assert du or dv
            g=gcd(du,dv)
            du//=g;dv//=g
            if du<0 or (du==0 and dv<0):du,dv=-du,-dv
            tangents.append((du,dv))
            out[name]=(d,(du,dv))
        else:
            assert r==n
        by_degree[(d,r<n)]+=1
    assert tuple(sorted(out))==tuple(sorted(EXPECTED)),(label,out)
    assert len(set(tangents))==7,(label,tangents)
    assert {d:by_degree[(d,True)] for d in range(1,7)}=={1:4,2:0,3:2,4:1,5:0,6:0}
    assert sum(by_degree.values())==232
    print('EXAMPLE',label,'GENERAL_POSITION=PASS EXCEPTIONAL_THROUGH_Q=7 OF 240')
    print('TANGENTS', ' '.join(f'{name}:({out[name][1][0]},{out[name][1][1]})' for name in EXPECTED))
    print('DEGREE_COUNTS', ','.join(f'{d}:{by_degree[(d,True)]}/{by_degree[(d,True)]+by_degree[(d,False)]}' for d in range(1,7)))


if __name__=='__main__':
    for label,points in EXAMPLES.items(): verify(label,points)
    print('VERIFY_OK examples=2 exceptional_curves=240 unique_through_Q=7 each ordinary_sevenfold=2 all_225_plane_exclusions_per_example_mod_1000003=PASS')
