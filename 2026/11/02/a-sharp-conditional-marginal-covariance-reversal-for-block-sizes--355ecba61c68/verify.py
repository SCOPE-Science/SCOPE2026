#!/usr/bin/env python3
"""Exact reproducibility checks for conditional block-size covariance in NC partitions.

Run: python3 verify.py
No external packages, internet access, or random seeds are required.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, factorial

checks = 0

def check(cond, *msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def expected_cov(n, k, r):
    """Independent stars-and-bars factorial-moment formula."""
    d = choose(n-1, k-1)
    assert d > 0
    e1 = Fraction(k*choose(n-2, k-2), d)
    er = Fraction(k*choose(n-r-1, k-2), d)
    if k == 2 and r == n-1:
        e1r = Fraction(2, n-1)
    else:
        e1r = Fraction(k*(k-1)*choose(n-r-2,k-3), d)
    return e1r-e1*er


def theorem_cov(n,k,r):
    if n < 3 or r < 2 or r > n or not 1 <= k <= n:
        raise ValueError((n,k,r))
    if r == n-1 and k == 2:
        return Fraction(2*(n-3),(n-1)**2)
    if r >= n-1 or k == 1 or k > n-r+1:
        return Fraction(0)
    p = Fraction(choose(n-r-1,k-2), choose(n-1,k-1))
    return p * Fraction(k*(k-1)*(r*k-2*(n-1)),(n-1)*(n-r-1))


def unconditional_cov(n, r):
    cat = Fraction(choose(2*n,n),n+1)
    a = Fraction(choose(2*n-2,n-1),cat)
    b = Fraction(choose(2*n-r-1,n-1),cat)
    ab = Fraction(n*choose(2*n-r-3,n-2),cat)
    return ab-a*b


def positive_polynomial(n,r):
    return (n+1)*(2*n-r-1)*(2*n-r-2)-2*(2*n-1)*(n-1)*(n-r)


def all_partitions(n):
    """Independent restricted-growth-string enumeration."""
    a = [0]*n
    def rec(pos, ma):
        if pos == n:
            blocks = [[] for _ in range(ma+1)]
            for i,b in enumerate(a): blocks[b].append(i)
            yield tuple(tuple(b) for b in blocks)
            return
        for b in range(ma+2):
            a[pos]=b
            yield from rec(pos+1,max(ma,b))
    yield from rec(1,0)


def is_noncrossing(blocks):
    for i in range(len(blocks)):
        a=blocks[i]
        for b in blocks[i+1:]:
            for p in range(len(a)):
                for q in range(p+1,len(a)):
                    x,y=a[p],a[q]
                    inside=any(x<t<y for t in b)
                    outside=any(t<x or t>y for t in b)
                    if inside and outside:
                        return False
    return True


def profile_count(n,profile):
    k=sum(profile.values())
    v=factorial(n)//factorial(n+1-k)
    for cnt in profile.values():
        check(v%factorial(cnt)==0,(n,profile,v))
        v//=factorial(cnt)
    return v


def direct_tests():
    for n in range(1,11):
        tab=defaultdict(Counter)
        profiles=Counter()
        uncond=defaultdict(Counter)
        total=0
        for blocks in all_partitions(n):
            if not is_noncrossing(blocks):continue
            total+=1
            sizes=Counter(map(len,blocks))
            k=len(blocks)
            profiles[tuple(sorted(sizes.items()))]+=1
            for r in range(2,n+1):
                tab[(k,r)][(sizes[1],sizes[r])]+=1
                uncond[r][(sizes[1],sizes[r])]+=1
        check(total == choose(2*n,n)//(n+1), (n,total))
        for prof,num in profiles.items():
            check(num==profile_count(n,dict(prof)),(n,prof,num))
        for r in range(2,n+1):
            counter=uncond[r]
            den=sum(counter.values())
            e1=Fraction(sum(a*v for (a,b),v in counter.items()),den)
            er=Fraction(sum(b*v for (a,b),v in counter.items()),den)
            e12=Fraction(sum(a*b*v for (a,b),v in counter.items()),den)
            check(e12-e1*er==unconditional_cov(n,r),(n,r,'marginal'))
            check(unconditional_cov(n,r)<0,(n,r,'marginal sign'))
        if n<3:continue
        for k in range(1,n+1):
            for r in range(2,n+1):
                counter=tab[(k,r)]
                den=sum(counter.values())
                check(den==choose(n,k)*choose(n,k-1)//n, (n,k,r,den))
                e1=Fraction(sum(s*v for (s,t),v in counter.items()),den)
                er=Fraction(sum(t*v for (s,t),v in counter.items()),den)
                e12=Fraction(sum(s*t*v for (s,t),v in counter.items()),den)
                actual=e12-e1*er
                check(actual==expected_cov(n,k,r),(n,k,r,actual,'moment'))
                check(actual==theorem_cov(n,k,r),(n,k,r,actual,'theorem'))
        print(f'exhaustive NC check n={n}: {total} partitions')


def exact_formula_tests():
    for n in range(3,161):
        for k in range(1,n+1):
            for r in range(2,n+1):
                cv=expected_cov(n,k,r)
                check(cv==theorem_cov(n,k,r),(n,k,r,cv))
                if r <= n-2 and 2 <= k <= n-r+1:
                    z=r*k-2*(n-1)
                    check((cv>0)-(cv<0)==(z>0)-(z<0),(n,k,r,z,cv))
        for r in range(2,n+1):
            check(unconditional_cov(n,r)<0,(n,r,'all-n marginal'))
            d=positive_polynomial(n,r)
            check(d>0,(n,r,d))
            check(4*(n+1)*d == (2*(n+1)*r-(7*n-5))**2 + (16*(n-3)**3+87*(n-3)**2+144*(n-3)+64),(n,r,'square'))
    print('exact symbolic-identity instances checked through n=160')


if __name__=='__main__':
    direct_tests()
    exact_formula_tests()
    print(f'PASS: {checks:,} exact assertions')
