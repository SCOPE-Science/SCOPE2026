"""Exact finite checks of permuted binary neighbor-XOR dynamics."""
from itertools import permutations
from random import Random

def rank(cols):
    piv={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k in piv: v^=piv[k]
            else: piv[k]=v;break
    return len(piv)

def action(v,n,p):
    y=0
    for i in range(n):
        y|=(((v>>((i-1)%n))^(v>>((i+1)%n)))&1)<<i
    z=0
    for i,j in enumerate(p):
        z|=((y>>j)&1)<<i
    return z

def check(n,p):
    cols=[action(1<<j,n,p) for j in range(n)]
    cols2=[action(c,n,p) for c in cols]
    a=rank(cols)
    b=rank(cols2)
    if n%2: assert(a,b)==(n-1,n-1),(n,p,a,b)
    elif n%4==2: assert(a,b)==(n-2,n-2),(n,p,a,b)
    else:
        E={j for j in range(n) if j%2==0}
        q=sum((p[i] in E) for i in E)%2
        assert(a,b)==(n-2,n-3 if q else n-4),(n,p,q,a,b)

cases=0
for n in range(3,9):
    for p in permutations(range(n)):
        check(n,p);cases+=1
print('exhaustive',cases)
rng=Random(0xC0FFEE)
for n in range(9,37):
    for k in range(100):
        p=list(range(n));rng.shuffle(p)
        check(n,p);cases+=1
    for r in range(1,n+1):
        p=list(range(n))
        if r>1:p[:r]=[r-1]+list(range(r-1))
        check(n,p);cases+=1
print('VERIFY_OK matrix_permutation_cases=',cases)
