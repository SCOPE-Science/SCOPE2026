#!/usr/bin/env python3
from itertools import combinations
from fractions import Fraction


def profiles(S):
    out=[]
    for a in range(1,S):
        for b in range(a,S):
            c=S-a-b
            if c < b:
                continue
            out.append((a,b,c))
    return out


def gini_three(x):
    a,b,c=x
    S=a+b+c
    return Fraction(2*(c-a),3*S)


def product_three(x):
    a,b,c=x
    return a*b*c

# Atkinson epsilon=1 is 1 - geometric_mean/arithmetic_mean.
# At fixed positive total S, larger Atkinson means smaller product.

reversal_counts={}
gini_tie_split_counts={}
prod_tie_split_counts={}
first_reversals={}
for S in range(3,12):
    ps=profiles(S)
    rev=[]; gt=[]; pt=[]
    for x,y in combinations(ps,2):
        gx=gini_three(x); gy=gini_three(y)
        px=product_three(x); py=product_three(y)
        # Strict opposite inequality rankings: Gini increases with inequality,
        # Atkinson_1 increases when the fixed-total product decreases.
        if (gx-gy)*(px-py) > 0:
            rev.append((x,y))
        if gx==gy and px!=py:
            gt.append((x,y))
        if px==py and gx!=gy:
            pt.append((x,y))
    reversal_counts[S]=len(rev)
    gini_tie_split_counts[S]=len(gt)
    prod_tie_split_counts[S]=len(pt)
    first_reversals[S]=rev

assert all(reversal_counts[S]==0 for S in range(3,11))
assert reversal_counts[11]==1
assert first_reversals[11]==[((1,5,5),(2,2,7))]
assert all(gini_tie_split_counts[S]==0 for S in range(3,9))
assert gini_tie_split_counts[9]==1
assert prod_tie_split_counts[9]==0

A=(1,5,5); B=(2,2,7)
assert sum(A)==sum(B)==11
assert gini_three(A)==Fraction(8,33)
assert gini_three(B)==Fraction(10,33)
assert product_three(A)==25 < 28==product_three(B)

# First weak-order split at total 9.
C=(1,4,4); D=(2,2,5)
assert sum(C)==sum(D)==9
assert gini_three(C)==gini_three(D)==Fraction(2,9)
assert product_three(C)==16 < 20==product_three(D)

# Two-household symbolic identity check on a large exact grid:
# with total S and gap d=|x2-x1|, product=(S^2-d^2)/4,
# so Gini increases and Atkinson_1 increases with the same d.
for S in range(2,501):
    vals=[]
    for a in range(1,S):
        b=S-a
        if a>b: continue
        d=b-a
        prod=a*b
        vals.append((d,prod))
    for (d1,p1),(d2,p2) in combinations(vals,2):
        assert (d1-d2)*(p1-p2) <= 0

# Three-household continuous ordering reduction replay on integer grids:
# Gini order is the range; Atkinson_1 order is reverse product order.
for S in range(3,80):
    ps=profiles(S)
    for x,y in combinations(ps,2):
        rx=x[2]-x[0]; ry=y[2]-y[0]
        gx=gini_three(x); gy=gini_three(y)
        assert (gx>gy)==(rx>ry)
        assert (gx<gy)==(rx<ry)
        px=product_three(x); py=product_three(y)
        reversal=((gx-gy)*(px-py)>0)
        criterion=((rx-ry)*(px-py)>0)
        assert reversal==criterion

print('VERIFY_OK')
print('reversal_counts_S3_to_S11',reversal_counts)
print('gini_tie_split_counts_S3_to_S11',gini_tie_split_counts)
print('first_strict_reversal',first_reversals[11])
print('witness_Gini',gini_three(A),gini_three(B),'products',product_three(A),product_three(B))
print('first_weak_split_S9',C,D,'Gini',gini_three(C),'products',product_three(C),product_three(D))
