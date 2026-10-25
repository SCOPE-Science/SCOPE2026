"""Independent finite checks for the consecutive-square occupancy window theorem.

This is supplementary to the unrestricted analytic proof in RESULT.md.
No conclusions about all parameters are inferred from bounded experiments.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, exp, log, log1p, sqrt, factorial

checks = 0

def check(ok):
    global checks
    checks += 1
    assert ok, 'assertion %d' % checks

def moments(m, n, r, s):
    a, b = Fraction(m-1, m), Fraction(m-2, m)
    er = Fraction(comb(n,r),m**(r-1))*a**(n-r)
    es = Fraction(comb(n,s),m**(s-1))*a**(n-s)
    ers = (Fraction((m-1)*comb(n,r)*comb(n-r,s),m**(r+s-1))
           *b**(n-r-s))
    return er, es, ers

def ratio(m,n,r,s):
    a,b=Fraction(m-1,m),Fraction(m-2,m)
    return (a*Fraction(comb(n-r,s),comb(n,s))
            *b**(n-r-s)/a**(2*n-r-s))

# Independent enumeration: exactly evaluate the empirical statistics.
for m in range(3,5):
    for n in range(5,8):
        sr=ss=srs=0
        for w in product(range(m), repeat=n):
            counts=Counter(w).values()
            nr=sum(x==1 for x in counts)
            ns=sum(x==4 for x in counts)
            sr+=nr; ss+=ns; srs+=nr*ns
        p=m**n
        e1,e4,e14=moments(m,n,1,4)
        check(Fraction(sr,p)==e1)
        check(Fraction(ss,p)==e4)
        check(Fraction(srs,p)==e14)
        check(Fraction(srs,p)-Fraction(sr*ss,p*p)==e14-e1*e4)

# Exact-rational event formulas and one-step ratio for several critical pairs.
for a in range(1,5):
    r,s=a*a,(a+1)**2
    lam=a*(a+1)
    for m in range(3,12):
        q=Fraction(m*(m-2),(m-1)**2)
        for n in range(r+s, r+s+4*m+1):
            er,es,ers=moments(m,n,r,s)
            rr=ratio(m,n,r,s)
            check(ers==er*es*rr)
            check((ers-er*es>0)==(rr>1))
            check(ratio(m,n+1,r,s)/rr
                  ==q*(1+Fraction(r*s,(n+1)*(n+1-r-s))))
        check(ratio(m,lam*m,r,s)>1)

# Second-order expansion: high-precision arithmetic independent of the
# proof's symbolic expansion.  This tests convergence, not asymptotic truth.
import mpmath as mp
mp.mp.dps=65
for a in (1,2,3,4,5):
    r,s=a*a,(a+1)**2
    lam=a*(a+1)
    for m in (1000,10000):
        for z in (-2,-1,0,1,2):
            n=round(lam*m+z*sqrt(m))
            x=mp.mpf(0)
            for j in range(s):
                x+=mp.log(n-r-j)-mp.log(n-j)
            x+=(n-r-s)*mp.log1p(-mp.mpf(2)/m)
            x-=(2*n-r-s-1)*mp.log1p(-mp.mpf(1)/m)
            theory=1-mp.mpf(z*z)/lam
            check(abs(x*m*m-theory)<mp.mpf('0.23'))

print('PASS',checks,'finite exact/high-precision checks')
