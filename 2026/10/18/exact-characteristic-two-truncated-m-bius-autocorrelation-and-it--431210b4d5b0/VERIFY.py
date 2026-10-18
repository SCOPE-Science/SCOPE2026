#!/usr/bin/env python3
"""Independent finite tests of local factors and shifted truncated Mobius means.
Uses only F_2 and Python stdlib. This file is not a proof
of the unbounded-degree result."""
from fractions import Fraction

def digits(x,q):
    if x==0:return [0]
    out=[]
    while x:
        out.append(x%q);x//=q
    return out

def normalize(c):
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def poly_add(a,b,q):
    x=digits(a,q);y=digits(b,q)
    return sum(((x[i] if i<len(x) else 0)+(y[i] if i<len(y) else 0))%q*q**i for i in range(max(len(x),len(y))))

def rem(a,b,q):
    aa=digits(a,q);bb=digits(b,q)
    if not b:raise ZeroDivisionError
    db=len(bb)-1; inv=pow(bb[-1],-1,q)
    for k in range(len(aa)-1,db-1,-1):
        c=aa[k]*inv%q
        if c:
            for j in range(db+1):aa[k-db+j]=(aa[k-db+j]-c*bb[j])%q
    return sum(aa[i]*q**i for i in range(min(len(aa),db)))

def mul(a,b,q):
    aa=digits(a,q);bb=digits(b,q);out=[0]*(len(aa)+len(bb)-1)
    for i,x in enumerate(aa):
        for j,y in enumerate(bb):out[i+j]=(out[i+j]+x*y)%q
    return sum(t*q**i for i,t in enumerate(out))

def primes_to(maxdeg,q):
    primes=[]
    for d in range(1,maxdeg+1):
        for p in range(q**d,2*q**d):
            if not all(rem(p,k,q) for k in primes if len(digits(k,q))-1<=d//2):
                continue
            primes.append(p)
    return primes

def local_expected(Q, divides, valuation1, short):
    if divides:
        return Fraction(Q*Q-(2 if valuation1 else 1),Q*Q)
    if short:return Fraction(Q*Q-4*Q+2,Q*Q)
    return Fraction(Q*Q-2,Q*Q)

def val(a,p,q):
    if a==0:return 100
    z=0
    while rem(a,p,q)==0:
        z+=1
        # only need if val >= 2
        if z==2: return z
        aa=digits(a,q);bb=digits(p,q)
        res=[0]*(len(aa)-len(bb)+1)
        for k in range(len(aa)-1,len(bb)-2,-1):
            t=aa[k]
            res[k-len(bb)+1]=t
            for j in range(len(bb)):aa[k-len(bb)+1+j]=(aa[k-len(bb)+1+j]-t*bb[j])%q
        a=sum(u*q**i for i,u in enumerate(res))
    return z

def local_test(q,a,p,M):
    d=len(digits(p,q))-1;Q=q**d;pp=mul(p,p,q);observed=0
    for f in range(Q*Q):
        g=poly_add(f,a,q)
        def wt(z):
            if rem(z,pp,q)==0:return 0
            return -1 if d<=M and rem(z,p,q)==0 else 1
        observed+=wt(f)*wt(g)
    vv=val(a,p,q)
    expected=local_expected(Q,vv>0,vv==1,d<=M)
    assert Fraction(observed,Q*Q)==expected, (q,a,p,M,observed,expected)
    return expected

def muM(f,prime_p,psq,M,q):
    for pp in psq:
        if rem(f,pp,q)==0:return 0
    neg=sum(1 for p in prime_p if len(digits(p,q))-1<=M and rem(f,p,q)==0)
    return (-1)**neg

def finite_mean(q,a,M,n):
    prime_p=primes_to(max(M,n//2),q)
    sq=[mul(p,p,q) for p in prime_p if len(digits(p,q))-1<=n//2]
    total=0
    for f in range(q**n,2*q**n):
        g=poly_add(f,a,q)
        total+=muM(f,prime_p,sq,M,q)*muM(g,prime_p,sq,M,q)
    return Fraction(total,q**n)

if __name__=='__main__':
    q=2
    primes=primes_to(3,q)
    count=0
    for a in (1,2,3,4,6):
        for p in primes:
            for M in (0,1,2,3):
                local_test(q,a,p,M)
                count+=1
    print('local_exact_residue_checks',count)
    for a,M,maxn in ((1,1,11),(2,1,11),(3,1,11),(4,1,11),(6,1,11),(2,2,10)):
        vals=[finite_mean(q,a,M,n) for n in range(1,maxn+1) if n>len(digits(a,q))-1]
        print('means',q,a,M,'n_count',len(vals),'last',str(vals[-1]),'previous',str(vals[-2]))
    print('all_exact_checks_passed')
