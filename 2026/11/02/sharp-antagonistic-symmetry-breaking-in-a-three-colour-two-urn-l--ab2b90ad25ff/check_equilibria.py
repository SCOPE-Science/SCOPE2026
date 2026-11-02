#!/usr/bin/env python3
"""Numerical sanity checks for the two-site three-colour logistic equilibrium theorem.
The accompanying proof establishes the all-parameter statements analytically.
"""
import itertools
import math


def bisect_sign_change(f, lo, hi, iterations=100):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        if f(mid) * flo > 0:
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def constructed(a):
    r = bisect_sign_change(lambda t: math.atanh(t)-a*t, 1e-5, 1-1e-12)
    H = lambda b: math.tanh(2*a*b)-b-math.atanh(b)/a
    b = bisect_sign_change(H, 1e-5, 1-1e-12)
    v = math.tanh(2*a*b)
    states = [(0., 0., 0.)]
    states += list(set(itertools.permutations((r,0.,-r))))
    states += list(set(itertools.permutations((-b,-b,v))))
    states += list(set(itertools.permutations((b,b,-v))))
    assert len(states) == 13
    return r,b,v,states


def drift(z,a):
    return [ -z[i]+math.tanh(-a*(sum(z)-z[i])) for i in range(3)]


def test():
    checks=0
    for a in [1.01,1.05,1.1,1.2,1.5,2.,3.,5.,8.,10.]:
        r,b,v,states=constructed(a)
        s=1-r*r
        trace=-2-a*s
        det=1+a*s-2*a*a*s
        antisym=a*s-1
        assert 0<r<1 and 0<b<1 and 0<v<1 and v>b
        assert trace<0 and det>0 and antisym<0,(a,trace,det,antisym)
        checks+=6
        for z in states:
            assert max(abs(t) for t in drift(z,a)) < 3e-12, (a,z,drift(z,a))
            checks+=3
        # Direct finite differences cross-check the analytic Jacobian.
        z=(r,0.,-r)
        eps=1e-6
        for i,j in itertools.product(range(3),repeat=2):
            plus=list(z);minus=list(z)
            plus[j]+=eps;minus[j]-=eps
            derivative=(drift(plus,a)[i]-drift(minus,a)[i])/(2*eps)
            expected=(-1. if i==j else -a*(1-z[i]*z[i]))
            assert abs(derivative-expected)<1e-6,(a,i,j,derivative,expected)
            checks+=1
    # Monotonicity certificate for the low-interaction branch.
    for a in [.01,.5,.9,1.]:
        for z in [-.95,-.5,-.01,0.,.01,.5,.95]:
            assert 1/(1-z*z)-a >= 0
            checks+=1
    print('PASS',checks,'checks; ten interaction strengths, 13 solutions each')

if __name__=='__main__':
    test()
