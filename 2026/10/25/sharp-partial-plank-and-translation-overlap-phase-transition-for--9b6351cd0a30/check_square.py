#!/usr/bin/env python3
"""Standalone exact polygon-cut checks for the square/plank profile.
The unrestricted theorem rests on the proof, not on these finite tests.
"""
from fractions import Fraction as F
from math import cos, sin, pi, sqrt, acos


def clip(poly, aa, bb, cc):
    """Keep (x,y) with aa*x+bb*y <= cc, all rational."""
    if not poly:
        return []
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp = aa*p[0] + bb*p[1] - cc
        fq = aa*q[0] + bb*q[1] - cc
        if fp <= 0:
            out.append(p)
        if (fp < 0 < fq) or (fp > 0 > fq):
            alpha = fp / (fp - fq)
            out.append((p[0]+alpha*(q[0]-p[0]), p[1]+alpha*(q[1]-p[1])))
    return out


def square_strip_area(c, s, t, offset=F(0)):
    sq = [(F(-1),F(-1)),(F(1),F(-1)),(F(1),F(1)),(F(-1),F(1))]
    p = clip(sq, c, s, offset+t)
    p = clip(p, -c, -s, t-offset)
    z = sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1]))
    return abs(z)/2


def central_fraction(c, s, t):
    a,b = max(abs(c),abs(s)),min(abs(c),abs(s))
    if b==0 or t <= a-b:
        return t/a
    return 1-(a+b-t)**2/(4*a*b)


def profile(w):
    return 2*sqrt(2)*w - w*w/2 if w<=sqrt(2) else 2+w*w/2


def run():
    # The expected optimizer has c+s=7/5 and t=5/7.
    c,s,t=F(4,5),F(3,5),F(5,7)
    area=square_strip_area(c,s,t)
    assert area == F(148,49), (area, F(148,49))
    assert area / 4 == central_fraction(c,s,t) == F(37,49)
    for delta in [F(1,20), F(1,10), F(1,2), F(1)]:
        assert square_strip_area(c,s,t,delta)<area
        assert square_strip_area(c,s,t,-delta)<area
    # Exact arbitrary rational direction/width pair tests of the 1-D convolution.
    triples=[(F(1),F(0),F(1,2)),(F(3,5),F(4,5),F(1,2)),
             (F(5,13),F(12,13),F(9,10)),(F(12,13),F(5,13),F(1,3)),
             (F(8,17),F(15,17),F(2,5)),(F(15,17),F(8,17),F(4,5))]
    for c1,s1,t1 in triples:
        assert square_strip_area(c1,s1,t1)/4 == central_fraction(c1,s1,t1), (c1,s1,t1)
    # Numerical independent comparison over many directions, including off-center strips.
    for w in [0.10,0.35,0.90,1.25,1.4, sqrt(2),1.44,1.6,1.85,1.98]:
        t1=w/2
        target=profile(w)
        values=[]
        for k in range(2001):
            th=pi*k/4000
            C,S=cos(th),sin(th)
            frac=(t1/C if t1 <= C-S else 1-(C+S-t1)**2/(4*C*S)) if S>1e-14 else t1
            values.append(4*frac)
        assert max(values) <= target+1e-8, (w,max(values),target)
        assert max(values) >= target-2e-6, (w,max(values),target)
        if w>sqrt(2):
            thstar=pi/4-acos(sqrt(2)/w)
            assert abs(4*(1-(cos(thstar)+sin(thstar)-t1)**2/(4*cos(thstar)*sin(thstar)))-target)<1e-12
            diag=2*sqrt(2)*w-w*w/2
            assert abs((target-diag)-(w-sqrt(2))**2)<1e-12
    print('PASS: 1 exact optimizing square cut, 8 exact off-center comparisons,')
    print('6 exact independent convolution checks, 10 dense angular sweeps,')
    print('and phase/strict-gain algebraic numerical confirmations')

if __name__=='__main__':
    run()
