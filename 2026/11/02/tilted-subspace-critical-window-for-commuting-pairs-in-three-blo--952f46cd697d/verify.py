#!/usr/bin/env python3
"""Direct small-field verification of three-block commutation and its row-space law."""
from itertools import product
from collections import Counter
from math import prod


def field(q):
    if q in (2,3,5):
        return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q
    if q==4:
        # GF(4)=GF(2)[t]/(t^2+t+1); bit encoding a+b*t.
        # Reduce binary polynomials modulo t^2+t+1.
        def mul(a,b):
            p=0
            for i in range(2):
                if (b>>i)&1:p^=a<<i
            for i in (2,):
                if (p>>i)&1:p^=0b111<<(i-2)
            return p
        return lambda a,b:a^b,mul
    raise ValueError(q)

def invs(q,mul):
    return {a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}

def mm(A,B,add,mul):
    return tuple(tuple(sum_field([mul(x,y) for x,y in zip(row,col)],add) for col in zip(*B)) for row in A)

def sum_field(seq,add):
    t=0
    for x in seq:t=add(t,x)
    return t

def mats(q,h,w):
    return [tuple(tuple(v[i*w:(i+1)*w]) for i in range(h)) for v in product(range(q),repeat=h*w)]

def rref(A,q,add,mul):
    A=[list(r) for r in A]
    inv=invs(q,mul); n=len(A); k=len(A[0]); pivot=0
    for j in range(k):
        t=next((i for i in range(pivot,n) if A[i][j]),None)
        if t is None:continue
        A[pivot],A[t]=A[t],A[pivot]
        A[pivot]=[mul(inv[A[pivot][j]],x) for x in A[pivot]]
        for i in range(n):
            if i!=pivot and A[i][j]:
                scalar=A[i][j]
                A[i]=[add(x,mul(scalar,y)) if q==4 or q==2 else (x-mul(scalar,y))%q for x,y in zip(A[i],A[pivot])]
        pivot+=1
        if pivot==n:break
    return tuple(tuple(r) for r in A[:pivot])

def qbinom(m,r,q):
    if r<0 or r>m:return 0
    num=prod(q**(m-i)-1 for i in range(r)); den=prod(q**(r-i)-1 for i in range(r))
    return num//den

def theoretical(q,a,b,c):
    m=2*b
    rank_tot=Counter()
    for r in range(min(a,m)+1):
        sub=qbinom(m,r,q)
        emb=prod(q**a-q**i for i in range(r))
        rank_tot[r]=sub*emb*q**((m-r)*c)
    return rank_tot

def check(q,a,b,c):
    add,mul=field(q)
    Xs=mats(q,a,b);Ys=mats(q,b,c)
    samples=[(X,Y) for X in Xs for Y in Ys]
    totals=Counter(); byspace=Counter()
    for X,Y in samples:
        for XP,YP in samples:
            # independent group products: Z parts of g*h and h*g differ only by XY' versus X'Y.
            lhs=mm(X,YP,add,mul);rhs=mm(XP,Y,add,mul)
            if lhs!=rhs:continue
            A=tuple(tuple(row)+tuple(((-v)%q if q!=4 else v) for v in rowp) for row,rowp in zip(X,XP))
            W=rref(A,q,add,mul)
            totals[len(W)]+=1
            byspace[W]+=1
    exp=theoretical(q,a,b,c)
    assert totals==exp,(q,a,b,c,totals,exp)
    # Check the exact individual-rowspace conditional weights, not just rank totals.
    for W,v in byspace.items():
        r=len(W)
        expect=prod(q**a-q**i for i in range(r))*q**((2*b-r)*c)
        assert v==expect,(q,a,b,c,W,v,expect)
    assert sum(totals.values())<=len(samples)**2
    print('PASS',q,a,b,c,'noncentral_elements',len(samples),'commuting_pairs',sum(totals.values()),'ranks',sorted(totals.items()),'rowspaces',len(byspace))

if __name__=='__main__':
    for args in [(2,1,1,1),(2,2,1,1),(2,1,1,2),(2,2,1,2),
                 (2,3,1,3),(2,2,2,2),(3,1,1,1),(3,2,1,2),(4,1,1,1)]:
        check(*args)
    for q in (2,3,4):
        b=1;m=2*b
        target=sum(qbinom(m,r,q) for r in range(m+1))
        for n in (6,10):
            s=sum(qbinom(m,r,q)*prod(1-q**(i-n) for i in range(r)) for r in range(m+1))
            assert 0<target-s<3*q**(m-n)*target
        print('LIMIT_PASS',q,'sum_subspaces',target)
    print('VERIFY_OK 9 exhaustive cases plus 6 diagonal-limit checks')
