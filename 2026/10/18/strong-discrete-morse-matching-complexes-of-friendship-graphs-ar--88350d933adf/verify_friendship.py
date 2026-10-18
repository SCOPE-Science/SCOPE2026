#!/usr/bin/env python3
"""Finite reproducibility checks of strong graph-Morse windmill decomposition.

The graph is one-dimensional: its 3-cycles are not filled triangles.
Only vertex-edge Hasse pairs occur. No external dependencies.
"""
from itertools import permutations, product
from collections import defaultdict, Counter


def graph(n):
    m = 2*n+1
    neigh = [0]*m
    for i in range(n):
        a,b = 2*i+1,2*i+2
        for v,w in [(0,a),(0,b),(a,b)]:
            neigh[v] |= 1<<w
            neigh[w] |= 1<<v
    arrows = sorted((v,w) for v in range(m) for w in range(m) if neigh[v]>>w&1)
    return neigh, {x:i for i,x in enumerate(arrows)}, arrows


def generated_from_orders(n):
    neigh,ids,_=graph(n)
    out=set()
    for order in permutations(range(2*n+1)):
        earlier=0
        mask=0
        for v in order:
            q=earlier&neigh[v]
            if q.bit_count()==1:
                mask|=1<<ids[(v,q.bit_length()-1)]
            earlier |= 1<<v
        out.add(mask)
    return out


def generated_by_subset_dp(n):
    neigh,ids,_=graph(n)
    N=2*n+1
    states={0:{0}}
    for _ in range(N):
        nxt=defaultdict(set)
        for seen,options in states.items():
            for v in range(N):
                if seen>>v&1:continue
                prev=neigh[v]&seen
                bit=1<<ids[(v,prev.bit_length()-1)] if prev.bit_count()==1 else 0
                nxt[seen|1<<v].update(m|bit for m in options)
        states=nxt
    return next(iter(states.values()))


def predicted_facets(n):
    _, ids, _ = graph(n)
    # With no hub-head pair, choose one of four oriented pairs per petal.
    D=[]
    P=[]
    for i in range(n):
        a,b=2*i+1,2*i+2
        D.append([ids[(a,b)],ids[(b,a)],ids[(a,0)],ids[(b,0)]])
        P.append([ids[(a,0)],ids[(b,0)]])
    facets=set()
    for choice in product(*D):
        facets.add(sum(1<<q for q in choice))
    # With hub paired to one outer vertex of petal i, all other
    # petals can contribute a unique outer-to-hub oriented pair.
    for i in range(n):
        for apex in [2*i+1,2*i+2]:
            for choice in product(*(P[j] for j in range(n) if j!=i)):
                facets.add((1<<ids[(0,apex)]) | sum(1<<q for q in choice))
    return facets


def downward(facets):
    found={0}
    for f in facets:
        v=f
        while v:
            found.add(v)
            v=(v-1)&f
    return found


def rank_mod2(columns):
    piv={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:
                piv[p]=v
                break
    return len(piv)


def homology(faces):
    bydim=defaultdict(list)
    for f in faces:
        if f:bydim[f.bit_count()-1].append(f)
    R={-1:0}
    for k in sorted(bydim):
        if k==0:
            R[k]=0
            continue
        rowids={x:i for i,x in enumerate(bydim[k-1])}
        cols=[]
        for face in bydim[k]:
            mask=0
            p=face
            while p:
                t=p&-p
                mask|=1<<rowids[face^t]
                p^=t
            cols.append(mask)
        R[k]=rank_mod2(cols)
    dims=sorted(bydim)
    betti={k:len(bydim[k])-R[k]-R.get(k+1,0)-(1 if k==0 else 0) for k in dims}
    fvec={k:len(bydim[k]) for k in dims}
    return fvec,betti


def main():
    for n in range(1,6):
        from_orders=generated_from_orders(n) if n<=4 else generated_by_subset_dp(n)
        predicted=predicted_facets(n)
        truefaces=downward(from_orders)
        modelfaces=downward(predicted)
        assert truefaces==modelfaces,(n,len(truefaces),len(modelfaces))
        maximal={f for f in from_orders if not any((f!=g and f&g==f) for g in from_orders)}
        assert maximal==predicted,(n,len(maximal),len(predicted))
        fvec,betti=homology(truefaces)
        expected_dim=n-1
        expected_rank=3**n+2*n if n>=2 else 5
        assert betti=={k:(expected_rank if k==expected_dim else 0) for k in fvec}, (n,betti)
        print(f'n={n} method={"orders" if n<=4 else "subset-DP"} full_matchings={len(from_orders)} facets={len(maximal)} faces={len(truefaces)-1} fvec={fvec} reduced_mod2_betti={betti}')
    print('PASS: exact face equality, predicted facets, and mod-2 Betti ranks for n=1,...,5')

if __name__=='__main__':
    main()
