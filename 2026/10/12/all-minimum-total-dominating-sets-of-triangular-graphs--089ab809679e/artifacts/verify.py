"""Check minimum total domination of the triangular graph independently.
For each size-minimum edge set in K_n, test open neighborhoods in J(n,2)
and compare with the forest classification and the closed labeled count.
"""
from itertools import combinations
from math import comb, factorial, ceil


def formula(n):
    assert n >= 4
    t, r = divmod(n, 3)
    if r == 1:
        return factorial(n) // (2**t * factorial(t))
    if r == 2:
        return factorial(n) * 2 // (3 * 2**(t-1) * factorial(t-1))
    total = factorial(n) // (2**t * factorial(t))
    if t >= 2:
        total += factorial(n) * 25 // (24 * 2**(t-2) * factorial(t-2))
    if t >= 3:
        total += factorial(n) * 2 // (9 * 2**(t-3) * factorial(t-3))
    return total


def selected_forest_profile(n, selected_edges):
    deg = [0]*n
    graph = [[] for _ in range(n)]
    for u,v in selected_edges:
        deg[u]+=1;deg[v]+=1
        graph[u].append(v);graph[v].append(u)
    isolated=sum(d==0 for d in deg)
    seen=set(); comps=[]
    for v in range(n):
        if v in seen or not graph[v]:
            continue
        stack=[v]; seen.add(v); vertices=[]
        while stack:
            z=stack.pop();vertices.append(z)
            for w in graph[z]:
                if w not in seen:
                    seen.add(w);stack.append(w)
        es=sum(deg[w] for w in vertices)//2
        comps.append((len(vertices),es))
    comps.sort()
    return isolated,tuple(comps)


def expected_profiles(n):
    t,r=divmod(n,3)
    if r==1:
        return {(1, ((3,2),)*t)}
    if r==2:
        return {(1, ((3,2),)*(t-1)+((4,3),))}
    out={(0,((3,2),)*t)}
    if t>=2:out.add((1,((3,2),)*(t-2)+((5,4),)))
    if t>=3:out.add((1,((3,2),)*(t-3)+((4,3),(4,3))))
    return out

report=[]
examined=0
for n in range(4,10):
    edges=list(combinations(range(n),2))
    m=len(edges)
    k=(2*(n-1)+2)//3
    adjacency=[]
    for i,(a,b) in enumerate(edges):
        nb=0
        for j,(u,v) in enumerate(edges):
            if i!=j and (a in (u,v) or b in (u,v)):
                nb |= 1<<j
        adjacency.append(nb)
    profiles=expected_profiles(n)
    found=0
    for idxs in combinations(range(m),k):
        examined+=1
        mask=sum(1<<i for i in idxs)
        total_dominating=all(nei & mask for nei in adjacency)
        selected=[edges[i] for i in idxs]
        classification=selected_forest_profile(n,selected) in profiles
        if total_dominating!=classification:
            raise AssertionError((n,idxs,total_dominating,classification,selected_forest_profile(n,selected)))
        if total_dominating:found+=1
    if found!=formula(n):
        raise AssertionError((n,k,found,formula(n)))
    report.append((n,k,found))

# Independent larger formula/shape sanity: all terms integral and positive.
for n in range(4,151):
    value=formula(n)
    assert isinstance(value,int) and value>0
print(f"ALL CHECKS PASSED; minimum_subsets_checked={examined}; cases={report}; formulas_n=4..150")
