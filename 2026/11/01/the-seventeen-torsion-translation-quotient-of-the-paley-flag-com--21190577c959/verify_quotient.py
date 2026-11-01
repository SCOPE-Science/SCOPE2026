#!/usr/bin/env python3
"""Exact orbit-cell reconstruction for the Paley-17 flag complex quotient."""
from itertools import combinations
from collections import Counter
p=17
Q={pow(i,2,p) for i in range(1,p)}
assert Q=={1,2,4,8,9,13,15,16}
def edge(a,b):return (b-a)%p in Q
faces={r:{x for x in combinations(range(p),r) if all(edge(a,b) for a,b in combinations(x,2))} for r in (1,2,3,4)}
assert [len(faces[r]) for r in (1,2,3,4)]==[17,68,68,0]
def shift(f,k):return tuple(sorted((v+k)%p for v in f))
def orbit(f):return {shift(f,k) for k in range(p)}
def partition(r):
    remain=set(faces[r]); groups=[]
    while remain:
        f=min(remain); o=orbit(f);assert len(o)==17 and o<=remain; remain-=o;groups.append(o)
    return groups
assert [len(partition(r)) for r in (1,2,3)]==[1,4,4]
edgereps=[(0,s) for s in (1,2,4,8)]
trianglereps=[(0,1,2),(0,2,4),(0,4,8),(0,1,9)]
assert all(f in faces[3] for f in trianglereps)
assert {tuple(sorted(f)) for o in [orbit(t) for t in trianglereps] for f in o} ==faces[3]
assert len(set().union(*[orbit(t) for t in trianglereps]))==68
steps=(1,2,4,8)
def edge_letter(a,b):
    d=(b-a)%p
    for s in steps:
        if d==s:return (s,1)
        if d==(p-s)%p:return (s,-1)
    raise ValueError((a,b,d))
words=[]
for a,b,c in trianglereps:
    words.append((edge_letter(a,b),edge_letter(b,c),edge_letter(c,a)))
assert words == [((1,1),(1,1),(2,-1)),((2,1),(2,1),(4,-1)),((4,1),(4,1),(8,-1)),((1,1),(8,1),(8,1))]
# Abelian cellular boundary: first 3 relators express x2=2*x1, x4=2*x2, x8=2*x4; fourth has coefficient 17.
coefs={1:1,2:2,4:4,8:8}
assert [sum(e*coefs[s] for s,e in word) for word in words]==[0,0,0,17]
# Cellular boundary determinant yields |H1|=17 and H2=0, independent of noncommutative reduction.
from itertools import permutations
B=[[sum(e for s,e in w if s==step) for w in words] for step in steps]
def sign(z):return (-1)**sum(z[i]>z[j] for i in range(4) for j in range(i+1,4))
det=sum(sign(z)*__import__("math").prod(B[i][z[i]] for i in range(4)) for z in permutations(range(4)))
assert det in (17,-17)
print('P17 flag face counts:',[len(faces[r]) for r in (1,2,3,4)])
print('C17 cell orbit counts:',[len(partition(r)) for r in (1,2,3)])
print('Triangle relator words:',words)
print('Cellular boundary determinant:',det)
print('Final attaching exponent:',sum(e*coefs[s] for s,e in words[3]))
print('H1 quotient = Z/17; H2 quotient = 0; universal-cover H2 = augmentation ideal of Z[C17]')
print('VERIFY_OK')
