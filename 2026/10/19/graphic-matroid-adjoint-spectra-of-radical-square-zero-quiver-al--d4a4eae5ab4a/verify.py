"""Standalone finite-field checks for a rank polynomial of radical-square-zero quiver algebras.

Run: python verify_adjoint_matroid.py
Uses only the Python standard library. The proof is symbolic and not dependent
on finite enumeration; these checks compare independent definitions in small cases.
"""
from itertools import product
from collections import Counter
from math import comb


def matrix_rank(mat, p):
    rows=[[(x%p) for x in row] for row in mat]
    if not rows: return 0
    ncol=len(rows[0]); lead=0; rank=0
    for col in range(ncol):
        pivot=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        v=pow(rows[rank][col],-1,p)
        rows[rank]=[(x*v)%p for x in rows[rank]]
        for j in range(rank+1,len(rows)):
            a=rows[j][col]
            if a:
                rows[j]=[(x-a*y)%p for x,y in zip(rows[j],rows[rank])]
        rank+=1
        if rank==len(rows): break
    return rank


def direct(n, edges, p):
    """Build ad(a): basis [vertex idempotents, oriented arrow basis]."""
    m=len(edges); counts=Counter()
    for coords in product(range(p), repeat=n+m):
        d=coords[:n]; z=coords[n:]; mat=[[0]*(n+m) for _ in range(n+m)]
        for t,(u,v) in enumerate(edges):
            row=n+t
            # arrow coefficient of [a, e_w], for w=u,v
            mat[row][u]=(mat[row][u]-z[t])%p
            mat[row][v]=(mat[row][v]+z[t])%p
            # [a, arrow_t] coefficient
            mat[row][n+t]=(d[u]-d[v])%p
        counts[matrix_rank(mat,p)]+=1
    return counts


def num_components(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    seen=set();ans=0
    for u in range(n):
        if u not in seen:
            ans+=1;seen.add(u);todo=[u]
            while todo:
                x=todo.pop()
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y);todo.append(y)
    return ans


def edge_rank(n, edges):
    return n-num_components(n, edges)


def by_flats(n,edges,q):
    m=len(edges); full_rank=edge_rank(n,edges);out=Counter()
    # Enumerate flats and proper q-colorings of contracted graph.
    for mask in range(1<<m):
        F=[edges[e] for e in range(m) if mask>>e&1]
        rF=edge_rank(n,F)
        # Flat iff no outside edge is spanned by F.
        if any(edge_rank(n,F+[edges[e]])==rF for e in range(m) if not (mask>>e&1)):
            continue
        colorings=0
        for d in product(range(q),repeat=n):
            if all(d[u]==d[v] for u,v in F) and all(d[u]!=d[v] for e,(u,v) in enumerate(edges) if not(mask>>e&1)):
                colorings+=1
        for sub in range(1<<m):
            if sub & ~mask: continue
            S=[edges[e] for e in range(m) if sub>>e&1]
            rank=(m-len(F))+edge_rank(n,S)
            out[rank]+=colorings*(q**(m-len(F)))*((q-1)**len(S))
    return out


def from_cycle(m,q):
    out=Counter()
    for j in range(m+1):
        out[j]+=comb(m,j)*(q*q-1)**j
        out[j]+=(q-1)*comb(m,j)*(-1)**j
    out[m-1]+=q*(q-1)**m
    out[m]-=q*(q-1)**m
    return +out


def forest(n,m,c,q):
    return Counter({j:q**c*comb(m,j)*(q*q-1)**j for j in range(m+1)})


def multiply(a,b):
    ans=Counter()
    for i,x in a.items():
        for j,y in b.items():ans[i+j]+=x*y
    return +ans


def checks():
    trials=[
        ('triangle',3,[(0,1),(1,2),(2,0)], [2,3]),
        ('reversed triangle',3,[(1,0),(1,2),(0,2)], [2,3]),
        ('square',4,[(0,1),(1,2),(2,3),(3,0)], [2,3]),
        ('square sink-source',4,[(1,0),(1,2),(3,2),(3,0)], [2,3]),
        ('triangle + bridge',4,[(0,1),(1,2),(2,0),(2,3)], [2,3]),
        ('path',4,[(0,1),(1,2),(2,3)], [2,3]),
        ('diamond',4,[(0,1),(0,2),(1,2),(1,3),(2,3)], [2,3]),
        ('K4',4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], [2]),
        ('two parallel edges',2,[(0,1),(0,1)], [2,3]),
    ]
    total=0
    for label,n,edges,primes in trials:
        for q in primes:
            a=direct(n,edges,q)
            b=by_flats(n,edges,q)
            assert a==b, (label,q,'flats',a,b)
            assert sum(a.values())==q**(n+len(edges))
            if label in {'triangle','reversed triangle','square','square sink-source'}:
                assert a==from_cycle(len(edges),q),(label,q,'cycle',a,from_cycle(len(edges),q))
            if label=='triangle + bridge':
                assert a==multiply(from_cycle(3,q),Counter({0:1,1:q*q-1})),(label,q,'bridge')
            if label=='path':
                assert a==forest(n,len(edges),1,q)
            total+=1
            print('OK',label,'q',q,'distribution',sorted(a.items()))
    print('VERIFY_OK',total,'independent direct-versus-flat comparisons')

if __name__=='__main__':checks()
