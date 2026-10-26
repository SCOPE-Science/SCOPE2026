#!/usr/bin/env python3
"""Exact finite tests for sibling-leaf pairs and root-degree dependence.
No imported nonstandard packages. Analytical proof is independent of these tests.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial

def calc(n, conditional=False):
    d = [0] * (n + 1)
    # direct recursion explores every increasing-parent tree
    count = sum_d = sum_z = sum_dz = 0
    pe = { (v,a,b):[0,0] for v in range(1,n-1) for a in range(v+1,n) for b in range(a+1,n+1)} if conditional else {}
    for parents in product(*(range(1,j) for j in range(2,n+1))):
        d = [0]*(n+1)
        for p in parents: d[p] += 1
        r=d[1]
        leaves=[j for j in range(2,n+1) if d[j]==0]
        z=sum(parents[a-2] == parents[b-2] for idx,a in enumerate(leaves) for b in leaves[idx+1:])
        count +=1;sum_d+=r;sum_z+=z;sum_dz+=r*z
        if conditional:
            for i,a in enumerate(leaves):
                for b in leaves[i+1:]:
                    v=parents[a-2]
                    if v==parents[b-2]:
                        pe[v,a,b][0] += 1
                        pe[v,a,b][1] += r
    assert count == factorial(n-1), (n,count)
    meanz=Fraction(sum_z,count)
    meanr=Fraction(sum_d,count)
    cov=Fraction(sum_dz,count)-meanr*meanz
    assert meanz==Fraction(n,6),(n,'E Z',meanz)
    predicted=Fraction(4*n*n-15*n+12,6*(n-1)*(n-2))
    assert cov==predicted,(n,'covariance',cov,predicted)
    if conditional:
        for (v,a,b),(ec,es) in pe.items():
            assert Fraction(ec,count)==Fraction(1,(n-1)*(n-2)),(n,v,a,b,ec)
            shift=Fraction(es,ec)-meanr
            expected=2*(v==1)-Fraction(1,n-2)-Fraction(1,n-1)
            assert shift==expected,(n,v,a,b,shift,expected)
    return (n,count,len(pe),meanz,cov)

def run():
    tests=0
    for n in range(3,10):
        n,trees,num_events,meanz,cov=calc(n,True)
        tests+=2+2*num_events
        print('n',n,'trees',trees,'triple events',num_events,'E pairs',meanz,'cov',cov)
    print('PASS',tests,'exact identities, exhaustive n=3..9')

if __name__=='__main__': run()
