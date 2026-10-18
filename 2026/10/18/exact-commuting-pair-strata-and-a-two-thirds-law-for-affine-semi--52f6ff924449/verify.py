#!/usr/bin/env python3
"""Finite-field checks of affine semisymmetric quasigroup commuting strata."""
from fractions import Fraction
from itertools import product
from math import prod


def gl(n, q):
    return prod(q**n - q**j for j in range(n))


def gamma(n, q):
    return prod(Fraction(q**i - 1, q**i) for i in range(1,n+1))


def prediction(n, q, characteristic):
    G=gl(n,q)
    out={r:0 for r in range(n+1)}
    if characteristic != 3:
        for r in out:
            if q % 3 == 1:
                out[r]=sum((Fraction(q**(n-r)*G, gl(n-r,q)*gl(b,q)*gl(r-b,q)) for b in range(r+1)), Fraction())
            elif r % 2 == 0:
                out[r]=Fraction(q**(n-r)*G, gl(n-r,q)*gl(r//2,q*q))
    else:
        for a in range(n//3+1):
            for b in range((n-3*a)//2+1):
                c=n-3*a-2*b
                r=2*a+b
                s=(a+b+c)**2+(a+b)**2+a*a
                centralizer=Fraction(q**s)*gamma(a,q)*gamma(b,q)*gamma(c,q)
                out[r]+=Fraction(q**(n-r)*G)/centralizer
    assert all(v.denominator==1 for v in out.values()), out
    return {r:int(v) for r,v in out.items()}


def field(q):
    if q in (2,3,5,7):
        return (lambda x,y:(x+y)%q, lambda x,y:x*y%q, q)
    if q==4:
        def mul(x,y):
            a=(x&1)*(y&1)
            b=((x&1)*((y>>1)&1)+((x>>1)&1)*(y&1))%2
            c=((x>>1)&1)*((y>>1)&1)
            return (a^c)|((b^c)<<1)  # X^2=X+1
        return (lambda x,y:x^y, mul, q)
    if q==9:
        def mul(x,y):
            a,b=x%3,x//3
            c,d=y%3,y//3
            return ((a*c- b*d)%3)+3*((a*d+b*c)%3)  # X^2=-1
        return (lambda x,y:(x%3+y%3)%3+3*((x//3+y//3)%3),mul,q)
    raise ValueError(q)


def mm(X,Y,n,add,mul):
    Z=[0]*(n*n)
    for i in range(n):
        for k in range(n):
            u=X[i*n+k]
            for j in range(n):
                Z[i*n+j]=add(Z[i*n+j],mul(u,Y[k*n+j]))
    return tuple(Z)


def rank(X,n,q,add,mul):
    M=[list(X[i*n:(i+1)*n]) for i in range(n)]
    pivots=0
    for col in range(n):
        k=next((r for r in range(pivots,n) if M[r][col]),None)
        if k is None: continue
        M[pivots],M[k]=M[k],M[pivots]
        inv=next(i for i in range(1,q) if mul(M[pivots][col],i)==1)
        M[pivots]=[mul(t,inv) for t in M[pivots]]
        for row in range(pivots+1,n):
            a=M[row][col]
            if a:
                minus=(q-a)%q if q in(2,3,5,7) else next(j for j in range(q) if add(j,a)==0)
                M[row]=[add(M[row][j],mul(minus,M[pivots][j])) for j in range(n)]
        pivots+=1
    return pivots


def actual(n,q):
    add,mul,_=field(q)
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    NEG_I=tuple(next(x for x in range(q) if add(x,i)==0) for i in I)
    counts={r:0 for r in range(n+1)}
    number_matrices=0
    for A in product(range(q),repeat=n*n):
        A2=mm(A,A,n,add,mul)
        A3=mm(A2,A,n,add,mul)
        if A3!=NEG_I: continue
        number_matrices+=1
        r=rank(tuple(add(A[i],I[i]) for i in range(n*n)),n,q,add,mul)
        counts[r]+=q**(n-r)
    return counts,number_matrices


def direct_laws(n,q):
    add,mul,_=field(q)
    I=tuple(int(i==j) for i in range(n) for j in range(n))
    neg=lambda x:next(t for t in range(q) if add(t,x)==0)
    negI=tuple(neg(v) for v in I)
    vectors=list(product(range(q),repeat=n))
    observed={r:0 for r in range(n+1)}
    for A in product(range(q),repeat=n*n):
        A2=mm(A,A,n,add,mul)
        if mm(A2,A,n,add,mul)!=negI:continue
        B=tuple(neg(x) for x in A2)
        M=tuple(add(A[k],I[k]) for k in range(n*n))
        r=rank(M,n,q,add,mul)
        def lin(T,v):
            return tuple(__import__('functools').reduce(add,(mul(T[i*n+j],v[j]) for j in range(n)),0) for i in range(n))
        def addv(x,y):return tuple(add(a,b) for a,b in zip(x,y))
        for c in vectors:
            if any(lin(M,c)):continue
            observed[r]+=1
            op=lambda x,y:addv(addv(lin(A,x),lin(B,y)),c)
            commuting=0
            for x in vectors:
                for y in vectors:
                    assert op(op(x,y),x)==y,('semisymmetry',n,q,A,c,x,y)
                    commuting+=int(op(x,y)==op(y,x))
            assert commuting==q**(2*n-r),('commuting',n,q,A,c,r,commuting)
    assert observed==prediction(n,q,2 if q%2==0 else 3 if q==3 else q), (n,q,observed,prediction(n,q,q))
    print(f'direct identity q={q} n={n}: op strata={observed}; PASS')


def run():
    cfg=[(2,1,2),(2,2,2),(2,3,2),(3,1,3),(3,2,3),(3,3,3),
         (4,1,2),(4,2,2),(5,1,5),(5,2,5),(7,1,7),(7,2,7),(9,1,3),(9,2,3)]
    for q,n,p in cfg:
        a,k=actual(n,q)
        b=prediction(n,q,p)
        assert a==b,(q,n,a,b)
        print(f'q={q} n={n}: matrices={k}; weighted counts={a}; PASS')
    for q,n in [(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),(5,1)]: direct_laws(n,q)
    print('VERIFY_OK: 14 exhaustive matrix strata and 7 direct quasigroup-identity checks')

if __name__=='__main__':run()
