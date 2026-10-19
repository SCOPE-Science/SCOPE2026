#!/usr/bin/env python3
"""Exact arithmetic verification of a single-edge weighted-cube reachability theorem.

Run: python3 verify_one_defect_cube.py
Uses only the Python standard library. All results are independent of floating point.
"""
from fractions import Fraction as F
from math import gcd


def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def mul_z_minus(p, a):
    q=[F(0)]*(len(p)+1)
    for i,x in enumerate(p):q[i]-=a*x; q[i+1]+=x
    return trim(q)

def characteristic(m, c, lo, hi):
    """det(zI-J[lo:hi,lo:hi]), J_{i,i}=m+2 (i>0), J_{0,0}=m+2c."""
    if lo>=hi:return [F(1)]
    p0=[F(1)]; p1=[-F(m+2*c if lo==0 else m+2), F(1)]
    for i in range(lo+1,hi):
        p2=mul_z_minus(p1,F(m+2))
        t=F(i*(m-i+1))
        for j in range(len(p0)):p2[j]-=t*p0[j]
        p0,p1=p1,trim(p2)
    return p1

def modpoly(a,b):
    a=trim(a[:]); b=trim(b[:]);
    while len(a)>=len(b) and a !=[0]:
        s=a[-1]/b[-1]; i=len(a)-len(b)
        for j in range(len(b)):a[i+j]-=s*b[j]
        trim(a)
    return a

def gcdd(a,b):
    while b !=[0]:a,b=b,modpoly(a,b)
    return len(a)-1

def predicted(d,c,j):
    if c==1:return d+1
    m=d-1
    if j==0 or j==m:return 2*d
    f=characteristic(m,c,0,j)
    g=characteristic(m,c,j+1,m+1)
    return 2*d-gcdd(f,g)

def rank_mod(A,p):
    a=[list(row) for row in A]; rows=len(a); cols=len(a[0]); r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][j]%p),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j]%p,-1,p); a[r]=[(x*inv)%p for x in a[r]]
        for i in range(r+1,rows):
            mult=a[i][j]%p
            if mult:a[i]=[(x-mult*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==rows:break
    return r

def krylov(d,c,u,p):
    n=1<<d; scale=c.denominator; special=scale*c.numerator//c.denominator
    # Equivalent integer Laplacian, all ordinary conductances multiplied by scale.
    v=[int(i==u) for i in range(n)]; cols=[]
    for _ in range(2*d):
        cols.append(v)
        w=[0]*n
        for i in range(n):
            for bit in range(d):
                k=i^(1<<bit)
                conductance=special if {i,k}=={0,1} else scale
                w[i]+=conductance*(v[i]-v[k])
        v=[x%p for x in w]
    return rank_mod([[col[i] for col in cols] for i in range(n)],p)

def verify():
    count=0
    for d in range(2,7):
        m=d-1
        for c in [F(1,3),F(1,2),F(1),F(3,2),F(2),F(5)]:
            for j in range(m+1):
                x=(1<<j)-1
                want=predicted(d,c,j)
                assert d+1 <= want <= 2*d
                for t in [0,1]:
                    u=2*x+t
                    for p in [1000003,1000033]:
                        got=krylov(d,c,u,p)
                        assert got==want,(d,c,j,t,p,got,want)
                        count+=1
    # Exceptional d=4,m=3,j=1: lambda=5 +- sqrt(3), c=1 +- sqrt(3)/2.
    # Eigenvector in non-symmetric shell-coordinates: (-2,0,1,5-lambda).
    # Row equations imply (5-lambda)^2=3, and 3+2c=lambda.
    for sign in [-1,1]:
        # Use Q(sqrt(3)) arithmetic for each coordinate a+b*sqrt(3).
        lam=(F(5),F(sign)); c=(F(1),F(sign,2))
        y=[(F(-2),F(0)),(F(0),F(0)),(F(1),F(0)),(F(0),-F(sign))]
        def add(x,z):return (x[0]+z[0],x[1]+z[1])
        def mul(x,z):return(x[0]*z[0]+3*x[1]*z[1],x[0]*z[1]+x[1]*z[0])
        diag=[(F(3)+2*c[0],2*c[1])]+[(F(5),F(0))]*3
        for i in range(4):
            total=mul(diag[i],y[i])
            if i>0:total=add(total,mul((F(-i),F(0)),y[i-1]))
            if i<3:total=add(total,mul((F(-(3-i)),F(0)),y[i+1]))
            assert total==mul(lam,y[i]),(sign,i,total)
            count+=1
        assert y[1]==(0,0)
    # Confirm all roots of the exceptional right 2x2 block are 5+-sqrt(3).
    assert characteristic(3,F(2),2,4)==[F(22),F(-10),F(1)]
    count+=1
    print('VERIFY_OK',count,'exact arithmetic checks')
if __name__=='__main__':verify()
