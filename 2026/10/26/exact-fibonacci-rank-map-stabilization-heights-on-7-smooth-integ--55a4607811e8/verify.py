#!/usr/bin/env python3
"""Reproduce finite checks for Fibonacci rank-map stabilization on 7-smooth inputs.

Only finite tests; the universal result follows from the valuation-state proof.
"""
from math import gcd


def direct_rank(n):
    if n == 1:
        return 1
    old, cur = 0, 1
    for j in range(1, 2*n + 1):
        if cur == 0:
            return j
        old, cur = cur, (old + cur) % n
    raise AssertionError(('rank upper bound', n))


def vector_rank(a,b,c,d):
    aa = bb = 0
    if a == 1:
        bb = 1
    elif a == 2:
        aa,bb = 1,1
    elif a >= 3:
        aa,bb = a-2,1
    if b:
        aa=max(aa,2); bb=max(bb,b-1)
    if d:
        aa=max(aa,3)
    return (aa,bb,c,max(d-1,0))


def predicted_height(a,b,d):
    r=(max(0,a-2)+1)//2
    if d>=2:
        return max(d+1,b-1,r)
    if d==1:
        return 3 if a==0 and b<=1 else max(2,b-1,r)
    if a<=3 and b<=1:
        return ((0,3),(4,1),(2,0),(2,1))[a][b]
    return max(0,b-1,r)


def actual_height(a,b,c,d):
    state=(a,b,c,d)
    for t in range(1200):
        new=vector_rank(*state)
        if new==state:
            return t,state
        state=new
    raise AssertionError('no eventual fixed point within bound')


def factor_7_smooth(n):
    r=[]
    for p in (2,3,5,7):
        e=0
        while n%p==0:
            e+=1; n//=p
        r.append(e)
    return (*r,n)


def main():
    rank_count=0
    for n in range(1,5001):
        a,b,c,d,residue=factor_7_smooth(n)
        if residue>1: continue
        a1,b1,c1,d1=vector_rank(a,b,c,d)
        predicted=(2**a1)*(3**b1)*(5**c1)*(7**d1)
        actual=direct_rank(n)
        assert predicted==actual, (n,predicted,actual)
        rank_count+=1
    tests=0
    for a in range(64):
        for b in range(64):
            for d in range(20):
                for c in (0,3):
                    h,att=actual_height(a,b,c,d)
                    assert h==predicted_height(a,b,d),(a,b,c,d,h,predicted_height(a,b,d))
                    assert att==(0,0,c,0) if (a==0 and b==0 and d==0) else att==(2,1,c,0), (a,b,c,d,att)
                    tests+=1
    # Height-5 to height-8 minimal smooth witness, independently enumerated.
    for h in range(5,9):
        bound=3**(h+1)
        smooth=[]
        for a in range(20):
            for b in range(15):
                for c in range(10):
                    for d in range(10):
                        n=2**a*3**b*5**c*7**d
                        if n<=bound:
                            smooth.append((n,a,b,c,d))
        actuals=[(n,a,b,c,d) for n,a,b,c,d in smooth if actual_height(a,b,c,d)[0]==h]
        assert len(actuals)==1 and actuals[0][0]==bound,(h,actuals)
    print(f'VERIFY_OK: {rank_count} independent direct modular Fibonacci ranks; {tests} exponent-state iterations; four exhaustive smooth minima (heights 5..8)')

if __name__=='__main__':
    main()
