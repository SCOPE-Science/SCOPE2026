#!/usr/bin/env python3
"""Exact-rational checks for two-atom random-step backward Euler OU tails.
Only standard-library modules are required. Finite checks do not replace the proof.
"""
from fractions import Fraction as Q
from random import Random
from math import log, isclose


def parameters(lam, sig, h):
    rate = Q(1, 1) / (1 + lam*h)
    return rate**2, sig**2*h*rate**2, sig**2/(lam*(2+lam*h))


def variance(lam, sig, a, b, p):
    r, u, va = parameters(lam, sig, a)
    s, w, vb = parameters(lam, sig, b)
    return (p*u+(1-p)*w)/(1-p*r-(1-p)*s)


def test():
    checks = 0
    lam = Q(1); sig = Q(1)
    cases = [(Q(1),Q(3),Q(1,2)), (Q(3,2),Q(4),Q(4,5))]
    for a,b,p in cases:
        assert p*a+(1-p)*b == 2
        assert variance(lam,sig,a,b,p) == Q(7,27)
        checks += 2
    r1,_,v1 = parameters(lam,sig,Q(1)); r2,_,v2=parameters(lam,sig,Q(3,2))
    assert v1==Q(1,3) and v2==Q(2,7)
    assert r1==Q(1,4) and r2==Q(4,25)
    assert Q(1,2)/v1 == Q(3,2)
    assert Q(1,2)/v2 == Q(7,4)
    assert Q(1,2)/v2-Q(1,2)/v1 == Q(1,4)
    checks += 5
    rnd = Random(220609970)
    for _ in range(6000):
        lam=Q(rnd.randrange(1,12),rnd.randrange(1,13))
        sig=Q(rnd.randrange(1,11),rnd.randrange(1,11))
        a=Q(rnd.randrange(1,10),rnd.randrange(1,13))
        b=a+Q(rnd.randrange(1,12),rnd.randrange(1,13))
        p=Q(rnd.randrange(1,16),rnd.randrange(16,30))
        r,u,va=parameters(lam,sig,a)
        s,w,vb=parameters(lam,sig,b)
        assert Q(0)<s<r<Q(1)
        assert va>vb>Q(0)
        assert u==(1-r)*va and w==(1-s)*vb
        v=variance(lam,sig,a,b,p)
        assert vb<v<va
        assert v==p*(r*v+u)+(1-p)*(s*v+w)
        # Defect map: short step shrinks, long step shifts it upward.
        D=va-v
        Delta=va-vb
        B=(1-s)*Delta
        assert va-(r*v+u)==r*D
        assert va-(s*v+w)==s*D+B
        assert Q(0)<B<=B+s*D<=Delta
        checks += 8
    # Check deterministic endpoint sandwich for finite sequences at exact fractions.
    lam=sig=Q(1); a=Q(1); b=Q(3)
    r,u,va=parameters(lam,sig,a)
    s,w,vb=parameters(lam,sig,b)
    Delta=va-vb; B=(1-s)*Delta
    for n in range(0,9):
        for mask in range(1<<8):
            d=Q(0)
            for i in range(8):
                if mask>>i&1:
                    d=s*d+B
                else:
                    d=r*d
            # The first long-step contribution, after n initial short steps:
            d = r**n*(s*d+B)
            assert r**n*B <= d <=r**n*Delta
            checks += 1
    for p,r in [(Q(1,2),Q(1,4)),(Q(4,5),Q(4,25))]:
        kappa=log(1/float(p))/log(1/float(r))
        assert kappa>0
        checks += 1
    print(f'PASS: {checks} exact-rational and numeric-parameter assertions; no finite census claimed as an infinite proof.')


if __name__=='__main__':
    test()
