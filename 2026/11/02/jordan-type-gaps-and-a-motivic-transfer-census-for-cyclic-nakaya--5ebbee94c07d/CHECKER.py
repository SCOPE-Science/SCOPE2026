#!/usr/bin/env python3
"""Independent finite-field checks of regular multiplication Jordan types.
Run using Python 3 standard library. No external packages are required.
"""
from itertools import product
from collections import Counter

# Fields: q = prime p, or GF(4)=F2[t]/(t^2+t+1).
def mul(a,b,q):
    if q == 4:
        c=0
        for i in range(2):
            if (b>>i)&1: c^=(a<<i)
        if c&8: c^=0b1100 # unused for degree <=2
        if c&4: c^=0b111
        return c
    return (a*b)%q

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def inv(a,q):
    for b in range(1,q):
        if mul(a,b,q)==1:return b
    raise ValueError('not invertible')

def rank(A,q):
    m=[list(row) for row in A]
    if not m:return 0
    h=len(m);w=len(m[0]);p=0
    for j in range(w):
        k=next((k for k in range(p,h) if m[k][j]),None)
        if k is None:continue
        m[p],m[k]=m[k],m[p]
        v=inv(m[p][j],q)
        m[p]=[mul(v,z,q) for z in m[p]]
        for i in range(h):
            if i==p or not m[i][j]:continue
            z=m[i][j]
            m[i]=[add(m[i][l],(mul(z,m[p][l],q) if q==4 else -mul(z,m[p][l],q)),q) for l in range(w)]
        p+=1
        if p==h:break
    return p

def matmul(A,B,q):
    d=len(A)
    C=[[0]*d for _ in range(d)]
    for i in range(d):
        for k in range(d):
            if A[i][k]:
                for j in range(d):
                    if B[k][j]:
                        C[i][j]=add(C[i][j],mul(A[i][k],B[k][j],q),q)
    return C

def multiplication_matrices(n,a,b,q):
    """Paths: (start,length) in a directed n-cycle, length 0,1,2."""
    d=3*n
    L=[[0]*d for _ in range(d)]
    R=[[0]*d for _ in range(d)]
    # Index of path (start,length) = 3*start+length.
    for s in range(n):
        for ell in range(3):
            j=3*s+ell
            # left multiply: path starting at s-1 or s-2,
            # ending at starting vertex s.
            if ell<=1:
                h=(s-1)%n
                L[3*h+(ell+1)][j]=a[h]
            if ell==0:
                h=(s-2)%n
                L[3*h+2][j]=b[h]
            # right multiply: x paths starting at ending vertex s+ell.
            end=(s+ell)%n
            if ell<=1:
                R[3*s+(ell+1)][j]=a[end]
            if ell==0:
                R[3*s+2][j]=b[end]
    return L,R

def poly_add(a,b):
    c=Counter(a)
    for key,val in b.items():
        c[key]+=val
    return c

def poly_mul(a,b):
    c=Counter()
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            c[(i+k,j+l)]+=x*y
    return c

def transfer_counts(n,q):
    """Compute trace(M^n) directly in the bivariate integer polynomial ring."""
    # Indices are (power of U, power of V).
    M=[[{(0,0):q-1,(0,1):1},{(0,0):q*(q-1)}],
       [{(0,0):q},{(1,0):q*(q-1)}]]
    E=[[{(0,0):int(i==j)} for j in range(2)] for i in range(2)]
    for _ in range(n):
        E=[[poly_add(poly_mul(E[i][0],M[0][j]),poly_mul(E[i][1],M[1][j])) for j in range(2)] for i in range(2)]
    return poly_add(E[0][0],E[1][1])

def run_case(n,q):
    got=Counter()
    for vals in product(range(q),repeat=2*n):
        a=vals[:n];b=vals[n:]
        L,R=multiplication_matrices(n,a,b,q)
        rL=rank(L,q);rR=rank(R,q)
        r2L=rank(matmul(L,L,q),q)
        r2R=rank(matmul(R,R,q),q)
        t=sum(a[i]!=0 and a[(i+1)%n]!=0 for i in range(n))
        z=sum(a[i]==a[(i+1)%n]==b[i]==0 for i in range(n))
        pred_r1=n+t-z
        assert (rL,rR,r2L,r2R)==(pred_r1,pred_r1,t,t),(n,q,a,b,rL,rR,r2L,r2R,pred_r1,t,z)
        got[(t,z)]+=1
    expected=transfer_counts(n,q)
    assert got==expected,(n,q,got-expected,expected-got)
    assert sum(got.values())==q**(2*n)
    absent=n-1 not in {t for t,z in got}
    assert absent
    assert len(got)==n*(n-1)//2+3
    return len(got),len(list(product(range(q),repeat=2*n)))

if __name__=='__main__':
    cases=[(3,2),(4,2),(5,2),(6,2),(3,3),(4,3),(3,4),(3,5)]
    print('case n q jordan_types radical_elements')
    for n,q in cases:
        kinds,num=run_case(n,q)
        print(n,q,kinds,num)
    print('NAKAYAMA_LOEWY3_REGULAR_JORDAN_OK',len(cases))
