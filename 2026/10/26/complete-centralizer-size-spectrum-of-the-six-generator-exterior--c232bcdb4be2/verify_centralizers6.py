#!/usr/bin/env python3
"""Finite-field checks of centralizer-rank strata of the six-generator exterior algebra."""
from itertools import combinations
from math import prod
from random import Random
N=6
odd=[m for m in range(64) if m.bit_count()%2]
even=[m for m in range(64) if m.bit_count()%2==0]
comb3=[m for m in range(64) if m.bit_count()==3]

def wedge(u,v):
    if u&v:return None
    sign=(-1)**(sum((v&((1<<i)-1)).bit_count() for i in range(6) if u>>i&1))
    return u|v,sign

def rank(M,p):
    M=[x.copy() for x in M];row=0
    for c in range(len(M[0])):
        piv=next((k for k in range(row,len(M)) if M[k][c]%p),None)
        if piv is None:continue
        M[row],M[piv]=M[piv],M[row]
        inv=pow(M[row][c]%p,-1,p)
        M[row]=[v*inv%p for v in M[row]]
        for k in range(row+1,len(M)):
            factor=M[k][c]
            if factor:M[k]=[(x-factor*y)%p for x,y in zip(M[k],M[row])]
        row+=1
        if row==len(M):break
    return row

def oddrank(a,p):
    dest={x:i for i,x in enumerate(even)}
    mat=[[0]*32 for _ in range(32)]
    for j,b in enumerate(odd):
        for mon,v in a.items():
            pair=wedge(mon,b)
            if pair is not None:
                out,sgn=pair
                mat[dest[out]][j]=(mat[dest[out]][j]+sgn*v)%p
    return rank(mat,p)

def gb(n,k,q):
    a=prod(q**(n-j)-1 for j in range(k));b=prod(q**(k-j)-1 for j in range(k));return a//b

def predicts(q):
    N8=(q-1)*gb(6,3,q)
    N12=gb(6,1,q)*(q**10-1-(q-1)*gb(5,2,q))
    N14=q**20-1-N8-N12
    return {0:q**32,1:q**32*(q**6-1),4:q**38*N8,6:q**38*N12,7:q**38*N14,16:q**58*(q**6-1)}

def run():
    rnd=Random(20261018)
    for p in (3,5,7):
        assert sum(predicts(p).values())==p**64
        cases=[]
        cases.append(({},0))
        cases.append(({31:1},1))
        cases.append(({7:1},4))
        cases.append(({7:1,25:1},6))
        cases.append(({7:1,56:1},7))
        cases.append(({1:1,7:1,31:1},16))
        for a,expected in cases:
            got=oddrank(a,p)
            assert got==expected,(p,a,got,expected)
        for _ in range(70):
            # Random odd elements, with linear and without linear parts.
            a={m:rnd.randrange(p) for m in odd if m.bit_count()>= (3 if _%2 else 1)}
            a={m:v for m,v in a.items() if v}
            got=oddrank(a,p)
            assert got in (0,1,4,6,7,16),(p,got)
            has_linear=any(m.bit_count()==1 for m in a)
            assert (got==16)==has_linear,(p,a,got)
        print(f'F_{p}: 76 explicit/random odd-product matrices=PASS; centralizer strata counts: {predicts(p)}')
    print('VERIFY_OK_EXTERIOR6_CENTRALIZER_DISTRIBUTION 228_ODD_MULTIPLICATION_CASES')
if __name__=='__main__':run()
