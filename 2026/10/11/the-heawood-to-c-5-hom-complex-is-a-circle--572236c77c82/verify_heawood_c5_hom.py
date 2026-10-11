#!/usr/bin/env python3
from collections import Counter, deque
import json
from pathlib import Path

EXPECTED = {
    "vertex_count": 14,
    "edge_count": 21,
    "homomorphism_count": 3300,
    "reconfiguration_edge_count": 11340,
    "reconfiguration_component_count": 1,
    "reconfiguration_diameter": 35,
    "reconfiguration_radius": 35,
    "degree_histogram": {"4": 210, "5": 700, "6": 840, "8": 980, "9": 420, "11": 140, "14": 10},
    "representative": [0,0,0,0,0,0,0,1,1,1,1,1,1,1],
    "orientation_topological_order": [0,1,2,3,4,5,6,7,8,9,11,10,12,13]
}

def heawood_graph():
    # 0..6 are Fano points; 7+i is line i; point j lies on line i iff j-i in {0,1,3} mod 7.
    edges=[]
    for i in range(7):
        for d in (0,1,3):
            edges.append(((i+d)%7, 7+i))
    adj=[set() for _ in range(14)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    assert len(edges)==EXPECTED["edge_count"]
    assert all(len(a)==3 for a in adj)
    # Fano pair condition: each two points occur on exactly one common line.
    for a in range(7):
        for b in range(a+1,7):
            assert len(adj[a] & adj[b]) == 1
    return edges, adj

def enumerate_homs(adj):
    order=sorted(range(14), key=lambda u:(-len(adj[u]),u))
    f=[-1]*14; homs=[]
    def rec(t):
        if t==14:
            homs.append(tuple(f)); return
        u=order[t]
        for c in range(5):
            if all(f[v] < 0 or (f[v]-c)%5 in (1,4) for v in adj[u]):
                f[u]=c; rec(t+1); f[u]=-1
    rec(0)
    assert len(homs)==EXPECTED["homomorphism_count"]
    return homs

def reconfiguration_graph(homs, adj):
    index={h:i for i,h in enumerate(homs)}
    nbr=[set() for _ in homs]
    for i,h0 in enumerate(homs):
        h=list(h0)
        for u in range(14):
            old=h[u]
            for c in range(5):
                if c==old: continue
                if all((h[v]-c)%5 in (1,4) for v in adj[u]):
                    h[u]=c
                    j=index[tuple(h)]
                    h[u]=old
                    if i!=j:
                        nbr[i].add(j); nbr[j].add(i)
    m=sum(map(len,nbr))//2
    assert m==EXPECTED["reconfiguration_edge_count"]
    hist=Counter(map(len,nbr))
    assert {str(k):v for k,v in sorted(hist.items())}==EXPECTED["degree_histogram"]
    return nbr

def bfs(nbr,s):
    dist=[-1]*len(nbr); dist[s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for v in nbr[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1; q.append(v)
    return dist

def verify_connectivity_and_diameter(nbr):
    d0=bfs(nbr,0)
    assert all(d>=0 for d in d0)
    ecc=[]
    for s in range(len(nbr)):
        ds=bfs(nbr,s)
        assert all(d>=0 for d in ds)
        ecc.append(max(ds))
    assert max(ecc)==EXPECTED["reconfiguration_diameter"]
    assert min(ecc)==EXPECTED["reconfiguration_radius"]
    return max(ecc), min(ecc)

def verify_orientation(edges):
    f=tuple(EXPECTED["representative"])
    out=[[] for _ in range(14)]; indeg=[0]*14
    for u,v in edges:
        if (f[v]-f[u])%5==1: a,b=u,v
        elif (f[u]-f[v])%5==1: a,b=v,u
        else: raise AssertionError("representative is not a homomorphism")
        out[a].append(b); indeg[b]+=1
    q=deque(sorted(u for u in range(14) if indeg[u]==0)); topo=[]
    while q:
        u=q.popleft(); topo.append(u)
        for v in sorted(out[u]):
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    assert len(topo)==14
    assert topo==EXPECTED["orientation_topological_order"]
    return topo

def main():
    edges,adj=heawood_graph()
    homs=enumerate_homs(adj)
    assert tuple(EXPECTED["representative"]) in set(homs)
    nbr=reconfiguration_graph(homs,adj)
    diam,rad=verify_connectivity_and_diameter(nbr)
    topo=verify_orientation(edges)
    cert=json.loads(Path(__file__).with_name("verification_data.json").read_text())
    assert cert==EXPECTED
    print("vertices",len(adj))
    print("edges",len(edges))
    print("homomorphisms",len(homs))
    print("reconfiguration_edges",sum(map(len,nbr))//2)
    print("components",1)
    print("diameter",diam)
    print("radius",rad)
    print("degree_histogram",dict(sorted(Counter(map(len,nbr)).items())))
    print("orientation_topological_order",topo)
    print("HEAWOOD_C5_HOM_VERIFY_OK")
if __name__=="__main__": main()
