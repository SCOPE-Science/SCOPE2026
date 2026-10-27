#!/usr/bin/env python3
"""Exact standard-library checker for length-four deletion covering."""
from fractions import Fraction
from itertools import product
from collections import Counter

WORDS = '''0010 0032 0213 1010 1012 1033 1131 1230 2020 2031
2121 2122 2323 3011 3022 3030 3132 3210 3313'''.split()

def shadow(word):
    return {word[:i]+word[i+1:] for i in range(len(word))}

def weight(y):
    a,b,c=y
    if a==b==c:
        return Fraction(1,2)
    if a==b or b==c:
        return Fraction(3,8)
    if a==c:
        return Fraction(1,8)
    return Fraction(1,4)

def rgs_words(n):
    for z in product(range(n),repeat=n):
        nxt=0
        for t in z:
            if t>nxt:break
            nxt=max(nxt,t+1)
        else:yield ''.join(map(str,z))

patterns=list(rgs_words(4))
assert len(patterns)==15
sums=[(''.join(x),sum((weight(y) for y in shadow(x)), Fraction(0))) for x in patterns]
assert all(s<=1 for _,s in sums)
print('PATTERN_CERTIFICATE', ' '.join('%s:%s'%(s,v) for s,v in sums))
for q in range(2,9):
    seq=[''.join(x) for x in product(map(str,range(q)),repeat=3)]
    total=sum((weight(y) for y in seq),Fraction(0))
    formula=Fraction(q*(2*q*q+q+1),8)
    assert total==formula
    max_shadow=max(sum((weight(y) for y in shadow(''.join(x))),Fraction(0))
                   for x in product(map(str,range(q)),repeat=4))
    assert max_shadow<=1
    print('DUAL_CHECK',q,'total',total,'max_shadow',max_shadow)
assert len(WORDS)==19 and len(set(WORDS))==19
assert all(len(x)==4 and set(x)<={'0','1','2','3'} for x in WORDS)
coverage=Counter()
for x in WORDS:
    for y in shadow(x):coverage[y]+=1
all_outputs={''.join(x) for x in product('0123',repeat=3)}
assert set(coverage)==all_outputs
multiplicities=dict(sorted(Counter(coverage.values()).items()))
print('WITNESS',len(WORDS),'WORDS_COVER',len(coverage),'MULTIPLICITIES',multiplicities)
assert Fraction(4*(2*4*4+4+1),8)==Fraction(37,2)
assert len(WORDS)==19
print('VERIFY_OK')
