#!/usr/bin/env python3
"""Vertex-subset enumeration of minimum strong total covers on rook graphs."""
from itertools import combinations
from math import comb

def census(m,n):
    N=m*n
    nbr=[]
    for a in range(N):
        ma=0
        for b in range(N):
            if a!=b and (a//n==b//n or a%n==b%n):ma|=1<<b
        nbr.append(ma)
    t=min(m,n,(m+n)//3); optimum=N-t
    total=0; profiles={}
    for U in range(1<<N):
        count=U.bit_count(); E=0;isolates=[]
        for a in range(N):
            if U>>a&1:
                ds=(nbr[a]&U).bit_count()
                E+=ds
                if not ds:isolates.append(a)
        E//=2
        cost=(N-count)+E+len(isolates)
        assert cost>=optimum,(m,n,U,'formula contradiction')
        if cost==optimum:
            ways=1
            for a in isolates:ways*=nbr[a].bit_count()
            total+=ways
            profiles[(E,len(isolates))]=profiles.get((E,len(isolates)),0)+ways
    return total,profiles

if __name__=='__main__':
    for n in range(2,9):
        actual,profiles=census(2,n)
        expected=comb(n,2)*comb(n-2,2) if n>=4 else (8 if n==2 else 45)
        assert actual==expected,(n,actual,expected,profiles)
        print('two_row',n,actual,profiles)
    print('three_by_three',census(3,3))
    print('VERIFY_OK')
