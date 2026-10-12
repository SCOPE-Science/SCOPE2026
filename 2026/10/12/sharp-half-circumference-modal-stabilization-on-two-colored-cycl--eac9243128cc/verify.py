#!/usr/bin/env python3
"""Independent finite checks for modal refinement on binary-coloured simple cycles.
Only standard-library Python is required.  No finite test claims an infinite proof.
"""
from itertools import product
from collections import Counter
from math import gcd
import random


def canon_factor(word, center, depth):
    n = len(word)
    w = tuple(word[(center+j) % n] for j in range(-depth, depth+1))
    return min(w, w[::-1])


def refine(word, limit=None):
    n = len(word)
    colors = tuple(word)
    out = [colors]
    for _ in range((n+2) if limit is None else limit):
        sig = [(colors[i], tuple(sorted((colors[(i-1)%n], colors[(i+1)%n]))))
               for i in range(n)]
        code = {x:j for j,x in enumerate(sorted(set(sig)))}
        nxt = tuple(code[x] for x in sig)
        out.append(nxt)
        if len(set(nxt)) == len(set(colors)):
            break
        colors = nxt
    return out


def same_partition(a,b):
    n=len(a)
    return all((a[i]==a[j])==(b[i]==b[j]) for i in range(n) for j in range(n))


def automorphism_orbits(word):
    n=len(word)
    maps=[(s,a) for s in (-1,1) for a in range(n)
          if all(word[i] == word[(s*i+a)%n] for i in range(n))]
    groups=[]
    used=set()
    for i in range(n):
        if i in used:continue
        orb={((s*i+a)%n) for s,a in maps}
        groups.append(orb)
        used.update(orb)
    return tuple(tuple(sorted(g)) for g in groups), len(maps)


def mu(k):
    y=k; primes=0; q=2
    while q*q<=y:
        if y%q==0:
            primes += 1; y//=q
            if y%q==0:return 0
            while y%q==0:y//=q
        q+=1
    if y>1:primes+=1
    return (-1)**primes


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def bracelet_count(n):
    primitive=sum(mu(d)*(1 << (n//d)) for d in divisors(n))
    refl=0
    for a in range(n):
        for d in divisors(n):
            m=n//d
            orbits=(m+1)//2 if m%2 else (m//2+1 if a%2==0 else m//2)
            refl += mu(d)*(1 << orbits)
    asym=primitive-refl
    assert asym>=0 and asym%(2*n)==0,(n,primitive,refl,asym)
    return asym//(2*n)


def depth_partition(word,t):
    c=tuple(word)
    for _ in range(t):
        s=[(c[i],tuple(sorted((c[(i-1)%len(c)],c[(i+1)%len(c)])))) for i in range(len(c))]
        tab={k:v for v,k in enumerate(sorted(set(s)))}
        c=tuple(tab[k] for k in s)
    return c


def rank(color):return len(set(color))


def multi_refinement(words):
    offsets=[];N=0
    for w in words:offsets.append(N);N+=len(w)
    col=tuple(x for w in words for x in w)
    neigh=[]
    for off,w in zip(offsets,words):
        n=len(w)
        neigh.extend([(off+(i-1)%n,off+(i+1)%n) for i in range(n)])
    for _ in range(N):
        s=[(col[i],tuple(sorted((col[a],col[b])))) for i,(a,b) in enumerate(neigh)]
        ids={x:k for k,x in enumerate(sorted(set(s)))}
        nxt=tuple(ids[v] for v in s)
        if rank(nxt)==rank(col):return col
        col=nxt
    raise AssertionError('nonstabilization')


def direct_modal_algebra(word):
    n=len(word)
    masks=set([0,(1<<n)-1, sum((1<<i) for i,c in enumerate(word) if c)])
    changed=True
    while changed:
        old=len(masks)
        add=set()
        for a in list(masks):
            add.add(((1<<n)-1)^a)
            add.add(sum((1<<i) for i in range(n)
                        if (a>>((i-1)%n))&1 or (a>>((i+1)%n))&1))
            for b in list(masks):add.add(a&b)
        masks|=add
        changed=len(masks)>old
    return len(masks)


def main():
    total=0;level=0;nontrivial=0;censuses=[]
    for n in range(3,13):
        depth=n//2-1;success=0; maxdepth=-1
        for mask in range(1<<n):
            word=tuple((mask>>i)&1 for i in range(n));total+=1
            orb,autos=automorphism_orbits(word)
            # Modal refinement, centered word windows, and automorphism orbits.
            for t in range(depth+1):
                c=depth_partition(word,t)
                windows=tuple(canon_factor(word,i,t) for i in range(n))
                assert same_partition(c,windows),(n,mask,t)
                level+=1
            c=depth_partition(word,depth)
            orbit_tags=[next(k for k,g in enumerate(orb) if i in g) for i in range(n)]
            assert same_partition(c,orbit_tags),(n,mask)
            if rank(c)==n:
                success+=1; assert autos==1
                first=next(t for t in range(depth+1) if rank(depth_partition(word,t))==n)
                maxdepth=max(first,maxdepth)
                nontrivial+=1
            else: assert autos>1
        b=bracelet_count(n)
        assert success==2*n*b,(n,success,b)
        if n>=6:assert maxdepth==depth,(n,maxdepth,depth)
        else:assert success==0
        censuses.append((n,success,b,maxdepth))
    # Every minimum-support witness is sharp through much larger sizes.
    witnesses=0
    for n in range(6,121):
        w=tuple(int(i in (0,1,3)) for i in range(n));t=n//2-1
        assert rank(depth_partition(w,t))==n
        assert rank(depth_partition(w,t-1))<n
        assert automorphism_orbits(w)[1]==1
        witnesses+=1
    # Direct Boolean closure of one atom: resulting algebra cardinality = 2^(modal types).
    closures=0
    for n in range(3,6):
        for m in range(1<<n):
            w=tuple((m>>i)&1 for i in range(n))
            assert direct_modal_algebra(w)==(1<<rank(depth_partition(w,n//2-1)))
            closures+=1
    # Across components, independence of equal-size asymmetric dihedral bracelets.
    multi_cases=0;multi_success={}
    for lengths in ((6,7),(7,7),(6,6)):
        n,m=lengths;count=0
        for a in range(1<<n):
            w=tuple((a>>i)&1 for i in range(n))
            for b in range(1<<m):
                x=tuple((b>>i)&1 for i in range(m))
                result=multi_refinement((w,x))
                if len(set(result))==n+m:count+=1
                multi_cases+=1
        expected=(2*n*bracelet_count(n))*(2*m*bracelet_count(m))
        if n==m:expected=(2*n*bracelet_count(n))*(2*n*(bracelet_count(n)-1))
        assert count==expected,(lengths,count,expected)
        multi_success[str(lengths)]=count
    rng=random.Random(20261009)
    rand=0
    for n in (20,31,50,101):
        for _ in range(80):
            word=tuple(rng.randrange(2) for _ in range(n))
            c=depth_partition(word,n//2-1)
            w=tuple(canon_factor(word,i,n//2-1) for i in range(n))
            assert same_partition(c,w)
            orb,_=automorphism_orbits(word)
            tags=[next(k for k,g in enumerate(orb) if i in g) for i in range(n)]
            assert same_partition(c,tags)
            rand+=1
    print('VERIFY_OK', 'exhaustive_cycle_colorings',total,'modal_level_comparisons',level,
          'generating_colorings',nontrivial,'direct_boolean_closures',closures,
          'two_component_colorings',multi_cases,'multi_success',multi_success,
          'sharp_witness_sizes',witnesses,'random_checks',rand,'censuses',censuses)

if __name__=='__main__':main()
