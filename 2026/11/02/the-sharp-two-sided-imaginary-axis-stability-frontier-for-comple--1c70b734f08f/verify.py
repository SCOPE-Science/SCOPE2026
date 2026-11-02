#!/usr/bin/env python3
"""Exact and floating-point checks for the two-sided degree-two imaginary-axis stability frontier.
Requires Python 3 and SymPy; no external input.
These are supplementary finite checks, not a substitute for the proof.
"""
from fractions import Fraction as F
from math import isclose
import cmath
import random
import sympy as s

R,S,a,b,y=s.symbols('R S a b y',real=True)
k=a+s.I*b
p=1+s.I*y-k*y**2
f=s.factor(s.expand_complex(p*s.conjugate(p))-1)
expect=s.expand(y*y*((a*a+b*b)*y*y-2*b*y+1-2*a))
assert s.simplify(f-expect)==0
print('Symbolic modulus identity: PASS')

# Disk center distance, squared, minus summed radii squared:
diff=s.factor(s.expand_complex(((1+s.I*R)/R**2-(1-s.I*S)/S**2)*s.conjugate((1+s.I*R)/R**2-(1-s.I*S)/S**2))-(1/R**2+1/S**2)**2)
assert s.simplify(diff-((R+S)**2-4)/(R**2*S**2))==0
print('Disk-tangency identity: PASS')

eta=s.symbols('eta',real=True)
ks=(1+s.I*eta)/(1+eta**2)
pexp=1+s.I*y-ks*y*y
identity=s.factor(s.expand_complex(pexp*s.conjugate(pexp))-1)
assert s.simplify(identity-y**2*(y-(1+eta))*(y+(1-eta))/(1+eta**2))==0
print('Sharp factorization: PASS')

# Independently verify exact rational parameter cases with exhaustive finite grids.
rng=random.Random(20261028)
count=0
for i in range(1,60):
    omega_plus=F(rng.randrange(1,100),rng.randrange(1,80))
    omega_minus=F(rng.randrange(1,100),rng.randrange(1,80))
    h=F(2)/(omega_plus+omega_minus)
    eta=(omega_plus-omega_minus)/(omega_plus+omega_minus)
    aa=F(1)/(1+eta*eta)
    bb=eta*aa
    rr=h*omega_plus
    ss=h*omega_minus
    assert rr+ss==2 and aa*aa+bb*bb==aa
    for j in range(101):
        t=-ss+(rr+ss)*F(j,100)
        # |1+it+(a+ib)(it)^2|^2 - 1
        poly=t*t*((aa*aa+bb*bb)*t*t-2*bb*t+1-2*aa)
        assert poly<=0, (i,j,t,poly)
        if j not in (0,100,50):
            assert poly<0, (i,j,t,poly)
        count+=1
print('Exact rational spectrum point tests: PASS',count)

# Asymmetry speedup and endpoint perturbations: direct double-precision tests.
more=0
for i in range(1,100):
    wplus=rng.uniform(.1,10)
    wminus=rng.uniform(.1,10)
    h=2/(wplus+wminus)
    e=(wplus-wminus)/(wplus+wminus)
    coeff=(1+1j*e)/(1+e*e)
    for omega in (-wminus,wplus):
        z=1j*h*omega
        assert abs(abs(1+z+coeff*z*z)-1)<2e-12
        zbad=1j*(h*1.05)*omega
        assert abs(1+zbad+coeff*zbad*zbad)>1+1e-12
        more+=1
    best_real=1/max(wplus,wminus)
    assert h>=best_real-1e-12
    assert h<=2*best_real+1e-12
print('Endpoint sharpness and real-method speedup: PASS',more)
print('VERIFY_OK')
