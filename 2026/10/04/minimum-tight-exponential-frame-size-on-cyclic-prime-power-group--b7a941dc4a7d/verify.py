#!/usr/bin/env python3
from itertools import combinations

def vp_mod(x,p,k):
    x%=p**k
    assert x
    v=0
    while x%p==0:
        x//=p; v+=1
    return v

def scales(A,p,k):
    return {k-vp_mod(a-b,p,k) for a in A for b in A if a!=b}

def phi_coeffs(p,s):
    m=p**(s-1); deg=(p-1)*m
    c=[0]*(deg+1)
    for j in range(p): c[j*m]=1
    return c

def poly_rem(poly,div):
    a=poly[:]
    d=len(div)-1
    for i in range(len(a)-1,d-1,-1):
        q=a[i]
        if q:
            sh=i-d
            for j,c in enumerate(div): a[sh+j]-=q*c
    return a[:d]

def zero_at_order(J,p,k,s):
    mod=p**s
    c=[0]*mod
    for j in J: c[j%mod]+=1
    return all(x==0 for x in poly_rem(c,phi_coeffs(p,s)))

def tight(A,J,p,k):
    return all(zero_at_order(J,p,k,s) for s in scales(A,p,k))

def construct(p,k,S):
    out=[0]
    for s in sorted(S):
        step=p**(s-1)
        out=[x+j*step for x in out for j in range(p)]
    return sorted(out)

def pred(A,p,k): return p**len(scales(A,p,k))

def exhaustive(p,k):
    N=p**k
    allsets=[]
    for mask in range(1,1<<N):
        allsets.append([i for i in range(N) if mask>>i&1])
    checked=0
    for A in allsets:
        target=pred(A,p,k)
        J0=construct(p,k,scales(A,p,k))
        assert len(J0)==target and tight(A,J0,p,k)
        best=N+1
        for J in allsets:
            if len(J)>=best: continue
            if tight(A,J,p,k): best=len(J)
        assert best==target,(p,k,A,target,best)
        checked+=1
    return checked

def larger_checks():
    cases=[(2,5,[0,1,3,8,17]),(3,3,[0,1,4,9,13]),(5,2,[0,1,5,11]),(7,2,[0,7,15,22])]
    for p,k,A in cases:
        S=scales(A,p,k); J=construct(p,k,S)
        assert tight(A,J,p,k)
        assert len(J)==p**len(S)
        # each required cyclotomic factor contributes p at x=1
        assert len(J)% (p**len(S))==0
    return len(cases)

if __name__=='__main__':
    total=0
    for p,k in [(2,2),(2,3),(3,2)]:
        n=exhaustive(p,k); total+=n
        print(f'exhaustive Z/{p**k}Z: {n} nonempty A checked')
    lc=larger_checks()
    print(f'larger constructed cases: {lc}')
    print(f'VERIFY_OK exhaustive_A={total} larger_cases={lc}')
