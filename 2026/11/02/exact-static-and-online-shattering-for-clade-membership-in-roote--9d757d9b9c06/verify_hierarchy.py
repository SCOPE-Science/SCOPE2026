#!/usr/bin/env python3
"""Finite checks for clade-membership concept classes (Python standard library only).

Mathematical proof for all n appears in RESULT.md. This program checks small
instances, the explicit VC witness construction and the positive-branch product.
"""
from functools import lru_cache
from itertools import combinations, product

@lru_cache(None)
def binary_trees(mask):
    if mask.bit_count()==1:
        return (mask,)
    bit=mask&-mask
    res=[]
    sub=(mask-1)&mask
    while sub:
        if sub&bit and sub!=mask:
            other=mask^sub
            for A in binary_trees(sub):
                for B in binary_trees(other):
                    res.append((A,B))
        sub=(sub-1)&mask
    return tuple(res)

def node_clades(T, full):
    if isinstance(T,int):return ((),T)
    A,maskA=node_clades(T[0],full)
    B,maskB=node_clades(T[1],full)
    union=maskA|maskB
    return (A+B+((union,) if union!=full else ()),union)

def class_code(n,maximal):
    full=(1<<n)-1
    queries=tuple(s for s in range(1,full) if 2<=s.bit_count()<n)
    qindex={s:i for i,s in enumerate(queries)}
    patterns=set()
    for T in binary_trees(full):
        clades,_=node_clades(T,full)
        mask=sum(1<<qindex[c] for c in clades)
        if maximal:patterns.add(mask)
        else:
            sub=mask
            while True:
                patterns.add(sub)
                if not sub:break
                sub=(sub-1)&mask
    return queries, tuple(sorted(patterns))

def littlestone(queries,patterns):
    n=len(patterns); m=len(queries)
    allh=(1<<n)-1
    column=[0]*m
    for j,p in enumerate(patterns):
        for k in range(m):
            if p>>k&1: column[k]|=1<<j
    @lru_cache(None)
    def can(S,d):
        if d==0:return True
        pop=S.bit_count()
        if pop<1<<d:return False
        half=1<<(d-1)
        branches=[]
        for k,c in enumerate(column):
            yes=S&c; ct=yes.bit_count()
            if ct>=half and pop-ct>=half:
                branches.append((abs(pop-2*ct),yes,S^yes))
        branches.sort(key=lambda x:x[0])
        for _,yes,no in branches:
            if can(yes,d-1) and can(no,d-1):return True
        return False
    for d in range(1,n.bit_length()+1):
        if not can(allh,d):return d-1,can.cache_info().currsize
    return n.bit_length(),can.cache_info().currsize

def graft(first,indices):
    """Rooted binary tree with first subtree plus a nonempty added leaf block."""
    assert indices
    rest=1<<indices[-1]
    for i in reversed(indices[:-1]):rest=(1<<i,rest)
    return (first,rest)

def witness(n,chosen):
    """Chosen subset of prefix lengths 2,...,n-1 is exactly realized."""
    T=1 # singleton leaf with bitmask 1
    a=1
    for b in sorted(chosen|{n}):
        T=graft(T,range(a,b))
        a=b
    return T

def test_prefix(n):
    Q,P=class_code(n,True)
    qs={q:i for i,q in enumerate(Q)}
    allpatterns=set(P)
    for j in range(1<<(n-2)):
        chosen={i+2 for i in range(n-2) if j>>i&1}
        T=witness(n,chosen)
        c,_=node_clades(T,(1<<n)-1)
        realized=set(c)
        support={ (1<<k)-1 for k in range(2,n) }
        desired={ (1<<k)-1 for k in chosen }
        assert realized&support==desired,(n,chosen,realized)
        code=sum(1<<qs[s] for s in realized)
        assert code in allpatterns
    print('PREFIX_VC_WITNESSES_PASS n={} labelings={}'.format(n,1<<(n-2)),flush=True)

def test_projection(n):
    """Validate bijections positive branch == Cartesian product for n<=5."""
    Q,P=class_code(n,False)
    full=(1<<n)-1
    concept_sets=[{Q[i] for i in range(len(Q)) if p>>i&1} for p in P]
    for A in Q:
        inside=tuple(sorted(x for x in range(n) if A>>x&1))
        outside=tuple(sorted(x for x in range(n) if not(A>>x&1)))
        # map inner proper clusters to original bitmasks, outer to B containing A or disjoint
        inner_queries={B for B in Q if B&A==B and B!=A}
        outer_queries={B for B in Q if B&A==0 or B&A==A}
        forbidden={B for B in Q if B not in inner_queries|outer_queries|{A}}
        positive=[F for F in concept_sets if A in F]
        assert all(not (F&forbidden) for F in positive)
        # All possible pairs of projections appear exactly once.
        pairs={(frozenset(F&inner_queries),frozenset(F&outer_queries)) for F in positive}
        inners={t[0] for t in pairs}; outers={t[1] for t in pairs}
        assert len(pairs)==len(inners)*len(outers),(n,A,len(pairs),len(inners),len(outers))
        assert len(pairs)==len(positive)
    print('POSITIVE_BRANCH_PRODUCT_PASS n={} queries={}'.format(n,len(Q)),flush=True)

def main():
    for n in range(2,8):
        Q,B=class_code(n,True)
        expected=1
        for j in range(3,2*n-2,2):expected*=j
        assert len(B)==expected,(n,len(B),expected)
        if n>=3:test_prefix(n)
        d,states=littlestone(Q,B)
        assert d==n-2,(n,d)
        print('BINARY_DIMENSIONS_PASS n={} trees={} Ldim={} states={}'.format(n,len(B),d,states),flush=True)
    for n in range(2,7):
        Q,P=class_code(n,False)
        d,states=littlestone(Q,P)
        assert d==n-2,(n,d)
        print('ALL_HIERARCHIES_DIMENSIONS_PASS n={} hierarchies={} Ldim={} states={}'.format(n,len(P),d,states),flush=True)
        if n<=5 and n>=3:test_projection(n)
    print('CLUSTER_QUERY_ALL_CHECKS_PASS')

if __name__=='__main__':main()
