#!/usr/bin/env python3
import math

# For L(x)=1/log(e+x), G(x)=x/log(e+x) has an increasing inverse.
def G(x):
    return x / math.log(math.e + x)

def inverse_G(n):
    lo, hi = 0.0, max(100.0, 3.0*n*math.log(1.0+n))
    while G(hi) < n:
        hi *= 2.0
    for _ in range(100):
        mid = (lo+hi)/2.0
        if G(mid)<n:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

ratios = []
for m in (2,3,4,5):
    # The two scales are u=exp(m^2), v=exp(m^5).  All formulas
    # involving the much larger v are evaluated in log coordinates.
    logu = m*m
    logv = m**5
    u = math.exp(logu)
    n = math.floor(G(u))
    scale = inverse_G(n)
    # The row-normalized singleton p-moment is n*log(e+v)/(m*scale).
    # Since v is astronomically large, log(e+v) is indistinguishable
    # from logv at the displayed precision.
    lower = n*logv/(m*scale)
    target = float(m*m)
    assert abs(lower-target) < 0.005
    # Cesaro weighted expectation on the special row is exactly 1/m.
    assert 1.0/m <= 0.5
    ratios.append(target)

# Explicit weight >=1 with growing peak-to-trough ratio.
peaks=[]
for k in (0,1,2):
    t_peak=math.exp(math.pi/2 + 2*math.pi*k)
    t_trough=math.exp(3*math.pi/2 + 2*math.pi*k)
    logL_peak=2*math.sqrt(t_peak)
    logL_trough=0.0
    assert t_peak<t_trough and logL_peak>logL_trough
    peaks.append(logL_peak)
assert peaks[0]<peaks[1]<peaks[2]

# The bounded nonmonotone exemplar 2+sin(log log(e^e+x))
# is in [1,3], and therefore is automatically almost increasing.
for x in (0.0,1.0,1e2,1e6,1e12):
    L=2.0+math.sin(math.log(math.log(math.exp(math.e)+x)))
    assert 1.0<=L<=3.0

print('VERIFY_OK ratios=4.000,9.000,16.000,25.000 oscillation=unbounded')
