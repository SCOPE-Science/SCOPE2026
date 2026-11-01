#!/usr/bin/env python3
"""Self-contained rational branch and endpoint phase checks; not a proof of the infinite theorem."""
from fractions import Fraction as Q
from math import log, sqrt

def maps(am,bm,ap,bp):
    xm=(bm-1)/(bm-am); xp=(1-ap)/(bp-ap)
    def fm(x): return am*x if x<=xm else 1-bm*(1-x)
    def fp(x): return bp*x if x<=xp else 1-ap*(1-x)
    return xm,xp,fm,fp

def check():
    am,bm,ap,bp=Q(1,4),Q(2),Q(3,4),Q(16)
    xm,xp,fm,fp=maps(am,bm,ap,bp)
    assert (xm,xp)==(Q(4,7),Q(1,61))
    assert fm(Q(0))==fp(Q(0))==0 and fm(Q(1))==fp(Q(1))==1
    assert am*xm==1-bm*(1-xm)
    assert bp*xp==1-ap*(1-xp)
    assert am*bp>1 and bm*ap>1  # Strict positive log means for equal probabilities.
    assert Q(1,2)/am+Q(1,2)/bp>1
    assert Q(1,2)/bm+Q(1,2)/ap<1
    d0=min(am*xm,bp*xp); d1=min(bm*(1-xm),ap*(1-xp))
    assert (d0,d1)==(Q(1,7),Q(45,61))
    assert d0/am==xm and d1/ap==(1-xp)
    checked=0
    for denominator in [100,251,1009,10007]:
        for j in range(1,denominator):
            r=Q(j,denominator)
            if r<d0:
                # Increasing maps: left-end inverse images lie entirely on the first affine pieces.
                assert fm(r/am)==r and fp(r/bp)==r
                assert r/am<=xm and r/bp<=xp
                checked+=2
            if r<d1:
                # Right-end inverse images lie on the last affine pieces.
                assert fm(1-r/bm)==1-r and fp(1-r/ap)==1-r
                assert 1-r/bm>=xm and 1-r/ap>=xp
                checked+=2
    # Exact golden-ratio factorization for the left slope Cramer root.
    golden=(1+sqrt(5))/2
    assert abs((golden-1)*(golden*golden-golden-1))<1e-12
    k0=log(golden)/log(4)
    def right_eq(t): return (2.0**(-t)+(4/3)**t)/2-1
    lo,hi=1.0,2.0
    assert right_eq(lo)<0 and right_eq(hi)>0
    for _ in range(90):
        mid=(lo+hi)/2
        if right_eq(mid)>0:hi=mid
        else:lo=mid
    k1=(lo+hi)/2
    assert 0<k0<1<k1<2 and abs(right_eq(k1))<1e-13
    print('PASS',checked,'exact rational branch checks; roots',format(k0,'.12f'),format(k1,'.12f'))
if __name__=='__main__':check()
