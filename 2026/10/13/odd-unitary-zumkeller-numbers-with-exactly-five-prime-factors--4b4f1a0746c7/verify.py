#!/usr/bin/env python3
import json, math, sys
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
W=json.loads((HERE/'witnesses.json').read_text(encoding='utf-8'))

def is_prime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def unitary_divisors(factors):
    ds=[1]
    for p,a in factors:
        b=p**a
        ds=ds+[d*b for d in ds]
    return sorted(ds)

def sigma_star(factors):
    z=1
    for p,a in factors:z*=1+p**a
    return z

# Exact inequalities used in the infinite reduction.
def prod_ratio(primes, squared_index=None):
    f=Fraction(1,1)
    for i,p in enumerate(primes):
        if i==squared_index:f*=Fraction(p*p+1,p*p)
        else:f*=Fraction(p+1,p)
    return f
assert prod_ratio([5,7,11,13,17]) < 2
assert prod_ratio([3,7,11,13,17]) < 2
assert prod_ratio([3,5,11,13,17]) < 2
for i in range(4):
    assert prod_ratio([3,5,7,11,13],i) < 2
assert Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(14,13)*Fraction(290,289) < 2
assert Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(12,11) == Fraction(768,385)

# Recreate exactly the candidate list forced by the symbolic proof.
expected=[]
for r in [11,13,17,19]:
    B=Fraction(32*(r+1),3*r-32)
    for s in range(r+1,385):
        if is_prime(s) and s<=B:
            expected.append(((3,1),(5,1),(7,1),(r,1),(s,1)))
for s in [13,17,19]:
    expected.append(((3,1),(5,1),(7,1),(11,1),(s,2)))
assert len(expected)==90

seen=[]
for row in W['rows']:
    fac=tuple((z['p'],z['a']) for z in row['factorization'])
    seen.append(fac)
    assert fac in expected
    n=math.prod(p**a for p,a in fac)
    assert n==row['n']
    sig=sigma_star(fac)
    assert sig==row['sigma_star'] and sig%2==0
    delta=sig//2-n
    assert delta==row['delta'] and delta>=0
    allu=set(unitary_divisors(fac))
    ww=row['witness_proper_unitary_divisors']
    assert len(ww)==len(set(ww))
    assert all(d in allu and d<n for d in ww)
    assert sum(ww)==delta
assert set(seen)==set(expected) and len(seen)==90

least=W['rows'][0]
assert least['n']==15015
# Four distinct odd primes can never reach unitary abundancy two.
assert Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(12,11) < 2
print('VERIFY_OK candidates=90 witnesses=90 least=15015')
