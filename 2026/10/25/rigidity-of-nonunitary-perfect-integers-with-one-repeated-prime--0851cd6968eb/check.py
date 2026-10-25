#!/usr/bin/env python3
"""Exact finite cross-checks for nonunitary-perfect powerful-core theorem.

No finite enumeration is used in the universal proof.
"""
from math import isqrt

def isprime(n):
    if n < 2: return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0: return False
    return True

def factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0: n//=p; e+=1
            out.append((p,e))
        p+=1 if p==2 else 2
    if n>1: out.append((n,1))
    return out

def sigma_and_unitary(n, f):
    s=u=1
    for p,e in f:
        pe=p**e
        s*= (pe*p-1)//(p-1)
        u*= (1+pe)
    return s,u

def family(a):
    m=2**(a-1)-1
    return 2**a*m if a>=3 and isprime(m) else None

# Full interval, using linear SPF sieve and per-number exact factorizations.
N=300000
spf=list(range(N+1))
for p in range(2,isqrt(N)+1):
    if spf[p]==p:
        for q in range(p*p,N+1,p):
            if spf[q]==q: spf[q]=p

def factor_spf(n):
    f=[]
    while n>1:
        p=spf[n];e=0
        while n%p==0: n//=p;e+=1
        f.append((p,e))
    return f

all_nonunitary=[]
unique_powerful=[]
for n in range(1,N+1):
    f=factor_spf(n)
    s,u=sigma_and_unitary(n,f)
    if s-u==n:
        all_nonunitary.append(n)
        if sum(e>=2 for p,e in f)<=1: unique_powerful.append(n)
expected=sorted(z for a in range(3,32) if (z:=family(a)) is not None and z<=N)
assert unique_powerful==expected,(unique_powerful,expected)
assert all_nonunitary==expected,(all_nonunitary,expected)
# Direct checks across arbitrary squarefree odd cofactors and singleton-powerful-core pairs.
case_count=0
for p in (2,3,5,7,11,13,17):
    for a in range(2,11):
        for q in (3,5,7,11,13,17,19,23):
            for r in (1,3,5,7,11):
                n=p**a*q*r
                if q==p or (r!=1 and (r==p or r==q)):
                    continue
                f=factors(n)
                if sum(e>=2 for pp,e in f)!=1:continue
                s,u=sigma_and_unitary(n,f)
                ok=(s-u==n)
                expect=(p==2 and q==2**(a-1)-1 and r==1 and isprime(q))
                assert ok==expect,(n,ok,expect)
                case_count+=1
for a in range(3,28):
    M=2**(a-1)-1
    n=2**a*M
    f=factors(n)
    s,u=sigma_and_unitary(n,f)
    assert (s-u==n)==isprime(M),(a,M)
print('VERIFY_OK interval',N,'all_nonunitary',all_nonunitary,'unique_powerful',unique_powerful,'extra_exact_families',case_count,'Mersenne_tests',25)
