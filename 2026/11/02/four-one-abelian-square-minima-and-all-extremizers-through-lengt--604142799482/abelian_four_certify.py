#!/usr/bin/env python3
"""Validate exhaustive result data and the four residue-class extremizer patterns.

Usage: python3 abelian_four_certify.py abelian_four_optimized_n128.txt
The standalone exhaustive enumeration is in abelian_four_optimized.cpp.
"""
import sys
from math import comb


def parity_count(lo, hi, p):
    if lo > hi: return 0
    if (lo & 1) != p: lo += 1
    return 0 if lo > hi else 1 + (hi - lo) // 2


def square_count(r):
    assert len(r) == 5 and all(isinstance(t, int) and t >= 0 for t in r)
    total = max(r) // 2
    for g in set(r[1:4]):
        pairs = [(r[i],r[i+2]) for i in range(3) if r[i+1] == g]
        for u in range(1+max(L for L,R in pairs)):
            Rmax = max(R for L,R in pairs if L >= u)
            total += parity_count(max(0, u-g), min(Rmax, u+g), (u-g)&1)
    for u in range(r[0]+1):
        total += parity_count(max(0,u+r[1]-r[2]-r[3]),
                              min(r[4],u+r[1]+r[2]-r[3]),
                              (u+r[1]+r[2]+r[3])&1)
    return total


def expected(n):
    m,t=divmod(n,4)
    if t==0: params=[(0,2*m-1,2*m-3)]
    elif t==1: params=[(0,2*m-1,2*m-2)]
    elif t==2: params=[(0,2*m-1,2*m-1), (0,2*m+1,2*m-3),
                       (1,2*m-1,2*m-2), (2,2*m-1,2*m-3)]
    else: params=[(0,2*m+1,2*m-2),(2,2*m-1,2*m-2)]
    found=set()
    for a,b,c in params:
        r=(a,b,0,0,c)
        assert sum(r)+4==n
        found.add(r);found.add(r[::-1])
    assert len(found)=={0:2,1:2,2:8,3:4}[t]
    return found


def verify(path):
    data={}
    for l in open(path,encoding='utf8'):
        if l.startswith('#'):continue
        n,val,ct,best,count=l.split()
        n=int(n);val=int(val);ct=int(ct);count=int(count)
        assert n not in data and count == comb(n,4)
        data[n]=(val,ct,count)
        p=tuple(map(int,best.split(',')))
        rr=(p[0],p[1]-p[0]-1,p[2]-p[1]-1,p[3]-p[2]-1,n-p[3]-1)
        assert square_count(rr)==val
    assert set(data)==set(range(4,129))
    for n in range(19,129):
        val,ct,_=data[n]
        assert val==(n+2)//4
        candidates=expected(n)
        assert len(candidates)==ct
        assert all(square_count(r)==val for r in candidates)
    print('PASS: 125 complete length profiles; 110 classified n=19..128;')
    print('sum tested binary four-one words:',sum(x[2] for x in data.values()))
    print('all 2/4/8 predicted labeled extremizers attained the recorded optimum')


if __name__=='__main__':verify(sys.argv[1] if len(sys.argv)>1 else 'abelian_four_optimized_n128.txt')
