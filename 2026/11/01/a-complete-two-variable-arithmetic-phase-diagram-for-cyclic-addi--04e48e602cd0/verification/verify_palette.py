#!/usr/bin/env python3
"""Independent exact pair-extension palette check for the doubling digraph."""
from collections import defaultdict
import json

def profile(n,x):
    a=0;m=n
    while not m%2:a+=1;m//=2
    z=x;t=0
    while z%(2**a): z=(2*z)%n;t+=1
    if z==0:c='F'
    elif (3*z)%n==0:c='T'
    else:c='L'
    return (c,t)

def inv(n):
    a=0;m=n
    while not m%2:a+=1;m//=2
    return(a,'F' if m==1 else 'FT' if m==3 else 'FL' if m%3 else 'FTL')

def signature(n):
    labels=[profile(n,x) for x in range(n)]
    support={}
    for x in range(n):
        k=labels[x]
        v=set()
        for y in range(n):
            v.add((labels[y],x==y,x==0,y==0,2*x%n==y,2*y%n==x))
        if k in support:
            assert support[k]==frozenset(v),(n,x,k,'palette not uniform within label')
        else:support[k]=frozenset(v)
    return tuple(sorted((k,tuple(sorted(v))) for k,v in support.items()))

def main(limit=160):
    sigs={n:signature(n) for n in range(1,limit+1)}
    names={n:inv(n) for n in sigs}
    collisions=[]; mismatches=[]
    for n in sigs:
        for m in range(1,n):
            e1=names[n]==names[m]
            e2=sigs[n]==sigs[m]
            if e1!=e2:mismatches.append((n,m,e1,e2))
            if e1 and n!=m:collisions.append((n,m))
    assert not mismatches,mismatches[:10]
    assert sigs[5]==sigs[7]
    assert sigs[9]==sigs[15]
    assert sigs[18]==sigs[30]
    assert sigs[10]==sigs[14]
    assert sigs[3]!=sigs[9]
    assert sigs[9]!=sigs[5]
    assert sigs[4]!=sigs[8]
    classes={v for v in names.values()}
    print(json.dumps({'check':'pair_extension_palette','max_n':limit,'ordered_anchor_elements_examined':limit*(limit+1)//2,'ordered_pairs_examined':limit*(limit+1)*(2*limit+1)//6,'distinct_invariants':len(classes),'all_modulus_pairs':limit*(limit-1)//2,'equivalent_distinct_pairs':len(collisions),'mismatches':len(mismatches),'example_equivalent':[[5,7],[9,15],[18,30],[10,14]],'example_separated':[[3,9],[5,9],[4,8]],'status':'PASS'}))

if __name__=='__main__':main()
