#!/usr/bin/env python3
"""Finite transformation checks for stylic automorphism rigidity.
This program constructs transformations of all subsets by column insertion,
then checks Green-order generator covers, ordered-pair tests and evacuation
on small ranks. No external dependencies.
"""
from itertools import permutations

def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def monoid(n):
    domain=range(1<<n)
    generators=[]
    for a in range(n):
        values=[]
        for c in domain:
            yi=next((j for j in range(a,n) if (c>>j)&1),None)
            d=c if yi is None else c & ~(1<<yi)
            values.append(d|(1<<a))
        generators.append(tuple(values))
    unit=tuple(domain)
    words={unit:()}
    queue=[unit]
    for p in queue:
        for a,g in enumerate(generators):
            h=compose(g,p)
            if h not in words:
                words[h]=(a,)+words[p]
                queue.append(h)
    return queue,words,generators

def bell(n):
    triangle=[[1]]
    for k in range(1,n+1):
        prev=triangle[-1]
        row=[prev[-1]]
        for j in range(1,k+1): row.append(row[-1]+prev[j-1])
        triangle.append(row)
    return triangle[n][0]

def main():
    for n in range(1,6):
        elements,words,gens=monoid(n)
        m=len(elements)
        assert m==bell(n+1),(n,m,bell(n+1))
        unit=elements[0]
        idx={v:i for i,v in enumerate(elements)}
        sup=lambda w:sum(1<<a for a in set(w))
        for p in elements:
            # Support of products is union, checked against the actual transform model.
            assert p[0]==(lambda s: __import__('functools').reduce(lambda c,a:gens[a][c],reversed(s),0))(words[p])
        idem={p for p in elements if compose(p,p)==p}
        assert len(idem)==(1<<n)
        # Rank-one-cover check, using the full J-order for n<=4.
        if n<=4:
            ideals={}
            for p in elements:
                ideals[p]=frozenset(compose(compose(x,p),y) for x in elements for y in elements)
            covers=[p for p in elements if p!=unit and not any(ideals[p] < ideals[z] < ideals[unit] for z in elements)]
            assert set(covers)==set(gens),(n,len(covers))
        for a in range(n):
            for b in range(n):
                if a==b:continue
                pair=compose(gens[a],gens[b])
                assert (pair in idem)==(a>b),(n,a,b)
        # The only valid permutation of intrinsic generators is the identity.
        valid=[]
        for pi in permutations(range(n)):
            if all((compose(gens[pi[a]],gens[pi[b]]) in idem)==(a>b)
                   for a in range(n) for b in range(n) if a!=b):
                valid.append(pi)
        assert valid==[tuple(range(n))]
        # Reverse-word / reverse-order map is an anti-automorphism.
        def tau(w):
            r=unit
            for a in w:
                r=compose(gens[n-1-a],r)
            return r
        # tau word should map w=a_1...a_k to reversed-letter word,
        # i.e. t_{theta(a_k)} ... t_{theta(a_1)};
        # iterative composition on the left does that.
        images={p:tau(words[p]) for p in elements}
        assert len(set(images.values()))==m
        assert all(images[images[p]]==p for p in elements)
        for p in elements:
            for q in elements:
                assert images[compose(p,q)]==compose(images[q],images[p]),(n,p,q)
        print('rank',n,'elements',m,'idempotents',len(idem),'generator permutations',len(valid),'anti-involution OK')
    print('VERIFY_OK')
if __name__=='__main__': main()
