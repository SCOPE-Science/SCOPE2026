#!/usr/bin/env python3
"""Independent finite checks for three-distinct-power-value coverage."""
from itertools import combinations
from math import gcd

def prime_power_check(p,m,d,expected_missing):
    n=p**m
    P=sorted({pow(x,d,n) for x in range(n)}-{0})
    got=set()
    for x,y,z in combinations(P,3): got.add((x+y+z)%n)
    assert set(range(n))-got==set(expected_missing), (p,m,d,sorted(set(range(n))-got))
    return len(P),len(got)

def extension_check(p,m,coeff,d,expected_missing):
    f=len(coeff); modulus=p**m; order=modulus**f
    def unpack(x):return [(x//(modulus**i))%modulus for i in range(f)]
    def pack(vals):return sum((v%modulus)*(modulus**i) for i,v in enumerate(vals))
    def add(a,b):return pack([u+v for u,v in zip(unpack(a),unpack(b))])
    def mul(a,b):
        u,v=unpack(a),unpack(b)
        w=[0]*(2*f-1)
        for i in range(f):
            for j in range(f):w[i+j]+=u[i]*v[j]
        for i in range(2*f-2,f-1,-1):
            for k in range(f):w[i-f+k]-=w[i]*coeff[k]
        return pack(w[:f])
    def power(a,k):
        ans=1
        while k:
            if k&1:ans=mul(ans,a)
            a=mul(a,a); k>>=1
        return ans
    P=sorted({power(x,d) for x in range(order)}-{0})
    got={add(add(x,y),z) for x,y,z in combinations(P,3)}
    assert set(range(order))-got==set(expected_missing), (p,m,f,sorted(set(range(order))-got))
    return len(P),len(got)

if __name__=='__main__':
    for p,m,d,miss in [
        (2,2,3,range(4)), (2,3,3,[0,2,4,6]),
        (2,4,3,[]),(2,5,3,[]),
        (3,1,5,range(3)),(3,2,5,[0]),(3,3,5,[]),
        (5,1,3,[0]),(5,2,3,[]),(7,1,5,[]),(11,1,3,[])]:
        prime_power_check(p,m,d,miss)
    # Polynomial x^3+x+1 over F2, x^2+x+1 over F2,
    # and x^2+1 over F3; all irreducible modulo p.
    extension_check(2,1,[1,1,0],5,[])
    extension_check(2,1,[1,1],5,[1,2,3])
    extension_check(2,2,[1,1],5,[])
    extension_check(3,1,[1,0],5,[])
    extension_check(3,2,[1,0],5,[])
    print('VERIFY_OK: 16 ring instances, exact target sets')
