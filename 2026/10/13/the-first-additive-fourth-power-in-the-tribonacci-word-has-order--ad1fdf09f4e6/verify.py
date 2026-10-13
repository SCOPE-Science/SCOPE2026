#!/usr/bin/env python3
import json
from pathlib import Path

M={"0":"01","1":"02","2":"0"}

def morph(w):
    return "".join(M[c] for c in w)

# Build sigma^8(0) in two ways.
u="0"
for _ in range(8):
    u=morph(u)

W0="0"
W1="01"
W2="0102"
ws=[W0,W1,W2]
for n in range(3,9):
    ws.append(ws[n-1]+ws[n-2]+ws[n-3])
v=ws[8]

assert u==v
assert len(u)==149

def factors(w,L):
    return {w[i:i+L] for i in range(len(w)-L+1)}

def add4(f,n):
    sums=[sum(int(c) for c in f[j*n:(j+1)*n]) for j in range(4)]
    return len(set(sums))==1, sums

expected_factor_counts=[9,17,25,33,41,49]
expected_power_counts=[0,0,0,0,0,1]
observed=[]
for n in range(1,7):
    L=4*n
    F=factors(u,L)
    # Published factor complexity of the Tribonacci word is p(L)=2L+1.
    # Reaching this number makes the observed set exhaustive.
    assert len(F)==2*L+1
    good=[]
    for f in sorted(F):
        ok,sums=add4(f,n)
        if ok:
            good.append((f,sums))
    observed.append(good)

assert [2*(4*n)+1 for n in range(1,7)]==expected_factor_counts
assert [len(x) for x in observed]==expected_power_counts

witness="102010102010010201010201"
assert observed[5]==[(witness,[4,4,4,4])]
assert [witness[i*6:(i+1)*6] for i in range(4)]==[
    "102010","102010","010201","010201"
]
assert u.find(witness)==76

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["factor_counts"]==expected_factor_counts
assert cert["additive_fourth_power_factor_counts"]==expected_power_counts
assert cert["unique_order_6_factor"]==witness
assert cert["order_6_block_sums"]==[4,4,4,4]

print(
    "VERIFY_OK sigma8_length=149 factors=9,17,25,33,41,49 "
    "additive4_counts=0,0,0,0,0,1 minimum_order=6 "
    "unique_factor=102010102010010201010201 first_index=76 "
    "constructors=morphism+tribonacci_recurrence"
)
