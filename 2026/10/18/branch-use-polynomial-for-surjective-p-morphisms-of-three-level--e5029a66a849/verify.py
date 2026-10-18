#!/usr/bin/env python3
"""Direct exhaustive finite verification of a branching p-morphism count.
Pure standard-library code; no external data or dependencies.
"""
from itertools import product
from math import comb
from hashlib import sha256
import json


def tree(profile):
    parents=[-1]; centers=[]
    for s in profile:
        center=len(parents); centers.append(center); parents.append(0)
        for j in range(s):parents.append(center)
    up=[]
    for x in range(len(parents)):
        descendants=[]
        for y in range(len(parents)):
            z=y
            while z != -1 and z != x:
                z=parents[z]
            if z==x:descendants.append(y)
        up.append(frozenset(descendants))
    return parents,up


def exhaustive(source,target):
    ps, up_s=tree(source)
    pt, up_t=tree(target)
    n,m=len(ps),len(pt)
    count=0
    # Both roots are forced because p-morphisms must be surjective.
    for tail in product(range(m),repeat=n-1):
        f=(0,)+tail
        if all(frozenset(f[z] for z in up_s[x])==up_t[f[x]] for x in range(n)):
            count+=1
    return count


def surj(n,k):
    return sum((-1)**(k-j)*comb(k,j)*j**n for j in range(k+1))


def formula(source,target):
    k=len(target); L=sum(target); ans=0
    for mask in range(1<<k):
        J=[j for j in range(k) if mask&(1<<j)]
        term=1
        for s in source:
            term*=L+sum(surj(s,target[j]) for j in J)
        ans+=(-1)**(k-len(J))*term
    return ans


def condition(source,target):
    s=sorted(source,reverse=True); t=sorted(target,reverse=True)
    return len(s)>=len(t) and all(s[j]>=t[j] for j in range(len(t)))


def dp(source,target):
    k=len(target); L=sum(target); ways={0:1}
    for s in source:
        nxt={}
        for mask,v in ways.items():
            nxt[mask]=nxt.get(mask,0)+v*L
            for j,l in enumerate(target):
                newmask=mask|(1<<j)
                nxt[newmask]=nxt.get(newmask,0)+v*surj(s,l)
        ways=nxt
    return ways.get((1<<k)-1,0)

def cases():
    for r in range(1,4):
        for src in product(range(1,4),repeat=r):
            if 1+r+sum(src)>7:continue
            for k in range(1,3):
                for tgt in product(range(1,3),repeat=k):
                    if 1+k+sum(tgt)>6:continue
                    yield src,tgt

def main():
    checked=0; zero=0; largest=0; records=[]
    for src,tgt in cases():
        actual=exhaustive(src,tgt)
        predicted=formula(src,tgt)
        feasible=condition(src,tgt)
        assert actual==predicted,(src,tgt,actual,predicted)
        assert (actual>0)==feasible,(src,tgt,actual,feasible)
        checked+=1;zero+=(actual==0);largest=max(largest,actual)
        records.append([list(src),list(tgt),actual])
    raw=json.dumps(records,separators=(',',':')).encode()
    print(json.dumps({'case_count':checked,'zero_cases':zero,'largest_count':largest,'case_table_sha256':sha256(raw).hexdigest(),'tested_source_vertices_at_most':7,'tested_target_vertices_at_most':6},sort_keys=True))
    # A dynamic subset-counting recurrence supplies a second independent implementation
    # of the branch-image enumeration, for a much larger parameter rectangle.
    big=0; positives=0; vmax=0
    for r in range(1,5):
        for src in product(range(1,5),repeat=r):
            for k in range(1,4):
                for tgt in product(range(1,4),repeat=k):
                    direct=dp(src,tgt); closed=formula(src,tgt)
                    assert direct==closed,(src,tgt,direct,closed)
                    assert (direct>0)==condition(src,tgt)
                    big+=1;positives+=(direct>0);vmax=max(vmax,direct)
    print(json.dumps({'larger_dp_cases':big,'positive_cases':positives,'largest_dp_count':vmax},sort_keys=True))
    print('VERIFIED')
if __name__=='__main__': main()
