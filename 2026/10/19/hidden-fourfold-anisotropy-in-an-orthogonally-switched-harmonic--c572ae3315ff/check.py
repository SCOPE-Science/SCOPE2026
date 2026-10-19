#!/usr/bin/env python3
"""Exact arithmetic verification for a two-axis telegraph-switched harmonic diffusion.

Uses only Python's standard library. Run: python3 check.py
"""
from fractions import Fraction as F


def quantities(k, a, s, D):
    assert k > a > 0 and s > 0 and D > 0
    T = k * (k + s) - a*a
    U = 2*(k*k-a*a) + k*s
    m = D*(k+s)/T
    b = -a*m/(k+s)
    M = 3*D*D*(2*a*a+2*k*k+3*k*s+s*s)/(U*T)
    Bs = (-4*a*M+12*D*b)/(4*k+2*s)
    V = D*m/k
    cov = -D*D*a*a*(k+s)/(k*T*T)
    Q = 12*D*D*a*a*(2*k+s)/(k*U*T)
    return T,U,m,b,M,Bs,V,cov,Q


def run():
    count = 0
    for ki in (2,3,5,7,11):
        for ai in (1,2,3,4):
            if ai >= ki: continue
            for si in (1,2,3,5,11):
                for Di in (1,2,7):
                    k,a,s,D = map(F,(ki,ai,si,Di))
                    T,U,m,b,M,Bs,V,cov,Q = quantities(k,a,s,D)
                    checks = [
                        -2*k*m-2*a*b+2*D == 0,
                        -2*(k+s)*b-2*a*m == 0,
                        -4*k*M-4*a*Bs+12*D*m == 0,
                        -(4*k+2*s)*Bs-4*a*M+12*D*b == 0,
                        -4*k*V+4*D*m == 0,
                        V-m*m==cov,
                        2*M-6*V==Q,
                        m>D/k,
                        cov<0,
                        Q>0,
                        M-3*m*m > 0,
                        cov < quantities(k,a,s+F(1,3),D)[7] < 0,
                        Q > quantities(k,a,s+F(1,3),D)[8] > 0,
                        (D*D*a*a*(a*a+k*k+k*s)/(k*T**3)) > 0,
                        k*(2*k+s) > U,
                        U>0,
                        T>0,
                        (4*k*V == 4*D*m),
                    ]
                    if not all(checks):
                        raise AssertionError((ki,ai,si,Di,[i for i,v in enumerate(checks) if not v]))
                    count+=len(checks)
    k,a,s,D=map(F,(2,1,1,1))
    _,_,m,_,M,_,V,cov,Q=quantities(k,a,s,D)
    expected=[m==F(3,5),V==F(3,10),M==F(51,40),cov==F(-3,50),Q==F(3,4)]
    assert all(expected)
    count+=len(expected)
    print('PASS exact rational checks:',count)
    print('Witness k=2,a=1,sigma=1,D=1: second=',m,'crossfourth=',V,'fourth=',M,'covariance=',cov,'angular_fourth=',Q)


if __name__=='__main__':
    run()
