#!/usr/bin/env python3
"""Exact elementary checks for central sums on consecutive integer cycles.

Finite checks illustrate the explicit constructions; the infinite theorem
uses CRT and the prime number theorem and is proved in RESULT.md.
"""
from math import gcd

PAIRS = [(17, 13), (29, 23), (41, 31), (47, 37)]

def crt(pairs):
    moduli = []
    residues = []
    for d,e in pairs:
        assert gcd(d,e)==1 and 4*e>3*d and 5*e<4*d
        moduli += [d,e]
        residues += [0, (-pow(4,-1,e)) % e]
    P=1
    for m in moduli:
        assert gcd(P,m)==1
        P*=m
    k0=sum(r*(P//m)*pow(P//m,-1,m) for m,r in zip(moduli,residues))%P
    assert all(k0 % m==r for m,r in zip(moduli,residues))
    return k0,P

def sample(pairs):
    k0,P=crt(pairs)
    k=k0 if k0>=3 else k0+P
    n=4*k
    T=n*(n+1)//2
    seen=set()
    print('pairs',len(pairs),'cycle size',n,'central target',T//2)
    for d,e in pairs:
        assert k%d==0 and (4*k+1)%e==0
        u=(2*k//d)*e
        v=d*((4*k+1)//e)
        a=(v-u+1)//2; b=(v+u-1)//2
        assert 2<=a<=b<=n-1
        assert u==b-a+1 and u*v==T
        assert (a+b)*(b-a+1)==T
        assert 0<u<n//2 and (n-u)>n//2
        standard=('standard',a,b)
        wrap=('wrap',1,a-1,b+1,n)
        assert standard not in seen and wrap not in seen
        seen.add(standard);seen.add(wrap)
        print(' ',d,e,'length',u,'interval',a,b,'complement length',n-u)
    assert len(seen)==2*len(pairs)

def direct(n):
    T=n*(n+1)//2
    if T%2:return 0
    target=T//2
    arr=list(range(1,n+1))
    return sum(sum(arr[(i+j)%n] for j in range(length)) == target
               for length in range(1,n) for i in range(n))

def interval_complement(n):
    T=n*(n+1)//2
    if T%2:return 0
    target=T//2
    internal=boundary=0
    for a in range(1,n+1):
        for b in range(a,n+1):
            if a==1 and b==n:continue
            if (a+b)*(b-a+1)==2*target:
                if a>1 and b<n:internal+=1
                else:boundary+=1
    return 2*internal+boundary

if __name__=='__main__':
    for h in range(1,len(PAIRS)+1):sample(PAIRS[:h])
    for n in range(2,81):
        assert direct(n)==interval_complement(n), n
    print('PASS: four CRT families, exact sums and endpoints, 79 small-cycle counts')
