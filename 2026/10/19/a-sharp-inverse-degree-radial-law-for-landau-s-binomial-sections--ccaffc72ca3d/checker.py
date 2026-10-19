#!/usr/bin/env python3
"""Finite arithmetic and high-precision checks for a binomial-section zero law.

Usage: python checker.py  (requires mpmath). Tests are finite and do not certify the asymptotic theorem.
"""
from fractions import Fraction
import mpmath as mp

for n in range(1, 151):
    a = [Fraction(1)]
    for k in range(1, n + 1):
        a.append(a[-1] * Fraction(2*k-1, 2*k))
    assert sum(a) == (2*n + 1)*a[-1]
    d = [a[k-1]-a[k] for k in range(1, n+1)]
    assert sum(k*d[k-1] for k in range(1,n+1)) == sum(a[:-1])/2
    # Identity (1-z) P_n=Q_n-a_n z^(n+1): exact coefficient equality.
    cp = [a[0]] + [a[k]-a[k-1] for k in range(1,n+1)] + [-a[n]]
    cq = [Fraction(1)] + [-v for v in d] + [-a[n]]
    assert cp == cq

mp.mp.dps = 50
H = lambda w: (2/mp.sqrt(mp.pi))*mp.hyp1f1(mp.mpf('0.5'), mp.mpf('1.5'), w)
Hp = lambda w: mp.diff(H, w)
guess = mp.mpc('1.43365931676195287935918','5.45705263632490130914145')
w0 = mp.findroot(H, (guess, guess + mp.mpc('0.002','0.002')))
assert abs(H(w0)) < mp.mpf('1e-40')
assert abs(H(w0)+2*w0*Hp(w0)-2*mp.exp(w0)/mp.sqrt(mp.pi)) < mp.mpf('1e-39')

for n in (20, 40, 80, 160, 320):
    a = [mp.mpf(1)]
    for k in range(1,n+1):
        a.append(a[-1]*(2*k-1)/(2*k))
    def poly_scaled(w):
        z=mp.exp(w/n)
        val=mp.mpc(0)
        for ak in reversed(a):
            val = val*z+ak
        return val
    wn=mp.findroot(poly_scaled,(w0,w0+mp.mpc('0.001','0.001')))
    assert abs(poly_scaled(wn))<mp.mpf('1e-36')
    assert abs(wn-w0)<mp.mpf(5)/n
    print('n=', n, 'scaled zero=', mp.nstr(wn, 24), 'n(radius-1)=',
          mp.nstr(n*(mp.exp(mp.re(wn)/n)-1), 20))
print('illustrative H zero:', mp.nstr(w0,40))
print('Finite checks passed; global minimality and infinite convergence rely on the proof.')
