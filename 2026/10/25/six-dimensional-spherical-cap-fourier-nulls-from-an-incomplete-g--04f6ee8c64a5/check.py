#!/usr/bin/env python3
"""Rational sign bounds and finite numerical illustrations."""
from fractions import Fraction as Q
from math import factorial
from hashlib import sha256
s=Q(7,2)
Klo,Khi=Q(53,250),Q(107,500)

def uv_bounds(c, parity, N=6):
    def term(j):
        e=2*j+parity
        return c**e/Q(factorial(e))/(s+e)
    S=sum(((-1)**j)*term(j) for j in range(N+1))
    e=(-1)**(N+1)*term(N+1)
    return (min(S,S+e),max(S,S+e))

def H_bounds(c,sqrtlo,sqrthi):
    Ulo,Uhi=uv_bounds(c,0); Vlo,Vhi=uv_bounds(c,1)
    powlo,powhi=c**3*sqrtlo,c**3*sqrthi
    L=Klo*powlo*(Ulo**2+Vlo**2)-Uhi+Vlo
    R=Khi*powhi*(Uhi**2+Vhi**2)-Ulo+Vhi
    return L,R

for c,l,r in [(Q(9,10),Q(948,1000),Q(949,1000)),(Q(1),Q(1),Q(1))]:
    L,R=H_bounds(c,l,r)
    print('H SIGN',str(c),'enclosure',[float(L),float(R)],'OK',R<0 if c<Q(1) else L>0)
    assert (R<0 if c<Q(1) else L>0)
# H' = -(U'-V') + K[(7/2)c^(5/2)(U²+V²)+2c^(7/2)(UU'+VV')].
# On [9/10,1], alternating-series derivative estimates give:
positive=Q(9,10)/Q(11,2)-Q(1)/(Q(6)*Q(15,2))+Q(2,9)-Q(1)/Q(13)
error=Khi*(s*((Q(2,7))**2+(Q(2,9))**2)+2*(Q(2,7)*Q(2,11)+Q(2,9)*Q(2,9)))
print('H DERIVATIVE lower',float(positive-error),'OK',positive>error)
assert positive>error

import mpmath as mp
mp.mp.dps=52
S=mp.mpf(7)/2;G=mp.gamma(S)
f=lambda c: abs(mp.gammainc(S,1j*c))**2/G**2-1
c0=mp.findroot(f,(mp.mpf('0.96'),mp.mpf('0.97')))
a=mp.exp(-1j*mp.pi*S/2)*mp.gammainc(S,1j*c0)
b=mp.exp(1j*mp.pi*S/2)*G
theta=(mp.arg(-b/a)/2)%mp.pi
assert mp.mpf('0.9')<c0<1
assert abs(f(c0))<mp.mpf('1e-45')
print('LIMIT ROOT c0',mp.nstr(c0,35),'theta',mp.nstr(theta,35))
# Verify the sliced Fourier integral at three finite frequencies.
for n in (10,20,40):
    def z(c,t):
        h=-1+c/t
        return mp.quad(lambda x:(1-x*x)**mp.mpf('2.5')*mp.exp(-1j*t*x),[h,-mp.mpf('.6'),0,mp.mpf('.6'),1])
    def pair(c,t):
        Z=z(c,t)*t**S/2**mp.mpf('2.5')
        return mp.re(Z),mp.im(Z)
    c,t=mp.findroot(pair,(c0,mp.pi*n+theta),solver='mdnewton',maxsteps=30, tol=mp.mpf('1e-39'))
    residue=abs(z(c,t))
    assert residue<mp.mpf('1e-35')
    print('FINITE WITNESS',n,'c',mp.nstr(c,21),'t-pi*n',mp.nstr(t-mp.pi*n,21),'h+1',mp.nstr(c/t,21),'residual',mp.nstr(residue,9))
print('CHECKS PASSED')
