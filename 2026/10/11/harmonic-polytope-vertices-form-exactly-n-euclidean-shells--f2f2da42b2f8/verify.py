#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from math import factorial
from collections import Counter

def is_fine_harmonic(n,k,p1,p2):
    pos1={v:i+1 for i,v in enumerate(p1)}
    pos2={v:i+1 for i,v in enumerate(p2)}
    for j in range(n):
        if j==k:
            continue
        if pos1[j]>pos1[k] and not pos2[j]<pos2[k]:
            return False
        if pos2[j]>pos2[k] and not pos1[j]<pos1[k]:
            return False
    return True

def shell_formula(n,b):
    return Fraction(n*(n*n-1),6)+Fraction(2*(n-1),n)+2*b

def multiplicity_formula(n,b):
    return factorial(n)//factorial(b)*sum(
        factorial(r)*factorial(n+b-1-r)
        for r in range(b,n)
    )

for n in range(2,6):
    counts=Counter()
    outer_sum=[Fraction(0) for _ in range(2*n)]
    outer_count=0
    total=0
    mu=Fraction(n+1,2)+Fraction(1,n)

    perms=list(permutations(range(n)))
    for k in range(n):
        for p1 in perms:
            pos1=p1.index(k)+1
            for p2 in perms:
                if not is_fine_harmonic(n,k,p1,p2):
                    continue
                pos2=p2.index(k)+1
                b=pos1+pos2-n-1
                assert 0<=b<=n-1

                x=[Fraction(p1.index(i)+1) for i in range(n)]
                y=[Fraction(p2.index(i)+1) for i in range(n)]
                x[k]+=1
                y[k]+=1
                v=x+y
                d2=sum((z-mu)**2 for z in v)
                assert d2==shell_formula(n,b)

                counts[b]+=1
                total+=1
                if b==n-1:
                    outer_count+=1
                    for i,z in enumerate(v):
                        outer_sum[i]+=z

    for b in range(n):
        assert counts[b]==multiplicity_formula(n,b),(n,b,counts[b],multiplicity_formula(n,b))

    source_total=factorial(n)**2*sum(Fraction(1,j) for j in range(1,n+1))
    assert total==source_total
    assert outer_count==n*factorial(n-1)**2
    assert all(z/outer_count==mu for z in outer_sum)

    R2=shell_formula(n,n-1)
    closed=Fraction((n*n-1)*(n*n+12),6*n)
    assert R2==closed

print("VERIFY_OK harmonic-polytope-shells n=2..5 exact=yes")
