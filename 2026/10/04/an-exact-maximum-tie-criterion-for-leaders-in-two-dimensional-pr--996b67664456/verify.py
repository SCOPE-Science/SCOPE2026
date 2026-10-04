from fractions import Fraction
from itertools import combinations
from math import comb

def h(n,k,l):
    if l > n-k:
        return Fraction(1,1)
    return Fraction(1,1)-Fraction(comb(n-k,l),comb(n,l))

# Direct subset enumeration of the conditional intersection probability.
for n in range(1,9):
    universe=range(n)
    for k in range(1,n+1):
        A=list(combinations(universe,k))
        for l in range(1,n+1):
            B=list(combinations(universe,l))
            hit=0
            total=len(A)*len(B)
            for a in A:
                sa=set(a)
                for b in B:
                    if sa.intersection(b):
                        hit += 1
            assert Fraction(hit,total)==h(n,k,l)

# Exact rational checks of the algebraic bounds.
for n in range(1,201):
    for k in range(1,n+1):
        for l in range(1,n+1):
            q=h(n,k,l)
            upper=min(Fraction(1,1),Fraction(k*l,n))
            assert q <= upper
            algebraic_lower=Fraction(1,1)-(Fraction(n-k,n) ** l)
            assert q >= algebraic_lower
            if k==1 and l==1:
                assert q==Fraction(1,n)

print('VERIFY_OK')
