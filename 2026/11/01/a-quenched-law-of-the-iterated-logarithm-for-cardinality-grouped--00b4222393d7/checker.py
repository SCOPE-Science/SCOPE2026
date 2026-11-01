#!/usr/bin/env python3
"""Exact finite tests for the conditional parity and independence identities.
The infinite-dimensional conclusions use the analytical argument, not these tests.
"""
from itertools import product
from fractions import Fraction
from math import comb

checks = 0

def check(pred, explanation):
    global checks
    if not pred:
        raise AssertionError(explanation)
    checks += 1

def parity_weight(s, row):
    return sum((comb(s,k) & 1)*row[k] for k in range(s+1)) & 1

def zeta(s,row):
    return 1 if parity_weight(s,row)==0 else -1

def law(s,pp):
    total = Fraction(0)
    for row in product((0,1),repeat=s+1):
        prob = Fraction(1)
        for j,b in enumerate(row):
            prob *= pp[j] if b else 1-pp[j]
        total += zeta(s,row)*prob
    return total

for s in range(0,1025):
    odd = sum(comb(s,k)&1 for k in range(s+1))
    check(odd==2**s.bit_count(), f'Lucas parity: s={s}')

# Direct probability enumeration for every value of S_n up to 10.
for s in range(11):
    pp=[Fraction(k+2,k+5) for k in range(s+1)]
    expected = Fraction(1)
    for k in range(s+1):
        if comb(s,k)&1:
            expected *= 1-2*pp[k]
    check(law(s,pp)==expected,f'conditional mean: s={s}')

# Subset-product definition agrees with the cardinality-folded parity formula.
for n in range(1,7):
    for signs in product((-1,1),repeat=n):
        s=signs.count(-1)
        for row in product((0,1),repeat=n+1):
            folded=zeta(s,row)
            direct=1
            for subset in product((0,1),repeat=n):
                k=sum(subset)
                if row[k]:
                    chosen=[signs[j] for j,v in enumerate(subset) if v]
                    direct *= max(chosen) if chosen else -1
            check(direct==folded,f'subset folding n={n}, s={s}')

# For separate rows, exact joint expectations factor conditionally on the walk.
for s,t in product(range(4),repeat=2):
    ps=[Fraction(j+2,j+5) for j in range(s+1)]
    pt=[Fraction(j+3,j+7) for j in range(t+1)]
    l1=law(s,ps)
    l2=law(t,pt)
    double=Fraction(0)
    for a in product((0,1),repeat=s+1):
        pa=Fraction(1)
        for j,b in enumerate(a): pa*= ps[j] if b else 1-ps[j]
        for b in product((0,1),repeat=t+1):
            pb=Fraction(1)
            for j,v in enumerate(b): pb*=pt[j] if v else 1-pt[j]
            double += zeta(s,a)*zeta(t,b)*pa*pb
    check(double==l1*l2,f'independent rows s={s}, t={t}')

for N in (31,63,127,255,511,1023):
    L=N.bit_length()
    for K in range(0,min(L,5)):
        actual=sum(s.bit_count()<=K for s in range(N+1))
        bound=sum(comb(L,j) for j in range(K+1))
        check(actual<=bound,f'sparse binary states N={N}, K={K}')

print(f'PASS: {checks} exact assertions')
