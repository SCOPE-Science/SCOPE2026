#!/usr/bin/env python3
"""Finite checks for bounded-grade term operations on complete S5 frames."""
import itertools
import math
import random
from collections import defaultdict

def clipped_classes(n, m, cap):
    out = defaultdict(set)
    for seq in itertools.product(range(m), repeat=n):
        c = tuple(seq.count(a) for a in range(m))
        v = tuple(min(cap, x) for x in c)
        out[v].add(c)
    return out

def exponent_by_histograms(n, m, cap):
    classes = clipped_classes(n, m, cap)
    return sum(sum(x > 0 for x in v) for v in classes),len(classes)

def exponent_closed_form(n,m,cap):
    e = 0
    for v in itertools.product(range(cap+1), repeat=m):
        s = sum(v)
        if (max(v)<cap and s==n) or (max(v)==cap and s<=n):
            e += sum(bool(x) for x in v)
    return e

def exponent_unbounded(n,m):
    return m * math.comb(n+m-2,m-1)

def exponent_stable(m,cap):
    return m * (cap*(cap+1)**(m-1) - (cap-1)*cap**(m-1))

def direct_clone_cardinality(n,cap):
    """Term-function closure in the actual n-point complex algebra, one input set."""
    ni=1<<n
    bit_count=n*ni
    top=(1<<bit_count)-1
    variable=sum((mask << (n*mask)) for mask in range(ni))
    zero=0
    full=sum(((1<<n)-1) << (n*mask) for mask in range(ni))
    ops={zero, full, variable}
    seen_list=list(ops)
    def diamond(f,k):
        out=0
        for x in range(ni):
            y=(f>>(n*x)) & (ni-1)
            if y.bit_count()>=k:
                out|=(ni-1) << (n*x)
        return out
    while True:
        old=len(seen_list)
        for x in tuple(seen_list):
            for z in (top ^ x, *(diamond(x,k) for k in range(1,cap+1))):
                if z not in ops:ops.add(z);seen_list.append(z)
        oldlist=tuple(seen_list)
        for i,x in enumerate(oldlist):
            for y in oldlist[:i+1]:
                z=x&y
                if z not in ops:ops.add(z);seen_list.append(z)
        if len(seen_list)==old:break
        assert len(seen_list)<10000
    return len(ops)

def random_formula_check(n,r,cap,trials,seed):
    rng=random.Random(seed)
    m=1<<r
    cases=list(itertools.product(range(m),repeat=n))
    group=defaultdict(list)
    for labels in cases:
        c=tuple(labels.count(a) for a in range(m))
        group[tuple(min(cap,v) for v in c)].append(labels)
    # Finite recursive formula syntax as tuples.
    def make(depth):
        if depth==0 or rng.randrange(4)==0:
            return ('var',rng.randrange(r)) if r else ('const',rng.randrange(2))
        op=rng.choice(('not','and','dia'))
        if op=='not':return ('not',make(depth-1))
        if op=='and':return ('and',make(depth-1),make(depth-1))
        return ('dia',rng.randrange(1,cap+1),make(depth-1))
    def val(t,l):
        typ=t[0]
        if typ=='var':return tuple((x>>t[1])&1 for x in l)
        if typ=='const':return (t[1],)*n
        if typ=='not':return tuple(1-x for x in val(t[1],l))
        if typ=='and':return tuple(a&b for a,b in zip(val(t[1],l),val(t[2],l)))
        child=val(t[2],l)
        return (int(sum(child)>=t[1]),)*n
    for _ in range(trials):
        t=make(4)
        profiles={}
        for clipped,ls in group.items():
            for l in ls:
                vv=val(t,l)
                mapping={a:next(v for a2,v in zip(l,vv) if a==a2) for a in set(l)}
                if clipped in profiles:
                    assert profiles[clipped]==mapping,(n,r,cap,t,clipped)
                else:profiles[clipped]=mapping
    return trials*len(cases)

def main():
    comparisons=0
    for n in range(1,7):
      for m in (1,2,4):
       if m**n>50000:continue
       for k in range(1,5):
        e,_=exponent_by_histograms(n,m,k)
        assert e==exponent_closed_form(n,m,k)
        if k>=n:assert e==exponent_unbounded(n,m)
        if n>=m*k:assert e==exponent_stable(m,k)
        comparisons+=1
    closure_cases=0
    for n,k in ((1,1),(2,1),(3,1),(3,2),(4,1),(4,2)):
        expected=2**exponent_closed_form(n,2,k)
        got=direct_clone_cardinality(n,k)
        assert got==expected,(n,k,got,expected)
        closure_cases+=1
    random_checks=0
    for n,r,k in ((2,1,1),(3,1,2),(4,2,1),(4,2,2),(5,2,3)):
        random_checks+=random_formula_check(n,r,k,20,n*100+r*10+k)
    for m in (2,4,8):
     for k in (1,2,3):
      assert exponent_closed_form(m*k,m,k)==exponent_stable(m,k)
      assert exponent_closed_form(m*k-1,m,k) < exponent_stable(m,k)
    cutoff_checks=0
    for m in (2,3,4,5):
      for n in range(1,15):
        # Directly enumerate weak compositions of n into m parts.
        def compositions(total, parts):
            if parts==1:
                yield (total,)
            else:
                for a in range(total+1):
                    for tail in compositions(total-a,parts-1):
                        yield (a,)+tail
        for k in range(1,min(7,n)+1):
            profiles={tuple(min(k,c) for c in v) for v in compositions(n,m)}
            e=sum(sum(bool(x) for x in v) for v in profiles)
            assert (e==exponent_unbounded(n,m))==(k >= ((n+1)//2))
            cutoff_checks+=1
    print('VERIFY_OK histogram_comparisons',comparisons,'direct_term_closures',closure_cases,'random_formula_checks',random_checks,'sharp_plateau_cases',9,'full_grade_cutoff_checks',cutoff_checks)
if __name__=='__main__':main()
