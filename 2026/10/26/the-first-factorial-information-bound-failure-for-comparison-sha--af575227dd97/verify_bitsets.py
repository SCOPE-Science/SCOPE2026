"""Exact Littlestone dimensions for comparison concepts on S_n, 1 <= n <= 7.

Usage: python verify_bitsets.py comparison_certificates.json

This implementation uses lexicographically indexed permutations as finite hypotheses.
It verifies explicit complete binary shattered-tree certificates and independently
rules out depth 12 on seven labels via exhaustive memoized splitting.
"""
import itertools
import json
import math
import sys
from functools import lru_cache


def universe(n):
    perms = list(itertools.permutations(range(n)))
    pairs = list(itertools.combinations(range(n), 2))
    masks = []
    for a,b in pairs:
        mask = 0
        for index,p in enumerate(perms):
            if p.index(a)<p.index(b):mask |= 1<<index
        masks.append(mask)
    return perms, pairs, masks


def solve(n):
    perms,pairs,masks=universe(n)
    full=(1<<len(perms))-1
    @lru_cache(None)
    def has_depth(state, depth):
        if depth==0: return True
        if state.bit_count() < (1<<depth):return False
        for m in masks:
            yes=state&m; no=state&~m
            if yes.bit_count() < (1<<(depth-1)) or no.bit_count() < (1<<(depth-1)):
                continue
            if has_depth(no,depth-1) and has_depth(yes,depth-1):return True
        return False
    max_depth=math.factorial(n).bit_length()-1
    dim=next((d for d in range(max_depth,-1,-1) if has_depth(full,d)),0)
    def positive_certificate(depth):
        nodes=[None]*((1<<depth)-1)
        leaves=[None]*(1<<depth)
        def visit(state,index,level,path):
            if level==0:
                assert state
                leaves[path]=(state&-state).bit_length()-1
                return
            for q,m in enumerate(masks):
                yes=state&m;no=state&~m
                if no.bit_count()>=(1<<(level-1)) and yes.bit_count()>=(1<<(level-1)) and has_depth(no,level-1) and has_depth(yes,level-1):
                    nodes[index]=q
                    visit(no,2*index+1,level-1,path<<1)
                    visit(yes,2*index+2,level-1,(path<<1)|1)
                    return
            raise AssertionError('No positive witness for expected depth')
        visit(full,0,depth,0)
        return {'n':n,'depth':depth,'pairs':[list(t) for t in pairs],'node_query_indices':nodes,'leaf_permutation_indices':leaves}
    return dim,positive_certificate(dim),has_depth


def verify_certificate(data):
    n=data['n']; depth=data['depth']; permutations,pairs,masks=universe(n)
    assert pairs==[tuple(p) for p in data['pairs']]
    nodes=data['node_query_indices'];leaves=data['leaf_permutation_indices']
    assert len(nodes)==(1<<depth)-1 and len(leaves)==(1<<depth)
    assert len(set(leaves))==len(leaves)
    def descend(state,index,level,path):
        if level==0:
            pi=leaves[path]; assert 0<=pi<len(permutations)
            assert (state>>pi)&1
            return
        q=nodes[index]; assert 0<=q<len(masks)
        a,b=masks[q],state
        assert state&a and state&~a
        descend(state&~a,2*index+1,level-1,path<<1)
        descend(state&a,2*index+2,level-1,(path<<1)|1)
    descend((1<<len(permutations))-1,0,depth,0)


def main():
    expected=(0,1,2,4,6,9,11)
    assert len(sys.argv)==2
    certs=json.load(open(sys.argv[1],encoding='utf8'))
    assert len(certs)==7
    for n,want in enumerate(expected,1):
        dim,cert,has_depth=solve(n)
        assert dim==want,(n,dim,want)
        assert certs[str(n)]==cert
        verify_certificate(cert)
        print(f'BITSET n={n} permutations={math.factorial(n)} ldim={dim} positive_leaves={1<<dim}')
        if n==7:
            all_perms,pairs,masks=universe(n)
            full=(1<<len(all_perms))-1
            assert not has_depth(full,12)
            for j,m in enumerate(masks):
                assert not has_depth(m,11)
                assert not has_depth(full&~m,11)
            print('BITSET n=7 depth_12_impossible=True root_branches_21x2_checked=True')
    print('BITSET_ALL_CHECKS_PASS')

if __name__=='__main__':main()
