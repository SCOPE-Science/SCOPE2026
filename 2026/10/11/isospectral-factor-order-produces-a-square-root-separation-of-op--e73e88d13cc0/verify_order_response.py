"""Standalone numerical diagnostic for two factor orders in a periodic oscillator.

The analytical argument, not discretization, proves the asymptotic theorem.
Uses only Python's standard library.  Run: python verify_order_response.py
"""
from math import sin, pi, exp, sqrt

PERIOD = 2*pi
N = 90000
STEP = PERIOD/N


def cumulative_trapezoid(values):
    accum = [0.0]
    running = 0.0
    previous = values[0]
    for current in values[1:]:
        running += STEP*(previous+current)/2
        accum.append(running)
        previous = current
    return accum


def constants(delta, a=1.0, b=1.0):
    time = [PERIOD*i/N for i in range(N+1)]
    exponent = [a*t+delta*sin(t) for t in time]
    integral = cumulative_trapezoid([exp(z) for z in exponent])
    base = integral[-1]/(exp(a*PERIOD)-1)
    v = [exp(-z)*(base+f) for z,f in zip(exponent,integral)]
    second = cumulative_trapezoid([exp(b*t)*z for t,z in zip(time,v)])
    base2 = second[-1]/(exp(b*PERIOD)-1)
    w = [exp(-b*t)*(base2+f) for t,f in zip(time,second)]
    return max(v)/b,max(w),time[max(range(len(w)),key=lambda i:w[i])]


def approximations(delta, a=1.0, b=1.0):
    common = exp(2*delta-a*pi)/(1-exp(-a*PERIOD))
    ka = common*sqrt(2*pi/delta)/b
    kb = common*(2*pi/delta)/(1-exp(-b*PERIOD))
    return ka,kb

ka0,kb0,_=constants(0)
print("delta0",repr(ka0),repr(kb0))
assert abs(ka0-1)<1e-7 and abs(kb0-1)<1e-7
previous_ratio = 0
previous_brel = 0
for delta in (25,80,240):
    ka,kb,phase=constants(delta)
    pa,pb=approximations(delta)
    ar=ka/pa
    br=kb/pb
    ratio=ka/kb
    assert 0.95<ar<1.08,(delta,ar)
    assert 0.65<br<0.94,(delta,br)
    assert ratio>previous_ratio,(delta,ratio)
    assert br>previous_brel,(delta,br)
    assert 1.5*pi<phase<1.5*pi+0.35,(delta,phase)
    previous_ratio=ratio
    previous_brel=br
    print(f"delta={delta}: KA/leading={ar:.8f} KB/leading={br:.8f} KA/KB={ratio:.8f}")
print("CHECK_OK")
