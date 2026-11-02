#!/usr/bin/env python3
"""Exact reproducibility checks for youngest nonleaf in uniform recursive trees.

No external packages, downloads, or random seeds are needed.
"""
from fractions import Fraction
from itertools import product
from math import factorial, sqrt, pi, lgamma, log, exp, expm1, log1p


def tail_prob(n, m):
    assert 1 <= m <= n-1
    a = n - m
    return Fraction(a ** m * factorial(a-1), factorial(n-1))


def conditional_mean_leaves(n, m):
    a = n - m
    return Fraction(m) + Fraction(a, 2) * Fraction(a-1, a)**m


def exact_covariance(n):
    return sum((tail_prob(n,m) *
                (conditional_mean_leaves(n,m)-Fraction(n,2))
                for m in range(1,n)), Fraction(0))


def exhaustive(n):
    totals = [0] * n
    sum_leaves_in_tail = [0] * n
    sum_h = sum_l = sum_hl = sum_ll = 0
    count = 0
    parent_ranges = [range(1, k) for k in range(2, n+1)]
    for parents in product(*parent_ranges):
        count += 1
        children = [0] * (n+1)
        for p in parents:
            children[p] += 1
        max_internal = max(v for v in range(1,n+1) if children[v])
        h = n - max_internal
        l = sum(children[v] == 0 for v in range(1,n+1))
        sum_h += h
        sum_l += l
        sum_hl += h*l
        sum_ll += l*l
        for m in range(1, h+1):
            totals[m] += 1
            sum_leaves_in_tail[m] += l
    return count, totals, sum_leaves_in_tail, sum_h, sum_l, sum_hl, sum_ll


def numerical_covariance(n):
    s=0.
    for m in range(2,n):
        a=n-m
        lp=m*log(a)+lgamma(a)-lgamma(n)
        if lp < -50.:
            continue
        p=exp(lp)
        loss= -expm1(m*log1p(-1/a)) if a>1 else 1.
        delta= (m-a*loss)/2.
        s+=p*delta
    return s


def main():
    assertions = 0
    for n in range(3,10):
        count, totals, suml, sumh, sl, shl, sll = exhaustive(n)
        assert count == factorial(n-1); assertions += 1
        assert Fraction(sl,count) == Fraction(n,2); assertions += 1
        assert Fraction(sll,count)-Fraction(sl,count)**2 == Fraction(n,12); assertions += 1
        observed_cov = Fraction(shl,count)-Fraction(sumh*sl,count**2)
        assert observed_cov == exact_covariance(n); assertions += 1
        assert observed_cov > 0; assertions += 1
        assert Fraction(sumh,count)==sum((tail_prob(n,m) for m in range(1,n)),Fraction(0)); assertions+=1
        for m in range(1,n):
            a=n-m
            assert Fraction(totals[m],count) == tail_prob(n,m); assertions += 1
            assert Fraction(suml[m],totals[m]) == conditional_mean_leaves(n,m); assertions += 1
            assert conditional_mean_leaves(n,m)>=Fraction(n,2); assertions += 1
            if m>=2:
                assert conditional_mean_leaves(n,m)>Fraction(n,2); assertions += 1
        print(f"n={n}, trees={count}, covariance={float(observed_cov):.10f}")
    k=sqrt(pi/2)/4
    for n in (1000,10000,100000):
        r=numerical_covariance(n)/sqrt(n)
        assert abs(r-k) < 0.012 if n==1000 else abs(r-k)<0.004
        assertions+=1
        print(f"n={n}, cov/sqrt(n)={r:.10f}, target={k:.10f}")
    print(f"PASS {assertions} exact/numerical assertions")

if __name__=='__main__': main()
