"""Reproducible tests for the edge-open-packing theorem on Möbius ladders.

Python 3.11+, NumPy and SciPy are required for MILP cross-checks.
All graph definitions and test instances are built here.
"""
from itertools import combinations
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix


def graph_edges(n):
    N = 2*n
    return sorted({tuple(sorted((i, (i+1)%N))) for i in range(N)} |
                  {(i, i+n) for i in range(n)})


def proposed_set(n):
    assert n >= 3
    q, r = divmod(n, 6)
    centers = list(range(0, 6*q, 6)) + [n+3+6*i for i in range(q)]
    if r == 3:
        centers = list(range(0, 2*n, 6))
    elif r == 4:
        centers.append(6*q)
    edges = set()
    def add(a, b):
        a %= 2*n; b %= 2*n
        assert a != b
        edges.add(tuple(sorted((a,b))))
    for c in centers:
        add(c, c-1); add(c, c+1); add(c,c+n)
    if r == 0:
        edges.remove((0,2*n-1))
    elif r == 2:
        add(6*q-1,6*q)
    elif r == 5:
        add(6*q-1,6*q);add(6*q,6*q+n)
        add(6*q+2,6*q+3);add(6*q+2,6*q+2+n)
    return edges


def is_packing(n, selected):
    G=set(graph_edges(n))
    if not selected <= G:
        return False
    edgelist=list(selected)
    for i, a in enumerate(edgelist):
        for b in edgelist[:i]:
            if any(tuple(sorted((u,v))) in G and tuple(sorted((u,v))) not in (a,b)
                   for u in a for v in b if u != v):
                return False
    return True


def is_packing_fast(n, selected):
    G=set(graph_edges(n))
    if not selected <= G:
        return False
    U=set(sum((list(e) for e in selected), []))
    induced={e for e in G if e[0] in U and e[1] in U}
    if induced != selected:
        return False
    adjacency={v:[] for v in U}
    for a,b in selected:
        adjacency[a].append(b);adjacency[b].append(a)
    unseen=set(U)
    while unseen:
        v=next(iter(unseen)); stack=[v]; unseen.remove(v); component=[]
        while stack:
            u=stack.pop();component.append(u)
            for w in adjacency[u]:
                if w in unseen:
                    unseen.remove(w);stack.append(w)
        if len(component)>2 and not any(len(adjacency[u])==len(component)-1 for u in component):
            return False
    return True


def optimum_milp(n):
    E=graph_edges(n); S=set(E)
    conflicting=[]
    for i,a in enumerate(E):
        for j,b in enumerate(E[:i]):
            if any(tuple(sorted((u,v))) in S and tuple(sorted((u,v))) not in (a,b)
                   for u in a for v in b if u != v):
                conflicting.append((i,j))
    M=lil_matrix((len(conflicting),len(E)),dtype=float)
    for k,(i,j) in enumerate(conflicting):
        M[k,i]=1.; M[k,j]=1.
    result=milp(c=-np.ones(len(E)), integrality=np.ones(len(E)),
                bounds=Bounds(np.zeros(len(E)),np.ones(len(E))),
                constraints=LinearConstraint(M.tocsr(),np.zeros(len(conflicting)),np.ones(len(conflicting))),
                options={'time_limit':12.0,'mip_rel_gap':0.0})
    assert result.status==0, (n,result.message)
    return int(round(-result.fun))


def brute_optimum(n):
    E=graph_edges(n)
    # This deliberately enumerates every subset, independently of MILP.
    best=0
    for size in range(1,len(E)+1):
        if size <= best:continue
        found=False
        for indices in combinations(range(len(E)), size):
            if is_packing(n,{E[i] for i in indices}):
                best=size;found=True;break
        if not found:
            break
    return best


def bipartition_equality_sets(n):
    assert n % 6 == 3
    k=(n+1)//2
    covers=[]
    for i in range(n):
        covers.append(sum(1 << (j%n) for j in (i,i-1,i-k)))
    allmask=(1<<n)-1
    source_to_rows=[[i for i in range(n) if (covers[i]>>j)&1] for j in range(n)]
    solutions=[]
    def dfs(covered, chosen):
        if covered==allmask:
            solutions.append(chosen)
            return
        choices=min(([i for i in source_to_rows[j] if not (covers[i]&covered)]
                     for j in range(n) if not (covered>>j)&1),key=len)
        for i in choices:
            dfs(covered|covers[i],chosen+(i,))
    dfs(0,tuple())
    return len(solutions)


def main():
    for n in range(3,1000):
        P=proposed_set(n)
        expect=n if n%6==3 else n-1
        assert len(P)==expect and is_packing_fast(n,P),n
    print('CONSTRUCTIONS_OK n=3..999, all six residue classes')
    for n in range(3,7):
        expect=n if n%6==3 else n-1
        x=brute_optimum(n)
        assert x==expect,(n,x,expect)
    print('FULL_SUBSET_ENUMERATION_OK n=3..6')
    for n in range(3,37):
        expect=n if n%6==3 else n-1
        x=optimum_milp(n)
        assert x==expect,(n,x,expect)
    print('EXACT_MILP_OK n=3..36, 34 instances')
    for n in [3,9,15,21,27,33]:
        assert bipartition_equality_sets(n)==3,n
    print('EQUALITY_CENSUS_OK n=3,9,15,21,27,33, three centers per parity')
    print('VERIFY_OK')

if __name__=='__main__':main()
