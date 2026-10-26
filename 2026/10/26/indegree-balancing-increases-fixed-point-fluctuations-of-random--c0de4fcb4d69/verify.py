"""Exact enumeration for fixed-point/indegree dependence in uniform random mappings."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def binpmf(m, r, n):
    if r < 0 or r > m:
        return Fraction(0)
    return Fraction(comb(m, r) * (n-1) ** (m-r), n ** m)


def claimed_cov(n, r):
    m = n - 2
    return Fraction(n-1, n*n) * (-binpmf(m,r,n) + 2*binpmf(m,r-1,n) - binpmf(m,r-2,n))


def check(n):
    count = n**n
    sum_f = 0
    sum_f2 = 0
    sum_x = [0]*(n+1)
    sum_f_x = [0]*(n+1)
    sum_f2_x = [0]*(n+1)
    degrees = defaultdict(lambda: [0, 0, 0]) if n <= 6 else None
    for values0 in product(range(n), repeat=n):
        f = sum(v == i for i,v in enumerate(values0))
        f2 = f*(f-1)
        d = [0]*n
        for v in values0: d[v] += 1
        profile = [0]*(n+1)
        for v in d: profile[v] += 1
        sum_f += f
        sum_f2 += f2
        for r,x in enumerate(profile):
            sum_x[r] += x
            sum_f_x[r] += f*x
            sum_f2_x[r] += f2*x
        if degrees is not None:
            row = degrees[tuple(d)]; row[0] += 1; row[1] += f; row[2] += f2
    assert sum_f == count
    assert Fraction(sum_f2,count) == Fraction(n-1,n)
    for r in range(n+1):
        assert Fraction(sum_f_x[r],count) == Fraction(sum_x[r],count), (n,r,'first covariance')
        found = Fraction(sum_f2_x[r],count) - Fraction(sum_f2*sum_x[r],count*count)
        assert found == claimed_cov(n,r), (n,r,found,claimed_cov(n,r))
        sgn = (found > 0)-(found < 0)
        wanted = -1 if r==0 or r>=3 or (n==2 and r==2) else (0 if n==3 and r==2 else 1)
        assert sgn == wanted, (n,r,sgn,wanted)
    if degrees is not None:
        for d, (cnt, fsum, f2sum) in degrees.items():
            c = sum(v*(v-1)//2 for v in d)
            assert Fraction(fsum,cnt) == 1, (n,d,'conditional E F')
            assert Fraction(f2sum,cnt) == 1-Fraction(2*c,n*(n-1)), (n,d,'conditional E F2')
    print('EXHAUSTIVE_PASS',n,'mappings',count,'degree_profiles',len(degrees) if degrees is not None else 'unchecked', 'multiplicity_classes',n+1)

for n in range(2,8):
    check(n)
for n in (2,3,4,5,11,47,100):
    for r in range(n+1):
        sgn = (claimed_cov(n,r)>0)-(claimed_cov(n,r)<0)
        target = -1 if r==0 or r>=3 or (n==2 and r==2) else (0 if n==3 and r==2 else 1)
        assert sgn==target, (n,r)
print('EXACT_ALL_R_SIGN_PASS selected n=2..100')
print('VERIFY_OK')
