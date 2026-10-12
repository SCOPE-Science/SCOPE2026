#!/usr/bin/env python3
import json
from itertools import product
from pathlib import Path

root=Path(__file__).resolve().parent
cert=json.loads((root/'certificate.json').read_text(encoding='utf-8'))

def is_prefix_normal(w):
    n=len(w)
    pref=0
    for k in range(1,n+1):
        pref += (w[k-1]=='1')
        best=max(s.count('1') for s in (w[i:i+k] for i in range(n-k+1)))
        if pref < best:
            return False
    return True

def pal_from_half(h,n):
    if n%2==0:
        return h+h[::-1]
    return h+h[-2::-1]

def pn_pals(n):
    hlen=(n+1)//2
    out=[]
    for bits in product('01', repeat=hlen):
        h=''.join(bits)
        w=pal_from_half(h,n)
        if is_prefix_normal(w): out.append(w)
    return out

def inject_even(w):
    m=len(w)//2
    x=w[:m]
    assert w==x+x[::-1]
    return x+'0'+x[::-1]

def structural_case_check(w):
    m=len(w)//2
    v=inject_even(w)
    assert v==v[::-1]
    for k in range(1,len(v)+1):
        pv=v[:k].count('1')
        for i in range(len(v)-k+1):
            u=v[i:i+k]
            assert u.count('1')<=pv
            # Replay the two cases used in the symbolic proof.
            center=m
            crosses=(i<=center<i+k)
            if k<=m:
                if crosses:
                    uprime=u[:center-i]+u[center-i+1:]
                    # Removing the inserted zero gives the corresponding factor of w.
                    j=i
                    assert w[j:j+k-1]==uprime
                    candidates=[]
                    if j>0: candidates.append(w[j-1:j+k-1])
                    if j+k-1<len(w): candidates.append(w[j:j+k])
                    assert any(len(z)==k and z.count('1')>=u.count('1') for z in candidates)
                else:
                    # Factors after the inserted zero shift left by one in w.
                    j=i if i+k<=center else i-1
                    assert w[j:j+k]==u
            else:
                assert crosses
                uprime=u[:center-i]+u[center-i+1:]
                j=i
                assert w[j:j+k-1]==uprime
                assert v[:k].count('1')==w[:k-1].count('1')
    return v

all_sets={}
for n in range(1,24):
    all_sets[n]=pn_pals(n)
assert [len(all_sets[n]) for n in range(1,24)]==cert['known_counts_n_1_to_23']

for m in range(1,12):
    even=all_sets[2*m]
    odd=set(all_sets[2*m+1])
    images=[]
    for w in even:
        v=structural_case_check(w)
        assert v in odd
        images.append(v)
    assert len(images)==len(set(images))==len(even)
    assert '1'*(2*m+1) in odd
    assert '1'*(2*m+1) not in images
    assert len(odd)>=len(even)+1

print('VERIFY_OK n=1..23 counts_match=1 m=1..11 injection=1 structural_cases=1 strict_witness=all_ones')
