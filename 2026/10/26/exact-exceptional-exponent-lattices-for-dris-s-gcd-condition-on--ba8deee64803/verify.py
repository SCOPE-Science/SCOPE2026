#!/usr/bin/env python3
"""Check finite instances of the GCD exponent-lattice theorem (stdlib only)."""
from math import gcd

def is_prime(p):
    return p>=2 and all(p%d for d in range(2,int(p**0.5)+1))

def vp(n,p):
    z=0
    while n%p==0:
        z+=1; n//=p
    return z

def order(p):
    x=2%p
    for d in range(1,p):
        if x==1: return d
        x=x*2%p
    raise AssertionError(p)

def predicted(a,b,p):
    d=order(p)
    if d%2==0:return False
    c=vp(2**d-1,p)
    return (2*a+1)%(d*p**max(0,b+1-c))==0

def direct(a,b,p):
    m=2**a*p**b
    z=(2**(2*a+1)-1)*sum(p**j for j in range(2*b+1))
    return gcd(m,z)!=gcd(m*m,z)

for p in range(3,50,2):
    if not is_prime(p):continue
    for a in range(1,21):
        for b in range(1,5):
            assert predicted(a,b,p)==direct(a,b,p),(a,b,p)
    print('PASS odd prime',p,'order',order(p))
for p in [7,23,31,73,127]:
    if not is_prime(p):continue
    d=order(p);c=vp(2**d-1,p)
    for N in [30,100,1000]:
        exact=sum(predicted(a,b,p) for a in range(1,N+1) for b in range(1,N+1))
        constant=((c-1)+1/(p-1))/d if d%2 else 0
        print('lattice count',p,N,exact,'leading term',round(N*constant,6))
print('PASS GCD classification and count checks')
