"""Exact finite checks of reciprocal LCM local means and an independent factorization identity."""
from fractions import Fraction
from math import gcd

def factor(n):
    out=[]; p=2
    while p*p<=n:
        a=0
        while n%p==0: a+=1;n//=p
        if a:out.append((p,a))
        p+=1
    if n>1:out.append((n,1))
    return out

def sigma_recip(n):
    out=Fraction(1)
    for p,a in factor(n):out*=sum((Fraction(1,p**j) for j in range(a+1)),Fraction(0))
    return out

def local_r2(n):
    value=Fraction(1)
    for p,a in factor(n):
        s=sum((Fraction(1,p**j) for j in range(a+1)),Fraction(0))
        value*=(s+(s-Fraction(1,p**a)))/2
    return value

def divisors(n):return [d for d in range(1,n+1) if n%d==0]

def direct_lcm(n):
    ds=divisors(n)
    f=sum((Fraction(1,a*b) for a in ds for b in ds if a*b//gcd(a,b)==n),Fraction(0))
    return Fraction(n,2**len(factor(n)))*f

for n in range(1,201):
    left=local_r2(n)
    assert left==direct_lcm(n),(n,left,direct_lcm(n))
    assert 1<=left<=sigma_recip(n)
for p in [2,3,5,7,11,19,31]:
    for a in range(1,6):
        s=sum((Fraction(1,p**j) for j in range(a+1)),Fraction(0))
        t=s-Fraction(1,p**a)
        assert Fraction(p**a,2)*(s*s-t*t)==(s+t)/2
for p in [2,3,5,7,11,13,17,19]:
    x=Fraction(1); term=Fraction(1)
    for a in range(1,21):
        s=sum((Fraction(1,p**j) for j in range(a+1)),Fraction(0))
        term+=Fraction(1,p**a)*(s+(s-Fraction(1,p**a)))/2
    x=(1-Fraction(1,p))*term
    exact=Fraction(1)+Fraction(1,2*p*(p-1))
    assert x<exact and 0<exact-x<Fraction(3,p**21),(p,float(exact-x))
print('VERIFY_OK exact LCM identity for 1..200; local prime-power identities and Euler factors')
