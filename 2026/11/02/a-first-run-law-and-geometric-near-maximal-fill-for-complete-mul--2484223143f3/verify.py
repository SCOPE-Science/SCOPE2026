#!/usr/bin/env python3
"""Exact checks of the complete multipartite symbolic-elimination fill law.

Standard-library only. Graph-theoretic elimination is evaluated independently
from the first-run formulas. Checks are finite diagnostics, not an infinite proof.
"""
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial
from collections import Counter

def falling(n, r):
    z = 1
    for j in range(r):
        z *= n-j
    return z

def part_graph(sizes):
    labels = tuple(i for i, n in enumerate(sizes) for _ in range(n))
    g = [set() for _ in labels]
    for u in range(len(labels)):
        for v in range(u+1, len(labels)):
            if labels[u] != labels[v]:
                g[u].add(v)
                g[v].add(u)
    return g

def graph_fill(sizes, order):
    g = part_graph(sizes)
    num_added = 0
    for v in order:
        nb = sorted(g[v])
        for j, u in enumerate(nb):
            for w in nb[j+1:]:
                if w not in g[u]:
                    g[u].add(w)
                    g[w].add(u)
                    num_added += 1
        for u in nb:
            g[u].remove(v)
        g[v].clear()
    return num_added

def pmf_formula(sizes):
    n = sum(sizes)
    missing = sum(comb(v,2) for v in sizes)
    out = {}
    for x in sizes:
        for run in range(1,x+1):
            fill = missing-comb(x,2)+comb(x-run,2)
            p = Fraction(falling(x,run)*(n-x),falling(n,run+1))
            out[fill] = out.get(fill, Fraction(0))+p
    return out

def expected_formula(sizes):
    n = sum(sizes)
    return sum((Fraction(comb(x,2)*(n-x), n-x+2) for x in sizes),Fraction(0))

def independent_pmf(sizes):
    n=sum(sizes)
    counts=Counter(graph_fill(sizes,order) for order in permutations(range(n)))
    return {k:Fraction(v,factorial(n)) for k,v in counts.items()}

def numeric_cholesky_fill(sizes, order):
    """Exact rational Schur-complement fill for I + graph Laplacian."""
    labels = tuple(i for i, n in enumerate(sizes) for _ in range(n))
    N=len(labels)
    mat=[[Fraction(0) for _ in range(N)] for _ in range(N)]
    for u in range(N):
        mat[u][u]=Fraction(1)
        for v in range(N):
            if u!=v and labels[u]!=labels[v]:
                mat[u][v]=Fraction(-1)
                mat[u][u]+=1
    alive=set(range(N))
    fill=0
    for v in order:
        others=sorted(alive-{v})
        d=mat[v][v]
        assert d>0
        for ii,u in enumerate(others):
            for w in others[ii:]:
                before=mat[u][w]
                new=before-mat[u][v]*mat[v][w]/d
                if u!=w and before==0 and new!=0: fill+=1
                mat[u][w]=mat[w][u]=new
        alive.remove(v)
    return fill

def verification():
    count=0
    for r in range(2,6):
        for sizes in product((1,2,3,4),repeat=r):
            if sum(sizes)>7:continue
            masses=pmf_formula(sizes)
            assert sum(masses.values())==1, sizes;count+=1
            avg=sum((k*v for k,v in masses.items()),Fraction(0))
            assert avg==expected_formula(sizes),sizes;count+=1
            m=sum(comb(x,2) for x in sizes)
            assert min(masses)==m-max(comb(x,2) for x in sizes),sizes;count+=1
            assert max(masses)==m-(min(sizes)-1),sizes;count+=1
            true=independent_pmf(sizes)
            assert true==masses,(sizes,true,masses);count+=1
    for sizes in ((2,2),(1,2,2),(2,2,2),(2,3,1)):
        for order in permutations(range(sum(sizes))):
            assert numeric_cholesky_fill(sizes, order)==graph_fill(sizes,order)
            count+=1
    for r in (2,3,4,7):
        for m in (2,3,4,5,8,15,40):
            sizes=(m,)*r
            masses=pmf_formula(sizes)
            n=r*m
            M=r*comb(m,2)
            avg=sum((k*v for k,v in masses.items()),Fraction(0))
            assert avg==Fraction(M*(r-1)*m, (r-1)*m+2);count+=1
            assert Fraction(avg,(r-1)*comb(m,2))==Fraction(r*m,(r-1)*m+2);count+=1
            # Explicit leading-run probabilities add to one.
            assert sum((Fraction(r*falling(m,s)*(n-m),falling(n,s+1)) for s in range(1,m+1)),Fraction(0))==1;count+=1
            if m>=3:
                pmax=Fraction((r-1)*m,r*m-1)
                assert masses[M-(m-1)]==pmax,(sizes,masses);count+=1
                pmin=Fraction(r*falling(m,m-1),falling(r*m,m-1))
                assert masses[(r-1)*comb(m,2)]==pmin,(sizes,masses);count+=1
    print('VERIFICATION_OK',count,'grouped exact assertions; all part vectors with 2..5 parts and <=7 vertices exhaustively checked.')
if __name__=='__main__': verification()
