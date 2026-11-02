#!/usr/bin/env python3
"""Standalone numerical and exact checks for the two-patch culling phase law.

Requires only Python 3 standard library. Run: python3 check.py
The analytical proof in RESULT.md, not sampling, establishes the theorem.
"""
from fractions import Fraction as Q
from math import cosh, exp, log, sinh, sqrt
from random import Random


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def scale(A, s):
    return [[v*s for v in row] for row in A]


def plus(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def tr(A):
    return A[0][0] + A[1][1]


def det(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]


def exp_series(A, t):
    """Independent scaling-and-squaring matrix power series, not the closed form."""
    H = scale(A, t)
    norm = max(sum(abs(x) for x in row) for row in H)
    n = 0
    while norm > 0.5:
        H = scale(H, 0.5)
        norm *= 0.5
        n += 1
    I = [[1.0, 0.0], [0.0, 1.0]]
    V = I
    term = I
    for j in range(1, 65):
        term = scale(mm(term, H), 1.0/j)
        V = plus(V, term)
    for _ in range(n):
        V = mm(V, V)
    return V


def analytic_data(A, T, p, h1, h2):
    a,b=A[0]
    c,d=A[1]
    tau=(a+d)/2
    k=sqrt(((a-d)/2)**2+b*c)
    et=exp(tau*T)
    base=et*((h1+h2)*cosh(k*T)+(h1-h2)*(a-d)/(2*k)*sinh(k*T))
    B=(1-h1)*(1-h2)*b*c*et/k**2
    return (base+B*sinh(k*p)*sinh(k*(T-p)),h1*h2*exp((a+d)*T),base,B,k)


def close(x,y,eps=4.e-10):
    assert abs(x-y)<=eps*max(1,abs(x),abs(y)), (x,y)


def run():
    assertions=0
    r=Random(20261029)
    for _ in range(1500):
        a=r.uniform(-2,2);d=r.uniform(-2,2)
        b=r.uniform(0.03,2.0);c=r.uniform(0.03,2.0)
        T=r.uniform(0.1,3.0);p=r.uniform(0,T)
        h1=r.uniform(0.1,0.95);h2=r.uniform(0.1,0.95)
        A=[[a,b],[c,d]]
        D1=[[h1,0.0],[0.0,1.0]]
        D2=[[1.0,0.0],[0.0,h2]]
        mon=mm(mm(mm(exp_series(A,T-p),D2),exp_series(A,p)),D1)
        stated,determinant,base,B,k=analytic_data(A,T,p,h1,h2)
        close(tr(mon),stated);assertions+=1
        close(det(mon),determinant);assertions+=1
        close(stated,analytic_data(A,T,T-p,h1,h2)[0]);assertions+=1
        mid=base+B*sinh(k*T/2)**2
        assert mid>=stated-1e-10*max(1,abs(mid));assertions+=1
        assert stated>=base-1e-10*max(1,abs(base));assertions+=1
        assert determinant>0 and tr(mon)>0 and tr(mon)**2>4*determinant-1e-10*max(1,abs(determinant));assertions+=1
    q=Q(97,100)
    S=[[Q(3),Q(1)],[Q(1),Q(3)]]
    D1=[[Q(1,2),Q(0)],[Q(0),Q(1)]]
    D2=[[Q(1),Q(0)],[Q(0),Q(1,2)]]
    ET=scale([[Q(5),Q(3)],[Q(3),Q(5)]],q/Q(4))
    M0=mm(ET,mm(D2,D1))
    Mhalf=scale(mm(mm(mm(S,D2),S),D1),q/Q(8))
    assert tr(M0)==Q(97,80);assertions+=1
    assert tr(Mhalf)==Q(3977,3200);assertions+=1
    assert det(M0)==det(Mhalf)==Q(9409,40000);assertions+=1
    assert tr(M0)-(1+det(M0))==-Q(909,40000);assertions+=1
    assert tr(Mhalf)-(1+det(Mhalf))==Q(607,80000);assertions+=1
    print('PASS: %d checks; exact rational stability reversal confirmed'%assertions)

if __name__=='__main__':
    run()
