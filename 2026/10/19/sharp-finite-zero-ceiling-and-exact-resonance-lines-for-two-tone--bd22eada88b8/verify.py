#!/usr/bin/env python3
"""Reproducibility checks for the two-tone Hermite-window zero theorem.

This checks finite-order instances and Fourier/STFT normalizations; the
all-order assertions follow from the analytic proof in RESULT.md.
Standard library only. Run: python3 verify.py
"""
import cmath
import math

PI = math.pi

def hermite_poly(n, x):
    if n == 0:
        return 1.0
    if n == 1:
        return 2.0 * x
    a, b = 1.0, 2.0 * x
    for k in range(2, n + 1):
        a, b = b, 2.0 * x * b - 2.0 * (k - 1) * a
    return b

def window(n, x):
    return (2.0 * PI)**(n / 2.0) * hermite_poly(n, math.sqrt(2.0 * PI) * x) * math.exp(-PI * x * x)

def form(n, gap, t, nu):
    d = gap / 2.0
    a = window(n, nu - d)
    b = window(n, nu + d)
    return ((-1j)**n * cmath.exp(-2j * PI * nu * t)
            * (cmath.exp(2j * PI * d * t) * a + cmath.exp(-2j * PI * d * t) * b))

def simpson_complex(f, lo, hi, N=6000):
    assert N % 2 == 0
    step = (hi-lo)/N
    total = f(lo)+f(hi)
    for k in range(1, N):
        total += (4 if k % 2 else 2)*f(lo+k*step)
    return total*step/3

checks=0
# Independent numerical evaluation of the defining integral.
for n in range(5):
    for gap in (0.8, 1.6):
        for t, nu in ((0.0, 0.0),(0.21, 0.34),(0.37,-0.25)):
            val = simpson_complex(lambda s:
                (cmath.exp(1j*PI*gap*s)+cmath.exp(-1j*PI*gap*s))
                *window(n,s-t)*cmath.exp(-2j*PI*nu*s), t-7, t+7)
            target=form(n,gap,t,nu)
            assert abs(val-target)<2e-8*(1+abs(target)), (n,gap,t,nu,val,target)
            checks+=1

# The n=2 window has exactly two roots at +/-1/(2 sqrt(pi)).
r2=1/(2*math.sqrt(PI))
assert abs(window(2,r2))<1e-10 and abs(window(2,-r2))<1e-10
# Gap 2*r2 creates a full horizontal zero line at frequency zero.
for k in range(17):
    assert abs(form(2,2*r2,k/(17*(2*r2)),0.0))<1e-8
    checks+=1
# The n=3 window has roots -r3, 0, r3. The gap r3 makes
# two entire frequency lines, centered at +/-r3/2.
r3=math.sqrt(3/(4*PI))
for root in (-r3,0,r3):
    assert abs(window(3,root))<1e-10
for nu in (-r3/2,r3/2):
    for k in range(17):
        assert abs(form(3,r3,k/(17*r3),nu))<1e-8
        checks+=1

# Check the sharp count 4n+1 for a fixed sufficiently large gap.
# Offset the frequency grid to avoid accidentally sampling an exact zero.
def zeros_sign_changes(n, gap, sign):
    d=gap/2
    L=d+3.0
    N=120000
    step=2*L/N
    def scalar(v):return window(n,v-d)+sign*window(n,v+d)
    last=scalar(-L+step/3)
    count=0
    for k in range(1,N):
        cur=scalar(-L+(k+1/3)*step)
        if cur*last<0:
            count+=1
        last=cur
    return count
for n in range(7):
    cS=zeros_sign_changes(n, 8.0, 1)
    cD=zeros_sign_changes(n, 8.0, -1)
    assert cS+cD==4*n+1, (n,cS,cD)
    assert (cS,cD)==((2*n,2*n+1) if n%2==0 else (2*n+1,2*n)), (n,cS,cD)
    checks+=2
print('VERIFY_OK', checks, 'integral, resonance, and sharp-count checks; n=0..6; gap=8')
