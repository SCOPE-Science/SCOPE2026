#!/usr/bin/env python3
"""Exact-rational log enclosures and conservative integer-mass convolutions.
Requires NumPy for fast exact uint64 convolution; rational bounds use the standard library. Run: python verify_unitary_density.py
"""
import numpy as np
from fractions import Fraction
from math import isqrt
from time import monotonic

P = 997
H = 100000
SCALE = 10**12
TAU = Fraction(11, 1000)
EXCEPTIONAL_CUTOFFS = {2:16, 3:12, 5:9, 7:7, 11:6, 13:5,
                       17:5, 19:5, 23:4, 29:4, 31:4,
                       37:4, 41:4, 43:4}
EXPECTED_LOWER_MASS = 772112456436
EXPECTED_UPPER_MASS = 784096956613

def primes_up_to(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]

def local_ratio(p, e):
    if e == 0:
        return Fraction(1)
    if e == 1:
        return Fraction(p+1,p)
    return Fraction(p**e+1, sum(p**d for d in range(1,e+1) if e % d == 0))

def log_enclosure(q):
    """Rational rigorous bounds on log(q) using 16 atanh terms."""
    if q == 1:
        return Fraction(0), Fraction(0)
    u = (q-1)/(q+1)
    term = u
    approx = Fraction(0)
    for k in range(16):
        approx += 2*term/(2*k+1)
        term *= u*u
    error = 2*abs(term)/(33*(1-u*u))
    return approx-error, approx+error

def shifts(p, cutoff, upper):
    out = []
    for exponent in range(cutoff):
        lo,hi = log_enclosure(local_ratio(p,exponent))
        if upper:
            q = hi*H
            t = -((-q.numerator)//q.denominator)
        else:
            q = lo*H
            t = q.numerator//q.denominator
        out.append(t)
    if upper:
        out.append(0) # tail exponents >= cutoff have log ratio <= 0
    return out

def convolution(upper):
    positions = np.array([SCALE], dtype=np.uint64)
    offset = 0
    primes = primes_up_to(P)
    for p in primes:
        cutoff = EXCEPTIONAL_CUTOFFS.get(p,3)
        positions_offsets = shifts(p, cutoff, upper)
        minimum = min(positions_offsets)
        maximum = max(positions_offsets)
        new = np.zeros(len(positions)+maximum-minimum, dtype=np.uint64)
        for e,shift in enumerate(positions_offsets):
            den = p**(e+1) if e<cutoff else p**cutoff
            multiplier = p-1 if e<cutoff else 1
            delta = shift-minimum
            if upper:
                added = (positions*multiplier+den-1)//den
            else:
                added = (positions*multiplier)//den
            new[delta:delta+len(positions)] += added
        positions = new
        offset += minimum
        # uint64 is exact: SCALE*max(p-1)<2^64, and all bin masses
        # are no larger than the sum, kept below 2*SCALE here.
        assert int(positions.sum(dtype=np.uint64)) < 2*SCALE
    if upper:
        first = max(0, 1-int(TAU*H)-offset)
    else:
        first = max(0, -offset)
    event = int(positions[first:].sum(dtype=np.uint64))
    return event, int(positions.sum(dtype=np.uint64)), len(positions), offset

def main():
    start = monotonic()
    low,total_low,n_low,off_low = convolution(False)
    print('lower_mass',low,'all_mass',total_low,'states',n_low,'offset',off_low, flush=True)
    high,total_high,n_high,off_high = convolution(True)
    print('upper_mass',high,'all_mass',total_high,'states',n_high,'offset',off_high, flush=True)
    assert low == EXPECTED_LOWER_MASS, (low,EXPECTED_LOWER_MASS)
    assert high == EXPECTED_UPPER_MASS, (high,EXPECTED_UPPER_MASS)
    # Probability of any squared prime >P is <=1/(2P).
    certified_low = Fraction(low, SCALE)*(1-Fraction(1,2*P))
    # Tail mean <=1/(2P), variance <=1/(4P^2).
    tail_chebyshev = Fraction(1,4*P*P)/(TAU-Fraction(1,2*P))**2
    certified_high = Fraction(high,SCALE)+tail_chebyshev
    assert certified_low > Fraction(7717,10000)
    assert certified_high < Fraction(7864,10000)
    print('CERTIFIED_INTERVAL', '>',Fraction(7717,10000), '<',Fraction(7864,10000))
    print('rational_lower',certified_low)
    print('rational_upper',certified_high)
    print('numerical_enclosure',float(certified_low),float(certified_high))
    print('elapsed_seconds',round(monotonic()-start,2),'VERIFY_OK')

if __name__=='__main__':
    main()
