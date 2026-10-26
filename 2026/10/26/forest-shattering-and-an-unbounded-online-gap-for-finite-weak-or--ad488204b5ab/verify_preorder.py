"""Self-contained verification of explicit shattering certificates for strict comparisons of weak orders.

Run: python verify_preorder.py adaptive_preorder_trees.json
No external dependencies. Zero means x is not strictly before y, including ties.
"""
import sys,json,itertools
from functools import lru_cache

def ordered_partitions(items):
    """Independent ordered-block recursion; produces all total preorders exactly once."""
    items=frozenset(items)
    if not items:
        yield ()
        return
    arr=sorted(items)
    for size in range(1,len(arr)+1):
        for block in itertools.combinations(arr,size):
            for rest in ordered_partitions(items.difference(block)):
                yield (block,)+rest

def rank_vectors(n):
    out=[]
    for blocks in ordered_partitions(range(n)):
        rank=[None]*n
        for i,block in enumerate(blocks):
            for v in block:rank[v]=i
        out.append(tuple(rank))
    assert len(out)==len(set(out))
    return out

def verify_tree(node,n,depth,allowed,path,seen):
    if depth==0:
        assert set(node)=={'ranks'},node
        r=tuple(node['ranks'])
        assert r in allowed and len(r)==n
        assert set(r)==set(range(max(r)+1))
        assert r not in seen,(path,r)
        seen.add(r)
        return 1,0
    assert set(node)=={'query','zero','one'},node
    i,j=node['query']
    assert type(i) is int and type(j) is int and 0<=i<n and 0<=j<n and i!=j
    no={r for r in allowed if not(r[i]<r[j])}
    yes={r for r in allowed if r[i]<r[j]}
    assert no and yes and not(no & yes) and no|yes==allowed
    leaves0,internal0=verify_tree(node['zero'],n,depth-1,no,path+'0',seen)
    leaves1,internal1=verify_tree(node['one'],n,depth-1,yes,path+'1',seen)
    return leaves0+leaves1,1+internal0+internal1

def exact_littlestone(orders):
    n=len(orders[0]); q=[(i,j) for i in range(n) for j in range(n) if i!=j]
    pos=[sum(1<<h for h,p in enumerate(orders) if p[i]<p[j]) for i,j in q]
    full=(1<<len(orders))-1
    @lru_cache(None)
    def rec(s):
        if s.bit_count()<=1:return 0
        best=0
        for mask in pos:
            yes=s&mask;no=s&~mask
            if yes and no:best=max(best,1+min(rec(yes),rec(no)))
        return best
    result=rec(full)
    return result,rec.cache_info().currsize

def exact_vc(orders):
    n=len(orders[0]); q=[(i,j) for i in range(n) for j in range(n) if i!=j]
    hm=[]
    for i,j in q:
        hm.append(sum(1<<h for h,p in enumerate(orders) if p[i]<p[j]))
    full=(1<<len(orders))-1
    max_d=0
    for d in range(1,len(q)+1):
        ok=False
        for chosen in itertools.combinations(hm,d):
            masks=[full]
            for m in chosen:
                masks=[s&~m for s in masks]+[s&m for s in masks]
                if 0 in masks:break
            if len(masks)==1<<d and all(masks):
                ok=True;break
        if not ok:return max_d
        max_d=d
    return max_d

def main(path):
    with open(path,encoding='utf-8') as fh:doc=json.load(fh)
    assert set(doc)=={'certificates'}
    assert [(c['n'],c['depth']) for c in doc['certificates']]==[(3,3),(4,5)]
    byn={1:0,2:1}
    for n in (1,2,3,4):
        orders=rank_vectors(n)
        expected={1:1,2:3,3:13,4:75}[n]
        assert len(orders)==expected
        vc=exact_vc(orders)
        ld,states=exact_littlestone(orders)
        assert vc==n-1,(n,vc)
        assert ld=={1:0,2:1,3:3,4:5}[n],(n,ld)
        if n>=3:
            cert=doc['certificates'][n-3]
            assert set(cert)=={'n','depth','tree'}
            seen=set()
            leaves,internal=verify_tree(cert['tree'],n,ld,set(orders),'',seen)
            assert leaves==2**ld and internal==2**ld-1 and len(seen)==leaves
            print(f'n={n} orders={len(orders)} vc={vc} ldim={ld} states={states} leaves={leaves} internal={internal}')
        else:
            print(f'n={n} orders={len(orders)} vc={vc} ldim={ld} states={states}')
        if n==4:
            lt=sum(o[0]<o[1] for o in orders)
            eq=sum(o[0]==o[1] for o in orders)
            assert (lt,eq)==(31,13)
            print('n=4 root strict-positive hypotheses=31, fewer than 32 required for depth-5 subtree')
    print('ALL_WEAK_ORDER_CHECKS_PASS')
if __name__=='__main__':
    assert len(sys.argv)==2,'usage: verify_preorder.py certificate.json'
    main(sys.argv[1])
