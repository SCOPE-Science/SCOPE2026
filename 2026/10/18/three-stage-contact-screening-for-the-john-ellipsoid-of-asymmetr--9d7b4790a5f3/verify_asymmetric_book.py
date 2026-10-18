#!/usr/bin/env python3
"""Reproduce leverage, determinant, threshold and regularity checks with stdlib."""
from fractions import Fraction as F
from math import sqrt, isclose
from itertools import product


def solve(A, b):
    n = len(b)
    M = [[A[i][j] for j in range(n)] + [b[i]] for i in range(n)]
    for i in range(n):
        pivot = next(j for j in range(i,n) if M[j][i] != 0)
        M[i],M[pivot]=M[pivot],M[i]
        piv=M[i][i]
        M[i]=[v/piv for v in M[i]]
        for j in range(n):
            if j != i:
                w=M[j][i]
                M[j]=[M[j][k]-w*M[i][k] for k in range(n+1)]
    return [M[i][-1] for i in range(n)]


def matrix(m, a, b, c):
    n=m+2
    L=[[a*0 for _ in range(n)] for __ in range(n)]
    for i,j,w in ([(0,k,a) for k in range(2,n)] +
                  [(1,k,b) for k in range(2,n)] + [(0,1,c)]):
        L[i][i]+=w; L[j][j]+=w; L[i][j]-=w; L[j][i]-=w
    return L


def resistance(L,i,j):
    n=len(L)
    # Ground the final vertex: this preserves intrinsic resistance.
    r=[0]*(n-1)
    if i<n-1:r[i]+=1
    if j<n-1:r[j]-=1
    x=solve([row[:-1] for row in L[:-1]],r)
    return sum(r[k]*x[k] for k in range(n-1))


def thresholds(m,A,B):
    D=B*B-A*A
    return sqrt(D),sqrt((A*A+B*B+sqrt((A*A+B*B)**2+(m*m-1)*D*D))/(m+1))


def weights(m,A,B,t):
    D=B*B-A*A
    t1,t2=thresholds(m,A,B)
    if t<t1-1e-11:
        return 1/A**2,0.0,1/t**2,1
    if t<t2-1e-11:
        X=(t*t-D)/(2*t);Y=(t*t+D)/(2*t)
        U=A*A-X*X
        return Y/(t*U),X/(t*U),(U-m*X*Y)/(U*t*t),2
    r=2*A*A/(m*D+sqrt(m*m*D*D+4*A*A*B*B))
    a=(m+r)/(m*A*A*(1+r))
    return a,r*a,0.0,3


def analytic_resistances(m,a,b,c):
    S=a+b
    k=S/(m*a*b+c*S)
    return (1/S+(b/S)**2*k,
            1/S+(a/S)**2*k,
            k)


def log_volume_without_dimension_constant(m,a,b,c):
    from math import log
    S=a+b
    return -.5*((m-1)*log(S)+log(m*a*b+c*S))


def main():
    checks=0
    for m,A,B in product([3,4,5,9], [1.,1.7], [2.5,3.5]):
        # Only B>A: all 16 choices here satisfy this.
        t1,t2=thresholds(m,A,B)
        assert B-A<t1<t2<A+B
        tvals=[B-A+.12*(t1-(B-A)), t1, (t1+t2)/2,
               t2, (t2+A+B)/2, A+B-.02]
        for t in tvals:
            a,b,c,phase=weights(m,A,B,t)
            assert min(a,b,c)>-1e-9
            L=matrix(m,a,b,c)
            ru,rv,rh=analytic_resistances(m,a,b,c)
            assert ru<=A*A+1e-7 and rv<=B*B+1e-7 and rh<=t*t+1e-7
            for x,y,R in [(0,2,ru),(1,2,rv),(0,1,rh)]:
                val=resistance(L,x,y)
                assert isclose(val,R,rel_tol=1e-8,abs_tol=1e-8), (m,A,B,t,x,y,val,R)
            for v,cap,wt in [(ru,A*A,a),(rv,B*B,b),(rh,t*t,c)]:
                if wt>1e-8: assert isclose(v,cap,rel_tol=1e-8,abs_tol=1e-8)
            checks+=1
    # Independently reconstruct the matrix-tree count for one exact middle-branch case.
    m=4; A=F(1);B=F(5,4);t=F(9,10)
    D=B*B-A*A
    assert t*t>D
    X=(t*t-D)/(2*t);Y=(t*t+D)/(2*t);U=A*A-X*X
    a=Y/(t*U);b=X/(t*U);c=(U-m*X*Y)/(U*t*t)
    assert all(v>0 for v in (a,b,c))
    L=matrix(m,a,b,c)
    for x,y,expected in [(0,2,A*A),(1,2,B*B),(0,1,t*t)]:
        assert resistance(L,x,y)==expected
    checks+=1
    # Check plateau and the dimension-dependent width by entirely separate expressions.
    for m in (3,10,100,1000):
        A=1.;B=1.5;d=B*B-A*A;t1,t2=thresholds(m,A,B)
        assert t2>t1
        if m==1000:
            assert abs(m*(t2-t1)-A*A/sqrt(d))<.01
        a,b,c,phase=weights(m,A,B,t2+.01*(A+B-t2))
        assert c==0 and phase==3
        checks+=1
    # Verify each one-sided curvature formula with finite differences on both sides.
    m=5;A=1.;B=1.5;t1,t2=thresholds(m,A,B)
    from math import log
    def f(t):
        a,b,c,p=weights(m,A,B,t)
        return log_volume_without_dimension_constant(m,a,b,c)
    eps=1e-4
    def second(t,side):
        return (f(t+3*side*eps)-2*f(t+2*side*eps)+f(t+side*eps))/(eps*eps)
    first_left=second(t1,-1);first_right=second(t1,1)
    assert abs((first_right-first_left)+m/(A*A))<.03
    U=A*A-((t2*t2-(B*B-A*A))/(2*t2))**2
    D=B*B-A*A
    known_left=-((m+1)+(m-1)*D*D/t2**4)/(2*U)
    assert abs(second(t2,-1)-known_left)<.03
    assert abs(second(t2,1))<.03
    checks+=1
    print('CHECK_PASS',checks)

if __name__=='__main__':main()
