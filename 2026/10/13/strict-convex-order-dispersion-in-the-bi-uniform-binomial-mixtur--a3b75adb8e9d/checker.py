"""Exact arithmetic checks for convex ordering of the two-level uniform law.

This finite test is a reproducibility check, not a proof of the universal theorem.
"""
from fractions import Fraction
from math import comb


def laws(n, p):
    mean = n*p
    k = mean.numerator // mean.denominator
    left = Fraction(n+1 - (2*mean-k), (k+1)*(n+1))
    right = Fraction(2*mean-k, (n-k)*(n+1))
    b = [Fraction(comb(n, x)) * p**x * (1-p)**(n-x) for x in range(n+1)]
    u = [left if x<=k else right for x in range(n+1)]
    return b, u


def check():
    checks = 0
    for n in range(2, 31):
        for numerator in range(1, 20):
            p = Fraction(numerator, 20)
            b, u = laws(n, p)
            assert sum(b) == sum(u) == 1
            checks += 1
            assert sum(x*v for x,v in enumerate(b)) == sum(x*v for x,v in enumerate(u)) == n*p
            checks += 1
            delta = [u[x]-b[x] for x in range(n+1)]
            k = (n*p).numerator // (n*p).denominator
            assert all(delta[x+1]<=delta[x] for x in range(k))
            assert all(delta[x+1]>=delta[x] for x in range(k+1, n))
            checks += 2
            assert all(sum(max(x-j,0)*delta[x] for x in range(n+1))>0 for j in range(1,n))
            checks += max(0,n-1)
            assert sum(x*x*delta[x] for x in range(n+1))>0
            checks += 1
    print(f"PASS: {checks} exact-rational checks across 551 parameter pairs")


if __name__ == "__main__":
    check()
