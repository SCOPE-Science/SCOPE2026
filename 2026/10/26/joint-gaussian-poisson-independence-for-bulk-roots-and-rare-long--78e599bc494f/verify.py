"""Finite permutation checks of cyclic-valley and root-gap identities."""
from itertools import permutations
from fractions import Fraction
from math import factorial


def a(i):
    return Fraction(i * 2 ** (i + 1), (i+1)*(i+2)*(i+4)*factorial(i))


def scores(seq):
    n=len(seq)
    roots=[j for j in range(n) if seq[j]<seq[(j-1)%n] and seq[j]<seq[(j+1)%n]]
    gap_count={i:0 for i in range(1,n)}
    for j, x in enumerate(roots):
        g=(roots[(j+1)%len(roots)]-x)%n
        if len(roots)==1: g=n
        assert 2<=g<=n
        gap_count[g-1]+=1
    assert sum(gap_count.values())==len(roots)
    assert sum((i+1)*v for i,v in gap_count.items())==n
    return len(roots), gap_count

for k in (7,8):
    n=factorial(k)
    sumr=sumr2=0
    ds={i:0 for i in range(1,k-3)}
    for p in permutations(range(k)):
        r,dc=scores(p)
        sumr+=r;sumr2+=r*r
        for i in ds:ds[i]+=dc[i]
    assert Fraction(sumr,n)==Fraction(k,3)
    assert Fraction(sumr2,n)-Fraction(k*k,9)==Fraction(2*k,45)
    for i,total in ds.items():
        assert Fraction(total,n)==k*a(i),(k,i,Fraction(total,n),k*a(i))
    print(f'K={k}: checked {n} permutations; means, variances, gap sums verified for i=1..{k-4}')
print('All finite consistency checks passed; infinite joint theorem uses analytic proof.')
