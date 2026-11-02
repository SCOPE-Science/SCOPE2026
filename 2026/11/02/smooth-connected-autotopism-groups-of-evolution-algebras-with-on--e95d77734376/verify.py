#!/usr/bin/env python3
"""Small finite-field exhaustive checks for rank-one-product algebra autotopisms.

No general theorem is inferred from finite enumeration. Run: python verify.py.
"""
from itertools import product
from math import prod

def det(M,p):
    n=len(M)
    x=[list(row) for row in M]
    z=1
    for i in range(n):
        j=next((j for j in range(i,n) if x[j][i]%p),None)
        if j is None:return 0
        if j!=i:x[i],x[j]=x[j],x[i];z=-z
        v=x[i][i]%p;z=z*v%p
        iv=pow(v,-1,p)
        for j in range(i+1,n):
            f=x[j][i]*iv%p
            for k in range(i,n):x[j][k]=(x[j][k]-f*x[i][k])%p
    return z%p

def gl(n,p):
    if n==0:return [()]
    return [tuple(tuple(flat[n*i:n*(i+1)]) for i in range(n))
            for flat in product(range(p),repeat=n*n)
            if det([flat[n*i:n*(i+1)] for i in range(n)],p)]

def order_gl(n,q):
    return prod(q**n-q**i for i in range(n))

def bilinear(M,x,y,p):
    return sum(x[i]*M[i][j]*y[j] for i in range(len(x)) for j in range(len(x)))%p

def check(n,r,p,uv,weights=None):
    weights=weights or [1]*r
    B=tuple(tuple(weights[i]%p if i==j and i<r else 0 for j in range(n)) for i in range(n))
    units=gl(n,p)
    countfg=0
    scalar_t_count={a:0 for a in range(1,p)}
    for F in units:
        for G in units:
            # F^T B G, with B diag 1,...,1,0,...,0
            K=tuple(tuple(sum(F[k][i]*weights[k]*G[k][j] for k in range(r))%p for j in range(n)) for i in range(n))
            for t in range(1,p):
                if all(K[i][j]==(t*B[i][j])%p for i in range(n) for j in range(n)):
                    countfg+=1;scalar_t_count[t]+=1
    # For each scalar, independently enumerate the H with H*u=t*u.
    hcount={t:sum(all(sum(H[i][j]*uv[j] for j in range(n))%p==(t*uv[i])%p for i in range(n)) for H in units) for t in range(1,p)}
    actual=sum(scalar_t_count[t]*hcount[t] for t in range(1,p))
    s=n-r
    expected=(p-1)*order_gl(r,p)*order_gl(s,p)**2 * p**(2*r*s+n-1)*order_gl(n-1,p)
    assert actual==expected, (n,r,p,actual,expected)
    assert countfg==(p-1)*order_gl(r,p)*order_gl(s,p)**2*p**(2*r*s)
    print(f"p={p} n={n} rank={r} weights={weights} u={uv}: pair count {countfg}, autotopisms {actual} = formula; PASS")

if __name__=='__main__':
    for n,r,p,u in [
        (1,1,2,(1,)), (1,1,3,(1,)),
        (2,1,2,(0,1)), (2,1,3,(0,1)),
        (2,2,2,(1,0)), (2,2,3,(1,0)),
        (3,1,2,(0,1,0)), (3,2,2,(0,0,1)),
        (3,3,2,(1,0,0)), (3,2,2,(1,1,0)),
    ]:
        check(n,r,p,u)
    check(2,2,3,(1,1),weights=[1,2])
    print('VERIFY_OK')
