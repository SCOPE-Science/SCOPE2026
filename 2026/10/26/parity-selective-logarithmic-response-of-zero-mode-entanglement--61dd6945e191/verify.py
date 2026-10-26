"""Numerical quadrature checks for weak-link zero-mode entropy (not a proof).
Requires Python 3 and mpmath; run `python verify.py`.
The mathematical proof is the uniform integral asymptotic in RESULT.md.
"""
import mpmath as mp
mp.mp.dps = 45

def entropy(e):
    return mp.log1p(mp.exp(-e)) + e / (1 + mp.exp(e))

def entropy_shifts(lam):
    a = mp.sqrt(1 - lam*lam)
    edge = 2 * mp.acosh(1 / lam)
    def weight(y, even):
        v = mp.cosh(y)
        u = mp.sinh(y)
        return ((1-a if even else 1+a) * (u*u-a if even else u*u+a)
                / (2*mp.pi*v*(v*v-lam*lam)))
    def integral(even):
        def f(y):
            e = 2*mp.acosh(mp.cosh(y)/lam)
            return weight(y,even)*entropy(e)
        return 2*mp.quad(f,[0,1,4,15,50])
    even = mp.log(2) - entropy(edge)/2 + integral(True)
    odd = -entropy(edge)/2 + integral(False)
    return even,odd

for literal in ('0.1','0.05','0.02','0.01'):
    lam=mp.mpf(literal)
    even,odd=entropy_shifts(lam)
    even_asymptotic=mp.log(2)-lam**2/8*(1+2*mp.log(2/lam))
    odd_asymptotic=lam**2/4*(mp.log(2)-mp.mpf('0.5'))
    print(literal, 'even residual',mp.nstr(even-even_asymptotic,15),
          'odd residual',mp.nstr(odd-odd_asymptotic,15))
