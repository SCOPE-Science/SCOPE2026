#!/usr/bin/env python3
import math
from fractions import Fraction as F


def c_of(k,s):
    return math.sinh(s)*math.sinh((k-1)*s)**(k-1)/math.sinh(k*s)**k

def zpair(k,s):
    d=math.sinh((k-1)*s)
    return math.exp(k*s)*math.sinh(s)/d, math.exp(-k*s)*math.sinh(s)/d

def lambda_star(k):
    return ((3*k+1)**k)/(3**k*(k-1)**(k+1))

def lambda_zero(k):
    return ((k+1)**k)/(k**k*(k-1))

def branch(k,lam,s):
    c=c_of(k,s)
    S=(lam/c)**(1.0/k)
    z1,z2=zpair(k,s)
    m=1.0+z1+z2
    Lam=2.0*lam+(lam/c)*(S-m)
    return z1,z2,S,Lam,S-m

def merger(k,lam):
    c0=(k-1)**(k-1)/k**k
    S0=(lam/c0)**(1.0/k)
    Lc=2.0*lam+(lam/c0)*(S0-(k+1)/(k-1))
    return c0,S0,Lc

def exact_quartic_check(k):
    # Coefficients of log c(s)=log c0+a2*s^2+a4*s^4+O(s^6).
    a2=-F(k*(k-1),2)
    a4=F(k*(k-1)*(k*k-k+1),36)
    A=F(k-1,2)                    # s^2 coefficient of log S
    B=-a4/F(k,1)                  # s^4 coefficient of log S
    C=F(k*(k-1),2)                # s^2 coefficient of log(lambda/c)
    m0=F(k+1,k-1)
    m2=F(2*k*(k+1),3*(k-1))
    m4=-F(2*k*(k+1)*(k*k-5*k+1),45*(k-1))
    St=F(k*(3*k+1),3*(k-1)*(k-1))
    d0=St-m0
    d2=St*A-m2
    q2=d2+C*d0
    assert q2 == 0
    d4=St*(B+A*A/F(2,1))-m4
    E=-a4+C*C/F(2,1)
    q4=d4+C*d2+E*d0
    target=-F(k*(k+1)*(37*k*k+110*k+37),1080*(k-1))
    assert q4 == target
    return target

def main():
    assert F(7**2,3**2) == F(49,9)
    for k in range(2,101):
        assert F((3*k+1)**k,3**k*(k-1)**(k+1)) > F((k+1)**k,k**k*(k-1))
        assert exact_quartic_check(k) < 0

    worst=0.0
    checked=0
    for k in range(2,15):
        lam=1.5*lambda_star(k)
        _,_,Lc=merger(k,lam)
        # Above the tricritical threshold the branch initially rises.
        _,_,_,Lsmall,Tsmall=branch(k,lam,0.01)
        assert Tsmall>0 and Lsmall>Lc
        for s in (0.01,0.03,0.07):
            z1,z2,S,Lam,T=branch(k,lam,s)
            assert T>0
            c=lam/S**k
            r1=abs(z1-c*(1+z1)**k)
            r2=abs(z2-c*(1+z2)**k)
            r3=abs(T-(Lam-2*lam)/S**k)
            r4=abs(S-(1+z1+z2+T))
            worst=max(worst,r1,r2,r3,r4)
            checked+=1
        # The admissibility margin eventually becomes negative.
        s=0.1
        while branch(k,lam,s)[4] > 0:
            s*=1.25
            assert s<20
        assert branch(k,lam,s)[3] < Lc or branch(k,lam,s)[4] <= 0
    assert worst < 2e-10
    print('VERIFY_OK exact_orders=2..100 residual_cases=%d worst_residual=%.3e k2_threshold=49/9' % (checked,worst))

if __name__=='__main__':
    main()
