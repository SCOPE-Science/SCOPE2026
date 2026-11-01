#!/usr/bin/env python3
"""Independent algebraic checks for matching-block sequential parity dynamics.
All arithmetic is exact over GF(2); the coordinate identities extend to fields of characteristic two.
"""
from math import gcd

def forward(x,n,k):
    y=x[:]
    for i in range(n):
        neighbors=[j for j in range(n) if j!=i and not (i<2*k and j==(i^1))]
        y[i] ^= sum(y[j] for j in neighbors)&1
    return y

def linear_map(x,n,k):
    m=n-2*k
    pairs=[(x[2*i],x[2*i+1]) for i in range(k)]
    d=[a^b for a,b in pairs]
    D=sum(d)&1
    z=x[2*k:]
    y=[u^D for u in z]
    E=sum(y[1::2])&1
    b=[a^E for a,_ in pairs]
    cy=[sum(y)&1]+y[:-1] if m else []
    bd=[b[i]^d[i]^D for i in range(k)]
    # coordinate transform inverse
    Ed=sum(cy[1::2])&1
    pp=[v^Ed for v in bd]
    qq=[pp[i]^d[i] for i in range(k)]
    DD=sum(d)&1
    zz=[v^DD for v in cy]
    r=[]
    for a,c in zip(pp,qq): r.extend((a,c))
    return r+zz

def order(n,k):
    m=n-2*k
    return (m+1)*(2 if k>=2 else 1)

def rankdim(t,n,k):
    M=n-2*k+1
    b=2*k if t%2==0 else k+(k%2)
    return gcd(M,t)-1+b

def exact_check():
    total=0
    for n in range(4,12,2):
        for k in range(n//2+1):
            L=order(n,k)
            fixed={t:0 for t in range(1,L+1) if L%t==0}
            # At most 2^16 configurations and at most 17 iterations.
            for v in range(1<<n):
                a=[(v>>j)&1 for j in range(n)]
                z=a[:]
                assert forward(a,n,k)==linear_map(a,n,k),(n,k,v)
                for t in range(1,L+1):
                    z=forward(z,n,k)
                    if t in fixed and z==a: fixed[t]+=1
                assert z==a,(n,k,v,L)
                total+=1
            for t, observed in fixed.items():
                expected=1<<rankdim(t,n,k)
                assert observed==expected,(n,k,t,observed,expected)
            print(f'n={n:2} k={k:2} M={n-2*k+1:2} order={L:2} fixed={fixed}')
    print('VERIFIED algebraic coordinate conjugacy, permutation order, and exact fixed populations;',total,'labelled configurations.')

if __name__=='__main__': exact_check()
