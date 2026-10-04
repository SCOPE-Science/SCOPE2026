#!/usr/bin/env python3
"""Finite sanity checks for the four-profile theorem for variable-free KB.

The theorem itself is proved by structural induction in RESULT.md.  This script
only checks the profile recursion against direct Kripke semantics on every
symmetric frame with at most four worlds and on all generated formulas of
syntax size at most seven.
"""
from functools import lru_cache
from itertools import product

BOT=('bot',)
def box(a): return ('box',a)
def imp(a,b): return ('imp',a,b)

@lru_cache(None)
def formulas(size):
    out=set()
    if size==1:
        out.add(BOT)
    if size>=2:
        for a in formulas(size-1): out.add(box(a))
    if size>=3:
        for left_size in range(1,size-1):
            right_size=size-1-left_size
            if right_size<1: continue
            for a in formulas(left_size):
                for b in formulas(right_size): out.add(imp(a,b))
    return frozenset(out)

def profile(f):
    tag=f[0]
    if tag=='bot': return (False,False)
    if tag=='box':
        _,a=f
        ai,an=profile(a)
        return (True,an)
    if tag=='imp':
        _,a,b=f
        ai,an=profile(a); bi,bn=profile(b)
        return ((not ai) or bi,(not an) or bn)
    raise ValueError(tag)

def symmetric_frames(n):
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    for bits in product((False,True), repeat=len(pairs)):
        R=[[False]*n for _ in range(n)]
        for bit,(i,j) in zip(bits,pairs):
            if bit:
                R[i][j]=R[j][i]=True
        yield R

def truth(f,R,w):
    tag=f[0]
    if tag=='bot': return False
    if tag=='imp': return (not truth(f[1],R,w)) or truth(f[2],R,w)
    if tag=='box':
        return all((not R[w][v]) or truth(f[1],R,v) for v in range(len(R)))
    raise ValueError(tag)

fs=set()
for s in range(1,8): fs.update(formulas(s))
profiles={profile(f) for f in fs}
assert profiles=={(False,False),(False,True),(True,False),(True,True)}
checked=0
for n in range(1,5):
    for R in symmetric_frames(n):
        isolated=[not any(R[w]) for w in range(n)]
        for f in fs:
            pi=profile(f)
            for w in range(n):
                want=pi[0] if isolated[w] else pi[1]
                got=truth(f,R,w)
                assert got==want, (n,R,f,w,pi,got,want)
                checked += 1
print('VERIFY_OK')
print('generated_formulas',len(fs))
print('profiles',sorted(profiles))
print('world_formula_checks',checked)
