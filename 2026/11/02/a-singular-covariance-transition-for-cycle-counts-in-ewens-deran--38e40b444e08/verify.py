#!/usr/bin/env python3
"""Exact checks for finite Ewens derangement cycle-count dependence.
Run: python3 verify.py. No external packages or input files are needed.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def normalizers(theta, N):
    z = [Fraction(1), Fraction(0)]
    for n in range(1, N):
        z.append((n*z[n] + theta*z[n-1]) / (n+1))
    return z

def cycle_counts(perm):
    n=len(perm); seen=set(); count={}
    for i in range(n):
        if i not in seen:
            j=i; length=0
            while j not in seen:
                seen.add(j); length+=1; j=perm[j]
            count[length]=count.get(length,0)+1
    return count

def expected_moments_enumerated(n, theta, r, s):
    total=Fraction(); ar=Fraction(); bs=Fraction(); ab=Fraction()
    for perm in permutations(range(n)):
        if any(perm[i] == i for i in range(n)):
            continue
        cc=cycle_counts(perm)
        weight=theta**sum(cc.values())
        total+=weight
        cr=cc.get(r,0); cs=cc.get(s,0)
        ar+=weight*cr; bs+=weight*cs; ab+=weight*cr*cs
    return ar/total,bs/total,ab/total,(ab*total-ar*bs)/(total*total)

def covariance(z, n, theta, r, s):
    return theta*theta*Fraction(1,r*s)*(z[n]*z[n-r-s]-z[n-r]*z[n-s])/(z[n]*z[n])

# Independent finite-cycle factorial-moment recurrence and direct counting.
for theta in (Fraction(1,2),Fraction(1),Fraction(2)):
    z=normalizers(theta,320)
    for n in range(2,31):
        check(n*z[n] == theta*sum(z[n-j] for j in range(2,n+1)),
              f'coefficient recurrence theta={theta} n={n}')
    for n in range(5,9):
        for r,s in ((2,3),(2,4)):
            if n<r+s: continue
            x,y,xy,cov=expected_moments_enumerated(n,theta,r,s)
            check(x == (theta/r)*z[n-r]/z[n],f'first mean theta={theta} n={n} r={r}')
            check(y == (theta/s)*z[n-s]/z[n],f'second mean theta={theta} n={n} s={s}')
            check(xy == (theta*theta/Fraction(r*s))*z[n-r-s]/z[n],f'joint moment theta={theta} n={n}')
            check(cov == covariance(z,n,theta,r,s),f'covariance theta={theta} n={n}')

# Every permitted size in this (finite) exact range, including the u=0,1 borders.
z=normalizers(Fraction(1),101)
for r in range(2,9):
    for s in range(r+1,10):
        for u in range(0,65):
            n=r+s+u
            sign=z[n]*z[u]-z[n-r]*z[n-s]
            check((sign>0) if u%2==0 else (sign<0),
                  f'parity theta=1 r={r} s={s} n={n}')

# Asymptotics: exact rational arithmetic, compared with analytic leading term.
for theta in (Fraction(1,2),Fraction(2),Fraction(3,2),Fraction(3,4)):
    z=normalizers(theta,321)
    for r,s in ((2,3),(2,5),(3,6)):
        n=300
        observed=float(covariance(z,n,theta,r,s)*n*n)
        limit=float(theta*theta*(1-theta))
        check(abs(observed-limit) < 0.07*abs(limit),
              f'asymptotic theta={theta} lengths={r,s} observed={observed} target={limit}')

print(f'PASS: {checks} exact integer/rational assertions and asymptotic numerical comparisons')
print('Finite enumeration is not used to prove statements for all n; see the written proof.')
