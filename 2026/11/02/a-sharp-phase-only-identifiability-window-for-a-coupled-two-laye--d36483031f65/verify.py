#!/usr/bin/env python3
"""Standalone checks for a two-layer harmonic climate-response phase-fold theorem.

Only Python's standard library is required. Exact-rational checks are separate
from floating-point examples; the accompanying proof covers all real parameters.
"""
from fractions import Fraction as Q
from math import atan, atan2, sqrt, pi, isclose
from random import Random

checks = 0

def check(flag, msg):
    global checks
    checks += 1
    if not flag:
        raise AssertionError(msg)

def inverse_response(lam, C, D, w, k):
    q = w * D
    den = k*k + q*q
    return lam + q*q*k/den, w*C + q*k*k/den

def phase(lam, C, D, w, k):
    x,y = inverse_response(lam,C,D,w,k)
    return atan2(y,x)

def fold(lam,C,D,w):
    return D*(sqrt(lam*lam + w*w*C*(C+D)) - lam)/(C+D)

def poly(lam,C,D,w,k):
    return (C+D)*k*k + 2*lam*D*k - w*w*C*D*D

def transfer_complex(lam,C,D,w,k):
    return 1/(lam + 1j*w*C + 1j*w*D*k/(k+1j*w*D))

r = Random(20261030)
for _ in range(19000):
    # Multiplicative rational sweeps avoid float cancellation in identities.
    lam, C, D, w, k = [Q(r.randint(1, 25),r.randint(1,25)) for i in range(5)]
    x,y = inverse_response(lam,C,D,w,k)
    q = w*D
    den = k*k+q*q
    # exact circle equation, positivity, exact transfer and derivative sign numerator
    check((x-lam)**2 +(y-w*(C+D/Q(2)))**2 == (q/Q(2))**2,'circle identity')
    check(x>lam and w*C<y<w*(C+D),'strict semicircle')
    check(x == lam+q*q*k/den and y == w*C+q*k*k/den,'inverse transfer')
    # exact derivative sign for positive branch: derivative of Y/X
    xp = q*q*(q*q-k*k)/(den*den)
    yp = 2*q*q*q*k/(den*den)
    numerator = yp*x-y*xp
    predicted = (w**3 * D**2)*poly(lam,C,D,w,k)/(den*den)
    check(numerator==predicted,'derivative factorization')
    check((numerator>0)==(poly(lam,C,D,w,k)>0),'derivative sign')
    # complex identity exact up to roundoff, checked on moderate ratios only
    xf,yf = float(x),float(y)
    hf=transfer_complex(float(lam),float(C),float(D),float(w),float(k))
    check(abs(1/hf-complex(xf,yf))<2e-9*max(1,abs(complex(xf,yf))),'complex transfer')

# Rational phase twins: both have tangent 8/11; complex amplitudes differ.
x1,y1 = inverse_response(Q(1),Q(1),Q(3),Q(1),Q(1,2))
x2,y2 = inverse_response(Q(1),Q(1),Q(3),Q(1),Q(3,2))
check((x1,y1)==(Q(55,37),Q(40,37)),'first phase twin')
check((x2,y2)==(Q(11,5),Q(8,5)),'second phase twin')
check(y1/x1==y2/x2==Q(8,11),'phase equality')
check(x1*x1+y1*y1==Q(125,37),'gain A exact')
check(x2*x2+y2*y2==Q(37,5),'gain B exact')
check(fold(1,1,3,1)>0.5 and fold(1,1,3,1)<1.5,'fold separates twins')

# Deterministic exact rational derivative classification on intervals.
for _ in range(18000):
    lam, C, D, w = [Q(r.randint(1,20),r.randint(1,20)) for i in range(4)]
    a,b = sorted([Q(r.randint(1,20),r.randint(1,20)) for i in range(2)])
    if a==b:continue
    # phase fold k* lies in interval iff polynomial changes sign strictly.
    interior=(poly(lam,C,D,w,a)<0<poly(lam,C,D,w,b))
    omega_low_sq=((C+D)*a*a+2*lam*D*a)/(C*D*D)
    omega_high_sq=((C+D)*b*b+2*lam*D*b)/(C*D*D)
    window=(omega_low_sq<w*w<omega_high_sq)
    check(interior==window,'exact design frequency window')
    check(poly(lam,C,D,w,b)>poly(lam,C,D,w,a),'strict monotonicity of derivative polynomial')

# Numeric climate-scale example: a pre-defined exchange interval, not data inference.
lam,C,D = 1.3,8.0,100.0
a,b = 0.5,1.2
lo = sqrt(((C+D)*a*a+2*lam*D*a)/(C*D*D))
hi = sqrt(((C+D)*b*b+2*lam*D*b)/(C*D*D))
check(lo < 2*pi/100 < hi,'century forcing lies inside aliasing window')
check(lo < hi and fold(lam,C,D,2*pi/100)>a and fold(lam,C,D,2*pi/100)<b,'climate fold in prior range')
print('VERIFY_OK assertions=%d' % checks)
print('phase twins tangent 8/11; k*=%.12f' % fold(1,1,3,1))
print('climate two-boundary period window: (%.7f, %.7f) years' % (2*pi/hi,2*pi/lo))
