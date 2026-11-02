#!/usr/bin/env python3
"""Independent non-counting three-pebble fixed-point refinement on finite incidence structures."""
from itertools import product
from verify_extension import CASES

def atom(v,blocks,t):
    a,b,c=t
    sorts=tuple(int(x>=v) for x in t)
    equal=(a==b,a==c,b==c)
    incidence=[]
    for x,y in ((a,b),(a,c),(b,c)):
        if (x<v)==(y<v):incidence.append(False)
        else:
            p=x if x<v else y
            j=y-v if y>=v else x-v
            incidence.append(p in blocks[j])
    return sorts,equal,tuple(incidence)

cases={key: CASES[key] for key in ('Fano_7_3_1','complement_Fano_7_4_2','biplane_11_5_2','projective_13_4_1')}
tables={}
for name,(v,blocks) in cases.items():
    n=2*v
    tuples=list(product(range(n),repeat=3))
    tables[name]=(n,tuples,{t:atom(v,blocks,t) for t in tuples})

colordict={};colors={}
for name,(n,ts,atoms) in tables.items():
    for t in ts:
        a=atoms[t]
        if a not in colordict: colordict[a]=len(colordict)
    colors[name]={t:colordict[atoms[t]] for t in ts}

for step in range(50):
    sigmap={};updated={}
    for name,(n,ts,atoms) in tables.items():
        old=colors[name]; new={}
        for a,b,c in ts:
            s=(old[(a,b,c)],
               frozenset(old[(z,b,c)] for z in range(n)),
               frozenset(old[(a,z,c)] for z in range(n)),
               frozenset(old[(a,b,z)] for z in range(n)))
            if s not in sigmap:sigmap[s]=len(sigmap)
            new[(a,b,c)]=sigmap[s]
        updated[name]=new
    old_count=len({z for d in colors.values() for z in d.values()})
    new_count=len(sigmap)
    print('refinement',step,'classes',new_count)
    colors=updated
    if new_count==old_count:break
else:raise AssertionError('no stabilization')

base=None
for name,(n,ts,atoms) in tables.items():
    single={colors[name][(a,a,a)] for a in range(n)}
    pairs={colors[name][(a,a,b)] for a in range(n) for b in range(n)}
    if base is None:base=(single,pairs)
    assert base==(single,pairs),(name,'disagree')
    print(name,'singleton-colors=',len(single),'pair-colors=',len(pairs))
print('PASS: all four designs have the same stable 3-pebble non-counting types')
