#!/usr/bin/env python3
"""Finite exact certificates for tortoise images of period-doubling factors.
No external dependencies. Requires Python 3.8+.
"""
from collections import defaultdict
from hashlib import sha256

def morph(word):
    return ''.join('01' if c == '0' else '00' for c in word)

def tau(word):
    j = word.find('1')
    return word if j < 0 else word[:j] + word[j+1:] + '1'

def iterate_tau(word, k):
    for _ in range(k):
        word = tau(word)
    return word

def windows(word, size):
    return {word[i:i+size] for i in range(len(word)-size+1)}

def pd_digit(n):
    # Independent digit recurrence, not substitution expansion.
    return '0' if n % 2 == 0 else ('1' if pd_digit(n//2) == '0' else '0')

w = '0'
for _ in range(7):
    w = morph(w)
assert len(w) == 128
F18 = windows(w, 18)
assert len(F18) == 28
assert all(len(v)==18 and set(v)<=set('01') for v in F18)
# Substitution-closure proves these, and ONLY these, are all length-18 factors.
T18 = set()
for v in F18:
    T18.update(windows(morph(v), 18))
assert T18 == F18, (len(T18-F18), len(F18-T18))
print('MORPHISM FACTOR CLOSURE: mu^7(0) length=128 F18=28, closure=28, PASS')

W8192 = ''.join(pd_digit(j) for j in range(8192))
wcheck = '0'
for _ in range(13):
    wcheck = morph(wcheck)
assert W8192 == wcheck
for n in range(1,19):
    F = {v[:n] for v in F18}
    assert F == windows(W8192, n)
print('INDEPENDENT DIGIT-RECURRENCE CROSS-CHECK: n=1..18, PASS')

F10 = {v[:10] for v in F18}
assert len(F10) == 16
assert all(s.count('1')>=1 for s in F10)
assert all(s.count('1')>=2 for s in F18)
for k, m, F in [(1,10,F10),(2,18,F18)]:
    images={iterate_tau(v,k) for v in F}
    assert len(images)==len(F)
    print(f'K={k} INJECTIVE AT LENGTH {m}: factors={len(F)} distinct_images={len(images)}, PASS')

print('n   p(n)   rho_t(n)  rho_t2(n)')
for n in range(1,19):
    F={v[:n] for v in F18}
    a=len({iterate_tau(v,1) for v in F})
    b=len({iterate_tau(v,2) for v in F})
    print(f'{n:2d}   {len(F):4d}   {a:8d}   {b:9d}')
for k, n in [(1,9),(2,17)]:
    F={v[:n] for v in F18}
    by_image=defaultdict(list)
    for v in sorted(F):
        by_image[iterate_tau(v,k)].append(v)
    collisions=[(image,values) for image,values in sorted(by_image.items()) if len(values)>1]
    assert collisions
    image,vals=collisions[0]
    print(f'K={k}, LENGTH {n}, COLLISION: {vals[0]} != {vals[1]} ; common image={image}')
print('ALL CHECKS PASS')
