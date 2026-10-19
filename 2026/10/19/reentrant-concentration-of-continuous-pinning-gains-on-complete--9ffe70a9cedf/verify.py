#!/usr/bin/env python3
"""Standalone finite arithmetic checks for bipartite pinning-gain allocation.

Requires Python 3 standard library only. Run: python verify.py
Finite tests supplement, and do not replace, the analytical proof.
"""
import math
import random
from fractions import Fraction


def h(p, q, z):
    return z**3 + 2*(q+1)*z**2 + (p+q*q+4*q-p*p)*z + 2*q*q


def trace_formula(p, q, x, y):
    a, b = q+x, p+y
    delta = a*b-p*q
    return (p-1)/a + (q-1)/b + (a+b)/delta


def marginal_values(p, q, x, y):
    a, b = q+x, p+y
    delta = a*b-p*q
    fa = (p-1)/(p*a*a) + (b*b+p*q)/(p*delta*delta)
    fb = (q-1)/(q*b*b) + (a*a+p*q)/(q*delta*delta)
    return fa, fb


def optimal_gains(p, q, B):
    assert 2 <= q <= p and B > 0
    if h(p, q, B/p) <= 0:
        return B/p, 0.0
    def diff(y):
        x = (B-q*y)/p
        fa, fb = marginal_values(p, q, x, y)
        return q*(fa-fb)
    low, high = 0.0, B/q
    assert diff(low) < 1e-9 and diff(high) > -1e-9
    for _ in range(120):
        mid = (low+high)/2
        if diff(mid) < 0:
            low = mid
        else:
            high = mid
    y=(low+high)/2
    return (B-q*y)/p, y


def inverse_trace(matrix):
    n = len(matrix)
    a = [[float(matrix[i][j]) for j in range(n)] + [float(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        imax=max(range(k, n),key=lambda i:abs(a[i][k]))
        a[k],a[imax]=a[imax],a[k]
        v=a[k][k]
        assert v > 0
        for j in range(2*n): a[k][j]/=v
        for i in range(n):
            if i == k: continue
            v=a[i][k]
            for j in range(2*n): a[i][j]-=v*a[k][j]
    return sum(a[i][n+i] for i in range(n))


def matrix_trace(p, q, gains):
    n=p+q
    mat=[[0.0]*n for _ in range(n)]
    for i in range(p):
        for j in range(p,n):
            mat[i][j]=mat[j][i]=-1.0
        mat[i][i]=q+gains[i]
    for j in range(p,n):mat[j][j]=p+gains[j]
    return inverse_trace(mat)


def verify():
    checks=0
    # Exact rational reentrance certificates: the boundary sign pattern is +,-,+.
    zvalues=[(Fraction(1,6),1),(Fraction(5,6),-1),(Fraction(20,6),1)]
    for z,sgn in zvalues:
        assert (h(6,2,z)>0) == (sgn>0)
        checks+=1
    assert h(6,2,Fraction(5,6)) == -Fraction(487,216)
    checks+=1
    # The two exact algebraic transition budgets for K_{6,2} are distinct.
    hlow,hhigh=3.0,5.0
    assert h(6,2,hlow/6)>0 and h(6,2,hhigh/6)<0
    for _ in range(100):
        mid=(hlow+hhigh)/2
        if h(6,2,mid/6)>0:hlow=mid
        else:hhigh=mid
    root1=(hlow+hhigh)/2
    hlow,hhigh=10.0,11.0
    for _ in range(100):
        mid=(hlow+hhigh)/2
        if h(6,2,mid/6)<0:hlow=mid
        else:hhigh=mid
    root2=(hlow+hhigh)/2
    assert abs(root1-3.3467996532637)<1e-8
    assert abs(root2-10.3824948581374)<1e-8
    checks+=2
    rng=random.Random(20261014)
    for p in range(2,10):
        for q in range(2,p+1):
            for B in (0.1, 1.0, 5.0, 20.0, 150.0):
                x,y=optimal_gains(p,q,B)
                assert x>0 and y>=0 and abs(p*x+q*y-B)<1e-9
                checks+=1
                exact=trace_formula(p,q,x,y)
                comp=matrix_trace(p,q,[x]*p+[y]*q)
                assert math.isclose(exact,comp,rel_tol=5e-9,abs_tol=1e-8),(p,q,B,exact,comp)
                checks+=1
                # Stationarity on the active face.
                fa,fb=marginal_values(p,q,x,y)
                if y>1e-8:
                    assert math.isclose(fa,fb,rel_tol=5e-8,abs_tol=5e-8)
                else:
                    assert fa>=fb-5e-8
                checks+=1
                for _ in range(8):
                    v=[rng.expovariate(1.0) for _ in range(p+q)]
                    v=[B*a/sum(v) for a in v]
                    assert matrix_trace(p,q,v)+1e-7>=exact
                    checks+=1
    # Verify boundary derivative identity for finite rational parameters.
    for p in range(2,14):
        for q in range(2,p+1):
            for B in (0.2, 1.0, 3.0, 20.0):
                x=B/p
                dy=max(1e-7,1e-6*B/q)
                derivative=(trace_formula(p,q,(B-q*dy)/p,dy)-trace_formula(p,q,x,0))/dy
                z=B/p
                identity=-q*h(p,q,z)/(p*p*z*(z+q)**2)
                assert abs(derivative-identity)<5e-3*(1+abs(identity)),(p,q,B,derivative,identity)
                checks+=1
    # Asymmetry never beats the unique block-constant design.
    for p,q,B in ((6,2,1.0),(6,2,5.0),(6,2,20.0),(8,3,10.0)):
        x,y=optimal_gains(p,q,B)
        assert (y==0) == (h(p,q,B/p)<=0)
        checks+=1
    print('PASS',checks,'finite cross-checks')
    print('K_6,2 transition budgets approximately',format(root1,'.12g'),format(root2,'.12g'))

if __name__=='__main__':verify()
