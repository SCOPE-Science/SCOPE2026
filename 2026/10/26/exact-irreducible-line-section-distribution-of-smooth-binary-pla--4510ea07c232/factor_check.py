#!/usr/bin/env python3
"""Independent F2 binary-quartic factorization verification of line-section spectrum.

Checks all orbit representatives, independently computing line restrictions by
binomial expansion over F2. The three irreducible binary quartics are the
monic irreducible polynomials of degree 4 over F2.
"""
import collections
import csv
import itertools
from pathlib import Path

HERE=Path(__file__).resolve().parent
M=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
P=[v for v in itertools.product((0,1),repeat=3) if any(v)]
L=[v for v in P]
IRRED={0b10011,0b11001,0b11111}

def choose(n,k):
    from math import comb
    return comb(n,k)%2

def expand_power(p,q,n):
    # polynomial in s of degree n, t exponent n-i, encoded by bit i
    return sum((choose(n,i) & p**i & q**(n-i))<<i for i in range(n+1))

def multiply(a,b):
    c=0
    i=0
    while a:
        if a&1: c^=b<<i
        a>>=1;i+=1
    return c

LINE_TABLES=[]
for line in L:
    ps=[p for p in P if not sum(a*b for a,b in zip(p,line))%2]
    assert len(ps)==3
    p,q=ps[:2]
    table=[]
    for a,b,c in M:
        x=multiply(multiply(expand_power(p[0],q[0],a),expand_power(p[1],q[1],b)),expand_power(p[2],q[2],c))
        table.append(x)
    LINE_TABLES.append(table)

def profile(F):
    count=0
    for table in LINE_TABLES:
        mask=F;restriction=0
        while mask:
            low=mask&-mask
            restriction^=table[low.bit_length()-1]
            mask^=low
        count+=restriction in IRRED
    return count

hist=collections.Counter()
with (HERE/'orbit_certificate.csv').open(encoding='utf8',newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==279
for row in rows:
    m=int(row['coefficient_bitmask'])
    size=int(row['orbit_size'])
    actual=profile(m)
    stated=int(row['inert_line_count'])
    assert actual==stated,(m,actual,stated)
    if int(row['geometrically_smooth']):hist[actual]+=size
assert dict(sorted(hist.items()))=={0:4666,1:3444,2:1722,3:504,4:420,5:84,6:56,7:24}
assert len(P)==7 and len(LINE_TABLES)==7
assert sum(hist.values())==10920
print('checked_orbit_representatives=279')
print('binary_quartic_irreducibles='+str(sorted(IRRED)))
print('line_restriction_method=independent_binomial_expansion_factorization')
print('smooth_curve_inert_line_histogram='+str(dict(sorted(hist.items()))))
print('independent_restriction_check_passed=true')
