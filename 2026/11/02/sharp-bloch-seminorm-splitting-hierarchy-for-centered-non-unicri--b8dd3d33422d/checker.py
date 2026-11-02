#!/usr/bin/env python3
"""Independent arithmetic corroboration of explicit local Bloch-norm coefficients.

Run: python checker.py
Finite tests do not replace the all-degree and uniform-remainder proof.
"""
import math
import mpmath as mp

mp.mp.dps = 75
checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def coeff(n, k):
    n = mp.mpf(n)
    k = mp.mpf(k)
    r = mp.sqrt((n-1)/(n+1))
    return (1-r*r)*r**(n-1)*((n+k)*r**k-(n-k)*r**(-k))

def base(n):
    r = mp.sqrt(mp.mpf(n-1)/(n+1))
    return n*(1-r*r)*r**(n-1)

def radial_test(n, k, t):
    """B(z)=z^(n-k) (z^k-t)/(1-t*z^k), at z=r_n>0."""
    r = mp.sqrt(mp.mpf(n-1)/(n+1))
    s = r**k
    derivative = ((n-k)*r**(n-k-1)*(s-t)/(1-t*s)
                  + k*r**(n-1)*(1-t*t)/(1-t*s)**2)
    return (1-r*r)*derivative

# Every centered nonregular mode has strictly positive sharp coefficient.
for n in range(3, 26):
    for k in range(2, n):
        c = coeff(n, k)
        check(c > 0, f'positive coefficient n={n}, k={k}')
        # The real maximizing ray agrees with the predicted first variation.
        t = mp.mpf('0.0000001')
        slope = (radial_test(n, k, t) - base(n))/t
        check(abs(slope-c) < mp.mpf('0.000001'), f'first variation n={n}, k={k}')

# Fixed-k cubic decay: derived by Taylor expansion of artanh(1/n).
for k in (2, 3, 4, 6):
    target = mp.mpf(4)*k*(k*k-1)/(3*mp.e)
    for n in (1000, 4000):
        est = n**3*coeff(n, k)
        check(abs(est/target-1) < mp.mpf('0.000008'), f'cubic degree asymptotic n={n}, k={k}')

# Generic complex centered constellations, with nonzero e_2 and e_3.
def symmetric2(arr):
    return sum(arr[i]*arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))

def bpprime(z, eps, zeros):
    aa=[eps*a for a in zeros]
    numerator=mp.mpc(1)
    denominator=mp.mpc(1)
    numerator_der=mp.mpc(0)
    denominator_der=mp.mpc(0)
    for a in aa:
        next_num=numerator*(z-a)
        numerator_der=numerator_der*(z-a)+numerator
        numerator=next_num
        next_den=denominator*(1-mp.conj(a)*z)
        denominator_der=denominator_der*(1-mp.conj(a)*z)-mp.conj(a)*denominator
        denominator=next_den
    return (numerator_der*denominator-numerator*denominator_der)/denominator**2

examples = [
    [mp.mpc(1,2),mp.mpc(2,-1),mp.mpc(-3,-1)],
    [mp.mpc(1,1),mp.mpc(-1,-1),mp.mpc(0),mp.mpc(0)],
    [mp.mpc(1,0),mp.mpc(1,2),mp.mpc(-2,-2),mp.mpc(0),mp.mpc(0)],
]
for zeros in examples:
    n=len(zeros)
    check(abs(sum(zeros)) < mp.mpf('1e-50'), 'centered')
    e2=symmetric2(zeros)
    check(abs(e2)>0, 'first nonzero elementary symmetric index k=2')
    r=mp.sqrt(mp.mpf(n-1)/(n+1))
    # For k=2 the maximizing angle solves Re(e2*exp(-2i*theta))=-|e2|.
    theta=(mp.arg(e2)-mp.pi)/2
    z=r*mp.exp(1j*theta)
    c=coeff(n,2)*abs(e2)
    for eps in [mp.mpf('0.001'),mp.mpf('0.0004')]:
        val=(1-r*r)*abs(bpprime(z,eps,zeros))
        slope=(val-base(n))/eps**2
        check(abs(slope/c-1) < mp.mpf('0.025'), 'complex-angle directional response')

print(f'PASS: {checks} deterministic checks; all asymptotics remain analytically proved separately.')
