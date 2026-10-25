"""Reproducible checks for two coeval inverse-time aftershock components.

Standard Python 3 library only. Checks complement, not replace, the proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose, log
from random import Random


def values(t, a, b, A, B):
    rate = A/(t+a) + B/(t+b)
    d_rate = -A/(t+a)**2 - B/(t+b)**2
    dd_rate = 2*A/(t+a)**3 + 2*B/(t+b)**3
    elasticity = -t*d_rate/rate
    derivative = -(d_rate+t*dd_rate)/rate + t*d_rate*d_rate/(rate*rate)
    pi = (A/(t+a))/rate
    X, Y = a/(t+a)**2, b/(t+b)**2
    Z = t*(b-a)**2/((t+a)**2*(t+b)**2)
    derived = pi*X+(1-pi)*Y-Z*pi*(1-pi)
    return elasticity, derivative, derived


def polynomial(t, R, w):
    c4 = R*w+R+w*w+w
    c3 = 4*R*(w+1)**2
    c2 = -R**3*w+6*R**2*w*w+7*R**2*w+7*R*w+6*R-w
    c1 = 4*R**3*w*w+8*R**2*w+4*R
    c0 = R**4*w*w+R**3*w+R**2*w+R
    return ((((c4*t+c3)*t+c2)*t+c1)*t+c0)


def derivative_from_polynomial(t, R, w):
    return polynomial(t,R,w)/((R+t)**2*(t+1)**2*(R*w+t*w+t+1)**2)


def bisect_zero(f, lo, hi):
    assert f(lo)*f(hi)<0
    for _ in range(110):
        mid = (lo+hi)/2
        if f(lo)*f(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def run():
    rng=Random(20261024)
    root=sqrt(2)
    critical=(3+2*root)**2
    for _ in range(3500):
        a=10**rng.uniform(-1,1)
        b=a*10**rng.uniform(0.0001,2.5)
        A,B=10**rng.uniform(-2,2),10**rng.uniform(-2,2)
        t=a*10**rng.uniform(-2.5,3)
        E,d,d2=values(t,a,b,A,B)
        assert 0<E<1
        assert isclose(d,d2,rel_tol=1e-8,abs_tol=2e-13)
        R=b/a;w=A/B;z=t/a
        assert isclose(a*d,derivative_from_polynomial(z,R,w),rel_tol=1e-7,abs_tol=2e-12)
        if R<critical*(1-1e-9):
            assert d>0, (a,b,A,B,t,d)
    # Exact rational witness at contrast 100 and weight one tenth.
    E,d,d2=values(F(10),F(1),F(100),F(1,10),F(1))
    assert E==F(1,2) and d==F(-41,4840) and d2==d
    R=100;w=.1
    f=lambda z:values(z,1,R,w,1)[1]
    u=bisect_zero(f,3,5)
    v=bisect_zero(f,25,28)
    assert 3.81<u<3.83 and 26.19<v<26.22
    assert f(1)>0 and f(10)<0 and f(100)>0
    assert 0<values(v,1,R,w,1)[0]<values(u,1,R,w,1)[0]<1
    # At the universal critical contrast the symmetric derivative touches zero.
    r=3+2*sqrt(2)
    E,d,d2=values(r,1,r*r,1/r,1)
    assert abs(E-.5)<1e-13 and abs(d)<1e-13
    # Well below the cutoff no amplitude is an exception, numerically.
    for ratio in [1.01,2,10,25,33.9]:
        for weight in [0.0001,.001,.01,.1,1,10,100,10000]:
            for i in range(201):
                t=10**(-3+7*i/200)
                assert values(t,1,ratio,weight,1)[1]>0
    print('PASS: 3500 randomized identities/derivatives; exact rational counterexample;')
    print('two isolated turning points: t_max=%.12f, t_min=%.12f' % (u,v))
    print('elasticities: %.12f, %.12f' % (values(u,1,R,w,1)[0],values(v,1,R,w,1)[0]))
    print('critical contrast = %.12f' % critical)
    print('PASS: threshold tangency and 8040 subthreshold samples')

if __name__=='__main__':
    run()
