"""Exhaustive pointed-cactus orbit/refinement comparison through order 9.
Requires networkx >=3.3. No external data files.
"""
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher


def is_cactus(g):
    return all(len(b)==2 or g.subgraph(b).number_of_edges()==len(b)
               for b in nx.biconnected_components(g))


def refinement(g, root):
    colors={v:int(v==root) for v in g}
    while True:
        keys={v:(colors[v],tuple(sorted(colors[u] for u in g[v]))) for v in g}
        palette={k:i for i,k in enumerate(sorted(set(keys.values())))}
        new={v:palette[keys[v]] for v in g}
        if len(set(new.values()))==len(set(colors.values())):
            return new
        colors=new


def rooted_orbit_exact(g, root):
    c=refinement(g,root)
    cells={}
    for v,k in c.items(): cells.setdefault(k,[]).append(v)
    for vs in cells.values():
        for b in vs[1:]:
            a=vs[0]
            # Tags mark root and, separately, the candidate pointed vertex.
            ga=g.copy();gb=g.copy()
            nx.set_node_attributes(ga, {v:(v==root,v==a) for v in g}, 'point')
            nx.set_node_attributes(gb, {v:(v==root,v==b) for v in g}, 'point')
            if not GraphMatcher(ga,gb,node_match=lambda x,y:x['point']==y['point']).is_isomorphic():
                return False, (root,a,b,sorted(len(v) for v in cells.values()))
    return True,None


def augment_one(g, mask):
    k=len(g)
    h=g.copy();h.add_node(k)
    for i in range(k):
        if mask >> i & 1:h.add_edge(i,k)
    return h


def degree_key(g):
    return (tuple(sorted(d for v,d in g.degree())),
            tuple(sorted(len(v) for v in nx.biconnected_components(g))))


def census(nmax=9):
    level=[nx.empty_graph(1)]
    counts=[]
    bad_summary=[]
    for n in range(1,nmax+1):
        bad=[]
        for gi,g in enumerate(level):
            for root in g:
                ok,details=rooted_orbit_exact(g,root)
                if not ok:
                    bad.append((gi,root,details,sorted(g.edges())))
        counts.append(len(level))
        bad_summary.append(len(bad))
        print('N',n,'CLASSES',len(level),'MARKS',n*len(level),'BAD',len(bad),flush=True)
        if n==nmax:
            assert len(bad)==1
            print('EXCEPTION',bad[0])
            break
        buckets={}
        for g in level:
            for mask in range(1,1<<n):
                h=augment_one(g,mask)
                if not is_cactus(h):continue
                key=degree_key(h)
                sub=buckets.setdefault(key,[])
                if not any(nx.is_isomorphic(h,z) for z in sub):
                    sub.append(h)
        level=[g for sub in buckets.values() for g in sub]
    assert counts==[1,1,2,4,9,23,63,188,596]
    assert bad_summary==[0,0,0,0,0,0,0,0,1]
    print('PASS')

if __name__=='__main__':
    census(9)
