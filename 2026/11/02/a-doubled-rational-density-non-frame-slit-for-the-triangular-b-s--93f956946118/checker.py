"""Exact rational checks for the triangular B-spline Gabor fiber identity.
Run with Python: python checker.py
The proof of the continuum statement is analytic and appears in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd


def positive_part(t):
    return max(t, Fraction(0))


def periodized_tent(b, s):
    # theta(s,b) = sum_n (1 - |s+3n|/b)_+
    assert b > 0
    return sum((positive_part(b-abs(s+3*n))/b for n in range(-6,7)), Fraction(0))


def fiber(b):
    return [[periodized_tent(b, Fraction(3*l,4)+k) for l in range(4)] for k in range(3)]


def rank(A):
    R=[r[:] for r in A]
    m=len(R); n=len(R[0]); pivotrow=0
    for j in range(n):
        pivot=next((i for i in range(pivotrow,m) if R[i][j]),None)
        if pivot is None: continue
        R[pivot],R[pivotrow]=R[pivotrow],R[pivot]
        scale=R[pivotrow][j]
        R[pivotrow]=[z/scale for z in R[pivotrow]]
        for i in range(m):
            if i!=pivotrow and R[i][j]:
                c=R[i][j]
                R[i]=[v-c*w for v,w in zip(R[i],R[pivotrow])]
        pivotrow+=1
        if pivotrow==m:break
    return pivotrow


def check(b):
    assert Fraction(11,4)<=b<=Fraction(13,4)
    M=fiber(b)
    C=Fraction(2)-Fraction(3)/b
    C0=Fraction(1) if b<=3 else Fraction(3)-Fraction(6)/b
    target=[[C0,C,C,C],[C]*4,[C]*4]
    assert M==target, (b,M,target)
    assert [M[1][j]-M[2][j] for j in range(4)]==[0]*4
    assert rank(M)==(1 if b==3 else 2)
    assert C0-C==abs(b-3)/b
    return True

if __name__=='__main__':
    bs=[Fraction(11,4)+Fraction(k,800) for k in range(401)]
    for b in bs: check(b)
    for b in [Fraction(11,4),Fraction(23,8),Fraction(3),Fraction(25,8),Fraction(13,4)]:
        check(b)
    for b in [Fraction(21,8),Fraction(27,8)]:
        assert fiber(b)[1]!=fiber(b)[2]
    print('PASS: 406 in-range rational fiber identities and two out-of-range distinctions')
