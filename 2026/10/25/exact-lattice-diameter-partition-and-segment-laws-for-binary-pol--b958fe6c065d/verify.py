"""Independent exact finite checks of diameter-segment and partition formulas.
Run: python verify.py.  No external dependencies.
"""
from math import gcd,comb
from itertools import product,combinations

def hypersimplex_points(d,k,n):
    return [p for p in product(range(n+1),repeat=d) if sum(p)==k*n]

def closed_count(d,k,n):
    out=0
    for s in range(1,min(k,d-k)+1):
        m=d-2*s; j=k-s
        c=sum(sum(t)==j*n for t in product(range(n+1),repeat=m))
        out+=comb(d,s)*comb(d-s,s)*c
    assert out%2==0
    return out//2

def brute_count(d,k,n):
    pts=hypersimplex_points(d,k,n)
    diameter=0; num=0
    for x,y in combinations(pts,2):
        g=0
        for a,b in zip(x,y):g=gcd(g,abs(a-b))
        if g>diameter:diameter=g;num=1
        elif g==diameter:num+=1
    return diameter,num,len(pts)

def residue_clique_stats(d,k,n):
    groups={}
    for x in hypersimplex_points(d,k,n):
        r=tuple(a%n for a in x)
        groups[r]=groups.get(r,0)+1
    edge_count=sum(s*(s-1)//2 for s in groups.values())
    max_clique=max(groups.values())
    # Independent explicit matching clique count, from residue decomposition.
    for r,size in groups.items():
        z=r.count(0);h=sum(r)//n
        assert sum(r)%n==0
        expected=comb(z,k-h) if 0<=k-h<=z else 0
        assert size==expected,(d,k,n,r,size,expected)
    return edge_count,max_clique,len(groups)

def checker():
    trials=0
    for d in range(2,8):
        for k in range(1,d):
            for n in range(1,4):
                closed=closed_count(d,k,n)
                diameter,brute,pts=brute_count(d,k,n)
                edge_count,clique,components=residue_clique_stats(d,k,n)
                assert diameter==n,(d,k,n,diameter)
                assert brute==closed==edge_count,(d,k,n,brute,closed,edge_count)
                assert clique==comb(d,k),(d,k,n,clique)
                trials+=1
    print('HYPERSIMPLEX_EXACT_OK cases=',trials)
if __name__=='__main__':checker()

def tetra_points(n):
    return [(a,b,c) for a,b,c in product(range(n+1),repeat=3)
            if a+b+c<=2*n and a<=b+c and b<=a+c and c<=a+b]

def tetra_brute(n):
    pts=tetra_points(n);counts={}
    dmax=0;edges=0
    for a,b in combinations(pts,2):
        dif=[v-u for u,v in zip(a,b)]
        g=0
        for x in dif:g=gcd(g,abs(x))
        if g>dmax:dmax=g;edges=1
        elif g==dmax:edges+=1
        if g==n:
            u=tuple(x//n for x in dif)
            if next(z for z in u if z)!=1:u=tuple(-z for z in u)
            counts[u]=counts.get(u,0)+1
    assert dmax==n and edges==6+3*(n%2==0),(n,dmax,edges)
    assert len(counts)==6+3*(n%2==0),(n,counts)
    return len(pts)

if __name__=='__main__':
    for n in range(1,15): tetra_brute(n)
    print('PARITY_TETRA_EXACT_OK cases=',14)
