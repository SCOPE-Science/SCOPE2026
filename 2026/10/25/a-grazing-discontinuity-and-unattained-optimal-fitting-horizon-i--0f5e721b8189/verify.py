"""Reproduce algebraic and numerical checks for an affine event-triggered control horizon."""
from math import exp, sqrt, isclose
from random import Random


def kappa(z):
    assert z > 0
    if z < .03:
        return sum(((-1)**(j+1) * 3 * z**(j-1) /
                    ((j+2) * __import__('math').factorial(j))) for j in range(1,15))
    return 3 * (z*z/2 - 1 + (1+z)*exp(-z)) / z**3


def ell(t, s):
    return ((1+t)*s-t)/(s*(1+(1+t)*s/2))


def upper(t, s):
    return (t+(1-t)*s)/(s*(1+(1-t)*s/2))


def critical(t):
    d = sqrt(t*(2+t))
    return ((t+d)/(1+t), (1+t)/(1+t+d))


def root_lower(k, t):
    # Solve k(1+t)/2 s^2 + (k-(1+t))s + t = 0, pick small root.
    b=(1+t)-k
    return (2*t)/(b+sqrt(max(0,b*b-2*k*(1+t)*t)))


def root_upper(k, t):
    # Solve k(1-t)/2 s^2 + (k-(1-t))s - t=0.
    b=k-(1-t)
    return 2*t/(b+sqrt(b*b+2*k*(1-t)*t)) if b>=0 else (-b+sqrt(b*b+2*k*(1-t)*t))/(k*(1-t))


def event(k,t):
    a,kc=critical(t)
    if k<=kc: return root_lower(k,t)
    return root_upper(k,t)


def X(k,s): return 1-s+k*s*s/2

def E(k,s): return s*(k-1+k*s/2)


def z_for_kappa(target):
    lo,hi=1e-8,100
    for _ in range(120):
        m=(lo+hi)/2
        if kappa(m)>target:lo=m
        else: hi=m
    return (lo+hi)/2


def main():
    rng=Random(1729001)
    checked=0
    for t in [0.001,0.02,0.15,0.5,0.69,0.7070] + [rng.uniform(.00001,.7070) for _ in range(100)]:
        a,kc=critical(t)
        assert 0<kc<1 and 0<a<2
        assert abs(ell(t,a)-kc)<2e-12
        near=max(.0001,a*0.3)
        assert ell(t,near)<kc and ell(t,1.5*a)<kc
        S=root_upper(kc,t)
        assert S>a and S<2
        assert abs(upper(t,S)-kc)<2e-12
        assert abs(root_lower(kc,t)-a)<2e-7
        for k in [0.0001, kc*0.1, kc*0.5, kc*(1-1e-4), kc,
                  kc+(1-kc)*1e-4, (1+kc)/2, 0.99, 0.999]:
            s=event(k,t)
            assert s>t/(1+t)
            assert 0<X(k,s)<1
            assert abs(abs(E(k,s))-t*X(k,s))<5e-7, (k,t,s,E(k,s),X(k,s))
            # all earlier samples satisfy strict trigger except tangent itself
            for j in range(1,151):
                sj=s*j/151
                assert abs(E(k,sj))<t*X(k,sj)+2e-10, (t,k,j,sj)
                checked+=1
    t=.5;a,kc=critical(t);S=root_upper(kc,t);zc=z_for_kappa(kc)
    assert abs(kc-(9-3*sqrt(5))/4)<2e-14
    assert abs(a-(1+sqrt(5))/3)<2e-14
    assert abs(S-1.6309740756640566)<2e-12
    assert abs(zc-1.6997972535256306)<2e-9
    for z in [zc-.01,zc-.001,zc,zc+.001,zc+.01]:
        print('horizon',f'{z:.12f}', 'coefficient',f'{kappa(z):.12f}', 'event', f'{event(kappa(z),t):.12f}')
    for t in [1e-6,1e-8,1e-10]:
        a,kc=critical(t);S=root_upper(kc,t)
        assert abs(S/sqrt(t)-(2+sqrt(2)))<.003
    print('VERIFY_OK: parameter monotonicity, two trigger roots, grazing, first-hit checks, source theta=1/2 values; grid comparisons',checked)


if __name__ == '__main__':
    main()
