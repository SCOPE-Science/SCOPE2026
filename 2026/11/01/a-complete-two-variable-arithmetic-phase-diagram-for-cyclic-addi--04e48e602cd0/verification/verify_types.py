#!/usr/bin/env python3
"""Exact noncounting FO^2 unary-type refinement for R(x,y,z) iff x+y=z."""
from collections import defaultdict
import json

def invariant(n):
    a=0; m=n
    while not m%2:
        a+=1;m//=2
    if m==1: phase='fixed-only'
    elif m==3: phase='fixed-and-two'
    elif m%3==0: phase='two-and-long'
    else: phase='long-no-two'
    return (a,phase)

def refine(max_n=160,max_q=12):
    offsets={};o=0
    for n in range(1,max_n+1):offsets[n]=o;o+=n
    labels=[int(a==0) for n in range(1,max_n+1) for a in range(n)]
    trace=[]
    for q in range(max_q+1):
        structures={n:frozenset(labels[offsets[n]:offsets[n]+n]) for n in offsets}
        groups=defaultdict(list)
        for n,v in structures.items():groups[v].append(n)
        wrong=[]
        vals=list(offsets)
        for i,n in enumerate(vals):
            for m in vals[:i]:
                if (structures[n]==structures[m])!=(invariant(n)==invariant(m)):
                    wrong.append((n,m))
        trace.append((q,len(set(labels)),len(groups),len(wrong)))
        if not wrong:
            print(json.dumps({'check':'all_pairs_agree','max_n':max_n,'quantifier_round':q,'unary_colors':len(set(labels)),'logical_classes':len(groups),'all_pairs_checked':max_n*(max_n-1)//2,'mismatches':0,'trace':trace}))
            return
        if q==max_q:break
        updated=[]
        for n in offsets:
            base=offsets[n]
            for x in range(n):
                # Atomic 2-variable diagrams include every substitution of x/y in R.
                patterns=set()
                for y in range(n):
                    atom=(x==y,x==0,y==0,(2*x)%n==y,(2*y)%n==x)
                    patterns.add((atom,labels[base+y]))
                updated.append((labels[base+x],frozenset(patterns)))
        lookup={};new=[]
        for s in updated:
            if s not in lookup:lookup[s]=len(lookup)
            new.append(lookup[s])
        labels=new
    print(json.dumps({'check':'FAIL','max_n':max_n,'trace':trace,'mismatches':wrong[:30]}))
    raise AssertionError('classification not matched')

if __name__=='__main__': refine()
