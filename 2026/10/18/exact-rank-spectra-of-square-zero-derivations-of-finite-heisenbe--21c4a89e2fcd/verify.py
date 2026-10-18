#!/usr/bin/env python3
"""Exact small-field checks for square-zero derivations of Heisenberg Lie algebras."""
import itertools
from collections import Counter
from math import prod


def plus(a,b,q):
    return a^b if q==4 else (a+b)%q


def neg(a,q):
    return a if q==4 else (-a)%q


def mult(a,b,q):
    if q!=4:
        return a*b%q
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&4: a^=7  # x^2+x+1
    return out


def inverse(a,q):
    assert a
    for i in range(1,q):
        if mult(a,i,q)==1: return i
    raise AssertionError('no inverse')


def product(A,B,q):
    out=[]
    for row in A:
        o=[]
        for j in range(len(B[0])):
            t=0
            for k,x in enumerate(row):
                t=plus(t,mult(x,B[k][j],q),q)
            o.append(t)
        out.append(o)
    return out


def rank(A,q):
    a=[list(row) for row in A]
    if not a: return 0
    rows,cols=len(a),len(a[0]); r=0
    for col in range(cols):
        pivot=next((i for i in range(r,rows) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=inverse(a[r][col],q)
        a[r]=[mult(v,inv,q) for v in a[r]]
        for i in range(rows):
            if i==r:continue
            c=a[i][col]
            if not c:continue
            a[i]=[plus(a[i][j],neg(mult(c,a[r][j],q),q),q) for j in range(cols)]
        r+=1
        if r==rows:break
    return r


def gauss_order(n,q):
    return prod(q**n-q**i for i in range(n))


def sp_order(m,q):
    return q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))


def symmetric_nondegenerate(n,q):
    if n==0:return 1
    if q%2:
        # Integer presentation of q^(n(n+1)/2) product_(i=1)^ceil(n/2)(1-q^(1-2i)).
        num=q**(n*(n+1)//2)
        for i in range(1,(n+1)//2+1):
            div=q**(2*i-1)
            assert num%div==0
            num=num//div*(div-1)
        return num
    if n%2:
        return gauss_order(n,q)//sp_order((n-1)//2,q)
    k=n//2
    gl=gauss_order(n,q)
    alt=gl//sp_order(k,q)
    nonalt=gl//(q**(2*k-1)*sp_order(k-1,q))
    return alt+nonalt


def isotropic(m,r,q):
    value=1
    for j in range(r):
        a=q**(2*(m-j))-1
        b=q**(r-j)-1
        value*=a
        assert value%b==0
        value//=b
    return value


def claimed_hist(m,q):
    out=Counter()
    for r in range(m+1):
        nr=isotropic(m,r,q)*symmetric_nondegenerate(r,q)
        out[r]+=nr*q**r
        out[r+1]+=nr*(q**(2*m-r)-q**r)
    assert out[m+1]==0
    del out[m+1]
    return dict(sorted(out.items()))


def list_symmetric(k,q):
    for coeff in itertools.product(range(q),repeat=k*(k+1)//2):
        A=[[0]*k for _ in range(k)]
        pos=0
        for i in range(k):
            for j in range(i,k):
                A[i][j]=A[j][i]=coeff[pos]
                pos+=1
        yield A


def sp_matrices(m,q):
    for p in itertools.product(range(q),repeat=m*m):
        P=[list(p[i*m:(i+1)*m]) for i in range(m)]
        for Q in list_symmetric(m,q):
            for R in list_symmetric(m,q):
                A=[]
                for i in range(m):A.append(P[i]+Q[i])
                for i in range(m):A.append(R[i]+[neg(P[j][i],q) for j in range(m)])
                yield A


def count_exhaustive(m,q):
    k=2*m; out=Counter(); a2_count=Counter()
    tested=0
    for A in sp_matrices(m,q):
        tested+=1
        AA=product(A,A,q)
        if any(t for row in AA for t in row): continue
        r=rank(A,q);a2_count[r]+=1
        for f in itertools.product(range(q),repeat=k):
            fA=[0]*k
            for j in range(k):
                x=0
                for i in range(k):x=plus(x,mult(f[i],A[i][j],q),q)
                fA[j]=x
            if any(fA): continue
            M=[row+[0] for row in A]+[list(f)+[0]]
            assert not any(t for row in product(M,M,q) for t in row)
            out[rank(M,q)]+=1
    expected=claimed_hist(m,q)
    actual={i:out[i] for i in range(m+1)}
    assert actual==expected,(m,q,actual,expected)
    assert sum(a2_count.values())==sum(isotropic(m,r,q)*symmetric_nondegenerate(r,q) for r in range(m+1))
    print('PASS',f'm={m}',f'q={q}', 'checked_sp_matrices=',tested,'A_rank_strata=',dict(a2_count),'D_rank_strata=',actual)


def count_symmetric_direct(n,q):
    return sum(rank(A,q)==n for A in list_symmetric(n,q))


def main():
    for q in (2,3,4,5):
        for n in (1,2,3):
            assert count_symmetric_direct(n,q)==symmetric_nondegenerate(n,q),(q,n)
    for m,q in ((1,2),(1,3),(1,4),(1,5),(2,2),(2,3)):
        count_exhaustive(m,q)
    assert claimed_hist(1,2)=={0:1,1:9}
    assert claimed_hist(2,2)=={0:1,1:45,2:330}
    assert claimed_hist(2,3)=={0:1,1:320,2:8400}
    assert claimed_hist(3,2)=={0:1,1:189,2:6930,3:45360}
    print('VERIFY_OK_HEISENBERG_SQUARE_ZERO_DERIVATION_RANKS')

if __name__=='__main__': main()
