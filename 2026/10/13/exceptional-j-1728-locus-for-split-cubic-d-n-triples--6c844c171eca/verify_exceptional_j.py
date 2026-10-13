#!/usr/bin/env python3
from fractions import Fraction


def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def poly_pow(a,n):
    out=[1]
    for _ in range(n): out=poly_mul(out,a)
    return out

def poly_add(a,b,sa=1,sb=1):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n): out[i]=(sa*(a[i] if i<len(a) else 0)+sb*(b[i] if i<len(b) else 0))
    return out

# 256(1-l+l^2)^3 - 1728 l^2(1-l)^2
lhs=poly_add([256*x for x in poly_pow([1,-1,1],3)], [1728*x for x in ([0,0]+poly_pow([1,-1],2))], 1, -1)
rhs=[64*x for x in poly_mul(poly_mul(poly_pow([1,1],2),poly_pow([-2,1],2)),poly_pow([-1,2],2))]
assert lhs==rhs, (lhs,rhs)

for s in [1,2,3,7,19,101]:
    a,b,c,n=6*s,8*s,12*s,-47*s*s
    vals=[a*b+n,a*c+n,b*c+n]
    assert vals==[s*s,25*s*s,49*s*s]
    lam=Fraction(b*(c-a),c*(b-a))
    assert lam==2
    assert Fraction(2,b)==Fraction(1,a)+Fraction(1,c)

def is_prime(n):
    if n<2: return False
    d=2
    while d*d<=n:
        if n%d==0: return False
        d+=1
    return True

def count_curve(p):
    total=1
    for x in range(p):
        v=(x*x*x-x)%p
        if v==0: total+=1
        elif pow(v,(p-1)//2,p)==1: total+=2
    return total

primes=[p for p in range(5,200) if is_prime(p)]
checked=0
for p in primes:
    n=count_curve(p)
    if p%4==3:
        assert n==p+1,(p,n)
        checked+=1
print(f"VERIFY_OK family_scales=6 primes_below_200={len(primes)} trace_zero_cases={checked}")
