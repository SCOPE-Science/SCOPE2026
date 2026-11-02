"""Reproduce rational sign certificates and numerical spot checks for a gamma-product logarithmic gain."""
from fractions import Fraction as Q
from math import factorial
from scipy.integrate import quad
from scipy.stats import chi2
import mpmath as mp

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def ei_bounds(z):
    # 0<z<1. The standard Euler-constant enclosure is deliberately loose.
    check(Q(0) < z < Q(1), 'z domain')
    gamma_lo, gamma_hi = Q(5772156649, 10**10), Q(5772156650, 10**10)
    t = (z-Q(1))/(z+Q(1))
    partial_log = 2*sum((t**(2*j+1))/Q(2*j+1) for j in range(31))
    err_log = 2*abs(t)**63/(63*(1-t*t))
    partial_ei = sum(z**j/Q(j*factorial(j)) for j in range(1,17))
    err_ei = 3*z**17/Q(17*factorial(17))
    return gamma_lo+partial_log-err_log+partial_ei, gamma_hi+partial_log+err_log+partial_ei+err_ei

def expminus_bounds(z):
    terms = [(-z)**j/Q(factorial(j)) for j in range(21)]
    return sum(terms[:20]), sum(terms[:21])

z2=Q(40,107)  # 1/(107/40): two queries
z4=Q(80,107)  # 2/(107/40): four queries
e2lo,e2hi=ei_bounds(z2)
e4lo,e4hi=ei_bounds(z4)
check(e2lo>0,'two-probe contraction: Ei(40/107)>0')
l4,u4=expminus_bounds(z4)
check(l4>0 and u4>l4,'alternating exponential bounds')
conservative_F4_lo=1-(1+z4)*u4*e4hi
check(conservative_F4_lo>0,'four-probe growth: 1-(1+80/107)e^(-80/107)Ei(80/107)>0')
print('RATIONAL CERTIFICATE: Ei(40/107) >',float(e2lo))
print('RATIONAL CERTIFICATE: F_4(107/40) >',float(conservative_F4_lo))

mp.mp.dps=45
f2=lambda a: -mp.exp(-1/a)*mp.ei(1/a)
f4=lambda a: 1-(1+2/a)*mp.exp(-2/a)*mp.ei(2/a)
r2=mp.findroot(f2,(mp.mpf('2.65'),mp.mpf('2.71')))
r4=mp.findroot(f4,(mp.mpf('2.60'),mp.mpf('2.70')))
check(mp.mpf('2.6845') < r2 < mp.mpf('2.6846'),'two-probe root')
check(mp.mpf('2.6629') < r4 < mp.mpf('2.6631'),'four-probe root')
a0=mp.mpf(107)/40
check(f2(a0)<mp.mpf('-.0035') and f4(a0)>mp.mpf('.0064'),'certified-sign compatibility')
for n,f in [(2,f2),(4,f4)]:
    aa=float(a0)
    integrand=lambda y: chi2.pdf(n*y,n)*n*__import__('math').log(abs(1-aa*y))
    val=quad(integrand,0,1/aa,epsabs=1e-10)[0]+quad(integrand,1/aa, float('inf'),epsabs=1e-10)[0]
    check(abs(val-float(f(a0)))<5e-9,f'gamma integral at n={n}')
for n in (2,4,10,20,100):
    aa=2*n/(n+2)
    expectation=1-2*aa+aa**2*(1+2/n)
    check(abs(expectation-1)<1e-12,f'mean-square threshold n={n}')
for n in (2,4):
    # Multipliers at zero smoothing are exactly one minus a normalized chi-square.
    for zz in (0.5,1,2):
        directional=(1-a0*zz)
        check(abs(float(directional)-(1-float(a0)*zz))<1e-13,'quadratic identity')
print('ROOTS:',mp.nstr(r2,18),mp.nstr(r4,18))
print('TOTAL CHECKS:',checks)
