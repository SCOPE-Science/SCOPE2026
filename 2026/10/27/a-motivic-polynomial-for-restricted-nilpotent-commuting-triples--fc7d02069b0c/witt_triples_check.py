#!/usr/bin/env python3
"""Finite checks for nilpotent commuting triples in truncated Witt algebras."""
import itertools
import numpy as np


def differential_coeffs(f, p):
    return [(i*f[i]) % p for i in range(1,p)] + [0]


def times(a,b,p):
    h=[0]*p
    for i,x in enumerate(a):
        for j in range(p-i):
            h[i+j]=(h[i+j]+x*b[j])%p
    return h


def restricted_p(f,p):
    h=list(f)
    for _ in range(p-1):
        h=times(f,differential_coeffs(h,p),p)
    return h


def point_pair_formula(p,q):
    a=(p-1)//2
    return q**(p-2)*(q+a*(q*q-1))


def ideal_pair_formula(p,q,m):
    return q**(p-2)*(q+(((p+1)//2)-m)*(q*q-1))


def triple_formula(p,q):
    a=(p-1)//2
    return (point_pair_formula(p,q)+(q-1)*q**p
            +(q-1)*sum(q**(p+r-1) for r in range(2,a+1))
            +(q-1)*sum(q**(m-2)*ideal_pair_formula(p,q,m)
                          for m in range(2,a+2)))


def commuting_array(F,p):
    F=np.asarray(F,dtype=np.int64)
    n=F.shape[0]
    result=np.ones((n,n),dtype=bool)
    for d in range(p):
        M=np.zeros((p,p),dtype=np.int64)
        for i in range(p):
            for j in range(p):
                if i+j-1==d:
                    M[i,j]=(j-i)%p
        result &= ((F @ M @ F.T)%p == 0)
    return result


def exact_for_p5():
    p=5
    all_witt=list(itertools.product(range(p), repeat=p))
    nils=[f for f in all_witt if all(t==0 for t in restricted_p(f,p))]
    assert len(nils)==p**(p-1),len(nils)
    A=commuting_array(nils,p)
    pairs=int(A.sum())
    assert pairs==point_pair_formula(p,p),(pairs,point_pair_formula(p,p))
    Z=A.astype(np.float64)
    prod=Z@Z
    triples=int(np.rint(np.sum(prod*Z)))
    assert triples==triple_formula(p,p),(triples,triple_formula(p,p))
    print('p=5 q=5 nilpotent points',len(nils),'pairs',pairs,'triples',triples)


def ideal_test(p,m):
    q=p
    d=p-m
    elements=np.zeros((q**d,p),dtype=np.int64)
    for k,coef in enumerate(itertools.product(range(q),repeat=d)):
        elements[k,m:]=coef
    A=commuting_array(elements,p)
    pair=int(A.sum())
    pred=ideal_pair_formula(p,q,m)
    assert pair==pred,(p,m,pair,pred)
    print('ideal',p,m,'size',len(elements),'commuting pairs',pair)


def centralizer_check(p):
    import random
    rng=random.Random(23)
    samples=[tuple(rng.randrange(p) for _ in range(p)) for _ in range(150)]
    for f in samples:
        r=next((i for i,v in enumerate(f) if v),p)
        # compute ad coefficients for the standard basis directly
        matrix=np.zeros((p,p),dtype=np.int64)
        for d in range(p):
            for j in range(p):
                for i in range(p):
                    if i+j-1==d:
                        matrix[d,j]+=((j-i)*f[i])
        matrix%=p
        a=matrix.copy().tolist()
        rank=0
        for col in range(p):
            k=next((row for row in range(rank,p) if a[row][col]%p),None)
            if k is None:continue
            a[rank],a[k]=a[k],a[rank]
            inv=pow(a[rank][col],-1,p)
            a[rank]=[(v*inv)%p for v in a[rank]]
            for row in range(p):
                if row!=rank:
                    c=a[row][col]
                    a[row]=[(v-c*w)%p for v,w in zip(a[row],a[rank])]
            rank+=1
        dim=p-rank
        expected=p if r==p else (1 if r==0 else (1 if r==1 else (r if r<=(p-1)//2 else r-1)))
        assert dim==expected,(p,f,r,dim,expected)
    print('centralizers',p,'random checks',len(samples))


if __name__=='__main__':
    exact_for_p5()
    ideal_test(5,2)
    ideal_test(5,3)
    ideal_test(7,3)
    ideal_test(7,4)
    centralizer_check(5)
    centralizer_check(7)
    print('WITT_TRIPLES_OK')
