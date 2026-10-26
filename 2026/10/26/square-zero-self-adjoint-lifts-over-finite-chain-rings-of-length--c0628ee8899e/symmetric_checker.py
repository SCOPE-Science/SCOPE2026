#!/usr/bin/env python3
"""Independent exhaustive checks for self-adjoint square-zero matrices over prime-square rings."""
from itertools import product
from collections import Counter

def rank_mod(M,p):
    a=[row[:] for row in M]; n=len(a);r=0
    for j in range(n):
        h=next((i for i in range(r,n) if a[i][j]%p),None)
        if h is None:continue
        a[r],a[h]=a[h],a[r]
        inv=pow(a[r][j]%p,-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(n):
            if i!=r:
                c=a[i][j]
                a[i]=[(u-c*v)%p for u,v in zip(a[i],a[r])]
        r+=1
    return r

def enumerate_square_zero(n,p,kind):
    q=p;mod=q*q; positions=[(i,j) for i in range(n) for j in range(i,n)]
    H=[[int(j==n-1-i) if (n%2==0 or i!=n//2) else int(i==j) for j in range(n)] for i in range(n)]
    # This anti-diagonal matrix is an involutory Gram form and has Witt index floor(n/2).
    def mul(a,b):
        if kind=='witt':return a*b%mod
        return (a%q*b%q)%q + q*(((a%q)*(b//q)+(a//q)*(b%q))%q)
    count=Counter()
    for vals in product(range(mod),repeat=len(positions)):
        S=[[0]*n for _ in range(n)]
        for (i,j),v in zip(positions,vals): S[i][j]=S[j][i]=v
        X=[[S[n-1-i][j] for j in range(n)] for i in range(n)]
        if any(sum(mul(X[i][k],X[k][j]) for k in range(n))%mod for i in range(n) for j in range(n)):
            # For the dual ring the arithmetic sum needs coefficientwise reduction, not mod q^2.
            if kind!='dual':continue
        if kind=='dual':
            bad=False
            for i in range(n):
                for j in range(n):
                    prods=[mul(X[i][k],X[k][j]) for k in range(n)]
                    if sum(v%q for v in prods)%q or sum(v//q for v in prods)%q:bad=True
            if bad:continue
        elif any(sum(mul(X[i][k],X[k][j]) for k in range(n))%mod for i in range(n) for j in range(n)):continue
        count[rank_mod([[v%q for v in row] for row in X],q)]+=1
    return dict(count)

if __name__=='__main__':
    cases=[(2,3,'witt',{0:27,1:12}), (2,3,'dual',{0:27,1:12}),
           (2,5,'witt',{0:125,1:40}),(3,3,'witt',{0:729,1:216}),
           (3,3,'dual',{0:729,1:216})]
    for n,p,kind,want in cases:
        got=enumerate_square_zero(n,p,kind)
        assert got==want,(n,p,kind,got,want)
        print('OK',n,p,kind,got,flush=True)
    print('SYMMETRIC_CHAIN_TWO_LIFTS_OK',flush=True)
