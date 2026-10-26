#!/usr/bin/env python3
"""Exact projective counts and smoothness certificate for a diagonal K3 over F5.
No third-party dependencies; F25 uses t^2=2 over F5.
"""
from itertools import combinations, product
from collections import Counter
P=5
A=[[1,0,0,1,-3,3], [0,1,0,-3,1,-3], [0,0,1,3,-3,1]]

def determinant_3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

minors=[determinant_3([[A[i][j] for j in ix] for i in range(3)])%5
        for ix in combinations(range(6),3)]
assert len(minors)==20 and all(x!=0 for x in minors), minors

def add(a,b):return (a%5+b%5)%5+5*((a//5+b//5)%5)
def minus(a):return (-a%5)+5*((-(a//5))%5)
def times(a,b):
    x,y=a%5,a//5
    u,v=b%5,b//5
    return ((x*u+2*y*v)%5)+5*((x*v+y*u)%5)
def scalar(a,k):return times(a,k%5)

def basepoints(q):
    for ix in range(3):
        for tail in product(range(q),repeat=2-ix):
            yield [0]*ix+[1]+list(tail)

def count_by_squares(q):
    squares={times(a,a) for a in range(q)}
    assert len(squares)==(q+1)//2
    counts=Counter()
    for aa,bb,cc in basepoints(q):
        yy=[add(add(minus(aa),scalar(bb,3)),minus(scalar(cc,3))),
            add(add(scalar(aa,3),minus(bb)),scalar(cc,3)),
            add(add(minus(scalar(aa,3)),scalar(bb,3)),minus(cc)),
            aa,bb,cc]
        nz=[u for u in yy if u!=0]
        if all(u in squares for u in nz) or all(u not in squares for u in nz):
            counts[len(nz)]+=1
    return sum(cnt*2**(num-1) for num,cnt in counts.items()),dict(sorted(counts.items()))

assert count_by_squares(5)==(96,{5:6}),count_by_squares(5)
assert count_by_squares(25)==(1176,{4:15,5:6,6:30}),count_by_squares(25)

# Separate direct projective enumeration (no character reduction) over F5.
direct=0
for i in range(6):
    for suffix in product(range(5),repeat=5-i):
        xx=[0]*i+[1]+list(suffix)
        yy=[v*v%5 for v in xx]
        if all(sum(A[row][col]*yy[col] for col in range(6))%5==0 for row in range(3)):
            direct+=1
assert direct==96,direct

n1,n2=96,1176
s1=n1-1-5*5
s2=n2-1-25*25
assert s1==70 and s2==22*25
plus=(22+s1//5)//2
minus_count=22-plus
assert (plus,minus_count)==(18,4)
print('20 nonzero maximal Jacobian-support minors:',len(minors))
print('F5 square-cover distribution:',count_by_squares(5))
print('F25 square-cover distribution:',count_by_squares(25))
print('F5 direct independent projective count:',direct)
print('H2 Frobenius multiplicities +5,-5:',plus,minus_count)
print('VERIFY_OK')
