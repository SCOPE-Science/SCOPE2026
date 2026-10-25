#!/usr/bin/env python3
"""Finite exact checks for domination of full and leaf-pruned rooted regular trees.
Python 3 standard library only. This script tests finite instances; the theorem has a separate proof.
"""
from itertools import combinations
from random import Random

INF=10**16

def better(choices):
    feasible=[(v,c) for v,c in choices if v<INF and c>0]
    if not feasible:return INF,0
    v=min(x for x,_ in feasible)
    return v,sum(c for x,c in feasible if x==v)

def add(a,b):
    if a[1]==0 or b[1]==0:return INF,0
    return a[0]+b[0],a[1]*b[1]

def dp_children(children_states):
    chosen=(1,1)
    for states in children_states:
        chosen=add(chosen,better(states))
    none=(0,1)
    some=(INF,0)
    for A,B,C in children_states:
        newnone=add(none,B)
        newsome=better((add(some,B), add(none,A), add(some,A)))
        none,some=newnone,newsome
    return chosen,some,none

def rooted_tree(d,h):
    parent=[-1]; levels=[[0]]
    for _ in range(h):
        L=[]
        for p in levels[-1]:
            for _ in range(d):
                L.append(len(parent));parent.append(p)
        levels.append(L)
    return parent,levels

def trim_tree(parent,remove):
    # original BFS labeling, restricted graph, no other assumptions
    keep=[i for i in range(len(parent)) if i not in remove]
    ix={v:j for j,v in enumerate(keep)}
    children=[[] for _ in keep]
    nbr=[set() for _ in keep]
    for v in keep:
        p=parent[v]
        if p>=0:
            assert p in ix
            a=ix[p];b=ix[v]
            children[a].append(b)
            nbr[a].add(b);nbr[b].add(a)
    return children,nbr

def graph_dp(children):
    val=[None]*len(children)
    for v in range(len(children)-1,-1,-1):
        val[v]=dp_children([val[w] for w in children[v]])
    return better(val[0][:2])

def brute_count(nbr,k):
    N=len(nbr)
    closed=[(1<<v)|sum(1<<w for w in nb) for v,nb in enumerate(nbr)]
    count=0
    for sel in combinations(range(N),k):
        bits=sum(1<<v for v in sel)
        if all(bits & n for n in closed): count+=1
    return count

def expected_full_optima(d,h,levels):
    cutoff={0:2,1:0,2:1}[h%3]
    base=set()
    for level in range(h-1,cutoff-1,-3):
        base.update(levels[level])
    if h%3==0:
        return {frozenset(base|{v}) for v in (levels[0]+levels[1])}
    return {frozenset(base)}

def formula(d,h):
    assert d>=2 and h>=1
    gamma=sum(d**(h-1-3*j) for j in range((h-1)//3+1))+(h%3==0)
    return gamma, d+1 if h%3==0 else 1

def run():
    dp_cases=0; stable_cases=0; threshold_cases=0; brute_cases=0; structural_cases=0
    rng=Random(20261023)
    for d in range(2,7):
        for h in range(1,7 if d<=3 else 6 if d==4 else 5):
            parent,levels=rooted_tree(d,h)
            children,nbr=trim_tree(parent,set())
            expected=formula(d,h)
            got=graph_dp(children)
            assert got==expected,('untrimmed',d,h,got,expected)
            dp_cases+=1
            # Delete <=d-2 leaves at every penultimate vertex, independently.
            for rep in range(3):
                groups={}
                for v in levels[-1]:groups.setdefault(parent[v],[]).append(v)
                removed=set()
                for group in groups.values():
                    count=rng.randrange(d-1)
                    removed.update(rng.sample(group,count))
                c,n=trim_tree(parent,removed)
                g=graph_dp(c)
                assert g==expected,('stable',d,h,rep,g,expected)
                stable_cases+=1
            # For just one exceptional sibling group, keep one leaf.
            group=[v for v in levels[-1] if parent[v]==levels[-2][0]]
            removed=set(group[1:])
            c,n=trim_tree(parent,removed)
            g=graph_dp(c)
            assert g==(expected[0],2*expected[1]),('threshold',d,h,g,expected)
            threshold_cases+=1
            # Also brute-force selected small graphs, including the boundary event.
            if (d==2 and h<=3) or (h<=2 and d<=5):
                for leaf_removed in [set(),removed]:
                    c2,nbr2=trim_tree(parent,leaf_removed)
                    gamma, zeta=graph_dp(c2)
                    assert brute_count(nbr2,gamma-1)==0,('brute lower',d,h,leaf_removed)
                    assert brute_count(nbr2,gamma)==zeta,('brute count',d,h,leaf_removed)
                    if not leaf_removed:
                        closed=[{v}|nb for v,nb in enumerate(nbr2)]
                        actual={frozenset(sel) for sel in combinations(range(len(nbr2)),gamma)
                                if all(any(w in sel for w in cl) for cl in closed)}
                        expected_sets=expected_full_optima(d,h,levels)
                        assert actual==expected_sets,('brute structure',d,h,actual,expected_sets)
                        structural_cases+=1
                    brute_cases+=1
    assert (dp_cases,stable_cases,threshold_cases,brute_cases,structural_cases)==(25,75,25,18,9), (dp_cases,stable_cases,threshold_cases,brute_cases,structural_cases)
    print('VERIFY_OK', 'full_dp_cases=',dp_cases,'stable_leaf_prunings=',stable_cases,
          'sharp_one_group_prunings=',threshold_cases,'brute_minimality_and_counts=',brute_cases,'brute_optimum_set_classifications=',structural_cases)

if __name__=='__main__':run()
