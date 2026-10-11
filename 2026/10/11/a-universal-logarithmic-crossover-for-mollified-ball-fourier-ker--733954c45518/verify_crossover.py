#!/usr/bin/env python3
"""Supplementary Bessel-normalization and coefficient checks; not a proof of limits."""
import mpmath as mp

mp.mp.dps = 70

def critical_coefficient(d):
    p = mp.mpf(2*d) / (d+1)
    area = 2*mp.pi**(mp.mpf(d)/2)/mp.gamma(mp.mpf(d)/2)
    amplitude = (2*mp.pi)**(-mp.mpf(d)/2)*mp.sqrt(2/mp.pi)
    mean = mp.gamma((p+1)/2)/(mp.sqrt(mp.pi)*mp.gamma((p+2)/2))
    return area*amplitude**p*mean

c2 = critical_coefficient(2)
prior_c2 = 2**(mp.mpf(1)/3)*mp.beta(mp.mpf(1)/2,mp.mpf(7)/6)/mp.pi**2
assert abs(c2-prior_c2) < mp.mpf('1e-65')
assert abs(c2-mp.mpf('0.23252513092951185')) < mp.mpf('1e-15')
c3 = critical_coefficient(3)
assert abs(c3-mp.mpf('0.07972900439561123')) < mp.mpf('1e-15')

def profile(d, lam):
    a=mp.mpf(d+1)/2
    if not lam: return mp.mpf(1)
    z = a*mp.mpf(lam)
    return mp.expm1(z)/z

for d in (2,3,5):
    for lam in (-2,-mp.mpf('.25'),0,mp.mpf('.25'),2):
        assert abs(profile(d,lam)-mp.quad(lambda t: mp.exp((d+1)*lam*t/2), [0,1])) < mp.mpf('1e-60')

# Exact radial 3D box-profile formula versus independently integrated ball kernels.
def three_dimensional_box_kernel(r,delta):
    low=1-delta/2
    high=1+delta/2
    G=lambda z: -z*mp.sin(z)-2*mp.cos(z)
    return (G(r*high)-G(r*low))/(2*mp.pi**2*r**4*delta)

def three_dimensional_quad_kernel(r,delta):
    low=1-delta/2
    high=1+delta/2
    return mp.quad(lambda R:(mp.sin(r*R)-r*R*mp.cos(r*R))/(2*mp.pi**2*r**3*delta),[low,high])

for r in (mp.mpf('0.4'),mp.mpf('3'),mp.mpf('12')):
    for delta in (mp.mpf('0.05'),mp.mpf('0.2')):
        assert abs(three_dimensional_box_kernel(r,delta)-three_dimensional_quad_kernel(r,delta)) < mp.mpf('1e-60')

print('PASS: critical constants d=2,3; d=2 published constant equality; profile integral; exact 3D box-kernel identity.')
print('C_2 =',mp.nstr(c2,30))
print('C_3 =',mp.nstr(c3,30))
print('The theorem is proved analytically in RESULT.md; checks do not prove a joint limit.')
