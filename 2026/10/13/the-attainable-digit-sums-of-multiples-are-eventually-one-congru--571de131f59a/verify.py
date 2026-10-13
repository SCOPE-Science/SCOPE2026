#!/usr/bin/env python3
from math import gcd

def ds(n,b):
    s=0
    while n:
        s += n%b
        n//=b
    return s

def bfree_core(n,b):
    m=n
    p=2
    x=b
    ps=[]
    while p*p<=x:
        if x%p==0:
            ps.append(p)
            while x%p==0:x//=p
        p+=1
    if x>1: ps.append(x)
    for p in ps:
        while m%p==0: m//=p
    return m

def order(b,m):
    if m==1:return 1
    x=b%m; r=1
    while x!=1:
        x=x*b%m; r+=1
    return r

def witness(b,n,target):
    g=gcd(n,b-1); q=(b-1)//g
    # select residue seed j in 1..q
    j=next(j for j in range(1,q+1) if (j*n-target)%(b-1)==0)
    seed=j*n; s0=ds(seed,b)
    assert target>=s0 and (target-s0)%(b-1)==0
    m=bfree_core(n,b); nu=order(b,m)
    # aggregate seed digits by exponent modulo nu, then spread to distinct exponents
    counts=[0]*nu; z=seed; e=0
    while z:
        d=z%b; counts[e%nu]+=d; z//=b; e+=1
    E=[]
    for r,c in enumerate(counts):
        E.extend(r+k*nu for k in range(c))
    if not E: raise AssertionError
    if max(E)==0: E=[x+1 for x in E]
    steps=(target-s0)//(b-1)
    E=set(E)
    for _ in range(steps):
        e=max(E); E.remove(e)
        new=[j*nu+e-1 for j in range(1,b+1)]
        assert len(set(new))==b and not (set(new)&E)
        E.update(new)
    # restore prime-power factors of n supported on b by a radix shift
    d=n//m; L=0; bp=1
    while bp%d:
        bp*=b; L+=1
    E={e+L for e in E}
    W=sum(pow(b,e) for e in E)
    assert W%n==0
    assert ds(W,b)==target
    return W

def main():
    cases=targets=adds=0
    for b in range(2,11):
        for n in range(1,51):
            g=gcd(n,b-1); q=(b-1)//g
            T=max(ds(j*n,b) for j in range(1,q+1))
            # necessity on a finite multiplier window
            for k in range(1,51):
                assert ds(k*n,b)%g==0
            start=(T+g-1)//g
            vals=[g*u for u in range(start,start+4)]
            ws=[]
            for t in vals:
                W=witness(b,n,t); ws.append((t,W)); targets+=1
            # addition by digit-block concatenation for first two witnesses
            t1,W1=ws[0]; t2,W2=ws[1]
            L=1
            while b**L<=W1:L+=1
            W=W1+(b**L)*W2
            assert W%n==0 and ds(W,b)==t1+t2
            adds+=1; cases+=1
    print('VERIFY_OK')
    print('base_modulus_cases='+str(cases))
    print('constructed_tail_witnesses='+str(targets))
    print('additive_closure_checks='+str(adds))
if __name__=='__main__': main()
