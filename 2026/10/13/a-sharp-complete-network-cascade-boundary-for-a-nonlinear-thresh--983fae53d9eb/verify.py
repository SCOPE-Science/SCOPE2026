#!/usr/bin/env python3
"""Exact algebra and finite examples for a complete-graph opinion cascade.

Standard-library arithmetic only. The universal statements require the proof
in RESULT.md; these calculations are not an exhaustive theorem certificate.
"""
from fractions import Fraction as F
from math import atan, pi, sqrt

COUNT=0
for n in range(2, 13):
    c=n-2
    for h in (4*n, 10*n, 100*n):
        s=F(1,h) # sqrt(gamma)
        gam=s*s
        critical_root=1+F(c,2)*s
        tau_star=critical_root**2
        assert gam < F(1,4*n*n)
        assert tau_star < 1/(4*gam)
        # Critical reduced scalar quadratic = (x-s)^2 exactly.
        mu=1-2*s*critical_root
        for x in (F(0), s/4, s/2, s, 2*s):
            q=x*x+(c*gam-2*s*critical_root)*x+gam
            assert q == (x-s)**2
        # Polynomial at x=s changes sign through the threshold.
        roots=[critical_root-F(1,20),critical_root,critical_root+F(1,20)]
        for R in roots:
            tau=R*R
            assert tau<F(1,4)/gam and R>0
            q_s=s*s+(c*gam-2*s*R)*s+gam
            assert (q_s>0) if R<critical_root else ((q_s==0) if R==critical_root else (q_s<0))
        # The source's clipped input remains below one through x=1/2.
        # This is needed for the exact passage-time quadrature at tau=1.
        mu_at_tie=1-2*s
        phi_half=mu_at_tie*F(1,2)+F(1,4)+gam*(1+F(c,2))
        assert F(0)<phi_half<1
        # n=2: no width; n>2: strict positive width.
        assert (tau_star>1)==(n>2)
        COUNT+=1

# Check the exact saddle ghost quadrature and its fixed-n asymptotic.
for n in (3,4,6,10):
    c=n-2
    ratios=[]
    for h in (200, 2000, 20000):
        s=1/h
        gam=s*s
        B=s-c*gam/2
        D2=c*gam**1.5-c*c*gam*gam/4
        assert D2>0
        D=sqrt(D2)
        time=(atan((.5-B)/D)+atan(B/D))/D
        ratios.append(time*gam**.75*sqrt(c)/pi)
    assert ratios[0]<ratios[1]<ratios[2]<1.0
    assert ratios[2]>.98

# Exact two numerical one-seed cases across strict LTM equality.
n,h=3,20
s=F(1,h); gam=s*s
star=(1+s/2)**2
assert F(1)<star
assert F(1)<F(1,4)/gam
print(f"VERIFY_OK: {COUNT} exact critical-polynomial parameter grids; "
      "strict LTM tie counterexamples and four saddle passage limits")
