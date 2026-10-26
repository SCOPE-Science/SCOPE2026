"""Finite precision and symbolic spot checks for a zonal Gegenbauer transform.

The infinite-dimensional positivity theorem depends on the accompanying analytic proof,
not on finite sampling in this script.
"""
import math
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 48


def integral(m, n, a):
    return mp.quad(lambda t: mp.exp(-a*t)*mp.sin(t)**(2*m)*
                   mp.gegenbauer(n, m, mp.cos(t)), [0, mp.pi/2, mp.pi])


def closed(m, n, a):
    return (mp.factorial(2*m)*mp.binomial(n+2*m-1, 2*m-1)*a*
            (1-(-1)**n*mp.exp(-mp.pi*a))/
            mp.fprod(a*a+(n+2*j)**2 for j in range(m+1)))


max_error = mp.mpf(0)
count = 0
for m in range(1, 6):
    for n in range(0, 7):
        for a in (mp.mpf('0.3'), mp.mpf('1.25'), mp.mpf('3.5')):
            x, y = integral(m,n,a), closed(m,n,a)
            err = abs(x-y)
            max_error = max(max_error,err)
            if err > mp.mpf('1e-37'):
                raise ArithmeticError((m,n,str(a),str(err)))
            count += 1

# Fourier-frequency sparsity and moment cancellations, using exact Laurent polynomials.
z=sp.Symbol('z'); checks=0
for m in range(1,6):
    for n in range(0,7):
        p=sp.expand(sp.gegenbauer(n,m,(z+z**-1)/2)*(-1)**m*((z-z**-1)/2)**(2*m))
        coeff={int(e[0]):sp.cancel(c) for e,c in sp.Poly(sp.expand(p*z**(n+2*m)),z).terms()}
        coeff={k-(n+2*m):v for k,v in coeff.items()}
        assert all(abs(k)>=n and abs(k)<=n+2*m and (abs(k)-n)%2==0 for k in coeff)
        assert all(sp.simplify(coeff.get(k,0)-coeff.get(-k,0))==0 for k in coeff)
        for j in range(m):
            assert sp.simplify(sum(v*k**(2*j) for k,v in coeff.items())) == 0
        checks += 1

# Explicit interval, positivity of all checked coefficients, and sign witnesses.
def slopes(m,a,n):
    e=mp.exp(-mp.pi*a)
    return (1/a + ((-1)**n)*mp.pi*e/(1-((-1)**n)*e) -
            2*a*mp.fsum(1/(a*a+(n+2*j)**2) for j in range(m+1)))

def endpoints(m,a):
    e=mp.exp(-mp.pi*a)
    r0=slopes(m,a,0)
    rmax=1/a+mp.pi*e/(1-e)
    return 1/r0,1/rmax

sign_checks=0
for m in (1,2,3,5,10):
    for a in (mp.mpf('.15'),mp.mpf('1.0'),mp.mpf('5')):
        lo,hi=endpoints(m,a)
        assert lo < 0 < hi < a
        assert abs(1-lo*slopes(m,a,0)) < mp.mpf('1e-43')
        for n in range(1,51):
            assert 1-lo*slopes(m,a,n) > 0
            assert 1-hi*slopes(m,a,n) > 0
            sign_checks += 2
        assert 1-(lo-mp.mpf('.01'))*slopes(m,a,0) < 0
        assert 1-(hi+mp.mpf('.01'))*slopes(m,a,5000) < 0

for a in (mp.mpf('.2'), mp.mpf('1'), mp.mpf('4')):
    lo,_=endpoints(1000,a)
    assert abs(lo+2/mp.pi)<mp.mpf('0.001')

print('Numerical Gegenbauer integral comparisons:',count)
print('Maximum absolute error:',mp.nstr(max_error,8))
print('Exact Laurent support/moment checks:',checks)
print('Finite coefficient sign checks:',sign_checks)
for m in (1,2,3,10,100):
    lo,hi=endpoints(m,mp.mpf(1))
    print('a=1 dimension',2*m+1,'lower',mp.nstr(lo,14),'upper',mp.nstr(hi,14))
print('All finite verification checks passed.')
