#!/usr/bin/env python3
"""Independent numerical checks for two-tone weighted Bergman radial moments.

Exact all-degree and essential-spectrum assertions are proved analytically
in RESULT.md; finite computations here check normalization and asymptotics.
"""
import mpmath as mp

mp.mp.dps = 60
cases = [(mp.mpf('0'),mp.mpf('1'),0),
         (mp.mpf('0'),mp.sqrt(2),4),
         (mp.mpf('1.5'),mp.mpf('0.73'),8),
         (mp.mpf('-0.25'),mp.mpf('1.2'),3),
         (mp.mpf('2.25'),mp.mpf('2.7'),15)]

def moment(alpha,beta,n):
    return mp.beta(n+1,alpha+1+1j*beta)/mp.beta(n+1,alpha+1)

def moment_gamma(alpha,beta,n):
    return (mp.gamma(alpha+1+1j*beta)*mp.gamma(n+alpha+2)
            /(mp.gamma(alpha+1)*mp.gamma(n+alpha+2+1j*beta)))

for alpha,beta,n in cases:
    num=mp.quad(lambda t:t**n*(1-t)**alpha*mp.exp(1j*beta*mp.log(1-t)),[0,mp.mpf('.5'),mp.mpf('.9'),1])
    den=mp.quad(lambda t:t**n*(1-t)**alpha,[0,mp.mpf('.5'),mp.mpf('.9'),1])
    assert abs(num/den-moment_gamma(alpha,beta,n))<mp.mpf('2e-29')
    assert abs(moment(alpha,beta,n)-moment_gamma(alpha,beta,n))<mp.mpf('1e-50')

for alpha,beta in [(mp.mpf('0'),mp.mpf('1')),
                   (mp.mpf('1.5'),mp.sqrt(2)),
                   (mp.mpf('-.25'),mp.mpf('2.7'))]:
    C=mp.gamma(alpha+1+1j*beta)/mp.gamma(alpha+1)
    # Leading-order gamma-ratio approximation, with inverse-degree error.
    for n in (10000,100000,1000000):
        err=abs(moment_gamma(alpha,beta,n)-C*mp.exp(-1j*beta*mp.log(n)))
        assert err < 40/n

# Algebraic geometry of a sum of two complex phases: all radii in [|a-b|,a+b].
for a,b in [(mp.mpf('0.2'),mp.mpf('0.4')),
            (mp.mpf('1'),mp.mpf('1')),
            (mp.mpf('0.37'),mp.mpf('0.94'))]:
    for k in range(41):
        rad=abs(a-b)+(a+b-abs(a-b))*k/40
        cos_theta=(rad**2-a*a-b*b)/(2*a*b)
        assert -1-mp.mpf('1e-40') <= cos_theta <= 1+mp.mpf('1e-40')
        val=a+b*mp.exp(1j*mp.acos(max(-1,min(1,cos_theta))))
        assert abs(abs(val)-rad)<mp.mpf('1e-45')

# Exact rational-frequency phase orbit is a one-dimensional periodic image.
for p,q in [(1,2),(2,3),(3,5)]:
    for j in range(31):
        theta=2*mp.pi*j/30
        u=mp.exp(-1j*p*theta)+2*mp.exp(-1j*q*theta)
        assert abs(u-(mp.exp(-1j*p*(theta+2*mp.pi))+
                      2*mp.exp(-1j*q*(theta+2*mp.pi))))<mp.mpf('1e-49')

print('VERIFY_OK: 5 independent quadratures, 5 beta/gamma identities, '
      '9 asymptotic tests, 123 annulus-radius tests, 93 periodicity tests')
