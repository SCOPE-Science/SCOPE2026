"""Reproduce algebraic identities and representative pulse-peak tests.

Only the accompanying mathematical proof establishes the universal result.
"""
from fractions import Fraction
from math import sqrt, exp, expm1, log


def modes(c1, c2, damping, mixing):
    trace = (damping + mixing) / c1 + mixing / c2
    det = damping * mixing / (c1 * c2)
    discriminant = trace * trace - 4 * det
    assert discriminant > 0
    return (trace - sqrt(discriminant)) / 2, (trace + sqrt(discriminant)) / 2


def pulse_peak(c1, c2, damping, mixing, duration):
    a, b = modes(c1, c2, damping, mixing)
    delay = (log(-expm1(-b * duration)) - log(-expm1(-a * duration))) / (b - a)
    return duration + delay


def deep_kernel(t, c1, c2, damping, mixing):
    a, b = modes(c1, c2, damping, mixing)
    return mixing * (exp(-a * t) - exp(-b * t)) / (c1 * c2 * (b - a))


def deep_pulse(t, c1, c2, damping, mixing, duration, amplitude=1):
    a, b = modes(c1, c2, damping, mixing)
    low = max(0.0, t - duration)
    high = max(t, 0.0)
    return amplitude * mixing / (c1 * c2 * (b - a)) * (
        (exp(-a * low) - exp(-a * high)) / a
        - (exp(-b * low) - exp(-b * high)) / b
    )


def analytic_derivative(t, c1, c2, damping, mixing, duration):
    if t < duration:
        return deep_kernel(t, c1, c2, damping, mixing)
    return deep_kernel(t, c1, c2, damping, mixing) - deep_kernel(t-duration, c1, c2, damping, mixing)


# Exact polynomial coefficient identity in rational arithmetic.
c1, c2 = Fraction(8), Fraction(100)
l, g = Fraction(13, 10), Fraction(7, 10)
trace = (l+g)/c1+g/c2
det = l*g/(c1*c2)
assert c1*c2*trace == c2*(l+g)+c1*g
assert c1*c2*det == l*g

# Numerically corroborate signs, the exact stationary-time formula and comparative statics.
for parameters in ((8.0,100.0,1.3,0.7,10.0),
                   (1.0,1.0,1.0,1.0,2.0),
                   (2.0,20.0,0.5,4.0,1.0),
                   (10.0,3.0,0.2,0.1,15.0)):
    c1,c2,l,g,duration=parameters
    peak = pulse_peak(*parameters)
    assert peak>duration
    assert analytic_derivative(duration, *parameters)>0
    assert abs(analytic_derivative(peak, *parameters)) < 1e-12
    assert analytic_derivative(peak+max(0.1, duration/2), *parameters)<0
    for scale in (0.7, 1.3):
        t=peak*scale
        if t>0:
            assert deep_pulse(t,*parameters)<deep_pulse(peak,*parameters)
    for index in range(4):
        p=list(parameters);p[index]*=1.2
        other=pulse_peak(*p)
        if index<2:
            assert other>peak
        else:
            assert other<peak
    assert pulse_peak(c1,c2,l,g,duration*1.2)>peak
    assert pulse_peak(c1,c2,l,g,duration*1.2)-duration*1.2 < peak-duration

p=(8.,100.,1.3,.7,10.)
print('CHECK_OK representative_peak=%.10f delay=%.10f' % (pulse_peak(*p),pulse_peak(*p)-p[-1]))
