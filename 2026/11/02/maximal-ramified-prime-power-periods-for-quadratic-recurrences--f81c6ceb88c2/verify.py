#!/usr/bin/env python3
"""Exact finite consistency checks for ramified quadratic recurrence periods."""

def prime_factors(n):
    f=[]
    d=2
    while d*d<=n:
        if n%d==0:
            f.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:f.append(n)
    return f

def matmul(A,B,N):
    return ((A[0]*B[0]+A[1]*B[2])%N,(A[0]*B[1]+A[1]*B[3])%N,(A[2]*B[0]+A[3]*B[2])%N,(A[2]*B[1]+A[3]*B[3])%N)

def power(A,k,N):
    R=(1,0,0,1)
    while k:
        if k&1:R=matmul(R,A,N)
        A=matmul(A,A,N)
        k>>=1
    return R

def ordp(a,p):
    k=1;t=a%p
    while t!=1:
        t=t*a%p;k+=1
        assert k<=p-1
    return k

I=(1,0,0,1)
cases=0
for p in (5,7,11,13):
    maxn=p*p
    for P in range(maxn):
        for Q in range(maxn):
            if Q%p==0 or (P*P-4*Q)%p:continue
            a=P*pow(2,-1,p)%p
            assert a!=0
            m=ordp(a,p)
            A=(P,-Q,1,0)
            for k in (1,2,3):
                N=p**k
                n=m*N
                assert power(A,n,N)==I,(p,P,Q,k,'order upper')
                assert power(A,n//p,N)!=I,(p,P,Q,k,'no maximal growth')
                for l in prime_factors(m):
                    assert power(A,n//l,N)!=I,(p,P,Q,k,'coprime factor')
            cases+=1
p=3
# Phi_3(X) = X^2 + X + 1 divides X^3 -1 modulo 9;
# the corresponding companion matrix has order 3 modulo both 3 and 9.
A=(-1,-1,1,0)
assert power(A,3,3)==I and power(A,3,9)==I
assert power(A,1,3)!=I
print(f'VERIFY_OK primes=5,7,11,13 coefficient_lifts={cases} levels=1,2,3 p3_exception=yes')
