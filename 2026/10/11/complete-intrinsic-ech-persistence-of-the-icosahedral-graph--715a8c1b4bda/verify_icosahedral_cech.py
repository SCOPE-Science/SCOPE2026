#!/usr/bin/env python3
"""Self-contained exact verifier for the icosahedral graph's intrinsic Čech filtration.

Usage: python3 verify_icosahedral_cech.py
Reads the adjacent MORSE_CERTIFICATE.json. Python 3.9+ standard library only.
"""
import json
from collections import Counter, deque
from pathlib import Path

N = 12

def graph_edges():
    edges = set()
    def edge(a, b):
        assert a != b and 0 <= a < N and 0 <= b < N
        edges.add((min(a,b), max(a,b)))
    for i in range(5):
        a, b = 2+i, 7+i
        edge(0, a)
        edge(1, b)
        edge(a, 2+(i+1)%5)
        edge(b, 7+(i+1)%5)
        edge(a, b)
        edge(a, 7+(i-1)%5)
    return sorted(edges)


def graph_data():
    E = graph_edges()
    adj = [set() for _ in range(N)]
    for a,b in E:
        adj[a].add(b);adj[b].add(a)
    dist=[]
    for a in range(N):
        ds=[-1]*N;ds[a]=0;q=deque([a])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if ds[w]<0:ds[w]=ds[v]+1;q.append(w)
        assert min(ds)>=0
        dist.append(ds)
    return E,adj,dist


def complexes():
    E,adj,d=graph_data()
    facets={}
    facets[0]=[1<<i for i in range(N)]
    facets[1]=[(1<<u)|(1<<v) for u,v in E]
    for r in (2,4):
        facets[r] = [sum(1<<j for j in range(N) if d[i][j]<=r//2) for i in range(N)]
    for r in (3,5):
        facets[r] = [sum(1<<j for j in range(N) if min(d[u][j],d[v][j])<=(r-1)//2) for u,v in E]
    out={}
    for r in range(6):
        F=sorted(set(facets[r]));S=set()
        for f in F:
            s=f
            while s: S.add(s);s=(s-1)&f
        out[r]=(F,S)
    return out


def all_hasse_edges(S):
    """Pairs (proper face, codimension-one coface), enumerated exactly once."""
    for t in S:
        bits=t
        while bits:
            b=bits&-bits;bits-=b
            s=t^b
            if s: assert s in S;yield s,t


def check_matching(r,S,c):
    pairs=[(int(a),int(b)) for a,b in c['pairs']]
    critical=[int(x) for x in c['critical']]
    used=set()
    assert len(critical)==len(set(critical))
    for x in critical:
        assert x in S and x not in used
        used.add(x)
    for s,t in pairs:
        assert s in S and t in S and s!=t
        assert (s&t)==s and t.bit_count()==s.bit_count()+1
        assert s not in used and t not in used
        used.add(s);used.add(t)
    assert used==S
    match=set(pairs)
    edges=list(all_hasse_edges(S))
    assert len(match)==len(pairs)
    assert match.issubset(set(edges))
    # Forman orientation: unmatched edge faces downward; matching edges upward.
    outgoing={x:[] for x in S}; indegree={x:0 for x in S}
    for s,t in edges:
        a,b=(s,t) if (s,t) in match else (t,s)
        outgoing[a].append(b);indegree[b]+=1
    queue=deque(x for x in S if indegree[x]==0)
    count=0
    while queue:
        s=queue.popleft();count+=1
        for t in outgoing[s]:
            indegree[t]-=1
            if indegree[t]==0:queue.append(t)
    assert count==len(S), ('gradient cycle detected',r,count,len(S))
    crit_dims=Counter(x.bit_count()-1 for x in critical)
    expected={2:Counter({0:1,2:1}),3:Counter({0:1,4:10})}[r]
    assert crit_dims==expected
    assert len(pairs)*2+len(critical)==len(S)
    print('MORSE',r,'faces',len(S),'pairs',len(pairs),'Hasse',len(edges),'critical',dict(sorted(crit_dims.items())),'acyclic=yes')


def mod2_boundary_ranks(S):
    D={}
    for s in S:D.setdefault(s.bit_count()-1,[]).append(s)
    ranks={}
    for k in range(1,max(D)+1):
        lower_index={s:i for i,s in enumerate(D[k-1])}
        echelon={}
        for upper in D[k]:
            col=0;bits=upper
            while bits:
                b=bits&-bits;bits-=b
                col^=1<<lower_index[upper^b]
            while col:
                pivot=col.bit_length()-1
                if pivot in echelon:col^=echelon[pivot]
                else:echelon[pivot]=col;break
        ranks[k]=len(echelon)
    betti={k:len(v)-ranks.get(k,0)-ranks.get(k+1,0) for k,v in D.items()}
    betti[0]-=1
    return ranks,{k:v for k,v in sorted(betti.items()) if v}


def main():
    E,adj,d=graph_data()
    assert len(E)==30 and all(len(a)==5 for a in adj)
    triangles=sum(1 for a in range(N) for b in range(a+1,N) for c in range(b+1,N) if b in adj[a] and c in adj[b] and a in adj[c])
    assert triangles==20 and max(map(max,d))==3
    assert [sum(x==3 for x in row) for row in d]==[1]*N
    C=complexes()
    assert [len(C[r][0]) for r in range(6)]==[12,30,12,30,12,1]
    assert [len(C[r][1]) for r in range(6)]==[12,42,446,2037,4094,4095]
    for r in range(5):assert C[r][1].issubset(C[r+1][1])
    assert C[4][1]==set(range(1,(1<<N)-1))
    assert C[5][1]==set(range(1,1<<N))
    certificate=json.loads(Path(__file__).with_name('MORSE_CERTIFICATE.json').read_text(encoding='utf-8'))
    assert certificate['format']=='icosahedral_cech_gradient_certificate_v1'
    for r,expected_faces,expected_betti in [(2,[12,60,140,150,72,12],{2:1}),(3,[12,66,220,465,612,452,180,30],{4:10})]:
        S=C[r][1]
        F=[sum(x.bit_count()==k for x in S) for k in range(1,max(x.bit_count() for x in S)+1)]
        assert F==expected_faces,(r,F)
        check_matching(r,S,certificate['scales'][str(r)])
        ranks,betti=mod2_boundary_ranks(S)
        assert betti==expected_betti,(r,betti)
        assert sum((-1)**k*F[k] for k in range(len(F)))==1+sum((-1)**dim*n for dim,n in expected_betti.items())
        print('CHAIN',r,'fvector',F,'boundary_ranks',ranks,'reduced_mod2_betti',betti)
    assert len(E)-N+1==19
    print('FILTRATION', 'r0=12 points; r1=wedge19 S1; r2=S2; r3=wedge10 S4; r4=S10; r5=point')
    print('BARCODES','reduced H0:11*[0,1), H1:19*[1,2), H2:[2,3), H4:10*[3,4), H10:[4,5)')
    print('VERIFY_OK')

if __name__=='__main__':main()
