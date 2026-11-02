#!/usr/bin/env python3
"""Exact independent-arithmetic checks for a quaternary deletion cover."""
from fractions import Fraction
from itertools import product
from collections import Counter
from pathlib import Path

ALPHABET = tuple('0123')
WORDS4 = list(product(ALPHABET, repeat=4))
WORDS3 = list(product(ALPHABET, repeat=3))


def descendants(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}


def signature(w):
    first = {}
    for a in w:
        if a not in first:
            first[a] = len(first)
    return ''.join(str(first[a]) for a in w)


def pattern3(t):
    a,b,c=t
    if a==b==c:
        return 'AAA'
    if a==c:
        return 'ABA'
    if a==b or b==c:
        return 'AAB_or_BAA'
    return 'ABC'

DUAL = {'AAA':Fraction(1,2), 'ABA':Fraction(1,8),
        'AAB_or_BAA':Fraction(3,8),'ABC':Fraction(1,4)}
PRIMAL = {'0012':Fraction(1,6), '0100':Fraction(1,3),
          '0101':Fraction(1,3), '0122':Fraction(1,12),
          '0123':Fraction(3,16)}

# Independently determine set-cover incidence via the four position deletions.
assert len(WORDS3)==64 and len(WORDS4)==256
parent=Path(__file__).resolve().parent
chosen=[tuple(line.strip()) for line in (parent/'codebook.txt').read_text().splitlines() if line.strip()]
assert len(chosen)==19 and len(set(chosen))==19
assert all(len(w)==4 and set(w)<=set(ALPHABET) for w in chosen)
covered=set().union(*(descendants(w) for w in chosen))
assert covered==set(WORDS3), ('missing', set(WORDS3)-covered)

# Every length-four word satisfies the dual cover inequality, exactly.
for w in WORDS4:
    assert sum((DUAL[pattern3(t)] for t in descendants(w)), Fraction(0))<=1, w
assert sum((DUAL[pattern3(t)] for t in WORDS3), Fraction(0))==Fraction(37,2)

# Fractional primal feasibility and matched optimum, over all 64 constraints.
for t in WORDS3:
    value=sum((PRIMAL.get(signature(w),Fraction(0)) for w in WORDS4
               if t in descendants(w)),Fraction(0))
    assert value==1,(t,value)
assert sum((PRIMAL.get(signature(w),Fraction(0)) for w in WORDS4),Fraction(0))==Fraction(37,2)

# Equality-pattern orbit table is a complete reduction under alphabet relabeling.
patterns={}
for w in WORDS4:
    pat=signature(w)
    value=sum((DUAL[pattern3(t)] for t in descendants(w)),Fraction(0))
    assert pat not in patterns or patterns[pat]==value
    patterns[pat]=value
assert len(patterns)==15
print('CHECK_PATTERNS')
for k,v in sorted(patterns.items()):
    print(k, str(v))
print('DUAL_TYPE_COUNTS',str(dict(Counter(map(pattern3, WORDS3)))))
print('FRACTIONAL_PRIMAL_DUAL', '37/2')
print('INTEGRAL_COVER_SIZE',len(chosen))
print('COVERED_OUTPUTS',len(covered))
print('VERIFY_OK')
