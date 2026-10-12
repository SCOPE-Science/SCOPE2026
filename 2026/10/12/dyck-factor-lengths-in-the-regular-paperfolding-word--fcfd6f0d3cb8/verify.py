#!/usr/bin/env python3
from pathlib import Path
import json

# Regular paperfolding word in the convention used here.
def p(n):
    assert n>=1
    m=n
    while m%2==0:
        m//=2
    return 0 if m%4==1 else 1

def inc(n):
    return 1-2*p(n)

def runs(n):
    if n==0:
        return 0
    b=bin(n)[2:]
    return 1+sum(b[j]!=b[j-1] for j in range(1,len(b)))

def target_length(L):
    if L<=0:
        return False
    # L=2^i(2^d-1), with i>=1 and d>=1.
    i=0
    x=L
    while x%2==0:
        x//=2; i+=1
    return i>=1 and ((x+1)&x)==0

def dyck_factor(start,L):
    # start is 1-based.
    h=0
    for n in range(start,start+L):
        h+=inc(n)
        if h<0:
            return False
    return h==0

# Independent recursive construction: W_{r+1}=W_r 0 complement(reverse(W_r)).
w='0'
for _ in range(1,15):
    w=w+'0'+''.join('1' if c=='0' else '0' for c in reversed(w))
assert len(w)==32767
oddpart=''.join(str(p(n)) for n in range(1,len(w)+1))
assert w==oddpart

# Prefix balance equals binary run count.
s=0
for n in range(1,1_000_001):
    s+=inc(n)
    assert s==runs(n),(n,s,runs(n))

# Direct exhaustive endpoint classification through 4096.
R=[runs(n) for n in range(4097)]
observed=set()
checked=0
for x in range(0,4096):
    h=R[x]
    mn=10**9
    for y in range(x+1,4097):
        mn=min(mn,R[y])
        if mn<h:
            break
        if R[y]==h:
            L=y-x
            observed.add(L)
            assert target_length(L),(x,y,L)
        checked+=1

expected={L for L in range(1,4096) if target_length(L)}
# Every target length <=4096 has its canonical factor inside the checked range.
for L in expected:
    # recover i=v2(L), d from odd part+1
    x=L; i=0
    while x%2==0:
        x//=2; i+=1
    d=(x+1).bit_length()-1
    k=i+d
    start=2**i
    assert start+L-1==2**k-1
    assert start+L-1<=4096
    assert dyck_factor(start,L),(start,L)
assert observed==expected

# Stress canonical factors at larger scales.
canon=0
for k in range(2,18):
    for i in range(1,k):
        L=(1<<k)-(1<<i)
        assert dyck_factor(1<<i,L)
        canon+=1

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text(encoding='utf-8'))
assert cert['source_primary_msc']=='68R15'
assert cert['dyck_length_classification']=='exactly 2^k-2^i with integers 1<=i<k'
print('VERIFY_OK recursive_prefix=32767 prefix_balance_n=1..1000000 '
      f'endpoint_pairs_scanned={checked} endpoint_max=4096 canonical_cases={canon} '
      'classification=2^k-2^i_1<=i<k')
