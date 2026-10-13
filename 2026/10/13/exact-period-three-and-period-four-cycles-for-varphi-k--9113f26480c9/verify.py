#!/usr/bin/env python3
from math import isqrt

KMAX=180

def sieve(n):
    isp=[True]*(n+1)
    if n>=0: isp[0]=False
    if n>=1: isp[1]=False
    for p in range(2,isqrt(n)+1):
        if isp[p]:
            step=p
            start=p*p
            isp[start:n+1:step]=[False]*(((n-start)//step)+1)
    return isp,[i for i in range(2,n+1) if isp[i]]

LIMIT=KMAX*KMAX//2+KMAX+100
ISP,PRIMES=sieve(LIMIT)

def isprime(n):
    if n<=LIMIT: return ISP[n]
    if n<2:return False
    for p in PRIMES:
        if p*p>n: break
        if n%p==0:return False
    return True

def lpf(n):
    assert n>=2
    x=n; ans=1
    for p in PRIMES:
        if p*p>x: break
        if x%p==0:
            ans=p
            while x%p==0:x//=p
        if x==1:break
    if x>1: ans=max(ans,x)
    return ans

def phi(x,k):
    return x+k if isprime(x) else lpf(x)

def canon(c):
    c=list(c); m=len(c)
    return min(tuple(c[i:]+c[:i]) for i in range(m))

def cycle_from(p,k):
    seen={}; seq=[]; x=p
    for _ in range(2000):
        if x in seen:
            return canon(seq[seen[x]:])
        seen[x]=len(seq);seq.append(x);x=phi(x,k)
    raise RuntimeError((p,k))

def is_power(n,b):
    if n<1:return False
    while n%b==0:n//=b
    return n==1

def class3(c,k):
    if len(c)!=3:return False
    # theorem's necessary and sufficient parameter test plus exact cycle
    if not is_power(k+1,2) or not isprime(k+2):return False
    target=canon([2,k+2,2*k+2])
    return c==target

def class4(c,k):
    if len(c)!=4:return False
    # rotate to start at prime and inspect composite count
    cc=list(c)
    comps=sum(not isprime(x) for x in cc)
    if comps==1:
        if not is_power(k+1,3):return False
        target=canon([3,k+3,2*k+3,3*k+3])
        return isprime(k+3) and isprime(2*k+3) and c==target
    if comps!=2:return False
    # find a prime whose successor is composite; then pattern p,C,q,C
    for i,x in enumerate(cc):
        if isprime(x) and not isprime(cc[(i+1)%4]):
            p=x; C=cc[(i+1)%4]; q=cc[(i+2)%4]; D=cc[(i+3)%4]
            if not isprime(q) or isprime(D):continue
            num=k+p+q; den=p*q
            if num%den:continue
            t=num//den
            if t<1:continue
            A=p*t-1;B=q*t-1
            if A<2 or B<2:continue
            if k!=p*q*t-p-q:continue
            if C!=q*A or D!=p*B:continue
            if lpf(A)>q or lpf(B)>p:continue
            return True
    return False

actual3=actual4=checked_orbits=0
examples3=set();examples4=set()
for k in range(1,KMAX+1):
    bound=max(2,k*k//2)
    cycles=set()
    for p in PRIMES:
        if p>bound:break
        cycles.add(cycle_from(p,k))
        checked_orbits+=1
    c3={c for c in cycles if len(c)==3}
    c4={c for c in cycles if len(c)==4}
    # iff for period 3: expected zero or the unique theorem cycle
    expected3=set()
    if is_power(k+1,2) and isprime(k+2):
        expected3={canon([2,k+2,2*k+2])}
    assert c3==expected3,(k,c3,expected3)
    for c in c3:
        assert class3(c,k);actual3+=1;examples3.add((k,c))
    for c in c4:
        assert class4(c,k),(k,c);actual4+=1;examples4.add((k,c))

# Direct converse checks for many period-4 alternating tuples.
converse4=0
small_primes=[p for p in PRIMES if p<=97]
for p in small_primes:
    for q in small_primes:
        if p==q:continue
        for t in range(1,8):
            A=p*t-1;B=q*t-1
            if A<2 or B<2:continue
            if lpf(A)<=q and lpf(B)<=p:
                k=p*q*t-p-q
                if k<=0:continue
                cyc=[p,p+k,q,q+k]
                if len(set(cyc))<4:continue
                assert all(phi(cyc[i],k)==cyc[(i+1)%4] for i in range(4)),(p,q,t,k,cyc)
                converse4+=1

# Bertrand-family spot checks: consecutive prime q chosen in (p,2p).
bertrand=0
for p in [x for x in small_primes if x>=3]:
    q=next(q for q in PRIMES if p<q<2*p)
    k=p*q-p-q
    cyc=[p,p+k,q,q+k]
    assert all(phi(cyc[i],k)==cyc[(i+1)%4] for i in range(4)),(p,q,k,cyc)
    bertrand+=1

print('VERIFY_OK')
print('KMAX',KMAX)
print('checked_starting_prime_orbits',checked_orbits)
print('period3_cycles_seen',actual3)
print('period4_cycles_seen',actual4)
print('alternating_converse_tuples',converse4)
print('bertrand_family_checks',bertrand)
print('period3_examples',sorted(examples3)[:8])
print('period4_examples',sorted(examples4)[:12])
