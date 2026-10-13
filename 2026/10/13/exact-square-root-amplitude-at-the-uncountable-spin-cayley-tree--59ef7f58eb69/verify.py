#!/usr/bin/env python3
import math
from fractions import Fraction

def theta_c(k,m): return Fraction(m+2,k*m)

def cubic_rational_direct(k,m):
    # coefficient divided by 2^(2/m), directly from the source's two sums
    first=Fraction(math.comb(k,2)*m,m+2)
    second=Fraction(math.comb(k,3)*m,m+4)*theta_c(k,m)
    return first-second

def cubic_rational_closed(k,m):
    return Fraction((k-1)*((k+1)*(m+2)**2-6*k),3*(m+2)*(m+4))

def P(k,m,theta,z):
    ans=0.0
    for i in range(1,k+2,2):
        ans += math.comb(k,i-1)*m/(m-1+i)*2.0**((i-1)/m)*z**i
    for i in range(1,k+1,2):
        ans -= theta*math.comb(k,i)*m/(m+1+i)*2.0**((i-1)/m)*z**i
    return ans

def positive_root(k,m,theta):
    lo=0.0; hi=2.0**(-1.0/m)
    # P(z)/z is negative near zero and positive at the source positivity bound.
    def q(z): return P(k,m,theta,z)/z
    if not q(1e-14)<0 or not q(hi)>0: raise AssertionError((k,m,theta,q(1e-14),q(hi)))
    lo=1e-14
    for _ in range(120):
        mid=(lo+hi)/2
        if q(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def amplitude(k,m):
    return 2.0**(-1.0/m)*math.sqrt(3*k*m*(m+4)/((k-1)*((k+1)*(m+2)**2-6*k)))

def main():
    for k in range(2,15):
        for m in (1,3,5,7,11):
            if Fraction(m+2,k*m) >= 1: continue
            if cubic_rational_direct(k,m) != cubic_rational_closed(k,m):
                raise AssertionError(('cubic',k,m,cubic_rational_direct(k,m),cubic_rational_closed(k,m)))
    worst=0.0; cases=0
    for k,m in ((4,1),(2,3),(3,3),(7,5),(12,7)):
        tc=float(theta_c(k,m)); A=amplitude(k,m)
        for delta in (1e-4,2e-5,4e-6):
            z=positive_root(k,m,tc+delta)
            rel=abs(z/math.sqrt(delta)/A-1.0)
            worst=max(worst,rel); cases+=1
        if rel>0.002: raise AssertionError(('asymptotic',k,m,A,rel))
    print('VERIFY_OK cases=%d worst_rel=%.3e' % (cases,worst))
if __name__=='__main__': main()
