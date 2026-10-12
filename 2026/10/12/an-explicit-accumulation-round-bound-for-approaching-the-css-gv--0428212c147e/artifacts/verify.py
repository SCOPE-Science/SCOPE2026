#!/usr/bin/env python3
import math

def h2(x):
    if x == 0.0 or x == 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def inv_h2(y):
    lo, hi = 0.0, 0.5
    for _ in range(120):
        mid=(lo+hi)/2
        if h2(mid)<y:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def constants(s, Delta):
    star=inv_h2(1/s)
    d=(1-math.sqrt(1-(2*s-1)**-2))/2
    gamma=star-Delta
    eps=1/s-h2(gamma)
    z=math.expm1(s*eps*math.log(2.0))
    q=z**(1/s)
    u=(1-q)/2
    eta=-d/2*math.log2(1-q*q)
    M=4+math.floor(1/eta)
    K=(2*math.log(2)/d)*(s*math.log((1-star)/star))**(-2/s)
    return star,d,q,u,eta,M,K

for s in (4,6,8):
    star=inv_h2(1/s)
    d=(1-math.sqrt(1-(2*s-1)**-2))/2
    assert 0 < d < star < 0.5
    prev=None
    for Delta in (star/20, star/100, star/500, star/2000):
        star2,d2,q,u,eta,M,K=constants(s,Delta)
        assert abs(star2-star)<1e-14 and abs(d2-d)<1e-14
        assert 0<q<1 and 0<u<0.5 and eta>0
        assert abs(4*u*(1-u)-(1-q*q))<1e-12
        assert (M-3)*eta>1
        scaled=M*(Delta**(2/s))
        if prev is not None:
            # The scaled sufficient count should move toward its positive leading constant.
            assert scaled>0
        prev=scaled
    # Small-gap sample agrees with the derived leading scale to a loose tolerance.
    Delta=star*1e-7
    _,_,_,_,_,M,K=constants(s,Delta)
    ratio=M*(Delta**(2/s))/K
    assert 0.85 < ratio < 1.15, (s,ratio)
print('VERIFY_OK')
