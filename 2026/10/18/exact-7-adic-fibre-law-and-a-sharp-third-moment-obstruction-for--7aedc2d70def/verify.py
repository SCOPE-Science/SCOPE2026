#!/usr/bin/env python3
"""Exact checks of the local two-cube representation and its moment law."""
from collections import Counter
from fractions import Fraction

def base_count(r):
    return {0:19,1:6,2:9,3:0,4:0,5:9,6:6}[r]

def formula(n,t):
    if n==0: return 1
    m=7**n;t%=m
    if t%7:
        return base_count(t%7)*7**(n-1)
    if n==1:return 19
    if n==2:return 126+(49 if t==0 else 0)
    return 18*7**(n-1)+(7**4*formula(n-3,t//343) if t%343==0 else 0)

def brute_all(n):
    m=7**n
    cubes=Counter(pow(x,3,m) for x in range(m))
    return [sum(cubes[v]*cubes[(t-v)%m] for v in cubes) for t in range(m)]

def main():
    for n in range(1,5):
        counts=brute_all(n)
        for t,c in enumerate(counts):
            assert c==formula(n,t),(n,t,c,formula(n,t))
        assert sum(counts)==7**(2*n)
        moment=Fraction(sum(c*c for c in counts),7**(3*n))
        print('n',n,'m',7**n,'mom2',moment,'float',float(moment))
    E1=Fraction(2,7)*(Fraction(6,7)+Fraction(9,7))+Fraction(49,343)*Fraction(18,7)
    # Branch probability 1/343 carries an additional 7*E[Y].
    assert E1+Fraction(7,343)==1
    B=(Fraction(2,7)*(Fraction(6,7)**2+Fraction(9,7)**2)
       +Fraction(48,343)*Fraction(18,7)**2
       +Fraction(1,343)*(Fraction(18,7)**2+36))
    assert B/Fraction(6,7)==Fraction(99,49)
    assert Fraction(99,49)-1==Fraction(50,49)
    print('E1=1, E2=99/49, variance=50/49. Branch formula verified.')
    # Verify exact shell formula numerically, distinguishing last nonzero 7-adic digit.
    for j in range(4):
        for r in range(1,7):
            t=7**(3*j)*r
            n=3*j+5
            num=formula(n,t)
            rho=Fraction(num,7**n)
            pred=Fraction(18,7)*sum(7**i for i in range(j))+7**j*Fraction(base_count(r),7)
            assert rho==pred,(j,r,rho,pred)
        for d in (1,2):
            t=7**(3*j+d)
            n=3*j+d+3
            rho=Fraction(formula(n,t),7**n)
            pred=Fraction(18,7)*sum(7**i for i in range(j+1))
            assert rho==pred,(j,d,rho,pred)
    print('Finite shell formulas checked for j=0..3, all units and two residual valuations.')

if __name__=='__main__':main()
