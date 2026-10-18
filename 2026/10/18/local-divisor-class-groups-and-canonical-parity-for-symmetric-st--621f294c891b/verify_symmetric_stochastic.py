#!/usr/bin/env python3
"""Exact fixed-chart ray-matrix verifier for symmetric stochastic polytopes."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
from collections import Counter
from itertools import product
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

@lru_cache(None)
def support_decompositions(vertices):
    """Each support consists of pairwise disjoint loops, pairs and odd cycles."""
    vertices = tuple(vertices)
    if not vertices:
        return ((),)
    a = vertices[0]
    rest = vertices[1:]
    ans=[]
    for tail in support_decompositions(rest):
        ans.append(((a,),)+tail)
    for b in rest:
        rr=tuple(x for x in rest if x!=b)
        for tail in support_decompositions(rr):
            ans.append(((a,b),)+tail)
    for length in range(3,len(vertices)+1,2):
        for others in combinations(rest,length-1):
            # Every undirected cycle containing a has two traversal choices.
            for order in permutations(others):
                if order[0]>order[-1]:
                    continue
                rr=tuple(x for x in rest if x not in others)
                for tail in support_decompositions(rr):
                    ans.append(((a,)+order,)+tail)
    return tuple(ans)

def analyze(n,components):
    offdiag=list(combinations(range(n),2))
    idx={edge:i for i,edge in enumerate(offdiag)}
    positive=set()
    loops=set()
    pairs=cycles=0
    for block in components:
        if len(block)==1:
            loops.add(block[0])
        elif len(block)==2:
            positive.add(tuple(sorted(block)))
            pairs+=1
        else:
            cycles+=1
            for j in range(len(block)):
                positive.add(tuple(sorted((block[j],block[(j+1)%len(block)]))))
    A=[]
    for edge in offdiag:
        if edge not in positive:
            row=[0]*len(offdiag)
            row[idx[edge]]=1
            A.append(row)
    for i in range(n):
        if i not in loops:
            A.append([-int(i in e) for e in offdiag])
    A=sp.Matrix(A)
    assert A.rank()==len(offdiag)
    D=smith_normal_form(A,domain=ZZ)
    diag=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]!=0]
    assert len(diag)==len(offdiag)
    torsion=[x for x in diag if x!=1]
    free=A.rows-A.cols
    assert free==pairs and torsion==[2]*cycles,(n,components,free,torsion,pairs,cycles)
    rhs=sp.ones(A.rows,1)
    solved=sp.linsolve((A,rhs))
    assert solved!=sp.EmptySet
    sol=list(next(iter(solved)))
    index=sp.ilcm(*[sp.denom(x) for x in sol])
    expect=2 if n%2==1 and cycles else 1
    assert index==expect,(n,components,index,expect)
    assert (len(A.tolist())==len(offdiag)+pairs)
    return pairs,cycles,index

def independent_polytope_vertices(n):
    """Independently enumerate all basic feasible solutions using facet subsets."""
    edges=list(combinations(range(n),2))
    d=len(edges)
    rows=[]; rhs=[]
    for j in range(d):
        row=[0]*d;row[j]=1;rows.append(row);rhs.append(0)
    for i in range(n):
        rows.append([-int(i in e) for e in edges]);rhs.append(-1)
    found=set()
    for active in combinations(range(d+n),d):
        A=sp.Matrix([rows[i] for i in active])
        if A.det()==0:continue
        sol=A.inv()*sp.Matrix([rhs[i] for i in active])
        if any(sum(row[j]*sol[j] for j in range(d))<rhs[k] for k,row in enumerate(rows)):continue
        found.add(tuple(Fraction(sol[j]) for j in range(d)))
    prescribed=set()
    for components in support_decompositions(tuple(range(n))):
        weights={e:Fraction(0) for e in edges}
        for b in components:
            if len(b)==2:weights[tuple(sorted(b))]=Fraction(1)
            elif len(b)>=3:
                for j in range(len(b)):
                    weights[tuple(sorted((b[j],b[(j+1)%len(b)])))]=Fraction(1,2)
        prescribed.add(tuple(weights[e] for e in edges))
    assert found==prescribed,(n,len(found),len(prescribed))
    print('independent_LP_vertices',n,len(found))

def main():
    for n in (3,4): independent_polytope_vertices(n)
    for n in range(3,7):
        verts=support_decompositions(tuple(range(n)))
        group=Counter()
        for v in verts:
            group[analyze(n,v)[:2]]+=1
        assert group[(0,0)]==1
        print('n=',n,'vertices=',len(verts),'classes=',dict(sorted(group.items())))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
