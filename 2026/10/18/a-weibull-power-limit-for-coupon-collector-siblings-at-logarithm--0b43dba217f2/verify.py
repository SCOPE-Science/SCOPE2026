#!/usr/bin/env python3
"""Exact finite checks related to growing-index sibling coupon-collector laws.

These are diagnostics of algebraic identities, not a certificate for the limit theorem.
No external dependencies and no network access are required.
"""
from fractions import Fraction
from math import comb, factorial, gamma, exp


def alternating_deficit(n, m):
    return sum(((-1) ** (a+1)) * Fraction(comb(n,a),a**m)
               for a in range(1,n+1))


def max_exp_mgf_coeff(n, m):
    # Product_{a=1}^n (1-t/a)^(-1) via the logarithmic derivative.
    powers=[None]+[sum((Fraction(1,a**r) for a in range(1,n+1)),Fraction(0))
                    for r in range(1,m+1)]
    c=[Fraction(1)]
    for j in range(1,m+1):
        c.append(sum((powers[r]*c[j-r] for r in range(1,j+1)),Fraction(0))/j)
    return c[m]


def direct_mgf_coeff(n, m):
    coeffs=[Fraction(1)]+[Fraction(0)]*m
    for r in range(1,n+1):
        nxt=[Fraction(0)]*(m+1)
        for k in range(m+1):
            for j in range(m-k+1):
                nxt[k+j]+=coeffs[k]*Fraction(1,r**j)
        coeffs=nxt
    return coeffs[m]


def poisson_tail_ratio(k,s):
    # e^s k! s^{-k} P(Pois(s)<=k): stable final-term division.
    product=1.
    total=1.
    for t in range(1,k+1):
        product*=(k-t+1)/s
        total+=product
    return total


def main():
    assertions=0
    for n in range(1,13):
        for m in range(1,9):
            a=alternating_deficit(n,m)
            b=max_exp_mgf_coeff(n,m)
            c=direct_mgf_coeff(n,m)
            assert a==b==c, (n,m,a,b,c)
            assert Fraction(1)<=a<=n
            assertions+=2
    # Two-type case: the last discovered type always misses later albums.
    for m in range(1,12):
        assert alternating_deficit(2,m)==2-Fraction(1,2**m)
        assertions+=1
    # Uniform Poisson lower tail: k/s strictly below one.
    for ratio in (0.15,0.3,0.6):
        for k in (100,500,2000):
            s=k/ratio
            correction=poisson_tail_ratio(k,s)
            assert correction>1
            assert correction <=1/(1-ratio)+1e-12
            if k==2000:
                assert abs(correction-1/(1-ratio))<0.004
            assertions+=2
    # For W~Exp(1): E[\\(W^{1-\\alpha}/(1-\\alpha)\\)]=\\(\\Gamma(1-\\alpha)\\).
    for alpha in (0.1,0.25,0.5,0.75,0.9):
        assert abs(gamma(2-alpha)/(1-alpha)-gamma(1-alpha))<1e-10
        assertions+=1
    print(f"PASS: {assertions} exact/arithmetic diagnostic assertions")


if __name__=='__main__':
    main()
