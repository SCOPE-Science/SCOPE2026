#!/usr/bin/env python3
"""Exact integer checks for the positive-root polytope edge classification.

Run: python3 verify.py
No third-party packages are required for the exact checks. An independent
linear-programming comparison is used if scipy is installed.
"""
from collections import deque
from itertools import combinations
from math import comb


def root(n, ij):
    i, j = ij
    return tuple((1 if t == i else -1 if t == j else 0) for t in range(1, n + 1))


def dot(h, ij):
    i, j = ij
    return h[i - 1] - h[j - 1]


def edge_case(e, f):
    (i, j), (k, ell) = e, f
    if i == k or j == ell:
        return 'shared'
    if j < k or ell < i:
        return 'disjoint'
    if (j == k and j == i + 1 and ell == k + 1) or (ell == i and ell == k + 1 and j == i + 1):
        return 'unit_chain'
    return 'no'


def witness(n, e, f):
    kind = edge_case(e, f)
    if kind == 'no':
        return None
    if kind == 'shared':
        (i, j), (k, ell) = e, f
        h = [1] * n
        if i == k:
            h[i - 1], h[j - 1], h[ell - 1] = 2, 0, 0
        else:
            h[i - 1], h[k - 1], h[j - 1] = 2, 2, 0
        return h
    if kind == 'disjoint':
        left, right = sorted((e, f))
        i, j = left
        k, ell = right
        assert i < j < k < ell
        h = [3] * n
        h[i-1], h[j-1], h[k-1], h[ell-1] = 4, 0, 6, 2
        return h
    a = min(e[0], f[0])
    h = [0]
    for t in range(1, n):
        h.append(h[-1] + (1 if t in (a, a+1) else 2))
    return h


def certify_pair(n, e, f, all_roots):
    kind = edge_case(e, f)
    if kind != 'no':
        h = witness(n, e, f)
        maximum = max(dot(h, v) for v in all_roots)
        attained = {v for v in all_roots if dot(h, v) == maximum}
        assert attained == {e, f}, (n, e, f, kind, attained)
        return
    (i, j), (k, ell) = e, f
    # Nonedges: either a four-root parallelogram or a nonunit chain.
    if j == k or ell == i:
        if ell == i:
            (i, j), (k, ell) = (k, ell), (i, j)
        assert j == k
        if j > i + 1:
            assert (i, i+1) not in (e, f)
        else:
            assert ell > j + 1
    else:
        # For neither same endpoint nor disjoint, the earlier source and
        # the other's source yield a crossing/nested parallelogram.
        if k < i:
            (i, j), (k, ell) = (k, ell), (i, j)
        assert i < k < j and ell > k
        other = [(i, ell), (k, j)] if ell != j else None
        if other:
            assert all(x[0] < x[1] for x in other)
            lhs = tuple(x+y for x,y in zip(root(n, e), root(n, f)))
            rhs = tuple(x+y for x,y in zip(root(n, other[0]), root(n, other[1])))
            assert lhs == rhs and set(other) != {e, f}


def check_exact(n):
    vertices = list(combinations(range(1, n + 1), 2))
    assert len(vertices) == comb(n,2)
    # Strictly isolate every candidate point with integer linear functional.
    for e in vertices:
        h = [0]*n
        h[e[0]-1],h[e[1]-1] = 1,-1
        assert {v for v in vertices if dot(h,v)==2} == {e}
    graph = {e:set() for e in vertices}
    for e,f in combinations(vertices,2):
        certify_pair(n,e,f,vertices)
        if edge_case(e,f) != 'no':
            graph[e].add(f);graph[f].add(e)
    assert sum(map(len,graph.values()))//2 == 2*comb(n,3)+comb(n,4)+n-2
    simple_count = 0
    for (i,j), neighbors in graph.items():
        d = n-i-1+j-2+comb(i-1,2)+comb(n-j,2)
        if j==i+1:
            d += (i>1)+(j<n)
        assert d == len(neighbors), (n,(i,j),d,len(neighbors))
        simple_count += d == n-1
    assert simple_count == ({3:3,4:2,5:1}.get(n,0)),(n,simple_count)
    for v in graph:
        distances={v:0}; q=deque([v])
        while q:
            u=q.popleft()
            for w in graph[u]:
                if w not in distances:
                    distances[w]=distances[u]+1
                    q.append(w)
        assert len(distances)==len(vertices)
        assert max(distances.values()) == (1 if n == 3 else 2)
    return len(vertices),sum(map(len,graph.values()))//2,simple_count


def check_lp(n):
    try:
        from scipy.optimize import linprog
    except ImportError:
        print('Independent LP check: scipy unavailable (optional)')
        return None
    vertices=list(combinations(range(1,n+1),2))
    outcomes=0
    for e,f in combinations(vertices,2):
        # h_e = h_f = T, all other h_v <= T-1;
        # fix h_1=0, leaving T and the other h entries free.
        Aeq=[];beq=[];Aub=[];bub=[]
        for v in vertices:
            i,j=v
            row=[0.]*(n+1)
            row[i-1]+=1;row[j-1]-=1;row[-1]-=1
            if v in (e,f):
                Aeq.append(row);beq.append(0)
            else:
                Aub.append(row);bub.append(-1)
        bounds=[(0,0)]+[(None,None)]*(n)
        result=linprog([0.]*(n+1),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=bounds,method='highs')
        assert result.success == (edge_case(e,f)!='no'),(n,e,f,result.message)
        outcomes+=1
    return outcomes


if __name__=='__main__':
    checks=[]
    for n in range(3,13):
        checks.append((n,)+check_exact(n))
    print('Exact integer vertex/exposure/parallelogram/degree/diameter checks:',checks)
    print('Independent LP pair comparisons:',[(n,check_lp(n)) for n in range(3,9)])
    print('VERIFY_OK')
