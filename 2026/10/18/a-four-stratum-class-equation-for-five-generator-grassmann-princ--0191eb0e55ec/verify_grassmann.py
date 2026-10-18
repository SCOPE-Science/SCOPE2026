#!/usr/bin/env python3
"""Exact and independent finite-field checks for Grassmann principal-unit centralizer strata."""
from itertools import product, combinations
from math import comb
from collections import Counter
import random


def exterior_basis(n, degree):
    return [sum(1<<i for i in c) for c in combinations(range(n),degree)]

def mul_monomial(a,b):
    if a&b:return (0,0)
    inversions=sum(((a>>(j+1)).bit_count()) for j in range(5) if (b>>j)&1)
    return (a|b, -1 if inversions%2 else 1)

def rank_mod(A,q):
    A=[[x%q for x in row] for row in A]
    if not A:return 0
    m=len(A);n=len(A[0]);r=0
    for j in range(n):
        piv=next((i for i in range(r,m) if A[i][j]),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][j],-1,q)
        A[r]=[(v*inv)%q for v in A[r]]
        for i in range(r+1,m):
            if A[i][j]:
                scale=A[i][j]
                A[i]=[(u-scale*v)%q for u,v in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def multiplication_rank_odd(coeffs,n,q):
    odds=[m for m in range(1<<n) if m.bit_count()%2]
    evens=[m for m in range(1<<n) if m.bit_count()%2==0 and m>0]
    rows={m:i for i,m in enumerate(evens)}
    M=[[0]*len(odds) for _ in evens]
    for i,c in coeffs.items():
        for col,j in enumerate(odds):
            k,s=mul_monomial(i,j)
            if s:M[rows[k]][col]+=c*s
    return rank_mod(M,q)

def threeform_rank(coeffs,n,q):
    vec=exterior_basis(n,1);out=exterior_basis(n,4)
    rows={m:i for i,m in enumerate(out)}
    M=[[0]*len(vec) for _ in out]
    for i,c in coeffs.items():
        for col,j in enumerate(vec):
            k,s=mul_monomial(i,j)
            if s:M[rows[k]][col]+=c*s
    return rank_mod(M,q)

def gauss(n,r,q):
    # Exact Gaussian binomial coefficient by numerator/denominator products.
    num=den=1
    for j in range(r):
        num*=q**(n-j)-1
        den*=q**(r-j)-1
    return num//den

def test_q3_trivectors():
    q=3;n=5;basis=exterior_basis(n,3)
    observed=Counter()
    for values in product(range(q),repeat=len(basis)):
        cs={i:v for i,v in zip(basis,values) if v}
        observed[threeform_rank(cs,n,q)]+=1
    N2=(q-1)*gauss(5,3,q)
    expected={0:1,2:N2,4:q**10-1-N2}
    assert dict(observed)==expected, (dict(observed),expected)
    print('TRIVECTOR_EXHAUSTIVE_Q3',dict(observed))

def test_odd_multiplication():
    random.seed(42017)
    q=3;n=5;b1=exterior_basis(n,1);b3=exterior_basis(n,3);b5=exterior_basis(n,5)
    for typ in ('linear','simple','nonsimple','central'):
        for t in range(45):
            coeff={}
            if typ=='linear':
                coeff[b1[t%5]]=1
                for m in b3+b5: coeff[m]=random.randrange(q)
                want=8
            elif typ=='simple':
                coeff[b3[0]]=1
                coeff[b5[0]]=random.randrange(q)
                want=2
            elif typ=='nonsimple':
                coeff[b3[0]]=1
                coeff[b3[-1]]=1
                coeff[b5[0]]=random.randrange(q)
                want=threeform_rank({b3[0]:1,b3[-1]:1},5,3)
                assert want==4
            else:
                coeff[b5[0]]=random.randrange(q)
                want=0
            assert multiplication_rank_odd(coeff,n,q)==want,(typ,t)
    print('ODD_MULTIPLICATION_Q3',4*45,'samples')

def test_full_commutator():
    q=3;n=5;dim=1<<n;nonzero_even=[m for m in range(1,dim) if m.bit_count()%2==0]
    odd=[m for m in range(1,dim) if m.bit_count()%2]
    def multiply(A,B):
        z=[0]*dim
        for i,a in enumerate(A):
            if a:
                for j,b in enumerate(B):
                    if b:
                        k,s=mul_monomial(i,j)
                        if s:z[k]=(z[k]+a*b*s)%q
        return z
    def add(A,B):return [(a+b)%q for a,b in zip(A,B)]
    def pure_odd(s):
        a=[0]*dim;a[0]=1
        for i,v in s.items():a[i]=v
        return a
    random.seed(9293)
    for t in range(80):
        s={i:random.randrange(q) for i in odd};v={i:random.randrange(q) for i in odd}
        x=pure_odd(s); y=pure_odd(v)
        a=[0]*dim;b=[0]*dim
        for i in nonzero_even:
            a[i]=random.randrange(q);b[i]=random.randrange(q)
        a[0]=b[0]=1
        g=multiply(a,x);h=multiply(b,y)
        gh=multiply(g,h);hg=multiply(h,g)
        wedge=multiply(x,y);rev=multiply(y,x)
        # Their equality is precisely vanishing of the alternating odd product
        assert (gh==hg)==(wedge==rev)
        assert (wedge==rev)==all((2*wedge[i])%q==0 for i in range(1,dim))
    print('DIRECT_GROUP_COMMUTATOR_Q3',80,'samples')

def exact_formula(q):
    N2=(q-1)*gauss(5,3,q);N4=q**10-1-N2
    elements={1:q**16,q**2:q**16*N2,q**4:q**16*N4,q**8:q**26*(q**5-1)}
    classes={s:n//s for s,n in elements.items()}
    assert sum(elements.values())==q**31
    assert sum(k*classes[k] for k in classes)==q**31
    assert all(elements[k]==classes[k]*k for k in classes)
    return elements,classes

if __name__=='__main__':
    test_q3_trivectors()
    test_odd_multiplication()
    test_full_commutator()
    for q in (3,5,7,9):
        e,c=exact_formula(q)
        print('CENTRALIZER_FORMULA',q, 'Nclasses',sum(c.values()),'classes',c)
    print('ALL_EXACT_CHECKS_PASSED')
