"""Reproducibility checks for Rips complexes of multipartite prisms.

Python 3 standard library only; comparisons use exact graph distances and GF(2) boundaries.
"""
from collections import deque
from itertools import combinations


def graph(sizes):
    vs=[(i,j,h) for i,a in enumerate(sizes) for j in range(a) for h in (0,1)]
    adj={u:set() for u in vs}
    for u,v in combinations(vs,2):
        i,j,h=u; I,J,H=v
        if (h==H and i!=I) or (h!=H and i==I and j==J):
            adj[u].add(v);adj[v].add(u)
    return vs,adj

def distances(vs,adj):
    dist={}
    for v in vs:
        d={v:0};q=deque([v])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y]=d[x]+1;q.append(y)
        assert len(d)==len(vs)
        dist[v]=d
    return dist

def simplices(vs,dist,r):
    # Exhaustive clique enumeration, with no use of the asserted decomposition.
    faces={0:[()]}
    for i,u in enumerate(vs):
        faces.setdefault(1,[]).append((i,))
    for d in range(2,len(vs)+1):
        old=faces[d-1]
        level=[]
        for comb in combinations(range(len(vs)),d):
            if all(dist[vs[i]][vs[j]]<=r for i,j in combinations(comb,2)):
                level.append(comb)
        if not level:break
        faces[d]=level
    return faces

def binary_rank(columns):
    basis={}
    for col in columns:
        v=col
        while v:
            pivot=v.bit_length()-1
            if pivot not in basis:
                basis[pivot]=v;break
            v^=basis[pivot]
    return len(basis)

def bettis(faces):
    ks=sorted(k for k in faces if k)
    ranks={0:0,1:0}
    for k in ks[1:]:
        lower={f:j for j,f in enumerate(faces[k-1])}
        cols=[]
        for simplex in faces[k]:
            x=0
            for j in range(k):
                sub=simplex[:j]+simplex[j+1:]
                x^=1<<lower[sub]
            cols.append(x)
        ranks[k]=binary_rank(cols)
    return {d-1:len(faces[d])-ranks[d]-ranks.get(d+1,0) for d in ks}

def check(sizes,check_homology):
    vs,adj=graph(sizes)
    dists=distances(vs,adj)
    k=len(sizes); N=sum(sizes);B=1
    for a in sizes:B*=a-1
    for u,v in combinations(vs,2):
        i,j,h=u;I,J,H=v
        d=dists[u][v]
        if h==H:want=1 if i!=I else 2
        elif i!=I:want=2
        elif j==J:want=1
        else:want=3
        assert d==want,(sizes,u,v,d,want)
    assert max(x for row in dists.values() for x in row.values())==3
    # Independently verify exact scale-two square graph partition into joins of two-clique-with-matching graphs.
    for u,v in combinations(vs,2):
        i,j,h=u;I,J,H=v
        predicted=i!=I or h==H or j==J
        assert (dists[u][v]<=2)==predicted
    if check_homology:
        for r in (1,2):
            f=simplices(vs,dists,r)
            bet=bettis(f)
            expected={0:1}
            if r==1:
                expected[1]=N-1
                expected[k-1]=expected.get(k-1,0)+2*B
            elif r==2:
                expected[2*k-1]=B
            for degree,val in bet.items():
                assert val==expected.get(degree,0),(sizes,r,degree,val,expected)
            assert len(faces_summary(f))>0
    return len(vs),B

def faces_summary(f):return [(k,len(v)) for k,v in f.items()]

if __name__=='__main__':
    tests=[(2,2),(2,3),(2,4),(3,3),(2,2,2),(2,2,3)]
    for sizes in tests:
        nv,mult=check(sizes,True)
        print('exact_homology_ok',sizes,'vertices',nv,'high_rank',mult)
    for sizes in [(2,3,4),(2,2,2,2),(3,3,3),(2,4,5),(2,2,2,3),(2,2,2,2,2)]:
        nv,mult=check(sizes,False)
        print('distance_partition_ok',sizes,'vertices',nv,'high_rank',mult)
    print('VERIFY_OK')
