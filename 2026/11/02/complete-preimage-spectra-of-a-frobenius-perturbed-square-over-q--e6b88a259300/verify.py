#!/usr/bin/env python3
"""Independent finite-field enumeration for f(x)=x*x+x**q over quadratic extensions.
Uses a quadratic basis, so the map is (u,v) -> (u^2+d*v^2+u, (2*u-1)*v).
All fields of odd characteristic; prime and quadratic-prime-power test cases.
"""
from collections import Counter
from math import gcd, isqrt

def prime_factors(n):
    r=[]; a=2
    while a*a<=n:
        if n%a==0:
            r.append(a)
            while n%a==0: n//=a
        a+=1
    if n>1:r.append(n)
    return r

class Field:
    def __init__(self,p,degree):
        self.p=p;self.degree=degree;self.q=p**degree
        assert p>=3 and all(p%d for d in range(2,isqrt(p)+1))
        self.d0=None
        if degree==2:
            self.d0=next(d for d in range(2,p) if pow(d,(p-1)//2,p)==p-1)
    def add(self,a,b):
        p=self.p
        if self.degree==1:return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(self,a):
        p=self.p
        if self.degree==1:return (-a)%p
        return ((-a)%p)+p*((-(a//p))%p)
    def mul(self,a,b):
        p=self.p
        if self.degree==1:return a*b%p
        x,y=a%p,a//p;z,w=b%p,b//p
        return (x*z+self.d0*y*w)%p+p*((x*w+y*z)%p)
    def power(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def find_nonsquare(self):
        m1=self.neg(1)
        return next(x for x in range(2,self.q) if self.power(x,(self.q-1)//2)==m1)

def check(p,d):
    F=Field(p,d);q=F.q
    nonsquare=F.find_nonsquare()
    cnt=Counter()
    minus1=F.neg(1)
    for u in range(q):
        u2=F.mul(u,u)
        for v in range(q):
            re=F.add(F.add(u2,F.mul(nonsquare,F.mul(v,v))),u)
            im=F.mul(F.add(F.add(u,u),minus1),v)
            cnt[re+q*im]+=1
    histogram=Counter(cnt.values())
    histogram[0]=q*q-len(cnt)
    g=gcd(3,q+1)
    want={0:3*(q*q-1)//8,
          1:(2*q*q+q+5-2*g)//6,
          2:(q-1)**2//4+g-1,
          3:(q+1-2*g)//2,
          4:(q*q-4*q-5+8*g)//24}
    assert all(v>=0 for v in want.values())
    assert {r:histogram.get(r,0) for r in range(5)}==want,(q,histogram,want)
    assert sum(want.values())==q*q
    assert sum(k*v for k,v in want.items())==q*q
    assert all(x<=4 for x in cnt.values())
    return q,q*q,len(cnt),sum(1 for c in cnt.values() if c==4)

def main():
    cases=[(p,1) for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]]
    cases += [(p,2) for p in [3,5,7]]
    results=[check(*c) for c in cases]
    print('VERIFY_OK cases={} total_inputs={} total_image_points={} four_fibers={}'.format(len(results),sum(x[1] for x in results),sum(x[2] for x in results),sum(x[3] for x in results)))
    print('TESTED_BASE_FIELD_ORDERS',','.join(str(x[0]) for x in results))
if __name__=='__main__':main()
