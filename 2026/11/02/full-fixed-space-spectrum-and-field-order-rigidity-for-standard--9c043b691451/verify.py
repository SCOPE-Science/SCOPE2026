#!/usr/bin/env python3
"""Exhaustive generator-image enumeration of fixed-point-free automorphisms
for the standard filiform Lie algebra over the fields of orders 2, 3, 4, 5.

The enumeration ranges over both generator images without assuming that
an automorphism preserves a particular abelian ideal. Any homomorphism must
send the defining iterated Lie brackets to the corresponding brackets,
which reconstructs the images of every basis vector. All relations are
checked before a candidate is counted as an automorphism.
"""
from itertools import product
from math import gcd
from collections import Counter
from fractions import Fraction


def field(q):
    if q == 4:
        def mul(a, b):
            # GF(4)=GF(2)[u]/(u^2+u+1)
            c0=(a&1)*(b&1)
            c1=((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1))
            c2=((a>>1)&1)*((b>>1)&1)
            return (c0 ^ c2) | ((c1 ^ c2)<<1)
        add=lambda a,b:a^b
    else:
        mul=lambda a,b:(a*b)%q
        add=lambda a,b:(a+b)%q
    neg=lambda a: a if q==4 else (-a)%q
    inv={a:next(b for b in range(1,q) if mul(a,b)==1)
         for a in range(1,q)}
    return add,mul,neg,inv


def rank(columns,q,ops, shift_identity=False):
    add,mul,neg,inv=ops
    size=len(columns)
    rows=[[columns[c][r] for c in range(size)] for r in range(size)]
    if shift_identity:
        for i in range(size): rows[i][i]=add(rows[i][i],neg(1))
    r=0
    for c in range(size):
        piv=next((k for k in range(r,size) if rows[k][c]),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        factor=inv[rows[r][c]]
        for j in range(c,size): rows[r][j]=mul(rows[r][j],factor)
        for i in range(r+1,size):
            a=rows[i][c]
            if a:
                for j in range(c,size):
                    rows[i][j]=add(rows[i][j],neg(mul(a,rows[r][j])))
        r+=1
        if r==size: break
    return r


def counts_by_generators(q,m):
    ops=field(q); add,mul,neg,_=ops
    n=m+1
    vecs=list(product(range(q),repeat=n))
    def bracket(u,v):
        z=[0]*n
        for i in range(1,m):
            # [t,e_(i+1)]=e_i; coordinate 0 corresponds to t.
            z[i]=add(mul(u[0],v[i+1]),neg(mul(v[0],u[i+1])))
        return tuple(z)
    aut=fpf=0
    histogram=Counter()
    for T in vecs:
        for E in vecs:
            images=[None]*n; images[0]=T; images[m]=E
            for j in range(m-1,0,-1):images[j]=bracket(T,images[j+1])
            # All defining brackets among e_1,...,e_m vanish.
            if any(any(bracket(images[i],images[j]))
                   for i in range(1,m+1) for j in range(i+1,m+1)):
                continue
            if any(bracket(T,images[1])):continue
            if rank(images,q,ops)!=n:continue
            aut+=1
            fixed_dim=n-rank(images,q,ops,True)
            histogram[fixed_dim]+=1
            if fixed_dim==0:fpf+=1
    return aut,fpf,dict(histogram)


def multiplicative_order(a,q,ops):
    mul=ops[1]
    acc=1
    for i in range(1,q):
        acc=mul(acc,a)
        if acc==1:return i
    raise AssertionError('bad field')


def counts_by_formula(q,m):
    Q=q-1
    n0=sum(Q-min(m,multiplicative_order(a,q,field(q)))
           for a in range(2,q))
    return Q*Q*q**(2*m-1), n0*q**(2*m-1)


def predicted_histogram(q,m):
    Q=q-1
    P=Counter()
    def add(k,val):P[k]+=val
    def M(L):
        if L<=0:return {0:Fraction(1)}
        out={d:Fraction(Q,q**d) for d in range(1,L)}
        out[L]=Fraction(1,q**(L-1))
        return out
    # a=1, b !=1
    add(1,Fraction(Q-1))
    # a=1, b=1
    for s in range(1,m+1):
        w=Fraction(Q,q**s) if s<m else Fraction(1,q**(m-1))
        add(s,w*(1-Fraction(1,q**s)))
        add(s+1,w*Fraction(1,q**s))
    # a has order r>1
    for a in range(2,q):
        r=multiplicative_order(a,q,field(q))
        add(0,Fraction(Q-r))
        for j in range(r):
            L=max(0,(m-j+r-1)//r)
            for k,p in M(L).items():add(k,p)
    multiplier=q**(2*m-1)
    assert all((v*multiplier).denominator==1 for v in P.values())
    return {i:int(P[i]*multiplier) for i in sorted(P) if P[i]}


def verify():
    cases=[(2,3),(2,4),(3,3),(3,4),(4,3),(5,3)]
    for q,m in cases:
        predicted=counts_by_formula(q,m)
        observed=counts_by_generators(q,m)
        assert observed[:2]==predicted,(q,m,observed,predicted)
        hist=predicted_histogram(q,m)
        assert observed[2]==hist,(q,m,observed[2],hist)
        print('PASS', 'q=',q,'m=',m,'|Aut|=',observed[0], '|FPF|=',observed[1], 'fixed-space:',hist)
    # The field-order dichotomy is tested independently by enumerating orders.
    for q in (2,3,4,5,7,11,13,17):
        for m in range(3,19):
            _,count=counts_by_formula(q,m)
            Q=q-1
            composite=any(1<d<Q and Q%d==0 for d in range(2,Q))
            assert (count>0)==(Q>m or composite),(q,m,count)
    print('VERIFY_OK: independent generator enumeration and field-order threshold')

if __name__=='__main__':verify()
