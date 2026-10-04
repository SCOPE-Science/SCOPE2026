#!/usr/bin/env python3
from math import comb, gcd
from itertools import combinations

# Exact integer polynomial utilities, coefficients low-to-high.
def trim(a):
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def div_exact(a,b):
    a=a[:]; b=trim(b[:])
    if b[-1] not in (1,-1):
        raise AssertionError('non-monic divisor')
    q=[0]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b) and any(a):
        c=a[-1]//b[-1]
        j=len(a)-len(b)
        q[j]=c
        for i,x in enumerate(b): a[i+j]-=c*x
        trim(a)
    assert all(x==0 for x in a)
    return trim(q)

PHI={1:[-1,1]}
def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]
def cyclo(n):
    if n in PHI: return PHI[n]
    a=[-1]+[0]*(n-1)+[1]
    for d in divisors(n):
        if d<n:
            a=div_exact(a, cyclo(d))
    PHI[n]=trim(a)
    return PHI[n]

def basis_remainders(q):
    phi=cyclo(q); deg=len(phi)-1
    out=[]
    for r in range(q):
        v=[0]*deg
        if r<deg:
            v[r]=1
        else:
            # iteratively multiply previous x^(r-1) by x modulo phi
            prev=out[-1]
            w=[0]+list(prev)
            lead=w.pop() if len(w)>deg else 0
            if lead:
                for i in range(deg): w[i]-=lead*phi[i]
            v=w+[0]*(deg-len(w))
        out.append(tuple(v))
    return out

BASIS={}
def exact_zero(N,A,k):
    if k==0: return False
    g=gcd(N,k); q=N//g; t=k//g
    B=BASIS.setdefault(q,basis_remainders(q))
    s=[0]*len(B[0])
    for a in A:
        v=B[(a*t)%q]
        for i,x in enumerate(v): s[i]+=x
    return all(x==0 for x in s)

def predicted(N,A):
    p=N//2
    antipodal = all(((x+p)%N in A) for x in A)
    parity2 = sum(x&1 for x in A)==2
    if antipodal:
        return set(range(1,N,2))
    if parity2:
        return {p}
    return set()

def isprime(p):
    return p>=2 and all(p%d for d in range(2,int(p**0.5)+1))

subset_total=0
freq_tests=0
for p in [q for q in range(3,14,2) if isprime(q)]:
    N=2*p
    counts={0:0,1:0,p:0}
    for A0 in combinations(range(N),4):
        A=set(A0); subset_total+=1
        direct={k for k in range(N) if exact_zero(N,A,k)}
        freq_tests+=N
        pred=predicted(N,A)
        assert direct==pred,(p,A0,direct,pred)
        counts[len(direct)]+=1
    expected={
        p:comb(p,2),
        1:comb(p,2)**2-comb(p,2),
        0:comb(2*p,4)-comb(p,2)**2,
    }
    assert counts==expected,(p,counts,expected)
    # Equivalent support sizes and counts.
    support_counts={2*p-z:c for z,c in counts.items()}
    assert support_counts[p]==comb(p,2)
    assert support_counts[2*p-1]==comb(p,2)**2-comb(p,2)
    assert support_counts[2*p]==comb(2*p,4)-comb(p,2)**2
    print('p',p,'counts',support_counts)
print('SUBSETS',subset_total)
print('EXACT_FOURIER_TESTS',freq_tests)
print('VERIFY_OK')
