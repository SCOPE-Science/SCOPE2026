#!/usr/bin/env python3
"""Finite exact coefficient checks and numerical reproducibility for a Jacobi/CIR fidelity hitting result.
Uses only the Python standard library; no random simulations or infinite certificates.
"""
from fractions import Fraction as Q
from math import exp, factorial, isclose


def transform_coefficient(n, q, k):
    c = Q(1)
    for j in range(k):
        c *= q + j + (Q(j*(j-1), n) if n else Q(0))
        c /= (j+1)*(j+1)
    return c


def mean_coefficient(n, k):
    c=Q(1, k*factorial(k))
    if n:
        for j in range(1,k-1):
            c *= 1+Q(j,n)
    return c


def mean_series(n,z,limit=120):
    val = 0.0
    for k in range(1,limit+1):
        # update via coefficient recurrence; n=None is limit
        val += float(mean_coefficient(n,k)) * z**k
    return val


def cumulant_sums(z,limit=160):
    h, b, harmonic, term = 0.0,0.0,0.0,1.0
    for k in range(1,limit+1):
        term *= z/k
        wk=term/k
        h+=wk
        b+=2*harmonic*wk
        harmonic+=1/k
        if k>z+30 and abs(wk)<1e-25: break
    return h,b


def test():
    asserts=0
    q=Q(7,11)
    for n in [3,5,8,17,51]:
        coeff=[transform_coefficient(n,q,k) for k in range(31)]
        for k in range(30):
            lhs=(k+1)**2*coeff[k+1]
            rhs=(q+k+Q(k*(k-1),n))*coeff[k]
            assert lhs==rhs
            asserts+=1
        for k in range(1,31):
            assert mean_coefficient(n,k)>0
            asserts+=1
            if k<=2:
                assert mean_coefficient(n,k)==mean_coefficient(None,k)
                asserts+=1
            else:
                assert mean_coefficient(n,k)>mean_coefficient(None,k)
                asserts+=1
    for n in [3,4,8,20,100]:
        for k in range(3,31):
            assert transform_coefficient(n,q,k)>transform_coefficient(n+1,q,k)
            assert transform_coefficient(n+1,q,k)>transform_coefficient(None,q,k)
            assert mean_coefficient(n,k)>mean_coefficient(n+1,k)>mean_coefficient(None,k)
            asserts+=3
    for z in [0.1,0.4,1.0,2.0,3.0]:
        h,b=cumulant_sums(z)
        assert h>0 and 0<b<h*h
        asserts+=1
        mean_limit=mean_series(None,z)
        assert isclose(mean_limit,h,rel_tol=5e-13)
        asserts+=1
        c=h+0.5*(z-3)*exp(z)+1.5
        assert c>0
        asserts+=1
        for n in [40,80,160,320]:
            if z>=n: continue
            m=mean_series(n,z)
            assert m>h
            asserts+=1
            err=abs(n*(m-h)-c)
            assert err<max(0.08*c,0.002) * (40/n)  # O(1/n) residual after scaling
            asserts+=1
    z=.001
    h,b=cumulant_sums(z)
    assert abs((1-b/(h*h))-.5)<.001
    asserts+=1
    z=15
    h,b=cumulant_sums(z)
    assert (1-b/(h*h))>.9999
    asserts+=1
    print(f'PASS: {asserts} exact-rational coefficient identities, strict comparisons and bounded numerical checks.')
    print('Limits and all-dimensional statements require the analytic argument, not these finite tests.')

if __name__=='__main__':
    test()
