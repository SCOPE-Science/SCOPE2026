#!/usr/bin/env python3
"""Exact finite checks of a four-consecutive-term modular Stern law.
These checks complement, rather than replace, the infinite proof.
"""
from math import gcd
from fractions import Fraction
from collections import Counter

def prim(m,a,b):
    return gcd(gcd(a,b),m)==1

def J(m):
    return sum(prim(m,a,b) for a in range(m) for b in range(m))

def K(m,w,z):
    w%=m; z%=m; g=gcd(w,m)
    if z%g: return Fraction(0)
    q=m//g
    r=((z//g)*pow(w//g,-1,q))%q if q>1 else Fraction(0)
    return Fraction(2**(q-r-1),2**q-1)

def prob(m,a,b,c,d,j):
    if not prim(m,a,b):return Fraction(0)
    even=K(m,2*(b-a),d+a-2*(b-a)) if (c-b+a)%m==0 else Fraction(0)
    odd=K(m,2*b,c+a-3*b) if (d-c+b)%m==0 else Fraction(0)
    return (even+odd)/(2*j)

def factors(n):
    p=2; out=[]
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:n//=p;k+=1
            out.append((p,k))
        p+=1
    if n>1:out.append((n,1))
    return out

def A_local(p,k):
    if p==2:
        return 3 if k==1 else 2**(3*k-2)+sum(2**(3*k-2*t-3) for t in range(1,k-1))+2**k
    return (p-1)*p**(3*k-1)+(p-1)**2*sum(p**(3*k-2*t-2) for t in range(1,k))+(p-1)*p**(k-1)

def A(m):
    a=1
    for p,k in factors(m):a*=A_local(p,k)
    return a

def stern(n):
    if n==0:return 0
    if n==1:return 1
    if n&1:return stern(n//2)+stern(n//2+1)
    return stern(n//2)

def main():
    checked=0
    for m in range(2,13):
        j=J(m)
        brute_a=sum(m//gcd(2*b,m) for a in range(m) for b in range(m) if prim(m,a,b))
        assert brute_a==A(m),(m,brute_a,A(m))
        support=0; mass=Fraction(0)
        for a in range(m):
            for b in range(m):
                for c in range(m):
                    for d in range(m):
                        mu=prob(m,a,b,c,d,j)
                        mass+=mu
                        support+=mu>0
                        checked+=1
        assert mass==1,(m,mass)
        assert support==2*A(m)-j,(m,support,A(m),j)
    # Unimodular binary suffix map and direct four-term identities.
    for t in range(0,4096):
        u,v=stern(t),stern(t+1)
        h=0; z=t+1
        while z%2==0:z//=2;h+=1
        n=2*t
        assert (stern(n),stern(n+1),stern(n+2),stern(n+3)) == (u,u+v,v,(2*h+2)*v-u)
        n=2*t+1
        assert (stern(n),stern(n+1),stern(n+2),stern(n+3)) == (u+v,v,(2*h+2)*v-u,(2*h+1)*v-u)
    # Residue sample is diagnostic only (not proof of density).
    m=7; j=J(m); N=1<<16
    arr=[0,1]
    for n in range(2,N+4):arr.append(arr[n//2] if n%2==0 else arr[n//2]+arr[n//2+1])
    observed=Counter(tuple(arr[n+i]%m for i in range(4)) for n in range(N))
    max_deviation=max(abs(Fraction(count,N)-prob(m,*key,j)) for key,count in observed.items())
    assert max_deviation<Fraction(1,300),max_deviation
    print(f'VERIFY_OK moduli=2..12 quadruples={checked} suffix-identities=4096 support-formula=11 exact-mass=11 max-empirical-error={float(max_deviation):.6g}')
if __name__=='__main__': main()
