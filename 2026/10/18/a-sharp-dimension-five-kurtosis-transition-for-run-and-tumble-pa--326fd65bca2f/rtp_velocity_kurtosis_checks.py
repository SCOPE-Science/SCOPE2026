#!/usr/bin/env python3
"""Reproducible finite checks of the analytic run-and-tumble fourth-cumulant law.

Python 3 standard library only. The checks compare independent generator and
conditional-Dirichlet/Poisson expressions. Finite checks are not a proof of the
all-time monotonicity theorem; its coefficient induction is given in RESULT.md.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb, factorial

getcontext().prec = 70
D = Decimal


def ab(x):
    y = (-x).exp()
    return (x*x + 4*x + 6)*y + 2*x - 6, -(x*x+8*x+10)*y - y*y - 4*x + 11


def analytical(d, second_speed, fourth_speed, x):
    m2 = second_speed/D(d)
    m4 = 3*fourth_speed/(D(d)*(d+2))
    a,b = ab(x)
    var = 2*m2*(x-1+(-x).exp())
    kappa4 = 12*(m4*a +m2*m2*b)
    return var,kappa4+3*var*var,kappa4


def poisson_dirichlet(d,second_speed,fourth_speed,x):
    m2=second_speed/D(d)
    m4=3*fourth_speed/(D(d)*(d+2))
    p=(-x).exp()
    v=D(0); m=D(0)
    # independent conditioning on the exact number of tumbles and uniform spacings
    for n in range(450):
        v += p*2*m2*x*x/D(n+2)
        m += p*x**4*(24*m4+12*D(n)*m2*m2)/D((n+2)*(n+3)*(n+4))
        p *= x / D(n+1)
    return v,m,m-3*v*v


def power_coefficient(n):
    # coefficient n! [x^n] of F(x)=-e^(3x) (B A' - B' A)
    # where F=2e^(3x)+(-2x^3+7x^2-18x+6)e^(2x)
    #         +(4x^2+12x-18)e^x+x^2+6x+10
    a=2*3**n + 6*2**n-(18*n*2**(n-1) if n>=1 else 0) + (7*n*(n-1)*2**(n-2) if n>=2 else 0)
    if n>=3:a-=2*n*(n-1)*(n-2)*2**(n-3)
    a+=4*n*(n-1)+12*n-18
    if n==0:a+=10
    elif n==1:a+=6
    elif n==2:a+=2
    return a


def main():
    checked=0
    for n in range(0,8):
        assert power_coefficient(n)==0, (n,power_coefficient(n)); checked+=1
    assert power_coefficient(8)==112;checked+=1
    for n in range(8,120):
        assert power_coefficient(n)>0
        q= Fraction(n**3-16*n*n+79*n-96,4)
        assert power_coefficient(n+1)-3*power_coefficient(n)==2**n*q-8*(n-2)*(n+3)
        assert q>=6 and 6*2**n > 8*(n-2)*(n+3)
        checked+=4
    for dim in [1,2,3,4,5,6,9,15]:
        for speeds in [(D(1),D(1)),(D(5),D(41)),(D(2),D(8)),(D('1.1'),D('1.4'))]:
            assert speeds[1] >= speeds[0]**2
            for x in [D('0.12'),D('0.5'),D('1'),D('2.08102085125232'),D('3'),D('7'),D('15')]:
                a=analytical(dim,*speeds,x);b=poisson_dirichlet(dim,*speeds,x)
                for v,w in zip(a,b):
                    assert abs(v-w)<=D('1e-53')*(1+abs(v)),(dim,speeds,x,v,w)
                    checked+=1
    # Exact two-speed example P(V=1)=P(V=3)=1/2; Q=41/25.
    second,fourth=D(5),D(41)
    assert D(4)/D(3)<fourth/second**2<D(2);checked+=1
    low,high=D('0.1'),D(30)
    for _ in range(210):
        mid=(low+high)/2
        q=D(3)*fourth/(2*second**2)
        a,b=ab(mid)
        if q*a+b>0:high=mid
        else:low=mid
    assert abs((low+high)/2-D('2.08102085125232078302751324342'))<D('1e-24');checked+=1
    # The fixed-speed dimension-five threshold exists; dimension four is negative at finite times.
    low,high=D('0.1'),D(40)
    for _ in range(210):
        mid=(low+high)/2
        a,b=ab(mid)
        if D(15)*a/D(7)+b>0:high=mid
        else:low=mid
    assert abs((low+high)/2-D('6.12239214208656'))<D('1e-12');checked+=1
    for x in [D('0.1'),D('1'),D('5'),D('25')]:
        a,b=ab(x)
        assert D(2)*a+b<0
        checked+=1
    print('PASS',checked,'analytic/Poisson-Dirichlet/symbolic coefficient checks')
    print('Two-speed 2D crossover gamma*t =', (low+high)/2 if False else '2.081020851252320783...')
    print('Fixed-speed 5D crossover gamma*t =',(low+high)/2)

if __name__=='__main__':main()
