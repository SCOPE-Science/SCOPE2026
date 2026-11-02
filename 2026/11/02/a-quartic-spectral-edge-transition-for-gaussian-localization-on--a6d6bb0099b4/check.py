#!/usr/bin/env python3
"""Supplementary finite numerical checks of the displayed Gaussian-band formulas.

The proof of statements for all parameters and infinite-dimensional operators
is analytic and is provided separately; this program is supplementary.
Only the Python standard library is required.
"""
import math

SQRT_PI = math.sqrt(math.pi)


def bisect(f, lo, hi, iterations=100):
    fl, fh = f(lo), f(hi)
    assert fl * fh < 0, (lo, hi, fl, fh)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        fm = f(mid)
        if fm == 0:
            return mid
        if fm * fl > 0:
            lo, fl = mid, fm
        else:
            hi, fh = mid, fm
    return (lo + hi) / 2


def critical_a(width):
    return bisect(lambda a: 2*a*width + width*width -
                  math.log1p(width/a), .000001, max(width, 1)*10)


def multiplier(t, a, b):
    return (math.erf(b-t)-math.erf(a-t) +
            math.erf(b+t)-math.erf(a+t)) / 2


def derivative(t, a, b):
    return (math.exp(-(t-a)**2) - math.exp(-(t-b)**2) +
            math.exp(-(t+b)**2) - math.exp(-(t+a)**2))/SQRT_PI


def mode(a,b):
    q = a*math.exp(-a*a)-b*math.exp(-b*b)
    if q <= 1e-13:
        return 0
    def f(t):
        return math.exp(-a*a)*math.sinh(2*a*t) - math.exp(-b*b)*math.sinh(2*b*t)
    hi = 1.0
    while f(hi)>0: hi *= 1.5
    return bisect(f,1e-6,hi)


def simpson(f, left, right, n=2048):
    assert n%2==0
    step=(right-left)/n
    return step/3*(f(left)+f(right)+4*sum(f(left+step*i) for i in range(1,n,2))+
                   2*sum(f(left+step*i) for i in range(2,n,2)))


checks=0
for width in (.5, 1., 2.):
    ac=critical_a(width)
    bc=ac+width
    assert abs(ac*math.exp(-ac*ac)-bc*math.exp(-bc*bc))<2e-13
    checks+=1
    for offset in (-.1,-.02,0,.02,.1):
        a=ac+offset
        if a<=0:continue
        b=a+width
        t=mode(a,b)
        q=a*math.exp(-a*a)-b*math.exp(-b*b)
        if q>1e-12:
            assert t>0 and abs(derivative(t,a,b))<1e-11
            assert multiplier(t,a,b)>multiplier(0,a,b)
            for trial in (.2*t,.6*t,1.01*t,2*t):
                assert derivative(trial,a,b)*(t-trial)>-2e-13
            checks+=7
        else:
            assert abs(t)<1e-13
            for test in (.01,.1,.3,1.,2.,3.):
                assert multiplier(0,a,b)>multiplier(test,a,b)
            checks+=7
    for t in (0.,.1,.3,.7,1.,1.9):
        integ=simpson(lambda y:math.exp(-(t-y)**2)+math.exp(-(t+y)**2),ac,bc)/SQRT_PI
        assert abs(integ-multiplier(t,ac,bc))<2e-12
        checks+=1

# Resolving the universal square-root unfolding in the fixed-width family.
w=1.; ac=critical_a(w); bc=ac+w
c=ac*math.exp(-ac*ac)
Delta=bc*bc-ac*ac
qprime=c*w*(2+1/(ac*bc))
kappa2=3*qprime/(2*c*Delta)
gainco=3*qprime*qprime/(2*SQRT_PI*c*Delta)
for eps in (0.002,.001,.0005):
    a=ac+eps; b=a+w
    tm=mode(a,b)
    assert abs(tm/math.sqrt(eps)-math.sqrt(kappa2)) < .1
    gain=multiplier(tm,a,b)-multiplier(0,a,b)
    assert abs(gain/eps**2-gainco)<.055
    checks+=2

# Spectral edge at the coalescence: level-set length has exponent one quarter.
D=2*c*Delta/(3*SQRT_PI)
M=multiplier(0,ac,bc)
for s in (.0002,.0001,.00005):
    root=bisect(lambda t:multiplier(t,ac,bc)-(M-s), 1e-6,1.)
    ratio=(2*root)/(2*(s/D)**.25)
    assert abs(ratio-1)<.013,(s,ratio)
    checks+=1

print('PASS', checks, 'checks', 'critical_a_width_1', repr(ac),
      'sqrt_mode_constant',repr(math.sqrt(kappa2)),
      'quadratic_norm_gain_coefficient',repr(gainco),
      'quartic_edge_coefficient',repr(D))
