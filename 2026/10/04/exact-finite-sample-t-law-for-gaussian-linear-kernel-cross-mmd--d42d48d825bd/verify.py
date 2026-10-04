#!/usr/bin/env python3
import math
from statistics import NormalDist
from fractions import Fraction

# Regularized incomplete beta I_x(a,b), Numerical Recipes continued fraction.
def _betacf(a,b,x):
    MAXIT=300
    EPS=3e-15
    FPMIN=1e-300
    qab=a+b; qap=a+1.0; qam=a-1.0
    c=1.0
    d=1.0-qab*x/qap
    if abs(d)<FPMIN: d=FPMIN
    d=1.0/d
    h=d
    for m in range(1,MAXIT+1):
        m2=2*m
        aa=m*(b-m)*x/((qam+m2)*(a+m2))
        d=1.0+aa*d
        if abs(d)<FPMIN: d=FPMIN
        c=1.0+aa/c
        if abs(c)<FPMIN: c=FPMIN
        d=1.0/d; h*=d*c
        aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2))
        d=1.0+aa*d
        if abs(d)<FPMIN: d=FPMIN
        c=1.0+aa/c
        if abs(c)<FPMIN: c=FPMIN
        d=1.0/d
        delta=d*c
        h*=delta
        if abs(delta-1.0)<EPS:
            return h
    raise RuntimeError('beta continued fraction did not converge')

def betai(a,b,x):
    if x < 0.0 or x > 1.0:
        raise ValueError('x outside [0,1]')
    if x==0.0: return 0.0
    if x==1.0: return 1.0
    bt=math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log1p(-x))
    if x < (a+1.0)/(a+b+2.0):
        return bt*_betacf(a,b,x)/a
    return 1.0-bt*_betacf(b,a,1.0-x)/b

def t_sf(x,nu):
    if x < 0:
        return 1.0-t_sf(-x,nu)
    y=nu/(nu+x*x)
    return 0.5*betai(nu/2.0,0.5,y)

def bisection_quantile_sf(alpha,nu):
    lo,hi=0.0,1.0
    while t_sf(hi,nu)>alpha: hi*=2.0
    for _ in range(100):
        mid=(lo+hi)/2
        if t_sf(mid,nu)>alpha: lo=mid
        else: hi=mid
    return (lo+hi)/2

def exact_algebra_check():
    # Deterministic rational samples; verifies the factorization and scale identity squared.
    X1=[Fraction(1),Fraction(2),Fraction(4),Fraction(7)]
    Y1=[Fraction(-1),Fraction(0),Fraction(3),Fraction(5)]
    X2=[Fraction(2),Fraction(3),Fraction(5),Fraction(11)]
    Y2=[Fraction(-2),Fraction(1),Fraction(4),Fraction(6)]
    s=len(X1)
    mean=lambda a: sum(a,Fraction(0))/len(a)
    mx,my=mean(X1),mean(Y1)
    bx,by=mean(X2),mean(Y2)
    A=mx-my; B=bx-by
    ss=sum((x-mx)**2 for x in X1)+sum((y-my)**2 for y in Y1)
    xmmd=A*B
    sigma2=B*B*ss/Fraction(s*s)
    # T^2 = xMMD^2/sigma^2; pooled t^2 = A^2*s(s-1)/ss.
    T2=xmmd*xmmd/sigma2
    t2=A*A*Fraction(s*(s-1),1)/ss
    assert T2 == Fraction(s,s-1)*t2
    assert (xmmd>0) == ((A>0)==(B>0))

def main():
    exact_algebra_check()
    nd=NormalDist()
    alpha=0.05
    z=nd.inv_cdf(1-alpha)
    expected={
        5:0.08972228912945557,
        10:0.06803194487037927,
        20:0.05858511585883524,
        50:0.053333686459325624,
        100:0.05165035780148737,
    }
    for s,val in expected.items():
        nu=2*s-2
        x=z*math.sqrt((s-1)/s)
        got=t_sf(x,nu)
        assert abs(got-val)<2e-12,(s,got,val)
        tq=bisection_quantile_sf(alpha,nu)
        c=math.sqrt(s/(s-1))*tq
        # Direct check that the calibrated cutoff has exact alpha tail.
        assert abs(t_sf(c*math.sqrt((s-1)/s),nu)-alpha)<2e-13
    coeff=math.exp(-z*z/2)/math.sqrt(2*math.pi)*(z**3+5*z)/8
    target=0.16339896947932403
    assert abs(coeff-target)<2e-15
    # First-order expansion: s*(size-alpha) -> coeff. Check stable approach.
    for s in (200,500,1000,2000):
        nu=2*s-2
        size=t_sf(z*math.sqrt((s-1)/s),nu)
        assert abs(s*(size-alpha)-coeff) < 0.001
    print('VERIFY_OK')

if __name__=='__main__': main()
