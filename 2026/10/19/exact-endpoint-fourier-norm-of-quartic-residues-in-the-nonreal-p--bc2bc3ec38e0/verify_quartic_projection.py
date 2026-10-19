#!/usr/bin/env python3
"""Independent arithmetic/complex checks for quartic-residue Fourier projections.
Public, reproducible mathematical regression tests only.
"""
import cmath
import math
from fractions import Fraction

def primes_upto(n):
    return [p for p in range(5,n+1) if all(p%d for d in range(2,math.isqrt(p)+1))]

def primitive_root(p):
    for g in range(2,p):
        if len({pow(g,k,p) for k in range(p-1)})==p-1: return g
    raise ValueError(p)

def signed_gauss_representation(p):
    candidates=[a for a in range(-math.isqrt(p),math.isqrt(p)+1)
                if a%4==1 and p-a*a>0 and math.isqrt((p-a*a)//4)**2*4==p-a*a]
    assert len(candidates)==1, (p,candidates)
    return candidates[0]

def test_prime(p):
    assert p%8==5
    g=primitive_root(p);h=(p-1)//4
    expo={pow(g,e,p):e%4 for e in range(p-1)}
    powers=(1,1j,-1,-1j)
    J=sum((powers[expo[x]]*powers[expo[(1-x)%p]] for x in range(2,p)),0j)
    a=signed_gauss_representation(p)
    assert abs(J.real+a)<1e-9 and abs(J.real-round(J.real))<1e-9,(p,a,J)
    assert abs(J.real**2+J.imag**2-p)<1e-9,(p,J)
    zeta=cmath.exp(2j*math.pi/p)
    eta=[sum(zeta**pow(g,(4*j+k)%(p-1),p) for j in range(h)) for k in range(4)]
    assert abs(eta[0]-eta[2].conjugate())<1e-9
    assert abs(eta[1]-eta[3].conjugate())<1e-9
    U=3*p+1+2*(a-1)*math.sqrt(p)
    V=3*p+1-2*(a-1)*math.sqrt(p)
    assert U>0 and V>0
    assert abs(abs(eta[0])**2-U/16)<1e-8,(p,eta[0],U)
    assert abs(abs(eta[1])**2-V/16)<1e-8,(p,eta[1],V)
    claim=(p-1)/(4*p)*(1+(math.sqrt(U)+math.sqrt(V))/2)
    kernel=( [h/p]+[eta[expo[x]]/p for x in range(1,p)])
    actual=sum(abs(x) for x in kernel)
    assert abs(claim-actual)<1e-8,(p,claim,actual)
    return claim,a

if __name__=='__main__':
    ps=[p for p in primes_upto(1000) if p%8==5]
    for p in ps:
        value,a=test_prime(p)
        if p in (5,13,29,37,53,101,197,997):
            print('p',p,'a',a,'L_infinity_norm',format(value,'.12f'))
    print('VERIFY_OK primes',len(ps),'range',ps[0],ps[-1])
