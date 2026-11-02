#!/usr/bin/env python3
"""Exact Laurent-coefficient checks and numerical cross-checks for a four-tap sixth moment."""
from collections import defaultdict
from fractions import Fraction
import cmath
import itertools
import math

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def convolve(a, b):
    c = [0j] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            c[j + k] += x * y
    return c


def moment(a, order=3):
    v = [1.0 + 0j]
    for _ in range(order):
        v = convolve(v, a)
    return sum(abs(x)**2 for x in v)

# Exact expansion: each of the 10 coefficients of (1+uz+vz^2+z^3)^3
# is a polynomial in u and v with nonnegative integer coefficients.
C = {(0, 0, 0): 1}
monomials = ((0, 0), (1, 0), (0, 1), (0, 0))
for _ in range(3):
    D = defaultdict(int)
    for (power, a, b), weight in C.items():
        for j, (da, db) in enumerate(monomials):
            D[(power+j, a+da, b+db)] += weight
    C = dict(D)
T = defaultdict(int)
for (power, a, b), weight in C.items():
    for (power2, aa, bb), weight2 in C.items():
        if power == power2:
            T[(a-aa, b-bb)] += weight * weight2

expected = {(0,0):256, (3,0):3, (-3,0):3,
            (0,3):3, (0,-3):3,
            (1,-2):42, (-1,2):42,
            (2,-1):42, (-2,1):42,
            (1,1):72, (-1,-1):72}
check(dict(T) == expected, 'exact Fourier-Laurent coefficients')
check(len(C) > 10 and len(T)==11, 'full coefficient enumeration')

xstar = 2 - math.sqrt(111)/6
min_exact = 616 - (148/3)*math.sqrt(111)
check(0 < xstar < 1, 'critical parameter inside interval')
check(abs((12*xstar*xstar-48*xstar+11)) < 1e-12, 'derivative zero')
check(abs(112+288*xstar*xstar-48*xstar**3-132*xstar-min_exact) < 1e-11, 'closed-form minimum')
check((576-288*xstar)>0, 'strict second derivative')
check(112>min_exact and 220>min_exact, 'both endpoints above minimum')

for i in range(13):
    for j in range(17):
        alpha = 2*math.pi*i/13
        beta = 2*math.pi*j/17
        u,v=cmath.exp(1j*alpha),cmath.exp(1j*beta)
        calc = moment((1,u,v,1))
        trig = (256+6*(math.cos(3*alpha)+math.cos(3*beta))
                +84*(math.cos(alpha-2*beta)+math.cos(2*alpha-beta))
                +144*math.cos(alpha+beta))
        half=(alpha+beta)/2
        d=(alpha-beta)/2
        reduced=112+288*math.cos(half)**2+(48*math.cos(half)**3+132*math.cos(half))*math.cos(3*d)
        check(abs(calc-trig)<1e-8, 'direct moment vs Laurent formula')
        check(abs(trig-reduced)<1e-8, 'trigonometric change of variables')
        check(calc>=min_exact-1e-8, 'global inequality on sample grid')

theta=math.acos(xstar)
for sign in (-1,1):
    w=-cmath.exp(1j*sign*theta)
    m=moment((1,w,w,1))
    check(abs(m-min_exact)<1e-9, 'complex minimizer')
    for k in range(3):
        z=cmath.exp(2j*math.pi*k/3)
        check(abs(moment((1,w*z,w*z*z,1))-min_exact)<1e-8, 'cube-root orbit')

binary=[]
for choices in itertools.product((-1,1),repeat=3):
    binary.append(round(moment((1,*choices))))
check(sorted(set(binary))==[112,220,580], 'all binary moments')
check(min(binary)==112 and binary.count(112)==4, 'binary optimum and count')

# The fourth-moment optimizer is different: its half-sum cosine is 1/4.
check(abs((0.25-xstar))>1e-4, 'fourth and sixth optimizer parameters differ')
check(abs(112+288*(.25**2)-48*(.25**3)-132*.25-96.25)<1e-12,
      'sixth moment at fourth-moment minimum')
check(min_exact<96.25, 'strict sixth-moment tradeoff')

# Primitive integer polynomial for twice the critical half-sum cosine.
check(abs(3*(2*xstar)**2-24*(2*xstar)+11)<1e-10, 'algebraic equation for 2cos(theta)')
check(int(math.isqrt(444))**2!=444, 'quadratic irreducibility discriminant')

print('PASS', checks, 'checks')
print('sixth-moment minimum:', format(min_exact,'.13f'))
print('critical cosine:', format(xstar,'.13f'))
print('binary minimum:', min(binary))
