#!/usr/bin/env python3
"""Finite, exact, self-contained certificates for the Rudin--Shapiro tortoise theorem.
No external data or packages are required. Run: python3 verify_rudin_tortoise.py
"""
from collections import defaultdict
from math import ceil, log2

MORPH = {'a':'ab','b':'ac','c':'db','d':'dc'}
PROJ = {'a':'0','b':'0','c':'1','d':'1'}

def morph(word):
    return ''.join(MORPH[a] for a in word)

def iterate(word, k):
    for _ in range(k):
        word = morph(word)
    return word

def pairs():
    # Start with the seed factor of the fixed point, then close under substitution.
    s = {'ab'}
    while True:
        t = s | {morph(ab)[i:i+2] for ab in s for i in range(3)}
        if t == s:
            return s
        s = t

def factors(n, projected=False):
    assert n >= 1
    k = 0
    while 2**k < n:
        k += 1
    ss = set()
    for ab in pairs():
        word = iterate(ab,k)
        if projected:
            word = ''.join(PROJ[c] for c in word)
        ss.update(word[i:i+n] for i in range(len(word)-n+1))
    return ss

def T(w):
    idx = w.find('1')
    return w if idx == -1 else w[:idx] + w[idx+1:] + '1'

P = pairs()
print('adjacent_four_letter_pairs', sorted(P))
assert len(P) == 8
assert '00000' not in factors(5,True)  # every 12-factor contains a 1

# All four-letter five-factors with more than one left extension:
sept = factors(7)
ctx = defaultdict(set)
for a in sept:
    ctx[a[2:]].add(a[:2])
special5 = {w: v for w,v in ctx.items() if len({x[1] for x in v}) > 1}
print('four_letter_left_special_length5',len(special5))
for w in sorted(special5):
    print(w,','.join(sorted(special5[w])))
assert len(special5)==8
assert all(cs == {'ac','db'} for cs in special5.values())

# Projection of all 4-letter factors of length 8 is injective.
U8 = factors(8)
dict8 = defaultdict(set)
for w in U8:
    dict8[''.join(PROJ[x] for x in w)].add(w)
assert len(U8)==56 and len(dict8)==56
assert all(len(v)==1 for v in dict8.values())
print('length8_four_letter_to_binary_decoding',len(U8),'unique')

# Exhaustive initial tortoise-complexity and the n=12 collision fibers.
p0=[]; t0=[]
for n in range(1,13):
    fb=factors(n,True)
    p0.append(len(fb)); t0.append(len({T(x) for x in fb}))
print('factor_complexity_n1_to12',p0)
print('tortoise_complexity_n1_to12',t0)
assert p0==[2,4,8,16,24,36,46,56,64,72,80,88]
assert t0==[2,3,5,9,14,24,31,43,52,61,71,80]

fb=factors(12,True)
fibers=defaultdict(set)
for w in fb:
    fibers[T(w)].add(w)
coll=[tuple(sorted(ws)) for ws in fibers.values() if len(ws)>1]
assert len(coll)==8 and all(len(c)==2 for c in coll)
assert all(a[:2]=='01' and b[:2]=='10' and a[2:]==b[2:] for a,b in coll)
print('length12_collision_pairs',len(coll))
for a,b in sorted(coll): print(a,b)

# Confirm the structural claim at additional finite lengths.
for n in (13,16,19,32,40,64,128):
    f=factors(n,True)
    assert len(f)==8*n-8
    assert len({T(x) for x in f})==8*n-16
    m=n-2
    left={w for w in factors(m,True) if '0'+w in factors(m+1,True) and '1'+w in factors(m+1,True)}
    context={w for w in factors(m,True) if '01'+w in f and '10'+w in f}
    assert len(left)==8 and left==context
    print('extended_length',n,'p',len(f),'rho',len({T(x) for x in f}),'left_special',len(left))
print('ALL_FINITE_CERTIFICATES_PASSED')
