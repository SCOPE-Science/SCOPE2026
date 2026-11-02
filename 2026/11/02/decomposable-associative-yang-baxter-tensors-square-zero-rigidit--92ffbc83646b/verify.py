#!/usr/bin/env python3
"""Finite-field direct check of tensor-rank-one associative Yang--Baxter solutions.

Usage: python3 verify.py
Standard library only. Tensor equation: r13*r12-r12*r23+r23*r13=0.
"""
from itertools import product
from math import prod


def field(q):
    if q in (2,3):
        return (lambda x,y:(x+y)%q),(lambda x,y:(x*y)%q)
    if q in (4,8):
        mod = 0b111 if q == 4 else 0b1011
        def times(x,y):
            z=0
            while y:
                if y&1:z^=x
                y>>=1;x<<=1
                if x & q:x^=mod
            return z
        return (lambda x,y:x^y),times
    raise ValueError(q)


def matmul(A,B,n,add,mul):
    C=[]
    for i in range(n):
        for j in range(n):
            t=0
            for k in range(n):
                t=add(t,mul(A[i*n+k],B[k*n+j]))
            C.append(t)
    return tuple(C)


def scalar(A,c,mul):return tuple(mul(c,x) for x in A)


def inverse(c,q,mul):
    return next(d for d in range(1,q) if mul(c,d)==1)


def rank(A,n,q,add,mul):
    X=[list(A[n*i:n*(i+1)]) for i in range(n)]
    k=0
    for j in range(n):
        pos=next((i for i in range(k,n) if X[i][j]),None)
        if pos is None:continue
        X[pos],X[k]=X[k],X[pos]
        h=inverse(X[k][j],q,mul)
        X[k]=[mul(x,h) for x in X[k]]
        for i in range(n):
            if i==k:continue
            v=X[i][j]
            if v:
                X[i]=[add(x,mul(-v%q,y)) if q in (2,3) else add(x,mul(v,y)) for x,y in zip(X[i],X[k])]
        k+=1
    return k


def gaussian(n,k,q):
    if n<0 or k<0 or k>n:return 0
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def general_linear(k,q):return prod(q**k-q**i for i in range(k))


def theoretical(n,q):
    L=n//2
    Z={b:gaussian(n,b,q)*gaussian(n-b,b,q)*general_linear(b,q) for b in range(1,L+1)}
    rank_counts={}
    pure=0
    mixed=0
    for a in range(1,L+1):
        for b in range(1,L+1):
            cnt=Z[a]*gaussian(n-a,b,q)*gaussian(n-b,b,q)*general_linear(b,q)//(q-1)
            pure+=cnt
            rank_counts[a*b]=rank_counts.get(a*b,0)+cnt
    for b in range(1,L+1):
        for s in range(b,n+1):
            cnt=2*Z[b]*gaussian(n-b,n-s,q)*q**(s*(n-s))
            mixed+=cnt
            rank_counts[s*b]=rank_counts.get(s*b,0)+cnt
    return pure,mixed,rank_counts


def original_tensor_test(A,B,AA,BB,BA,n,add,mul):
    # No use of the reduced equations in this test.
    for u,v,w in product(range(n*n), repeat=3):
        t=add(mul(mul(AA[u],B[v]),B[w]),mul(mul(A[u],A[v]),BB[w]))
        z=mul(mul(A[u],BA[v]),B[w])
        if t!=z:return False
    return True


def run(n,q,full_original=True):
    add,mul=field(q)
    vectors=[v for v in product(range(q),repeat=n*n) if any(v)]
    squares={v:matmul(v,v,n,add,mul) for v in vectors}
    ranks={v:rank(v,n,q,add,mul) for v in vectors}
    proportional={v:next((c for c in range(q) if squares[v]==scalar(v,c,mul)),None) for v in vectors}
    kinds={}; ranks_by_operator={}
    found=0
    for A in vectors:
        AA=squares[A];la=proportional[A]
        for B in vectors:
            BB=squares[B]; mu=proportional[B]
            BA=matmul(B,A,n,add,mul) if (full_original or la is not None and mu is not None) else None
            predicted=la is not None and mu is not None and BA==tuple(add(x,y) for x,y in zip(scalar(B,la,mul),scalar(A,mu,mul)))
            if full_original:
                actual=original_tensor_test(A,B,AA,BB,BA,n,add,mul)
                if actual!=predicted:
                    raise AssertionError(f'equation mismatch at n={n} q={q}: {A} {B}')
            else:
                actual=predicted
                if actual and not original_tensor_test(A,B,AA,BB,BA,n,add,mul):
                    raise AssertionError('counterexample to sufficiency')
            if not actual:continue
            if mul(la,mu):raise AssertionError('lambda*mu !=0')
            cat='nil-nil' if not la and not mu else 'mixed'
            kinds[cat]=kinds.get(cat,0)+1
            r=ranks[A]*ranks[B]
            ranks_by_operator[r]=ranks_by_operator.get(r,0)+1
            found+=1
    exp_pure,exp_mixed,exp_ranks=theoretical(n,q)
    assert found%(q-1)==0
    assert kinds.get('nil-nil',0)==exp_pure*(q-1),(kinds,exp_pure)
    assert kinds.get('mixed',0)==exp_mixed*(q-1),(kinds,exp_mixed)
    assert all(ranks_by_operator.get(k,0)==v*(q-1) for k,v in exp_ranks.items())
    assert set(ranks_by_operator)==set(exp_ranks)
    print(f'n={n} q={q} original={full_original} '
          f'nonzero_tensors={found//(q-1)} '
          f'nil_nil={exp_pure} mixed={exp_mixed} ranks={dict(sorted(exp_ranks.items()))}',flush=True)


def main():
    for n,q,full in [(2,2,True),(2,3,True),(2,4,True),(3,2,False)]:
        run(n,q,full)
    print('DECOMPOSABLE_AYBE_ALL_DIRECT_CHECKS_OK',flush=True)

if __name__=='__main__':main()
