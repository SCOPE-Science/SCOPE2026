"""Exact integer-arithmetic checks for a family of toric Nash charts.

The checks support, but do not replace, the symbolic proof in RESULT.md.
"""
from itertools import combinations
from math import gcd
from fractions import Fraction


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def primitive(x):
    g=gcd(*map(abs,x))
    return tuple(v//g for v in x)


def determinant(a, b, c):
    return dot(a, cross(b,c))


def verify(n):
    assert n>=2
    hilbert=[(1,0,0),(0,1,0),(0,0,1),(-1,-1,n)]
    minors=[determinant(*trip) for trip in combinations(hilbert,3)]
    assert list(map(abs,minors))==[1,n,1,1], minors
    v1=(1,1,1); v2=(0,-1,n+1); v3=(-1,0,n+1)
    diff=lambda x,y:tuple(a-b for a,b in zip(x,y))
    assert diff(v2,v1)==(-1,-2,n) and diff(v3,v1)==(-2,-1,n)
    cone=[(1,0,0),(0,1,0),(-1,-2,n),(-2,-1,n)]
    discovered=set()
    for a,b in combinations(cone,2):
        x=cross(a,b)
        if x==(0,0,0):continue
        if all(dot(x,g)>=0 for g in cone):discovered.add(primitive(x))
        if all(dot(x,g)<=0 for g in cone):discovered.add(primitive(tuple(-v for v in x)))
    g2=gcd(n,2);g3=gcd(n,3)
    r0=(0,0,1)
    rx=(n//g2,0,2//g2)
    ry=(0,n//g2,2//g2)
    rm=(n//g3,n//g3,3//g3)
    assert discovered=={r0,rx,ry,rm}, (n,discovered)
    assert all(gcd(*map(abs,r))==1 for r in discovered)
    # Dual facets: a two-ray face has a common annihilated primal extremal ray.
    cyc=[r0,rx,rm,ry]
    for i in range(4):
        a,b=cyc[i],cyc[(i+1)%4]
        assert sum(dot(a,x)==0 and dot(b,x)==0 for x in cone)==1
    indices=[gcd(*map(abs,cross(cyc[i],cyc[(i+1)%4]))) for i in range(4)]
    assert indices==[n//g2,n//(g2*g3),n//(g2*g3),n//g2]
    a=Fraction(g2-2,n)
    m=(a,a,Fraction(1))
    q_gor=(dot(m,rm)==1)
    assert q_gor==(g3==2*g2-1)
    assert q_gor==((n%2==1 and n%3!=0) or n%6==0)
    if q_gor:
        cartier_index=1 if n%6==0 else n
        assert all((cartier_index*v).denominator==1 for v in m)
        for i in range(1,cartier_index):
            assert any((i*v).denominator!=1 for v in m)
    nbad=sum(i>1 for i in indices)
    assert nbad==(0 if n==2 else 2 if n in (3,6) else 4)

for n in range(2,513):
    verify(n)
print('VERIFY_OK: independent dual-ray enumeration, lattice indices, and canonical index for n=2..512')
