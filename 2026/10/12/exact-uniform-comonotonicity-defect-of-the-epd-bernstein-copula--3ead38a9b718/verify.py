#!/usr/bin/env python3
from fractions import Fraction
from math import comb, lgamma, exp, pi, sqrt

def tail_num(n, r):
    # Numerator of P(Bin(n,1/2) >= r), denominator 2^n.
    return sum(comb(n,j) for j in range(r,n+1))

for n in range(1,121):
    den = 2**n
    center_c = sum(Fraction(tail_num(n,r)**2, den*den) for r in range(1,n+1)) / n
    center_defect = Fraction(1,2) - center_c
    formula = Fraction(comb(2*n,n), 2*(4**n))
    assert center_defect == formula, (n, center_defect, formula)

    lhs = sum((n-k)*comb(2*n,k) for k in range(n))
    rhs = n*comb(2*n,n)//2
    assert lhs == rhs, (n,lhs,rhs)

def tails(n, p):
    pmf = [(p**j)*((1-p)**(n-j))*comb(n,j) for j in range(n+1)]
    out = []
    running = 0.0
    for j in range(n,-1,-1):
        running += pmf[j]
        if j >= 1:
            out.append(running)
    return list(reversed(out))

for n in range(2,9):
    exact = comb(2*n,n)/(2.0*(4.0**n))
    grid = [i/40.0 for i in range(41)]
    T = {p:tails(n,p) for p in grid}
    best = -1.0
    best_uv = None
    for u in grid:
        for v in grid:
            c = sum(a*b for a,b in zip(T[u],T[v]))/n
            d = min(u,v)-c
            if d > best:
                best = d
                best_uv = (u,v)
            assert d <= exact + 2e-13, (n,u,v,d,exact)
    assert abs(best-exact) < 2e-13 and best_uv == (0.5,0.5), (n,best,best_uv,exact)

n = 10000
log_ratio = (lgamma(2*n+1)-2*lgamma(n+1)-n*__import__("math").log(4.0)) + 0.5*__import__("math").log(pi*n)
ratio = exp(log_ratio)
assert abs(ratio - 1.0) < 2e-5
print(f"VERIFY_OK exact_n=120 grid_n=8 asymptotic_ratio={ratio:.12f}")
