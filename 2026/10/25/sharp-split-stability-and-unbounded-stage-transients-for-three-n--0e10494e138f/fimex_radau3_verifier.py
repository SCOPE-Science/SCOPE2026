"""Exact-rational and numerical checks for the two-rate FIMEX-Radau(3,0) model.

Run: python fimex_radau3_verifier.py
The mathematical proof is independent of this finite checker.
"""
from fractions import Fraction as Q
from math import sqrt, exp, e, hypot


def source_step(s, t, x, y):
    # Published three-node coefficient equations, with r*lambda_1=-s,
    # r*lambda_2=-t, and two input components (x,y).
    b1 = y + t*(x-5*y)/6
    b2 = y + t*(3*x-7*y)/2
    a = 1 + Q(5,6)*s
    b = -Q(1,6)*s
    c = Q(3,2)*s
    d = 1 + Q(1,2)*s
    det = a*d-b*c
    return ((d*b1-b*b2)/det,(-c*b1+a*b2)/det)


def matrix(s,t):
    d = 2*s*s+4*s+3
    return ((t*(2*s+1)/(2*d), -(6*s*t-4*s+5*t-6)/(2*d)),
            (3*t*(2*s+3)/(2*d), -(10*s*t+4*s+21*t-6)/(2*d)))


def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def norm2(a):
    a11,a12=a[0]
    a21,a22=a[1]
    aa=a11*a11+a21*a21
    bb=a12*a12+a22*a22
    ab=a11*a12+a21*a22
    return sqrt((aa+bb+sqrt((aa-bb)**2+4*ab*ab))/2)


def threshold(s):
    return s+3.5-0.5*sqrt(24*s+37)


def main():
    checks=0
    for ns in range(15):
        s=Q(ns,4)
        for nt in range(41):
            t=Q(nt,8)
            a=matrix(s,t)
            for x,y in ((Q(1),Q(0)),(Q(0),Q(1)),(Q(2,3),Q(-3,5))):
                z=source_step(s,t,x,y)
                assert z == (a[0][0]*x+a[0][1]*y,a[1][0]*x+a[1][1]*y)
                checks+=1
            d=2*s*s+4*s+3
            tr=a[0][0]+a[1][1]
            det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
            assert tr == -(4*s*t+2*s+10*t-3)/d
            assert det == 2*t*(t-2)/d
            assert 1-tr+det == 2*(s+t)*(s+t+3)/d
            assert 1+tr+det == 2*((s-t)**2+s-7*t+3)/d
            assert 1-det == (2*s*s+4*s+3-2*t*t+4*t)/d
            checks+=5
    for s in (0.,.001,.1,1.,10.,100.,10000.):
        lo=threshold(s)
        hi=s+3.5+0.5*sqrt(24*s+37)
        detbound=1+sqrt(s*s+2*s+2.5)
        assert 0<lo<detbound<hi
        assert abs((lo-s-3.5)**2-(6*s+9.25))<1e-5
        checks+=2
    j=((.5,-1.5),(1.5,-2.5))
    n=((1.5,-1.5),(1.5,-1.5))
    assert matmul(n,n)==((0.,0.),(0.,0.))
    assert abs(norm2(j)-sqrt((11+3*sqrt(13))/2))<1e-12
    checks+=2
    for c in (.2,.5,.9,.99):
        k=10000000.
        assert c*k<threshold(k)
        actual=matrix(k,c*k)
        target=tuple(tuple(c*z for z in row) for row in j)
        assert max(abs(actual[i][h]-target[i][h]) for i in range(2) for h in range(2))<1e-5
        checks+=2
    for q in (100,1000,10000):
        c=1-1/q
        # The nilpotent identity (cJ)^n=(-c)^n(I-nN) is exact.
        # The two-term norm inequality implies the sharp limit 3/e.
        k=round(-1.0/__import__('math').log(c))
        val=(1-c)*3*k*c**k
        assert abs(val-3/e)<.03
        checks+=1
    print('PASS:',checks,'independent deterministic checks')


if __name__=='__main__':
    main()
