#!/usr/bin/env python3
"""Independent finite checks for edge-overlap concept lattices.
This verifier uses exhaustive incidence-matrix closure for n <= 6,
intersection-generation for n <= 9, and independently generated graph families.
"""
from itertools import combinations, permutations
from math import comb


def context(n):
    edges = tuple(combinations(range(n), 2))
    masks = tuple(sum(1 << j for j, f in enumerate(edges)
                      if e[0] in f or e[1] in f)
                  for e in edges)
    allmask = (1 << len(edges)) - 1
    return edges, masks, allmask


def polar(mask, masks, allmask):
    answer = allmask
    for i in range(len(masks)):
        if (mask >> i) & 1:
            answer &= masks[i]
    return answer


def formula(n):
    m = comb(n, 2)
    return 2 + 2*m + comb(m, 2) + 15*comb(n, 4) + comb(n, 3) + n + n*comb(n-1, 2)


def expected(n, edges):
    if n == 3:
        return {(1 << len(edges)) - 1}
    eidx = {e:i for i,e in enumerate(edges)}
    def mask(E):
        return sum(1 << eidx[tuple(sorted(e))] for e in set(map(frozenset,E)))
    def incident(a):
        return [e for e in edges if a in e]
    C = {0, (1 << len(edges)) - 1}
    for e in edges:
        C.add(1 << eidx[e])
    for a,b in combinations(range(len(edges)),2):
        C.add((1 << a) | (1 << b))
    for vs in combinations(range(n), 3):
        C.add(mask(combinations(vs, 2)))
    for vs in combinations(range(n), 4):
        for order in permutations(vs):
            C.add(mask((order[i],order[i+1]) for i in range(3)))
            C.add(mask((order[i],order[(i+1)%4]) for i in range(4)))
    for center in range(n):
        st = incident(center)
        C.add(mask(st))
        for b,c in combinations([v for v in range(n) if v!=center],2):
            C.add(mask(st + [(b,c)]))
    for a,b in edges:
        C.add(mask(set(incident(a)) | set(incident(b))))
    return C


def generated(masks, allmask):
    visited={allmask}
    layer=[allmask]
    for x in layer:
        for N in masks:
            nxt=x & N
            if nxt not in visited:
                visited.add(nxt)
                layer.append(nxt)
    return visited


def check():
    full_combinations = 0
    generated_total = 0
    witnesses=0
    for n in range(3,10):
        edges, neigh, universe = context(n)
        want=expected(n,edges)
        if n==3:
            assert want=={universe}
        else:
            assert len(want)==formula(n), (n,len(want),formula(n))
        got=generated(neigh,universe)
        assert got==want, (n,len(got),len(want),len(got-want),len(want-got))
        generated_total += len(got)
        if n<=6:
            seen=set()
            for x in range(universe+1):
                c=polar(polar(x,neigh,universe),neigh,universe)
                assert c in want
                assert (c & x)==x
                assert polar(polar(c,neigh,universe),neigh,universe)==c
                seen.add(c)
                full_combinations += 1
            assert seen==got
        if n>=5:
            pairs=tuple(combinations(range(len(edges)),2))
            for i,j in pairs:
                is_adj = bool(set(edges[i]) & set(edges[j]))
                cnt=sum(1 for k in range(len(edges)) if k!=i and k!=j and ((1<<i)|(1<<j)|(1<<k)) in want)
                assert cnt==(2*n-5 if is_adj else 4),(n,edges[i],edges[j],cnt)
                witnesses+=1
        if n<=5:
            # Every underlying vertex permutation preserves the complete family.
            idx={e:i for i,e in enumerate(edges)}
            for perm in permutations(range(n)):
                emap=tuple(idx[tuple(sorted([perm[e[0]],perm[e[1]]]))] for e in edges)
                for x in want:
                    y=sum(1<<emap[i] for i in range(len(edges)) if (x>>i)&1)
                    assert y in want
        print(f'CASE n={n} concepts={len(got)} exhaustive_initials={universe+1 if n<=6 else 0} PASS')
    print(f'VERIFY_OK generated_concepts={generated_total} exhaustive_initial_sets={full_combinations} line_graph_pair_witnesses={witnesses} n=3..9 direct_classification=PASS automorphism_invariants=PASS')
if __name__=='__main__':check()
