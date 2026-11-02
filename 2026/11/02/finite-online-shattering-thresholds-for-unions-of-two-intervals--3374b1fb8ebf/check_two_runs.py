#!/usr/bin/env python3
"""Exact finite Littlestone tests for binary words with at most two one-runs.
Concepts are subsets of [n] whose characteristic word has <=2 maximal 1-blocks.
No external dependencies. Use --full for n=1,...,14; without --full checks n=1,...,8.
Optional --certificate PATH to independently replay an explicit adaptive tree.
"""
from functools import lru_cache
import json, math, sys, argparse

def hypothesis_masks(n):
    return [s for s in range(1 << n) if (s & ~(s << 1) & ((1 << n)-1)).bit_count() <= 2]

def make_queries(H, n):
    return [sum(1 << j for j, s in enumerate(H) if (s >> p) & 1) for p in range(n)]

def exact_tree(n, depth, want_tree=False):
    H = hypothesis_masks(n)
    N = len(H)
    query = make_queries(H, n)
    FULL = (1 << N) - 1
    # Exact recurrence C(S,d): exists a complete depth-d shattered tree.
    # Base d=0 iff S nonempty. At d>0 both query fibres must satisfy C(S_b,d-1).
    @lru_cache(None)
    def C(S, d):
        if d == 0:
            return bool(S)
        if S.bit_count() < (1 << d):
            return False
        for Q in query:
            S1 = S & Q
            S0 = S & ~Q
            if S0 and S1 and C(S0,d-1) and C(S1,d-1):
                return True
        return False
    low = C(FULL, depth)
    high = C(FULL, depth+1)
    witness = None
    if want_tree and low and not high:
        def build(S,d):
            if d == 0:
                j = (S & -S).bit_length() - 1
                return {"witness": H[j]}
            for p,Q in enumerate(query):
                S1 = S & Q; S0 = S & ~Q
                if S0 and S1 and C(S0,d-1) and C(S1,d-1):
                    return {"query":p,"zero":build(S0,d-1),"one":build(S1,d-1)}
            raise AssertionError('cannot reconstruct')
        witness = build(FULL, depth)
    return N,low,high,C.cache_info().currsize,witness

def replay_tree(n, depth, tree):
    H = set(hypothesis_masks(n))
    nodes=0; leaves=[]
    def visit(node, constraints):
        nonlocal nodes
        if 'witness' in node:
            assert len(constraints) == depth, constraints
            s=node['witness']
            assert s in H
            assert all(((s >> p) & 1) == b for p,b in constraints)
            leaves.append(s)
            return
        assert set(node)=={'query','zero','one'}
        p=node['query'];assert type(p)==int and 0<=p<n
        assert len(constraints)<depth
        nodes+=1
        visit(node['zero'],constraints+[(p,0)])
        visit(node['one'],constraints+[(p,1)])
    visit(tree,[])
    assert nodes == 2**depth-1 and len(leaves) == 2**depth and len(set(leaves))==len(leaves)
    return nodes,len(leaves)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--full',action='store_true')
    ap.add_argument('--certificate')
    args=ap.parse_args()
    depths = [1,2,3,4,4,5,5,6,6,7,7,8,8,9]
    upto=14 if args.full else 8
    for n in range(1,upto+1):
        N,lo,hi,states,_=exact_tree(n,depths[n-1])
        assert lo and not hi,(n,N,lo,hi)
        formula=1+math.comb(n+1,2)+(math.comb(n+1,4) if n>=3 else 0)
        assert N == formula, (n,N,formula)
        print('EXACT',n,'concepts',N,'ldim',depths[n-1],'states',states,flush=True)
    assert (1+math.comb(8,2)+math.comb(8,4))==99
    if args.certificate:
        data=json.load(open(args.certificate,encoding='utf-8'))
        assert (data['n'],data['depth']) in ((7,5),(14,9))
        print('CERTIFICATE',data['n'],*replay_tree(data['n'],data['depth'],data['tree']))
    print('TWO_INTERVALS_CHECKS_PASS', upto)

if __name__=='__main__':main()
