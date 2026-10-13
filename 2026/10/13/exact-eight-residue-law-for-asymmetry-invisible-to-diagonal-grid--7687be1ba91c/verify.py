#!/usr/bin/env python3
"""Exact integer consistency checks for finite diagonal-grid copula asymmetry."""
from fractions import Fraction


def predicted(n):
    q, r = divmod(n, 8)
    a = (0, 3, 6, 11, 14, 17, 22, 25)
    b = (0, 0, 0, 2, 3, 5, 8, 10)
    return 15*q*q+a[r]*q+b[r]


def upper(i, j, n):
    h = lambda k: k*(n-k)
    H = max(h(k) for k in range(i, j+1))
    return min(h(i), h(j))-max(0, H-n*(j-i))


def grid_max(n):
    return max(upper(i,j,n) for i in range(n+1) for j in range(i+1,n+1))


def finite_witness(n, entries, expected):
    assert len(entries)==n and all(len(row)==n for row in entries)
    assert all(v>=0 and isinstance(v,int) for row in entries for v in row)
    assert all(sum(row)==n for row in entries)
    assert all(sum(entries[i][j] for i in range(n))==n for j in range(n))
    assert all(sum(entries[i][j] for i in range(k) for j in range(k))==k*k for k in range(n+1))
    def prefix(a,b): return sum(entries[i][j] for i in range(a) for j in range(b))
    attained=max(abs(prefix(i,j)-prefix(j,i)) for i in range(n+1) for j in range(i+1,n+1))
    assert attained==expected, (n,attained,expected)


M3=[[1,2,0],[0,1,2],[2,0,1]]
M8=[
 [1,0,0,0,7,0,0,0],
 [3,0,0,4,1,0,0,0],
 [1,0,4,3,0,0,0,0],
 [0,0,0,0,0,1,0,7],
 [0,0,0,1,0,7,0,0],
 [3,0,0,0,0,0,5,0],
 [0,8,0,0,0,0,0,0],
 [0,0,4,0,0,0,3,1]]


def run():
    finite_witness(3,M3,2)
    finite_witness(8,M8,15)
    for n in range(2,96):
        assert grid_max(n)==predicted(n), (n,grid_max(n),predicted(n))
        q,r=divmod(n,8)
        assert predicted(n)>=0
        if r:
            assert Fraction(predicted(n),n*n)<Fraction(15,64),n
        else:
            assert Fraction(predicted(n),n*n)==Fraction(15,64),n
    for n in (101,137,256,512,999,1200):
        h=lambda k: k*(n-k)
        H=max(h(k) for k in range(n+1))
        def centered(d):
            L=d+(n-d)%2
            return (n*n-L*L)//4-max(0,H-n*d)
        assert max(centered(d) for d in range(1,n))==predicted(n),n
    print('PASS: integer witnesses at n=3,8; complete grid bounds n=2..95;')
    print('large-n centered optimization and strict 8-divisibility equality checks.')

if __name__=='__main__': run()
