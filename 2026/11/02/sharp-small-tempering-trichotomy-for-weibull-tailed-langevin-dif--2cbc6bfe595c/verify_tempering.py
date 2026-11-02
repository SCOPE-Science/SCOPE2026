#!/usr/bin/env python3
"""Reproduce exact quadrature identities and endpoint constants for tempered one-dimensional diffusions."""
import math
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 55
checks = 0

def check(cond, tag):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(tag)

def ideal(eta, ell):
    e = mp.mpf(str(eta)); l = mp.mpf(str(ell))
    p = mp.mpf(2)/e
    z = 1-2*l
    # Quadrature of the exact beta integral for potential V(x)=|x|^eta.
    return mp.gamma(p)/e*mp.quad(lambda w: (1-z*w**e)**(-p),[0, mp.mpf('0.5'),1])

def ideal_hyper(eta,ell):
    e=mp.mpf(str(eta)); l=mp.mpf(str(ell))
    return mp.gamma(2/e)/e*mp.hyp2f1(2/e,1/e,1+1/e,1-2*l)

def leading_below(eta,ell):
    e=mp.mpf(str(eta));l=mp.mpf(str(ell))
    return mp.gamma(2/e-1)/(e*e)*(2*l)**(1-2/e)

def leading_above(eta,ell):
    e=mp.mpf(str(eta));l=mp.mpf(str(ell))
    return mp.gamma(2/e)/(e*(e-2))*(2*l)**(1-2/e)

def ideal_zero(eta):
    e=mp.mpf(str(eta))
    return mp.gamma(2/e)*mp.beta(1/e,1-2/e)/(e**2)

print('Analytic check: beta integral equals hypergeometric formula')
for eta in [mp.mpf('1'),mp.mpf('1.5'),mp.mpf('2'),mp.mpf('2.5'),mp.mpf('3'),mp.mpf('4'),mp.mpf('6')]:
    for ell in ['0.5','0.3','0.2','0.05','0.01']:
        m1=ideal(eta,ell);m2=ideal_hyper(eta,ell)
        check(abs(m1-m2)<mp.mpf('1e-40')*max(1,abs(m2)),f'quadrature identity {eta} {ell}')
        check(m1>0,f'positivity {eta} {ell}')
        check(m1>=ideal(eta,mp.mpf('0.5'))-mp.mpf('1e-40'),f'decreasing {eta} {ell}')
print('Quadrature and monotonicity checks passed')

print('Exact Ornstein-Uhlenbeck formula')
for ell in ['0.5','0.45','0.3','0.2','0.1','0.05','0.01','0.001','0.0001']:
    a=1-2*mp.mpf(ell)
    rhs=mp.mpf('0.5') if a==0 else mp.atanh(mp.sqrt(a))/(2*mp.sqrt(a))
    lhs=ideal(2,ell)
    check(abs(lhs-rhs)<mp.mpf('1e-35'),f'Gaussian formula {ell}')
    if mp.mpf(ell)<mp.mpf('0.5'):
        check(lhs>mp.mpf('0.5'),f'Gaussian endpoint {ell}')
print('OU closed form checks passed')

print('Exact threshold and small-tempering asymptotic checks')
for eta in [mp.mpf('2.5'),mp.mpf('3'),mp.mpf('4'),mp.mpf('6')]:
    M0=ideal_zero(eta)
    for ell in ['0.1','0.01','0.001','0.0001']:
        M=ideal(eta,ell)
        check(M<M0,f'finite upper {eta} {ell}')
        check(M>0,f'finite lower {eta} {ell}')
    for ell in ['0.001','0.0001']:
        delta= M0-ideal(eta,ell)
        check(delta>0,f'positive difference {eta} {ell}')
        ratio=delta/leading_above(eta,ell)
        check(mp.mpf('0.3')<ratio<mp.mpf('1.7'),f'superquadratic asympt scale {eta} {ell}: {ratio}')

for eta in [mp.mpf('1'),mp.mpf('1.5')]:
    check(ideal(eta,'0.001')>ideal(eta,'0.01')>ideal(eta,'0.1'),f'power divergence {eta}')
    for ell in ['0.001','0.0001']:
        ratio=ideal(eta,ell)/leading_below(eta,ell)
        check(mp.mpf('0.6')<ratio<mp.mpf('1.4'),f'subquadratic asympt scale {eta} {ell}: {ratio}')

for eta in [mp.mpf('3'),mp.mpf('4'),mp.mpf('6')]:
    check(ideal(eta,'0.0001')<ideal_zero(eta),f'superquadratic finite endpoint {eta}')
    check(ideal(eta,'0.0001')>ideal(eta,'0.01'),f'superquadratic monotone endpoint {eta}')

check(abs(ideal(1,'0.1')-mp.mpf(5))<mp.mpf('1e-40'),'linear potential exact mean 0.1')
check(abs(ideal(1,'0.01')-mp.mpf(50))<mp.mpf('1e-35'),'linear potential exact mean 0.01')
for ell in ['0.01','0.001','0.0001']:
    ratio=ideal(2,ell)/(mp.log(1/mp.mpf(ell))/4)
    check(ratio>1 and ratio<mp.mpf('1.3'),f'logarithmic regime {ell}')

print('A sample of exact parameter values:')
for eta in [1,2,3,4]:
    print('eta',eta,'M(ell=0.05)',mp.nstr(ideal(eta,'0.05'),14), 'M(ell=0.005)',mp.nstr(ideal(eta,'0.005'),14))
print('All',checks,'checks PASSED')
