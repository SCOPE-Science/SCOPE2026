"""Independent checks for two-degree hemispherical spherical-harmonic concentration.

The exact rational tests check the endpoint identities and the angular-order
comparison. Gaussian quadrature checks the normalized hemisphere integrals.
Finite tests corroborate, but do not replace, the proof for all degrees.
"""
from fractions import Fraction
from math import factorial, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gammaln, lpmv


def df(n):
    if n in (-1, 0):
        return 1
    assert n > 0
    a = 1
    while n > 1:
        a *= n
        n -= 2
    return a


def norm_square(j, m):
    return Fraction((2*j+1)*factorial(j-m), 2*factorial(j+m))


def end_square(j, m):
    assert (j+m) % 2 == 0
    return norm_square(j, m) * Fraction(df(j+m-1)**2, df(j-m)**2)


def deriv_square(j, m):
    assert (j+m) % 2 == 1
    return norm_square(j, m) * Fraction(df(j+m)**2, df(j-m-1)**2)


def overlap_square(l, d, m):
    k=l+d
    assert d % 2 == 1 and 0<=m<=l
    delta=k*(k+1)-l*(l+1)
    if (l+m)%2 == 0:
        return end_square(l,m)*deriv_square(k,m) / delta**2
    return deriv_square(l,m)*end_square(k,m) / delta**2


def top_closed_square(l,d):
    k=l+d
    delta=d*(l+k+1)
    c=Fraction((2*l+1)*(2*k+1),4) * Fraction(factorial(d),factorial(2*l)*factorial(2*l+d))
    c*=Fraction(df(2*l-1)**2*df(2*l+d)**2,df(d-1)**2)
    return c / delta**2

assertions=0
for l in range(0,27):
    for d in range(3,30,2):
        k=l+d
        vals=[overlap_square(l,d,m) for m in range(l+1)]
        assert vals[l] == top_closed_square(l,d); assertions+=1
        for m in range(l):
            r2=Fraction(k*(k+1)-m*(m+1), l*(l+1)-m*(m+1))
            expected=r2 if (l+m)%2 else 1/r2
            assert vals[m+1] == vals[m]*expected; assertions+=1
        assert all(vals[l] > v for v in vals[:l]);assertions+=1
        if l>=2:
            assert all(vals[l-2] > v for v in vals[:l-2]+vals[l-1:l]);assertions+=1
            r1=Fraction(k*(k+1)-(l-2)*(l-1),l*(l+1)-(l-2)*(l-1))
            r2=Fraction(k*(k+1)-(l-1)*l,l*(l+1)-(l-1)*l)
            assert vals[l-2]/vals[l] == r1/r2; assertions+=1

# Exact one-peak law as the lower degree varies at fixed odd gap.
for d in range(3,42,2):
    for l in range(0,2*d+15):
        actual=top_closed_square(l+1,d)/top_closed_square(l,d)
        formula=Fraction((2*l+3)*(2*l+2*d+3)*(2*l+d+2)*(2*l+d+1),
                         (2*l+2*d+1)*(2*l+2)*(2*l+d+3)**2)
        q=2*d*d+2*d*l+d-4*l*l-12*l-9
        assert actual == formula; assertions+=1
        assert (actual > 1 if l<d-1 else actual < 1);assertions+=1
        assert (q>0 if l<d-1 else q<0);assertions+=1

xx,ww=leggauss(240)
xx=(xx+1)/2
ww=ww/2
quadratures=0
max_err=0.
for l in range(0,20):
    for d in (3,5,7,9,11,15):
        k=l+d
        sign=(-1)**((d-1)//2)
        for m in range(l+1):
            a=lpmv(m,l,xx) * np.sqrt((2*l+1)*np.exp(gammaln(l-m+1)-gammaln(l+m+1))/2)
            b=lpmv(m,k,xx) * np.sqrt((2*k+1)*np.exp(gammaln(k-m+1)-gammaln(k+m+1))/2)
            numeric=np.dot(ww,a*b)
            expected=sign*sqrt(overlap_square(l,d,m))
            err=abs(numeric-expected)
            assert err<2e-11, (l,d,m,numeric,expected,err)
            quadratures+=1
            max_err=max(max_err,err)
print(f'VERIFY_OK exact_assertions={assertions} quadrature_integrals={quadratures} max_abs_error={max_err:.3e}')
