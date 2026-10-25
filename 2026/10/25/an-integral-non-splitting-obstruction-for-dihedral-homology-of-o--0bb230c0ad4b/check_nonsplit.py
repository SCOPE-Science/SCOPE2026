#!/usr/bin/env python3
"""Independent finite GF(2) checks for the odd-cycle reflection obstruction.
No third-party dependencies. Exhaustive q-face orbit linear algebra verifies that
no reflection-invariant cycle lifts a distinguished omitted facet for tested cases.
The general assertion is proved symbolically in RESULT.md, not by this enumeration.
"""
from itertools import combinations
from math import comb

def solvable(rows, nv):
    piv = {}
    for lhs, rhs in rows:
        a=lhs | (rhs<<nv)
        while a:
            p=(a & ((1<<nv)-1)).bit_length()-1
            if p<0:
                if a>>nv: return False
                break
            if p in piv: a^=piv[p]
            else: piv[p]=a; break
    return True

def examine(n,k):
    q=n-k; verts=range(n)
    B=set(range(k)); F=tuple(i for i in verts if i not in B)
    s=lambda i:(k-1-i)%n
    omitted={tuple(sorted(set(verts)-{(a+j)%n for j in range(k)})) for a in range(n)}
    assert len(omitted)==n and F in omitted
    orb={}; count=0
    for face in combinations(verts,q):
        if face in orb: continue
        mate=tuple(sorted(s(i) for i in face))
        orb[face]=count;orb[mate]=count;count+=1
    rows=[]
    for R in combinations(verts,q-1):
        bits=0
        for v in verts:
            if v not in R:
                bits ^= 1<<orb[tuple(sorted(R+(v,)))]
        rows.append((bits,0))
    for face in omitted: rows.append((1<<orb[face],int(face==F)))
    feasible=solvable(rows,count)
    if n%2 and k%2==0:
        fixed=[i for i in verts if s(i)==i]
        assert len(fixed)==1 and fixed[0] in F
        R=set(F)-set(fixed)
        assert {s(i) for i in R}==R
        assert all(s(i)!=i for i in B)
        assert not feasible, (n,k,'unexpected GF2 section')
    return feasible

if __name__=='__main__':
    tested=0; nonsplit=0
    for n in range(5,12):
        for k in range(3,n-1):
            good=examine(n,k)
            tested+=1
            if n%2 and k%2==0:
                assert not good
                nonsplit+=1
    print('PASS:',tested,'GF(2) invariant-cycle linear systems;',nonsplit,'odd-n/even-k obstructions')
    print('General non-splitting rests on the symbolic fixed-codimension-one-face parity argument.')
