#!/usr/bin/env python3
"""Exact two-round Ehrenfeucht--Fraisse certificate for finite nilpotent monogenic semigroups.
No libraries beyond Python standard library. Each truth-vector is a complete reduction of the
atomic diagram of (selected x,y,named zero)."""
from collections import defaultdict
from itertools import product

def binary_multiply(t,u,v): return min(t,u+v)
def pair_full(t,x,y):
    a=(x,y,t)
    return (tuple(a[i]==a[j] for i in range(3) for j in range(3)),
            tuple(binary_multiply(t,a[i],a[j])==a[k] for i in range(3) for j in range(3) for k in range(3)))
def pair_reduced(t,x,y):
    return (x==t,y==t,x==y,2*x>=t,2*y>=t,x+y>=t,
            binary_multiply(t,x,x)==y,binary_multiply(t,y,y)==x)
def portrait(t,which):
    fun=pair_full if which=='full' else pair_reduced
    byx={x:frozenset(fun(t,x,y) for y in range(1,t+1)) for x in range(1,t+1)}
    grouped=defaultdict(list)
    for x,p in byx.items(): grouped[p].append(x)
    return byx,grouped
for t in (16,20):
    a,ga=portrait(t,'full'); b,gb=portrait(t,'reduced')
    assert len(ga)==len(gb)==12
    assert all((a[x]==a[y])==(b[x]==b[y]) for x in a for y in a)
# Compare global interstructure correlations, not just within each structure.
all_x=[(t,x) for t in (16,20) for x in range(1,t+1)]
pairs_full={p:portrait(t,'full')[0][x] for p in all_x for t,x in [p]}
pairs_red={p:portrait(t,'reduced')[0][x] for p in all_x for t,x in [p]}
assert all((pairs_full[p]==pairs_full[q])==(pairs_red[p]==pairs_red[q]) for p in all_x for q in all_x)
g16=portrait(16,'reduced')[1];g20=portrait(20,'reduced')[1]
assert set(g16)==set(g20)
print('rank-two equivalence: PASS')
print('Complete one-point extension profiles:',len(g16))
print('Class | N16 first-move indices | N20 first-move indices | 8-bit patterns')
for i,p in enumerate(sorted(g16,key=lambda p:min(g16[p])),1):
    codes=sorted(sum(int(v)<<k for k,v in enumerate(a)) for a in p)
    print(i,','.join(map(str,g16[p])),','.join(map(str,g20[p])),','.join(map(str,codes)),sep=' | ')

def distinction(t):
    # Exists x,y,z with x*x=y, x*y=z, z*z=zero, y*z nonzero.
    return [(x,y,z) for x,y,z in product(range(1,t+1),repeat=3)
            if binary_multiply(t,x,x)==y and binary_multiply(t,x,y)==z
            and binary_multiply(t,z,z)==t and binary_multiply(t,y,z)!=t]
assert distinction(16)==[(3,6,9)]
assert distinction(20)==[]
print('Rank-three separator: PASS. N16 witness (3,6,9), N20 no witness.')
print('Arithmetic separator 5i<t<=6i: N16', [i for i in range(1,17) if 5*i<16<=6*i],
      'N20',[i for i in range(1,21) if 5*i<20<=6*i])
