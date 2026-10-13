#!/usr/bin/env python3
from itertools import combinations, permutations, product
from pathlib import Path
import json
ALPH='012'

def low_cut_A(w):
    n=len(w)
    for k in (1,2,3):
        for cuts in combinations(range(1,n),k):
            pts=(0,)+cuts+(n,)
            pieces=[w[pts[i]:pts[i+1]] for i in range(k+1)]
            for p in permutations(range(k+1)):
                left=''
                total=''.join(pieces[t] for t in p)
                for j in range(1,k+1):
                    left += pieces[p[j-1]]
                    if 2*len(left)==len(total) and left==total[len(left):]:
                        return True
    return False

def low_cut_B(w):
    n=len(w)
    if n%2: return False
    half=n//2
    for m in (2,3,4):
        for cuts in combinations(range(1,n),m-1):
            pts=(0,)+cuts+(n,)
            pieces=[w[pts[i]:pts[i+1]] for i in range(m)]
            for p in permutations(range(m)):
                lens=0
                for j in range(m-1):
                    lens += len(pieces[p[j]])
                    if lens>=half: break
                if lens!=half: continue
                s=''.join(pieces[i] for i in p)
                if s[:half]==s[half:]: return True
    return False

# Compute forbidden-factor dictionaries once with each independent predicate.
forbidA={}; forbidB={}
for n in range(1,9):
    A=set(); B=set()
    for tup in product(ALPH,repeat=n):
        w=''.join(tup)
        if low_cut_A(w): A.add(w)
        if low_cut_B(w): B.add(w)
    assert A==B, n
    forbidA[n]=A; forbidB[n]=B

def avoids(w,forbid):
    n=len(w)
    return all(w[i:j] not in forbid[j-i] for i in range(n) for j in range(i+1,n+1))

# Engine 1: full enumeration using forbidden factors from predicate A.
full={}
for n in range(1,9):
    full[n]=sorted(w for w in map(''.join,product(ALPH,repeat=n)) if avoids(w,forbidA))

# Engine 2: incremental suffix checking using predicate-B forbidden sets.
inc={}; cur=['']
for n in range(1,9):
    nxt=[]
    for w in cur:
        for c in ALPH:
            v=w+c
            if all(v[i:] not in forbidB[len(v)-i] for i in range(len(v))): nxt.append(v)
    inc[n]=sorted(nxt); cur=nxt
assert full==inc
expected=[3,6,12,18,30,24,18,0]
assert [len(full[n]) for n in range(1,9)]==expected
expected_max=['0102010','0102101','0121012','0201020','0201202','0212021','1012010','1012101','1020102','1202120','1210121','1210212','2010201','2021020','2021202','2101210','2120121','2120212']
assert full[7]==expected_max

def transforms(w):
    out=set()
    for p in permutations(ALPH):
        mp=dict(zip(ALPH,p)); v=''.join(mp[c] for c in w)
        out.add(v); out.add(v[::-1])
    return out
M=set(expected_max); seen=set(); orbits=[]
for w in expected_max:
    if w in seen: continue
    o=sorted(transforms(w)&M); orbits.append(o); seen.update(o)
assert [len(o) for o in orbits]==[6,6,6]
assert [o[0] for o in orbits]==['0102010','0102101','0121012'] and seen==M
cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text())
assert cert['counts_by_length']=={str(i):expected[i-1] for i in range(1,9)}
assert cert['maximum_words']==expected_max
assert cert['maximum_orbit_representatives']==[o[0] for o in orbits]
print('VERIFY_OK counts=3,6,12,18,30,24,18,0 max_length=7 max_words=18 symmetry_orbits=3 orbit_sizes=6,6,6 cut_predicates=2 enumeration_engines=full+incremental')
