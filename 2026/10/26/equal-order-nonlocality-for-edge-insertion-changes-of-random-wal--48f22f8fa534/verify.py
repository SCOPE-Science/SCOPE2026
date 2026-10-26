"""Finite exact checks for equal-order edge-insertion cover-time witnesses.

Run: python verify.py
Uses only the Python standard library. Finite examples corroborate, but do not
prove, the all-radius theorem proved in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import ceil, exp, log


def graph(r, k, kind):
    """Return (adjacency, index of marked s,u,v); leaves are vertices 1,2,3."""
    assert r >= 1 and k >= 2
    n = 4 + r + k
    adj = [set() for _ in range(n)]
    def edge(a, b):
        assert a != b and b not in adj[a]
        adj[a].add(b)
        adj[b].add(a)
    for leaf in (1,2,3):
        edge(0, leaf)
    if kind == 'path':
        for j in range(4,n):
            edge(0 if j==4 else j-1,j)
    else:
        # 4,...,r+3 is the r-vertex stem, and r+4 is clique entry.
        for j in range(4,4+r):
            edge(0 if j==4 else j-1,j)
        t=4+r
        edge(3+r,t)
        for i,j in combinations(range(t,n),2):
            edge(i,j)
    return adj


def solve(A,b):
    n=len(b)
    for i in range(n):
        pivot=next(j for j in range(i,n) if A[j][i])
        if pivot!=i:
            A[i],A[pivot]=A[pivot],A[i]
            b[i],b[pivot]=b[pivot],b[i]
        fac=A[i][i]
        for t in range(i,n): A[i][t] /= fac
        b[i] /=fac
        for j in range(i+1,n):
            fac=A[j][i]
            if fac:
                for t in range(i,n): A[j][t]-=fac*A[i][t]
                b[j]-=fac*b[i]
    ans=[Q(0) for _ in range(n)]
    for i in range(n-1,-1,-1):
        ans[i]=b[i]-sum(A[i][j]*ans[j] for j in range(i+1,n))
    return ans


def cover_expectation(adj,start=1):
    """Exact cover expectation by visited-mask Bellman elimination."""
    n=len(adj)
    full=(1<<n)-1
    old={full:{i:Q(0) for i in range(n)}}
    for cnt in range(n-1,0,-1):
        masks=[m for m in range(1<<n) if m.bit_count()==cnt and m & (1<<start)]
        for mask in masks:
            ids=[i for i in range(n) if mask>>i&1]
            ind={x:j for j,x in enumerate(ids)}
            mat=[[Q(int(i==j)) for j in range(len(ids))] for i in range(len(ids))]
            rhs=[Q(1) for _ in ids]
            for i,x in enumerate(ids):
                deg=len(adj[x])
                for y in adj[x]:
                    if mask >> y & 1:
                        mat[i][ind[y]]-=Q(1,deg)
                    else:
                        rhs[i]+=Q(1,deg)*old[mask|1<<y][y]
            old[mask]=dict(zip(ids,solve(mat,rhs)))
        # Later layers are never used again beyond the next layer.
        old={m:values for m,values in old.items() if m.bit_count() in (cnt,cnt+1)}
    return old[1<<start][start]


def insert_uv(adj):
    out=[set(v) for v in adj]
    out[2].add(3); out[3].add(2)
    return out


def path_formula(q):
    return Q(2*(6*q**3+5*q*q-23*q-10),3*(q+1)*(3*q+2))


def check_finite(r,k):
    a=graph(r,k,'path'); b=graph(r,k,'clique')
    assert len(a)==len(b)==4+r+k
    assert [len(g[j]) for g in [a,b] for j in (1,2,3)]==[1]*6
    for g in (a,b):
        assert len(g[0])==4
        seen={1,2,3}; frontier=seen.copy()
        for _ in range(r):
            frontier=set().union(*(g[i] for i in frontier))-seen
            seen|=frontier
        # ambient-degree-labelled rooted ball agrees between the graphs
        if g is a: ball0={i:len(g[i]) for i in seen}
        else:
            assert len(seen)==len(ball0)
            assert {i:len(g[i]) for i in seen} == ball0
    base_a=cover_expectation(a); new_a=cover_expectation(insert_uv(a))
    base_b=cover_expectation(b); new_b=cover_expectation(insert_uv(b))
    da=new_a-base_a; db=new_b-base_b
    assert da==path_formula(r+k), (r,k,da,path_formula(r+k))
    assert da>0>db, (r,k,da,db)
    return f'r={r}, K={k}, n={len(a)}: positive delta={da}, negative delta={db}'


def check_analytic(r):
    k=max(100,4*r+10)
    q=r+k
    assert 6*q**3+5*q*q-23*q-10>0
    assert k*(k-1)>12*r*r+28*r+11
    bound=4*(r+1)-Q(2,3)*(k*(k-1)+2*r+7)/Q(2*r+3)
    assert bound<0
    # Probability upper bounds for not visiting all clique vertices and exiting.
    d=ceil(3*(k-1)*log(k))
    failure=(k-1)*exp(-d/(k-1))+(1+d/(k-1))/k
    assert failure < 0.5
    return f'r={r}, K={k}, positive={float(path_formula(q)):.6f}, negative upper={float(bound):.6f}, clique failure upper={failure:.6f}'

if __name__=='__main__':
    for r,k in [(1,3),(2,4),(1,5)]:
        print(check_finite(r,k))
    for r in list(range(1,201))+[1000,10000,100000]:
        check_analytic(r)
    for r in [1,2,3,5,10,100,1000,100000]:
        print(check_analytic(r))
    print('All exact finite witnesses and analytic-bound samples passed.')
