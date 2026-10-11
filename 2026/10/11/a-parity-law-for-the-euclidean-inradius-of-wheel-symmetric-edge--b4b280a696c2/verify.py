#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

def expected(m):
    if m % 2 == 0:
        return Fraction(m-2, 1), m
    return Fraction(m*m-m-3, m+1), 2*m

def norm2(word):
    m=len(word)
    s=sum(word)
    return Fraction(sum(x*x for x in word),1)-Fraction(s*s,m+1)

def admissible(word):
    m=len(word)
    for i in range(m):
        a=word[i]
        b=word[(i+1)%m]
        if abs(a-b)>1:
            return False
    return True

def facet_word(word):
    if not admissible(word):
        return False
    m=len(word)
    for i in range(m):
        if word[i]==word[(i+1)%m]==word[(i+2)%m]==0:
            return False
    return True

def block_signature(word):
    m=len(word)
    nz=sum(x!=0 for x in word)
    z=m-nz
    if z!=2:
        return False
    p=sum(x==1 for x in word)
    q=sum(x==-1 for x in word)
    if p==0 or q==0:
        return False
    changes=0
    for i in range(m):
        if word[i]==0:
            left=word[(i-1)%m]
            right=word[(i+1)%m]
            if left*right==-1:
                changes+=1
    return changes==2

total=0
for m in range(5,12):
    best=None
    maximizers=[]
    for word in product((-1,0,1), repeat=m):
        if not admissible(word):
            continue
        q=norm2(word)
        if best is None or q>best:
            best=q
            maximizers=[word]
        elif q==best:
            maximizers.append(word)
    exp,count=expected(m)
    assert best==exp, (m,best,exp)
    assert len(maximizers)==count, (m,len(maximizers),count)
    assert all(facet_word(w) for w in maximizers)
    assert all(block_signature(w) for w in maximizers)
    total += len(maximizers)

print(f"VERIFY_OK wheel-sep-inradius m=5..11 maximizing_words={total} exact_rational=yes")
