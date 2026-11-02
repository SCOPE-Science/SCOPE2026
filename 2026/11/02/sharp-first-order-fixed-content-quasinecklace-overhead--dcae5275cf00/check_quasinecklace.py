"""Independent finite checks for binary fixed-content quasinecklaces.

Run: python3 check_quasinecklace.py
No external packages required.
"""
from itertools import combinations
from math import comb, gcd, factorial
from fractions import Fraction


def phi(d):
    return sum(gcd(j,d)==1 for j in range(1,d+1))


def divisors(x):
    return [d for d in range(1,x+1) if x%d==0]


def coefficient_bounded(s, max_value, degree):
    if degree == 0: return int(s == 0)
    if max_value == 0: return int(s == 0)
    return sum((-1)**j * comb(degree,j) * comb(s - j*(max_value+1) + degree-1, degree-1)
               for j in range(degree+1) if s >= j*(max_value+1))


def formula_Q(r, m):
    if r == 0: raise ValueError('r must be positive')
    return sum(coefficient_bounded(m-h,h,r-1) for h in range(m+1))


def formula_N(r, m):
    if r == 0: raise ValueError('r must be positive')
    return sum(phi(d)*comb((r+m)//d-1,r//d-1)
               for d in divisors(gcd(r,m)))//r


def direct_quasi(w):
    if len(set(w)) == 1: return True
    a=min(w)
    run=0
    best=0
    for c in w:
        run=run+1 if c==a else 0
        best=max(best,run)
    if w[:best]!= (a,)*best or w[-1]==a: return False
    b=w[best]
    for j in range(1,len(w)-best):
        if w[j:j+best] == (a,)*best and w[j+best]<b:
            return False
    return True


def direct_necklace(w):
    return all(w <= w[i:]+w[:i] for i in range(1,len(w)))


def gaps(r,m):
    if r==1:
        yield (m,)
    else:
        for x in range(m+1):
            for z in gaps(r-1,m-x):
                yield (x,)+z


checks=0
# Independently check both definitions for all fixed-composition words
for n in range(2,18):
    for r in range(1,min(n,8)+1):
        q=ncount=0
        for twos in combinations(range(n),r):
            w=tuple(int(i in twos) for i in range(n))
            q+=direct_quasi(w)
            ncount+=direct_necklace(w)
            checks+=1
        assert q==formula_Q(r,n-r), ('quasi',n,r,q,formula_Q(r,n-r))
        assert ncount==formula_N(r,n-r), ('neck',n,r,ncount,formula_N(r,n-r))
# Independent gap-orbit verification, including periodic gap tuples
for r in range(1,8):
    for m in range(0,17):
        qq=nn=0
        for g in gaps(r,m):
            qq+=int(g[0] == max(g))
            nn+=int(g == max(g[i:]+g[:i] for i in range(r)))
            # last line chooses lexicographically largest gap tuple
            checks+=1
        assert qq == formula_Q(r,m),('gapQ',r,m,qq,formula_Q(r,m))
        assert nn == formula_N(r,m),('gapN',r,m,nn,formula_N(r,m))
# Exact weight-three excess identity
for m in range(0,1000):
    assert formula_Q(3,m)-formula_N(3,m)==m//2-m//3
    checks+=1
# Leading asymptotic coefficient: finite corroboration only.
for r in range(3,9):
    m=400
    delta=formula_Q(r,m)-formula_N(r,m)
    leading=Fraction(m**(r-2),2*r*factorial(r-2))
    ratio=float(Fraction(delta,1)/leading)
    assert 0.8 < ratio < 1.15,(r,ratio)
    print(f'r={r} m={m} excess={delta} leading_ratio={ratio:.6f}')
    checks+=1
print(f'PASS {checks} direct/combinatorial checks; exhaustive n<=17 and r<=8, gap orbit checks m<=16 and r<=7.')
