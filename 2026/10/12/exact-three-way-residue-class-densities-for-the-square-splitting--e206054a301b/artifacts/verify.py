#!/usr/bin/env python3
"""Exact finite consistency tests for a three-valued multiplicative function.
The infinite progression limits are proved analytically, not inferred here.
"""
from math import gcd, pi
from fractions import Fraction
from itertools import product

N=400000
# independently construct classical Möbius function by linear sieve
mu=[0]*(N+1)
spf=[0]*(N+1)
primes=[]
mu[1]=1
for n in range(2,N+1):
    if spf[n]==0:
        spf[n]=n;primes.append(n);mu[n]=-1
    for p in primes:
        if p>spf[n] or p*n>N:break
        spf[p*n]=p
        if n%p==0:
            mu[p*n]=0;break
        else:mu[p*n]=-mu[n]
# direct prime-power rule from the square/squarefree decomposition
f=[0]*(N+1)
f[1]=1
for n in range(2,N+1):
    p=spf[n];m=n;e=0
    while m%p==0:
        m//=p;e+=1
    local={1:-1,2:-1,3:1}.get(e,0)
    f[n]=local*f[m]
# independent convolution of the two classical Mobius functions
conv=[0]*(N+1)
for d in range(1,int(N**0.5)+1):
    if not mu[d]:continue
    v=d*d
    for m in range(1,N//v+1):
        if mu[m]:conv[v*m]+=mu[d]*mu[m]
assert f==conv
assert all(x in (-1,0,1) for x in f[1:])

# fourth-power-free characteristic identity and all residue-class counts
sieve4=[1]*(N+1)
for d in range(2,int(N**0.25)+2):
    t=d**4
    if t>N:break
    for k in range(t,N+1,t):sieve4[k]=0
assert all(f[i]*f[i]==sieve4[i] for i in range(1,N+1))

def solcount(t,q,a,Y):
    g=gcd(t,q)
    if a%g:return 0
    Q=q//g
    if Q==1:return Y
    r=(a//g)*pow(t//g,-1,Q)%Q
    first=r or Q
    return max(0, (Y-first)//Q+1) if Y>=first else 0

def formula_count(q,a,X):
    return sum(mu[d]*solcount(d**4,q,a,X//d**4)
               for d in range(1,int(X**0.25)+2) if d**4<=X)

def kappa_local_ratio(q,a):
    # kappa(q,a) / (1/zeta(4)), exact rational number.
    z=Fraction(1,q)
    r=q
    for p in primes:
        if p*p>r:break
        if r%p:continue
        e=0
        while r%p==0:r//=p;e+=1
        h=min(e,4)
        local=Fraction(1) - (Fraction(p**h,p**4) if a%(p**h)==0 else Fraction(0))
        z*=local/(1-Fraction(1,p**4))
    if r>1:
        p=r;e=1;h=1
        local=Fraction(1) - (Fraction(1,p**3) if a%p==0 else Fraction(0))
        z*=local/(1-Fraction(1,p**4))
    return z

cases=[1,2,3,4,6,8,9,12,16,24,25,36]
tests=0
sample=[]
for q in cases:
    pos=[0]*q; neg=[0]*q; supp=[0]*q
    for n in range(1,N+1):
        a=n%q
        if f[n]==1:pos[a]+=1
        elif f[n]==-1:neg[a]+=1
        if f[n]:supp[a]+=1
    for a in range(q):
        tests+=1
        assert supp[a]==formula_count(q,a,N),(q,a,supp[a],formula_count(q,a,N))
        rr=kappa_local_ratio(q,a)
        expected=float(rr*Fraction(90,1))*N/(pi**4)
        assert abs(supp[a]-expected)< max(80,2*N**0.25*q),(q,a,supp[a],expected)
        if any((q%(p**4)==0 and a%(p**4)==0) for p in primes if p**4<=q):
            assert rr==0 and supp[a]==0
    for a in sorted({0,1,q//2}):
        if a>=q:continue
        sample.append((q,a,pos[a],neg[a],supp[a],str(kappa_local_ratio(q,a))))
print('VERIFY_OK', 'limit='+str(N), 'class_tests='+str(tests),
      'mobius_convolution=yes','fourth_power_free=yes',
      'crt_exact_counts=yes','local_product_values=yes')
print('q a plus minus support kappa_over_zeta4_inverse')
for row in sample:print(*row)
