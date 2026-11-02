"""Standalone reproducibility checks for the finite two-projector implicit Euler model.

Requires: Python >=3.9 and SymPy >=1.10. All finite-path checks are exact.
"""
from fractions import Fraction
from itertools import product
from math import exp, sqrt


def matmul(a, b):
    return tuple(sum(a[i][j] * b[j] for j in range(2)) for i in range(2))


def check_rational(c, s, h, max_n=8):
    assert c*c+s*s==1 and 0<c<1 and h>0
    t=h/(1+2*h)
    ap=1+c; am=1-c
    mp=1-t*ap; mm=1-t*am; g=t*s
    f=Fraction(0)
    assert mp>0 and mm>0 and g>0
    # In eigen-coordinates, each resolvent is B_sigma.
    for sign in (-1,1):
        B=((mp,-sign*g),(-sign*g,mm))
        P=((ap,sign*s),(sign*s,am))
        # B*(I+h*P) == I; P is A_sigma with eigenvalues 0,2.
        for i in range(2):
            for j in range(2):
                lhs=sum(B[i][k]*((int(k==j)+h*P[k][j])) for k in range(2))
                assert lhs==int(i==j)
    H=((mp*mp,g*g),(g*g,mm*mm))
    sec=(Fraction(1),Fraction(0))
    mean=(Fraction(1),Fraction(0))
    for n in range(1,max_n+1):
        sec=matmul(H,sec)
        mean=(mp*mean[0],mm*mean[1])
        ex=ey=ex2=ey2=exy=Fraction(0)
        for signs in product((-1,1),repeat=n):
            x,y=Fraction(1),Fraction(0)
            for sign in signs:
                x,y=mp*x-sign*g*y,mm*y-sign*g*x
            ex+=x;ey+=y;ex2+=x*x;ey2+=y*y;exy+=x*y
        denom=2**n
        assert ex/denom==mean[0]
        assert ey/denom==mean[1]==0
        assert ex2/denom==sec[0]
        assert ey2/denom==sec[1]
        assert exy==0
        # Cayley-Hamilton for spectral formula, avoid symbolic radicals.
        if n>=2:
            trace=H[0][0]+H[1][1]
            determinant=H[0][0]*H[1][1]-H[0][1]*H[1][0]
            assert sec[1] == trace*prev_y-determinant*prevprev_y
        if n==1:
            prevprev_y=Fraction(0)
        else:
            prevprev_y=prev_y
        prev_y=sec[1]
    return max_n


def second_moments(c,T,N):
    h=T/N; t=h/(1+2*h); s=sqrt(1-c*c)
    mp=1-t*(1+c); mm=1-t*(1-c); g=t*s
    x2,y2=1.,0.
    for j in range(N):
        x2,y2=mp*mp*x2+g*g*y2, g*g*x2+mm*mm*y2
    emean=mp**N
    target=exp(-(1+c)*T)
    err2=x2+y2-2*target*emean+target*target
    return err2/h,y2/h,(x2-emean*emean)/h


def run():
    count=0
    for c,s in [(Fraction(3,5),Fraction(4,5)),(Fraction(5,13),Fraction(12,13)),(Fraction(8,17),Fraction(15,17))]:
        for h in [Fraction(1,20),Fraction(1,5),Fraction(3,4)]:
            count+=check_rational(c,s,h,7)
    for c in [.2,.6,.9]:
        for T in [.3,1.0,2.5]:
            V=(1-c*c)/(4*c)*(exp(-2*(1-c)*T)-exp(-2*(1+c)*T))
            assert V>0
            err=[]; slow=[]; fast=[]
            for N in [200,400,800,1600,3200]:
                e,yy,xx=second_moments(c,T,N)
                err.append(abs(e-V)); slow.append(abs(yy-V));fast.append(xx)
            # Error decays with refinement; fast mode contributes lower order.
            assert err[-1]<1.3e-3 and slow[-1]<1.3e-3, (c,T,err[-1],slow[-1])
            assert abs(fast[-1])<1.3e-3, (c,T,fast[-1])
            count+=5
    print(f'PASS: {count} independent exact-path case lengths and asymptotic spot checks;')
    print('       each exact-path length includes all 2^n sequences and five moment identities.')


if __name__=='__main__':
    run()
