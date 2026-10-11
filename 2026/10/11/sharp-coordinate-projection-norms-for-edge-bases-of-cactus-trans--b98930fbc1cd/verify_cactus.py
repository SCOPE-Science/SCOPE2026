#!/usr/bin/env python3
"""Exact-rational independent graph-transport checks for cycle-block coordinate projections.

Use: python check_cactus.py
No external packages. Finite checks only; the proof applies at every size.
"""
from fractions import Fraction
from itertools import combinations


def spanning_trees(n,edges):
    for ix in combinations(range(len(edges)),n-1):
        parent=list(range(n))
        def root(a):
            while parent[a]!=a:a=parent[a]
            return a
        for k in ix:
            u,v,_=edges[k]
            parent[root(u)]=root(v)
        if len({root(i) for i in range(n)})==1:
            yield ix


def cost_on_tree(n,edges,chosen,demand):
    b=list(demand)
    neighbors=[[] for _ in range(n)]
    for k in chosen:
        u,v,w=edges[k]
        neighbors[u].append((v,k))
        neighbors[v].append((u,k))
    live=[True]*n
    total=Fraction(0)
    for _ in range(n-1):
        leaf=next(i for i in range(n) if live[i] and sum(live[j] for j,_ in neighbors[i])==1)
        parent,k=next((j,k) for j,k in neighbors[leaf] if live[j])
        total+=abs(b[leaf])*edges[k][2]
        b[parent]+=b[leaf]
        live[leaf]=False
    assert b[next(i for i in range(n) if live[i])]==0
    return total


def norm_demand(n,edges,demand):
    return min(cost_on_tree(n,edges,ix,demand) for ix in spanning_trees(n,edges))


def incidence(n,edges,k):
    u,v,_=edges[k]
    r=[Fraction(0)]*n
    r[u]=-1;r[v]=1
    return r


def test_case(n,edges,cycles,removals):
    # Each cycle is coherently oriented in its edge indexing.
    removed=set(removals)
    tree=sorted(set(range(len(edges)))-removed)
    assert len(tree)==n-1
    block_of={k:j for j,c in enumerate(cycles) for k in c}
    tree_list=list(spanning_trees(n,edges))
    assert tuple(tree) in tree_list
    checks=0
    for mask in range(1<<len(tree)):
        S={tree[i] for i in range(len(tree)) if (mask>>i)&1}
        rhs=Fraction(int(bool(S)))
        for j,c in enumerate(cycles):
            wtotal=sum((edges[k][2] for k in c),Fraction(0))
            wS=sum((edges[k][2] for k in c if k in S),Fraction(0))
            rhs=max(rhs,min(wS,wtotal-wS)/edges[removals[j]][2])
        lhs=Fraction(0)
        for e,(_,_,w) in enumerate(edges):
            if e in tree:
                demands=[incidence(n,edges,e)] if e in S else []
            else:
                j=block_of[e]
                # cycle orientations must be coherent, giving the relation sum incidence(e)=0
                demands=[incidence(n,edges,k) for k in cycles[j] if k in S]
            b=[-sum((r[i] for r in demands),Fraction(0)) if e in removed else sum((r[i] for r in demands),Fraction(0)) for i in range(n)]
            score=min((cost_on_tree(n,edges,ix,b) for ix in tree_list)) / w
            lhs=max(lhs,score)
        assert lhs==rhs,(n,edges,cycles,removals,S,lhs,rhs)
        checks+=1
    return checks


def W(u,v,w):return (u,v,Fraction(w))

# Cycle orientations are clockwise, including a second cycle sharing one vertex.
cases=[
(3,[W(0,1,1),W(1,2,1),W(2,0,1)],[[0,1,2]],[2]),
(3,[W(0,1,1),W(1,2,2),W(2,0,5)],[[0,1,2]],[2]),
(4,[W(0,1,1),W(1,2,1),W(2,3,1),W(3,0,1)],[[0,1,2,3]],[0]),
(4,[W(0,1,2),W(1,2,3),W(2,3,9),W(3,0,5)],[[0,1,2,3]],[2]),
(5,[W(0,1,1),W(1,2,1),W(2,0,1),W(2,3,2),W(3,4,3),W(4,2,4)],[[0,1,2],[3,4,5]],[2,5]),
(5,[W(0,1,1),W(1,2,1),W(2,3,1),W(3,0,1),W(3,4,8)],[[0,1,2,3]],[1]),
(7,[W(0,1,1),W(1,2,3),W(2,0,2),W(2,3,4),W(3,4,2),W(4,5,3),W(5,3,1),W(5,6,5)],[[0,1,2],[4,5,6]],[0,5]),
(4,[W(0,1,2),W(1,2,3),W(2,3,4)],[],[])
]
if __name__=='__main__':
    cases_checked=0;projection_checks=0
    for case in cases:
        c=test_case(*case)
        projection_checks+=c
        cases_checked+=1
    print('EXACT_CACTUS_CHECK_OK',cases_checked,projection_checks)
