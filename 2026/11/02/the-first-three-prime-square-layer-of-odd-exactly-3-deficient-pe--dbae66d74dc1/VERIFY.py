"""Exact certificate for the odd three-prime square layer of 3-deficient-perfect integers.
All operations are exact integers. Python >=3.8; no dependencies.
"""
from fractions import Fraction
from itertools import combinations
from math import isqrt

Q = (5, 7, 11, 13, 17, 19, 23, 29, 31)

def S(p):
    return Fraction(p*p+p+1, p*p)

def prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, isqrt(n)+1))

def proper_divisors(n):
    result=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            if d < n:result.append(d)
            if n//d != d and n//d < n:result.append(n//d)
    return set(result)

assert S(7)*S(11)*S(13)+Fraction(1,7)+Fraction(1,11)+Fraction(1,13) < 2
assert S(5)*S(7)*S(13)+Fraction(1,5)+Fraction(1,7)+Fraction(1,13) < 2
assert S(3)*S(37)*S(41)+Fraction(1,3)+Fraction(1,9)+Fraction(1,37) < 2

T = tuple((a,b,c) for a in range(3) for b in range(3)
          for c in range(3) if (a,b,c)!=(0,0,0))
assert len(T)==26

roots=[]
positives=0
squares=0
for q in Q:
    u=13*(q*q+q+1)
    for triple in combinations(T,3):
        v=[0,0,0]
        for a,b,c in triple:
            v[c] += 3**(2-a)*q**(2-b)
        k=18*q*q-u-v[0]
        b=u+v[1]
        d=u+v[2]
        if k<=0: continue
        positives += 1
        disc=b*b+4*k*d
        h=isqrt(disc)
        if h*h!=disc:continue
        squares += 1
        if (b+h)%(2*k):continue
        r=(b+h)//(2*k)
        if r<=q:continue
        assert d%r==0
        assert k*r*r==b*r+d
        roots.append((q,r,triple))

assert positives==22620
assert squares==57
assert len(roots)==9
assert sorted([r for q,r,tr in roots]) == [11,11,11,13,14,62,203,204,404]
actual=[]
for q,r,triple in roots:
    if not prime(r):continue
    n=9*q*q*r*r
    missing=tuple(sorted(3**(2-a)*q**(2-b)*r**(2-c) for a,b,c in triple))
    sigma=13*(q*q+q+1)*(r*r+r+1)
    assert len(set(missing))==3
    assert all(d in proper_divisors(n) for d in missing)
    assert sum(missing)==2*n-sigma
    actual.append((n,missing))
expected=[
    (27225,(1,25,825)),
    (27225,(11,15,825)),
    (38025,(195,585,1521)),
    (53361,(7,539,7623)),
]
assert sorted(actual)==expected

# The only unexcluded p=5 configuration is (p,q,r)=(5,7,11).
p,q,r=5,7,11
n=(p*q*r)**2
sigma=(p*p+p+1)*(q*q+q+1)*(r*r+r+1)
e=2*n-sigma
ds=proper_divisors(n)
assert len(ds)==26
assert not any(x+y+z==e for x,y,z in combinations(sorted(ds),3))
print(f'VERIFY_OK signatures={len(Q)*2600} positive_K={positives} square_discriminants={squares} integral_roots={len(roots)} witness_triples={len(actual)} integers={len(set(n for n,_ in actual))} excluded_p5_case={n}')
