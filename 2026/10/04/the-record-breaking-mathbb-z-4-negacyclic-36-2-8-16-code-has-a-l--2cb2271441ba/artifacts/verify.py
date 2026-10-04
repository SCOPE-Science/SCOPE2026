#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))
s=cert['source_generator_string_descending']
n=36
g=tuple(int(ch) for ch in s[::-1])
assert len(g)==n

def negashift(v):
    return ((-v[-1])%4,)+v[:-1]

shifts=[g]
for _ in range(1,n):
    shifts.append(negashift(shifts[-1]))

C={(0,)*n}
for v in shifts:
    old=tuple(C)
    new=set()
    for c in old:
        for a in range(4):
            new.add(tuple((c[i]+a*v[i])%4 for i in range(n)))
    C=new

assert len(C)==cert['code_size']==4096
torsion=sum(all((2*x)%4==0 for x in c) for c in C)
assert torsion==cert['two_torsion_size']==1024

lee=(0,1,2,1)
wd=Counter(sum(lee[x] for x in c) for c in C)
expected={int(k):v for k,v in cert['weight_distribution'].items()}
assert dict(sorted(wd.items()))==expected
assert min(w for w in wd if w)==cert['lee_distance']==16

gray=((0,0),(0,1),(1,1),(1,0))
def grayword(c):
    return tuple(bit for x in c for bit in gray[x])
B={grayword(c) for c in C}
assert len(B)==4096

def bint(v):
    return sum((bit&1)<<i for i,bit in enumerate(v))

def binary_basis(vectors):
    basis={}
    for v in vectors:
        x=bint(v) if not isinstance(v,int) else v
        while x:
            j=x.bit_length()-1
            if j in basis:
                x ^= basis[j]
            else:
                basis[j]=x
                break
    return basis

basis=binary_basis(B)
assert len(basis)==cert['gray_rank']==12
span={0}
for x in basis.values():
    span |= {y^x for y in tuple(span)}
assert len(span)==4096
assert span=={bint(v) for v in B}
assert cert['gray_kernel_dimension']==12

order=cert['orbit_coordinate_order_zero_based']
assert order==list(range(0,72,2))+list(range(1,72,2))
Bord={tuple(v[i] for i in order) for v in B}
# Direct cyclic closure in the orbit order.
assert all(v[-1:]+v[:-1] in Bord for v in Bord)

def degree(p): return p.bit_length()-1
def pmod(a,b):
    db=degree(b)
    while a and degree(a)>=db:
        a ^= b << (degree(a)-db)
    return a
def pgcd(a,b):
    while b:
        a,b=b,pmod(a,b)
    return a

mod=(1<<72)|1
gg=mod
for v in Bord:
    gg=pgcd(gg,bint(v))
exps=[i for i in range(73) if (gg>>i)&1]
assert exps==cert['binary_cyclic_generator_exponents_low_to_high']
assert hex(gg)==cert['binary_cyclic_generator_hex']
assert degree(gg)==60
assert pmod(mod,gg)==0

# The first 12 ordinary polynomial shifts generate the whole cyclic code.
cyc_basis=[gg<<i for i in range(12)]
cyc={0}
for x in cyc_basis:
    cyc |= {y^x for y in tuple(cyc)}
assert len(cyc)==4096
assert cyc=={bint(v) for v in Bord}

# Build a 12-row binary basis and test the dual distance through column dependencies.
bas2=binary_basis(Bord)
rows=[]
for _,x in sorted(bas2.items(),reverse=True):
    rows.append(tuple((x>>i)&1 for i in range(72)))
assert len(rows)==12
cols=[tuple(row[j] for row in rows) for j in range(72)]
ci=[bint(c) for c in cols]
assert all(ci)
assert len(set(ci))==72
colset=set(ci)
for i,j in combinations(range(72),2):
    assert (ci[i]^ci[j]) not in colset
witness=cert['dual_weight_four_witness_zero_based']
a,b,c,d=witness
assert len(set(witness))==4
assert ci[a]^ci[b]^ci[c]^ci[d]==0
assert cert['dual_minimum_distance']==4

print('VERIFY_OK')
