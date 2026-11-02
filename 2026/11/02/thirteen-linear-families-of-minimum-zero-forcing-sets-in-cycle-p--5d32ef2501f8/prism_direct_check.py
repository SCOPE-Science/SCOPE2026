#!/usr/bin/env python3
"""Independent direct zero-forcing and exchange enumeration for finite prisms."""
from itertools import combinations,product
from collections import Counter

def neighbours(n):
    result=[0]*(2*n)
    for z in (0,1):
        for i in range(n):
            j=i+n*z
            result[j]=(1<<((i-1)%n+n*z)) | (1<<((i+1)%n+n*z)) | (1<<(i+n*(1-z)))
    return result

def forces(seed_mask, nbrs):
    full=(1<<len(nbrs))-1
    active=seed_mask
    while active!=full:
        new=0
        for v in range(len(nbrs)):
            if active>>v&1:
                white=nbrs[v]&~active
                if white and white&(white-1)==0:new |= white
        if new==0:return False
        active |= new
    return True

def prism_templates(n):
    exemplars=( ((0,1),(0,1)), ((0,1),(0,n-1)),
                ((0,1,2,3),()), ((0,1,2),(0,)), ((0,1,3),(1,)) )
    all_sets=set()
    for u,l in exemplars:
        for ref in (-1,1):
            for rot in range(n):
                for sw in (0,1):
                    mask=0
                    for layer,arr in enumerate((u,l)):
                        for i in arr:
                            mask|=1<<((ref*i+rot)%n+n*(layer^sw))
                    all_sets.add(mask)
    return all_sets

def check_cyclic_words():
    count=0
    # This is an independently implemented check of every compressed
    # pattern. It does not use the fort automaton or its multiplication.
    cache={}
    for weight in (1,2,3,4):
        for cols in range((weight+1)//2,weight+1):
            for letters in product((1,2,3),repeat=cols):
                if sum(x.bit_count() for x in letters)!=weight: continue
                for gaps in product(range(6),repeat=cols):
                    n=cols+sum(gaps)
                    if n<6:continue
                    if n not in cache:cache[n]=(neighbours(n),prism_templates(n))
                    masks,templates=cache[n]
                    mask=0; i=0
                    for digit,gap in zip(letters,gaps):
                        if digit&1:mask|=1<<i
                        if digit&2:mask|=1<<(n+i)
                        i+=gap+1
                    expected=(weight==4 and mask in templates)
                    actual=forces(mask,masks)
                    if actual!=expected:
                        raise AssertionError(('cyclic mismatch',weight,n,letters,gaps,actual,expected))
                    count+=1
    print('INDEPENDENT_ALL_COMPRESSED_PATTERNS_PASS',count)

def check_small_prisms():
    for n in range(6,16):
        N=2*n
        nbrs=neighbours(n)
        templates=prism_templates(n)
        assert len(templates)==13*n
        for k in (1,2,3):
            for choose in combinations(range(N),k):
                s=sum(1<<v for v in choose)
                if forces(s,nbrs):raise AssertionError(('too small',n,s))
        sols=set()
        for choose in combinations(range(N),4):
            s=sum(1<<v for v in choose)
            if forces(s,nbrs):sols.add(s)
        assert sols==templates,('bad templates',n,len(sols))
        adj={v:set() for v in sols}
        for s in sols:
            for removed in range(N):
                if s>>removed&1:
                    for added in range(N):
                        if not(s>>added&1):
                            t=s^(1<<removed)^(1<<added)
                            if t in sols:adj[s].add(t)
        hist=Counter(map(len,adj.values()))
        assert hist == {5:4*n,8:8*n,12:n},('bad hist',n,hist)
        seen={next(iter(sols))}
        q=list(seen)
        for s in q:
            for t in adj[s]:
                if t not in seen:seen.add(t);q.append(t)
        assert seen==sols,('not connected',n)
        print('DIRECT_ENUMERATION_PASS',n,'vertices',len(sols),'edges',sum(map(len,adj.values()))//2)
    print('INDEPENDENT_DIRECT_EXCHANGE_ALL_TESTS_PASS')

if __name__=='__main__':
    check_cyclic_words()
    check_small_prisms()
