"""Exact enumeration of all abelian subspaces in finite graph Lie algebras.

Run: python3 verify_abelian.py
The exhaustive tests cover only listed prime fields; the mathematical proof
covers every field and the finite-field formulas cover every prime power.
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def gaussian(n,k,q):
    if k<0 or k>n: return 0
    k=min(k,n-k)
    return prod(q**(n-i)-1 for i in range(k)) // prod(q**(k-i)-1 for i in range(k))


def predicted(a,b,q):
    h=a*b
    n=a+b+h
    out=[0]*(n+1)
    mixed=(q**a-1)*(q**b-1)//(q-1)
    for t in range(0, max(a,b)+1):
        weight = (gaussian(a,t,q) if t>=1 else 1) + (gaussian(b,t,q) if t>=1 else 0)
        if t == 1: weight+=mixed
        if not weight: continue
        for j in range(0,h+1):
            out[t+j] += weight * gaussian(h,j,q)*q**(t*(h-j))
    return out


def rref_subspaces(n,d,p):
    # Exactly one RREF basis matrix for every subspace.
    for pivots in combinations(range(n),d):
        free=[(i,j) for i in range(d) for j in range(pivots[i]+1,n) if j not in pivots]
        for vals in product(range(p),repeat=len(free)):
            basis=[[int(j==pivots[i]) for j in range(n)] for i in range(d)]
            for (i,j),v in zip(free,vals): basis[i][j]=v
            yield basis


def abelian(basis,a,b,p):
    for i in range(len(basis)):
        x=basis[i]
        for j in range(i):
            y=basis[j]
            for s in range(a):
                for t in range(b):
                    if (x[s]*y[a+t]-y[s]*x[a+t])%p:
                        return False
    return True


def rowspace_included(left,right,p):
    # Containment tested by row-space rank, without using the classification.
    width=len(left[0]) if left else len(right[0]) if right else 0
    def rank(rows):
        M=[v[:] for v in rows]
        r=0
        for j in range(width):
            t=next((i for i in range(r,len(M)) if M[i][j]%p),None)
            if t is None: continue
            M[t],M[r]=M[r],M[t]
            c=pow(M[r][j],-1,p)
            M[r]=[(x*c)%p for x in M[r]]
            for i in range(len(M)):
                if i!=r and M[i][j]:
                    c=M[i][j]
                    M[i]=[(x-c*y)%p for x,y in zip(M[i],M[r])]
            r+=1
        return r
    return rank(right+left)==len(right)


def check_maximals(a,b,p):
    h=a+b
    good=[]
    for d in range(h+1):
        for B in rref_subspaces(h,d,p):
            if abelian(B,a,b,p):good.append(B)
    maximal=[]
    for B in good:
        if not any(len(C)>len(B) and rowspace_included(B,C,p) for C in good):
            maximal.append(B)
    expected=2+(p**a-1)*(p**b-1)//(p-1)
    dims=Counter(len(B)+a*b for B in maximal)
    assert len(maximal)==expected,(a,b,p,len(maximal),expected)
    assert dims[a*b+a] >= 1 and dims[a*b+b] >= 1
    assert sum(dims.values())==expected
    print('maximal',a,b,p,'OK',dict(dims))


def check(a,b,p):
    n=a+b+a*b
    expected=predicted(a,b,p)
    observed=[]
    for d in range(n+1):
        actual=sum(abelian(B,a,b,p) for B in rref_subspaces(n,d,p))
        observed.append(actual)
        assert actual==expected[d],(a,b,p,d,actual,expected[d])
    max_abelian=max(i for i,c in enumerate(observed) if c)
    assert max_abelian == a*b+max(a,b)
    print('case',a,b,p,'OK',observed)
    check_maximals(a,b,p)


if __name__=='__main__':
    for p in (2,3,5): check(1,1,p)
    for p in (2,3): check(1,2,p)
    check(2,2,2)
    print('VERIFY_OK')
