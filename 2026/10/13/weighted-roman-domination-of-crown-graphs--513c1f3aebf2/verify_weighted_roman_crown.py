#!/usr/bin/env python3
from itertools import product, combinations
import random

def formula(alpha,beta):
    n=len(alpha); A=sum(alpha); B=sum(beta)
    PA=min(alpha[i]+alpha[j] for i,j in combinations(range(n),2))
    PB=min(beta[i]+beta[j] for i,j in combinations(range(n),2))
    c20=A+PA
    c02=B+PB
    c11=min(2*alpha[i]+2*beta[j]+(0 if i==j else alpha[j]+beta[i]) for i in range(n) for j in range(n))
    c21=min(2*alpha[i]+2*alpha[j]+2*beta[k]+(0 if k in (i,j) else alpha[k]) for i,j in combinations(range(n),2) for k in range(n))
    c12=min(2*beta[i]+2*beta[j]+2*alpha[k]+(0 if k in (i,j) else beta[k]) for i,j in combinations(range(n),2) for k in range(n))
    c22=2*(PA+PB)
    return min(c20,c02,c11,c21,c12,c22)

def brute(alpha,beta):
    n=len(alpha); best=None
    for lab in product((0,1,2), repeat=2*n):
        ok=True
        for i in range(n):
            if lab[i]==0 and not any(lab[n+j]==2 for j in range(n) if j!=i): ok=False; break
            if lab[n+i]==0 and not any(lab[j]==2 for j in range(n) if j!=i): ok=False; break
        if ok:
            cost=sum(lab[i]*alpha[i] for i in range(n))+sum(lab[n+i]*beta[i] for i in range(n))
            best=cost if best is None or cost<best else best
    return best

checks=0
for weights in product((1,2,3), repeat=6):
    a=weights[:3]; b=weights[3:]
    assert formula(a,b)==brute(a,b), (a,b,formula(a,b),brute(a,b))
    checks+=1

rng=random.Random(20261005)
for n,count in [(4,80),(5,40)]:
    for _ in range(count):
        a=[rng.randint(1,17) for _ in range(n)]
        b=[rng.randint(1,17) for _ in range(n)]
        assert formula(a,b)==brute(a,b), (n,a,b,formula(a,b),brute(a,b))
        checks+=1

special=[
 ([1,1,20,20],[20,20,1,1]),
 ([1,2,20,20],[1,20,20,20]),
 ([1,20,20,20],[1,2,20,20]),
]
for a,b in special:
    assert formula(a,b)==brute(a,b), (a,b)
    checks+=1
print(f'ALL CHECKS PASSED; weight_profiles={checks}; exhaustive_Cr3=729; deterministic_Cr4=80; deterministic_Cr5=40')
