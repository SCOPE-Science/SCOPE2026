#!/usr/bin/env python3
"""Exact rational checks for a two-community, two-zealot voter process.

Only the finite test cases are certified by execution; the full parameter theorem
uses the algebraic argument in the accompanying mathematical text.
"""
from fractions import Fraction as F
from math import sqrt


def formula(m, a, b, z):
    a,b,z=map(F,(a,b,z))
    h=(a*m*b + a*z + m*b*b + 2*m*b*z + z*z)
    inside=F(2*m*b*z*(m*b+z),(2*m*b+z)*h)
    across=F(z*(a*m*b+a*z+2*m*m*b*b-m*b*b+2*m*b*z+z*z), (2*m*b+z)*h)
    mean=F(m*b,(z+2*m*b))
    return inside,across,mean


def stationary_counts(m,a,b,z):
    """Independent master equation on the two population count coordinates."""
    a,b,z=map(F,(a,b,z))
    states=[(i,j) for i in range(m+1) for j in range(m+1)]
    N=len(states); index={v:k for k,v in enumerate(states)}
    Q=[[F(0) for _ in range(N)] for _ in range(N)]
    for k,(i,j) in enumerate(states):
        jumps=[((i+1,j),(m-i)*(a*i+b*j)),
               ((i-1,j),i*(a*(m-i)+b*(m-j)+z)),
               ((i,j+1),(m-j)*(a*j+b*i+z)),
               ((i,j-1),j*(a*(m-j)+b*(m-i)))]
        for dst,rate in jumps:
            if rate:
                h=index[dst]; Q[k][h]+=rate; Q[k][k]-=rate
    A=[[Q[j][i] for j in range(N)]+[F(0)] for i in range(N)]
    A[-1]=[F(1)]*N+[F(1)]
    for col in range(N):
        pivot=next(k for k in range(col,N) if A[k][col])
        A[col],A[pivot]=A[pivot],A[col]
        fac=A[col][col]
        A[col]=[v/fac for v in A[col]]
        for row in range(N):
            if row!=col:
                fac=A[row][col]
                if fac:
                    A[row]=[q-fac*w for q,w in zip(A[row],A[col])]
    pi=[A[i][-1] for i in range(N)]
    assert all(p>=0 for p in pi) and sum(pi)==1
    inside=sum(pi[k]*F(2*i*(m-i),m*(m-1)) for k,(i,j) in enumerate(states))
    cross=sum(pi[k]*F(i*(m-j)+(m-i)*j,m*m) for k,(i,j) in enumerate(states))
    mean=sum(pi[k]*F(i,m) for k,(i,j) in enumerate(states))
    return inside,cross,mean


def derivative_polynomial(m,h,r):
    return (h+1)+2*m*(h+1)*r+m*(h*m-1)*r*r-4*m*m*r*r*r-2*m*m*m*r*r*r*r


def unique_positive_root(m,h):
    lo=0.0; hi=1.0
    while derivative_polynomial(m,h,hi)>0: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if derivative_polynomial(m,h,mid)>0: lo=mid
        else:hi=mid
    return (lo+hi)/2


def main():
    tested=0
    for m in (2,3,4):
        for a,b,z in ((1,1,1),(F(1,2),F(1,3),F(3,2)),(3,2,1),(1,F(1,4),2)):
            calculated=stationary_counts(m,a,b,z)
            predicted=formula(m,a,b,z)
            assert calculated==predicted,(m,a,b,z,calculated,predicted)
            tested+=1
    assert formula(2,1,1,1)==(F(6,25),F(7,25),F(2,5))
    for m in (2,3,4,9,16,25,64,100,400,1600):
        for h in (F(1,3),F(1,1),F(5,1)):
            r=unique_positive_root(m,float(h))
            assert r>0
            assert derivative_polynomial(m,float(h),r*.999)>0
            assert derivative_polynomial(m,float(h),r*1.001)<0
            w=float(formula(m,h,r,1)[0]);
            assert w>float(formula(m,h,r*0.999,1)[0]);assert w>float(formula(m,h,r*1.001,1)[0])
            tested+=5
    for h in (0.5,1.,3.):
        m=200000
        r=unique_positive_root(m,h)
        assert abs(sqrt(m)*r-sqrt(h/2))<0.02
        assert abs(float(formula(m,h,r,1)[0])-1/(h+2))<0.02
        tested+=2
    print('EXACT_MASTER_EQUATIONS_OK',12,'cases')
    print('ALL_CHECKS_OK',tested)
    print('m2_a1_b1_z1',formula(2,1,1,1))
    print('m2_a1_z1_peak',unique_positive_root(2,1))


if __name__=='__main__':
    main()
