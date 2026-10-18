#!/usr/bin/env python3
"""Independent finite checks of stated formulas; the general proof is analytic."""
from fractions import Fraction
from math import cos, sin, pi

def coeff_second(t, n):
    a = Fraction(1)
    c = Fraction(0)
    for _ in range(n):
        c = t*c + (1-t*t)*a*a
        a = t*a
    return a, c

def cformula(t, n):
    if n < 1: return Fraction(0)
    return (1+t)*t**(n-1)*(1-t**n)

def variance(t, n):
    return Fraction(n,2) + sum((n-d)*t**d for d in range(1,n))

def third_cumulant(t, n):
    return Fraction(3,4)*sum((n-q)*cformula(t,q) for q in range(1,n)) + Fraction(3,2)*sum((n-p-q)*t**p*cformula(t,q) for p in range(1,n) for q in range(1,n-p))

def numerical_values(t, K=6, num=32768):
    cov=[0.0]*(K+1)
    tri={(a,b):0.0 for a in range(K+1) for b in range(a,K+1)}
    sn2=[0.0]*(K+1)
    sn3=[0.0]*(K+1)
    for v in range(num):
        th=2*pi*(v+0.31347)/num
        z=complex(cos(th),sin(th))
        xs=[]
        for j in range(K+1):
            xs.append(z.real)
            z=z*(z+t)/(1+t*z)
        for j in range(K+1):
            cov[j]+=xs[0]*xs[j]
        for a,b in tri:
            tri[a,b]+=xs[0]*xs[a]*xs[b]
        run=0.0
        for j in range(K+1):
            run+=xs[j]
            sn2[j]+=run*run
            sn3[j]+=run*run*run
    return ([w/num for w in cov],{k:v/num for k,v in tri.items()},[v/num for v in sn2],[v/num for v in sn3])

def main():
    # A degree-two coefficient recurrence from B(z) = (t z + z^2)/(1+t z).
    for t in [Fraction(-4,5),Fraction(-1,2),Fraction(0),Fraction(1,3),Fraction(3,4)]:
        for n in range(1,16):
            a,c=coeff_second(t,n)
            assert a==t**n, (t,n,a)
            assert c==cformula(t,n), (t,n,c)
        for n in range(1,14):
            assert variance(t,n)==Fraction(n,2)+sum((n-d)*t**d for d in range(1,n))
            assert third_cumulant(t,n)==sum(Fraction(3 if i==j else 6,4)*t**(j-i)*cformula(t,k-j) for i in range(n) for j in range(i,n) for k in range(j+1,n))
    # Independent direct boundary quadrature (supporting checks, not infinite proofs).
    for t in [-0.5,0.0,0.5]:
        cov,tri,vs,ks=numerical_values(t,K=6,num=32768)
        for j in range(7):
            assert abs(cov[j]-0.5*t**j)<4e-10,(t,j,cov[j])
            assert abs(vs[j]-float(variance(Fraction(t),j+1)))<3e-9,(t,j,vs[j])
            assert abs(ks[j]-float(third_cumulant(Fraction(t),j+1)))<3e-8,(t,j,ks[j])
        for (a,b),val in tri.items():
            predicted=(t**a)*(float(cformula(Fraction(t),b-a))/4 if b>a else 0)
            assert abs(val-predicted)<6e-9,(t,a,b,val,predicted)
    print('VERIFY_OK: exact Taylor and finite combinatorial identities; independent circle quadrature of covariances, triple moments, and cumulative moments')
if __name__=='__main__': main()
