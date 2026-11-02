"""Exact independent checks for binary weight-three 3-subsequence deck classification.
Run: python3 deck3_candidate_verify.py
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb

def deck_direct(n, positions):
    s = [int(i in positions) for i in range(n)]
    ans = [0]*8
    for i,j,k in combinations(range(n),3):
        ans[4*s[i] + 2*s[j] + s[k]] += 1
    return tuple(ans)

def deck_dp(n, positions):
    s = [int(i in positions) for i in range(n)]
    # Independent recurrence for all length-three pattern multiplicities.
    d = [[0]*(1<<k) for k in range(4)]
    d[0][0] = 1
    for bit in s:
        for k in (3,2,1):
            for p in range(1<<(k-1)):
                d[k][2*p+bit] += d[k-1][p]
    return tuple(d[3])

def statistic(n,pos):
    p,q,r=pos
    return (2*p+q, r-p, p*p+q*q+r*r)

def mate(n,pos):
    p,q,r=pos
    a=q-p; b=r-q
    if (a-b)%3:
        return None
    other_p=p+(a-b)//3
    other=(other_p,other_p+b,other_p+a+b)
    if other == pos: return None
    if 0<=other[0]<other[1]<other[2]<n:
        return other
    return None

def count_pairs_formula(n):
    return sum(max(0,n-2*b-4*h) for b in range(1,(n+1)//2+1)
                                         for h in range(1,(n+1)//4+1))

def coeff_gf(n):
    # z^7 / [(1-z)^2 (1-z^2)(1-z^4)]
    return sum((n-6-2*i-4*j) for i in range(n//2+1)
                                     for j in range(n//4+1)
                                     if n-7-2*i-4*j>=0)

def run():
    allcollisions=[]
    for n in range(3,23):
        fibers=defaultdict(list); statfibers=defaultdict(list)
        for pos in combinations(range(n),3):
            d=deck_dp(n,pos)
            if n<=15: assert d == deck_direct(n,pos), (n,pos,d,deck_direct(n,pos))
            fibers[d].append(pos)
            statfibers[statistic(n,pos)].append(pos)
        assert {frozenset(v) for v in fibers.values()} == {frozenset(v) for v in statfibers.values()},n
        got_pairs=0
        for cls in fibers.values():
            assert len(cls)<=2, (n,cls)
            for x in cls:
                expected=[z for z in cls if z!=x]
                assert (mate(n,x) is None and not expected) or mate(n,x)==expected[0],(n,cls,x,mate(n,x))
            if len(cls)==2:
                got_pairs+=1
                if n==7: allcollisions.append(cls)
        assert got_pairs==count_pairs_formula(n)==coeff_gf(n), (n,got_pairs,count_pairs_formula(n),coeff_gf(n))
        assert len(fibers)==comb(n,3)-got_pairs,n
        print(f"n={n:2d} words={comb(n,3):5d} pairs={got_pairs:4d} decks={len(fibers):5d}")
    assert allcollisions==[[(0,4,5),(1,2,6)]] or allcollisions==[[(1,2,6),(0,4,5)]],allcollisions
    print('VERIFY_OK')

if __name__=='__main__':run()
