#!/usr/bin/env python3
"""Reproducible numerical diagnostics for the integrable ABC rotation theorem.

Only Python standard-library dependencies; universal conclusions require the
analytic proof in RESULT.md rather than these finite tests.
"""
import math
from fractions import Fraction


def simpson_integral(f, a, b, n):
    assert n > 0 and n % 2 == 0
    h = (b-a)/n
    value = f(a)+f(b)
    for j in range(1,n):
        value += (4 if j % 2 else 2)*f(a+j*h)
    return h*value/3


def rho(B,C,E,n=16384):
    assert B>C>0 and B-C<E<B+C
    u=(B+C-E)/(2*B)
    w=(C+E-B)/(2*B)
    integral=simpson_integral(
        lambda phi: 1/math.sqrt((1-u*math.sin(phi)**2)
                                      *(w+u*math.sin(phi)**2)),
        0,math.pi/2,n)
    period=4*integral/B
    return E*period/(2*math.pi)


def bisection(f,lo,hi,steps=68):
    vlo=f(lo);vhi=f(hi)
    assert vlo*vhi<0, (lo,hi,vlo,vhi)
    for _ in range(steps):
        mid=(lo+hi)/2
        vm=f(mid)
        if vm*vlo<=0:
            hi=mid
        else:
            lo=mid;vlo=vm
    return (lo+hi)/2


def main():
    rcrit=3+2*math.sqrt(2)
    assert 5<rcrit<6
    assert (Fraction(2+1)**2-8*Fraction(2)*Fraction(1)) == -7
    assert (Fraction(6+1)**2-8*Fraction(6)*Fraction(1)) == 1
    assert (2+1)**2 < 8*2*1 and (6+1)**2 > 8*6*1

    B,C=2.,1.
    rho0=(B+C)/math.sqrt(B*C)
    coeff=((B+C)**2-8*B*C)/(8*(B*C)**1.5)
    assert coeff<0
    for k in (0.01,0.001):
        computed=(rho(B,C,B+C-k)-rho0)/k
        assert abs(computed-coeff)<0.012, (k,computed,coeff)

    for E in (1.1,1.5,2.5,2.99):
        coarse=rho(B,C,E,n=8192)
        fine=rho(B,C,E,n=16384)
        assert abs(coarse-fine)<2e-9, (E,coarse,fine)

    assert rho(B,C,1.000001)>rho(B,C,1.01)
    assert rho(B,C,1.25)<rho0
    rleft=bisection(lambda E:rho(B,C,E)-1.75,1.00001,1.25)
    rright=bisection(lambda E:rho(B,C,E)-1.75,1.25,2.99)
    assert 1.03<rleft<1.04 and 1.91<rright<1.93
    assert abs(rho(B,C,rleft)-1.75)<1e-10
    assert abs(rho(B,C,rright)-1.75)<1e-10
    print('PASS: sharp center-twist signs, quadrature convergence, two rational-resonant energies')
    print('Example B=2,C=1, axial turns per planar cycle=7/4:',rleft,rright)


if __name__=='__main__':
    main()


def verify_singular_scaling():
    # Finite-parameter diagnostics only; asymptotic proof is in RESULT.md.
    for delta in (0.01, 0.003, 0.001):
        L=math.log(1/delta)
        s=delta/(2*L)
        observed=rho(1+delta, 1.0, delta+s, n=32768)
        leading=delta/math.pi*(2*L+math.log(L))
        assert observed>0 and 0.5<observed/leading<2.5
    return True

if __name__ == '__main__':
    verify_singular_scaling()
    print('SINGULAR_SCALING_DIAGNOSTICS_OK')
