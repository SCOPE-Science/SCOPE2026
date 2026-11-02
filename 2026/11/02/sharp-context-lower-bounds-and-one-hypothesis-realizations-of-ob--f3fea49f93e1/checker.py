#!/usr/bin/env python3
"""Finite tests for minimal Horn observation-contract realization resources.
The infinite lower bound is algebraic and not inferred from these tests.
"""
from itertools import combinations, product, permutations
from collections import Counter


def antichain(edges):
    return all(not (a & b == a or a & b == b) for a,b in combinations(edges,2))

def contract_from_families(contexts, families):
    """Enumerate minimal empty-intersection context sets and minimize spans."""
    bad=[]
    for k in range(1,len(contexts)+1):
        for ix in combinations(range(len(contexts)),k):
            inter=set(families[ix[0]])
            for j in ix[1:]: inter.intersection_update(families[j])
            if inter: continue
            if any(set(prev).issubset(ix) for prev in bad): continue
            bad.append(ix)
    spans=[]
    for ix in bad:
        union=0; intersect=(1<<30)-1
        for j in ix:
            union|=contexts[j]; intersect&=contexts[j]
        spans.append(union ^ intersect)
    return frozenset(e for e in spans if not any(f != e and (f & e)==f for f in spans))

def horn_valid(n, c, hyp, edges):
    f={f'x{i}{(c>>i)&1}' for i in range(n)}
    if hyp: f.add('h')
    rules=[]
    zero_body=frozenset(f'x{i}0' for i in range(n))
    rules.append((zero_body,'g'))
    rules.append((zero_body|{'h'},'bottom'))
    for e in edges:
        code=frozenset(f'x{i}{(e>>i)&1}' for i in range(n))
        rules.append((code|{'h'},'g'))
    while True:
        add={head for body,head in rules if body<=f}
        if add<=f: break
        f|=add
    return 'g' in f and 'bottom' not in f

def private_rank(edges):
    best=0
    for k in range(1,len(edges)+1):
        for sub in combinations(edges,k):
            if all(any((e & (1<<j)) and not any((f & (1<<j)) for f in sub if f!=e)
                       for j in range(max(sub).bit_length())) for e in sub):
                best=max(best,k)
    return best

def all_trees(n):
    for comb in combinations(list(combinations(range(n),2)),n-1):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        good=True
        for a,b in comb:
            ra,rb=root(a),root(b)
            if ra==rb: good=False; break
            parent[ra]=rb
        if good: yield comb

def check():
    tests=0
    # Exhaustive simple antichains on <=4 Boolean source variables.
    for n in range(1,5):
        subsets=range(1,1<<n)
        for selection in range(1<<len(subsets)):
            edges=tuple(e for j,e in enumerate(subsets) if (selection>>j)&1)
            if not antichain(edges): continue
            contexts=[0,*edges] if edges else [0]
            families=[]
            for c in contexts:
                choices=frozenset(h for h in (0,1) if horn_valid(n,c,h,edges)) if edges else frozenset({0})
                families.append(choices)
            got=contract_from_families(contexts,families)
            assert got == frozenset(edges), (n,edges,got,families)
            assert len(contexts)>=private_rank(edges)+1
            if edges:
                assert families[0]==frozenset({0})
                assert all(a==frozenset({1}) for a in families[1:])
            tests+=1
    # Exhaustively inspect all 4^8 partial two-choice semantic tables on the 3-cube.
    tables=0
    codes=list(range(8))
    for state in product((-1,0,1,2),repeat=8):
        cc=[c for c,s in zip(codes,state) if s!=-1]
        if not cc: continue
        fs=[frozenset((0,1)) if s==2 else frozenset((s,))
            for s in state if s!=-1]
        h=contract_from_families(cc,fs)
        if not h or 0 in h: continue
        assert len(cc) >= 1+private_rank(tuple(h))
        tables+=1
    # Each labeled tree on m+1 contexts with disjoint witness supports works.
    trees_checked=0
    for m in range(1,5):
        for tree in all_trees(m+1):
            for labels in permutations(1<<i for i in range(m)):
                adj=[[] for _ in range(m+1)]
                for (u,v),lab in zip(tree,labels):
                    adj[u].append((v,lab)); adj[v].append((u,lab))
                ctx={0:0}; color={0:0}; todo=[0]
                for u in todo:
                    for v,lab in adj[u]:
                        if v not in ctx:
                            ctx[v]=ctx[u]^lab
                            color[v]=1-color[u]
                            todo.append(v)
                assert len(set(ctx.values()))==m+1
                cc=[ctx[i] for i in range(m+1)]
                fs=[frozenset((color[i],)) for i in range(m+1)]
                assert contract_from_families(cc,fs)==frozenset(labels)
                trees_checked+=1
    print(f'ALL_CHECKS_OK antichains={tests} semantic_tables={tables} tree_models={trees_checked}')

if __name__=='__main__':
    check()
