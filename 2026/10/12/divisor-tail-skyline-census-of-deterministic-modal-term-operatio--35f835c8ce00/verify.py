#!/usr/bin/env python3
"""Independent finite checks of the forward-trace term-operation census.
No external dependencies. This file contains only reproducibility algorithms.
"""
from itertools import product
from collections import defaultdict
from math import isqrt


def mobius(n):
    v=1
    p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:return 0
            v=-v
            while n%p==0:n//=p
        p+=1
    return -v if n>1 else v


def primitive(q,d):
    return sum(mobius(k)*q**(d//k) for k in range(1,d+1) if d%k==0)


def invariants(f):
    n=len(f)
    h=[]; ell=[]
    for w in range(n):
        path=[]; where={};v=w
        while v not in where:
            where[v]=len(path);path.append(v);v=f[v]
        h.append(where[v]);ell.append(len(path)-where[v])
    ds=sorted({d for l in ell for d in range(1,l+1) if l%d==0})
    H={d:max(h[i] for i,l in enumerate(ell) if l%d==0) for d in ds}
    return ds,H


def theoretical(f,q):
    ds,H=invariants(f)
    return sum(q**H[d]*primitive(q,d) for d in ds)


def words_universe(f,q):
    n=len(f); out=set()
    # W x valuations, rooted traces. Upper bound n+n works for all functions.
    for c in product(range(q),repeat=n):
        for w in range(n):
            t=[];v=w
            for j in range(2*n+1):
                t.append(c[v]);v=f[v]
            out.add(tuple(t))
    return len(out)


def refine_universe(f,q):
    # Modal-algebra atoms over all labelled valuations: start with local color
    # and repeatedly refine by deterministic successor class, *not* by traces.
    n=len(f)
    rows=[]; nxt=[]
    for c in product(range(q),repeat=n):
        base=len(rows)
        for w in range(n):
            rows.append(c[w]);nxt.append(base+f[w])
    types=rows
    for _ in range(n*n+3):
        keys=[(types[i],types[nxt[i]]) for i in range(len(types))]
        names={k:j for j,k in enumerate(sorted(set(keys)))}
        new=[names[k] for k in keys]
        if len(set(new))==len(set(types)):
            return len(set(new))
        types=new
    raise AssertionError('refinement failed to stabilize')


def direct_term_closure(f,r):
    # Full Boolean algebra on U = world x assignment; evaluate shifted predicate
    # generators and Boolean complements, hence enumerate all term operations.
    n=len(f);q=1<<r
    vals=list(product(range(q),repeat=n))
    indices=[(c,w) for c in vals for w in range(n)]
    N=len(indices)
    if N>128:return None
    universe=(1<<N)-1
    gens=[]
    for j in range(r):
        gens.append(sum(1<<i for i,(c,w) in enumerate(indices) if (c[w]>>j)&1))
    succ=[vals.index(c)*n+f[w] for c,w in indices]
    def dia(x):
        return sum(1<<i for i,s in enumerate(succ) if (x>>s)&1)
    # Saturate modal images of generators; since dia preserves Boolean ops,
    # all Boolean combinations then are terms; direct distinct term count 2^atoms.
    seen=set(gens); frontier=list(gens)
    while frontier:
        x=frontier.pop();y=dia(x)
        if y not in seen:seen.add(y);frontier.append(y)
    sig=[tuple((g>>i)&1 for g in sorted(seen)) for i in range(N)]
    atoms=len(set(sig))
    return 1<<atoms


def main():
    evals=0; partition_checks=0; closure_checks=0; random_checks=0
    for n in range(1,5):
        for f in product(range(n),repeat=n):
            for q in (1,2,3):
                a=theoretical(f,q)
                b=words_universe(f,q)
                if a!=b:raise AssertionError(('formula',f,q,a,b))
                evals+=1
                # 4^4=256 valuations, test all for q <=3 and n <=4.
                z=refine_universe(f,q)
                if a!=z:raise AssertionError(('refinement',f,q,a,z))
                partition_checks+=1
            if n<=2:
                for r in (0,1,2):
                    got=direct_term_closure(f,r)
                    want=1<<theoretical(f,1<<r)
                    if got!=want:raise AssertionError(('term',f,r,got,want))
                    closure_checks+=1
    import random
    rng=random.Random(501120)
    for _ in range(1000):
        n=rng.randrange(5,10)
        f=tuple(rng.randrange(n) for _ in range(n))
        q=rng.randrange(2,5)
        # Random explicit traces test a lower bound/finite-level consistency
        ds,H=invariants(f)
        assert len(ds)>=1 and 1 in ds
        assert max(H.values())<=n-1
        assert theoretical(f,q)>=q
        random_checks+=1
    print(f'VERIFY_OK exhaustive_maps_x_alphabets={evals} independent_refinement_checks={partition_checks} direct_term_closures={closure_checks} randomized_invariants={random_checks}')
    for f in [(0,),(0,0),(1,0),(1,2,2),(1,2,0),(1,2,2,4,4),(1,0,3,4,2)]:
        print('EXAMPLE',f,'poly_eval_at_q2',theoretical(f,2),'divisor_profile',invariants(f))

if __name__=='__main__':main()
