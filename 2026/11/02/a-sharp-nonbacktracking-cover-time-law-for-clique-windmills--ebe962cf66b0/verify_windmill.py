#!/usr/bin/env python3
"""Exact finite-state checks for first-petal hitting probabilities.
Reproduces rational absorbing-chain calculations independently of the closed formulas.
"""
from fractions import Fraction
from itertools import product


def solve(a,b):
    n=len(b)
    if n==0:return []
    a=[[Fraction(x) for x in row]+[Fraction(b[i])] for i,row in enumerate(a)]
    for col in range(n):
        pivot=next((k for k in range(col,n) if a[k][col]),None)
        assert pivot is not None, 'nonabsorbing chain'
        a[col],a[pivot]=a[pivot],a[col]
        d=a[col][col]
        for k in range(col,n+1):a[col][k]/=d
        for i in range(n):
            if i==col:continue
            factor=a[i][col]
            if factor:
                for k in range(col,n+1):a[i][k]-=factor*a[col][k]
    return [a[i][-1] for i in range(n)]


def simple_avoid(m,s):
    marked=set(range(s)); unmarked=tuple(range(s,m)); idx={v:i for i,v in enumerate(unmarked)}
    if not unmarked:return Fraction(0)
    A=[]; b=[]
    for v in unmarked:
        row=[Fraction(int(v==w)) for w in unmarked]
        for w in unmarked: row[idx[w]]-=Fraction(1,m) if w!=v else Fraction(0)
        A.append(row);b.append(Fraction(1,m))
    x=solve(A,b)
    return sum(x,Fraction(0))/m


def nb_avoid(m,s):
    unmarked=tuple(range(s,m)); pairs=tuple((i,j) for i in unmarked for j in unmarked if i!=j)
    if not pairs:return Fraction(0)
    idx={st:i for i,st in enumerate(pairs)}
    A=[]; b=[]
    for i,j in pairs:
        row=[Fraction(int(st==(i,j))) for st in pairs]
        for k in unmarked:
            if k!=i and k!=j: row[idx[(j,k)]]-=Fraction(1,m-1)
        A.append(row);b.append(Fraction(1,m-1))
    x=solve(A,b)
    return sum(x,Fraction(0))/ (m*(m-1))


def main():
    checks=0
    for m in range(2,8):
        for s in range(1,m+1):
            expected_s=Fraction(m-s,m*(s+1))
            expected_n=Fraction((m-s)*(m-s-1),m*(m-1)*(s+1))
            actual_s=simple_avoid(m,s)
            actual_n=nb_avoid(m,s)
            assert actual_s==expected_s,(m,s,'simple',actual_s,expected_s)
            assert actual_n==expected_n,(m,s,'nonbacktracking',actual_n,expected_n)
            checks+=2
        q_s=1-simple_avoid(m,1); q_n=1-nb_avoid(m,1)
        assert q_s==Fraction(m+1,2*m)
        assert q_n==Fraction(m+2,2*m)
        assert q_s/q_n==Fraction(m+1,m+2)
        for s in range(2,m+1):
            assert 1-simple_avoid(m,s)>q_s
            assert 1-nb_avoid(m,s)>q_n if m>=3 else 1-nb_avoid(m,s)==q_n
            checks+=2
        checks+=3
    print('PASS',checks,'exact rational checks; m=2..7, all marked subsets up to symmetry')

if __name__=='__main__':main()
