"""Exact checks for the comparison-cost/inversion decoupling theorem.

Run: python verify.py
Requires only Python 3 standard library.
"""
from itertools import permutations
from fractions import Fraction
from collections import defaultdict
from math import factorial

def cost(seq):
    if len(seq) <= 1:
        return 0
    pivot=seq[0]
    return len(seq)-1 + cost(tuple(x for x in seq[1:] if x<pivot)) + cost(tuple(x for x in seq[1:] if x>pivot))

def inv(seq):
    return sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])

def harmonic(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction())

def rankperm(seq):
    return tuple(1+sum(x<y for y in seq) for x in seq)

def exhaustive(n):
    buckets=defaultdict(list)
    sums=[0,0,0,0]
    for p in permutations(range(1,n+1)):
        c=cost(p); i=inv(p)
        buckets[c].append(i)
        sums[0]+=c; sums[1]+=i; sums[2]+=c*i; sums[3]+=i*i
        rev=tuple(n+1-x for x in p)
        assert cost(rev)==c
        assert inv(rev)+i==n*(n-1)//2
    total=factorial(n)
    assert Fraction(sums[0],total)==2*(n+1)*harmonic(n)-4*n
    assert Fraction(sums[1],total)==Fraction(n*(n-1),4)
    assert Fraction(sums[2],total)==Fraction(sums[0]*sums[1],total**2)
    assert Fraction(sums[3],total)-Fraction(sums[1],total)**2==Fraction(n*(n-1)*(2*n+5),72)
    for c,ls in buckets.items():
        assert Fraction(sum(ls),len(ls))==Fraction(n*(n-1),4)
        assert sorted(ls)==sorted(n*(n-1)//2-i for i in ls)
    if n==3:
        assert len(buckets)==2  # nonindependence is explicit, not merely conjectured
        assert (0 not in buckets[min(buckets)])
    print('n',n,'permutations',total,'cost states',len(buckets),'exact covariance 0 and conditional symmetry OK')

def check_martingale(n):
    # Conditional next insertion rank is uniform; test path-depth and centered martingale identity.
    for seq in permutations(range(1,n+1)):
        c=cost(seq)
        ext=[]
        for r in range(1,n+2):
            expanded=tuple(x+int(x>=r) for x in seq)+(r,)
            ext.append(cost(expanded)-c)
        assert sum(ext)==c+2*n
        cnext=Fraction(sum(cost(tuple(x+int(x>=r) for x in seq)+(r,)) for r in range(1,n+2)),n+1)
        assert cnext == Fraction(n+2,n+1)*c+Fraction(2*n,n+1)
    print('n',n,'one-step martingale and external gap identity OK')

if __name__=='__main__':
    for n in range(1,9):
        exhaustive(n)
    for n in range(1,7):
        check_martingale(n)
    print('VERIFY_OK')
