#!/usr/bin/env python3
"""Independent direct rank-three first-order type recursion for finite graphs."""
from itertools import combinations
from functools import lru_cache
from verify_grassmann import subspaces,rank


def grassmann(q,n,k):
    vertices=list(subspaces(n,k,q))
    adj=[[int(i!=j and rank(U+W,q)==k+1) for j,W in enumerate(vertices)] for i,U in enumerate(vertices)]
    return adj


def johnson(n,k):
    v=list(map(frozenset,combinations(range(n),k)))
    return [[int(i!=j and len(a&b)==k-1) for j,b in enumerate(v)] for i,a in enumerate(v)]


def theory(adj,r=3):
    N=len(adj)
    @lru_cache(None)
    def logical(tup,d):
        atomic=tuple((int(tup[i]==tup[j]),adj[tup[i]][tup[j]]) for i in range(len(tup)) for j in range(i+1,len(tup)))
        if d==0:return ('atomic',atomic)
        return ('extend',atomic,frozenset(logical(tup+(v,),d-1) for v in range(N)))
    result=logical((),r)
    return result,logical.cache_info()


def main():
    cases={
        'projective_line':grassmann(2,2,1),
        'johnson_complete':johnson(3,1),
        'grassmann_k2':grassmann(2,4,2),
        'johnson_k2':johnson(6,2),
        'johnson_k3':johnson(7,3),
    }
    sig={}
    for name,graph in cases.items():
        t,stats=theory(graph)
        sig[name]=t
        print(f'DIRECT_RANK3_OK model={name} vertices={len(graph)} cached_types={stats.currsize}')
    assert sig['projective_line']==sig['johnson_complete']
    assert sig['grassmann_k2']==sig['johnson_k2']
    assert len({sig['projective_line'],sig['grassmann_k2'],sig['johnson_k3']})==3
    print('CROSS_FAMILY_LOGIC_OK complete_and_k2_equivalences=true three_distinct_types=true')
    print('DIRECT_VERIFY_OK')

if __name__=='__main__':main()
