#!/usr/bin/env python3
import json,itertools
from pathlib import Path

cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text())
V=cert['obstruction_vertices']
orders=cert['deletion_topological_orders']
assert len(V)==17 and set(orders)==set(V)

# Reconstruct the induced graph directly from the definition of S(3,3).
def adjacent(x,y):
    if x==y: return False
    return x[1:]==y[:2] or y[1:]==x[:2]

adj={x:{y for y in V if adjacent(x,y)} for x in V}
assert sum(map(len,adj.values()))%2==0
edge_count=sum(map(len,adj.values()))//2

# A topological order orients every edge from earlier to later.  It is
# semi-transitive iff no directed path of at least three edges whose endpoints
# are adjacent has a non-clique vertex set.
def check_order(vertices,order):
    assert set(order)==set(vertices) and len(order)==len(vertices)
    pos={v:i for i,v in enumerate(order)}
    out={v:[u for u in adj[v] if u in pos and pos[v]<pos[u]] for v in vertices}
    for x in order:
        for y in out[x]:
            stack=[(x,(x,))]
            while stack:
                v,path=stack.pop()
                for u in out[v]:
                    if pos[u]>pos[y]:
                        continue
                    if u==y:
                        if len(path)>=3:
                            p=path+(y,)
                            if any(b not in adj[a] for a,b in itertools.combinations(p,2)):
                                raise AssertionError(('shortcut',p,order))
                    elif pos[u]<pos[y]:
                        stack.append((u,path+(u,)))
    return True

for deleted in V:
    vertices=[x for x in V if x!=deleted]
    assert check_order(vertices,orders[deleted])

# Every proper induced subgraph omits at least one vertex v and is an induced
# subgraph of the certified word-representable graph S-v.  Word-representability
# is hereditary under induced subgraphs.
print(f'VERIFY_OK vertices=17 edges={edge_count} deletions=17 semi_transitive_orders=17 proper_subgraphs_covered=1')
