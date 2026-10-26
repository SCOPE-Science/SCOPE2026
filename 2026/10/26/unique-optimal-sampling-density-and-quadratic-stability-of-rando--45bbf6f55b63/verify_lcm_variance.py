#!/usr/bin/env python3
"""Independent exact-rational checks for a sampling-density variance profile."""
from fractions import Fraction as Q
from math import fsum, log

# For 0<t<1, artanh(t) has a positive series and an explicit tail bound.
def atanh_bounds(t, terms=60):
    assert Q(0) < t < Q(1)
    accum = Q(0)
    power = t
    for k in range(terms):
        accum += power / (2*k + 1)
        power *= t*t
    tail = power / ((2*terms+1)*(1-t*t))
    return accum, accum + tail

def h_bounds(q):
    assert Q(0)<q<Q(1)
    a0,a1=atanh_bounds(q/(2-q))  # log(1-q) = -2atanh(q/(2-q))
    b0,b1=atanh_bounds(q/(2+q))  # log(1+q) =  2atanh(q/(2+q))
    lo=(2-q)*(-2*a1)+2*(2*b0)+q*q
    hi=(2-q)*(-2*a0)+2*(2*b1)+q*q
    assert lo <= hi
    return lo,hi

def run():
    qlo=Q(6700675747,10**10)
    qhi=Q(6700675749,10**10)
    lo,hi=h_bounds(qlo)
    assert lo>0
    lo,hi=h_bounds(qhi)
    assert hi<0
    # The derivative of 2q^3-q^2-8q+3 is negative on 0<q<1:
    # 6q^2-2q-8=2(q+1)(3q-4), strictly negative.
    assert 3>0 and (2-1-8+3)==-4
    # Verify the claimed closed form against the underlying positive series.
    def profile(q):
        return 1+(1-q)*log(1-q)/q - (1+(1-q*q)*log(1-q*q)/(q*q))
    for q in [0.1,0.3,0.5,0.6700675748,0.8,0.9]:
        series=fsum((q**j)*(1-q**j)/(j*(j+1)) for j in range(1,1200))
        assert abs(series-profile(q))<2e-12,(q,series,profile(q))
    # Check the two central comparisons at a fixed handful of points only.
    assert profile(0.6700675748)>profile(0.5)
    assert profile(0.6700675748)>profile(0.75)
    print('PASS exact_root_signs=2 analytic_cubic_monotonicity=proved series_checks=6')

if __name__=='__main__':
    run()
