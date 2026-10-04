#!/usr/bin/env python3
from functools import lru_cache

WITNESS="0102101201020120212010210120102012102010210120102012021201021012010212021020102101201020120212010210120102012102010210120102012021201021012010"

def append_ok(s,c):
    t=s+c
    n=len(t)
    for h in range(1,n//2+1):
        if t[n-2*h:n-h] == t[n-h:n]:
            return False
    return True

def border_lengths(s):
    return [b for b in range(1,len(s)) if s[:b] == s[-b:]]

@lru_cache(None)
def squarefree_starting_zero(n):
    if n == 1:
        return ("0",)
    out=[]
    def dfs(s):
        if len(s)==n:
            out.append(s); return
        for c in "012":
            if append_ok(s,c):
                dfs(s+c)
    dfs("0")
    return tuple(out)

def connectors(u,m):
    out=[]
    def dfs(s,d):
        if d==m:
            t=s
            for c in u:
                if not append_ok(t,c):
                    return
                t += c
            out.append(s[len(u):])
            return
        for c in "012":
            if append_ok(s,c):
                dfs(s+c,d+1)
    dfs(u,0)
    return out

@lru_cache(None)
def words_with_at_least(n,r):
    # Alphabet-renaming symmetry lets us normalize the first symbol to 0.
    if r==0:
        return squarefree_starting_zero(n)
    out=set()
    # In a squarefree word every proper border has length < n/2.
    # If u is the longest border, every smaller border is a border of u.
    for b in range(1,(n-1)//2+1):
        for u in words_with_at_least(b,r-1):
            for mid in connectors(u,n-2*b):
                w=u+mid+u
                if len(border_lengths(w)) >= r:
                    out.add(w)
    return tuple(sorted(out))

mins=[]
for r in range(6):
    n=1
    while not words_with_at_least(n,r):
        n += 1
    mins.append(n)

assert mins == [1,3,7,23,59,142]
norm_minimizers=words_with_at_least(142,5)
assert len(norm_minimizers)==4
assert WITNESS in norm_minimizers
assert len(WITNESS)==142
assert border_lengths(WITNESS)==[1,3,11,30,67]
periods=sorted([len(WITNESS)-b for b in border_lengths(WITNESS)])
assert periods==[75,112,131,139,141]

print("VERIFY_OK minima=1,3,7,23,59,142 normalized_minimizers_142=4 witness_borders=1,3,11,30,67 periods=75,112,131,139,141")
