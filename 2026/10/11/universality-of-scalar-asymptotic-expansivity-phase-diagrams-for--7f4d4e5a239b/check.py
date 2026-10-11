#!/usr/bin/env python3
"""Finite arithmetic diagnostics for the geometric Cantor-gap example only."""
from fractions import Fraction as Q

def cantorset(level):
    pieces = [(Q(0), Q(1))]
    gaps = []
    for _ in range(level):
        new = []
        for a,b in pieces:
            length = b-a
            u = a+length/3
            v = b-length/3
            assert u < v
            gaps.append((u,v))
            new.extend([(a,u),(v,b)])
        pieces = new
    return pieces, gaps

def test():
    checked = 0
    for n in range(1,9):
        pieces,gaps = cantorset(n)
        assert len(pieces)==2**n
        assert len(gaps)==2**n-1
        assert sum(b-a for a,b in pieces)==Q(2,3)**n
        for a,b in gaps:
            assert 0<=a<b<=1
            assert any(u<=a<=v for u,v in pieces)
            assert any(u<=b<=v for u,v in pieces)
            assert not any(u <= (a+b)/2 <= v for u,v in pieces)
            checked += 3
        checked += 3
    print('PASS: ',checked,'exact rational finite Cantor checks')

if __name__=='__main__':
    test()
