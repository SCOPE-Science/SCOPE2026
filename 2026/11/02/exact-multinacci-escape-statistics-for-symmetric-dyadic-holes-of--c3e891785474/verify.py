#!/usr/bin/env python3
"""Exact finite-prefix checks for symmetric dyadic holes of the negative-doubling map.
This is a finite stress test. Infinite statements rely on the accompanying proof.
"""
from fractions import Fraction
from itertools import product

def T(x):
    return 1 - 2*x if x < Fraction(1,2) else 2 - 2*x

def itinerary(x, n):
    bits = []
    for _ in range(n):
        assert x != Fraction(1,2)
        bits.append('0' if x < Fraction(1,2) else '1')
        x = T(x)
    return ''.join(bits)

def critical_words(m):
    a = '00' + ''.join('1' if i % 2 == 0 else '0' for i in range(m-2))
    b = ''.join('1' if x == '0' else '0' for x in a)
    return a, b

def count_recurrence(m, n):
    r=m-2
    a={}
    for k in range(1,n+1):
        a[k]=2+sum(a.get(k-j,0) for j in range(1,r+1))
    return 1 if n==0 else a[n]

def count_words(m,n):
    forbidden=critical_words(m)
    return sum(not any(w in ''.join(chars) for w in forbidden)
               for chars in product('01', repeat=n))

def main():
    cases=0
    for m in range(2,9):
        cells={}
        mid=2**(m-1)
        for k in range(2**m):
            x=Fraction(2*k+1,2**(m+1))
            cells[k]=itinerary(x,m)
        assert set(cells.values())=={''.join(c) for c in product('01',repeat=m)}
        assert (cells[mid-1], cells[mid])==critical_words(m)
        for n in range(1,15):
            found=count_words(m,n)
            expect=count_recurrence(m,n)
            assert found==expect,(m,n,found,expect)
            cases+=1
        for n in range(1,m):
            assert count_recurrence(m,n)==2**n
        assert count_recurrence(m,m)==2**m-2
    # Independent first-hitting survival by explicit rational interval itinerary
    for m in range(2,7):
        a=Fraction(1,2)-Fraction(1,2**m)
        b=Fraction(1,2)+Fraction(1,2**m)
        for t in range(1,7):
            n=t+m-1
            hits=0
            for k in range(2**n):
                x=Fraction(2*k+1,2**(n+1))
                good=True
                for _ in range(t):
                    if a<x<b:
                        good=False
                        break
                    x=T(x)
                hits += int(good)
            assert hits==count_recurrence(m,n),(m,t,hits,count_recurrence(m,n))
    print(f'PASS: {cases} exhaustive forbidden-word counts; dyadic-cylinder identification m=2..8; direct rational orbit survival m=2..6, t=1..6.')
    print('Analytic-only: recurrence for all lengths, rational generating function, exact expectation and Perron entropy/escape asymptotics.')

if __name__=='__main__':
    main()
