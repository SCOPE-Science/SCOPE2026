#!/usr/bin/env python3
import itertools
import json
from fractions import Fraction
from pathlib import Path

ALPH='012'; N=22; TARGET=Fraction(20,11)

def is_period(s,p):
    return all(s[i]==s[i-p] for i in range(p,len(s)))

def least_period(s):
    for p in range(1,len(s)+1):
        if is_period(s,p): return p
    raise AssertionError

def suffix_bad_A(w):
    n=len(w)
    for L in range(1,n+1):
        s=w[n-L:]
        for p in range(1,L):
            if 11*L>20*p and is_period(s,p): return True
    return False

def suffix_bad_B(w):
    # Independent period computation: compute only the least period of each suffix.
    n=len(w)
    for L in range(1,n+1):
        s=w[n-L:]
        p=least_period(s)
        if 11*L>20*p: return True
    return False

def build(bad):
    levels=[['']]
    for _ in range(1,N+1):
        nxt=[]
        for w in levels[-1]:
            for c in ALPH:
                q=w+c
                if not bad(q): nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def circular_within_target(w):
    d=w+w
    for start in range(N):
        for L in range(1,N+1):
            s=d[start:start+L]
            # It suffices to test the least period.
            p=least_period(s)
            if 11*L>20*p: return False
    return True

def circular_ce_rotations(w):
    best=Fraction(1,1); crit=[]
    for k in range(N):
        r=w[k:]+w[:k]
        for i in range(N):
            for j in range(i+1,N+1):
                s=r[i:j]; p=least_period(s); e=Fraction(len(s),p)
                if e>best: best=e; crit=[s]
                elif e==best: crit.append(s)
    return best,sorted(set(crit))

def canonrot(w): return min(w[k:]+w[:k] for k in range(N))

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
A=build(suffix_bad_A); B=build(suffix_bad_B)
expected=cert['linear_threshold_survivor_counts_0_to_22']
assert [len(x) for x in A]==expected
assert [len(x) for x in B]==expected
assert A==B and len(A[N])==3042

# A word with circular CE <= target must lie in A[N]. Filter the complete set.
minimizers=[w for w in A[N] if circular_within_target(w)]
assert len(minimizers)==132
classes=sorted({canonrot(w) for w in minimizers})
assert classes==cert['rotation_classes'] and len(classes)==6
for w in classes:
    assert len({w[k:]+w[:k] for k in range(N)})==N
assert 6*N==len(minimizers)

# Every threshold survivor actually attains equality, so none has CE below target.
# This exact independent rotation scan also validates the stored critical factors.
for w in minimizers:
    ce,_=circular_ce_rotations(w)
    assert ce==TARGET
for w in classes:
    ce,crit=circular_ce_rotations(w); assert ce==TARGET
    for s in cert['critical_factors_by_rotation_representative'][w]:
        assert len(s)==20 and least_period(s)==11 and s in (w+w) and s in crit

perms=[str.maketrans(dict(zip(ALPH,p))) for p in itertools.permutations(ALPH)]
def class_orbit(w):
    out=set()
    for tr in perms:
        q=w.translate(tr); out.add(canonrot(q)); out.add(canonrot(q[::-1]))
    return out
rem=set(classes); orbits=[]
while rem:
    w=min(rem); o=class_orbit(w)&set(classes); orbits.append(sorted(o)); rem-=o
assert len(orbits)==1 and len(orbits[0])==6

print('VERIFY_OK threshold_survivors22=3042 minimizers_linear=132 rotation_classes=6 '
      'symmetry_orbits=1 min_ce=20/11 engines=2 ce_methods=2 counts=' + ','.join(map(str,expected)))
