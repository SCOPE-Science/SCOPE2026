#!/usr/bin/env python3
"""Independent arithmetic and quadrature checks for two-dimensional rank-one range projections."""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt, acos
from random import Random


def residual_from_gram(B, w):
    """Direct projector expansion, not the characteristic-polynomial shortcut."""
    a,b,c=B
    x,y=w
    den=a*x*x+2*b*x*y+c*y*y
    assert den>0
    tr=a+c
    # B^2 entries
    b2_00=a*a+b*b
    b2_01=b*(a+c)
    b2_11=b*b+c*c
    quad=b2_00*x*x+2*b2_01*x*y+b2_11*y*y
    return tr-quad/den


def closed(B,w):
    a,b,c=B
    x,y=w
    return (a*c-b*b)*(x*x+y*y)/(a*x*x+2*b*x*y+c*y*y)


def sign_average(B):
    return (residual_from_gram(B,(F(1),F(1)))+
            residual_from_gram(B,(F(1),F(-1))))/2


def formula(B):
    a,b,c=B
    s=(a+c)/2
    D=a*c-b*b
    return D*s/(s*s-b*b)


def exact_checks():
    n=0
    for a in range(1,13):
        for c in range(1,13):
            for b in range(-5,6):
                B=(F(a),F(b,4),F(c))
                if B[0]*B[2]<=B[1]*B[1]: continue
                for w in [(F(1),F(1)),(F(1),F(-1)),(F(2),F(3)),(F(5),F(-2))]:
                    assert residual_from_gram(B,w)==closed(B,w)
                    n+=1
                assert sign_average(B)==formula(B)
                n+=1
    diag=(F(100),F(0),F(1))
    rotated=(F(101,2),F(99,2),F(101,2))
    assert formula(diag)==F(200,101)
    assert formula(rotated)==F(101,2)
    assert sign_average(diag)==F(200,101)
    assert sign_average(rotated)==F(101,2)
    return n+4


def numerical_checks():
    rng=Random(20261026)
    n=0
    for k in [1.001,1.01,1.1,1.5,2,3,10,100,1000]:
        lam=k*k; mu=1.0
        D=lam*mu;s=(lam+mu)/2;d=(lam-mu)/2
        assert abs((D/s)-(2*lam*mu/(lam+mu)))<=1e-9*max(1,D/s)
        assert abs(D*s/(s*s-d*d)-s) <= 3e-9*max(1,s)
        t=sqrt(lam+mu)/(k+1)
        if k>1.02:
            th=0.5*__import__('math').asin(t)
            for z in [th-1e-5,th,th+1e-5]:
                off=d*sin(2*z)
                er=D*s/(s*s-off*off)
                if z<th-1e-6: assert er < k
                if z>th+1e-6: assert er > k
            n+=3
        for j in range(120):
            theta=rng.random()*pi/2
            b=d*sin(2*theta)
            er=D*s/(s*s-b*b)
            assert D/s-1e-8 <=er<=s+1e-8
            # Direct averaged projectors from Gram entries.
            a=s+d*cos(2*theta)
            c=s-d*cos(2*theta)
            e=(residual_from_gram((a,b,c),(1,1))+
               residual_from_gram((a,b,c),(1,-1)))/2
            assert abs(e-er)<=2e-7*max(1,er)
            n+=1
        midpoint_count=20000
        angavg=sum(D*s/(s*s-d*d*sin(2*pi*(i+0.5)/(2*midpoint_count))**2)
                   for i in range(midpoint_count))/midpoint_count
        assert abs(angavg-k)<=2e-8*max(1,k)
        # Analytic probability of worse Rademacher error under uniform rotation.
        riskfrac=2*acos(t)/pi
        assert 0<riskfrac<1
        n+=2
    # Midpoint Gaussian-direction quadrature, rotation invariance.
    for a,c in [(1.0,1.0),(100.0,1.0),(9.0,4.0),(10000.0,1.0)]:
        N=24000
        avg=sum(a*c/(a*cos(2*pi*(j+.5)/N)**2+c*sin(2*pi*(j+.5)/N)**2)
                for j in range(N))/N
        assert abs(avg-sqrt(a*c))<=4e-8*max(1,sqrt(a*c))
        n+=1
    return n

if __name__=='__main__':
    x=exact_checks();y=numerical_checks()
    print('VERIFY_OK exact='+str(x)+' numerical='+str(y))
