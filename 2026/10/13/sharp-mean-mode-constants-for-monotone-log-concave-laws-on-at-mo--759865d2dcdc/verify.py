#!/usr/bin/env python3
from fractions import Fraction

def root(f, lo=0.0, hi=1.0, steps=120):
    for _ in range(steps):
        mid=(lo+hi)/2.0
        if f(mid)<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

r4=root(lambda r:r*r*(1+2*r)-1)
r5=root(lambda r:r*r*(1+2*r+3*r*r)-1)
assert abs(r4-0.6572981061383759908)<2e-15
assert abs(r5-0.5677373609406794914)<2e-15

def mean_geom(r,n):
    w=[r**j for j in range(n)]
    return sum(j*w[j] for j in range(n))/sum(w)
assert abs(mean_geom(r4,4)-1.0)<2e-15
assert abs(mean_geom(r5,5)-1.0)<2e-15

# Supplemental exact-rational grid checks. These do not prove the theorem.
for N, rstar in [(4,r4),(5,r5)]:
    vals=[Fraction(i,20) for i in range(1,21)]
    checked=0
    if N==4:
        for a in vals:
            for b in vals:
                if b>a: continue
                for c in vals:
                    if c>b: continue
                    w=[Fraction(1),a,a*b,a*b*c]
                    mu=sum(Fraction(j)*w[j] for j in range(4))/sum(w)
                    if mu>=1:
                        assert float(a)+1e-15>=rstar
                        checked+=1
    else:
        for a in vals:
            for b in vals:
                if b>a: continue
                for c in vals:
                    if c>b: continue
                    for d in vals:
                        if d>c: continue
                        w=[Fraction(1),a,a*b,a*b*c,a*b*c*d]
                        mu=sum(Fraction(j)*w[j] for j in range(5))/sum(w)
                        if mu>=1:
                            assert float(a)+1e-15>=rstar
                            checked+=1
    assert checked>0
print('VERIFY_OK r4=%.16f r5=%.16f' % (r4,r5))
