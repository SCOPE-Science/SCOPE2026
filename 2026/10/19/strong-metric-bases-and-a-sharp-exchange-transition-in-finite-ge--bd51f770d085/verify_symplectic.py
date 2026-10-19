#!/usr/bin/env python3
"""Standalone finite checks for strong metric bases of symplectic GQ(q,q), q=2,3.
Only uses Python standard library. Prints a deterministic JSON certificate.
"""
import itertools, json, hashlib, collections
from collections import deque

def check(q):
    assert q in (2,3)
    def norm(v):
        j=next(i for i,a in enumerate(v) if a%q)
        a=pow(v[j],-1,q)
        return tuple(a*x%q for x in v)
    pts=sorted({norm(v) for v in itertools.product(range(q),repeat=4) if any(v)})
    pidx={p:i for i,p in enumerate(pts)}
    def wedge(u,v):return (u[0]*v[1]-u[1]*v[0]+u[2]*v[3]-u[3]*v[2])%q
    line_set=set()
    for ia,u in enumerate(pts):
        for v in pts[ia+1:]:
            if wedge(u,v)==0:
                L=frozenset(pidx[norm(tuple((a*u[k]+b*v[k])%q for k in range(4)))]
                    for a,b in itertools.product(range(q),repeat=2) if a or b)
                assert len(L)==q+1
                line_set.add(tuple(sorted(L)))
    lines=sorted(line_set); Np=len(pts); Nl=len(lines); N=Np+Nl
    assert Np==Nl==(q+1)*(q*q+1)
    assert len(set(lines))==Nl
    adj=[set() for _ in range(N)]
    through=[set() for _ in range(Np)]
    for j,L in enumerate(lines):
        for i in L:adj[i].add(Np+j);adj[Np+j].add(i);through[i].add(j)
    assert all(len(adj[i])==q+1 for i in range(N))
    # GQ axiom: unique collinear point on any nonincident line.
    for i in range(Np):
        for j,L in enumerate(lines):
            if i not in L:
                assert sum(any(z in through[i] for z in through[x]) for x in L)==1
    def distances(a):
        dist=[-1]*N;dist[a]=0;queue=deque([a])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if dist[w]==-1:dist[w]=dist[v]+1;queue.append(w)
        assert min(dist)>=0
        return dist
    dist=[distances(i) for i in range(N)]
    assert max(max(d) for d in dist)==4
    mmd=set()
    for i in range(N):
        for j in range(i+1,N):
            if all(dist[w][j]<=dist[i][j] for w in adj[i]) and all(dist[i][w]<=dist[i][j] for w in adj[j]):mmd.add((i,j))
    predicted={(i,j) for i in range(N) for j in range(i+1,N) if dist[i][j]==4}
    assert mmd==predicted
    # Classify maximum independent sets directly from incidence and check vertex-cover property.
    pt_lines={frozenset(L) for L in lines};line_pencils={frozenset(through[i]) for i in range(Np)}
    assert len(pt_lines)==Nl and len(line_pencils)==Np
    pt_cliques=set()
    for S in itertools.combinations(range(Np),q+1):
        if all(dist[i][j]==2 for i,j in itertools.combinations(S,2)):pt_cliques.add(frozenset(S))
    assert pt_cliques==pt_lines
    line_cliques=set()
    for S in itertools.combinations(range(Nl),q+1):
        if all(dist[Np+i][Np+j]==2 for i,j in itertools.combinations(S,2)):line_cliques.add(frozenset(S))
    assert line_cliques==line_pencils
    bases=[]
    for L in lines:
        for pen in sorted(line_pencils,key=lambda x:tuple(sorted(x))):
            omit=set(L)|{Np+j for j in pen}
            assert len(omit)==2*(q+1)
            # A basis is a vertex cover of MMD graph
            assert all(not (a in omit and b in omit) for a,b in mmd)
            bases.append(frozenset(range(N))-omit)
    assert len(bases)==Nl*Np and len(set(bases))==len(bases)
    # Exchange threshold and structure calculated directly from all bases.
    costs=collections.Counter()
    adjacency=[set() for _ in bases]
    for i in range(len(bases)):
        for j in range(i+1,len(bases)):
            cost=len(bases[i]-bases[j]);assert cost==len(bases[j]-bases[i]);costs[cost]+=1
            if cost<=q:adjacency[i].add(j);adjacency[j].add(i)
    # q=s=t so exchange threshold graph is the Cartesian product of GQ point/line graphs.
    assert {len(v) for v in adjacency}=={2*q*(q+1)}
    assert sum(len(v) for v in adjacency)//2==Nl*Np*q*(q+1)
    def ecc(root):
        d=[-1]*len(bases);d[root]=0;queue=deque([root])
        while queue:
            x=queue.popleft()
            for y in adjacency[x]:
                if d[y]<0:d[y]=d[x]+1;queue.append(y)
        assert min(d)>=0
        return max(d),collections.Counter(d)
    e0,profile=ecc(0)
    assert e0==4
    assert profile[0]==1 and sum(profile.values())==len(bases)
    encoded=';'.join(','.join(map(str,sorted(b))) for b in bases).encode()
    return dict(field_order=q,points=Np,lines=Nl,vertices=N,diameter=4,mmd_pairs=len(mmd),strong_metric_dimension=q*q*(2*q+2),min_bases=len(bases),smallest_exchange=q,threshold_degree=2*q*(q+1),threshold_edges=sum(len(v) for v in adjacency)//2,threshold_diameter=e0,distance_profile=[profile[k] for k in range(e0+1)],exchange_cost_histogram={str(k):v for k,v in sorted(costs.items())},bases_sha256=hashlib.sha256(encoded).hexdigest())

if __name__=='__main__':
    print(json.dumps([check(2),check(3)],sort_keys=True,separators=(',',':')))
