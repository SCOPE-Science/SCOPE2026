#!/usr/bin/env python3
"""Exact finite checks for three-part synchronous strict-neighbor majority.

No external packages or resources are required. This program tests finite
parameter ranges only; the all-size result relies on the accompanying proof.
"""
from itertools import combinations_with_replacement, product
from math import comb

def predicted(sizes):
    a,b,c=sizes
    fixed=2+(comb(a,a//2)*comb(b,b//2)*comb(c,c//2) if not (a%2 or b%2 or c%2) else 0)
    def central(p,q):
        return sum(comb(q,r) for r in range(q+1) if abs(2*r-q)<p)
    two=(int(a>max(b,c))+int(b>max(a,c))+int(c>max(a,b)))
    for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
        if sizes[i]==sizes[j]:
            two+=central(sizes[i],sizes[k])
    return fixed,two

def direct_transition(x,sizes):
    counts=[]; partitions=[];off=0
    for n in sizes:
        mask=((1<<n)-1)<<off
        partitions.append(mask)
        counts.append((x&mask).bit_count())
        off+=n
    ret=0
    for i,p in enumerate(partitions):
        degree=sum(sizes)-sizes[i]
        other_ones=sum(counts)-counts[i]
        if 2*other_ones>degree:ret|=p
        elif 2*other_ones==degree:ret|=(x&p)
    return ret

def direct_census(sizes):
    fixed=0; two=0
    for x in range(1<<sum(sizes)):
        y=direct_transition(x,sizes)
        if x==y: fixed+=1
        elif x<y and direct_transition(y,sizes)==x:two+=1
    return fixed,two

def aggregate_transition(counts,sizes):
    s=sum(counts);n=sum(sizes);out=[]
    for x,a in zip(counts,sizes):
        z=2*(s-x)-(n-a)
        out.append(a if z>0 else 0 if z<0 else x)
    return tuple(out)

def aggregate_census(sizes):
    fixed=0;points_two=0
    for x in product(*(range(a+1) for a in sizes)):
        y=aggregate_transition(x,sizes)
        weight=1
        for a,z in zip(sizes,x):weight*=comb(a,z)
        if x==y:fixed+=weight
        elif aggregate_transition(y,sizes)==x:points_two+=weight
    assert points_two%2==0
    return fixed,points_two//2

cases=0; states=0
for triple in combinations_with_replacement(range(1,9),3):
    if sum(triple)>16:continue
    actual=direct_census(triple)
    theory=predicted(triple)
    assert actual==theory,(triple,actual,theory)
    states+=1<<sum(triple);cases+=1
print('BRUTE_OK', 'size_triples',cases,'configurations',states)

cases2=0
for triple in combinations_with_replacement(range(1,21),3):
    if sum(triple)>38:continue
    actual=aggregate_census(triple)
    theory=predicted(triple)
    assert actual==theory,(triple,actual,theory)
    cases2+=1
print('WEIGHTED_AGGREGATE_OK', 'size_triples',cases2)

samples=((1,1,1),(2,2,2),(2,2,3),(1,3,4),(1,1,6),(1,1,7),(4,4,4),(4,4,5),(4,4,6),(3,4,5),(2,4,6))
for triple in samples:
    print('CASE',str(triple), 'fixed',predicted(triple)[0], 'primitive_two_orbits',predicted(triple)[1])
print('ALL_CHECKS_PASS')
