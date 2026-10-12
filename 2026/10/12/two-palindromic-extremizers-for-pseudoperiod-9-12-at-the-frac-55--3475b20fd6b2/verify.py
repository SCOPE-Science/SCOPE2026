#!/usr/bin/env python3
import json
from pathlib import Path

A,B=9,12
EN,ED=55,21

def pp_new(w):
    n=len(w)
    if n<=B:
        return True
    i=n-1-B
    return w[i]==w[i+A] or w[i]==w[i+B]

def bad_suffix_slices(w):
    n=len(w)
    for p in range(1,n+1):
        L=(EN*p+ED-1)//ED
        if L>n:
            break
        s=w[-L:]
        if s[p:]==s[:-p]:
            return True
    return False

def bad_suffix_loops(w):
    n=len(w)
    for p in range(1,n+1):
        L=(EN*p+ED-1)//ED
        if L>n:
            break
        start=n-L
        ok=True
        for j in range(start+p,n):
            if w[j]!=w[j-p]:
                ok=False
                break
        if ok:
            return True
    return False

def build(bad):
    levels=[['']]
    for _ in range(1,202):
        nxt=[]
        for w in levels[-1]:
            for c in '01':
                q=w+c
                if pp_new(q) and not bad(q):
                    nxt.append(q)
        levels.append(sorted(nxt))
    return levels

def pp_direct(w):
    return all(w[i]==w[i+A] or w[i]==w[i+B] for i in range(max(0,len(w)-B)))

def bad_direct(w):
    n=len(w)
    for p in range(1,n+1):
        L=(EN*p+ED-1)//ED
        if L>n:
            break
        need=L-p
        run=0
        for j in range(n-p):
            if w[j]==w[j+p]:
                run+=1
                if run>=need:
                    return True
            else:
                run=0
    return False

def comp(w):
    return ''.join('1' if c=='0' else '0' for c in w)

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))
A1=build(bad_suffix_slices)
A2=build(bad_suffix_loops)
assert A1==A2
assert [len(x) for x in A1]==cert['survivor_counts_by_length_0_to_201']
assert len(A1[200])==2
assert A1[201]==[]
assert A1[200]==sorted(cert['length_200_extremizers'])
w0,w1=A1[200]
assert w1==comp(w0)
assert w0==w0[::-1] and w1==w1[::-1]
assert cert['published_companion_witness'] in A1[200]
for w in A1[200]:
    assert pp_direct(w)
    assert not bad_direct(w)
    for c in '01':
        q=w+c
        assert (not pp_direct(q)) or bad_direct(q)
print('VERIFY_OK pseudoperiod=9,12 threshold=55/21 max=200 count200=2 count201=0 complement_pair=1 palindromes=2 engines=2 candidates='+str(sum(len(x) for x in A1)))
