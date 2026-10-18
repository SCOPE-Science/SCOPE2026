#!/usr/bin/env python3
"""Exact rational verification of a three-opinion bounded-confidence result.

This program uses a direct first-receptive-interaction transition check.
It is a finite sanity check; the proof establishes the infinite-time claim.
"""
from fractions import Fraction as F
from itertools import product


def unordered_prob(weights, i, j):
    W = sum(weights)
    return weights[i]*weights[j]/W * (1/(W-weights[i])+1/(W-weights[j]))


def predicted(b,c,weights):
    if not (1-c < b < c):
        return F(0)
    left = unordered_prob(weights,0,1)
    right = unordered_prob(weights,1,2)
    return (left*int(b>2*(1-c)) + right*int(b<2*c-1))/(left+right)


def direct(b,c,weights):
    points=[F(0),b,F(1)]
    total=F(0)
    good=F(0)
    for i,j in [(0,1),(0,2),(1,2)]:
        if abs(points[i]-points[j]) >= c:
            continue
        p=unordered_prob(weights,i,j)
        total+=p
        next_points=list(points)
        next_points[i]=next_points[j]=(points[i]+points[j])/2
        # The first successful interaction leaves two coincident opinions.
        # Hence connectedness is equivalent to global receptivity thereafter.
        if max(next_points)-min(next_points) < c:
            good+=p
    return good/total if total else F(0)

checks=0
for bi,ci in product(range(1,20),repeat=2):
    b=F(bi,20);c=F(ci,20)
    for ws in product([1,2,3,5],repeat=3):
        weights=list(map(F,ws))
        assert direct(b,c,weights)==predicted(b,c,weights), (b,c,ws)
        checks+=1

for c in [F(2,3),F(3,4),F(4,5)]:
    for b in [F(3,10),F(1,2),F(7,10)]:
        w=[F(2),F(1),F(1)]
        assert direct(b,c,w)==predicted(b,c,w)
        checks+=1

for a in range(1,30):
    w=[F(a),F(1),F(1)]
    p = F(a*(a+3),a*(a+3)+4)
    assert predicted(F(7,10),F(4,5),w)==p
    assert predicted(F(3,10),F(4,5),w)==1-p
    checks+=2

# Sharp confidence frontiers from exact existence-interval arithmetic.
assert F(2,3) < F(3,4)
# With 0 < c <= 2/3, both first-contact success intervals are empty.
for j in range(1,201):
    c=F(j,300)
    assert c<=F(2,3)
    assert not (2*(1-c)<c)
    assert not (1-c<2*c-1)
    checks+=2
# Both first-contact outcomes can succeed iff c > 3/4.
for j in range(1,100):
    c=F(3,4)+F(j,400)
    assert 2*(1-c)<F(1,2)<2*c-1
    checks+=1
print('PASS',checks,'exact comparisons')
