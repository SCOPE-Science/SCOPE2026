#!/usr/bin/env python3
"""Independent finite-field convolution check of the quadratic extension-deficit spectrum.
Run: python3 hyperbolic_hessian_check.py
Uses only the Python standard library. Prime fields and F_9 are supported.
"""
import cmath
import math
import random
from collections import defaultdict

class Field:
    def __init__(self,q):
        assert q in (3,5,7,9)
        self.q=q
        self.el=range(q)
        self.p=3 if q==9 else q
        self.zero=0
        self.one=1
    def add(self,a,b):
        if self.q!=9:return (a+b)%self.q
        return (a%3+b%3)%3+3*((a//3+b//3)%3)
    def neg(self,a):
        if self.q!=9:return (-a)%self.q
        return (-a%3)+3*(-(a//3)%3)
    def mul(self,a,b):
        if self.q!=9:return a*b%self.q
        a0,a1=a%3,a//3;b0,b1=b%3,b//3
        return ((a0*b0+2*a1*b1)%3)+3*((a0*b1+a1*b0)%3)
    def char(self,a):
        exponent=(2*(a%3))%3 if self.q==9 else a
        return cmath.exp(2j*math.pi*exponent/self.p)

def evaluate(q,h):
    F=Field(q)
    P=[(u,v) for u in F.el for v in F.el]
    r=defaultdict(list)
    for i,(u,v) in enumerate(P):
        for j,(a,b) in enumerate(P):
            s=(F.add(u,a),F.add(v,b),F.add(F.mul(u,v),F.mul(a,b)))
            r[s].append((i,j))
    # Expand the quartic deficit coefficient directly, without using the proposed spectrum.
    Q=0.0
    for pairs in r.values():
        n=len(pairs)
        linear=sum((h[i]+h[j] for i,j in pairs),0j)
        quadratic=sum((h[i]*h[j] for i,j in pairs),0j)
        Q+=abs(linear)**2+2*n*quadratic.real
    muR=sum(v.real for v in h)/q**2
    mu2=sum(abs(v)**2 for v in h)/q**2
    C=1+1/q-1/q**2
    actual=C*(4*muR**2+2*mu2)-Q/q**5
    # Independently calculate the claimed spectral quadratic form using direct Fourier sums.
    a=[z.real for z in h];b=[z.imag for z in h]
    predicted=0.
    for k in P:
        def coeff(v):
            return sum(v[i]*F.char(F.neg(F.add(F.mul(k[0],u),F.mul(k[1],w))))
                       for i,(u,w) in enumerate(P))/q**2
        ak,bk=coeff(a),coeff(b)
        if k==(0,0):continue
        axis=(k[0]==0 or k[1]==0)
        real_lam=2-4/q+4/q**2 if axis else 2-2/q+4/q**2
        imag_lam=2 if axis else 2-2/q
        predicted+=real_lam*abs(ak)**2+imag_lam*abs(bk)**2
    return actual,predicted

def main():
    rng=random.Random(59217)
    count=0
    for q in (3,5,7,9):
        F=Field(q)
        P=[(u,v) for u in F.el for v in F.el]
        modes=((1,0),(1,1),(0,1),(1,2))
        for k in modes:
            wave=[F.char(F.add(F.mul(k[0],u),F.mul(k[1],v))) for u,v in P]
            for h in ([z.real for z in wave],[1j*z.real for z in wave],
                      [z.imag for z in wave],[1j*z.imag for z in wave]):
                actual,predicted=evaluate(q,h)
                assert abs(actual-predicted)<2e-9,(q,k,actual,predicted)
                count+=1
        for _ in range(6):
            h=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in P]
            actual,predicted=evaluate(q,h)
            assert abs(actual-predicted)<3e-9,(q,actual,predicted)
            count+=1
    print('PASS',count,'quadratic-form tests over F_3, F_5, F_7 and F_9')
if __name__=='__main__':main()
