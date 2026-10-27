#!/usr/bin/env python3
"""Self-contained finite tests for three-block unipotent commutator distributions.
Usage: python verify_three_block_commutator.py
Tests are finite corroboration, not a proof of the general theorem.
"""
from itertools import product
from collections import Counter
from math import prod


def add(x,y,q):
    return (x ^ y) if q == 4 else (x + y) % q

def neg(x,q):
    return x if q in (2,4) else -x % q

def mul(x,y,q):
    if q != 4:
        return x*y % q
    p=0
    for i in range(2):
        if (y >> i) & 1:
            p ^= x << i
    if p & 8:
        p ^= 0b1110
    if p & 4:
        p ^= 0b111
    return p

def madd(A,B,q):
    return tuple(add(u,v,q) for u,v in zip(A,B))

def mneg(A,q):
    return tuple(neg(u,q) for u in A)

def mmul(A,B,a,b,c,q):
    out=[]
    for i in range(a):
        for j in range(c):
            s=0
            for k in range(b):
                s=add(s,mul(A[i*b+k],B[k*c+j],q),q)
            out.append(s)
    return tuple(out)

def gauss(n,k,q):
    if k<0 or k>n: return 0
    top=prod(q**n-q**i for i in range(k))
    bot=prod(q**k-q**i for i in range(k))
    assert top%bot==0
    return top//bot

def matrix_rank(A,a,c,q):
    mat=[list(A[i*c:(i+1)*c]) for i in range(a)]
    r=0
    for j in range(c):
        p=next((i for i in range(r,a) if mat[i][j]!=0),None)
        if p is None: continue
        mat[r],mat[p]=mat[p],mat[r]
        inv=next(i for i in range(1,q) if mul(i,mat[r][j],q)==1)
        mat[r]=[mul(v,inv,q) for v in mat[r]]
        for i in range(a):
            if i==r: continue
            c0=mat[i][j]
            mat[i]=[add(mat[i][h],neg(mul(c0,mat[r][h],q),q),q) for h in range(c)]
        r+=1
        if r==a: break
    return r

def factorization_count(a,c,d,r,q):
    total=0
    for s in range(r,min(a,d)+1):
        total+=gauss(a-r,s-r,q)*prod(q**d-q**i for i in range(s))*q**((d-s)*c)
    return total

def allm(q,n):
    return product(range(q),repeat=n)

def group_mult(g,h,a,b,c,q):
    X,Y,Z=g; U,V,W=h
    return madd(X,U,q),madd(Y,V,q),madd(madd(Z,W,q),mmul(X,V,a,b,c,q),q)

def group_inv(g,a,b,c,q):
    X,Y,Z=g
    return mneg(X,q),mneg(Y,q),madd(mneg(Z,q),mmul(X,Y,a,b,c,q),q)

def group_comm(g,h,a,b,c,q):
    v=group_mult(group_mult(group_mult(group_inv(g,a,b,c,q),group_inv(h,a,b,c,q),a,b,c,q),g,a,b,c,q),h,a,b,c,q)
    assert not any(v[0]) and not any(v[1])
    return v[2]

def direct_group(a,b,c,q):
    Xs=list(allm(q,a*b)); Ys=list(allm(q,b*c)); Zs=list(allm(q,a*c))
    elems=list(product(Xs,Ys,Zs))
    counts=Counter(group_comm(g,h,a,b,c,q) for g in elems for h in elems)
    return counts,len(elems)

def verify_one(a,b,c,q):
    counts,order=direct_group(a,b,c,q)
    assert sum(counts.values())==order*order
    for C in allm(q,a*c):
        rank=matrix_rank(C,a,c,q)
        target=q**(2*a*c)*factorization_count(a,c,2*b,rank,q)
        assert counts[C]==target,(a,b,c,q,C,counts[C],target)
    # A product of two independent commutators has independent central increments.
    sq=Counter()
    for U,nu in counts.items():
        for V,nv in counts.items():
            sq[madd(U,V,q)]+=nu*nv
    for C in allm(q,a*c):
        rank=matrix_rank(C,a,c,q)
        target=q**(4*a*c)*factorization_count(a,c,4*b,rank,q)
        assert sq[C]==target,(a,b,c,q,2,C,sq[C],target)
    assert sum(sq.values())==order**4
    return order

def brute_factor(a,c,d,q):
    # Independent product enumeration for the factorization formula.
    counts=Counter()
    B=list(allm(q,d*c))
    for A in allm(q,a*d):
        for V in B:
            counts[mmul(A,V,a,d,c,q)]+=1
    for C in allm(q,a*c):
        rank=matrix_rank(C,a,c,q)
        assert counts[C]==factorization_count(a,c,d,rank,q)
    return sum(counts.values())

def main():
    group_cases=[(1,1,1,2),(1,1,1,3),(1,1,1,4),(2,1,1,2),(1,2,1,2),(2,1,2,2),(1,2,1,3)]
    for a,b,c,q in group_cases:
        size=verify_one(a,b,c,q)
        print('group',a,b,c,q,size,'ok')
    fact_cases=[(2,2,2,2),(2,2,4,2),(1,1,4,3),(2,1,2,3),(1,2,2,4)]
    for a,c,d,q in fact_cases:
        n=brute_factor(a,c,d,q)
        print('factorization',a,c,d,q,n,'ok')
    print('VERIFY_OK_THREE_BLOCK_COMMUTATOR_FIBERS',len(group_cases),len(fact_cases))
if __name__=='__main__': main()
