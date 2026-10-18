#!/usr/bin/env python3
"""Exact rational cyclotomic reduction and independent frequency checks for a four-tap dyadic Fourier theorem."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
from math import gcd
import cmath
import random
import sympy as sp


def primitive_orders_zero(N, support, weights):
    # Exact coefficient reduction modulo X^(Q/2)+1 at each dyadic conductor Q.
    result=[]
    for r in range(1,N.bit_length()):
        Q=1<<r
        h=Q//2
        reduced=[Fraction(0) for _ in range(h)]
        for x,w in zip(support,weights):
            a=x%Q
            reduced[a%h]+=(1 if a<h else -1)*w
        if all(v==0 for v in reduced):
            result.append(r)
    return tuple(result)


def zero_freq_exact(N, support, weights, j):
    if j==0: return False
    order=N//gcd(j,N)
    h=order//2
    vec=[Fraction(0) for _ in range(h)]
    unit=j//(N//order)
    for x,w in zip(support,weights):
        e=(x*unit)%order
        vec[e%h]+=(1 if e<h else -1)*w
    return all(a==0 for a in vec)


def zero_freq_numeric(N,support,weights,j):
    return abs(sum(float(w)*cmath.exp(2j*cmath.pi*x*j/N) for x,w in zip(support,weights)))<1e-7


def run():
    signatures={}
    examples=[(1,1,1,1),(1,1,2,2),(1,1,1,2),(1,2,3,4),(1,2,2,4)]
    rand=random.Random(33159)
    for N in (8,16,32):
        for ws in examples:
            A=tuple(Fraction(a) for a in ws)
            hist=Counter()
            for S in combinations(range(N),4):
                orders=primitive_orders_zero(N,S,A)
                nu=sum(1<<(r-1) for r in orders)
                if len(set(A))!=1:
                    assert len(orders)<=1,(N,S,ws,orders)
                    assert nu<=N//2,(N,S,ws,nu)
                else:
                    assert len(orders)<=2,(N,S,ws,orders)
                    assert nu<=3*N//4,(N,S,ws,nu)
                    if nu==3*N//4:
                        assert S==tuple(sorted((S[0]+t*(N//4))%N for t in range(4)))
                hist[nu]+=1
                if rand.randrange(100)<3:
                    for j in range(N):
                        z0=zero_freq_exact(N,S,A,j)
                        z1=zero_freq_numeric(N,S,A,j)
                        assert z0==z1,(N,S,ws,j,z0,z1)
                    assert sum(zero_freq_exact(N,S,A,j) for j in range(N))==nu
            signatures[(N,ws)] = dict(sorted(hist.items()))
        print('N=',N,'histograms',[(w, signatures[N,w]) for w in examples], flush=True)
    z=sp.Symbol('z')
    a=1;b=1+sp.sqrt(2)
    P=1+b*z+b*z**2+z**3
    assert sp.simplify(P-(z+1)*(z*z+sp.sqrt(2)*z+1))==0
    assert sp.simplify(P.subs(z,-1))==0
    for j in (3,5):
        zeta=sp.exp(sp.I*sp.pi*j/4)
        assert sp.simplify(sp.expand_complex(P.subs(z,zeta)))==0
    for N in (8,16,32,64):
        q=N//8
        xs=[0,q,2*q,3*q]
        zeros=[]
        for j in range(N):
            v=complex(sp.N(P.subs(z,sp.exp(2*sp.pi*sp.I*j/8)),20))
            if abs(v)<1e-10:zeros.append(j)
        assert zeros==[j for j in range(N) if j%8 in (3,4,5)]
        print('irrational N=',N,'nullity',len(zeros),'orders', sorted({N//gcd(N,j) for j in zeros}))
    print('PASS exact rational tests, arithmetic bound, extremizers, and irrational resonance')

if __name__=='__main__':run()
