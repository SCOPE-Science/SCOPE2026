#!/usr/bin/env python3
"""Exact reproducible finite-field point-count certificate; Python standard library only.

The curve is the smooth projective model of y^5-y=x^4+x^2+x over F_5.
Every affine point is counted, and there is exactly one point at infinity.
"""
from math import isqrt
from itertools import product
P=5
MODS={1:(0,1),2:(2,0,1),3:(1,1,0,1),4:(2,0,0,0,1),5:(1,4,0,0,0,1),6:(2,1,0,0,0,0,1)}
EXPECTED=(6,6,156,646,3501,15576)
TRACES=((1,),(2,0),(3,0,3),(4,0,0,0),(0,0,0,0,4),(1,0,0,0,0,0))

def divrem(A,B):
    a=list(A);b=list(B)
    while len(a)>1 and a[-1]==0:a.pop()
    while len(b)>1 and b[-1]==0:b.pop()
    while len(a)>=len(b) and any(a):
        fac=a[-1]*pow(b[-1],P-2,P)%P
        for j in range(len(b)):
            a[len(a)-len(b)+j]=(a[len(a)-len(b)+j]-fac*b[j])%P
        while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)

def check_irreducible(poly):
    n=len(poly)-1
    if n==1:return
    for d in range(1,n//2+1):
        for coeffs in product(range(P),repeat=d):
            q=tuple(coeffs)+(1,)
            if divrem(poly,q)==(0,):
                raise AssertionError(('reducible',poly,q))

class Field:
    def __init__(self,n):
        self.n=n;self.q=P**n;self.poly=MODS[n]
        check_irreducible(self.poly)
        self.pows=tuple(P**j for j in range(n))
    def digits(self,a):
        return tuple(a//b%P for b in self.pows)
    def pack(self,a):
        return sum((v%P)*b for v,b in zip(a,self.pows))
    def plus(self,a,b):
        return self.pack((x+y)%P for x,y in zip(self.digits(a),self.digits(b)))
    def neg(self,a):
        return self.pack((-x)%P for x in self.digits(a))
    def times(self,a,b):
        if self.n==1: return a*b%P
        u=self.digits(a);v=self.digits(b)
        c=[0]*(2*self.n-1)
        for i in range(self.n):
            for j in range(self.n):
                c[i+j]+=u[i]*v[j]
        for k in range(2*self.n-2,self.n-1,-1):
            t=c[k]%P
            for j in range(self.n):
                c[k-self.n+j]-=t*self.poly[j]
        return self.pack(c[:self.n])
    def power(self,x,k):
        out=1
        while k:
            if k&1:out=self.times(out,x)
            k//=2
            if k:x=self.times(x,x)
        return out
    def f(self,x):
        x2=self.times(x,x);x4=self.times(x2,x2)
        return self.plus(self.plus(x,x2),x4)

def count_direct(F):
    """Enumerate all y and x, using the exact fibre-size histogram of y^5-y."""
    hist=[0]*F.q
    for y in range(F.q):
        y5=F.power(y,P)
        hist[F.plus(y5,F.neg(y))]+=1
    assert sorted(set(hist))==[0,P]
    assert sum(hist)==F.q
    return 1+sum(hist[F.f(x)] for x in range(F.q))

def count_trace(F):
    """Independently enumerate traces of x^4+x^2+x in a polynomial basis."""
    traces=[]
    for alpha_j in F.pows:
        total=0;z=alpha_j
        for _ in range(F.n):
            total=F.plus(total,z)
            z=F.power(z,P)
        assert F.digits(total)[1:]==(0,)*(F.n-1)
        traces.append(F.digits(total)[0])
    assert tuple(traces)==TRACES[F.n-1], (F.n,traces)
    histogram=[0]*P
    for x in range(F.q):
        f=F.f(x)
        tr=sum(a*b for a,b in zip(F.digits(f),traces))%P
        histogram[tr]+=1
    assert sum(histogram)==F.q
    return 1+P*histogram[0],tuple(histogram)

def polynomial_irreducible_mod2():
    """Rabin irreducibility criterion for the mod-2 reduction of L(T)."""
    # F(T) = T^12+T^8+T^7+T^6+T^5+T^4+1.
    f=(1<<12)|(1<<8)|(1<<7)|(1<<6)|(1<<5)|(1<<4)|1
    def degree(v):return v.bit_length()-1
    def rem(a,b):
        while a and degree(a)>=degree(b):a^=b<<(degree(a)-degree(b))
        return a
    def mul(a,b):
        c=0
        while b:
            if b&1:c^=a
            a<<=1;b>>=1
        return rem(c,f)
    def gcd(a,b):
        while b:a,b=b,rem(a,b)
        return a
    z=2;frobs={0:z}
    for j in range(1,13):
        z=mul(z,z);frobs[j]=z
    assert frobs[12]==2
    assert gcd(f,frobs[6]^2)==1
    assert gcd(f,frobs[4]^2)==1
    return True

def coefficients(counts):
    # N_n=q^n+1-S_n, where S_n is the n-th Frobenius power sum.
    s=[P**n+1-counts[n-1] for n in range(1,7)]
    c=[1]
    # L(T)=exp(-sum_n S_n*T^n/n)
    for k in range(1,7):
        a=-sum(c[k-j]*s[j-1] for j in range(1,k+1))
        assert a%k==0
        c.append(a//k)
    full=c+[P**(j-6)*c[12-j] for j in range(7,13)]
    return full,s

def is_prime(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))

def main():
    counts=[]
    for n in range(1,7):
        F=Field(n)
        a=count_direct(F)
        b,h=count_trace(F)
        assert a==b==EXPECTED[n-1],(n,a,b)
        counts.append(a)
        print('extension_degree',n,'field_size',F.q,'count',a,'trace_histogram',h)
    c,s=coefficients(counts)
    expected=(1,0,-10,10,55,-25,-175,-125,1375,1250,-6250,0,15625)
    assert tuple(c)==expected,(c,expected)
    assert polynomial_irreducible_mod2()
    cardinality=sum(c)
    assert cardinality==11731 and is_prime(cardinality)
    print('power_sums',s)
    print('L_coefficients_constant_first',c)
    print('irreducible_mod_2',True)
    print('jacobian_order',cardinality,'prime',True)
    print('VERIFY_OK')

if __name__=='__main__':main()
