#!/usr/bin/env python3
from itertools import combinations, permutations
from math import gcd

A=((0,1,0,0),(0,0,1,0),(0,0,0,1),(-1,65,-126,64))
B=((2,11,0,0),(0,0,1,0),(0,0,0,1),(11,61,-2,62))
EXPECTED={
1:((1,1,1,1),(1,1,1,1)),
2:((1,1,1,257),(1,1,1,257)),
3:((1,1,1,35911),(1,1,1,35911)),
4:((1,1,1,3951889),(1,1,1,3951889)),
5:((1,1,1,381168971),(1,1,1,381168971)),
6:((1,1,1,33787833947),(1,1,1,33787833947)),
7:((1,1,1,2823000025693),(1,1,1,2823000025693)),
8:((1,1,1,225691499518753),(1,1,1,225691499518753)),
9:((1,1,1,17433664684009219),(1,1,1,17433664684009219)),
10:((1,1,1,1309791722987654687),(1,1,11,119071974817059517)),
}

def mul(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(4)) for j in range(4)) for i in range(4))
def power(X,n):
    R=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
    while n:
        if n&1: R=mul(R,X)
        X=mul(X,X); n//=2
    return R
def det(M):
    n=len(M); total=0
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        z=1
        for i,j in enumerate(p): z*=M[i][j]
        total += -z if inv&1 else z
    return total
def invariants(M):
    delta=[1]
    for k in range(1,5):
        g=0
        for rs in combinations(range(4),k):
            for cs in combinations(range(4),k):
                m=tuple(tuple(M[i][j] for j in cs) for i in rs)
                g=gcd(g,abs(det(m)))
        delta.append(g)
    return tuple(delta[i]//delta[i-1] for i in range(1,5))
def calc(X,d):
    P=power(X,d)
    return invariants(tuple(tuple(P[i][j]-int(i==j) for j in range(4)) for i in range(4)))

first=None
for d in range(1,11):
    got=(calc(A,d),calc(B,d))
    assert got==EXPECTED[d], (d,got,EXPECTED[d])
    if got[0]!=got[1] and first is None: first=d
assert first==10
assert 11*119071974817059517==1309791722987654687
print('VERIFY_OK first_difference=10 d1_9_match=true d10_A=(1,1,1,1309791722987654687) d10_B=(1,1,11,119071974817059517) equal_torsion_order=true')
