#!/usr/bin/env python3
"""Exact finite-size and numerical checks for the two-preseeded-dimer spacing law.
Only the written proof establishes the infinite-size claims.
"""
from fractions import Fraction
from itertools import permutations
from functools import lru_cache
from math import factorial, exp

checks=0

def check(statement, description):
    global checks
    checks+=1
    if not statement:
        raise AssertionError(description)

def F_recurrence(N):
    f=[Fraction(0)]*(N+1)
    for m in range(2,N+1):
        f[m]=Fraction(1)+sum((f[j-1]+f[m-j-1] for j in range(1,m)),Fraction(0))/Fraction(m-1)
    return f

def F_coefficient(m):
    # [z^m] z(1-e^{-2z}) / (2(1-z)^2), extracted independently.
    if m==0:return Fraction(0)
    return (Fraction(m)-sum((Fraction(m-j)*Fraction((-2)**j,factorial(j)) for j in range(m)),Fraction(0)))/2

def greedy(n, order):
    occupied=0
    used=0
    for e in order:
        a,b=e,(e+1)%n
        if occupied & ((1<<a)|(1<<b)):
            continue
        occupied|=(1<<a)|(1<<b)
        used+=1
    return used

def brute(n,pins=()):
    rem=tuple(e for e in range(n) if e not in pins)
    total=0
    count=0
    for perm in permutations(rem):
        total+=greedy(n,tuple(pins)+perm)
        count+=1
    return Fraction(total,count)

f=F_recurrence(40)
for m in range(41):
    check(f[m]==F_coefficient(m),f'F coefficient {m}')
for n in range(3,9):
    check(brute(n)==1+f[n-2],f'cycle baseline {n}')
    for d in range(2,n-1):
        check(brute(n,(0,d))==2+f[d-2]+f[n-d-2],f'pinned finite formula n={n} d={d}')
        check(brute(n,(d,0))==brute(n,(0,d)),f'pinned ordering n={n} d={d}')

rho=(1-exp(-2))/2
for d in range(2,14):
    k=d-2
    target=1+float(f[k])-rho*d
    # Independently evaluate the integral using composite Simpson quadrature.
    def integrand(t):
        w=2*t*(1-t)*exp(-2*(1-t))
        p=(2*t)**k/factorial(k)
        if k>=1:p+=(2*t)**(k-1)/factorial(k-1)
        return w*p
    N=4096;h=1/N
    sm=integrand(0)+integrand(1)
    for j in range(1,N):sm+=(4 if j%2 else 2)*integrand(j*h)
    val=(((-1)**k)*sm*h/3)
    check(abs(target-val)<2e-10,f'integral d={d}')
    check(((-1)**d)*target>0,f'sign d={d}')

A={d:abs(1+float(f[d-2])-rho*d) for d in range(2,22)}
check(A[4]>A[2], 'max at four versus two')
check(A[3]>A[5], 'min at three versus five')
for d in range(4,21):
    check(A[d]>A[d+1],f'abs monotonicity {d}')
print(f'PASS: {checks} exact finite checks and independent numerical diagnostics')
