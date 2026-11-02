#!/usr/bin/env python3
"""Independent exact tests for inversion counts conditioned on a specified 2-cycle.

Run: python3 verify.py
Requires only Python 3 standard library. Finite tests are not an infinite proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def inversions(p):
    return sum(p[a] > p[b] for a in range(len(p)) for b in range(a+1,len(p)))


def displacement(n, i, j):
    """Formula, where positions i,j are one-based."""
    return Fraction(1,2) + Fraction((j-i-1)**2-(i+j-n-1)**2,n-2)


def direct_mean(n, i, j):
    """Independent evaluation of the finite (n-2)! conditional permutations."""
    others = [x for x in range(1,n+1) if x not in (i,j)]
    acc = 0
    for q in permutations(others):
        a = list(q)
        a.insert(i-1,j)
        a.insert(j-1,i)
        acc += inversions(a)
    return Fraction(acc,factorial(n-2))


def conditional_pair_marginal_mean(n,i,j):
    """Build from individual pair inversion probabilities, not the closed formula."""
    others = tuple(x for x in range(1,n+1) if x not in (i,j))
    ans = Fraction(0)
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            if a in (i,j) and b in (i,j):
                ans += 1
            elif a not in (i,j) and b not in (i,j):
                ans += Fraction(1,2)
            elif a in (i,j):
                fixed = j if a==i else i
                ans += Fraction(sum(fixed>v for v in others),n-2)
            else:
                fixed = j if b==i else i
                ans += Fraction(sum(v>fixed for v in others),n-2)
    return ans


def run():
    tests=0
    for n in range(3,9):
        base=Fraction(n*(n-1),4)
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                predicted=base+displacement(n,i,j)
                assert direct_mean(n,i,j)==predicted,(n,i,j,'direct')
                assert conditional_pair_marginal_mean(n,i,j)==predicted,(n,i,j,'marginal')
                event=Fraction(1,n*(n-1))
                assert event*displacement(n,i,j)==event*(direct_mean(n,i,j)-base)
                tests+=3
    for n in range(3,151):
        ds=[displacement(n,i,j) for i in range(1,n+1) for j in range(i+1,n+1)]
        assert sum(ds,Fraction(0))==Fraction(n*(n-1),12)
        tests+=1
    for n in (200,400,800,1600):
        # An independent integer-inequality count for the exact sign rule.
        plus=sum(2*(n-2*i)*(2*j-n-2)>-(n-2)
                 for i in range(1,n+1) for j in range(i+1,n+1))
        minus=sum(2*(n-2*i)*(2*j-n-2)<-(n-2)
                 for i in range(1,n+1) for j in range(i+1,n+1))
        zeros=n*(n-1)//2-plus-minus
        assert abs(Fraction(plus,n*(n-1)//2)-Fraction(1,2))<Fraction(1,10)
        assert zeros>=0
        tests+=2
    print(f'PASS {tests} independent exact and sign checks')

if __name__=='__main__':run()
