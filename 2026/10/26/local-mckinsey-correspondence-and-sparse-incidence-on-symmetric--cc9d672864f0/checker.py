#!/usr/bin/env python3
"""Independent finite tests for symmetric McKinsey-frame classification.

Usage: python3 checker.py. Standard library only.
"""
from math import comb, factorial, exp
from fractions import Fraction


def symmetric_rows(n, code, loops=True):
    rows = [0]*n
    bit=0
    for i in range(n):
        for j in range(i if loops else i+1,n):
            if code & (1<<bit):
                rows[i] |= 1<<j
                rows[j] |= 1<<i
            bit += 1
    return rows


def modal_at(rows,p,w):
    n=len(rows)
    ant = all(rows[u] & p for u in range(n) if (rows[w]>>u)&1)
    cons= any((rows[u] & ((1<<n)-1 ^ p))==0 for u in range(n) if (rows[w]>>u)&1)
    return not ant or cons


def at_all_valuations(rows,w):
    return all(modal_at(rows,p,w) for p in range(1<<len(rows)))


def structural(rows,w):
    return any(rows[u] == (1<<w) for u in range(len(rows)) if (rows[w]>>u)&1)


def globally_involutive(rows):
    return all(row.bit_count()==1 for row in rows)


def involutions(n):
    return sum(factorial(n)//(2**j * factorial(j) * factorial(n-2*j)) for j in range(n//2+1))


def rooted_count_formula(n):
    return sum((-1)**(j+1)*comb(n-1,j)*2**comb(n-j,2) for j in range(1,n))


def rooted_probability(n, p):
    return sum((-1)**(j+1)*comb(n-1,j)*(p**j)*((1-p)**(j*(n-2)-comb(j,2))) for j in range(1,n))


def run():
    checks=0
    for n in range(1,6):
        accepted=0
        for code in range(1<<(n*(n+1)//2)):
            rows=symmetric_rows(n,code)
            ans=[at_all_valuations(rows,w) for w in range(n)]
            predicted=[structural(rows,w) for w in range(n)]
            assert ans==predicted,(n,code,rows,ans,predicted)
            global_direct=all(ans)
            assert global_direct==globally_involutive(rows),(n,code,rows)
            checks += n+1
            accepted += global_direct
        assert accepted==involutions(n),(n,accepted,involutions(n))
        print('symmetric n=',n,'global valid=',accepted)
    for n in range(1,7):
        valid=0
        perfect=0
        hist=[0]*(n+1)
        for code in range(1<<(n*(n-1)//2)):
            rows=symmetric_rows(n,code,loops=False)
            ans=structural(rows,0)
            assert ans==at_all_valuations(rows,0)
            valid += ans
            perfect += globally_involutive(rows)
            hist[sum(structural(rows,i) for i in range(n))] += 1
            checks+=2
        assert valid==rooted_count_formula(n),(n,valid,rooted_count_formula(n))
        assert perfect==(factorial(n)//(2**(n//2)*factorial(n//2)) if n%2==0 else 0)
        assert sum(hist)==(1<<(n*(n-1)//2))
        p=Fraction(1,3)
        weighted=sum(Fraction(1,3)**code.bit_count() * Fraction(2,3)**(n*(n-1)//2-code.bit_count())
                     for code in range(1<<(n*(n-1)//2)) if structural(symmetric_rows(n,code,False),0))
        assert weighted == rooted_probability(n,p)
        print('simple n=',n,'root-valid=',valid,'globally valid=',perfect)
    for c in (0.1,0.5,1,2,4):
        approx = 1-exp(-c*exp(-c))
        assert abs(rooted_probability(500,c/500)-approx)<0.003,(c,rooted_probability(500,c/500),approx)
    print('ALL_CHECKS_OK',checks)

if __name__=='__main__':run()
