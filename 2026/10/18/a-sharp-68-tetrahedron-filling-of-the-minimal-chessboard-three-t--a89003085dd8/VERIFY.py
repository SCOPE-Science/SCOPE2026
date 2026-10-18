#!/usr/bin/env python3
"""Exact verification of a matching-complex two-cycle filling and its dual bound.

Run with Python 3 standard library from the directory containing CERTIFICATE.json.
"""
import json
from itertools import combinations,product
from pathlib import Path

def faces(k):
    return [t for t in combinations(range(25), k)
            if len({v//5 for v in t}) == k and len({v%5 for v in t}) == k]

F=[faces(k) for k in range(1,6)]
assert [len(L) for L in F]==[25,200,600,600,120]
index=[{t:i for i,t in enumerate(L)} for L in F]

def boundaries(k):
    return [{index[k-2][t[:i]+t[i+1:]]: (-1)**i
             for i in range(k)} for t in F[k-1]]

b2=boundaries(3)  # C_2 -> C_1
b3=boundaries(4)  # C_3 -> C_2
b4=boundaries(5)  # C_4 -> C_3

def apply(cols, coeff):
    ans={}
    for j,x in coeff.items():
        if not x:continue
        for i,v in cols[j].items():ans[i]=ans.get(i,0)+x*v
    return {i:v for i,v in ans.items() if v}

# Check that the chain complex itself uses consistent simplex orientations.
for j in range(len(b3)):
    assert not apply(b2,b3[j])
for j in range(len(b4)):
    assert not apply(b3,b4[j])

raw=json.loads(Path(__file__).with_name('CERTIFICATE.json').read_text(encoding='utf8'))
pairs=raw['pairs']
assert pairs==[[0,1],[7,8],[14,19]]
z={}
for bits in product((0,1),repeat=3):
    ordered=[pairs[i][bits[i]] for i in range(3)]
    t=tuple(sorted(ordered))
    sign=(-1)**(sum(bits)+sum(ordered[i]>ordered[j]
                  for i in range(3) for j in range(i+1,3)))
    pos=index[2][t];z[pos]=z.get(pos,0)+sign
z={i:v for i,v in z.items() if v}
assert len(z)==8
assert sorted([list(q) for q in z.items()])==sorted(raw['target_two_chain_z'])
assert not apply(b2,z)

w=dict(raw['primal_3chain'])
y_num=dict(raw['dual_2cochain_numerators_over_3'])
assert len(w)==68 and len(y_num)==357
assert set(w)<=set(range(600)) and set(y_num)<=set(range(600))
assert all(v in (-1,1) for v in w.values())
assert sum(abs(v) for v in w.values())==68
assert apply(b3,w)=={i:3*v for i,v in z.items()}
delta_num={j:sum(y_num.get(i,0)*a for i,a in c.items())
           for j,c in enumerate(b3)}
assert max(abs(t) for t in delta_num.values())==3
assert 3*sum(z.get(i,0)*y_num.get(i,0) for i in z)==204
assert sum(z.get(i,0)*y_num.get(i,0) for i in z)==68
# The pairing with 3z is 3 * (sum z*y_num/3) = 68.

# No scalar multiples of z that are nonzero over F_3 are boundaries;
# check directly that z does not belong to im(d3) modulo 3.
piv={}
for c in b3:
    v={i:x%3 for i,x in c.items() if x%3}
    while v:
        p=min(v)
        if p not in piv:
            fac=pow(v[p],-1,3)
            piv[p]={i:(x*fac)%3 for i,x in v.items()}
            break
        m=v[p]
        for i,a in piv[p].items():
            val=(v.get(i,0)-m*a)%3
            if val:v[i]=val
            elif i in v:del v[i]
assert len(piv)==423
v={i:x%3 for i,x in z.items() if x%3}
while v:
    p=min(v)
    if p not in piv:
        break
    m=v[p]
    for i,a in piv[p].items():
        val=(v.get(i,0)-m*a)%3
        if val:v[i]=val
        elif i in v:del v[i]
else:
    raise AssertionError('z would be a mod-three boundary')

# All induced six-vertex flag two-spheres are octahedra. They occur exactly
# when the incompatibility graph on the six rook placements is a matching.
octa=0;types={}
for W in combinations(range(25),6):
    conflict=[]
    for i in range(6):
        for j in range(i+1,6):
            a,b=W[i],W[j]
            if a//5==b//5 or a%5==b%5:
                conflict.append((i,j))
    if len(conflict)!=3 or len({x for pair in conflict for x in pair})!=6:
        continue
    number_row=sum(W[i]//5==W[j]//5 for i,j in conflict)
    types[number_row]=types.get(number_row,0)+1
    octa+=1
assert octa==1800 and types=={1:900,2:900},(octa,types)

print('VERIFY_OK F_VECTOR_25_200_600_600_120 TORSION_OCTAHEDRON_8')
print('THREE_TIMES_CYCLE_PRIMAL_AREA_68 DUAL_LOWER_BOUND_68 EXACT')
print('MOD3_BOUNDARY_RANK_423 OCTAHEDRAL_SUPPORTS_1800 TWO_900_ORBITS')
