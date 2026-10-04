#!/usr/bin/env python3
from math import isqrt

def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return sorted(out)

def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def rem_poly(f,g):
    f=f[:]; g=trim(g[:]); assert g[-1]==1
    while len(f)>=len(g):
        c=f[-1]
        if c:
            k=len(f)-len(g)
            for i,gi in enumerate(g): f[i+k]-=c*gi
        trim(f)
    return trim(f)

def eval_poly(a,x):
    v=0
    for c in reversed(a): v=v*x+c
    return v

def primes_upto(n):
    s=[True]*(n+1)
    if n>=0: s[0]=False
    if n>=1: s[1]=False
    for p in range(2,isqrt(n)+1):
        if s[p]:
            for j in range(p*p,n+1,p): s[j]=False
    return [i for i,v in enumerate(s) if v]

def is_prime_trial(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def pos_divs(n):
    n=abs(n); out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return out

expected={(2,2,5),(2,3,5),(6,2,5),(49,2,4363953127297)}
found=set(); divpairs=[]; maxC=0; maxinfo=None
for a in range(2,50):
    ds=[d for d in divisors(a) if d<a]
    m=max(ds)
    R=[0]*(m+1); R[0]=-1
    for d in ds: R[d]+=1
    F=[0]*(a+1); F[0]=1; F[a]=1
    B=rem_poly(F,R)
    C=sum(abs(c) for c in B)
    if C>maxC: maxC=C; maxinfo=(a,C,B[:])
    assert B[0]!=0
    for r in pos_divs(B[0]):
        if r>=2: assert eval_poly(B,r)!=0
    for p in primes_upto(C+1):
        Rp=eval_poly(R,p); num=p**a+1
        if num%Rp==0:
            q=num//Rp; divpairs.append((a,p,q))
            if q!=p and is_prime_trial(q): found.add((a,p,q))
assert maxC==1082 and maxinfo[0]==35
assert found==expected

# Cross-check the packaged divisibility certificate and its compositeness witnesses.
import os
cert=os.path.join(os.path.dirname(__file__),'candidates.tsv')
rows=[]
with open(cert,encoding='utf-8') as fh:
    header=fh.readline().rstrip('\n').split('\t')
    assert header==['a','p','q','status','witness_factor']
    for line in fh:
        a,p,q,status,w=line.rstrip('\n').split('\t')
        a=int(a); p=int(p); q=int(q)
        rows.append((a,p,q))
        if status=='prime_solution':
            assert (a,p,q) in expected and is_prime_trial(q)
            assert w==''
        else:
            f=int(w)
            assert 1<f<q and q%f==0
assert rows==divpairs

def sigma_star_pa_q(p,a,q): return (p**a+1)*(q+1)
def sigma_e_pa_q(p,a,q): return q*sum(p**d for d in divisors(a))
for a,p,q in sorted(found):
    assert sigma_star_pa_q(p,a,q)==sigma_e_pa_q(p,a,q)
print('VERIFY_OK exponents=2..49 max_C=1082 divisibility_pairs=%d solutions=%s' % (len(divpairs), sorted(found)))
