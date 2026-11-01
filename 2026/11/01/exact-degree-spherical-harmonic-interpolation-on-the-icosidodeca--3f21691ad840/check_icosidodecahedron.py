#!/usr/bin/env python3
"""Exact certificate for individual-degree spherical-harmonic interpolation
on the thirty vertices of a regular icosidodecahedron.

Requires only Python 3.10+ standard library. Rational arithmetic takes place in
Q(phi), phi**2=phi+1. Nonzero determinants through degree 262 are certified by
reduction modulo 1009, not by floating-point diagonalization.
"""
from fractions import Fraction as F

Z=(F(0),F(0)); U=(F(1),F(0)); PHI=(F(0),F(1))

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def scale(x,c):return (x[0]*c,x[1]*c)
def mul(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def inv(x):
    a,b=x
    n=a*a+a*b-b*b
    if n==0:raise ZeroDivisionError
    return ((a+b)/n,-b/n)
def dot(x,y):
    z=Z
    for a,b in zip(x,y):z=add(z,mul(a,b))
    return z

def configuration():
    """The edge-midpoints of the icosahedron, and one of each antipodal pair."""
    v=[]
    for s in (-1,1):
        for t in (-1,1):
            a=scale(U,s); b=scale(PHI,t)
            v += [(Z,a,b),(b,Z,a),(a,b,Z)]
    assert len(set(v))==12
    edge=[(i,j) for i in range(12) for j in range(i+1,12)
          if dot(v[i],v[j])==PHI]
    assert len(edge)==30
    c=scale(sub(PHI,U),F(1,2)) # (2 phi)^-1
    points=[tuple(mul(c,add(v[i][j],v[k][j])) for j in range(3))
            for i,k in edge]
    assert len(set(points))==30
    assert all(dot(x,x)==U for x in points)
    axes=[]
    for x in points:
        if all(x!=y and x!=tuple(neg(t) for t in y) for y in axes):
            axes.append(x)
    assert len(axes)==15
    assert all(any(tuple(neg(t) for t in x)==y for y in points) for x in points)
    R=sub(scale(PHI,2),U)
    a=scale(sub(R,U),F(1,4)); b=scale(U,F(1,2)); c=scale(add(R,U),F(1,4))
    allowed={Z,U,neg(U),a,neg(a),b,neg(b),c,neg(c)}
    table=[[dot(x,y) for y in axes] for x in axes]
    assert all(x in allowed for row in table for x in row)
    assert all(row.count(U)==1 and row.count(Z)==2 for row in table)
    assert all(row[j]==table[j][i] for i,row in enumerate(table) for j in range(15))
    return table

def legendre(x,n):
    if n==0:return U
    prev,now=U,x
    for k in range(1,n):
        prev,now=now,scale(sub(scale(mul(x,now),2*k+1),scale(prev,k)),F(1,k+1))
    return now

def rank_exact(a):
    a=[row[:] for row in a];m=len(a);rank=0
    for j in range(m):
        pivot=next((i for i in range(rank,m) if a[i][j]!=Z),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        ip=inv(a[rank][j])
        for i in range(rank+1,m):
            if a[i][j]!=Z:
                c=mul(a[i][j],ip)
                for k in range(j+1,m):a[i][k]=sub(a[i][k],mul(c,a[rank][k]))
                a[i][j]=Z
        rank+=1
    return rank

def rank_finite(a,p):
    a=[row[:] for row in a];m=len(a);rank=0
    for j in range(m):
        pivot=next((i for i in range(rank,m) if a[i][j]!=0),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        z=pow(a[rank][j],-1,p)
        for i in range(rank+1,m):
            if a[i][j]:
                c=a[i][j]*z%p
                for k in range(j+1,m):a[i][k]=(a[i][k]-c*a[rank][k])%p
                a[i][j]=0
        rank+=1
    return rank

def certify():
    tbl=configuration()
    targets=[1,3,5,7,9,11,10,15,14,15,15,15,15,15,14]
    for n in range(15):
        vals={x:legendre(x,n) for row in tbl for x in row}
        a=[[vals[x] for x in row] for row in tbl]
        assert rank_exact(a)==targets[n],(n,'exact rank')
        if n in (8,14):
            assert all(sum((x[0] for x in row),F(0))==0 and
                       sum((x[1] for x in row),F(0))==0 for row in a)
    print('PASS: exact Q(phi) ranks at all degrees 0..14:', targets)

    p=1009
    r=244 # r^2=5 (mod p)
    assert r*r%p==5
    phi=(1+r)*pow(2,-1,p)%p
    assert (phi*phi-phi-1)%p==0
    def reduce(x):
        def q(z):
            assert z.denominator%p!=0
            return z.numerator*pow(z.denominator,-1,p)%p
        return (q(x[0])+phi*q(x[1]))%p
    pt=[[reduce(x) for x in row] for row in tbl]
    arguments={x for row in pt for x in row}
    P={x:[1,x] for x in arguments}
    for n in range(1,263):
        for x in arguments:
            P[x].append(((2*n+1)*x*P[x][n]-n*P[x][n-1])*pow(n+1,-1,p)%p)
    for n in range(15,263):
        a=[[P[x][n] for x in row] for row in pt]
        assert rank_finite(a,p)==15,(n,'modular determinant')
    print('PASS: determinant nonzero modulo 1009 in every degree 15..262 (248 degrees)')

    # Off-diagonal absolute inner products are <= (sqrt(5)+1)/4 < sqrt(3)/2.
    # Standard Bernstein inequality for Legendre polynomials and pi>3 imply
    # |P_n(t)|<2/sqrt(3*(n+1/2)) for n>=1 at these 14 off-diagonal sites.
    # Thus every 15x15 Gram has Gershgorin radius <1 for n>=263.
    assert 3*(F(263)+F(1,2))>28**2
    print('PASS: exact rational strict-diagonal-dominance cutoff at degree 263')
    print('PASS: complete all-degree rank classification')

if __name__=='__main__':certify()
