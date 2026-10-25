"""Exact finite checks of product laws for rank-uniform partial bijections."""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial
from fractions import Fraction


def partial_bijections(n, rank):
    for source in combinations(range(n), rank):
        for target in permutations(range(n), rank):
            f = [-1] * n
            for i, j in zip(source, target):
                f[i] = j
            yield tuple(f)


def compose(g, f):
    """Return g after f, with -1 denoting undefined."""
    return tuple(-1 if v < 0 else g[v] for v in f)


def overlap_probability(n, deleted_sizes, s):
    prod = 1
    for a in deleted_sizes:
        prod *= comb(n, a)
    total = sum((-1) ** j * comb(s, j) *
                product_binomial(s-j, deleted_sizes)
                for j in range(s+1))
    return Fraction(total, prod)


def product_binomial(top, sizes):
    out=1
    for a in sizes:
        out *= comb(top, a) if top >= a else 0
    return out


def expected_probability(n, sizes, f):
    s=sum(t < 0 for t in f)
    return overlap_probability(n, sizes, s) * Fraction(factorial(s), factorial(n))


def verify(n, deleted_sizes):
    states=Counter({tuple(range(n)):1})
    denominator=1
    for a in deleted_sizes:
        layer=list(partial_bijections(n,n-a))
        denominator *= len(layer)
        nxt=Counter()
        for f,c in states.items():
            for g in layer:
                nxt[compose(g,f)] += c
        states=nxt
    assert sum(states.values()) == denominator
    for r in range(n+1):
        for f in partial_bijections(n,r):
            assert Fraction(states[f],denominator) == expected_probability(n,deleted_sizes,f), (n,deleted_sizes,f)
    return len(states)


def stirling2(k,s):
    row=[1]+[0]*s
    for _ in range(k):
        nxt=[0]*(s+1)
        for j in range(1,s+1):
            nxt[j]=j*row[j]+row[j-1]
        row=nxt
    return row[s]


def extra_check():
    for n in range(1,8):
        for k in range(0,8):
            for s in range(n+1):
                p=overlap_probability(n,[1]*k,s)
                expect=Fraction(factorial(s)*stirling2(k,s),n**k)
                assert p == expect, (n,k,s,p,expect)
        expected_absorption = sum(Fraction((-1)**(j+1)*comb(n,j),1) /
                                  (1-Fraction(n-j,n)) for j in range(1,n+1))
        assert expected_absorption == n*sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))
    return 'STIRLING_AND_HITTING_TIME_OK'




def falling(n, j):
    z = 1
    for i in range(j):
        z *= n-i
    return z


def spectral_check():
    tests = 0
    for n in range(1, 10):
        for a in range(n+1):
            for r in range(n+1):
                for j in range(n+1):
                    lhs = sum(Fraction(comb(r,s)* (comb(n-r,n-a-s) if 0 <= n-a-s <= n-r else 0),comb(n,n-a)) * falling(s,j) for s in range(r+1) if n-a-s >= 0)
                    rhs = Fraction(comb(n-j,a),comb(n,a))*falling(r,j) if n-j>=a else 0
                    assert lhs==rhs,(n,a,r,j,lhs,rhs)
                    tests+=1
    return tests

def main():
    num=0
    cases=[]
    for n in range(1,5):
        for profile in [(1,), (1,1), (1,1,1), (1,2), (2,2)]:
            if max(profile)>n: continue
            count=verify(n,profile)
            cases.append((n,profile,count))
            num += 1
    for profile in [(1,1),(1,2),(2,2)]:
        count=verify(5,profile)
        cases.append((5,profile,count))
        num+=1
    assert extra_check()=='STIRLING_AND_HITTING_TIME_OK'
    tests=spectral_check()
    print('VERIFY_OK_ROOK_MONOID_BATCH_COUPON_CONVOLUTION', num, 'product-profiles', len(cases), 'spectral-checks', tests)
    for case in cases: print(case)

if __name__=='__main__':
    main()
