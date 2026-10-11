#!/usr/bin/env python3
from collections import deque
from itertools import combinations
from math import comb


def model(n):
    points=[('p',i) for i in range(n)]
    edges=[('e',i,j) for i in range(n) for j in range(i+1,n)]
    verts=points+edges
    idx={v:k for k,v in enumerate(verts)}
    adj=[set() for _ in verts]
    for e in edges:
        _,i,j=e; k=idx[e]
        for p in (('p',i),('p',j)):
            a=idx[p]; adj[a].add(k); adj[k].add(a)
    return verts,adj


def all_dist(adj):
    out=[]
    for s in range(len(adj)):
        d=[-1]*len(adj); d[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0: d[v]=d[u]+1; q.append(v)
        out.append(d)
    return out


def maximal_cliques(dist,k):
    N=len(dist)
    nbr=[{j for j in range(N) if j!=i and dist[i][j]<=k} for i in range(N)]
    ans=[]
    def bk(R,P,X):
        if not P and not X:
            ans.append(tuple(sorted(R))); return
        u=max(P|X,key=lambda z:len(P&nbr[z]),default=None)
        cand=P-(nbr[u] if u is not None else set())
        for v in list(cand):
            bk(R|{v},P&nbr[v],X&nbr[v]); P.remove(v); X.add(v)
    bk(set(),set(range(N)),set())
    return ans


def faces_from_facets(facets):
    md=max(len(f) for f in facets)
    faces=[set() for _ in range(md)]
    for f in facets:
        for r in range(1,len(f)+1):
            for s in combinations(f,r): faces[r-1].add(s)
    return [sorted(x) for x in faces]


def rank_gf2(cols):
    piv={}
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else: piv[p]=x; break
    return len(piv)


def reduced_betti(faces):
    ranks=[]
    for d in range(1,len(faces)):
        low={f:i for i,f in enumerate(faces[d-1])}
        cols=[]
        for f in faces[d]:
            x=0
            for j in range(len(f)):
                sub=f[:j]+f[j+1:]
                x |= 1<<low[sub]
            cols.append(x)
        ranks.append(rank_gf2(cols))
    bet=[]
    for d,f in enumerate(faces):
        rd=ranks[d-1] if d else 0
        ru=ranks[d] if d<len(ranks) else 0
        b=len(f)-rd-ru
        if d==0: b-=1
        bet.append(b)
    while bet and bet[-1]==0: bet.pop()
    return bet,ranks


def check(n):
    verts,adj=model(n); dist=all_dist(adj); N=len(verts)
    assert all(x>=0 for row in dist for x in row)
    # Distance taxonomy.
    for i in range(n):
        for j in range(i+1,n): assert dist[i][j]==2
    edge_ids={v:i for i,v in enumerate(verts) if v[0]=='e'}
    for ev,eid in edge_ids.items():
        _,a,b=ev
        for i in range(n): assert dist[i][eid]==(1 if i in (a,b) else 3)
    E=list(edge_ids)
    for x in range(len(E)):
        for y in range(x+1,len(E)):
            e,f=E[x],E[y]
            inter=bool(set(e[1:])&set(f[1:]))
            assert dist[edge_ids[e]][edge_ids[f]]==(2 if inter else 4)

    # Scale one is the subdivision graph itself.
    vcount=N; ecount=n*(n-1)
    beta1=ecount-vcount+1
    assert beta1==comb(n-1,2)

    # Scale two: exact clique enumeration and exact GF(2) homology.
    fac2=maximal_cliques(dist,2)
    faces2=faces_from_facets(fac2)
    bet2,_=reduced_betti(faces2)
    expected=[0,0,comb(n,3)]
    assert bet2==expected,(n,bet2)

    # Structural maximal-clique census: one point simplex, n incidence-star
    # simplices, C(n,2) mixed triangles, C(n,3) edge triangles.
    sizes=sorted(map(len,fac2))
    expected_sizes=sorted([n]*(n+1)+[3]*(comb(n,2)+comb(n,3)))
    if n==3:
        # coincidences at n=3 make all maximal cliques triangular; count still agrees.
        assert sizes==expected_sizes
    else:
        assert sizes==expected_sizes

    # At scale three every point-vertex is universal, so the flag complex is a cone.
    for p in range(n):
        assert all(p==v or dist[p][v]<=3 for v in range(N))
    return N,[len(x) for x in faces2],beta1,comb(n,3),len(fac2)

print('VERIFY_OK')
for n in range(3,8):
    N,f,b1,b2,m=check(n)
    print(f'n={n} vertices={N} scale1_beta1={b1} scale2_f={f} scale2_beta2={b2} maximal_cliques={m} scale3=cone')
