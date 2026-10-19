#!/usr/bin/env python3
"""Exact finite clique-complex and homology checks for rank-one partial injections.

No external dependencies. Computes boundaries over F_2 and compares with sphere S^(n-2).
"""
from collections import defaultdict
from itertools import combinations


def maps(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def compose(f, g):
    # g after f, with an empty map encoded as None.
    return (f[0], g[1]) if f[1] == g[0] else None


def faces(n):
    arcs = maps(n)
    K = {frozenset()}
    for mask in range(1, (1 << n) - 1):
        A = {i for i in range(n) if mask & (1 << i)}
        eligible = [k for k, (i, j) in enumerate(arcs) if i in A and j not in A]
        for r in range(1, len(eligible)+1):
            for C in combinations(eligible, r):
                K.add(frozenset(C))
    return arcs, K


def gf2_rank(columns):
    pivots = {}
    for c in columns:
        while c:
            p = c.bit_length()-1
            if p in pivots:
                c ^= pivots[p]
            else:
                pivots[p] = c
                break
    return len(pivots)


def bettis(K):
    by_size = defaultdict(list)
    for face in K:
        if face: by_size[len(face)].append(tuple(sorted(face)))
    counts = {k:len(v) for k,v in by_size.items()}
    ranks = {}
    for k in sorted(by_size):
        if k == 1: ranks[k] = 0; continue
        below = {f:i for i,f in enumerate(by_size[k-1])}
        cols=[]
        for f in by_size[k]:
            c = 0
            for x in f:
                sub=tuple(y for y in f if y != x)
                c ^= 1 << below[sub]
            cols.append(c)
        ranks[k] = gf2_rank(cols)
    return counts, {k:counts[k]-ranks[k]-ranks.get(k+1,0)-(1 if k==1 else 0) for k in counts}



def permutation_sign(sequence):
    return (-1)**sum(sequence[i]>sequence[j] for i in range(len(sequence)) for j in range(i+1,len(sequence)))


def lef_trace(n, arcs, K, perm, invert):
    idx={a:i for i,a in enumerate(arcs)}
    on=[]
    for a,b in arcs:
        aa,bb=perm[a],perm[b]
        if invert: aa,bb=bb,aa
        on.append(idx[(aa,bb)])
    total=0
    for face in K:
        if not face: continue
        sf=sorted(face)
        image=[on[i] for i in sf]
        if set(image)!=face: continue
        induced=[sf.index(x) for x in image]
        total+=(-1)**(len(face)-1)*permutation_sign(induced)
    return (-1)**(n-2)*(total-1)


def check_actions(n, arcs, K):
    idperm=list(range(n))
    twoperm=list(range(n)); twoperm[0],twoperm[1]=twoperm[1],twoperm[0]
    cycle=list(range(1,n))+[0]
    for perm in (idperm,twoperm,cycle):
        for inv in (False,True):
            expected=permutation_sign(perm) * ((-1)**(n-1) if inv else 1)
            obtained=lef_trace(n,arcs,K,perm,inv)
            assert obtained==expected,(n,perm,inv,obtained,expected)

def main():
    for n in range(2,6):
        arcs, K = faces(n)
        for a,b in combinations(range(len(arcs)),2):
            i,j=arcs[a],arcs[b]
            assert ((compose(i,j)==compose(j,i)) ==
                    (i[1]!=j[0] and j[1]!=i[0]))
        for F in K:
            if F:
                pairs=list(combinations(F,2))
                assert all(compose(arcs[a],arcs[b])==compose(arcs[b],arcs[a]) for a,b in pairs)
        check_actions(n,arcs,K)
        f,b= bettis(K)
        assert sum((-1)**(size-1)*count for size,count in f.items()) == 1+(-1)**(n-2)
        assert b == {k:int(k-1==n-2) for k in f}
        assert sum(f.values())+1==len(K)
        expected_facets={frozenset(i for i,(a,c) in enumerate(arcs) if a in A and c not in A) 
          for size in range(1,n) for A in combinations(range(n),size)}
        facets={F for F in K if not any(F<T for T in K)}
        assert facets==expected_facets
        print('n=',n,'f=',f,'beta_F2=',b,'facets=',len(facets))
    print('VERIFY_OK_RANK_ONE_COMMUTING_EQUIVARIANT')


if __name__=='__main__':
    main()
