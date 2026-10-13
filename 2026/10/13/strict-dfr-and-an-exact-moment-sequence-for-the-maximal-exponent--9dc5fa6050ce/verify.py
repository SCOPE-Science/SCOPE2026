#!/usr/bin/env python3
import math

def x_from_q(q):
    return -math.log(q)/(1.0-q)

def hazard_q(q):
    return (1.0-q)**2/(1.0-q+q*math.log(q))

def z_from_e(t):
    if t == 0.0:
        return 1.0
    return t/(-math.expm1(-t))

# Exact low moments from the claimed series.
mean = math.pi**2/6.0
second = math.pi**2/3.0
variance = second-mean**2

# Strict hazard decrease in x: q decreases as x increases, while h increases in q.
qs=[math.exp(-j/400.0) for j in range(1,6001)]
xs=[x_from_q(q) for q in qs]
hs=[hazard_q(q) for q in qs]
assert all(xs[i] < xs[i+1] for i in range(len(xs)-1))
assert all(hs[i] > hs[i+1] for i in range(len(hs)-1))

# Direct numerical derivative of the survival parametrization confirms h=f/S.
for q in (0.99,0.9,0.7,0.4,0.1,0.01):
    eps=min(1e-6, q/10, (1-q)/10)
    dx=(x_from_q(q+eps)-x_from_q(q-eps))/(2*eps)
    h_num=(-1.0/dx)/q
    assert abs(h_num-hazard_q(q)) < 2e-8

# Endpoint checks.
assert abs(hazard_q(0.999999)-2.0) < 2e-6
assert abs(hazard_q(1e-12)-1.0) < 1e-9

# Numerical integration of transformed exponential moments by midpoint rule.
def moment_integral(m, T=32.0, N=800000):
    h=T/N
    s=0.0
    for i in range(N):
        t=(i+0.5)*h
        z=z_from_e(t)
        s += (z**m)*math.exp(-t)
    return s*h

m1=moment_integral(1)
m2=moment_integral(2)
m3=moment_integral(3)
target3=3.0*(math.pi**2/6.0 + 1.2020569031595942854)
assert abs(m1-mean) < 3e-7
assert abs(m2-second) < 2e-6
assert abs(m3-target3) < 2e-5

# Partial-series replay of the general formula for m=1,2,3.
def moment_series(m,N=200000):
    s=0.0
    # recurrence for C(m+n-2,m-1)
    c=1.0
    for n in range(1,N+1):
        if n==1:
            c=1.0
        else:
            c *= (m+n-2)/(n-1)
        s += c/(n**(m+1))
    return math.factorial(m)*s
assert abs(moment_series(1)-mean) < 6e-6
assert abs(moment_series(2)-second) < 2e-5
assert abs(moment_series(3)-target3) < 7e-5

print(f"VERIFY_OK mean={mean:.15f} variance={variance:.15f} hazard_endpoints=(2,1)")
