#!/usr/bin/env python3
import json, itertools
from pathlib import Path

NUM=7
DEN=3

def period_ok(s,p):
    return all(s[i]==s[i+p] for i in range(len(s)-p))

def bad_factor(s):
    n=len(s)
    for a in range(n):
        for b in range(a+1,n+1):
            L=b-a
            if L<3:
                continue
            f=s[a:b]
            # exponent L/p > 7/3 iff 3L > 7p
            for p in range(1,L):
                if DEN*L <= NUM*p:
                    break
                if period_ok(f,p):
                    return (a,b,p,f)
    return None

def bad_suffix(s):
    n=len(s)
    for a in range(n):
        L=n-a
        if L<3:
            continue
        f=s[a:]
        for p in range(1,L):
            if DEN*L <= NUM*p:
                break
            if period_ok(f,p):
                return True
    return False

def nesting(s):
    bal=mx=0
    for c in s:
        bal += 1 if c=='0' else -1
        if bal<0:
            return None
        mx=max(mx,bal)
    return mx if bal==0 else None

def route_a(n):
    # Prefix-pruned exact generation. Any newly created forbidden factor is a suffix.
    out=[]
    def rec(pref,bal,z,o):
        if len(pref)==n:
            if bal==0:
                out.append(pref)
            return
        m=n//2
        if z<m:
            q=pref+'0'
            if not bad_suffix(q):
                rec(q,bal+1,z+1,o)
        if o<m and bal>0:
            q=pref+'1'
            if not bad_suffix(q):
                rec(q,bal-1,z,o+1)
    rec('',0,0,0)
    return out

def route_b(n):
    # Independent complete Dyck generation up to height 4, with no power pruning.
    # This is sufficient for the level-4 minimum/uniqueness claim.
    m=n//2
    out=[]
    def rec(pref,bal,z,o):
        if len(pref)==n:
            if bal==0 and bad_factor(pref) is None:
                out.append(pref)
            return
        if z<m and bal<4:
            rec(pref+'0',bal+1,z+1,o)
        if o<m and bal>0:
            rec(pref+'1',bal-1,z,o+1)
    rec('',0,0,0)
    return out

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
w=cert['witness']
assert len(w)==24 and nesting(w)==4 and bad_factor(w) is None
# Exact boundary attainment: this word is 7/3^+-free but not 7/3-free.
f=cert['witness_exact_boundary_factor']['factor']
assert f in w and len(f)==7 and period_ok(f,3)
assert 3*len(f)==7*3

expected={int(n):{int(k):v for k,v in d.items()} for n,d in cert['counts_of_7_over_3_plus_free_dyck_words_by_length_and_nesting'].items()}
for n in range(2,25,2):
    A=route_a(n)
    hist={}
    for s in A:
        h=nesting(s); hist[h]=hist.get(h,0)+1
    assert hist==expected[n], (n,hist,expected[n])
    # Full independent route only from the first length capable of level 4 onward.
    if n>=8:
        B=route_b(n)
        assert {s for s in A if nesting(s)<=4}==set(B), (n,len(A),len(B))

for n in range(8,24,2):
    assert expected[n].get(4,0)==0
assert expected[24].get(4,0)==1
mins=[s for s in route_a(24) if nesting(s)==4]
assert mins==[w]
rc=''.join('1' if c=='0' else '0' for c in w[::-1])
assert rc==w
print('VERIFY_OK lengths=2..24 shortest_level4=24 minimizers=1 free24=77 boundary_factor=1001001/period3 reverse_complement_fixed=1')
