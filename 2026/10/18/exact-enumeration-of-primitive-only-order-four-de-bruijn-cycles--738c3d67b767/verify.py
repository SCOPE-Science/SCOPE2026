#!/usr/bin/env python3
"""Exact checks of primitive length-four de Bruijn cycle enumeration."""
from itertools import product
from math import factorial
from fractions import Fraction


def exact_determinant(a):
    # Fraction-free Bareiss elimination on integer matrix.
    a=[list(map(int,row)) for row in a]
    n=len(a)
    old=1
    sign=1
    for k in range(n-1):
        if a[k][k]==0:
            r=next((r for r in range(k+1,n) if a[r][k]),None)
            if r is None:return 0
            a[k],a[r]=a[r],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            aik=a[i][k]
            for j in range(k+1,n):
                num=a[i][j]*pivot - aik*a[k][j]
                assert num%old == 0
                a[i][j]=num//old
            a[i][k]=0
        old=pivot
    return sign*a[-1][-1]


def laplacian(q,primitive):
    vertices=list(product(range(q),repeat=3))
    index={v:i for i,v in enumerate(vertices)}
    N=len(vertices)
    L=[[0]*N for _ in range(N)]
    degrees=[]
    for u in vertices:
        i=index[u];d=0
        for symbol in range(q):
            word=(*u,symbol)
            if primitive and word[0]==word[2] and word[1]==word[3]:
                continue
            j=index[word[1:]]
            L[i][i]+=1;L[i][j]-=1;d+=1
        degrees.append(d)
    return L,degrees


def predicted(q):
    assert q>=2
    m=(q-1)*(q-2)//2
    numerator=factorial(q)**(q**3) * ((q-1)**2+1)**m
    denominator=q**(q*q-q+4) * (q-1)**(q*q-2*q+2)
    assert numerator%denominator == 0
    return numerator//denominator


def check_det(q):
    full,df=laplacian(q,False)
    prim,dp=laplacian(q,True)
    tf=exact_determinant([row[:-1] for row in full[:-1]])
    tp=exact_determinant([row[:-1] for row in prim[:-1]])
    assert tf==q**(q**3-4)
    R=(Fraction((q-1)**2,q*q)**(q-1)
       *Fraction((q-1)**2+1,q*q)**((q-1)*(q-2)//2))
    assert Fraction(tp,tf)==R
    best=tp
    for d in dp:
        best*=factorial(d-1)
    assert best==predicted(q)
    return (q,tf,tp,R,best)


def check_bruteforce_binary():
    q=2
    required={w for w in product(range(q),repeat=4)
              if not (w[0]==w[2] and w[1]==w[3])}
    N=len(required)
    reps=[]
    for number in range(1<<N):
        bits=tuple((number>>i)&1 for i in range(N))
        rot=[bits[i:]+bits[:i] for i in range(N)]
        if bits!=min(rot):continue
        factors=[tuple(bits[(i+j)%N] for j in range(4)) for i in range(N)]
        if len(set(factors))==N and set(factors)==required:
            reps.append(''.join(map(str,bits)))
    assert len(reps)==predicted(2)==4
    return reps


def check_incidence(q):
    # Independently compute the small determinant in the matrix determinant lemma.
    edges=[(a,b) for a in range(q) for b in range(a+1,q)]
    m=len(edges)
    K=[]
    for a,b in edges:
        row=[]
        for c,d in edges:
            dot=int(a==c)-int(a==d)-int(b==c)+int(b==d)
            val=Fraction(2*(q-1),q*q)*int((a,b)==(c,d))+Fraction(dot,q**3)
            row.append(Fraction(int((a,b)==(c,d)))-val)
        K.append(row)
    scale=q**3
    raw=[[int(scale*x) for x in row] for row in K]
    det=Fraction(exact_determinant(raw),scale**m)
    target=(Fraction((q-1)**2,q*q)**(q-1)
            *Fraction((q-1)**2+1,q*q)**((q-1)*(q-2)//2))
    assert det==target
    return (q,det)

if __name__=='__main__':
    for q in (2,3): print('DIRECT_MATRIX_TREE',check_det(q))
    for q in range(2,9): print('LOW_RANK_DETERMINANT',check_incidence(q))
    print('BINARY_CYCLIC_CLASSES',check_bruteforce_binary())
    print('ALL_CHECKS_PASS')
