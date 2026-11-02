"""Exact finite checks for shattering by radius-one graph balls.
Run: python verify_closed_balls.py
Requires networkx for nonisomorphic-tree and graph-atlas enumeration.
The mathematical theorem does not depend on these finite checks.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter
import networkx as nx

# Exact independent state recursion for full adaptive shattering.
def brute_dimensions(G):
    G=nx.convert_node_labels_to_integers(G)
    n=G.number_of_nodes()
    masks=[sum(1<<v for v in list(G.neighbors(u))+[u]) for u in range(n)]
    # A concept is a distinct set, irrespective of how many centers generate it.
    concepts=tuple(sorted(set(masks)))
    m=len(concepts)
    @lru_cache(None)
    def ldim(state):
        if state.bit_count()<2:return 0
        best=0
        for v in range(n):
            y=sum((1<<i) for i,c in enumerate(concepts) if (state>>i&1) and (c>>v&1))
            z=state^y
            if y and z:
                best=max(best,1+min(ldim(y),ldim(z)))
        return best
    vc=0
    for k in range(1,min(n,4)+1):
        if any(len({sum((c>>j&1)<<i for i,j in enumerate(s)) for c in concepts}) == 1<<k
                for s in combinations(range(n),k)):
            vc=k
        else:break
    return vc,ldim((1<<m)-1)

# No Littlestone recursion: local degrees and two closed-neighborhood counts only.
def local_prediction(G):
    G=nx.convert_node_labels_to_integers(G)
    n=G.number_of_nodes()
    closed=[set(G.neighbors(v))|{v} for v in range(n)]
    if n==1:return (0,0)
    if n==2:return (0,0)
    if n==3:return (1,1)
    if n==4 and max(dict(G.degree()).values())<3:return (1,2)
    vc=2 if n>=5 or max(dict(G.degree()).values())>=3 else 1
    if n<=4:return (vc,2)
    # For connected girth>=5, concepts of different centers are distinct.
    if any(len(closed[x])>=4 and
        any(2 <= len(closed[y]-closed[x]) <= n-len(closed[x])-2 for y in range(n))
        for x in range(n)):
        return (vc,3)
    return (vc,2)

def valid(G):
    # exact triangle/C4 exclusion (a girth of infinity is allowed)
    G=nx.convert_node_labels_to_integers(G)
    for z in range(3,5):
        for s in combinations(range(len(G)),z):
            H=G.subgraph(s)
            if z==3 and H.number_of_edges()==3:return False
            if z==4 and nx.is_isomorphic(H,nx.cycle_graph(4)):return False
    return True

if __name__=='__main__':
    c=0
    byn={}
    for G in nx.graph_atlas_g():
        if len(G)==0 or not nx.is_connected(G) or not valid(G):continue
        G=nx.convert_node_labels_to_integers(G)
        a=brute_dimensions(G);b=local_prediction(G)
        if a!=b:raise AssertionError(('atlas',a,b,list(G.edges())))
        byn.setdefault(len(G),Counter())[a]+=1;c+=1
    print('ATLAS_CONNECTED_GIRTH_GE5_PASS',c, 'order_counts=',str(byn),flush=True)
    trees=0
    minimal8=0
    for n in range(2,13):
        counts=Counter()
        for G in nx.nonisomorphic_trees(n):
            a=brute_dimensions(G);b=local_prediction(G)
            if a!=b:raise AssertionError(('tree',n,a,b,list(G.edges())))
            counts[a]+=1;trees+=1
        if n==8:minimal8=counts[(2,3)]
        print('TREES_PASS',n,dict(counts),flush=True)
    assert minimal8==12
    # One eight-vertex tree: two hubs (degree 4 and 3) separated by a degree-2 vertex.
    E=[(1,0),(1,2),(1,3),(1,4),(0,5),(5,6),(5,7)]
    B=nx.Graph();B.add_edges_from(E)
    assert sorted(dict(B.degree()).values())==[1,1,1,1,1,2,3,4]
    assert brute_dimensions(B)==(2,3)
    x=5;y=2
    N=lambda u:set(B.neighbors(u))|{u}
    outside=set(B)-N(x)
    assert len(N(x))==4 and outside=={1,2,3,4} and len(N(y)&outside)==2
    assert len(outside-N(y))==2
    print('EIGHT_VERTEX_SHARP_WITNESS_PASS',sorted(tuple(sorted(e)) for e in B.edges()), 'root',x,'negative_branch_split',y)
    print('ALL_CLOSED_BALL_CHECKS_PASS', 'trees=',trees, 'minimal_order=8', 'minimal_trees=12')
