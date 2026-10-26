#!/usr/bin/env python3
"""Reproduce scalar checks for a finite pulse in an absorbing advection-dispersion channel.
Only the Python standard library is required. Numerical tests are not a proof of the theorem.
"""
import math
import random


def equation(w, T, a):
    """Positive-root equation for reciprocal post-shutoff lag, w=c/delta."""
    tw = T * w
    return w - a*T - 1.5*math.log1p(tw) - w/(1.0+tw)


def root(T, a):
    assert T > 0 and a >= 0
    lo = 1e-12
    hi = max(10.0, a*T+20.0*math.log1p(T)+20.0)
    while equation(hi, T, a) <= 0.0:
        hi *= 2
    assert equation(lo, T, a) < 0 < equation(hi, T, a)
    for _ in range(130):
        mid = (lo+hi)/2.0
        if equation(mid,T,a) > 0: hi=mid
        else: lo=mid
    return (lo+hi)/2.0


def logdensity(t, a):
    return -1.5*math.log(t)-1.0/t-a*t


def logderivative(t, a):
    return -1.5/t+1.0/t**2-a


def mode(a):
    return 2.0/(1.5+math.sqrt(2.25+4.0*a))


def verify_one(T,a):
    w=root(T,a)
    y=1/w
    arrival=y+T
    m=mode(a)
    assert y<m<arrival, (T,a,y,m,arrival)
    assert abs(logdensity(y,a)-logdensity(arrival,a))<2e-8
    r1=logdensity(y*0.999,a)-logdensity(y*0.999+T,a)
    r2=logdensity(y*1.001,a)-logdensity(y*1.001+T,a)
    assert r1<0<r2, (T,a,r1,r2)
    us=logderivative(y,a)
    ut=logderivative(arrival,a)
    dt_dT=us/(us-ut)
    assert 0<dt_dT<1
    return y


def main():
    # Exact positive-root equation and crossing checks across dimensionless regimes.
    rng=random.Random(20261023)
    for _ in range(2000):
        T=10**rng.uniform(-1.25,5)
        a=0.0 if rng.random()<0.25 else 10**rng.uniform(-3,1.5)
        verify_one(T,a)
    print('2000 seeded pulse-peak derivative/crossing checks: PASS')

    # Drift shortens post-shutoff lag for identical duration and source scale.
    for _ in range(300):
        T=10**rng.uniform(-1,4)
        a1=10**rng.uniform(-4,-0.2)
        a2=a1+10**rng.uniform(-3,1)
        assert root(T,a2)>root(T,a1)
    print('300 drift-ordered lag checks: PASS')

    # The pulse duration moves peak time forward at speed between zero and one.
    for _ in range(300):
        a=10**rng.uniform(-4,1)
        T1=10**rng.uniform(-1,3)
        T2=T1*(1.0+rng.random())
        s1=1/root(T1,a)
        s2=1/root(T2,a)
        assert s2<s1 and T2+s2>T1+s1
    print('300 duration-ordered peak checks: PASS')

    # Dimensionless c=1 examples, where physical time is in units c.
    for a in (0.0,1.0):
        print('example T=100 a=%g post_shutoff_lag=%.11f'%(a,1/root(100,a)))

    # Exact asymptotic scales, checking convergent residuals at large horizon.
    T=math.exp(300)
    w0=root(T,0.0)
    refined=1.5*(math.log(T)+math.log(math.log(T))+math.log(1.5))
    assert abs(w0-refined)<0.04,(w0,refined)
    print('driftless refined log-log residual:',w0-refined)
    for a in (0.01,1.0,10.0):
        U=1e6
        wa=root(U,a)
        refined=a*U+3*math.log(U)+1.5*math.log(a)
        assert abs(wa-refined)<0.01,(wa,refined)
        print('positive-drift refined reciprocal lag a=%g residual=%.7f'%(a,wa-refined))
    for theta in (0.25,1.0,4.0):
        logT=300.0
        T=math.exp(logT)
        a=theta*logT/T
        w=root(T,a)
        assert abs(w/logT-(theta+1.5))<0.06
        print('crossover theta=%g empirical coefficient=%.7f'%(theta,w/logT))
    print('AS STATED: all executable checks PASS; analytic proof remains necessary.')

if __name__=='__main__':main()
