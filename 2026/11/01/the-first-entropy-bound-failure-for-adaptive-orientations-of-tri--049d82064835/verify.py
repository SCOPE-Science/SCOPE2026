"""Exact online-shattering check for acyclic edge orientations of triangular books.
Stdlib Python 3.10+. Run as: python verify.py CERTIFICATE.json
"""
import json
import sys
from functools import lru_cache

def states(r):
    # Coordinates: central edge (0,1), then pairs (0,i), (1,i), i=2,...,r+1.
    # Bit 0 sends lower-label endpoint to higher-label endpoint; bit 1 reverses.
    result=[]
    for s in (0,1):
        allowed=[(a,b) for a in (0,1) for b in (0,1)
                 if (a,b) != ((1,0) if s==0 else (0,1))]
        def recurse(x,j):
            if j==r:
                result.append(x)
                return
            for a,b in allowed:
                recurse(x | (a << (2*j+1)) | (b << (2*j+2)),j+1)
        recurse(s,0)
    return sorted(result)

def is_acyclic_by_topological_removal(bits,r):
    n=r+2
    edges=[(0,1)]+[(v,j) for j in range(2,n) for v in (0,1)]
    incoming=[0]*n
    for e,(u,v) in enumerate(edges):
        if bits>>e &1:
            u,v=v,u
        incoming[v] |= 1<<u
    remaining=(1<<n)-1
    while remaining:
        source=next((v for v in range(n) if (remaining>>v)&1 and incoming[v]&remaining==0),None)
        if source is None:return False
        remaining ^= 1<<source
    return True

def exact_depth(r):
    concepts=states(r)
    assert len(concepts)==2*3**r
    assert all(is_acyclic_by_topological_removal(x,r) for x in concepts)
    m=2*r+1
    support=[sum(1<<i for i,c in enumerate(concepts) if c>>q&1) for q in range(m)]
    U=(1<<len(concepts))-1
    @lru_cache(None)
    def possible(mask,d):
        if d==0:return bool(mask)
        if mask.bit_count() < (1<<d):return False
        for Q in support:
            one=mask&Q
            zero=mask^one
            if one and zero and possible(zero,d-1) and possible(one,d-1):
                return True
        return False
    dimension=0
    while dimension+1<=len(concepts).bit_length()-1 and possible(U,dimension+1):
        dimension+=1
    assert not possible(U,dimension+1)
    return dimension,possible.cache_info().currsize

def verify_tree(tree, r, depth, history, names):
    if len(history)==depth:
        assert set(tree)=={'witness'}
        w=tree['witness']
        assert isinstance(w,str) and len(w)==2*r+1 and set(w)<=set('01')
        bits=sum(int(v)<<i for i,v in enumerate(w))
        assert is_acyclic_by_topological_removal(bits,r)
        assert all(((bits>>i)&1)==b for i,b in history)
        names.append(w)
        return
    assert set(tree)=={'edge','zero','one'}
    q=tree['edge']
    assert type(q)==int and 0<=q<=2*r
    assert q not in [i for i,b in history]
    verify_tree(tree['zero'],r,depth,history+[(q,0)],names)
    verify_tree(tree['one'],r,depth,history+[(q,1)],names)

def main(path):
    expected=[2,4,5,7,8,10,11]
    stats=[]
    for r,expect in enumerate(expected,1):
        actual,states_count=exact_depth(r)
        assert actual==expect,(r,actual,expect)
        # VC dimension is r+1 by the independently established forest criterion.
        # Count and entropy comparator are checked as machine arithmetic.
        upper=(2*3**r).bit_length()-1
        assert (actual==upper)==(r<=6)
        stats.append((r,actual,states_count,upper))
    with open(path,encoding='utf8') as fp: certificate=json.load(fp)
    assert len(certificate['instances'])==7
    total_leaves=0
    for r,instance in enumerate(certificate['instances'],1):
        assert instance['r']==r
        assert instance['depth']==expected[r-1]
        assert instance['edge_order']==[[0,1]]+[[v,i] for i in range(2,r+2) for v in (0,1)]
        witnessed=[]
        verify_tree(instance['tree'],r,expected[r-1],[],witnessed)
        assert len(witnessed)==(1<<expected[r-1])
        assert len(set(witnessed))==len(witnessed)
        total_leaves+=len(witnessed)
    print('TRIANGULAR_BOOK_EXACT_DEPTHS_PASS',stats)
    print('TRIANGULAR_BOOK_TREES_PASS',7,total_leaves,total_leaves-7)
    print('FIRST_ENTROPY_BOUND_FAILURE_PASS r=7 depth=11 bound=12')

if __name__=='__main__':
    assert len(sys.argv)==2
    main(sys.argv[1])
