#!/usr/bin/env python3
"""Regenerate the unlabeled order-8 census used by verify.py.
Requires NetworkX 3.6.1 (or a compatible release).
"""
from pathlib import Path
from collections import defaultdict
import hashlib
import networkx as nx

EXPECTED_COUNT=12346
OUT=Path(__file__).with_name('generated_graph8.g6')

bases=[G.copy() for G in nx.graph_atlas_g() if G.number_of_nodes()==7]
assert len(bases)==1044
buckets=defaultdict(list)

def key(G):
    deg=tuple(sorted(dict(G.degree()).values()))
    return (G.number_of_edges(),deg,nx.weisfeiler_lehman_graph_hash(G))

for B in bases:
    B=nx.convert_node_labels_to_integers(B, ordering='sorted')
    for mask in range(1<<7):
        G=B.copy(); G.add_node(7)
        for v in range(7):
            if (mask>>v)&1: G.add_edge(v,7)
        k=key(G)
        if not any(nx.is_isomorphic(G,H) for H in buckets[k]):
            buckets[k].append(G)

graphs=[]
for k in sorted(buckets, key=repr):
    graphs.extend(buckets[k])
assert len(graphs)==EXPECTED_COUNT, len(graphs)
lines=sorted(nx.to_graph6_bytes(G,header=False).decode().strip() for G in graphs)
data=('\n'.join(lines)+'\n').encode('ascii')
OUT.write_bytes(data)
h=hashlib.sha256(data).hexdigest()
print('count',len(graphs))
print('sha256',h)
