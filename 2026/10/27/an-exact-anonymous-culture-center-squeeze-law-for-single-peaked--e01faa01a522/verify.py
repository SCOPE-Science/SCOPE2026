#!/usr/bin/env python3
"""Exact independent enumeration for a fixed-axis single-peaked IRV benchmark.

Uses only Python standard library and exact integer/rational comparisons.
"""
from math import comb
from fractions import Fraction

ORDERS=(('L','C','R'), ('C','L','R'), ('C','R','L'), ('R','C','L'))
CANDIDATES=('L','C','R')


def condorcet(hist):
    winners=[]
    n=sum(hist)
    for x in CANDIDATES:
        if all(sum(hist[j] for j,order in enumerate(ORDERS)
                   if order.index(x)<order.index(y))*2>n
               for y in CANDIDATES if y!=x):
            winners.append(x)
    assert len(winners)==1
    return winners[0]


def irv_winners(hist):
    """All winners across all legal first-round elimination ties."""
    n=sum(hist)
    first={z:sum(hist[j] for j,order in enumerate(ORDERS) if order[0]==z)
           for z in CANDIDATES}
    if any(v*2>n for v in first.values()):
        return {z for z,v in first.items() if v*2>n}
    low=min(first.values())
    results=set()
    for elim in [z for z in CANDIDATES if first[z]==low]:
        rem=[z for z in CANDIDATES if z!=elim]
        ct={z:sum(hist[j] for j,order in enumerate(ORDERS)
                  if order.index(z)<order.index(rem[1 if z==rem[0] else 0]))
            for z in rem}
        assert ct[rem[0]]+ct[rem[1]]==n
        results.add(rem[0] if ct[rem[0]]>ct[rem[1]] else rem[1])
    return results


def formula_count(n):
    assert n%2==1 and n>=1
    r=(n-1)//2
    q=r//2
    h=(2*r-1)//3
    return sum(m*(m+1) for m in range(1,q+1))+sum(
        (m+1)*(2*r-3*m) for m in range(q+1,h+1))


def independent_count(n):
    r=(n-1)//2
    total=0
    for m in range(n+1):
        for a in range(n-m+1):
            d=n-m-a
            if a<=r and d<=r and m<a and m<d:
                total+=m+1
    return total


def enumeration(n):
    numerator=0
    count=0
    for a in range(n+1):
        for b in range(n-a+1):
            for c in range(n-a-b+1):
                d=n-a-b-c
                hist=(a,b,c,d)
                actual=condorcet(hist) not in irv_winners(hist)
                predicted=(a<=n//2 and d<=n//2 and b+c<min(a,d))
                assert actual==predicted, (n,hist,actual,predicted)
                numerator+=actual
                count+=1
    assert count==comb(n+3,3)
    return numerator


def main():
    total=0
    for n in range(1,18,2):
        brute=enumeration(n)
        algebra=formula_count(n)
        independent=independent_count(n)
        assert brute==algebra==independent, (n,brute,algebra,independent)
        total+=comb(n+3,3)
        print('n=',n, 'count=',brute, 'probability=', Fraction(brute,comb(n+3,3)))
    for n in (21,101,501,2001):
        assert formula_count(n)==independent_count(n)
        print('n=',n,'probability=',float(Fraction(formula_count(n),comb(n+3,3))))
    assert abs(float(Fraction(formula_count(2001),comb(2004,3)))-7/144)<0.0001
    print('PASS',total,'complete histogram checks; rational target=',Fraction(7,144))


if __name__=='__main__':main()
