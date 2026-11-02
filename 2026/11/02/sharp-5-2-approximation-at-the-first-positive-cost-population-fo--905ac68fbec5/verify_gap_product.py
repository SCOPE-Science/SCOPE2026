#!/usr/bin/env python3
"""Reproducible exact checks of the four-report three-facility product-gap bound."""
from fractions import Fraction
from itertools import combinations
from random import Random


def direct(points):
    assert len(points)==4 and all(points[i]<points[i+1] for i in range(3))
    numer=Fraction(0);denom=Fraction(0)
    for inds in combinations(range(4),3):
        s=[points[i] for i in inds]
        weight=(s[1]-s[0])*(s[2]-s[1])
        cost=sum(min(abs(q-t) for t in s) for q in points)
        numer+=weight*cost
        denom+=weight
    opt=min(points[i+1]-points[i] for i in range(3))
    return numer/denom/opt


def closed(x,y,z):
    N=2*x*y*z+z*(x+y)*min(x,y)+x*(y+z)*min(y,z)
    Z=2*(x*y+x*z+y*z)
    return Fraction(N,Z*min(x,y,z))


def run():
    seen=0; best=Fraction(0)
    for x in range(1,31):
        for y in range(1,31):
            for z in range(1,31):
                actual=direct([0,x,x+y,x+y+z]);formula=closed(x,y,z)
                assert actual==formula,(x,y,z,actual,formula)
                assert actual<Fraction(5,2),(x,y,z,actual)
                if actual>best:best=actual
                seen+=1
    random=Random(26102026)
    for _ in range(10000):
        gaps=[random.randint(1,10**8) for _ in range(3)]
        assert direct([0,gaps[0],gaps[0]+gaps[1],sum(gaps)])==closed(*gaps)
        assert closed(*gaps)<Fraction(5,2)
    for epsilon in (Fraction(1,10),Fraction(1,100),Fraction(1,1000),Fraction(1,10**6)):
        r=closed(epsilon,Fraction(1),Fraction(1))
        assert r==(5+epsilon)/(2*(1+2*epsilon))
        assert r<Fraction(5,2)
    print('PASS: 27,000 exact rational grid instances: direct subset enumeration = closed form; ratio < 5/2')
    print('PASS: 10,000 exact rational large-gap instances')
    print('PASS: analytic sharp family formula and four small gap limits')
    print('Largest 1..30 grid ratio:',best,'=',float(best))

if __name__=='__main__':run()
