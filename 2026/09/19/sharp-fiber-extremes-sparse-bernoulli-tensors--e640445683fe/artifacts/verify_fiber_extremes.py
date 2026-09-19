#!/usr/bin/env python3
"""Deterministic checks for the sparse-Bernoulli fiber-extreme formulas.

Uses only the Python standard library.  It evaluates exact binomial upper
tails by starting from one binomial mass and summing the decreasing
recurrence, then compares one-mode maximum probabilities with the
second-order lattice profile.
"""
import math

def h(x):
    return x*math.log(x)-x+1.0

def hinv(y):
    lo, hi = 1.0, 2.0
    while h(hi) < y:
        hi *= 2.0
    for _ in range(100):
        mid=(lo+hi)/2.0
        if h(mid) < y:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def binom_tail(n,p,m):
    # P(Bin(n,p) >= m), for m above the mean.
    if m <= 0:
        return 1.0
    if m > n:
        return 0.0
    logcomb = sum(math.log(n-j)-math.log(j+1) for j in range(m))
    logpmf = logcomb + m*math.log(p) + (n-m)*math.log1p(-p)
    first = math.exp(logpmf)
    total = first
    term = first
    j = m
    while j < n:
        ratio = ((n-j)/(j+1))*(p/(1-p))
        term *= ratio
        total += term
        j += 1
        if term <= total*1e-17:
            break
    return total

def one_mode_cdf_less(n,k,c,m):
    d=c*math.log(n)
    p=d/n
    q=binom_tail(n,p,m)
    N=n**(k-1)
    return math.exp(N*math.log1p(-q))

k,c=3,2.0
xstar=hinv((k-1)/c)
A=math.sqrt(xstar)/((xstar-1)*math.sqrt(2*math.pi*c))
print("k=3, c=2")
print("x_star =",format(xstar,'.15f'))
print("sqrt(x_star) =",format(math.sqrt(xstar),'.15f'))
print("A =",format(A,'.15f'))
print("h(x_star) =",format(h(xstar),'.15f'))
print()

for n in (10_000,100_000,1_000_000):
    d=c*math.log(n)
    center=xstar*d-math.log(math.log(n))/(2*math.log(xstar))
    m=round(center-0.8)
    z=m-center
    exact=one_mode_cdf_less(n,k,c,m)
    asym=math.exp(-A*(xstar**(-z)))
    print("n =",n)
    print("  center =",format(center,'.12f'))
    print("  m =",m," z =",format(z,'.12f'))
    print("  exact P(M_mode < m) =",format(exact,'.12f'))
    print("  asymptotic profile  =",format(asym,'.12f'))
    print("  abs error =",format(abs(exact-asym),'.12f'))

r=2.0
xr=hinv((k-1+r)/c)
print()
print("r=2 polynomial-tail barrier")
print("x_r =",format(xr,'.15f'))
print("sqrt(x_r) =",format(math.sqrt(xr),'.15f'))
print("c*h(x_r) =",format(c*h(xr),'.15f'))
