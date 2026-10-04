import itertools, json
import networkx as nx

EXPECTED_TYPES = {4:1, 6:2, 8:5}

def truncation(G):
    H=nx.Graph()
    for v in G:
        ns=sorted(G.neighbors(v))
        assert len(ns)==3
        for u in ns: H.add_node((v,u))
        for a,b in itertools.combinations(ns,2): H.add_edge((v,a),(v,b))
    for u,v in G.edges(): H.add_edge((u,v),(v,u))
    return H

def conflict_graph(H):
    E=list(H.edges())
    idx={frozenset(e):i for i,e in enumerate(E)}
    L=nx.line_graph(H)
    F=nx.Graph(); F.add_nodes_from(range(len(E)))
    for e in L:
        seen=set(L[e])
        for f in L[e]: seen.update(L[f])
        i=idx[frozenset(e)]
        for f in seen:
            if f!=e: F.add_edge(i,idx[frozenset(f)])
    return F,E

def six_coloring(F):
    n=F.number_of_nodes(); adj=[set(F.neighbors(i)) for i in range(n)]
    col=[-1]*n; sat=[set() for _ in range(n)]; deg=[len(a) for a in adj]
    def rec(done):
        if done==n:return col.copy()
        v=max((i for i in range(n) if col[i]<0), key=lambda i:(len(sat[i]),deg[i]))
        for c in range(6):
            if c in sat[v]:continue
            col[v]=c; changed=[]; ok=True
            for w in adj[v]:
                if col[w]<0 and c not in sat[w]:
                    sat[w].add(c); changed.append(w)
                    if len(sat[w])==6: ok=False; break
            if ok:
                ans=rec(done+1)
                if ans is not None:return ans
            for w in changed:sat[w].remove(c)
            col[v]=-1
        return None
    return rec(0)

def generate_types(n):
    rem=[3]*n; E=[]; buckets={}; reps=[]; labeled_connected=0
    def consider():
        nonlocal labeled_connected
        G=nx.Graph();G.add_nodes_from(range(n));G.add_edges_from(E)
        if not nx.is_connected(G):return
        labeled_connected+=1
        h=nx.weisfeiler_lehman_graph_hash(G)
        for H in buckets.get(h,[]):
            if nx.is_isomorphic(G,H): return
        buckets.setdefault(h,[]).append(G.copy());reps.append(G.copy())
    def rec(v):
        while v<n and rem[v]==0:v+=1
        if v==n:
            if all(x==0 for x in rem):consider()
            return
        need=rem[v]
        cands=[u for u in range(v+1,n) if rem[u]>0]
        if len(cands)<need:return
        for ns in itertools.combinations(cands,need):
            rem[v]=0
            for u in ns:rem[u]-=1;E.append((v,u))
            seq=[rem[i] for i in range(v+1,n)]
            if all(x>=0 for x in seq) and sum(seq)%2==0 and nx.is_graphical(seq,method='hh'):
                rec(v+1)
            for u in reversed(ns):E.pop();rem[u]+=1
            rem[v]=need
    rec(0)
    return labeled_connected,reps

def local_k6_check(G,H,F,E):
    edge_index={frozenset(e):i for i,e in enumerate(E)}
    for v in G:
        ns=list(G.neighbors(v))
        local=[]
        for u in ns: local.append(edge_index[frozenset(((v,u),(u,v)))])
        for a,b in itertools.combinations(ns,2): local.append(edge_index[frozenset(((v,a),(v,b)))])
        assert len(local)==6
        for a,b in itertools.combinations(local,2): assert F.has_edge(a,b)

def main():
    rows=[]
    for n in (4,6,8):
        labeled,reps=generate_types(n)
        assert len(reps)==EXPECTED_TYPES[n], (n,len(reps))
        codes=[]
        for G in reps:
            H=truncation(G); F,E=conflict_graph(H)
            local_k6_check(G,H,F,E)
            sol=six_coloring(F)
            assert sol is not None
            assert all(sol[u]!=sol[v] for u,v in F.edges())
            codes.append(nx.to_graph6_bytes(G,header=False).decode().strip())
        rows.append({'base_order':n,'connected_labeled_generated':labeled,'isomorphism_types':len(reps),'graph6':sorted(codes),'all_truncations_strong_6_edge_colorable':True})
    print(json.dumps({'networkx':nx.__version__,'rows':rows,'conclusion':'Every connected simple cubic base graph on at most 8 vertices has truncation of strong chromatic index exactly 6; any simple-base counterexample has at least 10 base vertices and hence at least 30 truncation vertices.'},sort_keys=True))
if __name__=='__main__':main()
