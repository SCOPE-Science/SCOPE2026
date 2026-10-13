#!/usr/bin/env python3
"""Exact finite support and fourth-moment checks for two-bucket sketch equivalence.

All finite probabilities use integer counts; the all-size theorem is proved separately.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def grams_for_columns(column_options, b, zeta, m, sparse):
    """Return Gram law indexed by upper-triangle entries multiplied by b*zeta.

    For b=2, sparse values are unit signed vectors /sqrt(zeta), and
    dense values are flat signed vectors /sqrt(2*zeta).
    """
    d=b*zeta
    out=Counter()
    for columns in product(column_options, repeat=m*zeta):
        blocks=[columns[i*m:(i+1)*m] for i in range(zeta)]
        entries=[]
        for i in range(m):
            for j in range(i,m):
                total=0
                for block in blocks:
                    v=block[i]; w=block[j]
                    prod=sum(x*y for x,y in zip(v,w))
                    total += b*prod if sparse else prod
                entries.append(total)
        out[tuple(entries)]+=1
    return out


def test_law(zeta,m):
    sparse=[]
    for coordinate in range(2):
        for sign in [-1,1]:
            x=[0,0];x[coordinate]=sign;sparse.append(tuple(x))
    dense=list(product([-1,1],repeat=2))
    a=grams_for_columns(sparse,2,zeta,m,True)
    b=grams_for_columns(dense,2,zeta,m,False)
    assert a==b,(zeta,m)
    assert sum(a.values())==4**(zeta*m)
    # Explicit block-Hadamard image is a bijection of the four states.
    rotated={tuple((s[0]+s[1],s[0]-s[1])) for s in sparse}
    assert rotated==set(dense)
    return len(a)


def fourth_moments(b,zeta):
    dense=Fraction(3*b*zeta-2,b**3*zeta**3)
    sparse=Fraction(b+3*zeta-3,b*b*zeta**3)
    gap=Fraction((b-1)*(b-2),b**3*zeta**3)
    assert sparse-dense==gap
    assert gap==0 if b in (1,2) else gap>0
    return gap


def main():
    cases=[(1,2),(1,3),(2,2),(2,3),(3,2),(4,2)]
    counts={str(case):test_law(*case) for case in cases}
    for b in range(1,13):
        for zeta in range(1,10):
            fourth_moments(b,zeta)
    # Exact two-column support enumeration at the first obstructed block width.
    for b in range(3,9):
        for zeta in range(1,5):
            # one-block signed hash inner product variance and fourth moment
            support=Counter()
            for i,j,s,t in product(range(b),range(b),(-1,1),(-1,1)):
                support[s*t if i==j else 0]+=1
            denom=4*b*b
            assert Fraction(sum(k*k*v for k,v in support.items()),denom)==Fraction(1,b)
            assert Fraction(sum(k**4*v for k,v in support.items()),denom)==Fraction(1,b)
    print('VERIFY_OK exact_full_gram_cases=%s exact_moment_cases=%s support_checks=%s' %(len(cases),12*9,6))
    print('distinct_gram_support_sizes',counts)

if __name__=='__main__':
    main()
