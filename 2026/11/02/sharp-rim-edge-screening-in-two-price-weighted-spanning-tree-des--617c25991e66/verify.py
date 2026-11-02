#!/usr/bin/env python3
"""Exact and numerical checks for the two-price wheel tree-design theorem.

All checks use the Python standard library. This program is independent
of any stored ledger and constructs every tested matrix from its definition.
"""
from fractions import Fraction as F
from math import log, exp
import random


def grounded(m, spokes, rims):
    assert len(spokes)==len(rims)==m
    A = [[F(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        A[i][i] += spokes[i]
        j=(i+1)%m
        A[i][i] += rims[i]
        A[j][j] += rims[i]
        A[i][j] -= rims[i]
        A[j][i] -= rims[i]
    return A


def determinant(A):
    A=[list(map(F,row)) for row in A]
    n=len(A)
    sign=1
    for i in range(n):
        pivot=next((j for j in range(i,n) if A[j][i]),None)
        if pivot is None:return F(0)
        if pivot!=i:
            A[pivot],A[i]=A[i],A[pivot]
            sign=-sign
        v=A[i][i]
        for j in range(i+1,n):
            q=A[j][i]/v
            for k in range(i+1,n):
                A[j][k] -= q*A[i][k]
            A[j][i]=F(0)
    out=F(sign)
    for i in range(n):out*=A[i][i]
    return out


def phi(m,u):
    return (u+u**(m-1))/(1+u**m)


def optimal_u(m,r):
    if r>=2:return 0.0
    s=1-r/2
    lo,hi=0.0,s
    for _ in range(100):
        mid=(lo+hi)/2
        if phi(m,mid)<s:lo=mid
        else:hi=mid
    return (lo+hi)/2


def logdet_spd(A):
    n=len(A)
    L=[[0.0]*n for _ in range(n)]
    result=0.0
    for i in range(n):
        for j in range(i+1):
            v=float(A[i][j])-sum(L[i][k]*L[j][k] for k in range(j))
            if i==j:
                assert v>0
                L[i][j]=v**0.5
                result+=log(v)
            else:L[i][j]=v/L[j][j]
    return result


def exact_tests():
    count=0
    for m in range(3,12):
        for u in [F(0),F(1,7),F(1,4),F(1,2),F(2,3),F(3,4)]:
            t=u/(1-u)**2
            for r in [F(1,3),F(1),F(3,2),F(2),F(4)]:
                P=F(2);Q=P*r;B=F(7*m)
                s=B/(m*(P+Q*t));c=s*t
                matrix=grounded(m,[s]*m,[c]*m)
                observed=determinant(matrix)
                D=(1-u)**2+r*u
                expected=(B/(m*P))**m*(1-u**m)**2/D**m
                assert observed==expected,(m,u,r,observed,expected)
                count+=1
    # The derivative-polynomial identity is checked with independent terms.
    for m in range(3,101):
        for u in [F(0),F(1,8),F(1,3),F(3,5),F(9,10)]:
            for r in [F(1,3),F(1),F(7,4),F(2),F(7,2)]:
                D=(1-u)**2+r*u
                left=-(r-2+2*u)*(1-u**m)-2*u**(m-1)*D
                right=(2-r)*(1+u**m)-2*(u+u**(m-1))
                assert left==right
                count+=1
    # m=3 explicit optimum ratio and critical threshold.
    for r in [F(1,4),F(1,2),F(1),F(3,2),F(7,4)]:
        t=(2-r)/r
        # exact derivative of ((1+3t)^2)/(1+rt)^3 vanishes
        assert 6*(1+r*t)-3*r*(1+3*t)==0
        count+=1
    return count


def analytic_limits_tests():
    count=0
    for r in [.2,.5,.8,1.,1.25,1.5,1.75,1.9,1.99]:
        s=1-r/2
        assert 0<s<1
        for m in [3,4,5,8,16,32,64,128]:
            u=optimal_u(m,r)
            assert 0<=u<=s
            assert abs(phi(m,u)-s)<4e-14
            assert abs((s-u)-u**(m-1)*(1-u*u)/(1+u**m))<5e-14
            assert s-u<=s**(m-1)+1e-14
            count+=4
        if r>=.5:
            # Numerical finite-size asymptotic (avoid underflow beyond precision).
            m=20
            u=optimal_u(m,r)
            approx=(s-u)/s**(m-1)
            if s**(m-1)>1e-10:
                assert abs(approx-(1-s*s))<.12
                count+=1
    return count


def asymmetry_tests():
    rng=random.Random(91917)
    count=0
    for m in range(3,12):
        for r in [.2,.5,1.,1.5,1.99,2.,2.5,4.]:
            B=float(m)
            P=1.0;Q=r
            u=optimal_u(m,r)
            t=u/(1-u)**2
            s=B/(m*(P+Q*t));c=s*t
            optimum=logdet_spd(grounded(m,[s]*m,[c]*m))
            # Exact normalizing costs, perturbed values positive and feasible.
            for _ in range(25):
                spokes=[s*exp(rng.uniform(-1.4,1.4)) for _ in range(m)]
                rims=[max(c,.02)*exp(rng.uniform(-1.4,1.4)) for _ in range(m)]
                factor=B/(sum(spokes)+Q*sum(rims))
                spokes=[factor*x for x in spokes]
                rims=[factor*x for x in rims]
                candidate=logdet_spd(grounded(m,spokes,rims))
                assert candidate<=optimum+2e-11,(m,r,optimum,candidate)
                count+=1
    return count


def main():
    a=exact_tests();b=analytic_limits_tests();c=asymmetry_tests()
    print(f'VERIFY_OK exact={a} analytic_numerical={b} asymmetric={c} total={a+b+c}')

if __name__=='__main__':main()
