#!/usr/bin/env python3
"""Standalone finite checks for the Catalan-pellytope linear-depth vertex law.

Run: python3 CHECKER.py
Only Python's standard library is used. Finite checks are supplementary to the proof.
"""
import math
from functools import lru_cache

TABLE = {
    1: [2],
    2: [4,5],
    3: [8,12,14],
    4: [16,29,37,42],
    5: [32,70,98,118,132],
    6: [64,169,261,331,387,429],
    7: [128,408,694,934,1130,1298,1430],
    8: [256,985,1845,2645,3317,3905,4433,4862],
    9: [512,2378,4906,7476,9786,11802,13650,15366,16796],
    10:[1024,5741,13045,21120,28932,35862,42198,48204,53924,58786],
}

def catalan(k):
    return math.comb(2*k,k)//(k+1)

def blocks(d):
    return [0,2]+[catalan(j-1) for j in range(2,d+1)]

def vertices(n,d):
    """Coefficient computed by the published finite recurrence."""
    b=blocks(d)
    v=[1]+[0]*n
    for r in range(1,n+1):
        v[r]=sum(b[j]*v[r-j] for j in range(1,min(r,d)+1))
    return v[n]

def direct_composition_weight(n,d):
    """A different computation: enumerate ordered compositions, weight each block."""
    b=blocks(d)
    @lru_cache(None)
    def enumerate_compositions(r):
        if r==0:
            return ((),)
        return tuple((j,)+tail for j in range(1,min(r,d)+1)
                     for tail in enumerate_compositions(r-j))
    return sum(math.prod(b[j] for j in comp)
               for comp in enumerate_compositions(n))

def normalized_vertex(n,alpha):
    """Coefficient at critical z=1/4, avoiding exponentially large integers."""
    d=int(alpha*n)
    b=[0.]*(d+1)
    b[1]=0.5
    if d>=2: b[2]=1./16.
    for j in range(3,d+1):
        b[j]=b[j-1]*(4*j-6)/(4*j)
    v=[1.]+[0.]*n
    for r in range(1,n+1):
        v[r]=sum(b[j]*v[r-j] for j in range(1,min(r,d)+1))
    return n*n*v[n]

def constant(alpha):
    if alpha<=0.5: return 0.0
    return 16*(2*alpha-1)/(math.pi*math.sqrt(alpha*(1-alpha)))

def two_block(n,alpha):
    d=int(alpha*n)
    def b(j):
        if j==1: return 0.5
        return math.exp(math.lgamma(2*j-1)-math.lgamma(j)
                        -math.lgamma(j+1)-j*math.log(4))
    return n*n*sum(b(j)*b(n-j) for j in range(max(1,n-d),d+1)
                    if n-j>=1)

def main():
    count=0
    for n,row in TABLE.items():
        for d,expected in enumerate(row,start=1):
            actual=vertices(n,d)
            assert actual==expected,(n,d,actual,expected)
            count+=1
    print('Exact published-table comparisons:',count)
    count=0
    for n in range(1,12):
        for d in range(1,n+1):
            assert vertices(n,d)==direct_composition_weight(n,d),(n,d)
            count+=1
    print('Independent weighted-composition enumerations:',count)
    for a in (0.4,0.5,0.65,0.75,0.9):
        x=normalized_vertex(300,a)
        y=normalized_vertex(1600,a)
        c=constant(a)
        if a<=0.5: assert 0<y<x
        else: assert abs(y-c)/c<0.32,(a,y,c)
        print('alpha=',a,'n300=',round(x,7),'n1600=',round(y,7),
              'proven limit=',round(c,7))
    for a in (0.55,0.75,0.9):
        goal=(2*a-1)/(4*math.pi*math.sqrt(a*(1-a)))
        x=two_block(5000,a)
        assert abs(x-goal)<0.002,(a,x,goal)
        print('two-block n5000:',a,round(x,9),'limit',round(goal,9))
    print('CHECKER_OK')

if __name__=='__main__':main()
