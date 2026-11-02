#!/usr/bin/env python3
"""Standalone exact counts for prescribed size-two subsets in small Galois rings.
Finite tests are not a proof of universal claims.
"""
from itertools import combinations
from math import gcd


def ring_add(a,b,p,m,f):
    mod=p**m
    return tuple((a[i]+b[i])%mod for i in range(f))

def ring_mul(a,b,p,m,f,coeff):
    mod=p**m
    out=[0]*(2*f-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=(out[i+j]+x*y)%mod
    for k in range(2*f-2, f-1, -1):
        z=out[k]
        for j in range(f): out[k-f+j]=(out[k-f+j]-z*coeff[j])%mod
    return tuple(out[:f])

def ring_pow(a,d,p,m,f,coeff):
    o=(1,)+(0,)*(f-1)
    while d:
        if d&1:o=ring_mul(o,a,p,m,f,coeff)
        a=ring_mul(a,a,p,m,f,coeff);d//=2
    return o

def valuation(a,p,m):
    for t in range(m):
        if any(x%(p**(t+1)) for x in a):return t
    return m

def predicted(t,p,m,f,d):
    q=p**f
    S=list(range(0,m,d))
    sizes={s:(q-1)*q**(m-s-1) for s in S}
    r=sum(sizes[s] for s in S if s<t)
    if t<m and t in sizes:
        r+=(q-2)*q**(m-t-1)+2*sum(sizes[u] for u in S if u>t)
    diag=0
    if p!=2:
        diag=int(t<m and t in sizes)
    elif m==1:
        diag=(q-1) if t==m else 0
    else:
        if t<m and t>=1 and t-1 in sizes:diag=q
        if t==m and m-1 in sizes:diag=q-1
    assert (r-diag)%2==0 and r>=diag, (p,m,f,d,t,r,diag)
    return (r-diag)//2

def run():
    # f=1 gives Z/p^m; f=2 models unramified extension via monic
    # irreducible polynomial X^2+coefficient[1]*X+coefficient[0].
    cases=[(2,1,1,3,(0,1)),(2,2,1,3,(0,1)),(2,4,1,3,(0,1)),
        (2,4,1,5,(0,1)),(3,1,1,5,(0,1)),(3,2,1,5,(0,1)),
        (5,2,1,3,(0,1)),(7,2,1,5,(0,1)),
        (2,1,2,5,(1,1)),(2,2,2,5,(1,1)),
        (3,1,2,5,(1,0)),(3,2,2,5,(1,0))]
    total=0
    for p,m,f,d,coeff in cases:
        if gcd(d,p*(p**f-1))!=1:continue
        vals=range(p**m)
        from itertools import product
        domain=list(product(vals,repeat=f))
        zero=(0,)*f
        P={ring_pow(x,d,p,m,f,coeff) for x in domain}-{zero}
        c={b:0 for b in domain}
        for x,y in combinations(P,2):c[ring_add(x,y,p,m,f)]+=1
        for b in domain:
            t=valuation(b,p,m)
            assert c[b]==predicted(t,p,m,f,d),(p,m,f,d,b,c[b],predicted(t,p,m,f,d))
            total+=1
        print('PASS', (p,m,f,d), '|P|=',len(P),'targets=',len(domain))
    print('PASS TOTAL TARGET EQUALITIES',total)
if __name__=='__main__':run()
