#!/usr/bin/env python3
"""Exact reproducibility checks for a consecutive-pattern covariance theorem.

Only the Python standard library is needed.  Polynomial-degree reasoning in
RESULT.md upgrades the four-point coefficient check to a formal identity.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

POLYNOMIALS = {
 '1234': (3,-9,6), '1243': (2,-6,-2), '1324': (3,-15,18),
 '1342': (2,-18,40), '1423': (1,-3,-4), '1432': (1,-9,26),
 '2134': (2,-6,-2), '2143': (1,-3,-10), '2314': (1,-3,-4),
 '2341': (-1,9,-26), '2413': (-1,9,-26), '2431': (-2,18,-40),
 '3124': (2,-18,40), '3142': (1,-21,62), '3214': (1,-9,26),
 '3241': (-1,3,4), '3412': (-1,-9,46), '3421': (-2,6,2),
 '4123': (-1,9,-26), '4132': (-1,3,4), '4213': (-2,18,-40),
 '4231': (-3,27,-54), '4312': (-2,6,2), '4321': (-3,21,-42),
}
P2={'12':lambda n:Fraction(1,n),'21':lambda n:Fraction(-1,n)}
P3={'123':lambda n:Fraction(1,n),
    '132':lambda n:Fraction(n-3,2*n*(n-1)),
    '213':lambda n:Fraction(n-3,2*n*(n-1)),
    '231':lambda n:Fraction(-1,2*n),
    '312':lambda n:Fraction(-1,2*n),
    '321':lambda n:Fraction(-(n-3),n*(n-1))}

def C(n,k):
    return comb(n,k) if isinstance(n,int) and n>=0 and 0<=k<=n else 0

def poly(p,n):
    a,b,c=POLYNOMIALS[p]
    return a*n*n+b*n+c

def boundary(n,pat):
    k=len(pat)
    b=0
    for r,t in enumerate(pat,1):
        t=int(t)
        for j in range(1,r):
            b+=C(j-1,t-1)*C(n-j,k-t)
        for j in range(n-k+r+1,n+1):
            b+=C(j-1,t-1)*C(n-j,k-t)
    return b

def universal_cov(n,pat):
    k=len(pat)
    assert n>=k>=2
    den=factorial(n-1)//factorial(n-k)
    return (Fraction(1,factorial(k-2))-Fraction(boundary(n,pat),den))/n

def closed_cov(n,pat):
    k=len(pat)
    if k==4:return Fraction(poly(pat,n),6*n*(n-1)*(n-2))
    if k==3:return P3[pat](n)
    return P2[pat](n)

checks=0
# All k=4 boundary sums are polynomials of degree <=3. The displayed
# identity has degree <=3; equality at four distinct n implies identity.
for pat in POLYNOMIALS:
    for n in range(4,8):
        # B=(n-3)*[(n-1)(n-2)/2 - P(n)/6]
        assert 6*boundary(n,pat)==(n-3)*(3*(n-1)*(n-2)-poly(pat,n)),(n,pat)
        checks+=1

# Exact test of all closed forms beyond the interpolation points.
for k in (2,3,4):
    for p in permutations(range(1,k+1)):
        pat=''.join(map(str,p))
        for n in range(k,81):
            assert universal_cov(n,p)==closed_cov(n,pat),(n,pat)
            checks+=1

# Exhaustive full-permutation mixed moments; independent of boundary code.
number_of_permutations=0
moments=0
for n in range(2,10):
    fs=[factorial(x) for x in range(n+1)]
    counts={k:{''.join(map(str,p)):0 for p in permutations(range(1,k+1))}
            for k in (2,3,4) if k<=n}
    fp_weight={k:{p:0 for p in counts[k]} for k in counts}
    for arr in permutations(range(1,n+1)):
        f=sum(arr[i]==i+1 for i in range(n))
        for k in counts:
            for start in range(n-k+1):
                win=arr[start:start+k]
                pat=''.join(str(1+sum(z<value for z in win)) for value in win)
                counts[k][pat]+=1
                fp_weight[k][pat]+=f
        number_of_permutations+=1
    for k in counts:
        for pat in counts[k]:
            cov=Fraction(fp_weight[k][pat]-counts[k][pat],fs[n])
            assert cov==closed_cov(n,pat),(n,pat,cov,closed_cov(n,pat))
            moments+=1
# Sharp integer sign reversal classification.
reversals=set()
for pat in POLYNOMIALS:
    signs={0}
    signs=set()
    for n in range(4,200):
        v=poly(pat,n)
        signs.add((v>0)-(v<0))
    if {-1,1}<=signs:reversals.add(pat)
assert reversals=={'2143','3142','4231'},reversals
assert [n for n in range(4,40) if poly('2143',n)==0]==[5]
assert [n for n in range(4,40) if poly('4231',n)==0]==[6]
assert poly('3142',17)<0 and poly('3142',18)>0
checks+=3
print('VERIFY_OK polynomial_4point_certificates=96 exact_formula_checks=%d exhaustive_permutations=%d exhaustive_mixed_moments=%d reversal_patterns=2143,3142,4231' % (checks,number_of_permutations,moments))
