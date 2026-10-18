#!/usr/bin/env python3
"""Exact three-nonzero-digit palindrome census (standalone standard-library checker)."""
from itertools import product


def integer_product(a, b, c, g, h):
    # a*10**d + b*10**g + c, d=2*g+h, and its reversal.
    d = 2*g+h
    A = a*10**d+b*10**g+c
    A_rev = c*10**d+b*10**(d-g)+a
    return A*A_rev


def coefficient_product(a, b, c, g, h):
    # Formal multiplication, independently of the integer product.
    d = 2*g+h
    v = [0]*(2*d+3)
    for exponent, coefficient in (
        (0, a*c), (g, a*b), (g+h, b*c), (2*g+h, a*a+b*b+c*c),
        (3*g+h, b*c), (3*g+2*h, a*b), (4*g+2*h, a*c)
    ):
        v[exponent] += coefficient
    digits=[]
    carry=0
    for raw in v:
        q, r = divmod(raw+carry,10)
        digits.append(r)
        carry=q
    while carry:
        carry,r=divmod(carry,10)
        digits.append(r)
    while len(digits)>1 and digits[-1]==0:
        digits.pop()
    return digits


def is_pal(x):
    s=str(x)
    return s==s[::-1]


def run():
    # The finite certificate required by the proof: exactly four short-gap
    # cases and all 9^3 possible digit triples.
    short_gap_cases=((1,0),(1,1),(1,2),(2,0))
    for g,h in short_gap_cases:
        d=2*g+h
        bad=[]
        for a,b,c in product(range(1,10),repeat=3):
            x=integer_product(a,b,c,g,h)
            if len(str(x))==2*d+2 and is_pal(x):
                bad.append((a,b,c))
        assert bad==[],(g,h,bad)
    # Independent three-digit boundary census for the g=1,h>=3 regime.
    outer=[]
    for a,b,c in product(range(1,10),repeat=3):
        U=a*(10*c+b)
        V=a*(10*b+c)
        if U>=100 and str(U)==str(V).zfill(3)[::-1]:
            outer.append((a,b,c,U,V))
    assert outer==[(7,8,8,616,616),(8,7,7,616,616)]
    assert 101*8*8+10*(7*7+8*8+8*8)==8234
    assert 101*7*7+10*(8*8+7*7+7*7)==6569
    cases=0
    positive=0
    expected_triples={(1,1,1), (1,1,2), (1,2,1), (2,1,1),
                      (1,2,2), (2,1,2), (2,2,1)}
    count_grid={}
    for g,h in product(range(1,8),range(0,8)):
        recognized=set()
        for a,b,c in product(range(1,10), repeat=3):
            product_value=integer_product(a,b,c,g,h)
            digits=coefficient_product(a,b,c,g,h)
            assert product_value==sum(v*10**i for i,v in enumerate(digits)), (a,b,c,g,h)
            p0=is_pal(product_value)
            p1=(digits==digits[::-1])
            assert p0==p1, (a,b,c,g,h)
            expect=(a*a+b*b+c*c <=9)
            assert p0==expect, (a,b,c,g,h,p0,expect)
            cases+=1
            positive+=p0
            if p0: recognized.add((a,b,c))
        assert recognized==expected_triples, (g,h,recognized)
        count_grid[g,h]=len(recognized)
    # Supplementary tests outside the finite reduction window; not an infinite proof.
    far=0
    for g,h in ((1,31),(23,0),(8,51),(45,8),(101,137),(103,303)):
        for a,b,c in product(range(1,10),repeat=3):
            p0=is_pal(integer_product(a,b,c,g,h))
            p1=(a*a+b*b+c*c<=9)
            assert p0==p1, (g,h,a,b,c)
            far+=1
    print('SHORT_GAP_PROOF_CASES', 4*9**3)
    print('BOUNDARY_CENSUS_CASES',9**3)
    print('FINITE_CORE_CASES',cases)
    print('PALINDROMIC_CORE_CASES',positive)
    print('GRID_CELLS',len(count_grid))
    print('TRIPLES_PER_CELL',sorted(set(count_grid.values())))
    print('WIDE_GAP_SUPPLEMENTARY_TESTS',far)
    print('PASS')

if __name__=='__main__':
    run()
