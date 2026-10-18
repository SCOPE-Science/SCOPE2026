#!/usr/bin/env python3
"""Finite diagnostics for a geometric atomic Helson Gram and its theta band.
Run: python check.py. Requires mpmath; prints verified diagnostic count.
"""
import mpmath as mp
mp.mp.dps=70
checks=0

def close(a,b,tol):
    global checks
    assert abs(a-b) <= tol, (a,b,abs(a-b))
    checks+=1

for base in [mp.mpf('1.5'),mp.mpf('2'),mp.mpf('3')]:
    for delta in [mp.mpf('0.3'),mp.mpf('1'),mp.mpf('2')]:
        for j,k in [(1,1),(1,2),(2,5),(5,10),(8,3)]:
            w=2*delta*base**(-(j+k)/2)
            t=delta*(base**(-j)+base**(-k))
            g=w*mp.zeta(1+t)
            t0=1/mp.cosh((j-k)*mp.log(base)/2)
            err=w*(mp.zeta(1+t)-1/t)
            close(g,t0+err,mp.mpf('1e-60'))
    eta=base**(-mp.mpf('0.5'))
    th3=mp.jtheta(3,0,eta)**2
    th4=mp.jtheta(4,0,eta)**2
    # Absolute Fourier remainder is < ~2*eta**N/(1-eta).
    N=int(mp.ceil(1600/mp.log(base)))
    coeff=lambda n: 1/mp.cosh(n*mp.log(base)/2)
    f0=mp.mpf('1')+2*sum(coeff(n) for n in range(1,N+1))
    fpi=mp.mpf('1')+2*sum((-1)**n*coeff(n) for n in range(1,N+1))
    close(f0,th3,mp.mpf('1e-60'))
    close(fpi,th4,mp.mpf('1e-60'))
    assert 0<th4<th3
    checks+=1
    for theta in [mp.pi*j/9 for j in range(10)]:
        ft=mp.mpf('1')+2*sum(coeff(n)*mp.cos(n*theta) for n in range(1,N+1))
        assert th4-mp.mpf('1e-50') <= ft <= th3+mp.mpf('1e-50')
        checks+=1
print('PASS',checks,'finite diagnostics')
