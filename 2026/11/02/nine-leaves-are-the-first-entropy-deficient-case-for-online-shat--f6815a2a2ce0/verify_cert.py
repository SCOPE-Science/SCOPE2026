"""Reproduce pair-path certificates and independent online-rank calculations.
No network or non-standard modules required. Run from the directory containing certificates.json.
"""
import json
from pathlib import Path
from functools import lru_cache
from collections import deque
from itertools import combinations
from math import comb

def independent_path(G,a,b):
    queue=deque([(a,[a])]);seen={a}
    while queue:
        x,path=queue.popleft()
        if x==b:return frozenset(path)
        for y in G[x]:
            if y not in seen:seen.add(y);queue.append((y,path+[y]))
    raise AssertionError('Disconnected')

def rank_by_frozensets(C,vertices):
    @lru_cache(None)
    def go(sub):
        if len(sub)<2:return 0
        val=0
        for v in vertices:
            A=frozenset(i for i in sub if v in C[i]);B=sub-A
            if A and B:
                val=max(val,1+min(go(A),go(B)))
        return val
    return go(frozenset(range(len(C))))

def test():
    data=json.loads(Path(__file__).with_name('certificates.json').read_text())
    assert [x['m'] for x in data]==list(range(2,11))
    expected={2:0,3:1,4:2,5:3,6:3,7:4,8:4,9:4,10:5}
    for row in data:
        m=row['m'];G=row['adjacency'];n=len(G)
        for i,neighbors in enumerate(G):
            assert len(set(neighbors))==len(neighbors)
            for j in neighbors:assert i in G[j] and i!=j
        assert sum(map(len,G))==2*(n-1)
        leaves=[v for v in range(n) if len(G[v])==1]
        assert len(leaves)==m
        pairs=list(combinations(leaves,2))
        C=[independent_path(G,a,b) for a,b in pairs]
        assert len(C)==comb(m,2)==row['concept_count']
        assert len(set(C))==len(C)
        assert row['rank']==expected[m]
        used=[];nodes=0
        def visit(node,steps):
            nonlocal nodes
            if 'pair' in node:
                p=tuple(node['pair'])
                assert p in pairs
                concepts=C[pairs.index(p)]
                assert all((v in concepts)==bool(bit) for v,bit in steps)
                used.append(p)
                return
            nodes+=1
            v=node['query']
            assert isinstance(v,int) and 0<=v<n
            visit(node['0'],steps+[(v,0)])
            visit(node['1'],steps+[(v,1)])
        visit(row['shattered_tree'],[])
        assert len(used)==len(set(used))==2**row['rank']
        assert nodes==2**row['rank']-1
        # Independent recurrence also verifies that no deeper tree exists on each concrete example.
        if m<=10: assert rank_by_frozensets(C,range(n))==expected[m]
        print('CERTIFICATE_AND_INDEPENDENT_RANK_PASS',m,'rank',row['rank'],'leaves',len(used),'queries',nodes)
    # Enumerate integer partitions of nine with positive parts. Candidate first queries
    # with both branch cardinalities >=16 have only the types below.
    candidates=set()
    def parts(n,minval=1):
        if n==0:
            yield ()
            return
        for i in range(minval,n+1):
            for rest in parts(n-i,i):yield(i,)+rest
    for p in parts(9):
        if len(p)<2:continue
        neg=sum(comb(i,2) for i in p)
        pos=comb(9,2)-neg
        if min(neg,pos)>=16:candidates.add((p,pos,neg))
    assert candidates=={((3,6),18,18),((4,5),20,16),((1,2,6),20,16)},candidates
    print('NINE_LEAF_FIRST_QUERY_EXHAUSTIVE_SPLITS_PASS',sorted(candidates))
    print('ALL_LEAF_PAIR_SHATTERING_CHECKS_PASS')
if __name__=='__main__':test()
