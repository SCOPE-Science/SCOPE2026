#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import combinations


def norm(v, q):
    v = tuple(x % q for x in v)
    if v == (0, 0, 0):
        raise ValueError('zero vector')
    for x in v:
        if x:
            inv = pow(x, -1, q)
            return tuple((inv*y) % q for y in v)
    raise AssertionError


def pg2(q):
    reps = sorted({norm((a,b,c),q) for a in range(q) for b in range(q) for c in range(q) if (a,b,c)!=(0,0,0)})
    pts = reps
    lines = reps[:]  # coefficient triples for ax+by+cz=0
    inc = {(i,j) for i,p in enumerate(pts) for j,l in enumerate(lines)
           if sum(p[k]*l[k] for k in range(3)) % q == 0}
    return pts, lines, inc


def graph_data(q):
    pts, lines, inc = pg2(q)
    N = q*q+q+1
    assert len(pts)==len(lines)==N
    assert len(inc)==N*(q+1)
    for i in range(N):
        assert sum(1 for a,b in inc if a==i)==q+1
        assert sum(1 for a,b in inc if b==i)==q+1
    for a,b in combinations(range(N),2):
        assert sum(1 for j in range(N) if (a,j) in inc and (b,j) in inc)==1
        assert sum(1 for i in range(N) if (i,a) in inc and (i,b) in inc)==1
    n=2*N
    adj=[set() for _ in range(n)]
    for i,j in inc:
        u=i; v=N+j
        adj[u].add(v); adj[v].add(u)
    dist=[]
    for s in range(n):
        d=[None]*n; d[s]=0; Q=deque([s])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if d[v] is None:
                    d[v]=d[u]+1; Q.append(v)
        assert None not in d
        dist.append(d)
    assert max(max(row) for row in dist)==3
    for a,b in combinations(range(n),2):
        if a<N and b<N: assert dist[a][b]==2
        elif a>=N and b>=N: assert dist[a][b]==2
        else:
            p=a if a<N else b
            l=(b-N) if a<N else (a-N)
            assert dist[a][b] == (1 if (p,l) in inc else 3)
    return N, inc, adj, dist


def maximal_cliques_compat(dist, r=2):
    n=len(dist)
    neigh=[{j for j in range(n) if j!=i and dist[i][j]<=r} for i in range(n)]
    out=[]
    def bk(R,P,X):
        if not P and not X:
            out.append(frozenset(R)); return
        union=P|X
        u=max(union, key=lambda z:len(P&neigh[z])) if union else None
        cand=P-(neigh[u] if u is not None else set())
        for v in list(cand):
            bk(R|{v}, P&neigh[v], X&neigh[v])
            P.remove(v); X.add(v)
    bk(set(), set(range(n)), set())
    return set(out)


def expected_facets(q,N,inc):
    P=frozenset(range(N)); L=frozenset(range(N,2*N))
    fs={P,L}
    for j in range(N):
        fs.add(frozenset([N+j]+[i for i in range(N) if (i,j) in inc]))
    for i in range(N):
        fs.add(frozenset([i]+[N+j for j in range(N) if (i,j) in inc]))
    return fs


def all_faces(facets):
    faces=set()
    for F in facets:
        arr=sorted(F)
        for k in range(1,len(arr)+1):
            for s in combinations(arr,k): faces.add(s)
    return faces


def rank_f2(columns):
    piv={}
    rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; rank+=1; break
    return rank


def homology_f2(faces):
    by=defaultdict(list)
    for f in faces: by[len(f)-1].append(f)
    for d in by: by[d].sort()
    maxd=max(by)
    ranks={}
    for d in range(1,maxd+1):
        rows={f:i for i,f in enumerate(by[d-1])}
        cols=[]
        for s in by[d]:
            x=0
            for t in combinations(s,d): x |= 1<<rows[t]
            cols.append(x)
        ranks[d]=rank_f2(cols)
    betti=[]
    for d in range(maxd+1):
        dim=len(by[d]); rd=ranks.get(d,0); rup=ranks.get(d+1,0)
        betti.append(dim-rd-rup)
    return [len(by[d]) for d in range(maxd+1)], [ranks.get(d,0) for d in range(1,maxd+1)], betti


def check(q):
    N,inc,adj,dist=graph_data(q)
    exp=expected_facets(q,N,inc)
    got=maximal_cliques_compat(dist,2)
    assert got==exp, (q, len(got), len(exp), got^exp)
    faces=all_faces(exp)
    fvec,ranks,betti=homology_f2(faces)
    assert betti[0]==1
    assert betti[1]==0
    assert betti[2]==q**3
    assert all(x==0 for x in betti[3:])
    # Scale 1 is the connected incidence graph: beta1=E-V+1=q^3.
    assert len(inc)-2*N+1 == q**3
    # U and V from the proof intersect exactly in the incidence graph.
    Ufac=[frozenset(range(N))] + [frozenset([N+j]+[i for i in range(N) if (i,j) in inc]) for j in range(N)]
    Vfac=[frozenset(range(N,2*N))] + [frozenset([i]+[N+j for j in range(N) if (i,j) in inc]) for i in range(N)]
    UF=all_faces(Ufac); VF=all_faces(Vfac); inter=UF&VF
    expected_inter={(i,) for i in range(2*N)} | {tuple(sorted((i,N+j))) for i,j in inc}
    assert inter==expected_inter
    return N,len(faces),fvec,ranks,betti


def main():
    r2=check(2)
    r3=check(3)
    assert r2[0]==7 and r3[0]==13
    assert r2[1]==331
    # q=3 count is a useful independent finite stress test of the general proof.
    assert r3[1]==16720
    print('q=2:', r2)
    print('q=3:', r3)
    print('VERIFY_OK')

if __name__=='__main__': main()
