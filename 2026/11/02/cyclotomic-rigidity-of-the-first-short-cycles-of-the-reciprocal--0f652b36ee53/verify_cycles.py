#!/usr/bin/env python3
"""Exact finite-field checks of short cycles of t -> t + 1/t."""
from itertools import product
from math import isqrt


def primes_through(n):
    sieve = [True] * (n + 1)
    sieve[:2] = [False, False]
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for j in range(p*p, n+1, p):
                sieve[j] = False
    return [p for p in range(2,n+1) if sieve[p]]


def polynomial_remainder(a, b, p):
    a = list(a)
    inv = pow(b[-1], -1, p)
    for i in range(len(a) - len(b), -1, -1):
        z = a[i+len(b)-1]*inv % p
        for j in range(len(b)):
            a[i+j] = (a[i+j] - z*b[j]) % p
    return tuple(a[:len(b)-1])


def irreducible_polynomial(p, r):
    if r == 1:
        return (0, 1)
    for c in product(range(p), repeat=r):
        if c[0] == 0:
            continue
        f = c + (1,)
        ok = True
        for d in range(1, r//2 + 1):
            for b in product(range(p), repeat=d):
                if polynomial_remainder(f, b+(1,), p) == (0,)*d:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return f
    raise AssertionError('No irreducible polynomial found')


class Field:
    def __init__(self,p,r):
        self.p,self.r,self.q=p,r,p**r
        self.mod = irreducible_polynomial(p,r)
        self.zero = (0,)*r
        self.one = (1,) + (0,)*(r-1)
    def add(self,a,b):
        return tuple((x+y)%self.p for x,y in zip(a,b))
    def mul(self,a,b):
        p,r=self.p,self.r
        v=[0]*(2*r-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                v[i+j]=(v[i+j]+x*y)%p
        for t in range(2*r-2,r-1,-1):
            z=v[t]
            if z:
                for j in range(r):
                    v[t-r+j]=(v[t-r+j]-z*self.mod[j])%p
        return tuple(v[:r])
    def power(self,a,n):
        ans=self.one
        while n:
            if n&1:ans=self.mul(ans,a)
            a=self.mul(a,a)
            n//=2
        return ans
    def inv(self,a):
        assert a!=self.zero
        return self.power(a,self.q-2)
    def elements(self):
        return product(range(self.p),repeat=self.r)
    def cycles(self,period):
        ans=[]
        for a in self.elements():
            if a==self.zero:continue
            z=a
            steps=[]
            for k in range(period):
                if z==self.zero:break
                steps.append(z)
                z=self.add(z,self.inv(z))
            if len(steps)==period and z==a and len(set(steps))==period:
                ans.append(a)
        return len(ans)


def expected_three(p,r):
    if p==3:return 0
    if p==2:return 3 if r%3==0 else 0
    return 6 if (p**r)%9==1 else 0


def expected_two(p,r):
    if p==2:return 0
    q=p**r
    return 2 if pow((-2)%q, (q-1)//2, q)==1 else 0 if r==1 else None


def run():
    prime_cases=0
    extension_cases=0
    for p in primes_through(1000):
        f=Field(p,1)
        assert f.cycles(3)==expected_three(p,1), ('three',p)
        correct_two=2 if (p==3 or (p>2 and pow((-2)%p,(p-1)//2,p)==1)) else 0
        assert f.cycles(2)==correct_two,('two',p)
        prime_cases+=1
    for p,rmax in [(2,8),(3,5),(5,3),(7,3),(11,2),(13,2),(17,2),(19,2)]:
        for r in range(2,rmax+1):
            if p**r>2500:continue
            f=Field(p,r)
            got3=f.cycles(3)
            assert got3==expected_three(p,r),('three',p,r,got3,expected_three(p,r),f.mod)
            q=p**r
            if p==2: expected2=0
            else:
                val=(-2)%p
                chi=pow(val,(p-1)//2,p)
                expected2=2 if chi==1 or r%2==0 else 0
            got2=f.cycles(2)
            assert got2==expected2,('two',p,r,got2,expected2)
            extension_cases+=1
    print('VERIFY_OK prime_fields='+str(prime_cases)+' extension_fields='+str(extension_cases)+' all_exact_2_and_3_cycles_match')
if __name__=='__main__':run()
