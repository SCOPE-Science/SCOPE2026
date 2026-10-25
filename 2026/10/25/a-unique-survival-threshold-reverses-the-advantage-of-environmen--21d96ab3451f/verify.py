"""Independent arithmetic checks for a two-stage environmental-order threshold.

All universal statements are proved in RESULT.md; finite checks here test the
closed formulas and demonstrate their numerical behavior.
"""
from fractions import Fraction as F
from math import sqrt, log, isclose
import random


def mat(u1,u2,x,y,b,c,s):
    return ((u1*x+s*b, u1*y),(u2*x,u2*y+s*c))


def multiply(A,B):
    return tuple(tuple(A[i][0]*B[0][j]+A[i][1]*B[1][j] for j in range(2)) for i in range(2))


def perron(A):
    a,b=A[0]; c,d=A[1]
    return ((a+d)+sqrt((a-d)**2+4*b*c))/2


def threshold(u1,u2,x0,x1,y0,y1,b,c):
    dx=x0-x1;dy=y1-y0
    return ((u1*dx-u2*dy)/(c-b))*(x0/dx+y0/dy)


def main():
    u1,u2,x0,x1,y0,y1,b,c=(F(1),F(1),F(2),F(1),F(1),F(19,10),F(1,4),F(3,4))
    s=threshold(u1,u2,x0,x1,y0,y1,b,c)
    assert s==F(28,45)
    A0=mat(u1,u2,x0,y0,b,c,s)
    A1=mat(u1,u2,x1,y1,b,c,s)
    w=(F(9),F(10))
    value=F(49,15)
    for A in (A0,A1):
        assert all(A[i][0]*w[0]+A[i][1]*w[1]==value*w[i] for i in (0,1))
    print('exact common Perron vector: (9, 10); eigenvalue: 49/15; threshold: 28/45')

    gaps=[]
    for q in (F(1,4), F(1), F(2)):
        M0=mat(u1,u2,x0,y0,b,c,q)
        M1=mat(u1,u2,x1,y1,b,c,q)
        gaps.append(.5*log(perron(M0)*perron(M1)/perron(multiply(M0,M1))))
    assert gaps[0]>0 and gaps[1]<0 and gaps[2]<0
    print('growth gaps at s=1/4,1,2:',*[f'{g:.15g}' for g in gaps])

    rng=random.Random(20261024)
    strict_count=0
    equality_count=0
    max_abs_at_equality=0.
    for k in range(12000):
        U1=rng.uniform(.3,3)
        U2=rng.uniform(.3,3)
        X1=rng.uniform(.2,2)
        dX=rng.uniform(.1,1.5)
        Y0=rng.uniform(.2,2)
        dY=rng.uniform(.01,.9*U1*dX/U2)
        X0=X1+dX
        Y1=Y0+dY
        B=rng.uniform(.03,.5)
        C=rng.uniform(B+.06,1.8)
        crit=threshold(U1,U2,X0,X1,Y0,Y1,B,C)
        ratio=rng.choice((.06,.4,.8,1.,1.2,2.,5.,9.))
        param=ratio*crit
        H0=mat(U1,U2,X0,Y0,B,C,param)
        H1=mat(U1,U2,X1,Y1,B,C,param)
        p0=perron(H0);p1=perron(H1)
        pair=perron(multiply(H0,H1))
        gap=.5*log(p0*p1/pair)
        if ratio==1.:
            assert abs(gap)<1.e-11
            equality_count+=1
            max_abs_at_equality=max(max_abs_at_equality,abs(gap))
        else:
            assert abs(gap)<1.e-11 or ((gap>0)==(ratio<1))
            strict_count+=1
    print('randomized pair evaluations:',strict_count,'strict cases and',equality_count,'threshold cases')
    print('maximum numerical equality residual:',max_abs_at_equality)
    print('PASS')


if __name__=='__main__':
    main()
