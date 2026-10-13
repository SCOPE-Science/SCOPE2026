#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction


def admissible(L,t,v):
    return t>=0 and v>=0 and t+v<=L and 2*t+v<L and 2*v<L


def signatures(L):
    return [(t,v) for t in range(L+1) for v in range(L-t+1) if admissible(L,t,v)]


def fnum(L,t,v):
    # K2P = -1/4 log(F/L^3); comparison uses the positive integer F exactly.
    return (L-2*t-v)**2*(L-2*v)


def sgn(x):
    return (x>0)-(x<0)


def cmp_p(a,b):
    return sgn((a[0]+a[1])-(b[0]+b[1]))


def cmp_k(L,a,b):
    # K is decreasing in F.
    return -sgn(fnum(L,*a)-fnum(L,*b))

weak={}; strict={}
for L in range(1,10):
    weak[L]=[]; strict[L]=[]
    pts=signatures(L)
    for a,b in combinations(pts,2):
        cp=cmp_p(a,b); ck=cmp_k(L,a,b)
        if cp!=ck:
            weak[L].append((a,b))
        if cp*ck<0:
            strict[L].append((a,b))

assert all(not strict[L] for L in range(1,9))
assert strict[9]==[((2,3),(4,0))]
assert all(not weak[L] for L in range(1,3))
assert weak[3]==[((0,1),(1,0))]

A=(2,3); B=(4,0); L=9
assert Fraction(sum(A),L)==Fraction(5,9)
assert Fraction(sum(B),L)==Fraction(4,9)
assert fnum(L,*A)==12
assert fnum(L,*B)==9
assert cmp_p(A,B)>0 and cmp_k(L,A,B)<0

# Explicit common-reference realization.
R='A'*9
X='GGCCCAAAA'  # 2 A<->G transitions, 3 A<->C transversions
Y='GGGGAAAAA'  # 4 A<->G transitions

def counts(ref,seq):
    transitions={frozenset(('A','G')),frozenset(('C','T'))}
    t=v=0
    for a,b in zip(ref,seq):
        if a==b: continue
        if frozenset((a,b)) in transitions: t+=1
        else: v+=1
    return t,v
assert counts(R,X)==A
assert counts(R,Y)==B

print('VERIFY_OK')
print('first_weak_length',3,weak[3])
print('first_strict_length',9,strict[9])
print('witness_F',fnum(9,*A),fnum(9,*B))
print('witness_p',Fraction(5,9),Fraction(4,9))
