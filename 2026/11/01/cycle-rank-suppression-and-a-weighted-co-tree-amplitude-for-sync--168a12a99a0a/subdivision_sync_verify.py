"""Finite-lattice cross-checks for the edge-subdivision synchronization law.
Reproduces exact circulation probabilities by two independent combinatorial counts.
Python 3 standard library only.
"""
from collections import defaultdict, deque
from itertools import product
from math import comb, pi, sqrt
from fractions import Fraction


def basis(vertices, edges):
    parent = list(range(vertices))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    tree = []
    chords = []
    for j,(u,v) in enumerate(edges):
        a,b=find(u),find(v)
        if a!=b:
            parent[a]=b;tree.append(j)
        else:
            chords.append(j)
    adj=[[] for _ in range(vertices)]
    for j in tree:
        u,v=edges[j];adj[u].append((v,j,+1));adj[v].append((u,j,-1))
    B=[]
    for j in chords:
        u,v=edges[j];q=deque([(v,[])]);seen={v};path=None
        while q:
            x,p=q.popleft()
            if x==u:path=p;break
            for y,k,sgn in adj[x]:
                if y not in seen:seen.add(y);q.append((y,p+[(k,sgn)]))
        assert path is not None
        b=[0]*len(edges);b[j]=1
        for k,sgn in path:b[k]=sgn
        B.append(b)
    assert len(B)==len(edges)-vertices+1
    return B,tree


def coefficients(length):
    d={0:1}
    for _ in range(length):
        e=defaultdict(int)
        for s,c in d.items():
            for shift in (-1,0,1):e[s+shift]+=c
        d=dict(e)
    return d


def exact_probability(vertices,edges,lengths):
    B,_=basis(vertices,edges)
    r=len(B)
    d={(0,)*r:1}
    for j,L in enumerate(lengths):
        e=defaultdict(int)
        col=tuple(row[j] for row in B)
        for vec,cnt in d.items():
            for s,mult in coefficients(L).items():
                v=tuple(x+s*y for x,y in zip(vec,col))
                e[v]+=cnt*mult
        d=dict(e)
    raw=d[(0,)*r]
    return Fraction((3**r)*raw,3**sum(lengths))


def expanded(vertices,edges,lengths):
    paths=[];k=vertices
    for (u,v),L in zip(edges,lengths):
        points=[u]+list(range(k,k+L-1))+[v]
        k+=L-1
        paths.append(points)
    return k, paths


def direct_probability(vertices,edges,lengths):
    n,paths=expanded(vertices,edges,lengths)
    assert n<=11
    ok=0
    for x in product(range(3),repeat=n):
        totals=[]
        for path in paths:
            total=0
            for a,b in zip(path,path[1:]):
                total+=(x[b]-x[a]+1)%3-1
            totals.append(total)
        B,_=basis(vertices,edges)
        if all(sum(b[j]*totals[j] for j in range(len(edges)))==0 for b in B):ok+=1
    return Fraction(ok,3**n)


def weighted_cotrees(vertices,edges,lengths):
    m=len(edges);ans=0
    from itertools import combinations
    for selected in combinations(range(m),vertices-1):
        p=list(range(vertices))
        def root(a):
            while p[a]!=a:a=p[a]
            return a
        good=True
        for j in selected:
            u,v=edges[j];u,v=root(u),root(v)
            if u==v:good=False;break
            p[u]=v
        if good and len({root(x) for x in range(vertices)})==1:
            prod=1
            for j in range(m):
                if j not in selected:prod*=lengths[j]
            ans+=prod
    return ans


def main():
    graphs=[('triangle',3,[(0,1),(1,2),(0,2)]),
            ('diamond',4,[(0,1),(0,2),(1,2),(1,3),(2,3)]),
            ('K4',4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])]
    checks=0
    for name,v,edges in graphs:
        for L in (1,2):
            length=[L]*len(edges)
            p=exact_probability(v,edges,length)
            q=direct_probability(v,edges,length)
            assert p==q,(name,L,p,q)
            r=len(edges)-v+1
            K=weighted_cotrees(v,edges,[1]*len(edges))
            asymp=(27/(4*pi*L))**(r/2)/sqrt(K)
            print(name,'L',L,'r',r,'cotree',K,'exact',str(p),'asymptotic',round(asymp,7),'ratio',round(float(p)/asymp,6))
            checks+=1
    print('SUBDIVISION_SYNC_VERIFY_OK',checks)
if __name__=='__main__':main()
