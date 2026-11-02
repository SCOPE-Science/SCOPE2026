#!/usr/bin/env python3
"""Exact noncounting FO2 census of distributive ideal lattices J(P), |P|<=7.
Requires Python 3 and networkx for independent graph-isomorphism decisions.
No randomization; positional masks encode strict transitive order on P.
"""
from collections import defaultdict
import networkx as nx


def ideals(less):
    n=len(less)
    lower=[sum(1<<j for j in range(n) if less[j]>>i&1) for i in range(n)]
    return tuple(s for s in range(1<<n) if all(not(s>>i&1) or (s&lower[i])==lower[i] for i in range(n)))


def extensions(less):
    n=len(less)
    for down in ideals(less):
        yield tuple(v|((1<<n) if down>>i&1 else 0) for i,v in enumerate(less))+(0,)


def graph_and_key(less,ideal_count):
    n=len(less)
    out=[v.bit_count() for v in less]
    indeg=[sum(less[j]>>i&1 for j in range(n)) for i in range(n)]
    g=nx.DiGraph()
    g.add_nodes_from(range(n))
    g.add_edges_from((i,j) for i in range(n) for j in range(n) if less[i]>>j&1)
    return g,(tuple(sorted(zip(indeg,out))),ideal_count)


def representatives(bound):
    levels=[[()]]
    for n in range(1,bound+1):
        buckets=defaultdict(list);res=[]
        for old in levels[-1]:
            for poset in extensions(old):
                g,key=graph_and_key(poset,len(ideals(poset)))
                if all(not nx.is_isomorphic(g,other) for other in buckets[key]):
                    buckets[key].append(g)
                    res.append(poset)
        levels.append(res)
        print('poset_order',n,'isomorphism_classes',len(res),flush=True)
    return levels


def fo2_ranks(lattices,rank_cap=6):
    rel=[];indices=[]
    for k,D in enumerate(lattices):
        rel.append([[0 if a==b else 1 if a&b==a else 2 if a&b==b else 3 for b in D]for a in D])
        indices.extend((k,i) for i in range(len(D)))
    colors={idx:0 for idx in indices}
    ranks=[];collisions_by_rank=[]
    for t in range(rank_cap):
        if t:
            local=[]
            for k,D in enumerate(lattices):
                for i in range(len(D)):
                    local.append(frozenset((rel[k][i][j],colors[k,j])for j in range(len(D))))
            coding={v:i for i,v in enumerate(sorted(set(local),key=lambda s:tuple(sorted(s))))}
            colors={idx:coding[local[z]] for z,idx in enumerate(indices)}
        profiles=[frozenset(colors[k,i] for i in range(len(D))) for k,D in enumerate(lattices)]
        partition=defaultdict(list)
        for k,profile in enumerate(profiles):partition[profile].append(k)
        collisions=[members for members in partition.values()if len(members)>1]
        ranks.append(len(partition));collisions_by_rank.append(collisions)
        print('sentence_rank',t+1,'FO2_classes',len(partition),'colliding_classes',len(collisions),flush=True)
    return ranks,collisions_by_rank


def run():
    levels=representatives(7)
    expected=(1,1,2,5,16,63,318,2045)
    assert tuple(map(len,levels))==expected
    record=[(n,p,ideals(p)) for n,seq in enumerate(levels) for p in seq]
    ranks,collision=fo2_ranks([d for _,_,d in record])
    assert ranks==[1,5,78,789,2449,2451],ranks
    assert len(collision[4])==2 and all(len(g)==2 for g in collision[4])
    assert collision[5]==[]
    for i,group in enumerate(collision[4]):
        print('rank5_exception',i+1,[(record[k][0],len(record[k][2]),record[k][1])for k in group])
    print('PASS 2451 nonisomorphic finite distributive lattices have distinct FO2 theories by rank six')
    return record

if __name__=='__main__':run()
