"""Separate leaf-block construction and orbit search, exact through order 9.
Uses networkx only for unmarked graph-isomorphism deduplication, not orbit tests.
"""
from collections import Counter, defaultdict
import networkx as nx

def attach(g,at,k):
    h=g.copy();old=len(h);h.add_nodes_from(range(old,old+k))
    if k==1: h.add_edge(at,old)
    else:
        h.add_edge(at,old);h.add_edge(old+k-1,at)
        for i in range(k-1):h.add_edge(old+i,old+i+1)
    return h

def classes(g):
    n=len(g); adj=[set(g[v]) for v in range(n)]
    return adj

def wl(adj,root):
    n=len(adj);col=[int(v==root) for v in range(n)]
    while True:
        key=[(col[v],tuple(sorted(col[w] for w in adj[v]))) for v in range(n)]
        palette={v:i for i,v in enumerate(sorted(set(key)))}
        nxt=[palette[k] for k in key]
        if len(set(nxt))==len(set(col)):return nxt
        col=nxt

def has_root_automorphism(adj,root,a,b,stable):
    n=len(adj)
    if stable[a]!=stable[b]:return False
    degree=[len(s) for s in adj]
    # valid automorphisms must preserve both the distinguished root and stable colors
    if a==root and b!=root or b==root and a!=root:return False
    mapping={root:root};used={root}
    if a!=root:
        mapping[a]=b;used.add(b)
    def good(x,y):
        if y in used or stable[x]!=stable[y] or degree[x]!=degree[y]:return False
        return all(((u in adj[x])==(z in adj[y])) for u,z in mapping.items())
    if a!=root and (degree[a]!=degree[b] or any(((u in adj[a])!=(z in adj[b])) for u,z in [(root,root)])):
        return False
    def search():
        if len(mapping)==n:return True
        # smallest candidate set first; parent adjacency provides constraint
        best=None
        for x in range(n):
            if x in mapping:continue
            possible=[y for y in range(n) if good(x,y)]
            if not possible:return False
            if best is None or len(possible)<len(best[1]):best=(x,possible)
            if len(possible)==1:break
        x,possible=best
        for y in possible:
            mapping[x]=y;used.add(y)
            if search():return True
            used.remove(y);del mapping[x]
        return False
    return search()

def fail_point(adj,root):
    col=wl(adj,root); cells=defaultdict(list)
    for i,c in enumerate(col):cells[c].append(i)
    for cell in cells.values():
        for b in cell[1:]:
            if not has_root_automorphism(adj,root,cell[0],b,col):
                return (cell[0],b,sorted(map(len,cells.values())))
    return None

def key(g):
    return (tuple(sorted(d for v,d in g.degree())), tuple(sorted(len(b) for b in nx.biconnected_components(g))))

def run():
    catalog={1:[nx.empty_graph(1)]}
    for n in range(2,10):
        buckets=defaultdict(list)
        for k in range(1,n):
            for base in catalog[n-k]:
                for v in base:
                    h=attach(base,v,k)
                    bucket=buckets[key(h)]
                    if not any(nx.is_isomorphic(h,other) for other in bucket):bucket.append(h)
        catalog[n]=[g for chunk in buckets.values() for g in chunk]
    failures=[]
    for n in range(1,10):
        bad=[]
        for i,g in enumerate(catalog[n]):
            adj=classes(g)
            for root in range(n):
                detail=fail_point(adj,root)
                if detail:bad.append((i,root,detail,sorted(map(list,g.edges()))))
        print('N',n,'CLASSES',len(catalog[n]),'ROOTED',n*len(catalog[n]),'BAD',len(bad),flush=True)
        if n==9:failures=bad
    assert [len(catalog[n]) for n in range(1,10)]==[1,1,2,4,9,23,63,188,596]
    assert len(failures)==1
    print('EXCEPTION',failures[0])
    return True
if __name__=='__main__':run()
