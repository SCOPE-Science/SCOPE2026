#!/usr/bin/env python3
"""Exact identities and reproducible finite-sample checks for Gaussian Ritz-sketch risk."""
from fractions import Fraction
from math import sqrt
from random import Random

# Median CDF under the transformation u=x/sqrt(1+x*x):
# base CDF = (1+u)/2; median-of-three transformed density=3(1-u*u)/4.
def even_uniform_moment(k):
    return Fraction(2, 2*k+1)
assert Fraction(3, 4)*(even_uniform_moment(0)-even_uniform_moment(1)) == 1
assert Fraction(3, 4)*even_uniform_moment(1) == Fraction(1, 2)
assert 2 * (Fraction(3, 4)*even_uniform_moment(1)) == 1
# Shape-2 gamma inverse mean = Gamma(1)/Gamma(2)=1.
assert Fraction(1, 1) / Fraction(1, 1) == 1

rng = Random(4817)
def cn():
    return complex(rng.gauss(0, 1/sqrt(2)), rng.gauss(0, 1/sqrt(2)))

def median3(x):
    return sorted(x)[1]

def complex_median(zs):
    return complex(median3([z.real for z in zs]), median3([z.imag for z in zs]))

# Two-row unitary-column subspace, one-dimensional square sketch.
f = 1.2-0.4j
n = 130000
medrisk = 0.
overrisk = 0.
for _ in range(n):
    zs = [cn()/cn() for _ in range(3)]
    medrisk += abs(complex_median(zs)*f)**2
    g0,g1 = cn(),cn()
    h0,h1 = cn(),cn()
    z = (g0.conjugate()*h0+g1.conjugate()*h1)/(abs(g0)**2+abs(g1)**2)
    overrisk += abs(z*f)**2
medrisk /= n
overrisk /= n
target = abs(f)**2
assert abs(medrisk/target-1)<0.075, (medrisk,target)
assert abs(overrisk/target-1)<0.075, (overrisk,target)

# m=2 with n=3, residual F is 1-by-2; the same Gaussian H drives both columns.
f0,f1 = 0.8+0.5j,-0.4+0.9j
fsq = abs(f0)**2+abs(f1)**2
n = 100000
medrisk2 = 0.
overrisk2 = 0.
for _ in range(n):
    triples = [[],[],[],[]]
    for repeat in range(3):
        a,b,c,d = cn(),cn(),cn(),cn()
        h0,h1 = cn(),cn()
        det = a*d-b*c
        z0,z1 = (d*h0-b*h1)/det, (-c*h0+a*h1)/det
        for arr,z in zip(triples,(z0*f0,z0*f1,z1*f0,z1*f1)):
            arr.append(z)
    medrisk2 += sum(abs(complex_median(arr))**2 for arr in triples)

    # G: 3 by 2, H: 3 by 1. Closed-form normal-equation LS.
    a,c,e = cn(),cn(),cn()
    b,d,t = cn(),cn(),cn()
    h0,h1,h2=cn(),cn(),cn()
    aa=abs(a)**2+abs(c)**2+abs(e)**2
    bb=abs(b)**2+abs(d)**2+abs(t)**2
    ab=a.conjugate()*b+c.conjugate()*d+e.conjugate()*t
    u=a.conjugate()*h0+c.conjugate()*h1+e.conjugate()*h2
    v=b.conjugate()*h0+d.conjugate()*h1+t.conjugate()*h2
    det=aa*bb-abs(ab)**2
    z0=(bb*u-ab*v)/det
    z1=(aa*v-ab.conjugate()*u)/det
    overrisk2 += (abs(z0)**2+abs(z1)**2)*fsq
medrisk2 /= n
overrisk2 /= n
target2 = 2*fsq
assert abs(medrisk2/target2-1)<0.10, (medrisk2,target2)
assert abs(overrisk2/target2-1)<0.10, (overrisk2,target2)
print('PASS exact distribution moments; 460000 independent sketch trios/oversampling draws')
print('m=1 median3=%0.6f overplus1=%0.6f target=%0.6f'%(medrisk,overrisk,target))
print('m=2 median3=%0.6f overplus1=%0.6f target=%0.6f'%(medrisk2,overrisk2,target2))
