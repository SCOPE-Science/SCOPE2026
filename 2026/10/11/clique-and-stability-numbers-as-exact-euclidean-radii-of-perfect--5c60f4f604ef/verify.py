#!/usr/bin/env python3
from itertools import combinations

def edgeset(n, edges):
    E=set()
    for u,v in edges:
        if u>v: u,v=v,u
        E.add((u,v))
    return E

def is_edge(E,u,v):
    if u>v: u,v=v,u
    return (u,v) in E

def subsets(n):
    for mask in range(1<<n):
        yield tuple(i for i in range(n) if (mask>>i)&1)

def stable(E,S):
    return all(not is_edge(E,u,v) for u,v in combinations(S,2))

def clique(E,S):
    return all(is_edge(E,u,v) for u,v in combinations(S,2))

def rank_q(mat):
    A=[list(map(int,row)) for row in mat]
    if not A:
        return 0
    m=len(A); n=len(A[0]); r=0
    from fractions import Fraction
    A=[[Fraction(x) for x in row] for row in A]
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m:
            break
    return r

def check_graph(n,E,name):
    sts=[S for S in subsets(n) if stable(E,S)]
    cls=[C for C in subsets(n) if clique(E,C)]
    alpha=max(map(len,sts))
    omega=max(map(len,cls))
    vertices=[]
    for S in sts:
        chi=[1 if i in S else 0 for i in range(n)]
        vertices.append(tuple(chi+[1]))
        vertices.append(tuple([-x for x in chi]+[-1]))

    # Every clique inequality |2 x(C)-t| <= 1 is exact on all vertices.
    for C in cls:
        a=[2 if i in C else 0 for i in range(n)]+[-1]
        vals=[sum(a[j]*v[j] for j in range(n+1)) for v in vertices]
        assert max(vals)<=1 and min(vals)>=-1
        assert 1 in vals and -1 in vals

        # Both signed supporting hyperplanes have affine rank n.
        for sgn in (1,-1):
            face=[v for v,val in zip(vertices,vals) if val==sgn]
            base=face[0]
            diffs=[[v[j]-base[j] for j in range(n+1)] for v in face[1:]]
            assert rank_q(diffs)==n, (name,C,sgn)

    max_normal_sq=max(4*len(C)+1 for C in cls)
    max_vertex_sq=max(sum(x*x for x in v) for v in vertices)
    assert max_normal_sq==4*omega+1
    assert max_vertex_sq==alpha+1
    return len(sts),len(cls),alpha,omega

tests=[]
for n in range(1,6):
    tests.append((n,edgeset(n,[]),f"empty{n}"))
    tests.append((n,edgeset(n,list(combinations(range(n),2))),f"complete{n}"))
for n in range(2,7):
    tests.append((n,edgeset(n,[(i,i+1) for i in range(n-1)]),f"path{n}"))
for a,b in [(1,3),(2,2),(2,3),(3,3)]:
    n=a+b
    tests.append((n,edgeset(n,[(i,j) for i in range(a) for j in range(a,n)]),f"K{a},{b}"))
tests.append((4,edgeset(4,[(0,1),(1,2),(2,3),(3,0)]),"cycle4"))
tests.append((5,edgeset(5,[(0,1),(1,2),(2,3),(3,0),(0,4),(1,4)]),"split5"))

totv=totc=0
for n,E,name in tests:
    sv,cl,alpha,omega=check_graph(n,E,name)
    totv+=2*sv
    totc+=cl

print(f"VERIFY_OK hansen-radii graphs={len(tests)} signed_vertices={totv} cliques={totc} facet_ranks=exact")
