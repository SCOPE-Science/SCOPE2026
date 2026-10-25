#!/usr/bin/env python3
"""Independent finite checks of block-unipotent square-one conjugacy formulas."""
from itertools import product
from collections import Counter, defaultdict
from math import prod

def mulfield(x,y,q):
    if q==2: return x&y
    if q==4:
        v=0
        for i in range(2):
            if y>>i&1:v^=x<<i
        if v&8:v^=0b1100 # x^3=x^2+x
        if v&4:v^=0b111 # x^2=x+1
        return v
    raise ValueError(q)

def addfield(x,y,q):return x^y

def mprod(A,B,dim,q):
    r,s,t=dim
    return tuple(__import__('functools').reduce(lambda u,v:u^v,(mulfield(A[i*s+k],B[k*t+j],q) for k in range(s)),0) for i in range(r) for j in range(t))

def madd(A,B):return tuple(x^y for x,y in zip(A,B))
def zero(r,c):return (0,)*(r*c)

def gmul(u,v,a,b,c,q):
    X,Y,Z=u; P,Q,R=v
    return madd(X,P),madd(Y,Q),madd(madd(Z,R),mprod(X,Q,(a,b,c),q))

def inv(g,a,b,c,q):
    X,Y,Z=g
    return X,Y,madd(Z,mprod(X,Y,(a,b,c),q))

def rank(M,r,c,q):
    R=[list(M[i*c:(i+1)*c]) for i in range(r)]
    h=0
    def invert(x):
        return next(y for y in range(1,q) if mulfield(x,y,q)==1)
    for j in range(c):
        k=next((i for i in range(h,r) if R[i][j]),None)
        if k is None:continue
        R[h],R[k]=R[k],R[h]
        s=invert(R[h][j]); R[h]=[mulfield(z,s,q) for z in R[h]]
        for i in range(r):
            if i!=h and R[i][j]:
                s=R[i][j];R[i]=[R[i][v]^mulfield(s,R[h][v],q) for v in range(c)]
        h+=1
        if h==r:break
    return h

def gauss(n,k,q):
    if k<0 or k>n:return 0
    a=1
    for i in range(k):a=a*(q**(n-i)-1)//1
    b=prod((q**(i+1)-1) for i in range(k))
    return a//b

def gl(k,q):return prod((q**k-q**i) for i in range(k))

def formula(a,b,c,q):
    predicted=Counter()
    for r in range(min(a,b)+1):
        for s in range(min(c,b-r)+1):
            n=gauss(a,r,q)*gauss(b,r,q)*gl(r,q)*gauss(b-r,s,q)*gauss(c,s,q)*gl(s,q)
            d=a*s+c*r-r*s
            predicted[q**d]+=n*q**(a*c-d)
    return predicted

def check(a,b,c,q):
    pools=[list(product(range(q),repeat=n)) for n in (a*b,b*c,a*c)]
    elements=[(X,Y,Z) for X in pools[0] for Y in pools[1] for Z in pools[2]]
    square=[g for g in elements if gmul(g,g,a,b,c,q)==(zero(a,b),zero(b,c),zero(a,c))]
    # Identity coordinates represent the group identity in the unipotent embedding.
    seen=set(); actual=Counter()
    for g in square:
        if g in seen:continue
        orbit=set()
        for h in elements:
            orbit.add(gmul(gmul(h,g,a,b,c,q),inv(h,a,b,c,q),a,b,c,q))
        assert all(t in square for t in orbit)
        assert not (orbit&seen)
        seen.update(orbit)
        actual[len(orbit)]+=1
    assert len(seen)==len(square)
    expected=formula(a,b,c,q)
    assert actual==expected,(a,b,c,q,actual,expected)
    assert sum(size*number for size,number in actual.items())==len(square)
    maxd=max(size for size in actual)
    expected_max=q**(a*c if b>=min(a,c) else b*max(a,c))
    assert maxd==expected_max
    print(f'a={a} b={b} c={c} q={q}: square_one={len(square)} classes={sum(actual.values())} spectrum={dict(sorted(actual.items()))}, max={maxd}')

if __name__=='__main__':
    for params in ((1,1,1,2),(1,2,1,2),(2,1,1,2),(1,1,2,2),(2,1,2,2),(2,2,1,2),(1,1,1,4),(1,1,2,4)):
        check(*params)
    print('VERIFY_OK_THREE_BLOCK_SQUARE_ONE_CONJUGACY')
