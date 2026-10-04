#!/usr/bin/env python3
import math

def ystar(delta, a):
    q = delta / a
    return (q - 3.0 + math.sqrt((q + 1.0) * (q + 9.0))) / 4.0

def g(y, delta, a):
    return y*y*(delta-a*y)/(1.0+y)

for delta, a in [(1.0,2.0),(2.0,1.0),(0.2,3.0),(10.0,1.0),(3.7,4.2)]:
    y = ystar(delta,a)
    assert 0.0 < y < delta/a
    stationary = 2*delta + (delta-3*a)*y - 2*a*y*y
    assert abs(stationary) < 2e-12*(1+delta+a)
    best = g(y,delta,a)
    for j in range(1,10000):
        z = (delta/a)*j/10000.0
        assert g(z,delta,a) <= best + 2e-10*(1+best)

# Double-delta specialization: solve 2*k = alpha*(1+exp(-2*k*rho))
for alpha, rho in [(1.0,1.0),(2.0,0.4),(0.7,2.0),(3.0,0.2)]:
    lo = alpha/2.0
    hi = alpha
    for _ in range(120):
        k = (lo+hi)/2.0
        f = 2*k-alpha*(1+math.exp(-2*k*rho))
        if f > 0: hi = k
        else: lo = k
    k = (lo+hi)/2.0
    lhs = (math.exp(2*k*rho)+1)/(2*k)
    rhs = 1/(2*k-alpha)
    assert abs(lhs-rhs) < 2e-11*(1+rhs)
print('VERIFY_OK optimizer_cases=5 delta_cases=4')
