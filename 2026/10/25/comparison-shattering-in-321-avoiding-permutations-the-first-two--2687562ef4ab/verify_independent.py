"""Independent enumeration, exact depth feasibility, and external tree-certificate verification."""
import json,math
from functools import lru_cache
from itertools import combinations
from pathlib import Path
BASE=Path(__file__).resolve().parent

def avoid321(p):
    n=len(p)
    # Every right-to-left seen minimum is used to reject a two-step descent.
    for i in range(n):
        for j in range(i+1,n):
            if p[i]>p[j] and any(p[j]>p[k] for k in range(j+1,n)):
                return False
    return True

def by_insertion(n):
    arr=[()]
    for k in range(1,n+1):
        cand=[]
        for p in arr:
            for j in range(k):
                q=p[:j]+(k,)+p[j:]
                if avoid321(q):cand.append(q)
        arr=sorted(cand)
        assert len(set(arr))==len(arr)
    return arr

def calc(n):
    p=by_insertion(n)
    full=(1<<len(p))-1
    masks=[]
    for i,j in combinations(range(n),2):
        masks.append(sum((1<<t) for t,x in enumerate(p) if x[i]<x[j]))
    @lru_cache(None)
    def yes(s,k):
        if k==0:return bool(s)
        if s.bit_count()<1<<k:return False
        for m in masks:
            a=s&m;b=s&(~m)&full
            if a and b and yes(a,k-1) and yes(b,k-1):return True
        return False
    answer=0
    for d in range(1,len(p).bit_length()):
        if yes(full,d):answer=d
        else:break
    return len(p),answer,yes.cache_info().currsize

def certificate():
    data=json.loads((BASE/'tree_depth9.json').read_text('utf-8'))
    assert data['schema_version']==1 and data['n']==8 and data['depth']==9
    q=data['queries_heap_one_indexed']; leaves=data['leaf_witnesses_left_to_right']
    assert len(q)==511 and len(leaves)==512
    allp=set(by_insertion(8))
    assert len(allp)==1430
    assert len({tuple(p) for p in leaves})==512
    for offset,leaf in enumerate(leaves):
        p=tuple(leaf)
        assert p in allp,('not valid',offset,p)
        node=1
        for level in range(9):
            i,j=q[node-1]
            assert 0<=i<j<8
            bit=int(p[i]<p[j])
            want=(offset>>(8-level))&1
            assert bit==want,('bad path',offset,level)
            node=2*node+bit
        assert node==512+offset
    print('CERTIFICATE_VERIFIED 512 distinct 321-avoiding leaf witnesses, 511 query nodes')

def main():
    expected=[(1,1,0),(2,2,1),(3,5,2),(4,14,3),(5,42,4),(6,132,6),(7,429,7),(8,1430,9)]
    for n,N,d in expected:
        a,b,states=calc(n)
        assert (a,b)==(N,d),(n,a,b,N,d)
        print('INDEPENDENT_DIM',n,a,b,'states',states,flush=True)
    certificate()
    print('ALL_321_AVOIDING_CHECKS_PASS')
if __name__=='__main__':main()
