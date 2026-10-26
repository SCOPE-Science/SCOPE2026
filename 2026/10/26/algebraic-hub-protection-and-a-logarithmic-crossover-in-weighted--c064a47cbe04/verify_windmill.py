#!/usr/bin/env python3
"""Exact finite-state checks for weighted dimer adsorption on clustered hub graphs."""
from fractions import Fraction
from functools import lru_cache

def closed(blades, k, alpha, beta):
    b=Fraction(beta,alpha)
    q=Fraction(1)
    for j in range(1,k+1):
        q*=Fraction(2*j-1,1)/(2*j-1+2*b)
    return q**blades

def independent(blades,k,alpha,beta,odd=False):
    blade_size=2*k+int(odd)
    vertices=blades*blade_size+1
    edges=[]
    for i in range(blades):
        start=1+i*blade_size
        for u in range(start,start+blade_size):
            edges.append((0,u,Fraction(beta)))
            for v in range(u+1,start+blade_size):
                edges.append((u,v,Fraction(alpha)))
    @lru_cache(None)
    def f(mask):
        if mask&1:return Fraction(0)
        active=[(u,v,w) for (u,v,w) in edges if not mask>>u&1 and not mask>>v&1]
        if not active:return Fraction(1)
        total=sum(w for _,_,w in active)
        return sum(w*f(mask|(1<<u)|(1<<v)) for u,v,w in active)/total
    res=f(0)
    return res,f.cache_info().currsize

def main():
    tests=[]
    for n,k in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]:
        for a,b in [(1,1),(2,1),(1,3),(3,2)]:
            v,states=independent(n,k,a,b)
            expected=closed(n,k,a,b)
            assert v==expected,(n,k,a,b,v,expected)
            tests.append((n,k,a,b,states))
    print('exact independent occupancy-state comparisons:',len(tests))
    print('largest independently explored mask-state count:',max(x[-1] for x in tests))
    for n in range(1,6):
        for a,b in [(1,1),(1,5),(3,1)]:
            assert closed(n,1,a,b)==(Fraction(a,a+2*b))**n
    print('one-pair checks:',5*3)
    odd_checks=0
    for n,k in [(1,0),(2,0),(3,0),(1,1),(2,1)]:
        for a,b in [(1,1),(2,1),(1,4)]:
            v,_=independent(n,k,a,b,odd=True)
            assert v==0,(n,k,a,b,v)
            odd_checks+=1
    print('odd-blade checks:',odd_checks)
    print('all tests passed')
if __name__=='__main__':main()
