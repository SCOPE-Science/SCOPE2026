#!/usr/bin/env python3
"""Exact reproducibility checks for Erlang immunization on balanced rooted trees.
All work uses fractions and elementary integer binomial coefficients.
This program verifies finite samples, not the all-parameter theorem.
"""
from fractions import Fraction as F
from math import comb

def S(h,d,q):
    return sum((F(comb(h+j-1,j))*q**j for j in range(d)),F(0))

def descendants(b,H,d):
    return sum(b**t for t in range(1,H-d+1))

def rewards(b,H,h,q):
    return [F(descendants(b,H,d))*(1-q)**h*S(h,d,q) for d in range(1,H)]

def race_probability(h,d,q):
    # infection step with q, immunization step with 1-q; competition ends when either wins
    @__import__('functools').lru_cache(None)
    def p(i,j):
        if i>=h: return F(1)
        if j>=d: return F(0)
        return (1-q)*p(i+1,j)+q*p(i,j+1)
    return p(0,0)

sample_count=0
for b in range(2,6):
    for H in range(2,12):
        for h in range(1,9):
            previous_first_peak=0
            for q in [F(1,10), F(1,3), F(1,2), F(2,3), F(3,4), F(9,10)]:
                rr=rewards(b,H,h,q)
                for d in range(1,H):
                    assert rr[d-1] == descendants(b,H,d)*race_probability(h,d,q)
                # Strict log-concavity, implies adjacent-only optimal depths.
                assert all(rr[i]*rr[i]>rr[i-1]*rr[i+1] for i in range(1,len(rr)-1))
                peaks=[i+1 for i,v in enumerate(rr) if v==max(rr)]
                assert len(peaks)<=2 and (len(peaks)==1 or peaks[1]==peaks[0]+1)
                assert peaks[0]>=previous_first_peak  # level moves outward as infection outruns maturation
                previous_first_peak=peaks[0]
                rising=sum(rr[i+1]>rr[i] for i in range(len(rr)-1))
                assert peaks[0]==1+rising
                if h==1: assert peaks==[1]
                if h==2 and b>=3: assert peaks==[1]
                if h==2 and b==2:
                    predicted= 2 if H>=4 and q>F(2**(H-2),2**(H-1)-2) else 1
                    if H>=4 and q==F(2**(H-2),2**(H-1)-2): assert peaks==[1,2]
                    else: assert peaks==[predicted]
                sample_count+=1
assert rewards(2,4,2,F(3,4))==[F(7,8),F(15,16),F(2,1)*F(1,16)*(1+2*F(3,4)+3*F(3,4)**2)]
assert rewards(2,4,2,F(2,3))[0]==rewards(2,4,2,F(2,3))[1]
assert rewards(2,4,1,F(3,4))[0]>rewards(2,4,1,F(3,4))[1]
print('PASS',sample_count,'exact rational parameter families; direct race recursion, strict log-concavity and sharp two-stage cases')
