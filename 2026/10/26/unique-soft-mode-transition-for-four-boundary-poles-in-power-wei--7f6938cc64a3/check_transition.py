"""Reproducible exact endpoint-sign and rational-identity checks for a four-pole Bergman energy."""
from fractions import Fraction as Q
from math import log, pi

def a(t):
    return (1-t)/(1+t)**3

def b(t):
    return 4*t*(1-t*t)/(1+t*t)**3

def f2_partial(t):
    return (-24*(t-3)/(t*t+1)**2 + 12*(t-2)/(t*t+1)
            - 3 - 48/(t*t+1)**3 + 18/(t+1)
            - 36/(t+1)**2 + 24/(t+1)**3)

def f3_partial(t):
    return (4*t +64*(t-1)/(t*t+1)**3
            -64*(2*t-1)/(t*t+1)**2 +16*(3*t+1)/(t*t+1)
            -44+96/(t+1)-128/(t+1)**2+64/(t+1)**3)

# Each difference has a common strictly positive denominator
# (1+t)^3*(1+t^2)^3 and a polynomial numerator of degree <= 10.
# Twelve distinct exact roots thus prove each partial-fraction identity.
for m in range(1, 13):
    t = Q(m, 31)
    assert 3*(1-t)**2*(a(t)-b(t)) == f2_partial(t)
    assert 4*(1-t)**3*(a(t)-b(t)) == f3_partial(t)

# Machin pi identity, alternating rational arctangent series.
def atan_bracket(x, n=12):
    s = sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(n)), Q(0))
    term = x**(2*n+1)/Q(2*n+1)
    assert n % 2 == 0
    return s, s+term
lo5, hi5 = atan_bracket(Q(1,5))
lo239, hi239 = atan_bracket(Q(1,239))
pi_lo,pi_hi = 16*lo5-4*hi239,16*hi5-4*lo239
assert Q(314159,100000) < pi_lo < pi_hi < Q(314160,100000)

# log 2 = 2 artanh(1/3), with a geometric bound on its positive tail.
n=14
x=Q(1,3)
log_lo = 2*sum((x**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
log_hi = log_lo + 2*x**(2*n+1)/(Q(2*n+1)*(1-x*x))
assert Q(693147,1000000) < log_lo < log_hi < Q(693148,1000000)

# Exact antiderivative endpoint values are:
# F(2) = -12 - 3*pi/2 + 24*log(2).
# F(3) = -102 + 6*pi + 120*log(2).
f2_hi = -12-Q(3,2)*pi_lo+24*log_hi
f3_lo = -102+6*pi_lo+120*log_lo
assert f2_hi < 0 and f3_lo > 0
print('PASS: rational partial fractions and rigorous endpoint signs')
print('Certified sign margins (upper for F(2), lower for F(3)): ',
      float(f2_hi), float(f3_lo))

# Optional noncertifying numerical estimate of the unique root.
def simpson(alpha, n=4096):
    def val(t):
        return (alpha+1)*(1-t)**alpha*(float(a(t))-float(b(t)))
    h=1/n
    return h/3*(val(0)+val(1)+4*sum(val(k*h) for k in range(1,n,2))
                +2*sum(val(k*h) for k in range(2,n,2)))
lo,hi=2.0,3.0
for _ in range(35):
    m=(lo+hi)/2
    if simpson(m)>0:hi=m
    else:lo=m
print('Approximate crossover exponent (not proof):', (lo+hi)/2)
