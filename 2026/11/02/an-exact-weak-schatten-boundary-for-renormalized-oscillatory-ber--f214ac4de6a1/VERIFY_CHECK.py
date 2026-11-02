"""Finite checks for the radial imaginary-power Bergman semicommutator.
Requires mpmath. These checks corroborate, but do not replace, the proof.
"""
from math import comb, factorial
import mpmath as mp
mp.mp.dps=50
checks=0
for d in (1,2,3,4):
    for beta,s in ((mp.mpf('0.35'),mp.mpf('0.7')),(mp.mpf('1.0'),mp.mpf('1.4')),(mp.mpf('2.5'),mp.mpf('2.3'))):
        c=abs(mp.gamma(beta+1j*s)/mp.gamma(beta))**2
        assert 0<c<1
        checks+=1
        prev=None
        for n in (0,1,2,7,31,300,1000):
            m=n+d+beta
            lam=mp.gamma(beta+1j*s)/mp.gamma(beta)*mp.gamma(m)/mp.gamma(m+1j*s)
            r=abs(lam)**2-c
            assert r>0
            if prev is not None: assert r<prev
            prev=r
            # high-precision finite-product check against independent expression
            partial=mp.nprod(lambda k: 1+s*s/(m+k)**2,[0,20000])
            assert abs((abs(lam)**2/c)-partial) < mp.mpf('.003')
            checks+=3
            # first-order coefficient for sufficiently large n
            if n==1000:
                assert abs((n+d+beta)*r/(c*s*s)-1)<mp.mpf('.01')
                checks+=1
        for n in (0,1,2,20):
            count=sum(comb(k+d-1,d-1) for k in range(n+1))
            assert count==comb(n+d,d)
            checks+=1
        # singular-value weak-S_d constant sampled at a high degree
        N=1200
        m=N+d+beta
        lam=mp.gamma(beta+1j*s)/mp.gamma(beta)*mp.gamma(m)/mp.gamma(m+1j*s)
        r=abs(lam)**2-c
        j=comb(N+d,d)
        target=c*s*s/(mp.factorial(d)**(mp.mpf(1)/d))
        assert abs(j**(mp.mpf(1)/d)*r/target-1)<mp.mpf('.01')
        checks+=1
print(f'PASS: {checks} high-precision finite assertions')
