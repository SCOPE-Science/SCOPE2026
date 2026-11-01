"""Independent finite checks for the cut-degree census in parallel chip-firing.

Run: python verify_cut_cycles.py
Uses only Python standard library; no external packages required.
All configurations inside the mathematically proved confined box are inspected.
"""
from collections import Counter
from itertools import product, permutations
from math import prod, sqrt
from random import Random
import json


def degrees_edges(n, edges):
    neighbors=[[] for _ in range(n)]
    for a,b in edges:
        assert 0<=a<b<n
        neighbors[a].append(b)
        neighbors[b].append(a)
    assert all(neighbors), 'connected nontrivial graphs have no isolates'
    return neighbors


def direct_count(n, edges):
    nbrs=degrees_edges(n, edges)
    deg=[len(q) for q in nbrs]
    def f(state):
        firing=[state[i]>=deg[i] for i in range(n)]
        return tuple(state[i] - deg[i]*firing[i] + sum(firing[j] for j in nbrs[i]) for i in range(n))
    result=Counter()
    tested=0
    for state in product(*(range(2*d) for d in deg)):
        nxt=f(state)
        nxt2=f(nxt)
        if nxt2==state and nxt!=state:
            result[sum(state)]+=1
        tested+=1
    assert all(v%2==0 for v in result.values())
    return {s:v//2 for s,v in result.items()},tested


def by_cuts(n, edges):
    m=len(edges)
    res=Counter()
    cut_dist=Counter()
    for mask in range(1<<(n-1)):
        color=[0]+[(mask>>(i-1))&1 for i in range(1,n)]
        c=[0]*n
        s=0
        for a,b in edges:
            if color[a]!=color[b]:
                c[a]+=1;c[b]+=1;s+=1
        cut_dist[s]+=1
        if 0 in c:continue
        p=[1]
        for k in c:
            q=[0]*(len(p)+k-1)
            for j,coeff in enumerate(p):
                for u in range(k):
                    q[j+u]+=coeff
            p=q
        for j,v in enumerate(p):
            res[2*m-s+j]+=v
    return dict(res),max(cut_dist),cut_dist[max(cut_dist)]



def tree_count_dp(n, edges):
    nbrs=degrees_edges(n,edges)
    assert len(edges)==n-1
    seen=set()
    def solve(v,parent):
        assert v not in seen
        seen.add(v)
        P,Q=1,0
        for u in nbrs[v]:
            if u==parent:continue
            a,b=solve(u,v)
            P,Q=P*(a+b),Q*(a+b)+P*b
        return Q,P+Q
    ans=solve(0,-1)[0]
    assert len(seen)==n
    return ans

def path(n):
    return [(i,i+1) for i in range(n-1)]


def complete(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def cycle(n):
    return path(n)+[(0,n-1)]


def star(n):
    return [(0,i) for i in range(1,n)]


def pell(m):
    a,b=0,1
    for _ in range(m):a,b=b,2*b+a
    return a


def test_one(n,edges):
    p,mc,nmc=by_cuts(n,edges)
    q,count=direct_count(n,edges)
    assert p==q,(n,edges,p,q)
    assert min(p)==2*len(edges)-mc
    assert max(p)==2*len(edges)+mc-n
    assert p[min(p)]==nmc==p[max(p)]
    assert all(p.get(s,0)==p.get(4*len(edges)-n-s,0) for s in p)
    return count


def main():
    cases=0; states=0; class_by_n=Counter(); trees_dp_checked=0
    # Canonical representatives of every connected simple graph through 5 vertices.
    for n in range(2,6):
        all_edges=[(i,j) for i in range(n) for j in range(i+1,n)]
        seen=set()
        for mask in range(1,1<<len(all_edges)):
            edges=[e for j,e in enumerate(all_edges) if (mask>>j)&1]
            adj=[[] for _ in range(n)]
            for a,b in edges:adj[a].append(b);adj[b].append(a)
            reached={0}; frontier=[0]
            while frontier:
                for w in adj[frontier.pop()]:
                    if w not in reached: reached.add(w);frontier.append(w)
            if len(reached)!=n:continue
            invariant=min(tuple(sorted((min(perm[a],perm[b]),max(perm[a],perm[b]))
                                           for a,b in edges)) for perm in permutations(range(n)))
            if invariant in seen: continue
            seen.add(invariant)
            ct=test_one(n,edges)
            if len(edges)==n-1:
                assert tree_count_dp(n,edges)==sum(by_cuts(n,edges)[0].values())
                trees_dp_checked+=1
            states+=ct;cases+=1;class_by_n[n]+=1
    for n in range(6,11):
        for edges in (path(n),star(n)):
            ct=test_one(n,edges)
            states+=ct;cases+=1;class_by_n[n]+=1
    for n in range(6,9):
        ct=test_one(n,cycle(n))
        states+=ct;cases+=1;class_by_n[n]+=1
    for a,b in ((2,3),(2,4),(3,3),(3,4)):
        n=a+b
        edges=[(i,j) for i in range(a) for j in range(a,n)]
        ct=test_one(n,edges)
        states+=ct;cases+=1;class_by_n[n]+=1
    rng=Random(20261027)
    for n in (6,7):
        for _ in range(14):
            edges=set(path(n))
            for a in range(n):
                for b in range(a+2,n):
                    if rng.random()<0.15:edges.add((a,b))
            edges=sorted(edges)
            if prod(2*sum(u in e for e in edges) for u in range(n))>160000:continue
            ct=test_one(n,edges)
            states+=ct;cases+=1;class_by_n[n]+=1
    pell_values=[]
    for n in range(2,16):
        p,mc,nmc=by_cuts(n,path(n))
        val=sum(p.values())
        assert val==pell(n-1),(n,val,pell(n-1))
        pell_values.append(val)
        assert tree_count_dp(n,path(n))==val
        trees_dp_checked+=1
        assert mc==n-1 and nmc==1
    summary={
        'status':'CUT_CYCLE_ALL_CHECKS_PASSED',
        'graph_tests':cases,
        'tree_dp_recurrence_checks':trees_dp_checked,
        'full_confined_states_checked':states,
        'graph_tests_by_size':dict(sorted(class_by_n.items())),
        'path_cycle_counts_n2_to_n15':pell_values,
        'P4_energy_count':dict(sorted(by_cuts(4,path(4))[0].items())),
        'triangle_energy_count':dict(sorted(by_cuts(3,complete(3))[0].items())),
        'type_of_checks':'Independent state-level two-update tests vs weighted cut polynomial; maxima, extremes, and palindromicity; path Pell identity.',
    }
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__':main()
