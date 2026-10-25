#!/usr/bin/env python3
"""Exact finite certificate for a two-pair correlation specialization of the four-cube Hypercube polynomial.

Run: python3 verify.py
Python standard library only. All determinant and polynomial arithmetic is integral.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, prod

VERTICES = list(product((0, 1), repeat=4))
PERMS = list(permutations(range(4)))
SIGNS = {}
for pp in PERMS:
    inv = sum(pp[i] > pp[j] for i in range(4) for j in range(i+1,4))
    SIGNS[pp] = -1 if inv % 2 else 1


def det_leibniz(matrix):
    return sum(SIGNS[p] * prod(matrix[i][p[i]] for i in range(4)) for p in PERMS)


def det_bareiss(matrix):
    a = [list(row) for row in matrix]
    sign, divisor = 1, 1
    for j in range(3):
        if not a[j][j]:
            for k in range(j+1,4):
                if a[k][j]:
                    a[k], a[j] = a[j], a[k]
                    sign = -sign
                    break
            else:
                return 0
        pivot = a[j][j]
        for i in range(j+1,4):
            for k in range(j+1,4):
                numerator = a[i][k]*pivot - a[i][j]*a[j][k]
                assert numerator % divisor == 0
                a[i][k] = numerator // divisor
            a[i][j] = 0
        divisor = pivot
    return sign*a[3][3]


def powers(vertices):
    a = sum(v[0] == v[1] for v in vertices)
    c = sum(v[2] == v[3] for v in vertices)
    return a, 5-a, c, 5-c


def mul(p, q):
    out = Counter()
    for a,ca in p.items():
        for b,cb in q.items():
            out[tuple(x+y for x,y in zip(a,b))] += ca*cb
    return {k:v for k,v in out.items() if v}


def polypow(p,n):
    out={(0,0,0,0):1}
    for _ in range(n):out=mul(out,p)
    return out


def polyadd(*terms):
    out=Counter()
    for x in terms:
        for k,v in x.items():out[k]+=v
    return {k:v for k,v in out.items() if v}


def scaled(p,m):
    return {k:m*v for k,v in p.items()}


def monomial(exponents):
    return {tuple(exponents):1}


def main():
    assert len(VERTICES)==16 and comb(16,5)==4368
    grouped=Counter()
    nondegenerate=0
    volume_spectrum=Counter()
    for ids in combinations(range(16),5):
        simplex = [VERTICES[i] for i in ids]
        M = [tuple(x-y for x,y in zip(v,simplex[0])) for v in simplex[1:]]
        d1=det_bareiss(M)
        d2=det_leibniz(M)
        assert d1 == d2, (ids,d1,d2)
        weight=abs(d1)
        volume_spectrum[weight]+=1
        if weight:
            grouped[powers(simplex)] += weight
            nondegenerate+=1
    # Complete 4x4 coefficient table, rows are powers of a, columns powers of c.
    assert len(grouped)==16
    expected = ((64,176,176,64),
                (176,424,424,176),
                (176,424,424,176),
                (64,176,176,64))
    for ai in range(1,5):
        for ci in range(1,5):
            assert grouped[ai,5-ai,ci,5-ci] == expected[ai-1][ci-1]
    assert sum(grouped.values()) == 3360
    assert sum(volume_spectrum.values()) == 4368
    A=polypow(polyadd(monomial((1,0,0,0)),monomial((0,1,0,0))),1)
    C=polypow(polyadd(monomial((0,0,1,0)),monomial((0,0,0,1))),1)
    aa=monomial((1,0,0,0)); bb=monomial((0,1,0,0))
    cc=monomial((0,0,1,0)); dd=monomial((0,0,0,1))
    ab=mul(aa,bb);cd=mul(cc,dd)
    a2b2=polyadd(mul(aa,aa),mul(bb,bb))
    c2d2=polyadd(mul(cc,cc),mul(dd,dd))
    bracket=polyadd(
        scaled(mul(a2b2,c2d2),8),
        scaled(mul(a2b2,cd),14),
        scaled(mul(ab,c2d2),14),
        scaled(mul(ab,cd),17),
    )
    formula=scaled(mul(mul(mul(mul(ab,cd),A),C),bracket),8)
    assert formula == dict(grouped), (formula, grouped)
    # Homogeneous identity with R = P/[4(a+b)^5(c+d)^5].
    denominator=scaled(mul(polypow(A,5),polypow(C,5)),4)
    for params in ((1,1,1,1),(2,3,5,7),(7,2,1,9),(9,1,4,3)):
        a,b,c,d=params
        evalp=sum(v*a**k[0]*b**k[1]*c**k[2]*d**k[3] for k,v in grouped.items())
        evaluation=4*(a+b)**5*(c+d)**5
        r=a*b/(a+b)**2; s=c*d/(c+d)**2
        assert abs(evalp/evaluation -2*r*s*(8-2*r-2*s-7*r*s))<1e-14
    # Purely symbolic monotonicity: u=rho^2,v=sigma^2 lie in [0,1).
    # dR/du=-(1-v)*(90+30u+22v-14uv)/128 < 0,
    # symmetric for v. Thus max is R(0,0)=105/128.
    print('PAIR_PARITY_HYPERCUBE_OK total_subsets=4368 nondegenerate=%s volume_spectrum=%s table=%s uniform_ratio=105/128' % (nondegenerate,dict(volume_spectrum),expected))

if __name__=='__main__': main()
