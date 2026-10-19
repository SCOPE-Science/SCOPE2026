"""Reproduce exact Laguerre extreme-value reversal and check Wigner normalization.
Run: python artifacts/check.py. Requires sympy, scipy, numpy, mpmath.
"""
from fractions import Fraction
import math
import sympy as sp
import numpy as np
from scipy.special import roots_genlaguerre,eval_laguerre,eval_hermite
import mpmath as mp

x=sp.symbols('x')

def enclosure_at_root(n, index):
    """Rational interval enclosing -L_n at index-th positive critical point (1-based)."""
    p=sp.Poly(sp.factorial(n)*sp.laguerre(n,x),x)
    boxes=sp.polys.polytools.intervals(p.diff(),eps=sp.Rational(1,10**11))
    assert len(boxes)==n-1 and all(mult==1 for box,mult in boxes)
    (lo,hi),_ = boxes[index-1]
    assert lo>0
    # Polynomial interval Horner with rigorous exact rational arithmetic.
    lower=upper=p.all_coeffs()[0]
    for coefficient in p.all_coeffs()[1:]:
        choices=(lower*lo,lower*hi,upper*lo,upper*hi)
        lower=min(choices)+coefficient
        upper=max(choices)+coefficient
    factorial=sp.factorial(n)
    return (lo,hi),(-upper/factorial,-lower/factorial)

def compare(n):
    box1, h1=enclosure_at_root(n,1)
    box3, h3=enclosure_at_root(n,3)
    if n<24:
        assert h3[0]>h1[1], ('outer shall exceed inner',n)
    else:
        assert h1[0]>h3[1], ('inner shall exceed outer',n)
    return {"n":n,"x1":[str(q) for q in box1],"x3":[str(q) for q in box3],
            "m1":[str(q) for q in h1],"m2":[str(q) for q in h3],
            "m1_approx":[float(q) for q in h1],"m2_approx":[float(q) for q in h3]}

for n in range(4,25,2):
    proof=compare(n)
    print('EXACT_RATIONAL_CERTIFICATE',n,'m1=',proof['m1_approx'],'m2=',proof['m2_approx'])

# Independent numerical checks of the all-order ordering law. This is not the proof.
for n in range(1,65):
    z=roots_genlaguerre(n-1,1)[0] if n>1 else np.array([])
    v=eval_laguerre(n,z)
    if n%2==0:
        minima=[float(-v[j]) for j in range(0,n-1,2)]
    else:
        minima=[1.0]+[float(v[j]) for j in range(1,n-1,2)]
    assert min(minima)>0
    # Weak unimodality: any descent after an ascent would violate the law.
    slopes=np.diff(minima)
    phase='decrease'
    for slope in slopes:
        if phase=='decrease' and slope>1e-7:
            phase='increase'
        if phase=='increase':
            assert slope>=-1e-7,(n,minima)
    if len(minima)>1:
        first=1.0/(1.0+minima[0]); second=1.0/(1.0+minima[1])
        assert 0<first<1 and 0<second<1
print('NUMERIC_ORDER_CHECK n=1..64 PASS')

# Direct defining-integral Wigner tests of the classical Fock formula.
mp.mp.dps=30
for n in range(4):
    for q,p in [(mp.mpf('0.3'),mp.mpf('0.4')),(mp.mpf('0.9'),mp.mpf('-0.25'))]:
        def hermite_wave(t):
            return mp.hermite(n,t)*mp.e**(-t*t/2)/(mp.pi**mp.mpf('0.25')*mp.sqrt(2**n*mp.factorial(n)))
        val=mp.quad(lambda y: hermite_wave(q+y/2)*hermite_wave(q-y/2)*mp.e**(-1j*p*y), [-mp.inf,mp.inf])/(2*mp.pi)
        pred=(-1)**n*mp.e**(-(q*q+p*p))/mp.pi*mp.laguerre(n,0,2*(q*q+p*p))
        assert abs(val-pred)<mp.mpf('1e-24'),(n,q,p,val,pred)
print('WIGNER_INTEGRALS n=0..3 two-points-each PASS')
