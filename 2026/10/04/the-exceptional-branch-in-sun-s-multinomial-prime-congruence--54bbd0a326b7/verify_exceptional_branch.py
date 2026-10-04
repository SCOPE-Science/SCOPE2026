#!/usr/bin/env python3
"""Finite exact-arithmetic checks for the multinomial congruence dichotomy."""

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out

def mul(a,b,p,N):
    c=[0]*N
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                if i+j>=N: break
                c[i+j]=(c[i+j]+ai*bj)%p
    return c

def power(a,e,p,N):
    r=[1]+[0]*(N-1)
    b=a[:]
    while e:
        if e&1:
            r=mul(r,b,p,N)
        e//=2
        if e:
            b=mul(b,b,p,N)
    return r

def inv_series(a,p,N):
    assert a[0]%p
    b=[0]*N
    b[0]=pow(a[0],-1,p)
    for n in range(1,N):
        s=sum(a[k]*b[n-k] for k in range(1,min(n+1,len(a))))%p
        b[n]=(-s*b[0])%p
    return b

def F_poly(p,m):
    out=[]
    fact=1
    for k in range(p):
        if k:
            fact=fact*k%p
        out.append(1 if m==0 else pow(pow(fact,m,p),-1,p))
    return out

def S_mod(p,l,m,n):
    F=F_poly(p,m)
    c=power(F,l,p,p)[n]
    fact=1
    for k in range(1,n+1):
        fact=fact*k%p
    return c*pow(fact,m,p)%p

def T_mod(p,l,m):
    t=0
    for n in range(1,p):
        s=S_mod(p,l,m,n)
        if m==0:
            term=n*s
        else:
            term=s*pow(pow(n,m-1,p),-1,p)
        if (m*n)&1:
            term=-term
        t=(t+term)%p
    return t

def log_derivative_coeff(p,m):
    F=F_poly(p,m)
    invF=inv_series(F,p,p)
    dF=[((k+1)*F[k+1])%p for k in range(p-1)]
    prod=mul(dF,invF,p,p)
    return prod[p-1] if p-1<len(prod) else 0

def main():
    checks=0
    for p in primes_upto(19):
        for m in range(7):
            # exceptional coefficient should be 1
            assert log_derivative_coeff(p,m)==1%p, (p,m,log_derivative_coeff(p,m))
            for l in range(1,3*p+3):
                got=T_mod(p,l,m)
                want=(p-1) if (l+1)%p==0 else 0
                assert got==want,(p,l,m,got,want)
                checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__':
    main()
