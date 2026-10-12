#!/usr/bin/env python3
import math


def vp(n,p):
    if n==0:
        raise ValueError('valuation of zero')
    v=0
    while n%p==0:
        n//=p; v+=1
    return v


def phi_prime_power(p,j):
    return 1 if j==0 else (p-1)*p**(j-1)


def S(p,r,a):
    n=p**r
    total=0
    for j in range(r+1):
        d=p**j
        total += phi_prime_power(p,j)**2 * math.factorial(p**(r-j)) * d**(p**(r-j)) * a**(p**(r-j))
    return total

primes=[3,5,7,11]
exact_cases=0
for p in primes:
    for r in range(2,4):
        for a in range(1,13):
            if a%p:
                got=vp(S(p,r,a),p)
                want=3*r-2
                assert got==want,(p,r,a,got,want)
                exact_cases+=1

# Directly check the proof's valuation inequalities on a wider finite grid.
ineq_cases=0
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
    for r in range(2,13):
        target=3*r-2
        v0=(p**r-1)//(p-1)
        if (p,r)!=(3,2):
            assert v0>target,(p,r,'j0',v0,target)
        else:
            assert v0==target
        for j in range(1,r):
            m=r-j
            vj=2*j-2+(p**m-1)//(p-1)+j*p**m
            if (p,r,j)==(3,2,1):
                assert vj==target
            else:
                assert vj>target,(p,r,j,vj,target)
            ineq_cases+=1
        vr=3*r-2
        assert vr==target

# Exceptional normalized coefficients at p=3,r=2.
assert math.factorial(9)//81 % 3 == 1
assert (4*math.factorial(3)*3**3)//81 % 3 == 2
assert (36*9)//81 % 3 == 1
print(f'VERIFY_OK exact_cases={exact_cases} inequality_cases={ineq_cases} exceptional_normalized=1,2,1')
