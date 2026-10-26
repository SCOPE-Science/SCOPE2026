#!/usr/bin/env python3
"""Exact rank-three finite-structure checks for Kneser graphs, pure adjacency."""
from itertools import combinations
from math import comb


def graph(n, k):
    verts = [sum(1 << i for i in v) for v in combinations(range(n), k)]
    return [sum(1 << j for j, b in enumerate(verts) if i != j and a & b == 0)
            for i, a in enumerate(verts)]


def predicted(n, k):
    if n < 2*k:
        return 'isolated-one' if n == k else 'isolated-many'
    if n == 2*k:
        return 'edge-one' if k == 1 else 'matching-many'
    if k == 1:
        return 'clique-many'
    if n >= 3*k:
        return 'triangular-kneser'
    if n == 3*k-1:
        return 'triangle-free-full-codegree'
    return 'triangle-free-mixed-codegree'


def atomic3(a,b,c,adj):
    return (int(a==b),int(a==c),int(b==c),
            int(bool(adj[a] >> b & 1)),int(bool(adj[a] >> c & 1)),
            int(bool(adj[b] >> c & 1)))


def exact_rank_three(adj):
    """Independent ordinary FO finite type recursion on ordered tuples.
    q=0 is the complete atomic diagram; each successor type adds the set
    of types of extensions by one variable, including repeated vertices.
    """
    N=len(adj)
    pair_types = [[(int(a==b),int(bool(adj[a]>>b&1)),
                  tuple(sorted({atomic3(a,b,c,adj) for c in range(N)})))
                   for b in range(N)] for a in range(N)]
    pointed_types = [frozenset(pair_types[a]) for a in range(N)]
    return frozenset(pointed_types)


def observed_features(adj):
    """Independently compute explicit first-order sentences of rank <=3."""
    N=len(adj)
    edge=any(adj)
    nonedge=any(a!=b and not (adj[a] >> b & 1)
                for a in range(N) for b in range(N))
    deg2=any(x.bit_count()>=2 for x in adj)
    triangle=any((adj[a] & adj[b]) != 0 for a in range(N)
                 for b in range(a+1,N) if adj[a] >> b & 1)
    nonadj_common=any((adj[a] & adj[b]) != 0 for a in range(N)
                       for b in range(a+1,N) if not (adj[a]>>b&1))
    nonadj_zero=any((adj[a] & adj[b]) == 0 for a in range(N)
                       for b in range(a+1,N) if not (adj[a]>>b&1))
    return (N>=2, N>=3, edge, nonedge, deg2, triangle,
            nonadj_common, nonadj_zero)


def main():
    reps={'isolated-one':(1,1), 'isolated-many':(3,2),
          'edge-one':(2,1), 'matching-many':(4,2),
          'clique-many':(3,1), 'triangular-kneser':(6,2),
          'triangle-free-full-codegree':(5,2),
          'triangle-free-mixed-codegree':(7,3)}
    assert len(reps)==8
    types = {}
    features = {}
    for cl,(n,k) in reps.items():
        adj=graph(n,k)
        assert predicted(n,k)==cl
        types[cl]=exact_rank_three(adj)
        features[cl]=observed_features(adj)
    assert len(set(types.values())) == 8, 'representatives not pairwise distinguishable'
    assert len(set(features.values())) == 8, 'explicit rank-3 profiles fail to distinguish'
    tests=0
    byclass={}
    sample_max=0
    for k in range(1,6):
        for n in range(k,3*k+4):
            order=comb(n,k)
            if order>130:
                continue
            adj=graph(n,k)
            label=predicted(n,k)
            typ=exact_rank_three(adj)
            f=observed_features(adj)
            assert typ==types[label], (n,k,'rank-3 mismatch')
            assert f==features[label], (n,k,'formula mismatch')
            byclass.setdefault(label,[]).append((n,k,order))
            sample_max=max(order,sample_max)
            tests+=1
    assert len(byclass)==8, byclass.keys()
    assert max(comb(*v) for v in reps.values())==35
    print('EXACT_TYPE_OK classes=8 representative_max=35 samples=%d maximal_sample_order=%d'%(tests,sample_max))
    print('FEATURE_ORACLE_OK distinguishing_rank_three_sentences=8')
    for cl,pars in reps.items():
        print(cl, 'representative',pars,'order',comb(*pars),
              'feature_bits',''.join(map(str,map(int,features[cl]))),
              'tested',len(byclass[cl]))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
