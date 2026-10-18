#!/usr/bin/env python3
"""Compare independent subgroup, partition, and generating-function enumerations."""
from collections import Counter, defaultdict
from math import comb
from verify_subgroups import all_subspaces,signature,all_structures

def gaussian(k,d):
    num=den=1
    for j in range(d):
        num*=2**(k-j)-1
        den*=2**(d-j)-1
    assert num%den==0
    return num//den

def stirling(n,r):
    a=[[0]*(r+1) for _ in range(n+1)];a[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(r,i)+1):a[i][j]=a[i-1][j-1]+j*a[i-1][j]
    return a[n][r]

def coeffs(factors,lim):
    arr=[1]+[0]*lim
    for size,multiplicity in factors:
        for _ in range(multiplicity):
            for n in range(size,lim+1):arr[n]+=arr[n-size]
    return arr

def main():
    for k in range(1,5):
        sizes=Counter((1<<k)//len(h) for h in all_subspaces(k))
        predicted=Counter({1<<d:gaussian(k,d) for d in range(k+1)})
        assert sizes==predicted,(k,sizes,predicted)
        groups=defaultdict(set)
        for h in all_subspaces(k):groups[signature(k,h)].add((1<<k)//len(h))
        minimum=Counter(min(x) for x in groups.values())
        expected=Counter()
        for r in range(k+1):
            d=(r+1-1).bit_length() # ceil(log2(r+1))
            expected[1<<d]+=stirling(k+1,r+1)
        assert minimum==expected,(k,minimum,expected)
        print('k',k,'subgroups by orbit size',sorted(sizes.items()),'signatures by minimum orbit size',sorted(minimum.items()))
        if k<=3:
            iso=coeffs(sorted(sizes.items()),8)
            logical=coeffs(sorted(minimum.items()),8)
            for n in range(1,9):
                hs,items=all_structures(k,n)
                assert len(items)==iso[n]
                assert len({fp for fp,_ in items})==logical[n]
            print('  isomorphism counts n=1..8:',iso[1:])
            print('  C2 class counts n=1..8:',logical[1:])
    print('VERIFY_SERIES_OK')
if __name__=='__main__':main()
