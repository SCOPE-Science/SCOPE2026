#!/usr/bin/env python3
"""Exact independent checks of a seven-sign, cubic Walsh fourth moment bound."""
from itertools import combinations, product
from fractions import Fraction

n=7
triples=list(combinations(range(n),3))
N=len(triples)
assert N==35
masks=[sum(1<<v for v in s) for s in triples]
by_mask={m:i for i,m in enumerate(masks)}
counts={2:0,4:0,6:0}
quad=set()
A=[[0]*N for _ in range(N)]
for i,j in combinations(range(N),2):
    d=(masks[i]^masks[j]).bit_count()
    counts[d]+=1
    if len(set(triples[i])&set(triples[j]))==1:
        A[i][j]=A[j][i]=1
    mates=[]
    for k,l in combinations(range(N),2):
        if masks[k]^masks[l]==masks[i]^masks[j]:
            mates.append((k,l))
            if len({i,j,k,l})==4:
                quad.add(tuple(sorted((i,j,k,l))))
    assert len(mates)=={2:10,4:9,6:10}[d]
assert counts=={2:210,4:315,6:70},counts
assert len(quad)==840
assert all(sum(A[i])==18 for i in range(N))
for i in range(N):
    for j in range(N):
        assert sum(A[i][k]*A[k][j] for k in range(N))==9*(i==j)+9
# Moment via a 128-row exact Walsh evaluation and combinatorial formula.
w=[]
for signs in product((-1,1),repeat=7):
    w.append([prod for prod in (int(__import__('math').prod(signs[i] for i in S)) for S in triples)])
assert len(w)==128
for a in ([1]*N,
          [int(i%3==0)-int(i%3==1) for i in range(N)],
          [i-17 for i in range(N)],
          [1 if i==0 else 0 for i in range(N)]):
    B=sum(ai*ai for ai in a)
    brute=sum(sum(ai*wi for ai,wi in zip(a,row))**4 for row in w)//128
    assert brute*128==sum(sum(ai*wi for ai,wi in zip(a,row))**4 for row in w)
    alg=3*B*B-2*sum(ai**4 for ai in a)+24*sum(a[i]*a[j]*a[k]*a[l] for i,j,k,l in quad)
    assert alg==brute, (alg,brute)
    z=[Fraction(ai*ai,1)-Fraction(B,35) for ai in a]
    stab=Fraction(97,5)*B*B-14*sum(t*t for t in z)
    assert Fraction(alg,1)<=stab
assert Fraction(sum(sum(row)**4 for row in w),128*35**2)==Fraction(97,5)
print('VERIFY_OK 35 triples, 840 zero-XOR quadruples, A^2=9(I+J), exact moments and stability')
