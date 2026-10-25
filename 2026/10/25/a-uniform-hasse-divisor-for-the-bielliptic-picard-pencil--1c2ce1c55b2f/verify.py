#!/usr/bin/env python3
"""Exact finite-characteristic coefficient checks for a bielliptic Picard family.

This is a finite computational corroboration of the general algebraic proof.
It does not certify assertions for all primes by enumeration.
No third-party dependencies.
"""
from math import comb


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]


def coefpoly(k, m, p):
    # [u^m](1+2tu+u^2)^k as a polynomial in t (mod p).
    a = [0] * (m + 1)
    for j in range(k + 1):
        ell = m - 2*j
        if 0 <= ell <= k-j:
            a[ell] = (a[ell] + comb(k,j)*comb(k-j,ell)*pow(2,ell,p)) % p
    return trim(a)


def mul(a,b,p):
    z = [0] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j] = (z[i+j]+x*y)%p
    return trim(z)


def divmodp(a,b,p):
    a=trim([x%p for x in a]); b=trim([x%p for x in b])
    assert b != [0]
    q=[0]*max(1,(len(a)-len(b)+1))
    while a !=[0] and len(a)>=len(b):
        d=len(a)-len(b)
        x=a[-1]*pow(b[-1],-1,p)%p
        q[d]=x
        for j,y in enumerate(b): a[j+d]=(a[j+d]-x*y)%p
        a=trim(a)
    return trim(q),a


def gcdp(a,b,p):
    a=trim(a);b=trim(b)
    while b != [0]:
        a,b=b,divmodp(a,b,p)[1]
    inv=pow(a[-1],-1,p)
    return [(v*inv)%p for v in a]


def derivative(a,p):
    return trim([(j*a[j])%p for j in range(1,len(a))])


def power_factor(n,p):
    out=[1]
    for _ in range(n):out=mul(out,[-1,0,1],p)
    return out


def proportional(a,b,p):
    a=trim(a);b=trim(b)
    if len(a)!=len(b) or b==[0]:return False
    factor=a[-1]*pow(b[-1],-1,p)%p
    return factor!=0 and all((x-factor*y)%p==0 for x,y in zip(a,b))


def evalp(a,x,p):
    v=0
    for c in a[::-1]:v=(v*x+c)%p
    return v


def isprime(n):
    return n>1 and all(n%d for d in range(2,int(n**.5)+1))


def check_prime(p):
    r=(p-1)//6
    if p%6==1:
        assert p==6*r+1
        H=coefpoly(2*r,3*r,p)
        E=coefpoly(4*r,3*r,p)
        G=coefpoly(4*r,6*r,p)
        F=power_factor(r,p)
        assert proportional(E,mul(F,H,p),p),(p,'E identity')
        assert proportional(G,F,p),(p,'G identity')
        # The independent polynomial form of the Gegenbauer equation.
        k,m=2*r,3*r
    else:
        assert p==6*r+5
        H=coefpoly(2*r+1,3*r+2,p)
        A=coefpoly(4*r+3,3*r+2,p)
        F=power_factor(r+1,p)
        assert proportional(A,mul(F,H,p),p),(p,'A identity')
        k,m=2*r+1,3*r+2
    assert len(H)-1==r
    assert evalp(H,1,p)!=0 and evalp(H,-1,p)!=0
    assert gcdp(H,derivative(H,p),p)==[1]
    lhs=mul([1,0,-1],derivative(derivative(H,p),p),p)
    rhs=mul([0,(2*k-1)%p],derivative(H,p),p)
    q=max(len(lhs),len(rhs),len(H))
    assert all(( (lhs[j] if j<len(lhs) else 0)
                +(rhs[j] if j<len(rhs) else 0)
                +m*(m-2*k)*(H[j] if j<len(H) else 0))%p==0
               for j in range(q)),(p,'ODE')
    # Check the exceptional parameter count in the prime field directly.
    zeros=[t for t in range(p) if evalp(H,t,p)==0]
    assert all(t not in (1,p-1) for t in zeros)
    if p in (5,7,11,13,17,19,23):
        known={5:0,7:1,11:1,13:0,17:2,19:1,23:3}
        # For p=13 the two roots t^2=2 live outside F_13.
        assert len(zeros)==known[p],(p,zeros)
    return r,len(zeros)


def main():
    primes=[p for p in range(5,200) if isprime(p)]
    results={p:check_prime(p) for p in primes}
    print('CHECKED',len(primes),'primes from',primes[0],'through',primes[-1])
    for p in [5,7,11,13,17,19,23,29,31]:
        print('p',p,'geometric exceptions',results[p][0],
              'prime-field exceptions',results[p][1])
    print('VERIFY_OK: coefficient identities, root separability, Cartier-pattern consistency, Gegenbauer equation')


if __name__=='__main__':main()
