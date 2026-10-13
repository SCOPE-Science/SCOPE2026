#!/usr/bin/env python3
"""Exhaustive prescribed-value fibers of XY+YX on M2(Fq), q=3,5."""
from collections import Counter
from itertools import product

def check(q):
    assert q in (3, 5)
    mats = list(product(range(q), repeat=4))
    def matmul(A, B):
        a,b,c,d=A; e,f,g,h=B
        return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
    def anticommutator(A,B):
        return tuple((x+y)%q for x,y in zip(matmul(A,B),matmul(B,A)))
    fibers=Counter(anticommutator(A,B) for A in mats for B in mats)
    assert sum(fibers.values()) == q**8
    def prediction(B):
        a,b,c,d = B
        if B == (0,0,0,0):
            return q**5+3*q**4-2*q**3-2*q**2+q
        if b==c==0 and a==d:
            return q**5+q**4-2*q**3-q**2+q
        eigenlines=zerolines=0
        lines=[(1,t) for t in range(q)]+[(0,1)]
        for v,w in lines:
            x=(a*v+b*w)%q; y=(c*v+d*w)%q
            if (x,y)==(0,0): zerolines+=1
            if (x*w-y*v)%q==0: eigenlines+=1
        return q**4-q**2+q*(q-1)*(q*zerolines-eigenlines)
    for B in mats:
        assert fibers[B]==prediction(B),(q,B,fibers[B],prediction(B))
    distinct=sorted(set(fibers.values()))
    expected={3:[60,66,72,78,84,264,417],
              5:[560,580,600,660,680,3480,4705]}[q]
    assert distinct==expected,(q,distinct)
    print(f"q={q} targets={len(fibers)} total={sum(fibers.values())} values={distinct}")

if __name__=='__main__':
    check(3)
    check(5)
    print('VERIFY_OK')
