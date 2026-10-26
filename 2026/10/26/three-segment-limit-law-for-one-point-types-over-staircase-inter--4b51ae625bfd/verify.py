#!/usr/bin/env python3
"""Independent finite one-point extension enumeration for staircase interval orders."""
from collections import Counter
from fractions import Fraction
from itertools import product


def brute(n):
    # An ordered list of n lower a_i and n upper b_j (i,j are 0-based),
    # with a_i < b_j exactly when i <= j.  Each ternary choice labels
    # an existing parameter as below x, incomparable to x, or above x.
    N = 2 * n + 1
    x = 2 * n
    base = [[False] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                base[i][n + j] = True
    dist = Counter()
    for status in product((-1, 0, 1), repeat=2*n):
        order = [row[:] for row in base]
        for i, s in enumerate(status):
            if s == -1: order[i][x] = True
            if s == 1: order[x][i] = True
        # Directly test the enlarged strict relation's transitivity,
        # not the ideal/filter decomposition used by the proof.
        valid = True
        for i in range(N):
            if order[i][i]: valid = False; break
            for j in range(N):
                if order[i][j]:
                    for k in range(N):
                        if order[j][k] and not order[i][k]:
                            valid = False; break
                    if not valid: break
            if not valid: break
        if valid:
            dist[(sum(s == -1 for s in status),sum(s == 1 for s in status))] += 1
    return dist


def polynomial(n):
    # Independent coefficient construction of the explicit conjectured
    # enumerator, using binomial coefficients rather than transitivity.
    from math import comb
    d = Counter()
    # One-sided ideals with first missing lower point i (1-based).
    for i in range(1,n+1):
        for q in range(n):
            d[(i-1+q,0)] += comb(n-1,q)
            d[(0,i-1+q)] += comb(n-1,q)
    # All lower parameters are selected; arbitrary upper parameters.
    for q in range(n+1):
        d[(n+q,0)] += comb(n,q)
        d[(0,n+q)] += comb(n,q)
    d[(0,0)] -= 1
    # Mixed: the earliest selected upper parameter is b_j.
    for j in range(1,n+1):
        for p in range(1,j+1):
            for q in range(n-j+1):
                d[(p,1+q)] += comb(j,p)*comb(n-j,q)
    return +d


def check_small():
    assert polynomial(1) == Counter({(0,0):1,(1,0):1,(2,0):1,(0,1):1,(0,2):1,(1,1):1})
    total=0
    for n in range(1,6):
        a=brute(n); b=polynomial(n)
        assert a==b,(n,a-b,b-a)
        assert sum(a.values())==(2*n+1)*2**n
        # Nonempty two-sided types have the exact independent count.
        assert sum(v for (p,q),v in a.items() if p and q)==(n-1)*2**n+1
        total += sum(a.values())
        print(f'n={n}, types={sum(a.values())}, nonzero_coefficients={len(a)}, mixed={(n-1)*2**n+1}')
    print('FINITE_ENUMERATION_TOTAL_TYPES=', total)


def asymptotic_moments():
    from math import comb
    # No enumeration here: exact finite-n moments from closed coefficients.
    limit_cov=Fraction(-23,192)
    limit_var=Fraction(11,64)
    assert limit_cov/limit_var==Fraction(-23,33)
    for n in (10,30,100):
        d=polynomial(n)
        N=sum(d.values())
        EX=Fraction(sum(a*w for (a,b),w in d.items()),n*N)
        EY=Fraction(sum(b*w for (a,b),w in d.items()),n*N)
        EX2=Fraction(sum(a*a*w for (a,b),w in d.items()),n*n*N)
        EXY=Fraction(sum(a*b*w for (a,b),w in d.items()),n*n*N)
        v=EX2-EX*EX; cov=EXY-EX*EY
        rho=cov/v
        print(f'n={n}, normalized_mean={float(EX):.8f}, corr={float(rho):.8f}')
        assert abs(float(rho)-float(Fraction(-23,33))) < 3/n
    print('LIMIT_MOMENT_IDENTITIES_PASS')

if __name__ == '__main__':
    check_small()
    asymptotic_moments()
    print('ALL_TESTS_PASS')
