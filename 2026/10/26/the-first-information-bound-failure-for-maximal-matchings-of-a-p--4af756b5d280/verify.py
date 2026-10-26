#!/usr/bin/env python3
"""Standalone exhaustive verifier for finite maximal matchings on paths.
Only ordinary finite set operations are used; no nonstandard libraries.
"""
from functools import lru_cache
import json

def maximal_matchings(m):
    # Edge i and i+1 are incident on a path with m edges.
    ans=[]
    for bits in range(1<<m):
        if bits & (bits<<1):
            continue
        if all((bits >> i)&1 or (i>0 and (bits>>(i-1))&1) or
               (i+1<m and (bits>>(i+1))&1) for i in range(m)):
            ans.append(bits)
    return ans

def game(masks,m):
    queries=[]
    for i in range(m):
        queries.append(sum(1<<j for j,v in enumerate(masks) if (v>>i)&1))
    @lru_cache(None)
    def L(s):
        best=0
        for i,Q in enumerate(queries):
            a=s&Q;b=s&~Q
            if a and b:
                best=max(best,1+min(L(a),L(b)))
        return best
    full=(1<<len(masks))-1
    dim=L(full)
    def tree(s,d):
        if d==0:
            witness=next(j for j in range(len(masks)) if s>>j&1)
            return {'witness':masks[witness]}
        for i,Q in enumerate(queries):
            a=s&Q;b=s&~Q
            if a and b and L(a)>=d-1 and L(b)>=d-1:
                return {'query':i+1,'zero':tree(b,d-1),'one':tree(a,d-1)}
        raise AssertionError('shattering witness missing')
    return queries,dim,L.cache_info().currsize,tree(full,dim)

def independently_check_tree(tree,masks,m):
    def rec(t,cands):
        if 'witness' in t:
            assert t['witness'] in cands
            return 0
        q=t['query']-1
        assert 0<=q<m
        a={v for v in cands if v>>q&1}
        b={v for v in cands if not (v>>q&1)}
        assert a and b
        za=rec(t['zero'],b)
        oa=rec(t['one'],a)
        assert za==oa
        return 1+za
    return rec(tree,set(masks))

def main():
    rows=[]; trees={}
    for m in range(0,16):
        masks=maximal_matchings(m)
        queries,dim,states,tr=game(masks,m)
        upper=len(masks).bit_length()-1
        assert dim==upper if m<=14 else dim==5
        assert independently_check_tree(tr,masks,m)==dim
        rows.append({'edges':m,'hypotheses':len(masks),'information_bound':upper,
                     'littlestone_dimension':dim,'memo_states':states})
        trees[str(m)]=tr
    m=15; masks=maximal_matchings(m); queries,dim,_,_=game(masks,m)
    F=(1<<len(masks))-1
    n=len(masks)
    root_candidates=[i+1 for i,Q in enumerate(queries) if min((F&Q).bit_count(),(F&~Q).bit_count())>=32]
    assert root_candidates==[4,12]
    witness={}
    for root,other in [(4,12),(12,4)]:
        N=F&~queries[root-1]
        candidates=[(i+1, (N&Q).bit_count(), (N&~Q).bit_count()) for i,Q in enumerate(queries)
                    if min((N&Q).bit_count(),(N&~Q).bit_count())>=16]
        assert candidates==[(other,16,17)]
        seventeen=N&~queries[other-1]
        assert seventeen.bit_count()==17
        next_candidates=[(i+1,(seventeen&Q).bit_count(),(seventeen&~Q).bit_count())
                         for i,Q in enumerate(queries)
                         if min((seventeen&Q).bit_count(),(seventeen&~Q).bit_count())>=8]
        assert next_candidates==[(8,9,8)]
        nine=seventeen&queries[7]; eight=seventeen&~queries[7]
        assert (nine.bit_count(),eight.bit_count())==(9,8)
        maxima={str(v.bit_count()):max(min((v&Q).bit_count(),(v&~Q).bit_count()) for Q in queries)
                for v in (nine,eight)}
        assert maxima=={'9':3,'8':3}
        witness[str(root)]={'negative_count':N.bit_count(), 'next_query_candidates':candidates,
                            'seventeen_size':seventeen.bit_count(),'third_query_candidates':next_candidates,
                            'last_branch_max_smaller_side':maxima}
    print('EXACT_PROFILE',json.dumps(rows,separators=(',',':')))
    print('DEPTH_SIX_OBSTRUCTION',json.dumps(witness,sort_keys=True,separators=(',',':')))
    with open('shattered_trees.json','w',encoding='utf-8') as f:
        json.dump(trees,f,separators=(',',':'),sort_keys=True)
        f.write('\n')
    print('CERTIFICATES',len(trees),'validated')
    print('ALL_CHECKS_PASS')
if __name__=='__main__':main()
