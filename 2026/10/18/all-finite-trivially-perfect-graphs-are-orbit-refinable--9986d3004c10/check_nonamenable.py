"""Check orbit-refinement versus graph identification on a small example."""
import networkx as nx
from collections import Counter

def refine(g):
    labels={v:0 for v in g}
    for _ in range(len(g)+2):
        sig={v:(labels[v],tuple(sorted(Counter(labels[x] for x in g[v]).items()))) for v in g}
        names={s:i for i,s in enumerate(sorted(set(sig.values())))}
        nxt={v:names[sig[v]] for v in g}
        if nxt==labels:return nxt
        labels=nxt
    assert False

G=nx.disjoint_union(nx.complete_graph(3),nx.complete_graph(3))
H=nx.cycle_graph(6)
assert nx.is_isomorphic(G,H) is False
both=nx.disjoint_union(G,H)
col=refine(both)
assert len(set(col.values()))==1
assert nx.number_connected_components(G)==2
assert nx.number_connected_components(H)==1
assert len(set(refine(G).values()))==1
print('two_disjoint_triangles_and_six_cycle_indistinguishable=YES')
print('PASS')
