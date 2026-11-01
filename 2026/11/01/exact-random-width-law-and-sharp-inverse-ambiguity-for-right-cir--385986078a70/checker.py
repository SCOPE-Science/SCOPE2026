"""Standalone verification for the random width of a circular cylinder."""
import math
from scipy.integrate import quad
from scipy.optimize import brentq


def cdf(w, diameter, height):
    a, b = diameter, height
    s2=a*a+b*b; s=math.sqrt(s2)
    if w<=min(a,b): return 0.
    if w>=s: return 1.
    z=math.sqrt(max(0.,s2-w*w))
    if w>=max(a,b): return 1.-2.*a*z/s2
    if a<b: return (b*w-a*z)/s2
    return 1.-(b*w+a*z)/s2


def width(t,a,b):
    return a*math.sqrt(1.-t*t)+b*t

for a,b in [(1.,2.),(2.,1.),(1.,1.),(0.04,10.),(10.,0.04),(.5,3.)]:
    s=math.hypot(a,b)
    for j in range(1,101):
        z=min(a,b)+(s-min(a,b))*j/101
        # Independent numerical inversion on the two monotone intervals.
        peak=b/s
        v1=brentq(lambda t: width(t,a,b)-z,0,peak,xtol=1e-14) if z>=a else 0.
        v2=1.-brentq(lambda t: width(t,a,b)-z,peak,1,xtol=1e-14) if z>=b else 0.
        assert abs(v1+v2-cdf(z,a,b))<1e-9,(a,b,z,v1+v2,cdf(z,a,b))
    mu=quad(lambda t:width(t,a,b),0,1,epsabs=1e-12)[0]
    assert abs(mu-(math.pi*a/4+b/2))<2e-12
    m=min(a,b); swapped_mu=math.pi*b/4+a/2
    assert abs(abs(mu-swapped_mu)-(math.pi-2)/4*abs(a-b))<2e-12
    # Verify total continuous density via derivative-free CDF endpoints.
    assert abs(cdf(m,a,b))<1e-12 and abs(cdf(s,a,b)-1)<1e-12
print('INDEPENDENT_MONOTONE_ROOTS_VERSUS_CDF_PASSED')
print('MEAN_AND_SHARP_SWAP_GAP_PASSED')
print('ALL_CHECKS_PASSED')
