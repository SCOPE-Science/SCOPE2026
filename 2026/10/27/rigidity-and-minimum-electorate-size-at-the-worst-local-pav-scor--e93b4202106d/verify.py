"""Exact checks for equality cases and sparse worst-case PAV elections.

A finite checker supporting, not replacing, the analytic proof.
"""
from fractions import Fraction
from itertools import combinations
from math import ceil


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m + 1)), Fraction(0))


def gamma(r, u, x, y):
    if u == 0:
        return Fraction(r*x)
    return Fraction(x*(r-y), u+1) - Fraction(y*(r-x), u)


def expected_minimum(k):
    return Fraction((3*k-1)*(k+1), 4) if k % 2 else Fraction((3*k-1)*(k+2), 2)


def example(k):
    assert k >= 2
    t = (k+1)//2 if k % 2 else k//2+1
    d = [1 if j < t else 0 for j in range(k)] if k % 2 else [2 if j < t else 0 for j in range(k)]
    S = sum(d)
    assert all((Fraction(S)-Fraction(k+1,2)*v).denominator == 1 for v in d)
    b = [int(Fraction(S)-Fraction(k+1,2)*v) for v in d]
    assert min(b) >= 0
    ballots = []
    for j in range(k):
        for a, count in enumerate(d):
            ballots += [{j,k+a}] * count
    for a,count in enumerate(b):
        ballots += [{k+a}] * count
    assert len(ballots) == expected_minimum(k)
    W=set(range(k));O=set(range(k,2*k))
    def score(com):
        return sum((harmonic(len(com & v)) for v in ballots),Fraction(0))
    SW,SO=score(W),score(O)
    assert SO > SW and Fraction(SW, SO) == Fraction(2*k, 3*k-1)
    for w in W:
        for a in O:
            assert score((W-{w})|{a}) == SW
    if k <= 6:
        assert all(score(set(T)) <= SO for T in combinations(range(2*k),k))
    return len(ballots), SW, SO


def main():
    inequalities = 0
    equality = 0
    for r in range(2,21):
        for u in range(0,25):
            for y in range(min(r,u)+1):
                for x in range(r+1):
                    g=gamma(r,u,x,y)
                    diff=Fraction(3*r-1)*harmonic(u)+2*g-2*r*harmonic(u+x-y)
                    assert diff>=0, (r,u,x,y,diff)
                    eq=diff==0
                    desired=(u==0 and x<=1) or (u==1 and y==1 and x==1)
                    assert eq==desired, (r,u,x,y,diff)
                    inequalities+=1
                    equality+=eq
    for k in range(2,15):
        count,s1,s2=example(k)
        print('k',k,'minimum_voters',count,'PAV_baseline',s1,'PAV_optimal',s2,'ratio',Fraction(s1,s2))
    print('pointwise exact identities and inequality checks:', inequalities, 'equalities:', equality)
    print('All checks passed; finite tests do not prove all-size theorem.')

if __name__=='__main__':main()
