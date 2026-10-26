"""Finite diagnostics for an analytic study of a square-root cusp map.
These tests are not a proof of the infinite-scale assertions.
"""
from math import sqrt, log, isclose


def family(theta):
    K = (1-theta/2)/sqrt(2)
    L = 1+theta/2
    def f(x):
        t=abs(x-.5)
        return 1-theta*t-2*K*sqrt(t)
    def g0(y):
        z=(1-y)/(sqrt(K*K+theta*(1-y))+K)
        return .5-z*z
    def g1(y):
        z=(1-y)/(sqrt(K*K+theta*(1-y))+K)
        return .5+z*z
    return K,L,f,g0,g1


def check():
    checks=0
    for theta in (1.2,1.5,1.8):
        K,L,f,g0,g1=family(theta)
        d0=log(2)/log(L)
        assert 1 < d0 < 2 and 0 < d0/2 < 1
        for q in range(1001):
            y=q/1000
            for g in (g0,g1):
                assert isclose(f(g(y)),y,abs_tol=1e-11,rel_tol=1e-11)
                checks+=1
        assert isclose(f(.5),1,abs_tol=1e-14)
        assert isclose(f(0),0,abs_tol=1e-14)
        assert isclose(f(1),0,abs_tol=1e-14)
        delta=0.1
        x=delta
        b=[]
        for n in range(1,21):
            x=g0(x)
            if n in (10,15,20): b.append(x*L**n)
        assert max(b)-min(b) < 0.005
        for r in (1e-3,1e-4,1e-5,1e-6):
            q=theta*r+2*K*sqrt(r)
            assert isclose(f(.5+r),1-q,abs_tol=1e-12)
            assert isclose(f(.5-r),1-q,abs_tol=1e-12)
            checks+=2
        print(f"theta={theta} endpoint_exponent={d0:.12f} cusp_exponent={d0/2:.12f} iter_scale={b[-1]:.12f}")
    print(f"FINITE_IDENTITY_DIAGNOSTICS_PASS {checks}")

if __name__=='__main__':
    check()
