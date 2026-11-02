#!/usr/bin/env python3
"""Finite exhaustive shattering verification for 321-avoiding involutions.
Usage: python3 verify.py [tree_certificate.json]
No external dependencies.
"""
from itertools import combinations, permutations
from functools import lru_cache
from math import comb
from pathlib import Path
import json

EXPECTED=[(1,0,0),(2,1,1),(3,1,1),(6,2,2),(10,2,2),
          (20,3,3),(35,3,4),(70,4,5),(126,4,5),
          (252,5,6),(462,5,7),(924,6,8)]

def involutions(n):
    """Enumerate involutions via fixed points or two-cycles on the least unused index."""
    def walk(unused,perm):
        if not unused:
            yield tuple(perm)
            return
        i=unused[0]
        perm[i]=i
        yield from walk(unused[1:],perm)
        for j in unused[1:]:
            perm[i]=j
            perm[j]=i
            yield from walk(tuple(k for k in unused[1:] if k!=j),perm)
        perm[i]=-1
        for j in unused[1:]:perm[j]=-1
    yield from walk(tuple(range(n)),[-1]*n)

def avoids321(p):
    """No triple i<j<k with p[i]>p[j]>p[k]."""
    n=len(p)
    for j in range(1,n-1):
        if any(p[i]>p[j] for i in range(j)) and any(p[k]<p[j] for k in range(j+1,n)):
            return False
    return True

def concepts(n):
    a=sorted(p for p in involutions(n) if avoids321(p))
    assert len(a)==len(set(a))
    assert len(a)==comb(n,n//2),('count disagreement',n,len(a))
    return a

def matrix(C):
    q=list(combinations(range(len(C[0])),2))
    masks=[]
    for i,j in q:
        masks.append(sum(1<<k for k,p in enumerate(C) if p[i]>p[j]))
    return q,masks

def vc_dimension(q,masks,m):
    """Exhaustively extend increasing query index sets; each fiber must split."""
    full=(1<<m)-1
    best=0;best_support=[];nodes=0
    def explore(start,fibers,S):
        nonlocal best,best_support,nodes
        nodes+=1
        if len(S)>best:
            best=len(S);best_support=S
        if not all(f.bit_count()>=2 for f in fibers):return
        for t in range(start,len(masks)):
            M=masks[t]
            nxt=[]
            for fiber in fibers:
                A=fiber&M;B=fiber^A
                if A==0 or B==0:break
                nxt.extend((A,B))
            else:
                explore(t+1,nxt,S+(t,))
    explore(0,[full],())
    return best,[q[i] for i in best_support],nodes

def littlestone(masks,m):
    """Exact recurrence L(S)=1+max_q min(L(S&Q),L(S\\Q))."""
    full=(1<<m)-1
    @lru_cache(None)
    def L(S):
        if S.bit_count()<2:return 0
        bound=S.bit_count().bit_length()-1
        best=0;seen=set()
        for M in masks:
            A=S&M;B=S^A
            if not A or not B or A in seen:continue
            seen.add(A);seen.add(B)
            if min(A.bit_count(),B.bit_count())<(1<<best):continue
            val=1+min(L(A),L(B))
            if val>best:best=val
            if best==bound:break
        return best
    return L,L(full)

def verify_tree(node,S,q,masks,C,depth):
    if depth==0:
        assert isinstance(node,dict) and set(node)=={'witness'}
        k=node['witness']
        assert isinstance(k,int) and 0<=k<len(C) and ((S>>k)&1)
        return {k}
    assert isinstance(node,dict) and set(node)=={'query','zero','one'}
    t=node['query'];assert isinstance(t,int) and 0<=t<len(q)
    A=S&masks[t];B=S^A
    assert A and B
    leaves0=verify_tree(node['zero'],B,q,masks,C,depth-1)
    leaves1=verify_tree(node['one'],A,q,masks,C,depth-1)
    assert leaves0.isdisjoint(leaves1)
    return leaves0|leaves1

def main():
    certificates=json.loads(Path(__file__).with_name('tree_certificate.json').read_text(encoding='utf-8'))
    assert set(certificates)=={'11','12'}
    for n,(expected_count,expected_vc,expected_ld) in enumerate(EXPECTED,1):
        C=concepts(n);q,masks=matrix(C)
        assert len(C)==expected_count
        vc,support,nodes=vc_dimension(q,masks,len(C))
        assert vc==expected_vc,(n,'VC',vc,expected_vc)
        L,ld=littlestone(masks,len(C))
        assert ld==expected_ld,(n,'Ldim',ld,expected_ld)
        if str(n) in certificates:
            ct=certificates[str(n)]
            assert ct['n']==n and ct['depth']==ld
            leafset=verify_tree(ct['tree'],(1<<len(C))-1,q,masks,C,ld)
            assert len(leafset)==2**ld
            # Independent branch truth against actual permutation responses.
            for k in leafset:assert C[k]==tuple(C[k])
            print('TREE_PASS',n,'depth',ld,'leaves',len(leafset),flush=True)
        print('DIM_PASS',n,'concepts',len(C),'VC',vc,'Ldim',ld,'VC_nodes',nodes,'L_states',L.cache_info().currsize,flush=True)
    # Cross-check with a second enumeration using all permutations at small orders.
    for n in range(1,9):
        A=concepts(n)
        B=sorted(p for p in permutations(range(n))
                 if all(p[p[i]]==i for i in range(n)) and avoids321(p))
        assert A==B
    print('INDEPENDENT_PERMUTATION_ENUM_PASS_n1_to_n8',flush=True)
    print('INVERSION_INVOLUTIONS_EXACT_CLASSIFICATION_PASS',flush=True)
if __name__=='__main__':main()
