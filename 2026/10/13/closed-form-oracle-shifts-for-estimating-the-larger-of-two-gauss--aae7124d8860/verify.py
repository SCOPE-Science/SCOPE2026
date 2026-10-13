#!/usr/bin/env python3
import math

SQRT2 = math.sqrt(2.0)
SQRTPI = math.sqrt(math.pi)

def phi(x):
    return math.exp(-0.5*x*x)/math.sqrt(2.0*math.pi)

def Phi(x):
    return 0.5*(1.0 + math.erf(x/SQRT2))

def h(delta):
    return SQRT2*phi(delta/SQRT2) - delta*Phi(-delta/SQRT2)

def simpson(f, a, b, n=120000):
    if n % 2:
        n += 1
    step = (b-a)/n
    total = f(a)+f(b)
    for i in range(1,n):
        total += (4.0 if i % 2 else 2.0)*f(a+i*step)
    return total*step/3.0

def positive_part_numeric(delta):
    # Density of N(-delta,2), integrated over y>0.
    def density(y):
        return math.exp(-((y+delta)**2)/4.0)/(2.0*math.sqrt(math.pi))
    return simpson(lambda y: y*density(y), 0.0, 14.0, 100000)

for delta in (0.0, 0.2, 0.7, 1.5, 3.0):
    numeric = positive_part_numeric(delta)
    closed = h(delta)
    assert abs(numeric-closed) < 2e-11, (delta,numeric,closed)

for delta in (0.1, 0.7, 2.0):
    eps = 1e-6
    numerical_derivative = (h(delta+eps)-h(delta-eps))/(2.0*eps)
    exact_derivative = -Phi(-delta/SQRT2)
    assert abs(numerical_derivative-exact_derivative) < 2e-9

target = 1.0/(2.0*SQRTPI)
lo, hi = 0.0, 4.0
assert h(lo) > target and h(hi) < target
for _ in range(100):
    mid = (lo+hi)/2.0
    if h(mid) > target:
        lo = mid
    else:
        hi = mid
delta_star = (lo+hi)/2.0
assert abs(delta_star-0.6994548019050194) < 2e-15

def risk_diff_boundary(delta):
    return 1.0/math.pi - 2.0*h(delta)/SQRTPI

assert risk_diff_boundary(0.0) < 0.0
assert risk_diff_boundary(delta_star*0.999999) < 0.0
assert abs(risk_diff_boundary(delta_star)) < 5e-16
assert risk_diff_boundary(delta_star*1.000001) > 0.0
assert risk_diff_boundary(5.0) > 0.0

print(f"VERIFY_OK delta_star={delta_star:.12f} h0={h(0.0):.12f}")
