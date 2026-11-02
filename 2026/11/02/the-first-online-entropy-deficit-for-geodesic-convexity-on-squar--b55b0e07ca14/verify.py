"""Independent executable checks for finite interval/parity-geodesic concept classes.
The finite online recurrence exhausts every vertex query at each reachable version space.
Python 3.9+; no external packages or data files.
"""
from functools import lru_cache
from itertools import combinations
from collections import deque
from math import comb, floor, log2
import json


def candidate_concepts(n):
    out = {0}
    for a in range(n):
        for b in range(a,n):
            out.add(sum(1 << x for x in range(a,b+1)))
        for b in range(a+2,n,2):
            out.add(sum(1 << x for x in range(a,b+1,2)))
    return tuple(sorted(out))


def expected_count(n):
    m=n//2
    return 3*m*m+1 if n%2==0 else 3*m*m+3*m+2


def expected_triples(n):
    return n*(n*n-4)//24 if n%2==0 else n*(n*n-1)//24


def graph_convex_concepts(n):
    graph=[[j for j in range(n) if j!=i and abs(i-j)<=2] for i in range(n)]
    dist=[]
    for start in range(n):
        d=[n+1]*n;d[start]=0
        q=deque([start])
        while q:
            v=q.popleft()
            for w in graph[v]:
                if d[w]>d[v]+1:d[w]=d[v]+1;q.append(w)
        dist.append(d)
    result=[]
    for mask in range(1<<n):
        vertices=[i for i in range(n) if mask>>i&1]
        ok=True
        for i,u in enumerate(vertices):
            for v in vertices[i+1:]:
                for w in range(n):
                    if dist[u][w]+dist[w][v]==dist[u][v] and not(mask>>w&1):
                        ok=False;break
                if not ok:break
            if not ok:break
        if ok: result.append(mask)
    return tuple(result)


def prepare(n):
    concepts=candidate_concepts(n)
    positives=tuple(sum(1<<k for k,c in enumerate(concepts) if c>>x&1) for x in range(n))
    full=(1<<len(concepts))-1
    @lru_cache(maxsize=None)
    def dimension(version):
        if version.bit_count()<2:return 0
        best=0
        for positive_mask in positives:
            yes=version&positive_mask
            no=version^yes
            if not yes or not no: continue
            # To exceed 'best' both children must each have at least 2**best concepts.
            if min(yes.bit_count(),no.bit_count()) < (1 << best):continue
            score=1+min(dimension(yes),dimension(no))
            if score>best:best=score
        return best
    return concepts,positives,full,dimension


def can_depth_independent(n,depth):
    concepts=candidate_concepts(n)
    probes=tuple(sum(1<<i for i,c in enumerate(concepts) if c>>x&1) for x in range(n))
    full=(1<<len(concepts))-1
    @lru_cache(None)
    def can(version,d):
        if d==0:return bool(version)
        if version.bit_count() < (1<<d):return False
        for p in probes:
            a=version&p; b=version^a
            if a.bit_count()>=(1<<(d-1)) and b.bit_count()>=(1<<(d-1)):
                if can(a,d-1) and can(b,d-1):return True
        return False
    return can(full,depth)


def witness_tree(n,depth):
    concepts,positives,full,dimension=prepare(n)
    assert dimension(full)>=depth
    def build(version,d):
        if d==0:
            hidx=(version & -version).bit_length()-1
            return {'witness': concepts[hidx]}
        for x,p in enumerate(positives):
            yes=version&p;no=version^yes
            if yes and no and dimension(yes)>=d-1 and dimension(no)>=d-1:
                return {'query':x,'zero':build(no,d-1),'one':build(yes,d-1)}
        raise AssertionError('tree construction failed')
    tree=build(full,depth)
    def check(node,d,restrictions=()):
        if not d:
            h=node['witness']
            assert h in concepts
            assert all(((h>>x)&1)==v for x,v in restrictions)
            return [h]
        x=node['query']
        assert x not in [a for a,_ in restrictions]
        leaf0=check(node['zero'],d-1,restrictions+((x,0),))
        leaf1=check(node['one'],d-1,restrictions+((x,1),))
        return leaf0+leaf1
    ws=check(tree,depth)
    assert len(ws)==(1<<depth) and len(set(ws))==len(ws)
    return tree


def check_all():
    rows=[]
    for n in range(1,21):
        concepts,probes,full,rank=prepare(n)
        N=len(concepts)
        assert N==expected_count(n),(n,N,expected_count(n))
        if n<=11:
            graph=graph_convex_concepts(n)
            assert graph==concepts,(n,len(graph),N)
        triples=0
        for a,b,c in combinations(range(n),3):
            S=(1<<a)|(1<<b)|(1<<c)
            trace={h&S for h in concepts}
            yes=len(trace)==8
            want=(b-a)%2==1 and (c-b)%2==1
            assert yes==want,(n,a,b,c)
            triples+=yes
        assert triples==expected_triples(n),(n,triples)
        if n<=12:
            # Separate predicate recursion, independent of numerical-rank recursion.
            assert can_depth_independent(n,rank(full)), n
            assert not can_depth_independent(n,rank(full)+1), n
        val=rank(full)
        rows.append([n,N,val,N.bit_length()-1,triples])
    expected=[1,2,3,3,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7]
    assert [r[2] for r in rows]==expected
    assert rows[9][2]==5 and rows[9][3]==6
    assert all(row[2]==row[3] for row in rows[:9])
    assert [r[0] for r in rows if r[2]<r[3]]==[10,13,14,15,19,20]
    C,P,F,rank=prepare(10)
    root_branches=[]
    for x,p in enumerate(P):
        yes=F&p;no=F^yes
        root_branches.append([x,yes.bit_count(),no.bit_count(),rank(yes),rank(no)])
    assert max(1+min(v[3],v[4]) for v in root_branches)==5
    tree=witness_tree(10,5)
    return rows,root_branches,tree

if __name__=='__main__':
    rows,branches,tree=check_all()
    print('n,number_of_convex_hypotheses,exact_littlestone_dimension,information_ceiling,shattered_triples')
    for row in rows:print(*row,sep=',')
    print('ten_vertex_root_branch_table [query, positives, negatives, positive_depth, negative_depth]')
    for row in branches:print(row)
    print('all graph-distance, independent static, independent online feasibility, and tree witness checks PASS')
    print('SQUARED_PATH_CONVEXITY_ALL_CHECKS_PASS')
