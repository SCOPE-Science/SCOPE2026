#!/usr/bin/env python3
"""Finite face-incidence traces and adaptive-tree replay; standard library only."""
import json
from itertools import combinations, product
from functools import lru_cache
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent

def coordinate_faces(d,k):
    out=[]
    for free_tpl in combinations(range(d),k):
        free=set(free_tpl)
        fixed=tuple(i for i in range(d) if i not in free)
        for bits in product((0,1),repeat=len(fixed)):
            mask=0
            for x in range(1<<d):
                if all((x>>i)&1==b for i,b in zip(fixed,bits)):
                    mask|=1<<x
            out.append(mask)
    assert len(out)==comb(d,k)*2**(d-k) and len(set(out))==len(out)
    return out

def trace_set(rows,queries):
    return {sum(((face>>x)&1)<<j for j,x in enumerate(queries)) for face in rows}

def shattered(rows,queries):
    return len(trace_set(rows,queries))==(1<<len(queries))

def rank_witness(rows,d,depth):
    """Find a full tree of prescribed depth by finite exact version-space search."""
    at_query=[sum(1<<j for j,face in enumerate(rows) if (face>>q)&1)
              for q in range(1<<d)]
    whole=(1<<len(rows))-1
    @lru_cache(None)
    def rec(version,remaining):
        if remaining==0:
            first=(version&-version).bit_length()-1
            return {'h':first}
        if version.bit_count()<(1<<remaining):return None
        for q,positives in enumerate(at_query):
            yes=version&positives
            no=version&(whole^positives)
            if min(yes.bit_count(),no.bit_count())<(1<<(remaining-1)):
                continue
            a=rec(yes,remaining-1)
            if a is None: continue
            b=rec(no,remaining-1)
            if b is not None:
                return {'q':q,'yes':a,'no':b}
        return None
    tree=rec(whole,depth)
    return tree,rec.cache_info().currsize

def replay(rows,tree,depth):
    leaves=[];nodes=[]
    def go(t,version,h):
        if h==0:
            assert set(t)=={'h'} and t['h'] in version
            leaves.append(t['h'])
            return
        assert set(t)=={'q','yes','no'}
        q=t['q'];nodes.append(q)
        assert isinstance(q,int) and q>=0
        pos=[i for i in version if (rows[i]>>q)&1]
        neg=[i for i in version if not ((rows[i]>>q)&1)]
        assert pos and neg
        go(t['yes'],pos,h-1);go(t['no'],neg,h-1)
    go(tree,list(range(len(rows))),depth)
    assert len(nodes)==(1<<depth)-1
    assert len(leaves)==len(set(leaves))==(1<<depth)
    return len(nodes),len(leaves)

def main():
    for d,k,expected in [(4,3,64),(5,3,320)]:
        rows=coordinate_faces(d,k)
        total=sum(shattered(rows,S) for S in combinations(range(1<<d),k))
        assert total==expected==2**d*comb(d,k)
        print(f'EXHAUSTIVE_MAX_SUPPORT_CENSUS_PASS d={d} k={k} supports={total}')
    for d,k in [(4,3),(5,3),(6,4),(7,4),(8,5)]:
        rows=coordinate_faces(d,k)
        S=[1<<i for i in range(k)]
        assert shattered(rows,S)
        assert len(trace_set(rows,S))==2**k
        print(f'UNIT_VECTOR_TRACE_PASS d={d} k={k} patterns={2**k}')
    for d,k in [(5,3),(7,4),(9,5)]:
        rows=coordinate_faces(d,k)
        throughzero=[f for f in rows if f&1]
        tree,states=rank_witness(throughzero,d,k)
        assert tree is not None
        replay(throughzero,tree,k)
        opposite=[f for f in rows if all(not ((f>>x)&1) for x in range(0,1<<d,2))]
        support=[1|(1<<i) for i in range(1,k+1)]
        assert shattered(opposite,support)
        print(f'ONLINE_TWO_BRANCH_WITNESS_PASS d={d} k={k} positive_states={states}')
    rows=coordinate_faces(5,3)
    payload=json.loads((HERE/'certificate.json').read_text(encoding='utf-8'))
    assert payload['d']==5 and payload['k']==3 and payload['depth']==4
    nleaf=replay(rows,payload['tree'],4)
    fresh,_=rank_witness(rows,5,4)
    assert fresh==payload['tree']
    print(f'DEPTH_FOUR_CERTIFICATE_PASS internal={nleaf[0]} leaves={nleaf[1]}')
    assert len(coordinate_faces(3,3))==1
    assert len(coordinate_faces(4,3))==8
    print('ALL_FIXED_FACE_SHATTERING_CHECKS_PASS')

if __name__=='__main__':main()
