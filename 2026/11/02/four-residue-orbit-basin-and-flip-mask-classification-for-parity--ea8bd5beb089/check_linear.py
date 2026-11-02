#!/usr/bin/env python3
"""Independent binary-matrix verification of parity dynamics on two-set Kneser graphs."""
from itertools import combinations
from math import comb

def rank2(rows):
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = row
                break
            row ^= basis[pivot]
    return len(basis)

def rows_times(x, y):
    result=[]
    for row in x:
        bits=0
        while row:
            k=(row & -row).bit_length()-1
            bits ^= y[k]
            row &= row-1
        result.append(bits)
    return result

def construct(n):
    sets=list(combinations(range(n),2))
    return [sum(1<<j for j,(c,d) in enumerate(sets) if a!=c and a!=d and b!=c and b!=d) for a,b in sets]

def run():
    print('n N mod4 rankA rank(A-I) rank(A^2) rank(A^3) fixed period initial T1 Q2 identity')
    for n in range(5,18):
        a=construct(n); N=len(a); I=[1<<i for i in range(N)];
        a2=rows_times(a,a); a3=rows_times(a2,a)
        ranka=rank2(a); rkfixed=rank2([x^y for x,y in zip(a,I)])
        r2=rank2(a2); r3=rank2(a3)
        f=1<<(N-rkfixed)
        periodic=1<<ranka if n%4!=0 else 1<<N
        predicted_fixed=1<<(N-n+(1 if n%2==0 else 0))
        expected_rank={0:N,1:N-n+1,2:N-1,3:N-n}[n%4]
        expected_q2=(periodic-f)//2
        assert f==predicted_fixed and ranka==expected_rank
        if n%4==0:
            assert a2==I
            identity='A^2=I'
        elif n%4==3:
            assert a2==a
            identity='A^2=A'
        else:
            assert a3==a
            identity='A^3=A'
        assert expected_q2 >=0
        print(n,N,n%4,ranka,rkfixed,r2,r3,f,periodic,(1<<N)-periodic,expected_q2,identity)
    print('LINEAR_VERIFY_OK')

if __name__=='__main__': run()
