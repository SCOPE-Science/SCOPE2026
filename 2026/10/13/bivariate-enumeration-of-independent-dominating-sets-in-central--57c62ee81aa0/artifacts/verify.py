"""Exact small-graph census for central-graph independent-domination enumerators."""
from collections import Counter
import itertools
import networkx as nx


def central_graph(G):
    H=nx.Graph()
    H.add_nodes_from(('v',v) for v in G.nodes)
    for u,v in G.edges:
        e=('e',min(u,v),max(u,v))
        H.add_edge(('v',u),e)
        H.add_edge(('v',v),e)
    for u,v in itertools.combinations(G.nodes,2):
        if not G.has_edge(u,v):
            H.add_edge(('v',u),('v',v))
    return H


def direct_bivariate(H):
    vs=list(H.nodes)
    adj=[sum(1<<j for j,v in enumerate(vs) if H.has_edge(u,v)) for u in vs]
    original_mask=sum(1<<i for i,v in enumerate(vs) if v[0]=='v')
    poly=Counter()
    for mask in range(1,1<<len(vs)):
        if any((mask>>i)&1 and (mask & adj[i]) for i in range(len(vs))):
            continue
        if any(not (mask>>i)&1 and not (mask&adj[i]) for i in range(len(vs))):
            continue
        poly[(mask.bit_count(), (mask&original_mask).bit_count())]+=1
    return +poly


def predicted_bivariate(G):
    m=G.number_of_edges()
    deg=dict(G.degree())
    P=Counter({(m,0):1})
    for v in G.nodes:
        if all(deg[u]>1 for u in G.neighbors(v)):
            P[(m+1-deg[v],1)]+=1
    for u,v in G.edges:
        P[(m+3-deg[u]-deg[v],2)]+=1
    return +P


def predicted_minimum(G):
    deg=dict(G.degree())
    m=G.number_of_edges()
    D=max(deg[u]+deg[v] for u,v in G.edges)
    e=sum(deg[u]+deg[v]==D for u,v in G.edges)
    v=sum(deg[v]==D-2 and all(deg[u]>1 for u in G.neighbors(v)) for v in G.nodes)
    return m+3-D, e+v+int(D==3)


def spider(lengths):
    T=nx.Graph()
    T.add_node(0)
    nxt=1
    for length in lengths:
        parent=0
        for _ in range(length):
            T.add_edge(parent,nxt)
            parent=nxt
            nxt+=1
    return T


def univariate(P):
    result=Counter()
    for (size,original_count),count in P.items():
        result[size]+=count
    return dict(sorted(result.items()))


checked=0
candidates=0
for G in nx.graph_atlas_g():
    n=G.number_of_nodes()
    if n<3 or n>7 or not nx.is_connected(G) or G.number_of_edges()<2:
        continue
    if any(len(c)==3 for c in nx.enumerate_all_cliques(G)):
        continue
    H=central_graph(G)
    direct=direct_bivariate(H)
    formula=predicted_bivariate(G)
    if direct!=formula:
        raise AssertionError(('bivariate',n,sorted(G.edges()),direct,formula))
    k=min(deg for deg,_ in direct)
    minimum=(k,sum(count for (d,s),count in direct.items() if d==k))
    if minimum!=predicted_minimum(G):
        raise AssertionError(('minimum',n,sorted(G.edges()),minimum,predicted_minimum(G)))
    count_expected=G.number_of_edges()+1+sum(
        all(G.degree(u)>1 for u in G.neighbors(v)) for v in G.nodes
    )
    if sum(direct.values())!=count_expected:
        raise AssertionError(('total',n,count_expected,sum(direct.values())))
    checked+=1
    candidates+=(1<<len(H))-1

for length_vector,expected in [((2,2,1),{3:2,4:1,5:6}),((3,1,1),{3:1,4:4,5:5})]:
    T=spider(length_vector)
    observed=univariate(direct_bivariate(central_graph(T)))
    if observed!=expected:
        raise AssertionError(('spider',length_vector,observed,expected))

print('ALL CHECKS PASSED; '
      f'connected_triangle_free_atlas_graphs={checked}; '
      f'subsets_examined={candidates}; '
      'original_orders=3..7; '
      'bivariate_polynomials=yes; minimum_counts=yes; '
      'spider_profiles=2')
